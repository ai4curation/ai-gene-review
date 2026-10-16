"""AKAP12: test whether the reported PKC-binding motifs coincide with the
UniProt-annotated AKAP CaM-binding (WSK / WXSXK) motifs in the HUMAN sequence.

Reported PKC-binding motifs (PMID:21903576, Gelman lab, rodent SSeCKS numbering):
    consensus EG(I/V)(T/S)XWXSFK(K/R)(M/L)VTP(K/R)K(K/R)X(K/R)XXXEXXXE(E/D)
    at aa 592-620 and 741-769.

UniProt human Q02952 MOTIF lines (PROSITE-ProRule PRU01241 "AKAP CaM-binding"):
    607..627, 756..776, 801..821.

This script does NOT assume the numbering transfers; it searches the human
sequence with the published regex and reports where it actually matches.
"""
import re
import sys
from pathlib import Path


def load_seq(path):
    txt = Path(path).read_text()
    seq_block = txt.split("\nSQ   ", 1)[1]
    lines = seq_block.splitlines()[1:]
    return "".join(ln.replace(" ", "") for ln in lines if not ln.startswith("//"))


# Gelman consensus translated to a regex.
PKC_MOTIF = re.compile(r"EG[IV][TS].W.SFK[KR][ML]VTP[KR]K[KR].[KR]...E...E[ED]")
# The WSK motif core that PROSITE PRU01241 is built around.
WSK_CORE = re.compile(r"W.S.K")

UNIPROT_CAM_MOTIFS = [(607, 627), (756, 776), (801, 821)]

if __name__ == "__main__":
    seq = load_seq(sys.argv[1] if len(sys.argv) > 1 else
                   "genes/human/AKAP12/AKAP12-uniprot.txt")
    print(f"human Q02952 length = {len(seq)}  (UniProt header says 1782)")
    assert len(seq) == 1782, f"sequence length {len(seq)} != 1782 — parse error"

    print("\n-- PKC-binding consensus (PMID:21903576) matches in HUMAN AKAP12 --")
    hits = [(m.start() + 1, m.end(), m.group()) for m in PKC_MOTIF.finditer(seq)]
    if not hits:
        print("  none (exact consensus does not match the human sequence)")
    for s, e, g in hits:
        print(f"  {s}-{e}  {g}")

    print("\n-- W.S.K (WSK) core occurrences --")
    for m in WSK_CORE.finditer(seq):
        s, e = m.start() + 1, m.end()
        inside = [f"{a}-{b}" for a, b in UNIPROT_CAM_MOTIFS if a <= s <= b]
        print(f"  {s}-{e}  {m.group()}   inside UniProt CaM motif: {inside or 'NO'}")

    print("\n-- UniProt-annotated AKAP CaM-binding motif sequences --")
    for a, b in UNIPROT_CAM_MOTIFS:
        print(f"  {a}-{b}: {seq[a - 1:b]}")

    print("\n-- windows named by PMID:21903576 (rodent numbering), shown on human seq --")
    for a, b in [(592, 620), (741, 769)]:
        print(f"  {a}-{b}: {seq[a - 1:b]}")
