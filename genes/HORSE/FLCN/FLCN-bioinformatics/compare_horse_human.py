# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Global alignment of horse FLCN (A0A3Q2LPC0) to human FLCN (Q8NFG4); report identity and
conservation of experimentally defined human residues (UniProt SITE/MUTAGEN features)."""
import re
from pathlib import Path
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent


def read_seq(path: Path) -> str:
    text = path.read_text()
    block = text.split("\nSQ   ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", block)


def features(path: Path, kinds=("SITE", "MUTAGEN")):
    out = []
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"FT   (\w+)\s+(\d+)$", line)
        if m and m.group(1) in kinds:
            note = ""
            for nxt in lines[i + 1 : i + 4]:
                if '/note="' in nxt:
                    note = nxt.split('/note="')[1].rstrip('"')
                    break
            out.append((m.group(1), int(m.group(2)), note))
    return out


horse = read_seq(HERE.parent / "FLCN-uniprot.txt")
human_file = HERE / "human_Q8NFG4-uniprot.txt"
human = read_seq(human_file)

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aln = aligner.align(human, horse)[0]

hmap = {}
pairs = ident = 0
for (hs, he), (qs, qe) in zip(*aln.aligned):
    for k in range(he - hs):
        hmap[hs + k + 1] = qs + k + 1
        pairs += 1
        ident += human[hs + k] == horse[qs + k]

print(f"Horse A0A3Q2LPC0 length: {len(horse)}; human Q8NFG4 length: {len(human)}")
print(f"Aligned pairs: {pairs}; identical: {ident}; identity: {100*ident/pairs:.2f}%")
print(f"Coverage of human: {100*pairs/len(human):.2f}%; coverage of horse: {100*pairs/len(horse):.2f}%")
for kind, pos, note in features(human_file):
    hpos = hmap.get(pos)
    hres = horse[hpos - 1] if hpos else "-"
    print(f"{kind} human {human[pos-1]}{pos} -> horse {hres}{hpos if hpos else ''} ({note})")
Path(HERE / "alignment_rereview.txt").write_text(str(aln))
