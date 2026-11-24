"""Run with `uv run python genes/RHIME/cheA/cheA-source-analysis/verify_identity.py`.

Compare frozen, normally fetched UniProt sequences with official deposited source
records. Requires Biopython (provided by the repository environment).
"""
from pathlib import Path
import hashlib
import json
from Bio import SeqIO

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
operon = SeqIO.read(HERE / "U13166.1.embl", "embl")
translations = {f.qualifiers["protein_id"][0]: f.qualifiers["translation"][0]
                for f in operon.features if f.type == "CDS"}
targets = [("RHIML", "cheY1", "AAA86673.1"),
           ("RHIML", "cheY2", "AAA86678.1"),
           ("RHIML", "cheS", "AAA86672.1"),
           ("RHIME", "cheA", "AAA86674.1"),
           ("RHIME", "cheT", "NP_384751.1")]
results = []
for organism, gene, source in targets:
    uniprot_path = ROOT / "genes" / organism / gene / f"{gene}-uniprot.txt"
    uniprot = SeqIO.read(uniprot_path, "swiss")
    target = str(uniprot.seq)
    if source.startswith("NP_"):
        source_path = ROOT / "genes/RHIME/cheT/cheT-source-analysis/NP_384751.1.gp"
        reference = str(SeqIO.read(source_path, "genbank").seq)
    else:
        source_path = HERE / "U13166.1.embl"
        reference = translations[source]
    assert len(target) == len(reference), (gene, len(target), len(reference))
    differences = [{"position": i, "current_uniprot": a, "deposited_source": b}
                   for i, (a, b) in enumerate(zip(target, reference), 1) if a != b]
    results.append({"organism": organism, "gene": gene, "uniprot": uniprot.id,
                    "source_protein": source, "length": len(target),
                    "identical": target == reference, "differences": differences,
                    "uniprot_sha256": hashlib.sha256(uniprot_path.read_bytes()).hexdigest(),
                    "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest()})
(HERE / "identity-proof.json").write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2))
