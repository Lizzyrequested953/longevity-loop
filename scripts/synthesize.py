#!/usr/bin/env python3
"""Frontier → roadmap synthesizer — turn live signal into human-gated proposals.

The step track.py was missing: it doesn't just dump signal, it DRAFTS what the
signal means for us. For each tracked researcher it finds the most recent
publication (Europe PMC — covers journals AND bioRxiv, where aging work lives,
unlike arXiv-only track.py), diffs it against our curated data/frontier.yml, and
emits two review drafts into data/_synthesis.md:

  A) proposed frontier updates — only where a NEWER work than the curated one exists
  B) roadmap signal — fresh topics mapped to roadmap phases, each with its evidence

Discipline (same as the rest of the repo): NO EVIDENCE ⇒ NO CLAIM. It never
writes a quote it didn't fetch, never invents a link, records "none found" when a
search is empty, and NEVER edits frontier.yml / roadmap.yml directly — a human
reviews data/_synthesis.md and promotes what's real (the weekly PR carries it).

  synthesize.py            # fetch + diff + write data/_synthesis.md
Auth: none needed (Europe PMC is open). Degrades gracefully offline.
"""
from __future__ import annotations

import json
import pathlib
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = DATA / "_synthesis.md"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
# Aging terms constrain the author search so a common surname can't match the wrong person.
AGING = "(aging OR ageing OR longevity OR senescence OR epigenetic OR geroscience)"
AGING_KEYS = ("aging", "ageing", "longevity", "senescen", "epigenetic", "geroscience", "lifespan")

# topic → substrings that imply it (mirrors build_graph.py so proposals speak the graph's language)
TOPICS = {
    "aging clocks": ["clock", "phenoage", "grimage", "dunedin", "epigenetic", "biological age", "methylation"],
    "reprogramming": ["reprogram", "rejuven", "yamanaka"],
    "AI / foundation models": ["foundation model", "llm", "deep learning", "machine learning", "generative", "transformer"],
    "single-cell / multi-omics": ["single-cell", "single cell", "multi-omic", "transcriptom", "proteom"],
    "interventions": ["rapamycin", "metformin", "senolytic", "calorie", "intervention", "trial"],
    "hallmarks / mechanisms": ["hallmark", "splicing", "damage", "mitochond", "autophagy", "inflamm"],
}


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


_PARTICLES = {"de", "van", "von", "der", "den", "la", "le", "di", "da", "el"}


def surname(name: str) -> str:
    return strip_accents(name.split()[-1])


def author_token(name: str) -> str:
    """Europe PMC 'Lastname Initials' form, e.g. 'Levine M', 'Magalhaes JP'.
    Adding initials is what separates the right Levine from an epidemiology Levine —
    surname-only (like track.py's arXiv search) is far too loose to trust."""
    parts = name.split()
    initials = "".join(p[0] for p in parts[:-1] if p.lower() not in _PARTICLES)
    return f"{surname(name)} {strip_accents(initials)}".strip()


def load(name: str):
    p = DATA / f"{name}.yml"
    return (yaml.safe_load(p.read_text()) if p.exists() else []) or []


def _get(url: str, timeout: int = 15) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "longevity-loop-synthesize"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def latest_publication(name: str) -> dict:
    """Most recent aging-relevant publication for a surname, via Europe PMC.

    Returns {} on 'nothing found' and {"error": ...} on a network/API failure —
    both are reported honestly; neither is ever turned into a fake entry.
    """
    q = f'AUTH:"{author_token(name)}" AND {AGING}'
    params = urllib.parse.urlencode(
        {"query": q, "format": "json", "resultType": "core",
         "pageSize": 1, "sort": "P_PDATE_D desc"}
    )
    try:
        raw = _get(f"{EPMC}?{params}")
        time.sleep(1)  # be polite to the open API
    except urllib.error.HTTPError as exc:
        return {"error": f"europepmc http {exc.code}"}
    except Exception as exc:  # noqa: BLE001
        return {"error": f"europepmc {type(exc).__name__}"}
    try:
        results = json.loads(raw).get("resultList", {}).get("result", [])
    except json.JSONDecodeError:
        return {"error": "europepmc bad json"}
    if not results:
        return {}
    r = results[0]
    doi = r.get("doi", "")
    link = f"https://doi.org/{doi}" if doi else (
        f"https://europepmc.org/article/{r.get('source','')}/{r.get('id','')}" if r.get("id") else "")
    title = " ".join(str(r.get("title", "")).split()).rstrip(".")
    return {
        "title": title,
        "year": str(r.get("pubYear", "")),
        "date": r.get("firstPublicationDate", ""),
        "link": link,
        "journal": r.get("journalTitle", "") or r.get("source", ""),
        "abstract": " ".join(re.sub(r"<[^>]+>", " ", str(r.get("abstractText", ""))).split()),
        # Aging term in the TITLE ⇒ strong relevance; only in the abstract ⇒ weak
        # (a common surname matching an off-topic paper usually fails this).
        "title_relevant": any(k in title.lower() for k in AGING_KEYS),
    }


def topics_of(text: str) -> list[str]:
    t = text.lower()
    return [topic for topic, keys in TOPICS.items() if any(k in t for k in keys)]


def is_newer(found: dict, curated: dict) -> bool:
    """A found work is worth proposing if we have no curated entry, or it looks
    strictly newer, or its title differs from the one we already list."""
    if not curated:
        return True
    fy, cy = found.get("year", ""), str(curated.get("year", ""))
    if fy and cy and fy > cy:
        return True
    cur_title = str(curated.get("recent_work", "")).lower()[:40]
    return bool(cur_title) and cur_title not in found.get("title", "").lower()


def main() -> int:
    people = load("people")
    curated = {e["name"]: e for e in load("frontier")}

    updates, none_found, errors, fresh_topics = [], [], [], {}
    print("Synthesizing frontier signal (Europe PMC)…")
    for p in people:
        name = p["name"]
        found = latest_publication(name)
        if "error" in found:
            errors.append((name, found["error"]))
            print(f"  ! {name}: {found['error']}")
            continue
        if not found:
            none_found.append(name)
            print(f"  · {name}: none found")
            continue
        if is_newer(found, curated.get(name)):
            updates.append((name, found))
            for topic in topics_of(f"{found['title']} {found['abstract']}"):
                fresh_topics.setdefault(topic, []).append((name, found))
            print(f"  ✓ {name}: NEWER → {found['title'][:60]}")
        else:
            print(f"  = {name}: curated entry still current")

    L: list[str] = [
        "# Frontier → roadmap synthesis (DRAFT — human review required)",
        "",
        "> GENERATED by `scripts/synthesize.py`. NO EVIDENCE ⇒ NO CLAIM: every item below is a",
        "> *proposal* backed by a real Europe PMC record. Nothing here is a claim until a human",
        "> promotes it into `data/frontier.yml` / `data/roadmap.yml`. Verify each quote against the",
        "> linked source — abstracts are shown as quote-source, never as a pre-written quote.",
        "",
        "## A) Proposed frontier updates",
        "",
    ]
    if updates:
        L.append("A newer aging-relevant publication than our curated entry was found for the "
                 "researchers below. **Strong** = an aging term is in the title; **weak** = only "
                 "in the abstract (likely a same-surname false match — check identity first).")
        L.append("")
        updates.sort(key=lambda nf: not nf[1].get("title_relevant"))  # strong matches first
        for name, f in updates:
            cur = curated.get(name)
            strength = "strong" if f.get("title_relevant") else "weak"
            L += [f"### {name}  · _relevance: {strength}_",
                  f"- **Found:** [{f['title']}]({f['link']}) — _{f['journal']}, {f['year']}_ (pub {f['date']})",
                  f"- **⚠ Confirm identity:** matched on author `{author_token(name)}` — open the link and "
                  "check it is the same person before promoting (initials-match ≠ proof).",
                  f"- **We currently list:** {cur.get('recent_work','(none)') if cur else '(not in frontier.yml yet)'}"
                  + (f" _({cur.get('year')})_" if cur else ""),
                  "- **Verbatim quote:** pick one sentence from the abstract below and paste into `quote:` "
                  "(do NOT paraphrase):",
                  f"  > {f['abstract'][:600] or '(no abstract returned — open the link to source a quote)'}",
                  ""]
    else:
        L += ["_No newer works than the curated frontier were found this run._", ""]

    L += ["## B) Roadmap signal", ""]
    if fresh_topics:
        L.append("Fresh works cluster on these topics — check each against `data/roadmap.yml` and "
                 "decide if a phase/week should shift (attach the evidence link if you do):")
        L.append("")
        for topic, items in sorted(fresh_topics.items(), key=lambda kv: -len(kv[1])):
            names = ", ".join(sorted({n for n, _ in items}))
            L.append(f"- **{topic}** ({len(items)} fresh work(s): {names})")
            for name, f in items:
                L.append(f"  - evidence: [{f['title'][:70]}]({f['link']}) — {name}, {f['year']}")
        L.append("")
    else:
        L += ["_No new topic signal this run._", ""]

    L += ["## Coverage (honest ledger)", "",
          f"- Researchers checked: **{len(people)}**",
          f"- Newer-work proposals: **{len(updates)}**",
          f"- None found (searched, empty): **{len(none_found)}**"
          + (f" — {', '.join(none_found)}" if none_found else ""),
          f"- Errors (not measured this run): **{len(errors)}**"
          + (f" — {', '.join(f'{n} ({e})' for n, e in errors)}" if errors else ""),
          ""]

    OUT.write_text("\n".join(L))
    print(f"\nWrote {OUT.relative_to(ROOT)} — {len(updates)} proposal(s), "
          f"{len(none_found)} none-found, {len(errors)} error(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
