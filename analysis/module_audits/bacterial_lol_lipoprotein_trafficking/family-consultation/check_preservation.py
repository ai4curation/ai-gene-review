"""Verify immutable family assertions and inputs against pre-edit captures."""

import csv
import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assertion_payload(row):
    return {
        key: value
        for key, value in row.items()
        if key
        not in {
            "assessment",
            "assessment_reason",
            "supported_by",
            "affected_subfamilies",
        }
    }


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    root_baseline = json.loads((HERE.parent / "baseline.json").read_text())
    assert digest(HERE.parent / "baseline.json") == baseline["root_baseline_sha256"]
    failures = []
    protected = dict(root_baseline["protected_files_sha256"])
    protected.update(
        {
            path: value
            for path, value in baseline["family_files_sha256"].items()
            if not path.endswith("-review.yaml")
        }
    )
    for path, expected in protected.items():
        if digest(ROOT / path) != expected:
            failures.append(f"protected input changed: {path}")
    nodes = 0
    terms = 0
    for path, saved in baseline["reviews"].items():
        old = saved["document"]
        current = yaml.safe_load((ROOT / path).read_text())
        old_nodes = [assertion_payload(n) for n in old["node_assessments"]]
        new_nodes = [assertion_payload(n) for n in current["node_assessments"]]
        if old_nodes != new_nodes:
            failures.append(f"ordered assertion payload changed: {path}")
        nodes += len(old_nodes)
        for key in ("family_id", "family_name", "reference_protein"):
            if old[key] != current[key]:
                failures.append(f"identity changed: {path}/{key}")
        old_members = [
            (s["subfamily_id"], s["label"], s.get("representative_members", []))
            for s in old["subfamilies"]
        ]
        new_members = [
            (s["subfamily_id"], s["label"], s.get("representative_members", []))
            for s in current["subfamilies"]
        ]
        if old_members != new_members:
            failures.append(f"original member assignments changed: {path}")
        old_terms = [t["assessed_term"] for t in old["term_assessments"]]
        new_terms = [t["assessed_term"] for t in current["term_assessments"]]
        if old_terms != new_terms:
            failures.append(f"original term assessments removed or reordered: {path}")
        terms += len(old_terms)
    labels = {}
    obo = (ROOT / "interpro/panther/panther.obo").read_text().splitlines()
    for i, line in enumerate(obo):
        if line.startswith("id: PANTHER:") and obo[i + 1].startswith("name: "):
            labels[line[4:]] = obo[i + 1][6:]
    memberships = []
    for path in baseline["reviews"]:
        current = yaml.safe_load((ROOT / path).read_text())
        assert labels[current["family_id"]] == current["family_name"]
        entries = ROOT / Path(path).with_name(
            Path(path).name.replace("-review.yaml", "-entries.csv")
        )
        inventory = {row["id"]: row for row in csv.DictReader(entries.open())}
        for sf in current["subfamilies"]:
            assert labels[sf["subfamily_id"]] == sf["label"]
            for member in sf.get("representative_members", []):
                accession = member["id"].split(":")[-1]
                bare_sf = sf["subfamily_id"].removeprefix("PANTHER:")
                evidence = []
                if (
                    accession in inventory
                    and inventory[accession]["subfamily"] == bare_sf
                ):
                    evidence.append(str(entries.relative_to(ROOT)))
                review_path = member.get("gene_review")
                if review_path:
                    raw = ROOT / review_path.replace("-ai-review.yaml", "-uniprot.txt")
                    if raw.exists() and f"PANTHER; {bare_sf};" in raw.read_text():
                        evidence.append(str(raw.relative_to(ROOT)))
                if not evidence:
                    failures.append(f"no source for membership: {accession}/{bare_sf}")
                memberships.append(
                    {"accession": accession, "subfamily": bare_sf, "sources": evidence}
                )
    local_quotes = 0

    def check_local(value):
        nonlocal local_quotes
        if isinstance(value, dict):
            ref = value.get("reference_id", "")
            quote = value.get("supporting_text")
            if ref.startswith("file:") and quote:
                rel = ref[5:]
                source = ROOT / rel
                if not source.exists():
                    source = ROOT / "genes" / rel

                def clean(text):
                    return re.sub(r"\s+", " ", text).strip()

                assert clean(quote) in clean(source.read_text()), (ref, quote)
                local_quotes += 1
            for child in value.values():
                check_local(child)
        elif isinstance(value, list):
            for child in value:
                check_local(child)

    for path in baseline["reviews"]:
        check_local(yaml.safe_load((ROOT / path).read_text()))
    result = {
        "local_quotes_verified": local_quotes,
        "status": "PASS" if not failures else "FAIL",
        "families": len(baseline["reviews"]),
        "ordered_paint_assertions": nodes,
        "original_term_assessments": terms,
        "protected_files": len(protected),
        "member_assignments": memberships,
        "failures": failures,
    }
    (HERE / "preservation-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))
    assert not failures, failures


if __name__ == "__main__":
    main()
