"""Check target residue counts; not a direct metal-binding assay."""
from pathlib import Path
from Bio import SeqIO
import json, hashlib
here = Path(__file__).resolve().parent
raw = here.parent / "nirD-uniprot.txt"
seq = str(SeqIO.read(raw, "swiss").seq)
residues = {aa: [i+1 for i, r in enumerate(seq) if r == aa] for aa in ("C", "H")}
assert residues == {"C": [18, 95], "H": [87]}
result = {"target": "Q88M68", "length": len(seq), "residues": residues,
          "target_raw_sha256": hashlib.sha256(raw.read_bytes()).hexdigest()}
(here / "ligands.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
