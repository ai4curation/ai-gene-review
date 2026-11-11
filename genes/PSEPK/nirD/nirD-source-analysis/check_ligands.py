"""Report cysteine/histidine positions from immutable UniProt flat files.
Counts are observations, not a metal-binding assay or a ligand-site prediction.
"""
import argparse, json, hashlib
from pathlib import Path
from Bio import SeqIO
p = argparse.ArgumentParser()
p.add_argument("--input", type=Path, nargs="+", required=True)
p.add_argument("--output", type=Path, required=True)
a = p.parse_args()
results = []
for path in a.input:
    record = SeqIO.read(path, "swiss")
    seq = str(record.seq)
    residues = {aa: [i+1 for i, r in enumerate(seq) if r == aa] for aa in ("C", "H")}
    results.append({"target": record.id, "length": len(seq), "residues": residues,
                    "target_raw_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
result = results[0] if len(results) == 1 else {"targets": results}
a.output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
