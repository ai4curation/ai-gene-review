"""Check exact members, independent families, evidence placement and production semantics.

Run: uv run python modules/bacterial_ammonia_assimilation-source-analysis/check_module.py
The member index is bounded to the 12 reviewed proteins. It is built from independently
retrieved PANTHER 19 classification files and the normal UniProt fallback, not guessed
from module descriptors and not installed as a release-wide cache.
"""

from pathlib import Path
import json
import re
import yaml
from ai_gene_review.datamodel.gene_review_model import ModuleReview
from ai_gene_review.validation.module_validator import validate_module_file

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def walk(x):
    if isinstance(x, dict):
        yield x
        for v in x.values():
            yield from walk(v)
    elif isinstance(x, list):
        for v in x:
            yield from walk(v)


def main():
    path = ROOT / "modules/bacterial_ammonia_assimilation.yaml"
    d = yaml.safe_load(path.read_text())
    ModuleReview.model_validate(d)
    panel = json.loads((HERE / "members.json").read_text())
    verification = json.loads((HERE / "family-verification.json").read_text())
    idx = verification["independent_member_index"]
    mapping = idx["uniprot"]
    gene_index = {}
    obo = (ROOT / "interpro/panther/panther.obo").read_text()
    labels = {}
    for block in obo.split("[Term]"):
        i = re.search(r"^id: PANTHER:(.+)$", block, re.M)
        n = re.search(r"^name: (.+)$", block, re.M)
        if i and n:
            labels[i[1]] = n[1]
    for m in panel:
        p = ROOT / m["path"]
        g = yaml.safe_load(p.read_text())
        raw = (ROOT / m["raw"]).read_text()
        acc = m["accession"]
        gene_index[acc] = p
        assert g["id"] == acc and g["taxon"] == m["taxon"]
        assert re.search(r"^AC   " + re.escape(acc) + r";", raw, re.M)
        assert f"PANTHER; {m['family']}; {m['family_label']};" in raw
        assert labels[m["family"]] == m["family_label"]
        assert mapping[acc] == m["family"]
        if acc in idx["panther"]:
            assert idx["panther"][acc] == m["family"]
    exact = [x for x in walk(d) if x.get("selector_type") == "GENE_PRODUCT"]
    assert len(exact) == 12
    for x in exact:
        a = x["gene_product"]["term"]["id"].split(":")[1]
        assert x["family"]["term"]["id"] == "PANTHER:" + mapping[a]
        assert x.get("taxon") and x["family"].get("evidence")
    assert {x["gene_product"]["term"]["id"].split(":")[1] for x in exact} == set(
        mapping
    )
    assert not any(x.get("selector_type") == "FAMILY" for x in walk(d))
    assert not any(x.get("ancestral_nodes") for x in walk(d))
    annotations = [a for x in walk(d) for a in x.get("annotons", [])]
    edges = [e for x in walk(d) for e in x.get("connections", [])]
    units = [u for x in walk(d) for u in x.get("active_units", [])]
    assert len(annotations) == len(edges) == len(units) == 8
    for x in annotations + edges + units:
        assert x.get("evidence")
        assert any(e["source_id"].startswith(("PMID:", "file:")) for e in x["evidence"])
    result = validate_module_file(path, member_index=mapping, gene_index=gene_index)
    report = {
        "valid": result.is_valid,
        "errors": result.errors,
        "warnings": result.warnings,
        "members": 12,
        "activities": 8,
        "complex_units": 8,
        "evidenced_edges": 8,
        "member_mapping": mapping,
        "verification_sources": {
            "panther_release": "19.0",
            "panther_matches": len(idx["panther"]),
            "independent_uniprot_matches": len(mapping),
        },
    }
    out = ROOT / ".cache/module-audit-logs/ammonia-module-review"
    out.mkdir(parents=True, exist_ok=True)
    (out / "production-validation.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()
