"""Compare S. pombe eno102 (Q8NKC2) with its paralog eno101 (P40370).

Reads the two UniProt flat files fetched into the repo, performs a global
BLOSUM62 alignment, reports percent identity, and checks that the residues
UniProt annotates as active-site / substrate / Mg2+-binding in each entry
are identical and fall at aligned positions.

Run from the repo root:
    uv run --with biopython python genes/SCHPO/eno102/eno102-bioinformatics/compare_enolases.py
"""
import re
import sys
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
FILES = {
    "eno101": ROOT / "genes/SCHPO/eno101/eno101-uniprot.txt",
    "eno102": ROOT / "genes/SCHPO/eno102/eno102-uniprot.txt",
}


def parse(path):
    seq, on, sites = [], False, []
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"FT   (ACT_SITE|BINDING)\s+(\d+)(?:\.\.(\d+))?", line)
        if m:
            start = int(m.group(2))
            end = int(m.group(3) or start)
            sites.extend(range(start, end + 1))
        if line.startswith("SQ"):
            on = True
            continue
        if line.startswith("//"):
            break
        if on:
            seq.append(line.replace(" ", ""))
    return "".join(seq), sorted(set(sites))


def main():
    s1, sites1 = parse(FILES["eno101"])
    s2, sites2 = parse(FILES["eno102"])
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(s1, s2)[0]
    # map positions
    map12 = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for k in range(a1 - a0):
            map12[a0 + k + 1] = b0 + k + 1
    ident = sum(1 for p, q in map12.items() if s1[p - 1] == s2[q - 1])
    print(f"eno101 length {len(s1)}, eno102 length {len(s2)}")
    print(f"aligned pairs {len(map12)}, identical {ident}, "
          f"identity over eno101 length {ident / len(s1):.1%}")
    print("Annotated eno101 functional residues -> aligned eno102 residue:")
    ok = True
    for p in sites1:
        q = map12.get(p)
        r2 = s2[q - 1] if q else "-"
        same = q is not None and s1[p - 1] == r2
        ok &= same
        flag = "" if same else "  <-- DIFFERS"
        annotated = "annotated" if q in sites2 else "not annotated"
        print(f"  {s1[p-1]}{p} -> {r2}{q} ({annotated} in eno102){flag}")
    print("All annotated functional residues conserved:", ok)
    return 0


if __name__ == "__main__":
    sys.exit(main())
