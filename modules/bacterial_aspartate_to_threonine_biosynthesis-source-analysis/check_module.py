"""Validate the bounded native threonine panel with the production module validator.

Run from the repository root with ``uv run python <this-file>``. Family membership
is read from unedited target UniProt records; names are checked by the validator
against the committed PANTHER ontology. No global family-index download is needed.
"""

import json
from pathlib import Path
import re

import yaml

from ai_gene_review.validation.module_validator import validate_module_file
from ai_gene_review.validation.local_source_text import (
    quote_matches,
    resolve_local_source,
)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATA = ROOT / "analysis/module_audits/bacterial_aspartate_to_threonine_biosynthesis"


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def main():
    panel = yaml.safe_load((DATA / "members.yaml").read_text())
    members, reviews = {}, {}
    for member in panel:
        path = ROOT / member["path"]
        doc = yaml.safe_load(path.read_text())
        accession = member["accession"]
        assert doc["id"] == accession
        assert doc["taxon"]["id"] == "NCBITaxon:" + str(member["taxon_id"])
        raw = path.with_name(member["gene"] + "-uniprot.txt").read_text()
        assert re.search(r"^AC   " + re.escape(accession) + r";", raw, re.M)
        assert re.search(r"NCBI_TaxID=" + str(member["taxon_id"]) + r"(?:\s|;)", raw)
        families = re.findall(r"^DR   PANTHER; ([^;]+);", raw, re.M)
        if families:
            members[accession] = next(
                (family for family in families if ":SF" in family), families[0]
            )
        assert all(
            row["review"]["action"] != "PENDING" for row in doc["existing_annotations"]
        )
        reviews[accession] = path
    path = ROOT / "modules/bacterial_aspartate_to_threonine_biosynthesis.yaml"
    doc = yaml.safe_load(path.read_text())
    used = {
        node["id"].split(":", 1)[1]
        for node in walk(doc["module"])
        if str(node.get("id", "")).startswith("UniProtKB:")
    }
    used = {accession.split("-")[0] for accession in used}
    candidates = {
        m["accession"] for m in panel if m["role"].startswith("assessed candidate")
    }
    assert used == set(reviews) - candidates, (
        used - set(reviews),
        set(reviews) - candidates - used,
    )
    activities = [a for node in walk(doc["module"]) for a in node.get("annotons", [])]
    connections = [
        c for node in walk(doc["module"]) for c in node.get("connections", [])
    ]
    assert all(a.get("evidence") for a in activities)
    assert all(c.get("evidence") for c in connections)
    assert not any(
        str(node.get("source_id", "")).endswith("-ai-review.yaml") for node in walk(doc)
    )
    # The production module validator checks literature quotes. Also check local
    # and URL-cache evidence here, including findings that inherit a reference id.
    quoted = {
        (node["source_id"], node["supporting_text"])
        for node in walk(doc)
        if node.get("source_id") and node.get("supporting_text")
    }
    quoted.update(
        (ref["id"], finding["supporting_text"])
        for ref in doc["references"]
        for finding in ref.get("findings", [])
        if finding.get("supporting_text")
    )
    for reference, quote in quoted:
        if reference.startswith("file:"):
            source = resolve_local_source(reference, ROOT)
        elif reference.startswith("PMID:"):
            source = ROOT / "publications" / (reference.replace(":", "_") + ".md")
        elif reference.startswith("url:"):
            source = (
                ROOT / "publications" / (re.sub(r"[^\w.-]", "_", reference) + ".md")
            )
        else:
            raise AssertionError(f"Uncovered quoted source: {reference}")
        assert source and source.is_file(), reference
        assert quote_matches(quote, source), (reference, quote)
    result = validate_module_file(path, member_index=members, gene_index=reviews)
    report = {
        "valid": result.is_valid,
        "errors": result.errors,
        "warnings": result.warnings,
        "members": len(panel),
        "activities": len(activities),
        "connections": len(connections),
        "references": len(doc.get("references", [])),
        "distinct_source_quotes_checked": len(quoted),
        "findings": sum(
            len(ref.get("findings", [])) for ref in doc.get("references", [])
        ),
        "member_classifications": members,
    }
    (DATA / "validation-results.yaml").write_text(
        yaml.safe_dump(report, sort_keys=False, allow_unicode=True)
    )
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()
