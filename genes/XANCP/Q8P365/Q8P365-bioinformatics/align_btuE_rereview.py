"""Pairwise alignment of Q8P365 against E. coli BtuE (P06610) and the Xanthomonas
in-paralog Q8PAI2; report residues aligned to GPx catalytic positions.

Sequences are fetched live from UniProt REST. Run:
    uv run --with biopython --with requests python align_btuE_rereview.py
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = ["Q8P365", "P06610", "Q8PAI2"]


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
    q = seqs["Q8P365"]
    print(f"Q8P365 length {len(q)}; cysteines at {[i + 1 for i, c in enumerate(q) if c == 'C']}")
    for other in ["P06610", "Q8PAI2"]:
        s = seqs[other]
        aln = aligner.align(q, s)[0]
        # map query positions -> subject positions
        qmap = {}
        for (qs, qe), (ss, se) in zip(*aln.aligned):
            for k in range(qe - qs):
                qmap[qs + k] = ss + k
        ident = sum(1 for i, j in qmap.items() if q[i] == s[j])
        print(f"\n== Q8P365 vs {other} (length {len(s)}) ==")
        print(f"identity over aligned positions: {ident}/{len(qmap)} = {ident / len(qmap):.1%}")
        print(f"{other} cysteines at {[i + 1 for i, c in enumerate(s) if c == 'C']}")
        for i, c in enumerate(q):
            if c in "CWQN" and i in qmap and s[qmap[i]] == c and c != "N" or (c == "C" and i in qmap):
                print(f"  Q8P365 {c}{i + 1} <-> {other} {s[qmap[i]]}{qmap[i] + 1}" if c == "C" else "", end="")
                if c == "C":
                    print()
        for pos in [37, 71, 83, 143, 144]:
            i = pos - 1
            if i in qmap:
                print(f"  Q8P365 {q[i]}{pos} aligns to {other} {s[qmap[i]]}{qmap[i] + 1}")
        print(aln)


if __name__ == "__main__":
    main()
