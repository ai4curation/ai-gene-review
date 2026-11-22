"""Compare bonobo A0A2R9CAF4 with human SLC26A11 (Q86WA9) and mouse Slc26a11 (Q80ZD3).

Reports global identity, length, and conservation of residues highlighted in the
human SLC26A11 structure/function study (PMID:42509233), notably Glu-320.

Run: uv run python compare_to_human_rereview.py
"""

import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent
TARGET_TXT = HERE.parent / "A0A2R9CAF4-uniprot.txt"


def seq_from_flatfile(text: str) -> str:
    lines = text.splitlines()
    i = next(n for n, line in enumerate(lines) if line.startswith("SQ "))
    out = []
    for line in lines[i + 1 :]:
        if line.startswith("//"):
            break
        out.append(line.replace(" ", ""))
    return "".join(out)


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as fh:
        fasta = fh.read().decode()
    return "".join(fasta.splitlines()[1:])


def align(a: str, b: str):
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    return aligner.align(a, b)[0]


def identity(aln) -> tuple[int, int]:
    s1, s2 = aln[0], aln[1]
    cols = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    return sum(x == y for x, y in cols), len(cols)


def map_position(aln, ref_pos: int) -> tuple[int | None, str]:
    """Map 1-based position in sequence 2 (reference) to sequence 1 (target)."""
    s1, s2 = aln[0], aln[1]
    i1 = i2 = 0
    for x, y in zip(s1, s2):
        if x != "-":
            i1 += 1
        if y != "-":
            i2 += 1
            if i2 == ref_pos:
                return (i1 if x != "-" else None), x
    return None, "-"


def main() -> None:
    target = seq_from_flatfile(TARGET_TXT.read_text())
    print(f"A0A2R9CAF4 length: {len(target)}")
    for acc in ["Q86WA9", "Q80ZD3"]:
        ref = fetch(acc)
        aln = align(target, ref)
        ident, cols = identity(aln)
        print(f"{acc} length: {len(ref)}; identical {ident}/{cols} aligned "
              f"({100 * ident / cols:.1f}%); exact match: {target == ref}")
        if acc == "Q86WA9":
            pos, res = map_position(aln, 320)
            print(f"  human Q86WA9 residue 320 = {ref[319]}; "
                  f"bonobo aligned position {pos} = {res}")


if __name__ == "__main__":
    main()
