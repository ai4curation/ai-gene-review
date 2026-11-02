"""Compare canonical horse GPAM (A0A9L0TCA8) with experimentally studied GPAT1 orthologs.

Fetches sequences from UniProt REST, aligns horse, mouse (Q61586) and rat
(P97564) GPAT1 globally to human GPAT1 (Q9HCL2; BLOSUM62, open -10, extend
-0.5, free end gaps) and reports identity, human coverage, human-coordinate
gaps, and conservation of human features: HXXXXD catalytic motif 230-235,
CoA-binding residues 278/279/288/293/328/462 and the N-terminal
mitochondrial-localization region 80-120 (positions as in the human
Swiss-Prot record). Also reports the PANTHER subfamily of the horse entry
and the PAINT IBD assertions for PTHR12563 from the repository cache.

Run: uv run --with biopython python compare_gpat1.py
"""

import csv
import json
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent
REPO = HERE.parents[3]
REFERENCE = "Q9HCL2"
QUERIES = {"A0A9L0TCA8": "horse", "Q61586": "mouse", "P97564": "rat"}
FEATURES = {
    "HXXXXD_230_235": list(range(230, 236)),
    "CoA_binding": [278, 279, 288, 293, 328, 462],
    "mito_region_80_120": list(range(80, 121)),
}
PAINT = REPO / "interpro/panther/PTHR12563/PTHR12563-paint.tsv"
UNIPROT = HERE.parent / "GPAM__A0A9L0TCA8-uniprot.txt"


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    lines = urllib.request.urlopen(url).read().decode().strip().splitlines()
    return "".join(lines[1:])


def make_aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.end_gap_score = 0
    return a


def ref_map(aln) -> dict[int, int]:
    m = {}
    for (rs, re_), (qs, _qe) in zip(*aln.aligned):
        for i in range(re_ - rs):
            m[rs + i + 1] = qs + i + 1
    return m


def gaps(m: dict[int, int], n: int) -> list[list[int]]:
    out, start = [], None
    for p in range(1, n + 1):
        if p not in m:
            start = p if start is None else start
        elif start is not None:
            out.append([start, p - 1])
            start = None
    if start is not None:
        out.append([start, n])
    return out


def main() -> None:
    ref = fetch(REFERENCE)
    al = make_aligner()
    proteins = {}
    for acc, species in QUERIES.items():
        seq = fetch(acc)
        m = ref_map(al.align(ref, seq)[0])
        ident = sum(ref[r - 1] == seq[q - 1] for r, q in m.items())
        feats = {}
        for name, pos in FEATURES.items():
            same = [p for p in pos if p in m and ref[p - 1] == seq[m[p] - 1]]
            feats[name] = f"{len(same)}/{len(pos)}"
        motif = "".join(seq[m[p] - 1] if p in m else "-" for p in FEATURES["HXXXXD_230_235"])
        proteins[acc] = {
            "species": species,
            "length": len(seq),
            "identity_over_aligned": round(ident / len(m), 4),
            "human_coverage": round(len(m) / len(ref), 4),
            "human_gaps": gaps(m, len(ref)),
            "features_identical": feats,
            "motif_230_235": motif,
        }
    panther = [ln.split(";")[1].strip() for ln in UNIPROT.read_text().splitlines()
               if ln.startswith("DR   PANTHER;")]
    with open(PAINT) as fh:
        paint = [
            {k: row[k] for k in ("node", "go_id", "aspect", "evidence", "taxon", "seeds")}
            for row in csv.DictReader(fh, delimiter="\t")
        ]
    result = {
        "reference": REFERENCE,
        "reference_length": len(ref),
        "horse_panther": panther,
        "proteins": proteins,
        "paint_PTHR12563": paint,
    }
    (HERE / "results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
