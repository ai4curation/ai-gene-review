"""Compare horse MTMR9 A0A5F5PR89 with human MTMR9 Q96QG7 region by region.

Reads the sequences from the cached UniProt flat files:
  genes/HORSE/MTMR9__A0A5F5PR89/MTMR9__A0A5F5PR89-uniprot.txt
  genes/human/MTMR9/MTMR9-uniprot.txt

Reports overall identity, identity within the PH-GRAM domain, the
myotubularin phosphatase-like domain and the C-terminal coiled coil (human
coordinates), the residues of the HCX5R active-site loop, and every
substitution. Writes RESULTS.md and results.json next to this script.

Run from repo root:
  uv run python genes/HORSE/MTMR9__A0A5F5PR89/MTMR9__A0A5F5PR89-bioinformatics/compare_to_human.py
"""

import json
from pathlib import Path

from Bio import Align

here = Path(__file__).resolve().parent
genes = here.parents[2]

# Human coordinates. Domain bounds from the human UniProt record features;
# the loop start (332) is where the myotubularin HCX5R loop aligns in the
# active paralogs MTMR6/7/8 (genes/human/MTMR9/MTMR9-bioinformatics).
REGIONS = {
    "PH-GRAM (human 4-99)": (4, 99),
    "myotubularin phosphatase-like domain (human 123-498)": (123, 498),
    "C-terminal coiled coil (human 508-542)": (508, 542),
}
LOOP = (332, 340)


def uniprot_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, x in enumerate(lines) if x.startswith("SQ "))
    seq = []
    for x in lines[start + 1 :]:
        if x.startswith("//"):
            break
        seq.append(x.replace(" ", ""))
    return "".join(seq)


horse = uniprot_seq(genes / "HORSE/MTMR9__A0A5F5PR89/MTMR9__A0A5F5PR89-uniprot.txt")
human = uniprot_seq(genes / "human/MTMR9/MTMR9-uniprot.txt")

aligner = Align.PairwiseAligner()
aligner.mode = "global"
aligner.match_score = 2
aligner.mismatch_score = -1
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aln = aligner.align(human, horse)[0]
x, y = str(aln[0]), str(aln[1])

# map human position -> horse residue ('-' if gap)
hmap: dict[int, str] = {}
pos = 0
gaps_in_horse = 0
extra_in_horse = 0
for u, v in zip(x, y):
    if u == "-":
        extra_in_horse += 1
        continue
    pos += 1
    hmap[pos] = v
    if v == "-":
        gaps_in_horse += 1


def identity(a: int, b: int) -> float:
    same = sum(human[i - 1] == hmap[i] for i in range(a, b + 1))
    return round(same / (b - a + 1), 4)


subs = [
    f"{human[i - 1]}{i}{hmap[i]}"
    for i in range(1, len(human) + 1)
    if hmap[i] != human[i - 1]
]
loop_human = human[LOOP[0] - 1 : LOOP[1]]
loop_horse = "".join(hmap[i] for i in range(LOOP[0], LOOP[1] + 1))

res = {
    "horse_length": len(horse),
    "human_length": len(human),
    "gaps_in_horse": gaps_in_horse,
    "extra_residues_in_horse": extra_in_horse,
    "overall_identity": identity(1, len(human)),
    "regions": {k: identity(*v) for k, v in REGIONS.items()},
    "active_site_loop_human": loop_human,
    "active_site_loop_horse": loop_horse,
    "substitutions_human_to_horse": subs,
}
(here / "results.json").write_text(json.dumps(res, indent=2) + "\n")

md = [
    "# Horse MTMR9 A0A5F5PR89 vs human MTMR9 Q96QG7",
    "",
    "Script: `compare_to_human.py` (global pairwise alignment, Biopython). Output: `results.json`.",
    "",
    f"- Lengths: horse {len(horse)} aa, human {len(human)} aa; "
    f"gaps in horse {gaps_in_horse}; extra horse residues {extra_in_horse}",
    f"- Overall identity: {res['overall_identity']:.1%}",
]
for k, v in res["regions"].items():
    md.append(f"- {k}: {v:.1%} identity")
md += [
    f"- HCX5R active-site loop (human {LOOP[0]}-{LOOP[1]}): human `{loop_human}`, "
    f"horse `{loop_horse}`",
    f"- Substitutions ({len(subs)}): {', '.join(subs)}",
    "",
]
(here / "RESULTS.md").write_text("\n".join(md))
print("\n".join(md))
