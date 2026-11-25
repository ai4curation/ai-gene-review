"""Compare mouse Aldh7a1 (Q9DBF1) with vertebrate ALDH7A1 orthologs.

Input: orthologs.fasta (downloaded from the UniProt REST API, see RESULTS.md).
For each ortholog, aligns its canonical sequence globally to mouse Q9DBF1
(BLOSUM62, gap open -10, extend -0.5) and reports
  * percent identity over aligned columns,
  * the residues aligned to the mouse UniProt ACT_SITE positions (E296, C330),
  * the residue aligned to mouse position 130, which corresponds to human
    canonical Ser130 (= Ser102 in the 511-aa human isoform 2 numbering used in
    PMID:31492851), the AMPK phosphosite annotated in human P49419,
  * an 11-residue window around that position.

Run: uv run python genes/mouse/Aldh7a1/Aldh7a1-bioinformatics/compare_orthologs.py
"""

from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
MOUSE_ACC = "Q9DBF1"
POSITIONS = {"catalytic Glu (ACT_SITE)": 296, "catalytic Cys (ACT_SITE)": 330,
             "human AMPK site S130 equivalent": 130}


def aligner() -> PairwiseAligner:
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def main() -> None:
    recs = {r.id.split("|")[1]: r for r in SeqIO.parse(str(HERE / "orthologs.fasta"), "fasta")}
    mouse = str(recs[MOUSE_ACC].seq)
    al = aligner()
    print(f"mouse {MOUSE_ACC} length {len(mouse)}")
    print("mouse window 125-135:", mouse[124:135])
    for acc, rec in recs.items():
        if acc == MOUSE_ACC:
            continue
        other = str(rec.seq)
        aln = al.align(mouse, other)[0]
        pos_map: dict[int, int] = {}
        ident = 0
        for (ms, me), (os_, oe) in zip(*aln.aligned):
            for i, j in zip(range(ms, me), range(os_, oe)):
                pos_map[i + 1] = j + 1
                ident += mouse[i] == other[j]
        name = rec.description.split(" OS=")[1].split(" OX=")[0]
        print(f"\n{acc} ({name}) length {len(other)}: identity {ident / len(pos_map):.3f} "
              f"over {len(pos_map)} aligned columns")
        for label, p in POSITIONS.items():
            q = pos_map.get(p)
            res = f"{other[q - 1]}{q}" if q else "gap"
            print(f"  mouse {mouse[p - 1]}{p} ({label}) -> {res}")
        q = pos_map.get(130)
        if q:
            print(f"  window around equivalent of mouse 130: {other[q - 6:q + 5]}")


if __name__ == "__main__":
    main()
