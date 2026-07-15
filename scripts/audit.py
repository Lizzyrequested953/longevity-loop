#!/usr/bin/env python3
"""Loop self-audit — is this project still an AI-native compounding loop?

Scores the principles in data/loop.yml from real evidence in the repo (a file
that must exist, or a regex that must be found). No evidence ⇒ the principle
fails. `--gate N` exits non-zero below N so CI blocks a regression in HOW we work.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOOP = yaml.safe_load((ROOT / "data" / "loop.yml").read_text())


def has(item: dict) -> bool:
    target = ROOT / item["file"]
    if not target.exists():
        return False
    if "grep" not in item:
        return True
    try:
        return re.search(item["grep"], target.read_text(errors="ignore")) is not None
    except OSError:
        return False


def run() -> dict:
    out = []
    for p in LOOP["principles"]:
        ev = p.get("evidence", [])
        frac = sum(has(e) for e in ev) / len(ev) if ev else 0.0
        out.append({"id": p["id"], "frac": round(frac, 2),
                    "status": "met" if frac == 1 else "partial" if frac else "fail"})
    score = round(100 * sum(p["frac"] for p in out) / len(out)) if out else 0
    return {"score": score, "threshold": LOOP.get("pass_threshold", 80), "principles": out}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", type=int)
    args = ap.parse_args()
    r = run()
    icon = {"met": "✅", "partial": "🟡", "fail": "❌"}
    verdict = "AI-NATIVE LOOP" if r["score"] >= r["threshold"] else "NOT YET"
    print(f"Loop audit: {r['score']}/100 (threshold {r['threshold']}) — {verdict}\n")
    for p in r["principles"]:
        print(f"  {icon[p['status']]} {p['id']:<26} {int(p['frac']*100):>3}%")
    if args.gate is not None and r["score"] < args.gate:
        print(f"\n::gate:: FAILED — loop score {r['score']} < {args.gate}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
