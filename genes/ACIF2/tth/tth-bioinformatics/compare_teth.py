"""Compare the four CMMMech TetH/Tth UniProt entries against each other and
against experimentally characterised TetH sequences, and examine the
A. thiooxidans ATCC 19377 tth locus for a split/fragmented gene model.

All sequences are fetched live (UniProt REST, NCBI E-utilities); nothing is
hard-coded except accessions and coordinates taken from the GenBank records.
Run:  uv run python compare_teth.py > results.txt
"""
import io
import time
import urllib.request

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.Seq import Seq

UNIPROT = {
    "B7J3C9 (A. ferrooxidans ATCC 23270, Af-Tth, Swiss-Prot)": "B7J3C9",
    "F9ZNI0 (A. caldus SM-1, Atc_1595)": "F9ZNI0",
    "A0A060URH6 (A. ferrivorans, tetH)": "A0A060URH6",
    "A0A5P9XPU3 (A. thiooxidans ATCC 19377, GCD22_00683)": "A0A5P9XPU3",
    # full-length tth copy elsewhere in the same ATCC 19377 genome (CP045571.1:2055336..2056847)
    "A0A5P9XS05 (A. thiooxidans ATCC 19377, GCD22_02315)": "A0A5P9XS05",
}
NCBI_PROT = {
    "ABP38225 (A. caldus KU/ATCC 51756 TetH, Rzhepishevska 2007)": "ABP38225",
    "QFX95165 (A. thiooxidans ATCC 19377, GCD22_00682)": "QFX95165",
    # A. ferrivorans SS3 tetH1 (Acife_0037) and tetH2 (Acife_2602), Liljeqvist 2013 / Christel 2016
    "AEM46280 (A. ferrivorans SS3 tetH1, Acife_0037)": "AEM46280",
    "AEM48684 (A. ferrivorans SS3 tetH2, Acife_2602)": "AEM48684",
}
# GCD22_00681 (IS5 transposase) ends at 618910 (complement); GCD22_00683 ends at 620560;
# the window is extended 2000 nt downstream to look for the missing C-terminal region.
REGION = ("CP045571.1", 618911, 622560)
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def get(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode()


def uniprot_seq(acc):
    txt = get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
    return str(next(SeqIO.parse(io.StringIO(txt), "fasta")).seq)


def ncbi_prot(acc):
    time.sleep(0.4)
    txt = get(f"{EUTILS}?db=protein&id={acc}&rettype=fasta&retmode=text")
    return str(next(SeqIO.parse(io.StringIO(txt), "fasta")).seq)


def ncbi_nuc(acc, start, stop):
    time.sleep(0.4)
    txt = get(f"{EUTILS}?db=nuccore&id={acc}&rettype=fasta&retmode=text"
              f"&seq_start={start}&seq_stop={stop}")
    return str(next(SeqIO.parse(io.StringIO(txt), "fasta")).seq)


def aligner(mode="global"):
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = mode
    return a


def identity(s1, s2, mode="global"):
    aln = aligner(mode).align(s1, s2)[0]
    ident = aligned = 0
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for i, j in zip(range(a0, a1), range(b0, b1)):
            aligned += 1
            ident += s1[i] == s2[j]
    return ident, aligned, aln


def map_residue(ref, other, pos):
    """Return residue in `other` aligned to 1-based position `pos` of `ref`."""
    aln = aligner("global").align(ref, other)[0]
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        if a0 <= pos - 1 < a1:
            j = b0 + (pos - 1 - a0)
            return f"{other[j]}{j + 1}"
    return "gap"


def main():
    seqs = {k: uniprot_seq(v) for k, v in UNIPROT.items()}
    seqs.update({k: ncbi_prot(v) for k, v in NCBI_PROT.items()})
    names = list(seqs)
    print("## Sequence lengths and N-termini")
    for n in names:
        print(f"- {n}: {len(seqs[n])} aa; N-term {seqs[n][:40]}")
    ref = seqs[names[0]]
    print("\n## Global identity to B7J3C9 (identical/aligned positions; coverage of B7J3C9)")
    for n in names[1:]:
        i, al, _ = identity(ref, seqs[n])
        print(f"- {n}: {i}/{al} = {100*i/al:.1f}% identity; covers {100*al/len(ref):.1f}% of B7J3C9")
    print("\n## Pairwise global identities (all vs all)")
    for x in range(len(names)):
        for y in range(x + 1, len(names)):
            i, al, _ = identity(seqs[names[x]], seqs[names[y]])
            print(f"- {names[x].split()[0]} vs {names[y].split()[0]}: {100*i/al:.1f}% over {al} aligned")
    print("\n## Residue aligned to B7J3C9 Asp325 (catalytic acid, Kanao 2021) and Cys301")
    print(f"- B7J3C9 residue 325 = {ref[324]}, residue 301 = {ref[300]}")
    for n in names[1:]:
        print(f"- {n}: D325 -> {map_residue(ref, seqs[n], 325)}; C301 -> {map_residue(ref, seqs[n], 301)}")
    print("\n## A. thiooxidans ATCC 19377 locus CP045571.1:%d-%d (forward strand)" % REGION[1:])
    nuc = ncbi_nuc(*REGION)
    print(f"- region length {len(nuc)} nt")
    for frame in range(3):
        sub = nuc[frame:]
        sub = sub[: len(sub) - len(sub) % 3]
        prot = str(Seq(sub).translate())
        print(f"- frame +{frame}:")
        offset = 0
        for frag in prot.split("*"):
            if len(frag) >= 40:
                i, al, aln = identity(ref, frag, mode="local")
                if al >= 30 and i / al >= 0.35:
                    rs, re_ = aln.aligned[0][0][0] + 1, aln.aligned[0][-1][1]
                    nt0 = REGION[1] + frame + 3 * (offset + aln.aligned[1][0][0])
                    print(f"  - stop-free segment of {len(frag)} aa (starts ~nt {REGION[1] + frame + 3*offset}): "
                          f"{i}/{al} identical ({100*i/al:.0f}%) to B7J3C9 {rs}-{re_}; first aligned codon at nt {nt0}")
            offset += len(frag) + 1


if __name__ == "__main__":
    main()
