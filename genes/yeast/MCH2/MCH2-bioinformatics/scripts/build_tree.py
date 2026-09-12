#!/usr/bin/env python3
"""Build a neighbor-joining tree from an MSA to show subfamily placement.

Uses Biopython's DistanceCalculator (identity distance) + NJ. Writes a Newick
tree and an ASCII rendering. Runs on any aligned FASTA.

Usage:
    python build_tree.py --aln results/panel_aln.fasta \
        --newick results/panel_nj.nwk --ascii results/panel_nj_ascii.txt
"""
import argparse
from pathlib import Path

from Bio import AlignIO
from Bio.Phylo import write as phylo_write
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--aln", required=True, type=Path)
    ap.add_argument("--newick", required=True, type=Path)
    ap.add_argument("--ascii", required=True, type=Path)
    args = ap.parse_args()

    aln = AlignIO.read(str(args.aln), "fasta")
    # shorten ids for readability
    for rec in aln:
        rec.id = rec.id.split("|")[-1]
        rec.name = rec.id
        rec.description = ""

    calc = DistanceCalculator("identity")
    dm = calc.get_distance(aln)
    constructor = DistanceTreeConstructor()
    tree = constructor.nj(dm)
    tree.ladderize()

    args.newick.parent.mkdir(parents=True, exist_ok=True)
    phylo_write(tree, str(args.newick), "newick")

    import io

    from Bio import Phylo

    buf = io.StringIO()
    Phylo.draw_ascii(tree, file=buf)
    args.ascii.write_text(buf.getvalue())
    print(buf.getvalue())
    print(f"Wrote {args.newick} and {args.ascii}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
