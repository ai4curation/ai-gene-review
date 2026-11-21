#!/usr/bin/env python3
"""Compare deposited historical CDS translations with the cached UniProt record.

Uses only the Python standard library and local, unmodified source records.
This compares accession sequences, not the unavailable experimental plasmids.
"""

import argparse
import hashlib
import json
import re
from pathlib import Path


def fingerprint(path):
    data = path.read_bytes()
    return {"file": path.name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def genbank(path):
    text = path.read_text()
    translations = re.findall(r'/translation="([A-Z\s]+)"', text)
    if len(translations) != 1:
        raise ValueError(f"Expected exactly one annotated CDS translation in {path}")
    return {
        "accession": re.search(r"^VERSION\s+(\S+)", text, re.M).group(1),
        "protein_id": re.search(r'/protein_id="([^"]+)"', text).group(1),
        "sequence": re.sub(r"\s+", "", translations[0]),
    }


def sequence_record(record):
    sequence = record.pop("sequence")
    return {**record, "length": len(sequence), "sequence_sha256": hashlib.sha256(sequence.encode()).hexdigest()}


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--uniprot", type=Path, default=here.parent / "GJC2-uniprot.txt")
    args = parser.parse_args()
    paths = [here / "inputs" / "AY285161.1.gb", here / "inputs" / "AF014643.1.gb"]
    ay, af = [genbank(path) for path in paths]
    text = args.uniprot.read_text()
    accession = re.search(r"^AC\s+([^;]+);", text, re.M).group(1)
    sequence_section = re.split(r"^SQ[^\n]*\n", text, flags=re.M)
    if len(sequence_section) != 2:
        raise ValueError("Expected exactly one UniProt sequence section")
    current = "".join(re.findall(r"[A-Z]+", sequence_section[1].split("//", 1)[0]))
    offset = current.find(ay["sequence"])
    ay_length = len(ay["sequence"])
    matched = offset >= 0 and current.count(ay["sequence"]) == 1
    comparable = len(ay["sequence"]) == len(af["sequence"])
    differences = [
        {"historical_position": i + 1, "AY285161": a, "AF014643": b,
         "current_position": i + 1 + offset if matched else None}
        for i, (a, b) in enumerate(zip(ay["sequence"], af["sequence"])) if a != b
    ] if comparable else None
    position = 33
    numbering = {
        "historical_position": position,
        "AY285161_residue": ay["sequence"][position - 1],
        "AF014643_residue": af["sequence"][position - 1],
        "current_position": position + offset if matched else None,
        "current_residue": current[position - 1 + offset] if matched else None,
    }
    result = {
        "inputs": [fingerprint(path) for path in paths + [args.uniprot]],
        "AY285161": sequence_record(ay), "AF014643": sequence_record(af),
        "current": sequence_record({"accession": accession, "sequence": current}),
        "AY_unique_exact_subsequence_of_current": matched,
        "current_interval_1based": [offset + 1, offset + ay_length] if matched else None,
        "historical_sequences_equal_length": comparable,
        "historical_sequence_differences": differences,
        "historical_position_33_mapping": numbering,
        "limits": [
            "Deposited CDS translations are compared; the 2009 experimental plasmid sequence was not recovered.",
            "No endogenous initiation site, additional natural isoform, or mouse construct equivalence is inferred.",
        ],
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
