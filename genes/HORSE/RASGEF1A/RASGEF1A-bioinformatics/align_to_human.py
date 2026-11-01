# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Global alignment of horse RASGEF1A (A0A9L0R5H6) to human RASGEF1A (Q8N9B8).

Reads sequences from the local UniProt flat files and reports identity,
the human Met1 position in the horse model, and per-domain identity using
the domain boundaries annotated in the human Swiss-Prot entry.
"""
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent
HORSE = HERE.parent / "RASGEF1A-uniprot.txt"
HUMAN = HERE / "RASGEF1A-human-Q8N9B8-uniprot.txt"
# Human domain boundaries from Q8N9B8 FT lines (PROSITE-ProRule)
HUMAN_DOMAINS = {"N-terminal Ras-GEF (REM)": (41, 170), "Ras-GEF catalytic": (214, 461)}


def read_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("SQ "))
    seq = []
    for l in lines[start + 1 :]:
        if l.startswith("//"):
            break
        seq.append(l.replace(" ", ""))
    return "".join(seq)


def main() -> None:
    horse, human = read_seq(HORSE), read_seq(HUMAN)
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(horse, human)[0]
    # map human positions -> horse positions
    h2e: dict[int, int] = {}
    for (hs, he), (us, ue) in zip(*aln.aligned):
        for k in range(he - hs):
            h2e[us + k + 1] = hs + k + 1
    pairs = [(horse[h2e[u] - 1], human[u - 1]) for u in sorted(h2e)]
    ident = sum(a == b for a, b in pairs)
    print(f"horse length: {len(horse)}")
    print(f"human length: {len(human)}")
    print(f"aligned pairs: {len(pairs)}; identical: {ident}; identity: {100*ident/len(pairs):.2f}%")
    print(f"human residues unaligned: {len(human) - len(h2e)}")
    print(f"human Met1 aligns to horse position: {h2e.get(1)} ({horse[h2e[1]-1] if 1 in h2e else '-'})")
    print(f"horse N-terminal residues before human Met1: {horse[: h2e[1]-1] if 1 in h2e else 'NA'}")
    print(f"horse C-terminal residues after human last residue: {horse[h2e[len(human)]:] if len(human) in h2e else 'NA'}")
    for name, (s, e) in HUMAN_DOMAINS.items():
        cov = [u for u in range(s, e + 1) if u in h2e]
        idn = sum(horse[h2e[u] - 1] == human[u - 1] for u in cov)
        print(f"{name} human {s}-{e}: covered {len(cov)}/{e-s+1}, identical {idn} ({100*idn/max(1,len(cov)):.1f}%)")
    print()
    print(aln)


if __name__ == "__main__":
    main()
