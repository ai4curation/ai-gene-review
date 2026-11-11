# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.81", "requests"]
# ///
"""Compare Drosophila Pcf11 A1Z9W4 with other fly Pcf11 products and with
characterised yeast/human Pcf11 (same PANTHER subfamily PTHR15921:SF3).

Outputs (stdout, TSV-like sections):
  1. length and shared N-terminal prefix of fly Pcf11 products vs A1Z9W4
  2. local-alignment identity of the A1Z9W4 CID (InterPro IPR047415 17-149)
     and C-terminal region (from residue 1400) vs human O94913 / yeast P39081
  3. candidate C2H2-like zinc-finger motifs (C-x2-5-C-x(n)-H-x(n)-H scan) per
     protein, reported only as pattern matches

Run: uv run compare_pcf11.py > compare_pcf11.out.txt
"""

import re

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "A1Z9W4": "Drosophila Pcf11 long (reference proteome)",
    "Q8IGR2": "Drosophila Pcf11 573-aa product",
    "C0P8M6": "Drosophila Pcf11 86-aa product",
    "O94913": "Human PCF11",
    "P39081": "Yeast Pcf11",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def shared_prefix(a: str, b: str) -> int:
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


def local_identity(a: str, b: str) -> tuple[float, int, float]:
    aligner = Align.PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    ident = 0
    cols = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            cols += 1
            ident += a[i] == b[j]
    return aln.score, cols, (100.0 * ident / cols if cols else 0.0)


ZNF = re.compile(r"C.{2,5}C.{8,16}H.{2,6}H")


def main() -> None:
    seqs = {acc: fetch(acc) for acc in ACCS}
    ref = seqs["A1Z9W4"]
    print("## 1. Fly Pcf11 products vs A1Z9W4")
    print("accession\tdescription\tlength\tshared_N_terminal_prefix_with_A1Z9W4")
    for acc, desc in ACCS.items():
        if acc.startswith(("A1Z", "Q8I", "C0P")):
            print(f"{acc}\t{desc}\t{len(seqs[acc])}\t{shared_prefix(ref, seqs[acc])}")
    # Is the 573-aa product a contiguous substring of A1Z9W4 apart from its tail?
    q = seqs["Q8IGR2"]
    print(f"Q8IGR2 is exact substring of A1Z9W4: {q in ref}")

    print("\n## 2. Local alignment of A1Z9W4 regions vs characterised orthologs")
    print("region\tpartner\tscore\taligned_columns\tpercent_identity")
    regions = {"CID_17-149": ref[16:149], "Cterm_1400-end": ref[1399:]}
    for rname, rseq in regions.items():
        for partner in ("O94913", "P39081"):
            score, cols, pid = local_identity(rseq, seqs[partner])
            print(f"{rname}\t{partner}\t{score:.1f}\t{cols}\t{pid:.1f}")

    print("\n## 3. C2H2-like pattern matches (C-x2-5-C-x8-16-H-x2-6-H)")
    print("accession\tstart\tend\tmatch")
    for acc in ("A1Z9W4", "O94913", "P39081"):
        for m in ZNF.finditer(seqs[acc]):
            print(f"{acc}\t{m.start() + 1}\t{m.end()}\t{m.group()}")


if __name__ == "__main__":
    main()
