"""Check the scoped panel with production module and source-text validators."""

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
import yaml
from ai_gene_review.validation.module_validator import validate_module_file
from ai_gene_review.validation.local_source_text import quote_matches

ROOT = Path(__file__).resolve().parents[2]
SLUG = "bacterial_c_di_amp_signaling"
DATA = ROOT / "analysis/module_audits" / SLUG


def walk(x):
    if isinstance(x, dict):
        yield x
        for v in x.values():
            yield from walk(v)
    elif isinstance(x, list):
        for v in x:
            yield from walk(v)


def main():
    baseline = yaml.safe_load((DATA / "seed-baseline.yaml").read_text())
    members = {}
    reviews = {}
    actions = Counter()
    row_count = 0
    raw_count = 0
    new_rows = []
    for r in baseline["members"]:
        p = ROOT / r["review_path"]
        d = yaml.safe_load(p.read_text())
        acc = r["accession"]
        reviews[acc] = p
        original = r["original_annotations"]
        current = [
            {k: v for k, v in a.items() if k != "review"}
            for a in d.get("existing_annotations", [])
            if a["review"]["action"] != "NEW"
        ]
        assert current == original, (p, "machine annotation payload changed")
        for a in d.get("existing_annotations", []):
            if a["review"]["action"] == "NEW":
                assert a["review"].get("supported_by"), (p, "new row lacks evidence")
                new_rows.append(
                    {"review_path": r["review_path"], "term": a["term"]["id"]}
                )
        row_count += len(original)
        for path, digest in r["raw_sha256"].items():
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, (
                path
            )
            raw_count += 1
        assert d["id"] == acc and d["status"] == "COMPLETE", p
        actions.update(a["review"]["action"] for a in d.get("existing_annotations", []))
        raw = (p.parent / (r["gene"] + "-uniprot.txt")).read_text()
        assert re.search(
            r"NCBI_TaxID=" + d["taxon"]["id"].split(":")[1] + r"(?:\s|;)", raw
        ), p
        families = re.findall(r"^DR   PANTHER; ([^;]+);", raw, re.M)
        if families:
            members[acc] = next((f for f in families if ":SF" in f), families[0])
    assert not actions["PENDING"]
    planned = yaml.safe_load((DATA / "new-annotations.yaml").read_text())["annotations"]
    def key(annotation):
        return annotation["review_path"], annotation["term"]
    assert sorted(new_rows, key=key) == sorted(planned, key=key), (
        "Unplanned or missing new recommendation"
    )
    p = ROOT / "modules" / (SLUG + ".yaml")
    d = yaml.safe_load(p.read_text())
    gene_proposal = yaml.safe_load(reviews["A0A0H2XFX6"].read_text())[
        "proposed_new_terms"
    ][0]
    module_proposal = next(
        p
        for n in walk(d["module"])
        for p in n.get("proposed_terms", [])
        if p["proposed_name"] == "pApA hydrolase activity"
    )
    for key in ["proposed_name", "proposed_definition"]:
        assert gene_proposal[key] == module_proposal[key], (
            "canonical pApA proposal",
            key,
        )
    used = {
        n["id"].split(":", 1)[1]
        for n in walk(d["module"])
        if str(n.get("id", "")).startswith("UniProtKB:")
    }
    assert used == set(reviews), (used - set(reviews), set(reviews) - used)
    annotons = [a for n in walk(d["module"]) for a in n.get("annotons", [])]
    connections = [a for n in walk(d["module"]) for a in n.get("connections", [])]
    assert all(a.get("evidence") for a in annotons + connections)
    quoted = {
        (n["source_id"], n["supporting_text"])
        for n in walk(d)
        if n.get("source_id", "").startswith("PMID:") and n.get("supporting_text")
    }
    quoted.update(
        (n["reference_id"], n["supporting_text"])
        for n in walk(d)
        if n.get("reference_id", "").startswith("PMID:") and n.get("supporting_text")
    )
    quoted.update(
        (r["id"], f["supporting_text"])
        for r in d["references"]
        for f in r.get("findings", [])
        if f.get("supporting_text")
    )
    for ref, q in quoted:
        assert quote_matches(
            q, ROOT / "publications" / (ref.replace(":", "_") + ".md")
        ), (ref, q)
    result = validate_module_file(p, member_index=members, gene_index=reviews)
    report = {
        "valid": result.is_valid,
        "errors": result.errors,
        "warnings": result.warnings,
        "members": len(reviews),
        "original_rows_preserved": row_count,
        "new_recommendations": len(new_rows),
        "raw_sources_preserved": raw_count,
        "actions": dict(actions),
        "activities": len(annotons),
        "connections": len(connections),
        "references": len(d["references"]),
        "findings": sum(len(r.get("findings", [])) for r in d["references"]),
        "distinct_quotes_checked": len(quoted),
        "member_classifications": members,
    }
    (DATA / "validation-results.yaml").write_text(
        yaml.safe_dump(report, sort_keys=False, allow_unicode=True)
    )
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()
