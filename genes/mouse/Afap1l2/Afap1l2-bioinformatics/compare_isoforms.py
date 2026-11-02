"""Compare mouse Afap1l2 (Q5DTU0) with human AFAP1L2 (Q8N4X5) and map the
mouse construct used by Yamanaka et al. 2016 (NM_001177796 -> NP_001171267)
onto UniProt isoforms. Sequences are fetched live; nothing is hardcoded."""
import urllib.request
from Bio import Align
from Bio.Align import substitution_matrices


def fasta(url: str) -> str:
    txt = urllib.request.urlopen(url).read().decode()
    return "".join(line for line in txt.splitlines() if not line.startswith(">"))


up = "https://rest.uniprot.org/uniprotkb/{}.fasta"
seqs = {
    "mouse_Q5DTU0-1": fasta(up.format("Q5DTU0")),
    "mouse_Q5DTU0-2": fasta("https://rest.uniprot.org/uniprotkb/Q5DTU0-2.fasta"),
    "human_Q8N4X5-1": fasta(up.format("Q8N4X5")),
    "mouse_NP_001171267": fasta(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=NP_001171267&rettype=fasta&retmode=text"
    ),
}
for k, v in seqs.items():
    print(f"{k}\tlength={len(v)}")
print("NP_001171267 identical to Q5DTU0-2:", seqs["mouse_NP_001171267"] == seqs["mouse_Q5DTU0-2"])
print("NP_001171267 identical to Q5DTU0-1:", seqs["mouse_NP_001171267"] == seqs["mouse_Q5DTU0-1"])

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"
h, m = seqs["human_Q8N4X5-1"], seqs["mouse_Q5DTU0-1"]
aln = aligner.align(h, m)[0]
pairs = {}
ident = aligned = 0
for (hs, he), (ms, me) in zip(*aln.aligned):
    for i, j in zip(range(hs, he), range(ms, me)):
        pairs[i + 1] = j + 1
        aligned += 1
        ident += h[i] == m[j]
print(f"human vs mouse canonical: identical={ident} aligned={aligned} pct_identity_over_human={100*ident/len(h):.1f}")
for pos in (54,):
    mp = pairs.get(pos)
    print(f"human {h[pos-1]}{pos} -> mouse canonical {m[mp-1] if mp else '-'}{mp}")
# Construct residues 830-840 (Yamanaka F-actin-binding region) on NP_001171267
c = seqs["mouse_NP_001171267"]
seg = c[829:840]
off = m.find(seg)
print(f"construct 830-840 = {seg}; found in canonical at {off+1}-{off+len(seg)}" if off >= 0 else f"construct 830-840 = {seg}; not found in canonical")
print("human 48-60:", h[47:60], " mouse 48-60:", m[47:60])
