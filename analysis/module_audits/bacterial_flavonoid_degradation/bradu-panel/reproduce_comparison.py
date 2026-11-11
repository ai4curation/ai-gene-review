"""Recheck the committed comparison against frozen UniProt flat files, without network."""

import hashlib
import json
from pathlib import Path
from Bio import Align
from Bio.Align import substitution_matrices

out = Path(__file__).resolve().parent
records = json.loads((out / "sequence-comparison.json").read_text())
aligner = Align.PairwiseAligner()
aligner.mode = "global"
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
for gene, r in records.items():
    paths = list(r["source_hashes"])
    for p, h in r["source_hashes"].items():
        assert hashlib.sha256(Path(p).read_bytes()).hexdigest() == h, p

    def sequence(path):
        return "".join(
            Path(path)
            .read_text()
            .split("SQ   SEQUENCE")[1]
            .split("\n", 1)[1]
            .split("//")[0]
            .split()
        )

    a = aligner.align(sequence(paths[0]), sequence(paths[1]))[0]
    pairs = [(x, y) for x, y in zip(str(a[0]), str(a[1])) if x != "-" and y != "-"]
    assert (
        len(pairs) == r["aligned_pairs"]
        and sum(x == y for x, y in pairs) == r["identical"]
    ), gene
    print(gene, "PASS")
