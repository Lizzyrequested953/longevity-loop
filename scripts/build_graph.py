#!/usr/bin/env python3
"""Build the field's spatiotemporal knowledge graph → site/graph.json.

Models the field as a bi-temporal KG (à la getzep/graphiti): nodes = people,
orgs, topics; edges carry a `since` year so the structure can be queried over
time. Structural now; scripts/track.py refreshes dated paper nodes each run, so
it becomes genuinely spatiotemporal (evolving) as the loop turns.
"""
from __future__ import annotations

import json
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "site" / "graph.json"

# topic → substrings that imply it (matched against known_for / focus, lowercased)
TOPICS = {
    "aging clocks": ["clock", "phenoage", "grimage", "dunedin", "epigenetic age", "biological age"],
    "reprogramming": ["reprogram", "rejuven", "yamanaka", "partial reprogram"],
    "AI drug discovery": ["ai drug", "generative", "drug discovery", "molecule", "target discovery"],
    "single-cell / multi-omics": ["single-cell", "single cell", "multi-omics", "multiomics", "transcriptom", "virtual cell"],
    "proteomics": ["proteom", "plasma", "organ aging"],
    "senolytics": ["senolytic", "senescen"],
    "systems / genetics": ["genetics", "centenarian", "gene-therapy", "gene therapy", "synthetic biology", "databases"],
    "geroscience / interventions": ["rapamycin", "metformin", "nad", "geroscience", "autophagy", "sirtuin", "physics"],
}


def topics_for(text: str) -> list[str]:
    t = text.lower()
    return [topic for topic, keys in TOPICS.items() if any(k in t for k in keys)]


def main() -> int:
    people = yaml.safe_load((DATA / "people.yml").read_text()) or []
    startups = yaml.safe_load((DATA / "startups.yml").read_text()) or []
    frontier = {}
    fp = DATA / "frontier.yml"
    if fp.exists():
        frontier = {e["name"]: e for e in (yaml.safe_load(fp.read_text()) or [])}

    nodes, links, seen = [], [], set()

    def node(nid: str, label: str, ntype: str, **extra):
        if nid not in seen:
            seen.add(nid)
            nodes.append({"id": nid, "label": label, "type": ntype, **extra})

    for topic in TOPICS:
        node(f"topic:{topic}", topic, "topic")

    for p in people:
        pid = f"person:{p['name']}"
        node(pid, p["name"], "person", url=p.get("url", ""), ai=bool(p.get("ai_forward")))
        org = p.get("org", "")
        if org:
            node(f"org:{org}", org, "org")
            links.append({"source": pid, "target": f"org:{org}", "rel": "affiliated"})
        for topic in topics_for(p.get("known_for", "")):
            links.append({"source": pid, "target": f"topic:{topic}", "rel": "works-on"})
        # dated recent-work node (the temporal signal)
        fw = frontier.get(p["name"])
        if fw and fw.get("recent_work") and fw.get("recent_work") != "-":
            wid = f"work:{p['name']}"
            node(wid, fw["recent_work"][:60], "work", url=fw.get("link", ""), since=fw.get("year"))
            links.append({"source": pid, "target": wid, "rel": "authored", "since": fw.get("year")})

    for s in startups:
        sid = f"org:{s['name']}"
        node(sid, s["name"], "org", url=s.get("url", ""), ai=bool(s.get("ai_native")))
        for topic in topics_for(s.get("focus", "")):
            links.append({"source": sid, "target": f"topic:{topic}", "rel": "builds"})

    graph = {"schema": "bi-temporal (edges carry optional `since`); modeled after getzep/graphiti",
             "nodes": nodes, "links": links,
             "counts": {"nodes": len(nodes), "links": len(links)}}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(graph, ensure_ascii=False, indent=2))
    print(f"Wrote {OUT.relative_to(ROOT)} — {len(nodes)} nodes, {len(links)} links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
