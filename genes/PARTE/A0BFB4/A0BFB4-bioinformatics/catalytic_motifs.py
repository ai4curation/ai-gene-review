"""Locate canonical protein-kinase catalytic motifs in A0BFB4 (UniProt sequence).

Run: uv run python catalytic_motifs.py  -> prints JSON, writes catalytic_motifs.json
"""

import json
import re
from pathlib import Path

import requests

HERE = Path(__file__).parent
seq = requests.get("https://rest.uniprot.org/uniprotkb/A0BFB4.fasta", timeout=60).text
seq = "".join(seq.splitlines()[1:])
MOTIFS = {
    "glycine_rich_loop_GxGxxG": r"G.G..G",
    "beta3_lysine_AxK": r"A.K",
    "catalytic_loop_HRD": r"HRD",
    "DFG": r"DFG",
    "APE": r"APE",
}
out = {"length": len(seq), "motifs": {}}
for name, pat in MOTIFS.items():
    out["motifs"][name] = [
        {"start": m.start() + 1, "match": m.group(), "context": seq[max(0, m.start() - 5) : m.end() + 5]}
        for m in re.finditer(pat, seq)
    ]
(HERE / "catalytic_motifs.json").write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))
