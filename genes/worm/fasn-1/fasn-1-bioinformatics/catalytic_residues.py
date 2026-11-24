"""Align C. elegans FASN-1 (P91871) to human FASN (P49327) and report whether the
catalytic / prosthetic-group residues annotated on human FASN (UniProt ACT_SITE and
MOD_RES features) are conserved at the aligned positions in FASN-1.

Inputs are the cached UniProt flat files in the repository; nothing is hardcoded
except the file paths. Run from the repository root:
    uv run python genes/worm/fasn-1/fasn-1-bioinformatics/catalytic_residues.py
"""
import re
import sys
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
WORM = ROOT / "genes/worm/fasn-1/fasn-1-uniprot.txt"
HUMAN = ROOT / "genes/human/FASN/FASN-uniprot.txt"


def features(path, keys=("ACT_SITE", "MOD_RES")):
    """Return list of (key, position, note) for single-residue features."""
    out = []
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"FT   (\S+)\s+(\d+)$", line)
        if m and m.group(1) in keys:
            note = ""
            for nxt in lines[i + 1 : i + 4]:
                n = re.search(r'/note="([^"]*)', nxt)
                if n:
                    note = n.group(1)
                    break
            out.append((m.group(1), int(m.group(2)), note))
    return out


def main():
    worm = str(SeqIO.read(WORM, "swiss").seq)
    human = str(SeqIO.read(HUMAN, "swiss").seq)
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aln = aligner.align(human, worm)[0]
    # map human positions -> worm positions
    hmap = {}
    for (hs, he), (ws, we) in zip(*aln.aligned):
        for k in range(he - hs):
            hmap[hs + k] = ws + k
    ident = sum(1 for h, w in hmap.items() if human[h] == worm[w])
    print(f"human FASN length {len(human)}, worm FASN-1 length {len(worm)}")
    print(f"aligned pairs {len(hmap)}, identical {ident} "
          f"({100*ident/len(hmap):.1f}% of aligned pairs)")
    print("\nhuman_feature\thuman_pos\thuman_res\tworm_pos\tworm_res\tconserved\tnote")
    for key, pos, note in features(HUMAN):
        if key == "MOD_RES" and "pantetheine" not in note:
            continue
        h0 = pos - 1
        w0 = hmap.get(h0)
        wres = worm[w0] if w0 is not None else "-"
        wpos = w0 + 1 if w0 is not None else "-"
        print(f"{key}\t{pos}\t{human[h0]}\t{wpos}\t{wres}\t{human[h0] == wres}\t{note}")


if __name__ == "__main__":
    sys.exit(main())
