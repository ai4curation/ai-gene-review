"""Check the GalE catalytic residues of PTHR43725 members against E. coli GalE.

Run from the repository root:
    .venv/bin/python interpro/panther/PTHR43725/active_site_check.py
Writes interpro/panther/PTHR43725/PTHR43725-active-site-check.txt.

E. coli GalE (P09147) catalytic residues are taken from its UniProt record
(ACT_SITE 149, the catalytic Tyr; BINDING 124, the Ser), plus Lys153, the Lys of the
YxxxK motif four residues after Tyr149.
Each query is globally aligned to P09147 (BLOSUM62, gap open -10, extend -0.5)
and the aligned residue at each position is reported. Sequences are fetched
live from UniProt REST; nothing about the result is hard-coded.
"""
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

REF = "P09147"
POSITIONS = {124: "catalytic Ser", 149: "catalytic Tyr (base)", 153: "catalytic Lys"}
QUERIES = {
    "Q14376": "human GALE (characterized epimerase; control)",
    "P73424": "Synechocystis slr1540 (PAINT IRD leaf PTN001621994)",
}
OUT = Path(__file__).resolve().parent / "PTHR43725-active-site-check.txt"


def fasta(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "ai-gene-review"}), timeout=60) as r:
        return "".join(r.read().decode().splitlines()[1:])


def main():
    aligner = Align.PairwiseAligner(mode="global")
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score, aligner.extend_gap_score = -10, -0.5
    ref = fasta(REF)
    lines = [f"reference {REF} length {len(ref)}; " + "; ".join(f"{p}{ref[p-1]} {d}" for p, d in POSITIONS.items())]
    for acc, desc in QUERIES.items():
        q = fasta(acc)
        aln = aligner.align(ref, q)[0]
        rmap = {}
        for (rs, re_), (qs, qe) in zip(*aln.aligned):
            for i in range(re_ - rs):
                rmap[rs + i + 1] = qs + i + 1
        cells = []
        for p in POSITIONS:
            qp = rmap.get(p)
            cells.append(f"{ref[p-1]}{p}->{q[qp-1]}{qp}" if qp else f"{ref[p-1]}{p}->gap")
        ident = sum(1 for p in range(1, len(ref) + 1) if p in rmap and ref[p - 1] == q[rmap[p] - 1])
        lines.append(f"{acc} length {len(q)} identity_to_ref {ident}/{len(ref)} {' '.join(cells)} | {desc}")
    OUT.write_text("\n".join(lines) + "\n")
    print(OUT.read_text())


if __name__ == "__main__":
    main()
