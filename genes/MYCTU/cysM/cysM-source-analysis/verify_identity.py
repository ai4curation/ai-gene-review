"""Reproduce primary PDB construct comparisons from frozen local sources. No network."""

from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[4]
checks = []
for gene, pdb, prefix, changes, pmid in [
    ("cysK1", "2Q3B", "GSH", {}, "17567578"),
    ("cysM", "3DWG", "RH", {}, "18771296"),
    ("cysM", "3DKI", "GSH", {2: "A"}, "18799456"),
]:
    directory = root / "genes/MYCTU" / gene
    sd = directory / f"{gene}-source-analysis"
    record = (directory / f"{gene}-uniprot.txt").read_text()
    seq = re.sub(
        "[^A-Z]", "", record.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    )
    target = list(seq)
    for pos, residue in changes.items():
        target[pos - 1] = residue
    entity = json.loads((sd / f"{pdb}-polymer_entity.json").read_text())
    entry = json.loads((sd / f"{pdb}-entry.json").read_text())
    actual = re.sub(r"\s+", "", entity["entity_poly"]["pdbx_seq_one_letter_code_can"])
    assert actual == prefix + "".join(target), (gene, pdb)
    assert str(entry["rcsb_primary_citation"]["pdbx_database_id_PubMed"]) == pmid
    checks.append(
        {
            "gene": gene,
            "pdb": pdb,
            "status": "PASS",
            "sequence_length": len(seq),
            "prefix": prefix,
            "substitutions": changes,
            "primary_pmid": pmid,
        }
    )
print(json.dumps(checks, indent=2))
