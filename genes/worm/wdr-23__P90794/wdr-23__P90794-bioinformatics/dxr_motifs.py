# /// script
# requires-python = ">=3.10"
# ///
"""Locate (W/Y)DxR "DxR box" motifs in WDR-23A (P90794) and map them onto UniProt WD repeats.

Reads only the UniProt flat file in the parent folder. Prints a JSON report.
Run: uv run --script dxr_motifs.py
"""
import json
import re
from pathlib import Path

here = Path(__file__).resolve().parent
flat = (here.parent / "wdr-23__P90794-uniprot.txt").read_text().splitlines()

seq = "".join(
    line.strip().replace(" ", "") for line in flat if line.startswith("     ")
)
repeats = []
for i, line in enumerate(flat):
    m = re.match(r"FT   REPEAT\s+(\d+)\.\.(\d+)", line)
    if m:
        note = re.search(r'/note="([^"]+)"', flat[i + 1]).group(1)
        repeats.append((note, int(m.group(1)), int(m.group(2))))


def repeat_of(pos: int) -> str | None:
    for note, s, e in repeats:
        if s <= pos <= e:
            return note
    return None


hits = []
for m in re.finditer(r"(?=([WY]D.R))", seq):
    start = m.start() + 1
    arg = start + 3
    hits.append(
        {
            "motif": m.group(1),
            "start": start,
            "arginine_position": arg,
            "wd_repeat": repeat_of(start),
        }
    )

report = {
    "accession": "P90794",
    "length": len(seq),
    "wd_repeats": [{"note": n, "start": s, "end": e} for n, s, e in repeats],
    "wdxr_motifs": hits,
    "residue_342": seq[341],
    "residue_389": seq[388],
}
print(json.dumps(report, indent=2))
