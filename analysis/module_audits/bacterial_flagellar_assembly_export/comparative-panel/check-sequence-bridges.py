#!/usr/bin/env python3
"""Verify deposited construct strings against unchanged reference UniProt sequences."""

from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
seqs = {}
for block in (HERE / "construct-sequences.fasta").read_text().split(">")[1:]:
    lines = block.splitlines()
    seqs[lines[0].split()[0]] = "".join(lines[1:])
rows = [
    ("SALTY", "fliJ", "3AJW_1", 1, 147, "GSH", ""),
    ("SALTY", "flgE", "6K3I_1", 2, 403, "", ""),
    ("SALTY", "fliK", "2RRL_1", 204, 370, "HM", ""),
    ("VIBAL", "pomA", "8ZYW_2", 1, 253, "", ""),
    ("VIBAL", "pomB", "8ZYW_1", 1, 315, "", "HHHHHH"),
]
results = []
for org, g, pdb, start, end, prefix, suffix in rows:
    p = ROOT / "genes" / org / g / f"{g}-uniprot.txt"
    text = p.read_text()
    seq = "".join(
        re.findall(r"[A-Z]+", text.split("\nSQ   ")[1].split("\n", 1)[1].split("//")[0])
    )
    expected = prefix + seq[start - 1 : end] + suffix
    assert expected == seqs[pdb], (g, pdb)
    results.append(
        {
            "target": f"{org}/{g}",
            "construct": pdb,
            "reference_start": start,
            "reference_end": end,
            "prefix": prefix,
            "suffix": suffix,
            "exact_match": True,
            "reference_file_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        }
    )
print(json.dumps({"passed": True, "checks": results}, indent=2))
