# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Compare donkey STX3 (A0A8C4LHZ8) with experimentally characterised mammalian syntaxin 3A
orthologs and with donkey syntaxin 3B, and check conserved functional motifs.

Run: uv run --script compare_orthologs.py
Writes sequences.fasta and results.json next to this script.
"""
import json
import re
from pathlib import Path

import requests
from Bio import Align

HERE = Path(__file__).parent
TARGET = "A0A8C4LHZ8"
REFS = {
    "Q13277": "human STX3 (isoform A, canonical)",
    "Q08849": "rat Stx3 (syntaxin 3A)",
    "Q64704": "mouse Stx3 (syntaxin 3A, canonical)",
    "A0A8C4PQW9": "donkey STX3 syntaxin 3B gene model",
    "Q16623": "human STX1A (paralog, plasma membrane syntaxin)",
    "Q12846": "human STX4 (paralog, plasma membrane syntaxin)",
}

# Motifs from the literature, searched as literal strings in the target
MOTIFS = {
    "FMDE apical targeting motif (PMID:16785322)": "FMDE",
    "Munc18 N-peptide region start (MKDRL)": "MKDRL",
    "SNARE zero-layer glutamine context (ENQGEML)": "NQGEML",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def identity(a: str, b: str) -> dict:
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.match_score = 2
    aligner.mismatch_score = -1
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    s1, s2 = aln[0], aln[1]
    cols = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    ident = sum(1 for x, y in cols if x == y)
    return {
        "aligned_columns": len(cols),
        "identical": ident,
        "percent_identity_over_target": round(100 * ident / len(a), 1),
    }


def main() -> None:
    seqs = {TARGET: fetch(TARGET)}
    for acc in REFS:
        seqs[acc] = fetch(acc)
    with open(HERE / "sequences.fasta", "w") as fh:
        for acc, s in seqs.items():
            fh.write(f">{acc}\n{s}\n")
    target = seqs[TARGET]
    results = {"target": TARGET, "target_length": len(target), "comparisons": {}, "motifs": {}}
    for acc, label in REFS.items():
        d = identity(target, seqs[acc])
        d["label"] = label
        d["length"] = len(seqs[acc])
        results["comparisons"][acc] = d
    for name, motif in MOTIFS.items():
        hits = [m.start() + 1 for m in re.finditer(motif, target)]
        results["motifs"][name] = {"motif": motif, "positions_1based": hits}
    (HERE / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
