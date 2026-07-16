# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

`longevity-loop` is a solo builder's public, self-improving loop for AI × longevity. It is **not an app** — it is a data-driven artifact: `data/*.yml` is the single source of truth, and every human-readable output (README, roadmap, live dashboard, field graph) is *generated* from it. The mission is to climb the code-only [Biomarkers of Aging Challenge](https://www.longevityprize.com/prize/biomarker) leaderboard, built in public, one falsifiable "turn" at a time. It is a sibling of [FM-os](https://github.com/wjlgatech/FM-os) and applies the same spec-as-data discipline.

Guiding rule that shows up throughout the code and content: **no evidence ⇒ no claim.** Computational results on public data are kept strictly separate from any wet-lab/therapeutic claim. Never fabricate a paper, a score, or a dataset — scripts are written to record "none found" rather than invent (see `track.py`, `baseline.py`).

## Commands

```bash
make build       # regenerate README.md + docs/ROADMAP.md from data/*.yml
make validate    # schema-gate data/*.yml (required fields, valid+unique URLs)
make audit       # self-audit vs the AI-native loop principles, gate at 80/100
make eval        # roadmap-execution checkbox + before→after eval; fails on a fake ✅
make check       # CI finish line: validate + audit + eval + build --check (drift gate)
make site        # compile site/data.json + site/graph.json for the dashboard
make track       # refresh live frontier signal into data/_frontier.yml (needs network)
make synthesize  # draft frontier+roadmap PROPOSALS into data/_synthesis.md (Europe PMC)
make recap-dry   # preview the daily recap offline (no API key, no tokens)
```

Run a single script directly, e.g. `python3 scripts/audit.py --gate 80` or `python3 scripts/build.py --check`. There is no unit-test suite; `make check` is the correctness gate. Python 3.12 in CI; the core dependency is `pyyaml`. Two scripts add more, but only in their own (non-`check`) workflows: `synthesize.py` is stdlib-only (Europe PMC over `urllib`); `recap.py` needs `anthropic` + an `ANTHROPIC_API_KEY` (used only by the `recap` cron).

## The generation pipeline (most important thing to understand)

`data/*.yml` → scripts → generated outputs. **Never hand-edit generated files** — edit the YAML and rerun the generator. CI drift-gates this: `build.py --check` fails if `README.md` or `docs/ROADMAP.md` don't match what the current data would produce.

- `scripts/build.py` — renders `README.md` + `docs/ROADMAP.md`. With `--check`, compares instead of writing (the drift gate).
- `scripts/validate.py` — schema gate. `REQUIRED` dict defines required fields per file; also enforces `http(s)` URLs and no duplicate URLs.
- `scripts/audit.py` — scores `data/loop.yml`'s `principles` from real repo evidence (a file must exist, or a `grep` regex must match). No evidence ⇒ the principle fails. `--gate N` exits non-zero below N so CI blocks a regression in *how* the project works.
- `scripts/build_site.py` — compiles `data/*.yml` → `site/data.json` (dashboard consumes it, so the live site can't drift from the README).
- `scripts/build_graph.py` — builds `site/graph.json`, a bi-temporal knowledge graph (nodes = people/orgs/topics/works; edges carry an optional `since` year). Topic assignment is keyword-matching in the `TOPICS` dict against each entry's `known_for`/`focus`.
- `scripts/track.py` — refreshes live arXiv + GitHub signal into the GENERATED `data/_frontier.yml`. arXiv rate-limits hard (429), so it degrades gracefully and never blocks. Note: `frontier.yml` (curated, hand-authored, verified quotes) and `_frontier.yml` (generated, live) are different files.
- `scripts/eval.py` — reads `data/executions.yml` and enforces the honest-eval rule: an execution marked `done: true` must carry a real `eval.before` AND `eval.after` (never "pending"/empty). `--gate` exits non-zero on a violation, so CI blocks a fake ✅. Part of `make check`.
- `scripts/synthesize.py` — the frontier→roadmap synthesizer. For each tracked researcher it finds the most recent aging-relevant publication via **Europe PMC** (covers journals + bioRxiv, unlike arXiv-only `track.py`), diffs it against curated `data/frontier.yml`, and writes DRAFT proposals (frontier updates + roadmap-delta signal) to the GENERATED `data/_synthesis.md`. Human-gated by design: it never edits `frontier.yml`/`roadmap.yml`, flags every match `⚠ Confirm identity` (surname+initials ≠ proof), and records "none found" rather than invent. A person promotes what's real.
- `scripts/recap.py` — the daily build-in-public recap generator. Signal-gated: skips days with no new commits / synthesis change (no filler). On signal it asks Claude (Opus 4.8, adaptive thinking, effort=high) to write a four-rubric explainer, then renders a self-contained page under `site/writings/` (with a templated animated SVG) plus an RSS item in `site/feed.xml` (`<category>` is cosmetic — the portfolio tags articles by the *source label*, so register the feed with label `longevity-loop`). `--dry-run` renders a deterministic offline placeholder (no API, no tokens) so the pipeline is testable in CI.

## Data files (`data/`)

Content lives here. Files consumed by `build.py`/`build_site.py`: `meta`, `loop`, `roadmap`, `turns`, `frontier`, `reflections`, `people`, `startups`, `stack`, `ecosystem`. When adding an entry, match the existing schema in that file and the required fields in `validate.py`'s `REQUIRED` map — then run `make check`.

- `loop.yml` is dual-purpose: its `stages` render the README's loop table, and its `principles` (with `evidence` file/grep checks) are what `audit.py` scores. Adding a principle means adding real, checkable evidence in the repo.
- `stack.yml` entries need a `kind` (`model`/`tool`/`clock`/`dataset`/`benchmark`) — `build.py` groups the stack section by kind.
- `executions.yml` — the roadmap-execution ledger `eval.py` gates (checkbox + before→after per execution). Not consumed by `build.py` (doesn't render into README).
- Underscore-prefixed files are GENERATED review artifacts, tracked but not hand-edited: `_frontier.yml` (from `track.py`) and `_synthesis.md` (from `synthesize.py`). Neither is read by `build.py`/`validate.py`, so they don't affect `make check`.

## Turns (`turns/turn-NN-*/`)

Each turn is one falsifiable pass of the loop (QUESTION → DATA → MODEL → VERIFY → WRITE-UP → SHARE → COMPOUND). Structure: `README.md` (the falsifiable question + metric + the null you'd accept), a runnable Python entry point (e.g. `baseline.py`, `finetune.py`), `requirements.txt`, and `PROOF.md`. A turn's status in `data/turns.yml` may only be `done` once `PROOF.md` holds a real result (including the null) **and** a reproduce command. Turn scripts are honest scaffolds: they compute a real metric once you wire the open data (`# TODO(you)`) and refuse to fabricate scores.

## CI / automation (`.github/workflows/`)

- `ci.yml` — runs `make check` + a `lychee` link check on `README.md`/`docs/ROADMAP.md` (config in `lychee.toml`) on every push/PR to `main`.
- `pages.yml` — on changes to `site/**` or `data/**`, rebuilds the site + graph and deploys to GitHub Pages.
- `track.yml` — weekly (Mondays 08:00 UTC), runs `track.py` + `synthesize.py` + `build_graph.py` and opens a PR (`bot/frontier`) carrying the refreshed signal + the `_synthesis.md` proposals to review.
- `recap.yml` — daily (23:00 UTC), runs `recap.py` (needs the `ANTHROPIC_API_KEY` secret); if the day moved, commits the new `site/writings/` page + `site/feed.xml`, which `pages.yml` then redeploys.

## Working conventions

- Editing content = edit `data/*.yml`, then `make build && make check` before committing. If you touch site-facing data, also `make site`.
- Keep the `no evidence ⇒ no claim` discipline in any content you add: verified links and real quotes only; label computed-on-public-data results as such and separate from wet-lab claims.
