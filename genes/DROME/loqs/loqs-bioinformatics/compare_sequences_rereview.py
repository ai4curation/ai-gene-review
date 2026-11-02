"""Re-review check: locate the single PF (X2J5X6) vs PB (Q9VJY9) indel and
report its position relative to UniProt-curated PB features.

Reads sequences and FT lines from the cached UniProt flat files; prints a JSON report.
Run: python3 compare_sequences_rereview.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE = HERE.parent


def read_seq(path: Path) -> str:
    text = path.read_text()
    body = text.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[\s\d]", "", body)


def read_features(path: Path):
    feats = []
    for m in re.finditer(r"^FT   (DOMAIN|MUTAGEN|VAR_SEQ|REGION)\s+(\d+)\.\.(\d+)\n((?:FT {19}.*\n)+)",
                         path.read_text(), re.M):
        note = " ".join(l[21:].strip() for l in m.group(4).splitlines())
        feats.append({"type": m.group(1), "start": int(m.group(2)), "end": int(m.group(3)), "text": note})
    return feats


pf = read_seq(GENE / "loqs-uniprot.txt")
ref_path = GENE / "loqs-reference-Q9VJY9-uniprot.txt"
pb = read_seq(ref_path)

# first mismatch scanning left to right
i = next((k for k in range(min(len(pf), len(pb))) if pf[k] != pb[k]), min(len(pf), len(pb)))
single_deletion = pf[:i] == pb[:i] and pf[i:] == pb[i + 1:]
# leftmost/rightmost equivalent placements of a one-residue deletion
left = i
while left > 0 and pb[left - 1] == pb[i]:
    left -= 1
report = {
    "pf_length": len(pf),
    "pb_length": len(pb),
    "single_residue_deletion_in_pf": single_deletion,
    "deleted_pb_residue": pb[i],
    "deleted_pb_position_1based": i + 1,
    "equivalent_positions_1based": list(range(left + 1, i + 2)),
    "pb_context": pb[i - 8:i + 8],
    "pf_context": pf[i - 8:i + 7],
    "nearby_pb_features": [f for f in read_features(ref_path)
                           if f["start"] - 10 <= i + 1 <= f["end"] + 10 and f["type"] != "REGION"
                           or (f["type"] == "REGION" and f["start"] <= i + 1 <= f["end"] + 5)],
}
print(json.dumps(report, indent=2))
