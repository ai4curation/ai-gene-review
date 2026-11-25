"""Re-review analysis: compare all horse DNMT3A UniProt gene models with human Q9Y6K1.

Fetches sequences live from the UniProt REST API, globally aligns each horse
model to human DNMT3A (BLOSUM62, gap open -10, extend -0.5) and reports:
  * identity over aligned pairs
  * human residue ranges with no horse counterpart (deletions)
  * horse insertions relative to human
  * whether key human catalytic/reader residues are conserved

Run:  uv run python compare_isoforms_rereview.py > RESULTS-rereview-alignment.txt
"""

import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

HUMAN = "Q9Y6K1"
HORSE = [
    "A0A9L0TK01",
    "A0A3Q2IAR2",
    "F6Q5D1",
    "A0A9L0RGD3",
    "A0A9L0T4V1",
    "A0A3Q2HNA6",
    "A0A9L0TMC0",
]
# Human residues of interest (UniProt Q9Y6K1 numbering)
KEY_SITES = {
    "PWWP W330 (aromatic cage)": 330,
    "PWWP D333": 333,
    "PC motif C710 (catalytic nucleophile)": 710,
    "ENV motif E756": 756,
    "TRD R836 (CpG recognition)": 836,
    "R882 (tetramer interface, AML hotspot)": 882,
}
DOMAINS = {"PWWP": (292, 350), "ADD": (482, 614), "MTase": (634, 912)}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as r:
        lines = r.read().decode().splitlines()
    return "".join(lines[1:])


def ranges(positions: list[int]) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for p in positions:
        if out and p == out[-1][1] + 1:
            out[-1] = (out[-1][0], p)
        else:
            out.append((p, p))
    return out


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    human = fetch(HUMAN)
    print(f"Human {HUMAN} length {len(human)}")
    for acc in HORSE:
        horse = fetch(acc)
        aln = aligner.align(human, horse)[0]
        h2x: dict[int, int] = {}
        for (hs, he), (xs, xe) in zip(*aln.aligned):
            for k in range(he - hs):
                h2x[hs + k + 1] = xs + k + 1
        pairs = len(h2x)
        ident = sum(1 for h, x in h2x.items() if human[h - 1] == horse[x - 1])
        missing = [i for i in range(1, len(human) + 1) if i not in h2x]
        mapped_x = set(h2x.values())
        inserted = [j for j in range(1, len(horse) + 1) if j not in mapped_x]
        print(f"\n== {acc} length {len(horse)}")
        print(f"aligned pairs {pairs}; identity {ident}/{pairs} = {100 * ident / pairs:.1f}%")
        print(f"human residues absent: {ranges(missing)}")
        print(f"horse residues inserted: {ranges(inserted)}")
        for name, (s, e) in DOMAINS.items():
            cov = sum(1 for i in range(s, e + 1) if i in h2x)
            print(f"  {name} {s}-{e}: {cov}/{e - s + 1} human residues aligned")
        for name, pos in KEY_SITES.items():
            if pos in h2x:
                x = h2x[pos]
                print(f"  {name}: human {human[pos - 1]}{pos} -> horse {horse[x - 1]}{x}")
            else:
                print(f"  {name}: human {human[pos - 1]}{pos} -> ABSENT")


if __name__ == "__main__":
    main()
