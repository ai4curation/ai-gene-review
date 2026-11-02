"""Map the human CH25H histidine-box motifs (UniProt MOTIF features) onto horse F6T000.

Run from the repository root: uv run python genes/HORSE/CH25H/CH25H-bioinformatics/hisbox_rereview.py
Writes RESULTS-rereview.md and results-rereview.json next to this script.
Pairwise alignment only: it checks conservation of the diiron-coordinating
histidine boxes, it does not establish orthology (that comes from PANTHER/PAINT).
"""

import json
import re
from pathlib import Path

from Bio import Align, SeqIO

here = Path(__file__).resolve().parent
root = next(p for p in here.parents if (p / "pyproject.toml").exists())
human = SeqIO.read(root / "genes/human/CH25H/CH25H-uniprot.txt", "swiss")
horse = SeqIO.read(here.parent / "CH25H-uniprot.txt", "swiss")
a, b = str(human.seq), str(horse.seq)

aligner = Align.PairwiseAligner(
    mode="global", match_score=2, mismatch_score=-1, open_gap_score=-10, extend_gap_score=-0.5
)
al = aligner.align(a, b)[0]
hmap = {}
for (s, e), (t, u) in zip(*al.aligned):
    for i, j in zip(range(s, e), range(t, u)):
        hmap[int(i)] = int(j)

motifs = []
for f in human.features:
    if f.type != "MOTIF":
        continue
    start, end = int(f.location.start), int(f.location.end)
    hres = a[start:end]
    hpos = [hmap.get(i) for i in range(start, end)]
    bres = "".join(b[j] if j is not None else "-" for j in hpos)
    his_h = [start + k + 1 for k, c in enumerate(hres) if c == "H"]
    his_b_conserved = all(hmap.get(p - 1) is not None and b[hmap[p - 1]] == "H" for p in his_h)
    motifs.append(
        {
            "motif": str(f.qualifiers.get("note", "")),
            "human_range_1based": [start + 1, end],
            "human_residues": hres,
            "horse_range_1based": [
                min(j for j in hpos if j is not None) + 1,
                max(j for j in hpos if j is not None) + 1,
            ],
            "horse_residues": bres,
            "human_histidines_1based": his_h,
            "all_histidines_conserved_in_horse": his_b_conserved,
        }
    )

# independent regex scan of the horse sequence for canonical FA-hydroxylase His boxes
regex_hits = {
    "HX3H": [(m.start() + 1, b[m.start():m.start() + 5]) for m in re.finditer(r"(?=H.{3}H)", b)],
    "HX2HH": [(m.start() + 1, b[m.start():m.start() + 5]) for m in re.finditer(r"(?=H.{2}HH)", b)],
}

n = len(hmap)
ident = sum(a[i] == b[j] for i, j in hmap.items())
res = {
    "human_id": human.id,
    "horse_id": horse.id,
    "human_length": len(a),
    "horse_length": len(b),
    "identity_paired_percent": round(100 * ident / n, 2),
    "histidine_box_motifs": motifs,
    "horse_regex_hits": regex_hits,
}
(here / "results-rereview.json").write_text(json.dumps(res, indent=2) + "\n")

lines = [
    "# CH25H horse F6T000: histidine-box conservation (re-review)",
    "",
    f"Human {human.id} ({len(a)} aa) vs horse {horse.id} ({len(b)} aa); global alignment identity "
    f"{res['identity_paired_percent']}% over {n} paired residues.",
    "",
    "## Human UniProt histidine-box MOTIF features mapped to horse",
    "",
]
for m in motifs:
    lines.append(
        f"- {m['motif']}: human {m['human_range_1based'][0]}-{m['human_range_1based'][1]} {m['human_residues']} -> "
        f"horse {m['horse_range_1based'][0]}-{m['horse_range_1based'][1]} {m['horse_residues']}; "
        f"all histidines conserved: {m['all_histidines_conserved_in_horse']}"
    )
lines += [
    "",
    "## Horse regex scan for HX2HH boxes (1-based start, motif)",
    "",
    ", ".join(f"{p} {s}" for p, s in regex_hits["HX2HH"]),
    "",
    "Interpretation: conservation of every histidine in the three boxes is consistent with an intact "
    "diiron site, as required for catalysis in the human/mouse enzymes; it is not an assay of horse activity.",
    "",
    "Reproduce with `uv run python genes/HORSE/CH25H/CH25H-bioinformatics/hisbox_rereview.py`.",
]
(here / "RESULTS-rereview.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
