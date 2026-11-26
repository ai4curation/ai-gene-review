"""Map canonical relay residues onto frozen KT2440 sequences; no assay identity claim."""

import hashlib
from pathlib import Path

import yaml
from Bio.Align import PairwiseAligner
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent


def sequence(path):
    text = path.read_text().split("SQ   SEQUENCE", 1)[1]
    return "".join(
        "".join(line.split()) for line in text.splitlines()[1:] if line.startswith(" ")
    )


def main():
    aligner = PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    result = {}
    for gene, positions in {
        "mnmA": [99, 102, 199],
        "tusA": [19],
        "tusD": [78],
        "tusE": [108],
    }.items():
        paths = [
            ROOT / f"genes/{org}/{gene}/{gene}-uniprot.txt"
            for org in ["ECOLI", "PSEPK"]
        ]
        seqs = [sequence(p) for p in paths]
        alignment = aligner.align(*seqs)[0]
        pairs = {
            int(i) + 1: int(j) + 1
            for i, j in zip(*alignment.indices, strict=True)
            if i >= 0 and j >= 0
        }
        aligned_pairs = [
            (i, j) for i, j in zip(*alignment.indices, strict=True) if i >= 0 and j >= 0
        ]
        result[gene] = {
            "source_sha256": {
                str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in paths
            },
            "lengths_ecoli_psepk": list(map(len, seqs)),
            "alignment": str(alignment),
            "identical_aligned_residues": sum(
                seqs[0][i] == seqs[1][j] for i, j in aligned_pairs
            ),
            "aligned_residue_pairs": len(aligned_pairs),
            "residue_bridge": [
                {
                    "ecoli_position": p,
                    "ecoli_residue": seqs[0][p - 1],
                    "psepk_position": pairs.get(p),
                    "psepk_residue": seqs[1][pairs[p] - 1] if p in pairs else None,
                }
                for p in positions
            ],
            "scope": "Sequence-based homolog mapping, not exact assay-construct identity or direct KT2440 activity measurement.",
        }
    (OUT / "sequence-bridge.yaml").write_text(
        yaml.safe_dump(result, sort_keys=False, width=100)
    )
    print(
        yaml.safe_dump(
            {k: v["residue_bridge"] for k, v in result.items()}, sort_keys=False
        )
    )


if __name__ == "__main__":
    main()
