"""Scan an explicit motif in a UniProt flat file; no functional inference is computed."""
import argparse
import hashlib
import json
from pathlib import Path
import re

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("input", type=Path)
parser.add_argument("--pattern", required=True)
args = parser.parse_args()
raw = args.input.read_bytes()
text = raw.decode()
if "SQ   SEQUENCE" not in text:
    raise ValueError("Expected a UniProt sequence record")
sequence = "".join(re.findall(r"[A-Z]+", text.split("SQ   SEQUENCE", 1)[1].split("\n", 1)[1].split("//", 1)[0]))
if not sequence or re.search(r"[^ACDEFGHIKLMNPQRSTVWYBXZJUO]", sequence):
    raise ValueError("Invalid protein sequence")
expression = re.compile(args.pattern)
print(json.dumps({"input": str(args.input), "input_sha256": hashlib.sha256(raw).hexdigest(), "length": len(sequence), "pattern": args.pattern, "matches": [{"start_1based": m.start()+1, "end_inclusive": m.end(), "sequence": m.group()} for m in expression.finditer(sequence)]}, indent=2))
