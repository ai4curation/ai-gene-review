# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Compare the horse NADK2 benchmark gene model (A0A3Q2GYY5) with the other horse
NADK2 TrEMBL models and with the reviewed human (Q4G0N4) and mouse (Q8C5H8) NADK2.

Fetches sequences live from UniProt REST, runs global pairwise alignments
(BLOSUM62, gap open -10, extend -0.5) against human Q4G0N4 and reports
identity plus N-terminal extension and internal insertion/deletion blocks
relative to human. Usage: uv run --script compare_gene_models.py
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = ["Q4G0N4", "Q8C5H8", "A0A3Q2GYY5", "F7DCV0", "A0A3Q2H586", "A0A9L0K2P4"]


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    seqs = {a: fetch(a) for a in ACCS}
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    ref = seqs["Q4G0N4"]
    for acc in ACCS[1:]:
        s = seqs[acc]
        aln = aligner.align(ref, s)[0]
        ident = sum(1 for a, b in zip(aln[0], aln[1]) if a == b and a != "-")
        cols = sum(1 for a, b in zip(aln[0], aln[1]) if a != "-" and b != "-")
        print(f"== {acc} length={len(s)} human_len={len(ref)} "
              f"identity_over_aligned={ident}/{cols} ({100*ident/cols:.1f}%)")
        print(f"   first human-start motif 'MTCYRGF' at query position: "
              f"{s.find('MTCYRGF')+1 if 'MTCYRGF' in s else 'absent'}")
        # gap blocks
        r_row, q_row = aln[0], aln[1]
        rpos = qpos = 0
        i = 0
        while i < len(r_row):
            if r_row[i] == "-":
                j = i
                while j < len(r_row) and r_row[j] == "-":
                    j += 1
                print(f"   insertion in {acc} of {j-i} aa after human pos {rpos}: "
                      f"{q_row[i:j]}")
                qpos += j - i
                i = j
                continue
            if q_row[i] == "-":
                j = i
                while j < len(q_row) and q_row[j] == "-":
                    j += 1
                print(f"   deletion in {acc} of human {rpos+1}..{rpos+j-i}: {r_row[i:j]}")
                rpos += j - i
                i = j
                continue
            rpos += 1
            qpos += 1
            i += 1
        for motif in ("AAGGDGT", "ALNEVF"):
            print(f"   motif {motif}: human pos {ref.find(motif)+1}, {acc} pos "
                  f"{s.find(motif)+1 if motif in s else 'absent'}")
        print(aln.format() if acc == "A0A3Q2GYY5" else "")


if __name__ == "__main__":
    main()
