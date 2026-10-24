# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Global alignment (BLOSUM62) of Q7SAD4 against human FMO3 (P31513), reporting the
Q7SAD4 residues aligned to FMO3 motif positions (FAD GxGxxG 9-14, FMO motif 166-176,
NADPH GxGxxG 191-196, FATGY 327-331) and overall identity."""
import re
import urllib.request
from pathlib import Path
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent


def seq_from_flatfile(text: str) -> str:
    s = text.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", s)


def fetch(acc: str) -> str:
    txt = urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").read().decode()
    return "".join(txt.splitlines()[1:])


q = seq_from_flatfile((HERE.parent / "NCU06296-uniprot.txt").read_text())
t = fetch("P31513")
al = Align.PairwiseAligner(mode="global", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                           open_gap_score=-10, extend_gap_score=-0.5)
a = al.align(t, q)[0]
# map FMO3 position -> Q7SAD4 position
m = {}
for (ts, te), (qs, qe) in zip(*a.aligned):
    for k in range(te - ts):
        m[ts + k + 1] = qs + k + 1
ident = sum(1 for i, j in m.items() if t[i - 1] == q[j - 1])
print(f"aligned pairs: {len(m)}; identical: {ident}; identity over aligned pairs: {ident/len(m):.3f}")
for name, (s, e) in {"FAD GxGxxG": (9, 14), "FMO motif FxGxxxHxxxY": (166, 176),
                     "NADPH GxGxxG": (191, 196), "FATGY": (327, 331)}.items():
    fm = t[s - 1:e]
    qq = "".join(q[m[i] - 1] if i in m else "-" for i in range(s, e + 1))
    qpos = [m.get(i) for i in (s, e)]
    print(f"{name}: FMO3 {s}-{e} {fm} -> Q7SAD4 {qpos} {qq}")
