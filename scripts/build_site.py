#!/usr/bin/env python3
"""Compile data/*.yml -> site/data.json for the build-in-public dashboard.

Same single source of truth as the README, so the live site can't drift from it.
"""
from __future__ import annotations

import json
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "site" / "data.json"


def load(name: str):
    p = DATA / f"{name}.yml"
    return (yaml.safe_load(p.read_text()) if p.exists() else []) or []


def main() -> int:
    bundle = {n: load(n) for n in ("meta", "loop", "roadmap", "turns", "frontier", "reflections",
                                   "people", "startups", "stack", "ecosystem")}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(bundle, ensure_ascii=False, indent=2))
    counts = {k: (len(v) if isinstance(v, list) else 1) for k, v in bundle.items()}
    print(f"Wrote {OUT.relative_to(ROOT)} — {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
