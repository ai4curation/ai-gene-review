#!/usr/bin/env python3
"""Shortest metabolite->gene->metabolite route through the assembled network.

Usage: uv run python trace_path.py ORG "source metabolite" "target metabolite"
Reads results/<ORG>/gene_reactions.tsv written by build_network.py. Paths are
undirected (Rhea master reactions carry no physiological direction).
"""
import csv
import sys
from pathlib import Path

import networkx as nx

org, src, dst = sys.argv[1:4]
B = nx.Graph()
for r in csv.DictReader((Path(__file__).parent / "results" / org / "gene_reactions.tsv").open(), delimiter="\t"):
    for m in r["metabolites"].split("; "):
        if m:
            B.add_edge("gene:" + r["gene"], m)
try:
    path = nx.shortest_path(B, src, dst)
except (nx.NetworkXNoPath, nx.NodeNotFound) as e:
    sys.exit(f"no path: {e}")
print("  ->  ".join(f"[{p[5:]}]" if p.startswith("gene:") else p for p in path))
