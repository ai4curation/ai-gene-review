"""Scan S. rosetta Yorkie homolog F2UDK1 for Warts/LATS HXRXXS motifs and
compare its N-terminal region with the TEAD-binding domain of human YAP1 and
Drosophila Yorkie by local alignment.

Run from the repository root:  uv run python genes/SALRS/yorkie/yorkie-bioinformatics/motif_scan.py
Sequences are fetched live from the UniProt REST API.
"""
import re
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    txt = urllib.request.urlopen(url).read().decode()
    return "".join(txt.split("\n")[1:])


sr = fetch("F2UDK1")   # S. rosetta PTSG_06057
yap = fetch("P46937")  # human YAP1
yki = fetch("Q45VV3")  # Drosophila Yorkie
print(f"F2UDK1 length: {len(sr)}")

print("\n## HXRXXS/T (Warts/LATS consensus) motifs in F2UDK1")
for m in re.finditer(r"(?=(H.R..[ST]))", sr):
    s = m.start()
    print(f"  {s + 1}-{s + 6}  {m.group(1)}  phosphoacceptor {m.group(1)[-1]}{s + 6}  context {sr[max(0, s - 3):s + 10]}")
for name, seq in [("YAP1 (reference)", yap), ("Yki (reference)", yki)]:
    print(f"  {name}: {[(m.start() + 6, m.group(1)) for m in re.finditer(r'(?=(H.R..[ST]))', seq)]}")

print("\n## Short TEAD-interface motifs (YAP alpha1 'LxxLF', omega-loop 'PxxFF')")
for pat in [r"L..LF", r"P.[ST]FF", r"SFF"]:
    print(f"  {pat}: F2UDK1 {[(m.start() + 1, m.group()) for m in re.finditer(pat, sr)]}"
          f"  YAP1 {[(m.start() + 1, m.group()) for m in re.finditer(pat, yap)]}"
          f"  Yki {[(m.start() + 1, m.group()) for m in re.finditer(pat, yki)]}")

al = Align.PairwiseAligner()
al.mode = "local"
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10
al.extend_gap_score = -0.5
print("\n## Local alignment of YAP1/Yki TEAD-binding regions to F2UDK1 1-188 (N-terminal to WW1)")
for name, q in [("YAP1 50-100", yap[49:100]), ("Yki 20-80", yki[19:80])]:
    a = al.align(q, sr[:188])[0]
    print(f"{name}: score {a.score}")
    print(a)
# control: same query against an unrelated region of F2UDK1 (500-714)
for name, q in [("YAP1 50-100 vs F2UDK1 500-714 (control)", yap[49:100])]:
    a = al.align(q, sr[499:])[0]
    print(f"{name}: score {a.score}")

# ---------------------------------------------------------------------------
# Which S. rosetta protein is the Yorkie ortholog?  PANTHER places F2UDK1 in
# PTHR10316 (MAGI-related) while another S. rosetta WW protein, F2U5K0
# (PTSG_03848), is classified in PTHR17616 (YAP1 family). Compare both against
# YAP1, Yorkie and Capsaspora coYki by full-length local alignment, with a
# shuffled-sequence control (same composition) for each pair.
import random

other = fetch("F2U5K0")  # S. rosetta PTSG_03848
coyki = fetch("A0A0D2WY30")  # Capsaspora coYki
print("\n## HXRXXS/T motifs in F2U5K0 (PTSG_03848)")
print("  ", [(m.start() + 6, m.group(1)) for m in re.finditer(r"(?=(H.R..[ST]))", other)])
random.seed(0)
print("\n## Full-length local alignment scores (BLOSUM62, gap -10/-0.5); shuffled control = mean of 20 shuffles of the S. rosetta sequence")
for qname, q in [("YAP1", yap), ("Yki", yki), ("coYki", coyki)]:
    for tname, t in [("F2UDK1", sr), ("F2U5K0", other)]:
        real = al.score(q, t)
        shuf = []
        for _ in range(20):
            lst = list(t)
            random.shuffle(lst)
            shuf.append(al.score(q, "".join(lst)))
        print(f"  {qname:6s} vs {tname}: score {real:.1f}  shuffled mean {sum(shuf) / len(shuf):.1f}  max {max(shuf):.1f}")
