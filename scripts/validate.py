#!/usr/bin/env python3
"""Schema gate for data/*.yml — required fields + working URLs, no duplicates."""
from __future__ import annotations

import pathlib
import sys

import yaml

DATA = pathlib.Path(__file__).resolve().parent.parent / "data"
REQUIRED = {
    "people": ["name", "url", "org"],
    "startups": ["name", "url", "focus"],
    "stack": ["name", "url", "kind"],
    "ecosystem": ["name", "url", "type"],
    "frontier": ["name", "recent_work", "link"],
}


def check_file(name: str, fields: list[str]) -> list[str]:
    path = DATA / f"{name}.yml"
    if not path.exists():
        return [f"{name}.yml: missing"]
    try:
        rows = yaml.safe_load(path.read_text()) or []
    except yaml.YAMLError as exc:
        return [f"{name}.yml: invalid YAML — {exc}"]
    errs, seen = [], set()
    for i, e in enumerate(rows):
        where = f"{name}.yml[{i}]"
        if not isinstance(e, dict):
            errs.append(f"{where}: not a mapping")
            continue
        errs += [f"{where}: missing '{f}'" for f in fields if not e.get(f)]
        url = str(e.get("url", ""))
        if url and not url.startswith(("http://", "https://")):
            errs.append(f"{where}: bad url {url!r}")
        if url and url in seen:
            errs.append(f"{where}: duplicate url {url}")
        seen.add(url)
    return errs


def main() -> int:
    errors: list[str] = []
    for name, fields in REQUIRED.items():
        errors += check_file(name, fields)
    if errors:
        print("Validation FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  ✗ {e}", file=sys.stderr)
        return 1
    print("Validation passed — data/*.yml well-formed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
