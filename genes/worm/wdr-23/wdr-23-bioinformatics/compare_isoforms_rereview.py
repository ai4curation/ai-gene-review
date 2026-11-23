# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Re-review: map S6FN32 (D2030.9d) onto the reviewed WDR-23A/B isoforms of P90794.

Inputs (all in the gene folder): wdr-23-uniprot.txt (S6FN32 flat file),
wdr-23-reference-isoforms.fasta (P90794 canonical, WDR-23A) and
wdr-23-reference-isoform-b.fasta (P90794-2, WDR-23B).
Writes RESULTS-rereview.json next to this script and prints a report.
"""
import json
import re
from pathlib import Path

here = Path(__file__).resolve().parent
gene = here.parent


def fasta(path):
    lines = path.read_text().splitlines()
    return "".join(l.strip() for l in lines if not l.startswith(">"))


def uniprot_seq(path):
    text = path.read_text()
    block = text.split("\nSQ   ", 1)[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", block)


target = uniprot_seq(gene / "wdr-23-uniprot.txt")
iso_a = fasta(gene / "wdr-23-reference-isoforms.fasta")
iso_b = fasta(gene / "wdr-23-reference-isoform-b.fasta")

res = {"S6FN32_length": len(target), "WDR23A_P90794_length": len(iso_a),
       "WDR23B_P90794-2_length": len(iso_b)}
for name, ref in (("WDR23A_P90794", iso_a), ("WDR23B_P90794-2", iso_b)):
    i = ref.find(target)
    res[f"S6FN32_start_in_{name}"] = i + 1 if i >= 0 else None
    res[f"{name}_residues_absent_from_S6FN32"] = ref[:i] if i >= 0 else None

# shared N-terminal segment of A and B upstream of S6FN32 start
a_up = res["WDR23A_P90794_residues_absent_from_S6FN32"]
b_up = res["WDR23B_P90794-2_residues_absent_from_S6FN32"]
k = 0
while k < min(len(a_up), len(b_up)) and a_up[-1 - k] == b_up[-1 - k]:
    k += 1
res["shared_AB_segment_absent_from_S6FN32"] = a_up[len(a_up) - k:]
res["WDR23A_specific_N_terminus"] = a_up[: len(a_up) - k]
res["WDR23B_specific_N_terminus"] = b_up[: len(b_up) - k]

# DCAF DxR-box-like motifs ((W/Y)DxR) in the target, 1-based positions
res["S6FN32_WY_D_x_R_motifs"] = [
    {"pos": m.start() + 1, "motif": target[m.start():m.start() + 4]}
    for m in re.finditer(r"(?=[WY]D.R)", target)
]

(here / "RESULTS-rereview.json").write_text(json.dumps(res, indent=2) + "\n")
print(json.dumps(res, indent=2))
