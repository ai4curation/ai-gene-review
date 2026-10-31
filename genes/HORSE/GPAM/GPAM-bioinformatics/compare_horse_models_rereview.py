"""Compare all UniProt horse GPAM gene models with human/mouse/rat GPAT1.

Re-review analysis (2026-10-20). Downloads sequences from UniProt REST,
aligns each to human Q9HCL2 (global, BLOSUM62), and reports length,
identity, human-coordinate gaps, and retention of experimentally defined
human features (HXXXXD motif 230-235, CoA-binding residues, the 80-120
mitochondrial-localization region). Writes results-rereview.json and
models-rereview.fasta next to this script.

Run: uv run --with biopython python compare_horse_models_rereview.py
"""

import json
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent
REFERENCE = "Q9HCL2"
ORTHOLOGS = ["Q61586", "P97564"]  # mouse, rat GPAT1 (Swiss-Prot)
HORSE_MODELS = [
    "A0A9L0TCA8", "A0A9L0TTC1", "A0A9L0TA25", "A0A9L0SEV4", "A0A9L0RK03",
    "A0A3Q2L5A4", "A0A3Q2HJJ9", "A0A9L0RLS5", "A0A9L0S6K6",
]
HUMAN_FEATURES = {
    "HXXXXD_motif_230_235": list(range(230, 236)),
    "CoA_binding_278_279_288_293_328_462": [278, 279, 288, 293, 328, 462],
    "mito_localization_region_80_120": list(range(80, 121)),
    "segment_370_407": list(range(370, 408)),
}


def fetch(acc: str) -> tuple[str, str]:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    text = urllib.request.urlopen(url).read().decode()
    header, *seq = text.strip().splitlines()
    return header, "".join(seq)


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.end_gap_score = 0
    return a


def ref_to_query_map(aln) -> dict[int, int]:
    """Map 1-based reference positions to 1-based query positions."""
    mapping = {}
    for (rs, re_), (qs, qe) in zip(*aln.aligned):
        for i in range(re_ - rs):
            mapping[rs + i + 1] = qs + i + 1
    return mapping


def gaps(mapping: dict[int, int], ref_len: int) -> list[list[int]]:
    out, start = [], None
    for p in range(1, ref_len + 1):
        if p not in mapping:
            start = p if start is None else start
        elif start is not None:
            out.append([start, p - 1])
            start = None
    if start is not None:
        out.append([start, ref_len])
    return out


def main() -> None:
    seqs = {acc: fetch(acc) for acc in [REFERENCE, *ORTHOLOGS, *HORSE_MODELS]}
    ref = seqs[REFERENCE][1]
    al = aligner()
    results = {"reference": REFERENCE, "reference_length": len(ref), "proteins": {}}
    for acc, (header, seq) in seqs.items():
        if acc == REFERENCE:
            continue
        aln = al.align(ref, seq)[0]
        m = ref_to_query_map(aln)
        ident = sum(1 for r, q in m.items() if ref[r - 1] == seq[q - 1])
        feats = {}
        for name, positions in HUMAN_FEATURES.items():
            present = [p for p in positions if p in m]
            same = [p for p in present if ref[p - 1] == seq[m[p] - 1]]
            feats[name] = {
                "positions": len(positions),
                "aligned": len(present),
                "identical": len(same),
            }
        results["proteins"][acc] = {
            "header": header,
            "length": len(seq),
            "aligned_pairs": len(m),
            "identity_over_aligned": round(ident / len(m), 4) if m else 0.0,
            "human_coverage": round(len(m) / len(ref), 4),
            "query_extra_residues": len(seq) - len(m),
            "human_gaps": gaps(m, len(ref)),
            "features": feats,
        }
    (HERE / "results-rereview.json").write_text(json.dumps(results, indent=2) + "\n")
    with open(HERE / "models-rereview.fasta", "w") as fh:
        for acc, (header, seq) in seqs.items():
            fh.write(f"{header}\n")
            for i in range(0, len(seq), 60):
                fh.write(seq[i:i + 60] + "\n")
    for acc, r in results["proteins"].items():
        print(acc, r["length"], r["identity_over_aligned"], r["human_coverage"],
              r["query_extra_residues"], r["human_gaps"],
              {k: f'{v["identical"]}/{v["positions"]}' for k, v in r["features"].items()})


if __name__ == "__main__":
    main()
