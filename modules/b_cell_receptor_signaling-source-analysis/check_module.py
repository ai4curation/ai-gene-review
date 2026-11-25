"""Validate BCR identities, bounded family membership and evidence placement.

Run with: uv run python modules/b_cell_receptor_signaling-source-analysis/check_module.py
Membership is read independently from fetched UniProt records. No release-wide
PANTHER index or inferred ancestral placement is manufactured by this check.
"""

from pathlib import Path
import json
import re
import yaml
from ai_gene_review.validation.module_validator import validate_module_file

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def main():
    panel = yaml.safe_load((HERE / "members.yaml.txt").read_text())["members"]
    mapping, gene_index = {}, {}
    for entry in panel:
        path = ROOT / entry["review"]
        review = yaml.safe_load(path.read_text())
        accession = entry["accession"]
        assert review["id"] == accession, path
        raw = path.with_name(entry["gene"] + "-uniprot.txt").read_text()
        assert re.search(r"^AC   " + re.escape(accession) + r";", raw, re.M), path
        assert re.search(r"NCBI_TaxID=" + entry["taxon"] + r"(?:\s|;)", raw), path
        assert review["taxon"]["id"] == "NCBITaxon:" + entry["taxon"], path
        families = re.findall(r"^DR   PANTHER; ([^;]+);", raw, re.M)
        assert families, path
        mapping[accession] = next((f for f in families if ":SF" in f), families[0])
        gene_index[accession] = path
    path = ROOT / "modules/b_cell_receptor_signaling.yaml"
    doc = yaml.safe_load(path.read_text())
    result = validate_module_file(path, member_index=mapping, gene_index=gene_index)
    annotons = [a for item in walk(doc) for a in item.get("annotons", [])]
    assert all(any(x.get("family") for x in walk(a["participant"])) for a in annotons)
    assert all(a.get("evidence") for a in annotons)
    connections = [e for item in walk(doc) for e in item.get("connections", [])]
    assert all(e.get("evidence") for e in connections)
    used = {
        x["id"].split(":", 1)[1]
        for x in walk(doc)
        if str(x.get("id", "")).startswith("UniProtKB:")
    }
    assert used == set(gene_index), (used - set(gene_index), set(gene_index) - used)
    report = {
        "valid": result.is_valid,
        "errors": result.errors,
        "warnings": result.warnings,
        "reviewed_panel": len(panel),
        "annotons": len(annotons),
        "connections": len(connections),
        "member_mapping": mapping,
    }
    log = ROOT / ".cache/module-audit-logs/b-cell-module-validation.json"
    log.parent.mkdir(parents=True, exist_ok=True)
    log.write_text(json.dumps(report, indent=2) + "\n")
    print(
        f"{len(panel)} members; {len(annotons)} grounded activities; {len(connections)} evidenced connections"
    )
    print(f"{len(result.errors)} errors; {len(result.warnings)} warnings")
    for error in result.errors:
        print("ERROR:", error)
    for warning in result.warnings:
        print("WARNING:", warning)
    raise SystemExit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()
