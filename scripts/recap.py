#!/usr/bin/env python3
"""Daily recap — teach the day's longevity-loop progress as a viral-quality explainer.

Signal-gated by design (the cadence decision): it only writes an article when the
day actually moved (new commits, a frontier-synthesis change, or a turn/execution
update). Quiet day ⇒ it exits 0 without publishing — no filler, no wasted tokens.

When there IS signal it asks Claude (Opus 4.8, adaptive thinking, effort=high) to
write to four rubrics — (1) one simple mental model a 15-year-old gets, with a
self-contained animated SVG; (2) grounded in the day's real evidence; (3) sharp
reasoning + industrial insight + a futuristic bird's-eye; (4) genuine humor and
taste — then renders a self-contained page under site/writings/ plus an RSS item.
The portfolio's Writing section ingests that RSS feed (category = "longevity-loop").

  recap.py [--date YYYY-MM-DD] [--dry-run] [--since <git-ref-or-ISO>]
    --dry-run   render a deterministic placeholder (no API call, no tokens) — proves
                the pipeline offline and in CI; the real cron omits it.

Auth: ANTHROPIC_API_KEY (GitHub Actions secret). Deps: anthropic, pyyaml.
"""
from __future__ import annotations

import argparse
import html
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
WRITINGS = SITE / "writings"
FEED = SITE / "feed.xml"
SITE_BASE = "https://wjlgatech.github.io/longevity-loop"
CATEGORY = "longevity-loop"  # becomes the portfolio Article.category (its "tag")
MODEL = "claude-opus-4-8"    # per claude-api: default unless the user names another


# ── 1. gather the day's real signal ─────────────────────────────────────────
def _git(*args: str) -> str:
    try:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                              text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def gather_signal(since: str, date: str) -> dict:
    """What moved today: commit subjects + which tracked data files changed."""
    rng = f"{since}..HEAD" if since else "HEAD~20..HEAD"
    commits = [c for c in _git("log", rng, "--no-merges", "--pretty=%s").splitlines()
               if c and not c.startswith(("chore(release)", "Merge"))]
    changed = _git("diff", "--name-only", rng).splitlines() if since else []
    notable = [f for f in changed
               if f.startswith(("data/", "turns/", "scripts/")) and not f.endswith(".pyc")]
    synth = ""
    sp = ROOT / "data" / "_synthesis.md"
    if sp.exists() and ("data/_synthesis.md" in changed or not since):
        synth = sp.read_text()[:4000]
    return {"date": date, "commits": commits, "changed": notable, "synthesis": synth,
            "has_signal": bool(commits or notable or synth)}


# ── 2. a reliable, self-contained animated SVG (the "one mental model" visual) ──
def flywheel_svg() -> str:
    """The compounding loop as a rotating flywheel — deterministic, no JS, no deps."""
    stages = ["QUESTION", "DATA", "MODEL", "VERIFY", "WRITE-UP", "SHARE", "COMPOUND"]
    spokes = []
    for i, s in enumerate(stages):
        ang = i * (360 / len(stages))
        spokes.append(
            f'<g transform="rotate({ang} 150 150)">'
            f'<line x1="150" y1="150" x2="150" y2="40" stroke="#8a6f4e" stroke-width="2"/>'
            f'<circle cx="150" cy="40" r="6" fill="#c96f3f"/>'
            f'<text x="150" y="26" text-anchor="middle" font-size="11" fill="#3a3226" '
            f'transform="rotate({-ang} 150 40)">{s}</text></g>')
    return (
        '<svg viewBox="0 0 300 300" role="img" aria-label="The compounding loop flywheel" '
        'style="max-width:340px;width:100%;height:auto;display:block;margin:1.5rem auto">'
        '<g style="transform-origin:150px 150px;animation:llspin 24s linear infinite">'
        f'{"".join(spokes)}'
        '<circle cx="150" cy="150" r="26" fill="#3a3226"/>'
        '<text x="150" y="155" text-anchor="middle" font-size="13" fill="#f4f1ea">loop</text>'
        '</g><style>@keyframes llspin{to{transform:rotate(360deg)}}</style></svg>')


# ── 3. the model call (Opus 4.8, adaptive thinking, effort=high, streamed) ──
SYSTEM = """You write the daily build-in-public recap for `longevity-loop`, a solo \
builder's public AI x longevity research loop. Audience: the builder and a curious \
public. Follow FOUR rubrics, all of them, every time:
1. ONE simple mental model a sharp 15-year-old fully gets — a single vivid analogy \
   that carries the whole piece. (A rotating flywheel SVG is inserted for you; open \
   by grounding the reader in it.)
2. Grounded in the REAL evidence provided below. No invented results, papers, or \
   numbers. If today was mostly scaffolding/tooling, say so plainly — honesty is the \
   brand ("no evidence => no claim").
3. Sharp reasoning + a real industrial insight + a short futuristic bird's-eye of \
   where this is heading.
4. Genuine, dry humor and good taste. Never cringe, never hype, never emoji-spam.
Length: 500-800 words. Return body as clean semantic HTML (<p>, <h3>, <ul>, <blockquote>, \
<strong>) — NO <html>/<head>/<style>/<script>, NO images (the SVG is added for you)."""

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "title": {"type": "string"},
        "dek": {"type": "string"},          # one-line standfirst
        "summary": {"type": "string"},      # <=200 chars for the RSS description
        "body_html": {"type": "string"},
    },
    "required": ["title", "dek", "summary", "body_html"],
}


def generate_article(signal: dict) -> dict:
    import anthropic  # imported lazily so --dry-run needs no dependency

    evidence = json.dumps({k: signal[k] for k in ("date", "commits", "changed", "synthesis")},
                          ensure_ascii=False, indent=2)
    client = anthropic.Anthropic()
    with client.messages.stream(
        model=MODEL,
        max_tokens=16000,
        thinking={"type": "adaptive"},
        output_config={"effort": "high", "format": {"type": "json_schema", "schema": SCHEMA}},
        system=SYSTEM,
        messages=[{"role": "user", "content":
                   f"Today is {signal['date']}. The day's real evidence (git + synthesis):\n"
                   f"```json\n{evidence}\n```\nWrite today's recap."}],
    ) as stream:
        msg = stream.get_final_message()
    if msg.stop_reason == "refusal":  # per claude-api: check before reading content
        raise RuntimeError(f"model refused: {getattr(msg, 'stop_details', None)}")
    text = next(b.text for b in msg.content if b.type == "text")
    return json.loads(text)


def placeholder_article(signal: dict) -> dict:
    """Deterministic offline article so the pipeline is testable without the API."""
    bullets = "".join(f"<li>{html.escape(c)}</li>" for c in signal["commits"][:8]) or \
        "<li>Housekeeping only — no headline change.</li>"
    return {
        "title": f"Daily recap — {signal['date']} (placeholder)",
        "dek": "Generated with --dry-run: the pipeline works; the prose is a stub.",
        "summary": f"{len(signal['commits'])} change(s) on {signal['date']} — placeholder recap.",
        "body_html": (
            "<p>The loop is a flywheel: every honest turn adds a little spin, and spin "
            "compounds. Here's what nudged it today.</p>"
            f"<h3>What moved</h3><ul>{bullets}</ul>"
            "<p><em>(This is a dry-run stub. With ANTHROPIC_API_KEY set, the real recap "
            "teaches the day through one mental model, grounded in this same evidence.)</em></p>"),
    }


# ── 4. render a self-contained page + RSS item ──────────────────────────────
PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — longevity-loop</title>
<meta name="description" content="{summary}">
<style>
:root{{color-scheme:light}}
body{{max-width:44rem;margin:0 auto;padding:2rem 1.2rem;background:#f4f1ea;color:#2c2620;
 font:17px/1.65 Georgia,"Iowan Old Style",serif}}
a{{color:#c96f3f}} h1{{font-size:2rem;line-height:1.15;margin:.2em 0}}
.dek{{font-style:italic;color:#6b5d49;font-size:1.15rem;margin:.4em 0 1.2em}}
.meta{{font:13px/1.4 ui-sans-serif,system-ui;color:#8a7d68;text-transform:uppercase;letter-spacing:.06em}}
h3{{font-size:1.15rem;margin-top:1.6em}} blockquote{{border-left:3px solid #c96f3f;margin:1em 0;padding-left:1em;color:#54493a}}
footer{{margin-top:3rem;border-top:1px solid #d8d0c0;padding-top:1rem;font:13px/1.5 ui-sans-serif,system-ui;color:#8a7d68}}
</style></head><body>
<p class="meta">longevity-loop · daily recap · {date}</p>
<h1>{title}</h1><p class="dek">{dek}</p>
{svg}
{body}
<footer>Part of <a href="{base}/">longevity-loop</a> — an AI-native compounding loop for
aging science. Generated the day it happened; grounded in that day's real commits.
Not medical advice; computational results on public data only.</footer>
</body></html>"""


def render_page(article: dict, date: str) -> pathlib.Path:
    WRITINGS.mkdir(parents=True, exist_ok=True)
    out = WRITINGS / f"{date}.html"
    out.write_text(PAGE.format(
        title=html.escape(article["title"]), dek=html.escape(article["dek"]),
        summary=html.escape(article["summary"]), date=date, svg=flywheel_svg(),
        body=article["body_html"], base=SITE_BASE))
    return out


RSS_ITEM = """  <item>
    <title>{title}</title>
    <link>{url}</link>
    <guid isPermaLink="true">{url}</guid>
    <category>{cat}</category>
    <pubDate>{date}</pubDate>
    <description>{summary}</description>
  </item>"""


def update_feed(article: dict, date: str, url: str) -> None:
    item = RSS_ITEM.format(title=html.escape(article["title"]), url=url, cat=CATEGORY,
                           date=date, summary=html.escape(article["summary"]))
    existing = ""
    if FEED.exists():
        m = re.search(r"(<item>.*</item>)", FEED.read_text(), re.S)
        existing = m.group(1) if m else ""
    # newest first; drop any prior item for the same URL (idempotent re-runs)
    existing = re.sub(rf"\s*<item>(?:(?!</item>).)*?{re.escape(url)}.*?</item>", "", existing, flags=re.S)
    FEED.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>\n'
        "  <title>longevity-loop — daily recaps</title>\n"
        f"  <link>{SITE_BASE}/writings/</link>\n"
        "  <description>Build-in-public daily recaps for an AI x longevity research loop.</description>\n"
        f"{item}\n{existing}\n</channel></rss>\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None, help="YYYY-MM-DD (pass in; scripts can't read the clock)")
    ap.add_argument("--since", default="", help="git ref or ISO date bounding 'today'")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    date = args.date or _git("log", "-1", "--pretty=%cs") or "undated"

    signal = gather_signal(args.since, date)
    if not signal["has_signal"]:
        print(f"No meaningful signal for {date} — skipping (quiet day, no filler).")
        return 0

    article = placeholder_article(signal) if args.dry_run else generate_article(signal)
    page = render_page(article, date)
    url = f"{SITE_BASE}/writings/{date}.html"
    update_feed(article, date, url)
    print(f"Wrote {page.relative_to(ROOT)} + updated {FEED.relative_to(ROOT)}")
    print(f"  → {url}  (category: {CATEGORY})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
