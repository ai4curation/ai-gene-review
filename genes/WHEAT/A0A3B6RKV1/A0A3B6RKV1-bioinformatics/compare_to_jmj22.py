"""Align wheat A0A3B6RKV1 to Arabidopsis JMJ22 (Q67XX3) and human JMJD8 (Q96S16).

Maps the JMJ22 Fe(II)-binding residues (UniProt Q67XX3 FT BINDING 324, 326, 407)
and the JMJ22 F-box/JmjC domain boundaries onto the wheat sequence, and reports
global identity. Sequences are fetched live from UniProt REST.

Run: uv run --with biopython --with requests python compare_to_jmj22.py
"""

import requests
from Bio import Align
from Bio.Align import substitution_matrices


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def align(a: str, b: str):
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    return aligner.align(a, b)[0]


def pos_map(aln) -> dict[int, int]:
    """Map 1-based positions in target (seq 0) to query (seq 1)."""
    m = {}
    for (s0, e0), (s1, e1) in zip(*aln.aligned):
        for i in range(e0 - s0):
            m[s0 + i + 1] = s1 + i + 1
    return m


def identity(aln) -> tuple[int, int]:
    ident = 0
    cols = 0
    for (s0, e0), (s1, e1) in zip(*aln.aligned):
        for i in range(e0 - s0):
            cols += 1
            ident += aln.target[s0 + i] == aln.query[s1 + i]
    return ident, cols


wheat = fetch("A0A3B6RKV1")
for acc, label, sites, domains in [
    ("Q67XX3", "AtJMJ22", [324, 326, 407], {"F-box": (80, 126), "JmjC": (279, 439)}),
    ("Q96S16", "HsJMJD8", [], {}),
]:
    other = fetch(acc)
    aln = align(other, wheat)
    ident, cols = identity(aln)
    print(f"== {label} {acc} (len {len(other)}) vs A0A3B6RKV1 (len {len(wheat)})")
    print(f"aligned columns {cols}, identical {ident} ({100 * ident / cols:.1f}% of aligned)")
    m = pos_map(aln)
    for p in sites:
        w = m.get(p)
        print(f"  {label} {other[p - 1]}{p} -> wheat {wheat[w - 1] + str(w) if w else 'gap'}")
    for name, (s, e) in domains.items():
        print(f"  {label} {name} {s}-{e} -> wheat {m.get(s)}-{m.get(e)}")
        sub = [(p, m[p]) for p in range(s, e + 1) if p in m]
        same = sum(other[p - 1] == wheat[q - 1] for p, q in sub)
        print(f"    domain identity {same}/{e - s + 1} ({100 * same / (e - s + 1):.1f}%)")
