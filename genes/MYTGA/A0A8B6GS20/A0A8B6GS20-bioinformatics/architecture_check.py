# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Compare A0A8B6GS20 against characterised MTMR9 (SF56 human, SF73 worm) and
active MTMR6 (control). Reports local-alignment coverage of each reference and
the residues aligned to the reference catalytic Cys/Arg of the C(X)5R motif."""
import re
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"target": "A0A8B6GS20", "MTMR9_HUMAN": "Q96QG7",
        "MTM9_CAEEL": "Q965W9", "MTMR6_HUMAN": "Q9Y217"}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


seqs = {k: fetch(v) for k, v in ACCS.items()}
t = seqs["target"]
print(f"target {ACCS['target']} length {len(t)}")
aligner = Align.PairwiseAligner(mode="local")
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -11
aligner.extend_gap_score = -1

for name in ["MTMR9_HUMAN", "MTM9_CAEEL", "MTMR6_HUMAN"]:
    ref = seqs[name]
    aln = aligner.align(t, ref)[0]
    tb, rb = aln.aligned
    t_start, t_end = tb[0][0] + 1, tb[-1][1]
    r_start, r_end = rb[0][0] + 1, rb[-1][1]
    mapping = {}
    ident = pairs = 0
    for (ts, te), (rs, re_) in zip(tb, rb):
        for i, j in zip(range(ts, te), range(rs, re_)):
            mapping[j] = i
            pairs += 1
            ident += t[i] == ref[j]
    # catalytic motif position in reference: [VI]H[CG]S[DE]G[WF]D followed by R/T; use the HxSxGxD core
    m = re.search(r"[VI]H[CG]S[DE]G[WF]D", ref)
    print(f"\n{name} ({ACCS[name]}, length {len(ref)}): score {aln.score:.0f}")
    print(f"  target {t_start}-{t_end} aligned to reference {r_start}-{r_end}")
    print(f"  reference coverage {pairs / len(ref):.1%}; identity over aligned pairs {ident / pairs:.1%}")
    if m:
        cpos = m.start() + 2  # Cys (or Gly) position, 0-based
        rpos = cpos + 6       # Arg of C(X)5R
        ref_motif = ref[m.start():m.start() + 10]
        tgt = "".join(t[mapping[j]] if j in mapping else "-" for j in range(m.start(), m.start() + 10))
        print(f"  reference motif at {m.start() + 1}: {ref_motif}  (C-pos residue {ref[cpos]}{cpos + 1}, R-pos residue {ref[rpos]}{rpos + 1})")
        print(f"  target residues aligned to motif: {tgt}")
    print("  reference N-terminal residues 1-%d not covered by the target alignment" % (r_start - 1))

# Reference residues aligned to the target's own motif-like segment (position of
# the residue aligned to the MTMR6 catalytic Cys, plus 9 residues)
tm = re.search(r"VH[A-Z]S[A-Z]G[A-Z]D", t)
print(f"\ntarget motif-like segment at {tm.start() + 1}: {t[tm.start():tm.start() + 10]}")
for name in ["MTMR9_HUMAN", "MTM9_CAEEL", "MTMR6_HUMAN"]:
    ref = seqs[name]
    aln = aligner.align(t, ref)[0]
    tmap = {}
    for (ts, te), (rs, re_) in zip(*aln.aligned):
        for i, j in zip(range(ts, te), range(rs, re_)):
            tmap[i] = j
    seg = "".join(ref[tmap[i]] if i in tmap else "-" for i in range(tm.start(), tm.start() + 10))
    first = tmap.get(tm.start())
    print(f"  {name}: {seg} (starting at reference residue {first + 1 if first is not None else 'NA'})")

# Residues of the target that precede any MTMR alignment
print(f"\ntarget residues 1-{361} lie upstream of the region homologous to MTMR9")
