"""Reproduce the historical sequence bridge using preserved ENA and UniProt bytes.
Run from repository root: uv run python genes/PSEPK/PP_1703/PP_1703-source-analysis/check_historical_identity.py
Dependencies: Biopython from the repository environment.
"""
from pathlib import Path
from Bio import SeqIO
import hashlib, json
here = Path(__file__).resolve().parent
raw = here.parent / "PP_1703-uniprot.txt"
seq = str(SeqIO.read(raw, "swiss").seq)
results = {}
for accession in ["AF203789", "AF240673"]:
    path = here / (accession + ".embl")
    rec = SeqIO.read(path, "embl")
    cds = next(f for f in rec.features if f.type == "CDS")
    protein = cds.qualifiers["translation"][0]
    offset = seq.find(protein)
    tail_offset = seq.find(protein[1:])
    results[accession] = {
        "source_url": "https://www.ebi.ac.uk/ena/browser/api/embl/" + accession,
        "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "protein_length": len(protein), "gene": cds.qualifiers.get("gene"),
        "protein_id": cds.qualifiers.get("protein_id"),
        "full_exact_target_start_1based": offset + 1 if offset >= 0 else None,
        "excluding_initiator_exact_target_start_1based": tail_offset + 1 if tail_offset >= 0 else None,
        "target_at_historical_initiator": seq[tail_offset-1] if tail_offset >= 1 else None,
    }
assert results["AF203789"]["protein_length"] == 724
assert results["AF203789"]["full_exact_target_start_1based"] == 1
assert results["AF240673"]["protein_length"] == 521
assert results["AF240673"]["excluding_initiator_exact_target_start_1based"] == 822
assert results["AF240673"]["target_at_historical_initiator"] == "V"
output = {"target": "Q88M71", "target_length": len(seq),
          "target_raw_sha256": hashlib.sha256(raw.read_bytes()).hexdigest(),
          "historical_records": results}
(here / "historical-identity.json").write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps(output, indent=2))
