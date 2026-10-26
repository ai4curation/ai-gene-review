"""Bounded production validation using exact local UniProt classifications.

Run: uv run python modules/acetylcholine_signaling-source-analysis/check_module.py
The member list includes the exact VAChT interface protein as well as all direct
module members. It deliberately does not expand every generic module interface.
No release-wide PANTHER index is built; membership comes from the normally
fetched records, independently of the family IDs authored in the module.
"""

from pathlib import Path
import json
import re
import yaml
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
    panel = json.loads((HERE / "members.json").read_text())
    mapping = {}
    gene_index = {}
    for x in panel:
        org, sym, acc = x["organism"], x["symbol"], x["accession"]
        p = ROOT / f"genes/{org}/{sym}/{sym}-ai-review.yaml"
        review = yaml.safe_load(p.read_text())
        assert review["id"] == acc, (p, acc)
        raw = p.with_name(sym + "-uniprot.txt").read_text()
        assert re.search(r"^AC   " + re.escape(acc) + r";", raw, re.M), (p, acc)
        assert "NCBI_TaxID=" + review["taxon"]["id"].split(":")[1] + ";" in raw
        fs = re.findall(r"^DR   PANTHER; ([^;]+);", raw, re.M)
        if fs:
            mapping[acc] = next((f for f in fs if ":SF" in f), fs[0])
        gene_index[acc] = p
    module = ROOT / "modules/acetylcholine_signaling.yaml"
    result = validate_module_file(module, member_index=mapping, gene_index=gene_index)
    data = yaml.safe_load(module.read_text())
    members = {
        x["id"].split(":", 1)[1]
        for x in walk(data)
        if str(x.get("id", "")).startswith("UniProtKB:")
    }
    assert members <= set(gene_index), members - set(gene_index)
    annotons = [a for x in walk(data) for a in x.get("annotons", [])]
    ungrounded = [
        a["id"]
        for a in annotons
        if not any(x.get("family") for x in walk(a["participant"]))
    ]
    assert not ungrounded, ungrounded
    connections = [e for x in walk(data) for e in x.get("connections", [])]
    missing_edge_evidence = [
        (e["source"], e["target"]) for e in connections if not e.get("evidence")
    ]
    report = {
        "valid": result.is_valid,
        "module_status": data.get("status"),
        "errors": result.errors,
        "warnings": result.warnings,
        "review_panel_size": len(panel),
        "direct_member_count": len(members),
        "annotons_with_family_grounding": len(annotons),
        "connections_missing_direct_evidence": missing_edge_evidence,
        "member_mapping": mapping,
    }
    log = ROOT / ".cache/module-audit-logs"
    log.mkdir(exist_ok=True, parents=True)
    (log / "acetylcholine-module-validation.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    print(
        f"Production validation: {result.is_valid}; {len(result.errors)} errors; {len(result.warnings)} warnings."
    )
    print(
        f"{len(panel)} identities checked; {len(annotons)} family-grounded annotons; {len(missing_edge_evidence)} edges still require evidence."
    )
    for e in result.errors:
        print("ERROR:", e)
    raise SystemExit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()
