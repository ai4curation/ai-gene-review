#!/usr/bin/env python3
"""Locate PAINT IBD/IKR/IRD annotations on the PANTHER tree path to a gene.

For a PANTHER family and one or more gene identifiers (as PANTHER writes them,
e.g. ``FlyBase:FBgn0014396``), print the root-to-leaf path of tree nodes with
each node's persistent PTN id, event type (speciation/duplication), taxon and
subfamily, and every node-level PAINT annotation (IBD, IKR, IRD; NOT qualifier
shown) that sits on that path. Optionally list the leaves under named nodes.

Inputs are fetched live (stdlib only, no third-party packages):
  * PANTHER tree: https://pantherdb.org/services/oai/pantherdb/treeinfo?family=<FAM>
  * PAINT node GAF: IBD.gaf from the pinned PAINT snapshot (same URL the
    repository's ai_gene_review.etl.panther_families module uses).

Usage:
  python paint_node_placement.py PTHR22940 FlyBase:FBgn0014396 FlyBase:FBgn0038118 \
      --leaves PTN008585096
Downloads go to --cache-dir (default: a temporary directory).
"""
from __future__ import annotations

import argparse
import json
import tempfile
import urllib.request
from pathlib import Path

TREE_URL = "https://pantherdb.org/services/oai/pantherdb/treeinfo?family={fam}"
IBD_URL = "https://data.pantherdb.org/ftp/downloads/paint/19.0/2026-08-28/IBD.gaf"


def fetch(url: str, dest: Path) -> Path:
    if not dest.exists():
        with urllib.request.urlopen(url, timeout=300) as r:
            dest.write_bytes(r.read())
    return dest


def kids(node: dict) -> list:
    ch = node.get("children") or {}
    k = ch.get("annotation_node", [])
    return [k] if isinstance(k, dict) else k


def walk(node: dict, path: list):
    path = path + [node]
    if not kids(node):
        yield path
    for k in kids(node):
        yield from walk(k, path)


def find(node: dict, pid: str):
    if node.get("persistent_id") == pid:
        return node
    for k in kids(node):
        hit = find(k, pid)
        if hit:
            return hit
    return None


def leaves(node: dict):
    if not kids(node):
        yield node
    for k in kids(node):
        yield from leaves(k)


def describe(n: dict) -> str:
    return (
        f"{n.get('persistent_id')}  event={n.get('event_type') or '-'}  "
        f"taxon={n.get('species') or n.get('organism') or '-'}  "
        f"subfamily={n.get('sf_id') or '-'}  gene={n.get('gene_symbol') or '-'}"
    )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("family")
    ap.add_argument("genes", nargs="+", help="PANTHER gene ids, e.g. FlyBase:FBgn0014396")
    ap.add_argument("--leaves", nargs="*", default=[], help="PTN ids whose leaves to list")
    ap.add_argument("--cache-dir", type=Path, default=None)
    a = ap.parse_args()
    cache = a.cache_dir or Path(tempfile.mkdtemp())
    cache.mkdir(parents=True, exist_ok=True)
    tree = json.loads(fetch(TREE_URL.format(fam=a.family), cache / f"{a.family}_tree.json").read_text())
    root = tree["search"]["tree_topology"]["annotation_node"]
    ibd: dict = {}
    for line in fetch(IBD_URL, cache / "IBD.gaf").read_text().splitlines():
        if line.startswith("!") or not line.strip():
            continue
        f = line.split("\t")
        ibd.setdefault(f[1], []).append(f"{('NOT ' if 'NOT' in f[3] else '')}{f[4]} {f[6]} from {f[7]}")
    print(f"# {a.family}: tree root {root.get('persistent_id')} ({root.get('species')})")
    print(f"# IBD.gaf: {IBD_URL}")
    for path in walk(root, []):
        leaf = path[-1]
        if leaf.get("gene_id") not in a.genes:
            continue
        print(f"\n## Path to {leaf.get('gene_symbol')} {leaf.get('gene_id')} ({leaf.get('organism') or leaf.get('species')})")
        for depth, n in enumerate(path):
            print("  " * depth + describe(n))
            for row in ibd.get(n.get("persistent_id"), []):
                print("  " * depth + f"    PAINT: {row}")
    for pid in a.leaves:
        node = find(root, pid)
        if node is None:
            print(f"\n## {pid}: not found")
            continue
        print(f"\n## Leaves under {describe(node)}")
        for lf in leaves(node):
            print(f"  {lf.get('organism') or lf.get('species')}\t{lf.get('gene_symbol')}\t{lf.get('gene_id')}")
        under = [(n.get("persistent_id"), r) for n in [node, *[x for p in walk(node, []) for x in p]]
                 for r in ibd.get(n.get("persistent_id"), [])]
        seen = set()
        print(f"  PAINT rows on nodes at or below {pid}:")
        for nid, r in under:
            if (nid, r) in seen:
                continue
            seen.add((nid, r))
            print(f"    {nid}: {r}")


if __name__ == "__main__":
    main()
