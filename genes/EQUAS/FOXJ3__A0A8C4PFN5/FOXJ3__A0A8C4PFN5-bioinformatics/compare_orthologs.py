# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Global alignment of donkey FOXJ3 (A0A8C4PFN5) to reviewed mouse and human FOXJ3.

Usage (from this folder):
    uv run --script compare_orthologs.py ../FOXJ3__A0A8C4PFN5-uniprot.txt \
        mouse-Q8BUR3-uniprot.txt human-Q9UPW0-uniprot.txt > orthologs.json

Reports percent identity over aligned positions and over the fork-head
DNA_BIND span annotated in each reference record, plus the PANTHER
cross-references stated in each flat file.
"""

import json
import sys

from Bio import Align
from Bio.Align import substitution_matrices


def parse(path: str) -> dict:
    seq_lines, in_seq = [], False
    acc, panther, dna_bind = None, [], None
    with open(path) as fh:
        lines = fh.readlines()
    for i, line in enumerate(lines):
        if line.startswith("AC   ") and acc is None:
            acc = line[5:].split(";")[0].strip()
        if line.startswith("DR   PANTHER;"):
            panther.append(line.split(";")[1].strip())
        if line.startswith("FT   DNA_BIND") and dna_bind is None:
            a, b = line.split()[2].split("..")
            dna_bind = (int(a), int(b))
        if line.startswith("SQ   "):
            in_seq = True
            continue
        if line.startswith("//"):
            in_seq = False
        if in_seq:
            seq_lines.append("".join(line.split()))
    return {"acc": acc, "seq": "".join(seq_lines), "panther": panther, "dna_bind": dna_bind}


def compare(q: dict, r: dict) -> dict:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aln = aligner.align(q["seq"], r["seq"])[0]
    qmap = {}
    ident = aligned = 0
    for (qs, qe), (rs, re_) in zip(*aln.aligned):
        for k in range(qe - qs):
            aligned += 1
            qmap[rs + k + 1] = qs + k + 1
            if q["seq"][qs + k] == r["seq"][rs + k]:
                ident += 1
    out = {
        "reference": r["acc"],
        "reference_length": len(r["seq"]),
        "reference_panther": r["panther"],
        "aligned_positions": aligned,
        "identical_positions": ident,
        "percent_identity_aligned": round(100 * ident / aligned, 2),
    }
    if r["dna_bind"]:
        a, b = r["dna_bind"]
        span = [p for p in range(a, b + 1)]
        mapped = [p for p in span if p in qmap]
        same = sum(1 for p in mapped if q["seq"][qmap[p] - 1] == r["seq"][p - 1])
        out["reference_forkhead_span"] = [a, b]
        out["forkhead_positions_aligned"] = len(mapped)
        out["forkhead_identical"] = same
    return out


def main() -> None:
    query = parse(sys.argv[1])
    refs = [parse(p) for p in sys.argv[2:]]
    result = {
        "query": query["acc"],
        "query_length": len(query["seq"]),
        "query_panther": query["panther"],
        "comparisons": [compare(query, r) for r in refs],
    }
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
