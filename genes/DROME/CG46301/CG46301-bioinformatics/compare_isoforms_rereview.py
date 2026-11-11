"""Compare the four UniProt CG46301 products and the vertebrate NOL4/NOL4L proteins.

Run: uv run --with biopython python compare_isoforms_rereview.py

Inputs are UniProt FASTA files in this folder (downloaded 2026-10-20 from
rest.uniprot.org). Reports, for each fly product, its length, where it maps on
the 1237-aa A0A1W5PXH3 product (local alignment), and the identity of the
A0A1W5PXH3 NOL4 helical domain (Pfam PF23079, residues 789-886) to human NOL4,
human NOL4L and mouse Nol4 by local alignment.
"""

from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
FLY = ["A0A1W5PXH3", "A0A1W5Q009", "A0A1W5PVN5", "A0A1W5PW03"]
VERT = {"O94818": "human NOL4", "Q96MY1": "human NOL4L", "P60954": "mouse Nol4"}
HTH = (789, 886)


def load(acc: str) -> str:
    return str(next(SeqIO.parse(HERE / f"{acc}.fa", "fasta")).seq)


def aligner() -> PairwiseAligner:
    a = PairwiseAligner()
    a.mode = "local"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    return a


def summarize(query: str, target: str) -> tuple[int, int, int, int, float, int]:
    aln = aligner().align(query, target)[0]
    qb, tb = aln.aligned
    ident = sum(
        sum(1 for i, j in zip(range(q0, q1), range(t0, t1)) if query[i] == target[j])
        for (q0, q1), (t0, t1) in zip(qb, tb)
    )
    alen = sum(q1 - q0 for q0, q1 in qb)
    return qb[0][0] + 1, qb[-1][1], tb[0][0] + 1, tb[-1][1], ident / alen, alen


def main() -> None:
    ref = load("A0A1W5PXH3")
    print("## Fly CG46301 products mapped onto A0A1W5PXH3 (1237 aa)")
    for acc in FLY:
        s = load(acc)
        qs, qe, ts, te, pid, alen = summarize(s, ref)
        covers_hth = ts <= HTH[0] and te >= HTH[1]
        print(
            f"{acc}\tlen={len(s)}\tquery {qs}-{qe} -> ref {ts}-{te}\t"
            f"identity={pid:.3f} over {alen}\tcovers_HTH_789-886={covers_hth}"
        )
    hth = ref[HTH[0] - 1 : HTH[1]]
    print("\n## A0A1W5PXH3 HTH_NOL4 domain (789-886) vs vertebrate relatives")
    for acc, name in VERT.items():
        s = load(acc)
        qs, qe, ts, te, pid, alen = summarize(hth, s)
        print(
            f"{acc} ({name}, {len(s)} aa)\tdomain {qs + HTH[0] - 1}-{qe + HTH[0] - 1}"
            f" -> {ts}-{te}\tidentity={pid:.3f} over {alen}"
        )
    print("\n## Full-length A0A1W5PXH3 vs vertebrate relatives")
    for acc, name in VERT.items():
        s = load(acc)
        qs, qe, ts, te, pid, alen = summarize(ref, s)
        print(f"{acc} ({name})\tref {qs}-{qe} -> {ts}-{te}\tidentity={pid:.3f} over {alen}")


if __name__ == "__main__":
    main()
