"""Re-review analysis: compare all horse SHLD2 UniProt/Ensembl protein models with
human SHLD2 isoforms 1 and 2 (Q86V20-1, Q86V20-2).

Fetches sequences from the UniProt REST API (saved to horse_shld2_models_rereview.fasta),
runs global alignments (BLOSUM62, gap open -10, extend -0.5) and reports, per model:
length, identity to each human isoform over aligned columns, coverage, and
the last human residue aligned with >=70% local identity in a 30-column window
(to locate where each horse C-terminus diverges).

Run: uv run --with biopython --with requests python compare_isoforms_rereview.py
"""
import json
import requests
from Bio import Align
from Bio.Align import substitution_matrices

HORSE = ["A0A9L0RGD6", "A0A9L0TUF0", "F6W5G1", "A0A3Q2HUD4", "A0A9L0RPS9",
         "A0A9L0TSK2", "A0A3Q2I8C2"]
HUMAN = ["Q86V20-1", "Q86V20-2"]


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    lines = r.text.strip().splitlines()
    return "".join(lines[1:])


def last_conserved_human_pos(aln, window: int = 30, thresh: float = 0.7) -> tuple:
    """(human, horse) coordinates at the end of the last window with >= thresh identity."""
    a, b = aln[0], aln[1]
    hpos = []
    pos = 0
    for ca in a:
        if ca != "-":
            pos += 1
        hpos.append(pos)
    qpos = []
    pos = 0
    for cb in b:
        if cb != "-":
            pos += 1
        qpos.append(pos)
    best = (0, 0)
    for i in range(0, len(a) - window + 1):
        idn = sum(1 for x, y in zip(a[i:i + window], b[i:i + window]) if x == y and x != "-")
        if idn / window >= thresh:
            best = (hpos[i + window - 1], qpos[i + window - 1])
    return best


def main() -> None:
    seqs = {acc: fetch(acc) for acc in HORSE + HUMAN}
    with open("horse_shld2_models_rereview.fasta", "w") as fh:
        for acc, s in seqs.items():
            fh.write(f">{acc}\n{s}\n")
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aligner.end_gap_score = 0
    results = []
    for h in HORSE:
        row = {"horse": h, "length": len(seqs[h]), "n_terminal_20": seqs[h][:20], "c_terminal_20": seqs[h][-20:]}
        for hu in HUMAN:
            aln = aligner.align(seqs[hu], seqs[h])[0]
            a, b = aln[0], aln[1]
            pairs = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
            ident = sum(1 for x, y in pairs if x == y)
            row[hu] = {
                "human_length": len(seqs[hu]),
                "paired": len(pairs),
                "identity_pct": round(100 * ident / len(pairs), 1),
                "human_coverage_pct": round(100 * len(pairs) / len(seqs[hu]), 1),
                "last_conserved_human_residue": last_conserved_human_pos(aln)[0],
                "horse_residue_at_that_point": last_conserved_human_pos(aln)[1],
            }
        results.append(row)
    with open("compare_isoforms_rereview.json", "w") as fh:
        json.dump(results, fh, indent=2)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
