# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83"]
# ///
"""Align the donkey canonical CADM1 product (A0A9L0IJE9) to reviewed human (Q9BY67)
and mouse (Q8R5M8) CADM1, and report identity per human topological region.

Run from this folder:
  uv run --script compare_canonical_to_orthologs.py

Global alignment, Biopython PairwiseAligner, BLOSUM62, gap open -10, gap extend -0.5.
Region boundaries are read from the human UniProt flat file at run time.
"""
import re
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent


def uniprot_seq(path: Path) -> str:
    seq, in_sq = [], False
    for line in path.read_text().splitlines():
        if line.startswith("SQ"):
            in_sq = True
            continue
        if in_sq:
            if line.startswith("//"):
                break
            seq.append(line.replace(" ", "").strip())
    return "".join(seq)


def fasta_seq(path: Path) -> str:
    return "".join(l.strip() for l in path.read_text().splitlines() if not l.startswith(">"))


def human_regions(path: Path) -> list[tuple[str, int, int]]:
    regions = []
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"FT   (SIGNAL|TOPO_DOM|TRANSMEM|DOMAIN)\s+(\d+)\.\.(\d+)", line)
        if m:
            note = ""
            if i + 1 < len(lines) and "/note=" in lines[i + 1]:
                note = lines[i + 1].split('"')[1]
            regions.append((f"{m.group(1)} {note}".strip(), int(m.group(2)), int(m.group(3))))
    return regions


def mapping(a: str, b: str):
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    pairs = {}
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for k in range(e1 - s1):
            pairs[s2 + k + 1] = s1 + k + 1  # human pos -> donkey pos (1-based)
    return pairs


def main() -> None:
    donkey = uniprot_seq(HERE.parent / "CADM1__A0A9L0IJE9-uniprot.txt")
    human = fasta_seq(HERE / "human-CADM1-Q9BY67.fasta")
    mouse = fasta_seq(HERE / "mouse-Cadm1-Q8R5M8.fasta")
    print(f"Donkey A0A9L0IJE9: {len(donkey)} aa; C-terminal 4 residues: {donkey[-4:]}")
    print(f"Human Q9BY67: {len(human)} aa; C-terminal 4 residues: {human[-4:]}")
    print(f"Mouse Q8R5M8: {len(mouse)} aa; C-terminal 4 residues: {mouse[-4:]}")
    for name, other in [("human Q9BY67", human), ("mouse Q8R5M8", mouse)]:
        pairs = mapping(donkey, other)
        ident = sum(1 for h, d in pairs.items() if other[h - 1] == donkey[d - 1])
        print(f"vs {name}: paired {len(pairs)}, identical {ident}, "
              f"identity over paired {100 * ident / len(pairs):.2f}%")
    pairs = mapping(donkey, human)
    print("Per-region identity, human Q9BY67 coordinates:")
    for label, s, e in human_regions(HERE / "human-CADM1-Q9BY67-uniprot.txt"):
        span = range(s, e + 1)
        paired = [h for h in span if h in pairs]
        ident = sum(1 for h in paired if human[h - 1] == donkey[pairs[h] - 1])
        print(f"  {label} {s}..{e}: {len(paired)}/{len(span)} aligned, {ident} identical")
    cyto = [r for r in human_regions(HERE / "human-CADM1-Q9BY67-uniprot.txt")
            if r[0].startswith("TOPO_DOM Cytoplasmic")][0]
    hs = human[cyto[1] - 1: cyto[2]]
    ds = "".join(donkey[pairs[h] - 1] if h in pairs else "-" for h in range(cyto[1], cyto[2] + 1))
    print(f"Human cytoplasmic tail : {hs}")
    print(f"Donkey aligned residues: {ds}")


if __name__ == "__main__":
    main()
