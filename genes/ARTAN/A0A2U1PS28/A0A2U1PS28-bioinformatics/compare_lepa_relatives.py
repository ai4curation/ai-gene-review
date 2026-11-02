"""Global pairwise identity of A0A2U1PS28 to characterised LepA/GUF1 relatives.

Fetches sequences from UniProt REST, aligns with Biopython PairwiseAligner
(BLOSUM62, gap open -10, extend -0.5) and reports identity over aligned
columns, plus N-terminal extension relative to E. coli LepA and the
composition of the N-terminal 60 residues (transit-peptide-like features).
"""
import urllib.request
from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "A0A2U1PS28"
RELATIVES = {
    "Q9FNM5": "Arabidopsis cpLEPA At5g08650 (PTHR43512:SF4)",
    "P60785": "E. coli LepA (PTHR43512:SF4)",
    "Q9FLE4": "Arabidopsis mitochondrial GUF1 At5g39900 (PTHR43512:SF7)",
    "P46943": "S. cerevisiae Guf1 (PTHR43512:SF7)",
    "Q8N442": "Human GUF1 (PTHR43512:SF7)",
}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    text = urllib.request.urlopen(url).read().decode()
    return "".join(text.splitlines()[1:])


def identity(a: str, b: str) -> tuple[float, int]:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    s1, s2 = aln[0], aln[1]
    cols = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    ident = sum(1 for x, y in cols if x == y)
    return 100.0 * ident / len(cols), len(cols)


def main() -> None:
    tseq = fetch(TARGET)
    print(f"{TARGET} length {len(tseq)}")
    for acc, desc in RELATIVES.items():
        s = fetch(acc)
        pid, n = identity(tseq, s)
        print(f"{acc}\t{desc}\tlen={len(s)}\tidentity={pid:.1f}% over {n} aligned columns")
    nterm = tseq[:60]
    st = sum(nterm.count(c) for c in "ST")
    acid = sum(nterm.count(c) for c in "DE")
    basic = sum(nterm.count(c) for c in "KR")
    print(f"N-terminal 60 aa: {nterm}")
    print(f"  Ser+Thr={st} ({100*st/60:.0f}%), Asp+Glu={acid}, Lys+Arg={basic}")
    i = tseq.find("DTPGH")
    print(f"DTPGH (G3/switch II) motif at {i+1}-{i+5}; catalytic His at {i+5}")
    j = tseq.find("GHVDFS")
    print(f"GHVDFS at {j+1}")


if __name__ == "__main__":
    main()
