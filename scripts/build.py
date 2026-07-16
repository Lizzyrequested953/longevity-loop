#!/usr/bin/env python3
"""Render README.md + docs/ROADMAP.md from data/*.yml — the single source of truth.

Never hand-edit the generated files; edit data/*.yml and run `make build`
(CI drift-gates them). This is the same spec-as-data discipline as FM-os.
"""
from __future__ import annotations

import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
README = ROOT / "README.md"
ROADMAP = ROOT / "docs" / "ROADMAP.md"
BADGE = "https://img.shields.io/github"


def load(name: str):
    p = DATA / f"{name}.yml"
    return (yaml.safe_load(p.read_text()) if p.exists() else []) or []


def esc(t: object) -> str:
    return " ".join(str("" if t is None else t).split())


def render_readme() -> str:
    meta, loop, road = load("meta"), load("loop"), load("roadmap")
    people, startups, stack, eco = load("people"), load("startups"), load("stack"), load("ecosystem")
    turns, frontier, reflections = load("turns"), load("frontier"), load("reflections")
    slug = f"{meta['repo_owner']}/{meta['repo_name']}"
    L: list[str] = []

    L += [
        f"# {meta['title']}", "",
        "<div align=\"center\">", "",
        f"[![CI]({BADGE}/actions/workflow/status/{slug}/ci.yml?style=flat-square&label=loop%20check)](https://github.com/{slug}/actions)",
        f"[![Last Updated]({BADGE}/last-commit/{slug}?style=flat-square&label=last%20turn)](https://github.com/{slug}/commits/main)",
        f"[![License]({BADGE}/license/{slug}?style=flat-square)](LICENSE)", "",
        esc(meta["sibling_banner"]), "",
        esc(meta["tagline"]), "",
        esc(meta["north_star"]), "",
        "</div>", "", "---", "",
        f"> {esc(meta['disclaimer'])}", "", "---", "",
    ]

    # The loop
    L += ['<h2 id="the-loop">♻️ The Loop (one turn of the flywheel)</h2>', "",
          "Each turn is falsifiable and ends in a shared, verifiable artifact. No evidence ⇒ no claim.", "",
          "| # | Stage | What happens |", "|--:|---|---|"]
    for s in loop["stages"]:
        L.append(f"| {s['n']} | **{esc(s['name'])}** | {esc(s['do'])} |")
    L += ["", "> ⑦ COMPOUND feeds back into ① — each turn adds data, a tool, or a connection, so the next question is bigger.", "", "---", ""]

    # Turns ledger (build-in-public progress)
    icon = {"scaffolded": "🧩", "in-progress": "🔄", "done": "✅"}
    L += ['<h2 id="turns">📓 Turns Log</h2>', "",
          "Every turn of the loop, logged honestly. `done` requires a PROOF (result incl. the null + a reproduce command).", "",
          "| Turn | Question | Stage | Status |", "|---|---|---|:--|"]
    for t in turns:
        L.append(f"| [{esc(t['id'])}]({t['path']}) | {esc(t['question'])} | {esc(t['stage'])} | {icon.get(t['status'],'')} {esc(t['status'])} |")
    L += ["", "---", ""]

    # Frontier Radar (individual recent works) + congregational graph
    if frontier:
        L += ['<h2 id="frontier">🛰️ Frontier Radar</h2>', "",
              "The frontier groundbreakers' most recent deep works — verified, with a link + a real "
              "quote. Refreshed weekly by [`scripts/track.py`](scripts/track.py) (arXiv + GitHub).", ""]
        for f in frontier:
            link = f"[{esc(f['recent_work'])}]({f['link']})" if f.get("link") and f["link"] != "-" else esc(f.get("recent_work", ""))
            L.append(f"- **{esc(f['name'])}** — {link} _({esc(f.get('year',''))})_")
            L.append(f"  {esc(f.get('summary',''))}")
            if f.get("quote") and f["quote"] != "-":
                L.append(f"  > \"{esc(f['quote'])}\"")
            if f.get("future_direction") and f["future_direction"] != "-":
                L.append(f"  → _Future:_ {esc(f['future_direction'])}")
        L += ["",
              "**🕸️ Congregational view:** the field as a spatiotemporal knowledge graph "
              "(modeled after [getzep/graphiti](https://github.com/getzep/graphiti)) — "
              "**[open the field graph →](https://wjlgatech.github.io/longevity-loop/graph.html)**.", ""]
        if reflections:
            L += ["**Reflections — what else could be important?** _(synthesis, not claims)_", ""]
            L += [f"- {esc(r)}" for r in reflections]
        L += ["", "---", ""]

    # Roadmap summary
    L += ['<h2 id="90-day-roadmap">🗺️ 90-Day Roadmap</h2>', "",
          "Three tracks every week — full weekly plan in **[docs/ROADMAP.md](docs/ROADMAP.md)**:", ""]
    L += [f"- {esc(t)}" for t in road["tracks"]]
    L += [""]
    for ph in road["phases"]:
        L += [f"### {esc(ph['title'])} · _{esc(ph['days'])}_", f"{esc(ph['theme'])}", "",
              f"**{esc(ph['milestone'])}**", ""]
    L += ["**Signal ladder** (each rung recruits the next):", ""]
    L += [f"{i}. {esc(r)}" for i, r in enumerate(road["signal_ladder"], 1)]
    L += ["", "---", ""]

    # Landscape
    L += ['<h2 id="people">🧠 Researchers</h2>', "",
          "🤖 = AI-forward · 💬 = active in the open community (good first contacts).", ""]
    for p in people:
        marks = ("🤖" if p.get("ai_forward") else "") + ("💬" if p.get("approachable") else "")
        L.append(f"- **[{esc(p['name'])}]({p['url']})** {marks} — {esc(p['org'])}: {esc(p['known_for'])}")
    L += ["", "---", "", '<h2 id="startups">🏢 Startups & Labs</h2>', "",
          "🤖 = AI-native platform.", ""]
    for s in startups:
        L.append(f"- **[{esc(s['name'])}]({s['url']})** {'🤖' if s.get('ai_native') else ''} — {esc(s['focus'])} _({esc(s.get('stage',''))})_")
    L += ["", "---", "", '<h2 id="stack">🛠️ The Buildable Stack (open, code-only)</h2>', ""]
    for kind in ("model", "tool", "clock", "dataset", "benchmark"):
        rows = [x for x in stack if x.get("kind") == kind]
        if not rows:
            continue
        L.append(f"### {kind.title()}s")
        L += [f"- **[{esc(x['name'])}]({x['url']})** — {esc(x['note'])}" for x in rows]
        L.append("")
    L += ["---", "", '<h2 id="ecosystem">🤝 Funding & Community</h2>', "",
          "✅ = realistically open to a solo/independent builder.", ""]
    for e in eco:
        L.append(f"- **[{esc(e['name'])}]({e['url']})** {'✅' if e.get('open_to_independents') else '🔒'} _{esc(e['type'])}_ — {esc(e['note'])}")
    L += ["", "---", "",
          '<h2 id="build-in-public">📣 Build in public</h2>', "",
          "This repo IS the artifact: every turn commits data, a result, or a connection. Follow the commits, "
          "open an issue with a paper/dataset/collaborator, or PR an entry to `data/*.yml`.", "",
          "<sub>Generated from <code>data/*.yml</code> by <code>scripts/build.py</code> — do not edit by hand. "
          "A sibling of <a href=\"https://github.com/wjlgatech/FM-os\">FM-os</a>.</sub>", ""]
    return "\n".join(L)


def render_roadmap() -> str:
    road = load("roadmap")
    L = ["# longevity-loop — 90-Day Roadmap", "",
         "_Generated from `data/roadmap.yml`. Three tracks every week: 🧠 Knowledge · 🛠️ Tooling · 🤝 Connections._", ""]
    for t in road["tracks"]:
        L.append(f"- {esc(t)}")
    L.append("")
    for ph in road["phases"]:
        L += [f"## {esc(ph['title'])} · {esc(ph['days'])}", "", f"_{esc(ph['theme'])}_", ""]
        for w in ph["weeks"]:
            L += [f"### Week {esc(w['week'])}",
                  f"- 🧠 **Knowledge** — {esc(w['knowledge'])}",
                  f"- 🛠️ **Tooling** — {esc(w['tooling'])}",
                  f"- 🤝 **Connections** — {esc(w['connections'])}", ""]
        L += [f"> ✅ **{esc(ph['milestone'])}**", "", "---", ""]
    return "\n".join(L)


def main() -> int:
    outputs = {README: render_readme(), ROADMAP: render_roadmap()}
    if "--check" in sys.argv:
        stale = [p.name for p, txt in outputs.items() if (p.read_text() if p.exists() else "") != txt]
        if stale:
            print(f"Out of date: {', '.join(stale)}. Run `make build`.", file=sys.stderr)
            return 1
        print("README.md + docs/ROADMAP.md are up to date.")
        return 0
    for p, txt in outputs.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(txt)
    print(f"Wrote {README.name} + docs/{ROADMAP.name}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
