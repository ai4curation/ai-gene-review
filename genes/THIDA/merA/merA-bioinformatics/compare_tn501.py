"""Align Thiobacillus denitrificans MerA (Q3SJ73) with Tn501 MerA (P00392).

Reports global identity and which Q3SJ73 residues align to the experimentally
characterised Tn501 catalytic cysteines and NmerA GMTCXXC motif. Also reports
global identity to the two non-MerA PTHR43014 subfamily representatives that the
committed family entry list names: P9WHH7 (M. tuberculosis LpdA, PTHR43014:SF1,
the IBD seed for GO:0003955) and P77212 (E. coli RclA, PTHR43014:SF4).
Run: uv run python genes/THIDA/merA/merA-bioinformatics/compare_tn501.py
"""
import re
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices


def fasta(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    txt = urllib.request.urlopen(url).read().decode()
    return "".join(txt.split("\n")[1:])


al = Align.PairwiseAligner()
al.mode = "global"
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10
al.extend_gap_score = -0.5


def align(query, target):
    """Return (alignment, target_pos -> query_pos map, aligned, identical)."""
    aln = al.align(query, target)[0]
    pos_map = {}
    ident = aligned = 0
    for (qs, qe), (ts, te) in zip(*aln.aligned):
        for i in range(qe - qs):
            pos_map[ts + i + 1] = qs + i + 1
            aligned += 1
            ident += query[qs + i] == target[ts + i]
    return aln, pos_map, aligned, ident


def find_once(pattern, seq, what):
    """Locate an anchored motif, failing loudly unless it occurs exactly once."""
    hits = [m.start() for m in re.finditer(pattern, seq)]
    if len(hits) != 1:
        raise SystemExit(
            f"expected exactly one {what} ({pattern}) in the sequence, found {len(hits)}"
        )
    return hits[0]


q = fasta("Q3SJ73")
t = fasta("P00392")
print(f"Q3SJ73 length {len(q)}; P00392 (Tn501 MerA) length {len(t)}")

_, t2q, aligned, ident = align(q, t)
print(f"aligned positions {aligned}; identical {ident}; identity {100*ident/aligned:.1f}% of aligned")

# Non-MerA PTHR43014 subfamily representatives, for comparison with the MerA reference.
for acc, label in (
    ("P9WHH7", "M. tuberculosis LpdA, PTHR43014:SF1, GO:0003955 IBD seed"),
    ("P77212", "E. coli RclA, PTHR43014:SF4"),
):
    o = fasta(acc)
    _, _, oaligned, oident = align(q, o)
    print(
        f"Q3SJ73 vs {acc} ({label}): length {len(o)}; aligned {oaligned}; "
        f"identical {oident}; identity {100*oident/oaligned:.1f}% of aligned"
    )

# Tn501 landmarks: locate in the P00392 sequence by anchored motif rather than hard-coding numbers
landmarks = {}
s = find_once(r"GMTC..C", t, "NmerA GMTCxxC motif")
landmarks["NmerA GMTCxxC first Cys"] = s + 4
landmarks["NmerA GMTCxxC second Cys"] = s + 7
s = find_once(r"CVNVGC", t, "redox-active CVNVGC motif")
landmarks["redox-active disulfide Cys1"] = s + 1
landmarks["redox-active disulfide Cys2"] = s + 6
for pos in (558, 559):
    if t[pos - 1] != "C":
        raise SystemExit(f"P00392 position {pos} is {t[pos-1]}, not the expected Cys")
    landmarks[f"Tn501 Cys{pos} (C-terminal pair)"] = pos
for name, tp in landmarks.items():
    qp = t2q.get(tp)
    print(f"{name}: P00392 {t[tp-1]}{tp} -> Q3SJ73 " + (f"{q[qp-1]}{qp}" if qp else "gap"))
