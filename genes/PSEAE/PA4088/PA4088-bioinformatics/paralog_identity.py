"""Pairwise global identity among members of PANTHER node PTN000241400.

Fetches sequences live from UniProt REST and reports percent identity
(identical aligned positions / aligned columns without end gaps) using
Biopython's PairwiseAligner (BLOSUM62, gap open -10, extend -0.5).
Also reports the residue aligned to E. coli HemL Lys265 (PLP Schiff-base lysine).
Run: uv run python paralog_identity.py
"""
import urllib.request
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
import io

ACCS = {
    "P23893": "E. coli HemL",
    "P48247": "PAO1 HemL PA3977",
    "Q9HWU0": "PAO1 PA4088",
    "Q9HT50": "PAO1 PA5523",
    "Q89FR7": "B. japonicum blr6632",
    "Q89PD0": "B. japonicum blr3552",
}

# Other PAO1 class-III aminotransferases (outside PTHR43713), as a background
# for what "same fold, different enzyme" identity looks like.
BACKGROUND = {
    "Q9I693": "PAO1 BioA PA0420",
    "Q9I6J2": "PAO1 SpuC PA0299",
    "Q9I6M4": "PAO1 DavT PA0266",
    "O30508": "PAO1 AruC PA0895",
}


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as fh:
        return str(next(SeqIO.parse(io.StringIO(fh.read().decode()), "fasta")).seq)


def aligner():
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def identity(aln):
    s1, s2 = aln[0], aln[1]
    cols = [(x, y) for x, y in zip(s1, s2)]
    # trim end gaps
    while cols and ("-" in cols[0]):
        cols.pop(0)
    while cols and ("-" in cols[-1]):
        cols.pop()
    ident = sum(1 for x, y in cols if x == y and x != "-")
    return 100.0 * ident / len(cols) if cols else 0.0


def residue_at(aln, ref_pos):
    """Residue in seq 2 aligned to 1-based position ref_pos of seq 1."""
    i = 0
    for x, y in zip(aln[0], aln[1]):
        if x != "-":
            i += 1
            if i == ref_pos:
                return y
    return None


def main():
    seqs = {a: fetch(a) for a in ACCS}
    al = aligner()
    print("accession\tname\tlength")
    for a, n in ACCS.items():
        print(f"{a}\t{n}\t{len(seqs[a])}")
    print()
    print("pair\tpercent_identity")
    keys = list(ACCS)
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            aln = al.align(seqs[a], seqs[b])[0]
            print(f"{a}-{b}\t{identity(aln):.1f}")
    print()
    ref = seqs["P23893"]
    print(f"E. coli HemL residue 265: {ref[264]}")
    print("accession\tresidue aligned to E. coli HemL K265")
    for a in keys[1:]:
        aln = al.align(ref, seqs[a])[0]
        print(f"{a}\t{residue_at(aln, 265)}")
    print()
    print("background pair\tpercent_identity")
    for b, n in BACKGROUND.items():
        sb = fetch(b)
        for a in ("Q9HWU0", "P48247"):
            aln = al.align(seqs[a], sb)[0]
            print(f"{a}-{b} ({n})\t{identity(aln):.1f}")


if __name__ == "__main__":
    main()
