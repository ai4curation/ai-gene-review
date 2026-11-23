# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython==1.85"]
# ///
"""Compare the benchmark donkey FOXJ3 model with the full-length donkey model and human FOXJ3.

Usage (from this folder):
  uv run --script compare_gene_models_rereview.py ../FOXJ3-uniprot.txt \
      donkey-A0A8C4PFN5-uniprot.txt human-Q9UPW0-uniprot.txt alignment_rereview.json

For each pair (benchmark vs full-length donkey; full-length donkey vs human;
benchmark vs human) it reports identity among paired residues, the ranges of
the longer sequence with no partner, and whether the annotated fork-head
domain (taken from each record's DNA_BIND feature) is gap-free. Global
alignment, BLOSUM62, gap open -10, extension -0.5. Sequence similarity alone
does not establish function.
"""
import json
import sys
from pathlib import Path

from Bio import Align, SeqIO
from Bio.Align import substitution_matrices


def dna_bind(rec):
    for f in rec.features:
        if f.type == "DNA_BIND":
            return int(f.location.start) + 1, int(f.location.end)
    return None


def compare(a, b):
    al = Align.PairwiseAligner()
    al.mode = "global"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    best = al.align(a.seq, b.seq)[0]
    x, y = str(best[0]), str(best[1])
    ai = bi = 0
    paired = ident = 0
    a_unpaired, b_unpaired = [], []
    b_of_a = {}
    for cx, cy in zip(x, y):
        if cx != "-":
            ai += 1
        if cy != "-":
            bi += 1
        if cx != "-" and cy != "-":
            paired += 1
            ident += cx == cy
            b_of_a[ai] = bi
        elif cx != "-":
            a_unpaired.append(ai)
        elif cy != "-":
            b_unpaired.append(bi)

    def ranges(ps):
        out = []
        for p in ps:
            if out and p == out[-1][1] + 1:
                out[-1][1] = p
            else:
                out.append([p, p])
        return out

    fh = dna_bind(a)
    fh_gapfree = None
    if fh:
        fh_gapfree = all(i in b_of_a for i in range(fh[0], fh[1] + 1))
    return {
        "a": a.id,
        "b": b.id,
        "len_a": len(a.seq),
        "len_b": len(b.seq),
        "paired": paired,
        "identity_pct": round(100 * ident / paired, 2),
        "a_ranges_without_partner": ranges(a_unpaired),
        "b_ranges_without_partner": ranges(b_unpaired),
        "a_forkhead_dna_bind": fh,
        "a_forkhead_gap_free": fh_gapfree,
    }


def main():
    bench, full, human, out = map(Path, sys.argv[1:5])
    rb, rf, rh = (SeqIO.read(p, "swiss") for p in (bench, full, human))
    res = [compare(rf, rb), compare(rh, rf), compare(rh, rb)]
    Path(out).write_text(json.dumps(res, indent=2))
    for r in res:
        print(json.dumps(r))


if __name__ == "__main__":
    main()
