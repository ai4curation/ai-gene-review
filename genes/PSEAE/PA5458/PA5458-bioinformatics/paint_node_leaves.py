"""List the leaf IBAs propagated from the two PAINT nodes seeded by PA5458.

Reads the PAINT leaf GAF (gene_association.paint_uniprot.gaf.gz from
https://data.pantherdb.org/ftp/downloads/paint/current/, cached by
projects/PSEUDOCAP/build_iba_seed_worklist.py at .cache/paint/leaf.gaf.gz)
and the IBD.gaf, and reports, for PTN000546841 (GO:0009103) and PTN000546715
(GO:0000271), the IBD rows, the leaf proteins/symbols, and taxon counts.

Usage: python -I paint_node_leaves.py <leaf.gaf.gz> <IBD.gaf>
"""

import collections
import gzip
import sys

NODES = {"PTN000546841": "GO:0009103", "PTN000546715": "GO:0000271"}


def main(leaf_path: str, ibd_path: str) -> None:
    print("## IBD rows at the nodes")
    for line in open(ibd_path):
        f = line.rstrip("\n").split("\t")
        if len(f) > 7 and (f[1] in NODES or any(n in f[7] for n in NODES)):
            print("\t".join([f[1], f[3], f[4], f[6], f[7], f[12]]))
    rows = collections.defaultdict(list)
    with gzip.open(leaf_path, "rt") as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            f = line.rstrip("\n").split("\t")
            for node, term in NODES.items():
                if f[4] == term and node in f[7]:
                    rows[node].append((f[1], f[2], f[12]))
    for node, term in NODES.items():
        r = sorted(set(rows[node]))
        taxa = collections.Counter(x[2] for x in r)
        print(f"\n## {node} {term}: {len(r)} leaf IBAs in {len(taxa)} taxa")
        for t, n in taxa.most_common():
            print(f"{t}\t{n}")
        print("leaves:")
        for acc, sym, tax in r:
            print(f"  {acc}\t{sym}\t{tax}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
