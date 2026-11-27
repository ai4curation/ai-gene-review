"""Verify exact protected inputs, PAINT payloads, unchanged judgments and quotes."""

import copy
import gzip
import hashlib
import json
import subprocess
from pathlib import Path

import yaml
from ai_gene_review.etl.panther_trees import compact_tree
from ai_gene_review.validation.family_gene_crosscheck import check_member_exceptions
from ai_gene_review.validation.local_source_text import (
    quote_matches,
    resolve_local_source,
)
from ai_gene_review.validation.supporting_text import build_supporting_text_validator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
TARGETS = {
    "PTHR30035": set(),
    "PTHR36573": {"GO:0030288", "GO:0120010"},
    "PTHR43023": {"GO:0120014", "GO:0006869", "GO:0120010"},
    "PTHR30188": {"GO:0015914"},
    "PTHR33371": {"GO:0120014", "GO:0120010"},
    "PTHR35849": {"GO:0120014", "GO:0006974"},
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def quotes(obj):
    if isinstance(obj, dict):
        if obj.get("supporting_text"):
            yield obj["reference_id"], obj["supporting_text"]
        for value in obj.values():
            yield from quotes(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from quotes(value)


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    root = yaml.safe_load((HERE.parent / "baseline.yaml").read_text())
    protected = {
        p: h
        for p, h in root["source_files_sha256"].items()
        if not p.endswith("-review.yaml") and not p.startswith("modules/")
    }
    protected.update(
        {
            p: h
            for p, h in baseline["existing_files_sha256"].items()
            if not p.endswith("-review.yaml")
        }
    )
    for path, h in protected.items():
        assert sha(ROOT / path) == h, ("protected input changed", path)
    histories = subprocess.check_output(
        [
            "git",
            "ls-tree",
            "-r",
            "--name-only",
            root["base"],
            "--",
            *[
                f"history/other/{f}{suffix}"
                for f in TARGETS
                for suffix in ["", "-family-review"]
            ],
        ],
        cwd=ROOT,
        text=True,
    ).splitlines()
    for path in histories:
        assert (ROOT / path).read_bytes() == subprocess.check_output(
            ["git", "show", root["base"] + ":" + path], cwd=ROOT
        ), path
    docs = {}
    nodes = []
    unchanged = 0
    scope_changes = json.loads((HERE / "scope-changes.json").read_text())
    expected_scope = {(x["family"], x["term"]): x for x in scope_changes}
    for path, old in baseline["reviews"].items():
        before = old["document"]
        after = yaml.safe_load((ROOT / path).read_text())
        f = before["family_id"].split(":")[-1]
        docs[f] = after
        for key in [
            "family_id",
            "family_name",
            "reference_protein",
            "review_date",
            "reviewed_by",
            "review_status",
        ]:
            assert before.get(key) == after.get(key), (f, key)
        assert all(r in after["references"] for r in before["references"]), (
            f,
            "original reference changed",
        )
        for a, b in zip(before["subfamilies"], after["subfamilies"], strict=True):
            assert a["subfamily_id"] == b["subfamily_id"] and a["label"] == b["label"]
            assert (
                a.get("representative_members", [])
                == b.get("representative_members", [])[
                    : len(a.get("representative_members", []))
                ]
            )
        for a, b in zip(
            before["node_assessments"], after["node_assessments"], strict=True
        ):
            immutable = set(a) | set(b) - {"assessment", "assessment_reason"}
            immutable -= {"assessment", "assessment_reason"}
            assert {k: a[k] for k in immutable if k in a} == {
                k: b[k] for k in immutable if k in b
            }, (f, a["node_id"], "PAINT payload/support changed")
            if a["asserted_term"]["id"] not in TARGETS[f]:
                assert a == b, (f, "unrelated node changed", a["node_id"])
                unchanged += 1
            nodes.append(
                {
                    "family": f,
                    "node": a["node_id"],
                    "term": a["asserted_term"]["id"],
                    "old": a["assessment"],
                    "new": b["assessment"],
                    "payload_exact": True,
                    "object_exact": a == b,
                }
            )
        for a, b in zip(
            before["term_assessments"], after["term_assessments"], strict=True
        ):
            key = (f, a["assessed_term"]["id"])
            if key not in expected_scope:
                assert a == b, (key, "unrelated term changed")
            else:
                assert a == expected_scope[key]["before"]
                assert a["assessed_term"] == b["assessed_term"]
                assert all(
                    x in b.get("supported_by", []) for x in a.get("supported_by", [])
                )
    archive = json.loads((HERE / "original-member-exceptions.json").read_text())
    for row in archive:
        original = next(
            t
            for t in baseline["reviews"][
                f"interpro/panther/{row['family']}/{row['family']}-review.yaml"
            ]["document"]["term_assessments"]
            if t["assessed_term"]["id"] == row["term"]
        )
        assert row["original_exception"] in original["member_exceptions"]
    current = json.loads((HERE / "current-member-assessments.json").read_text())
    assert len(archive) == len(current) == 13
    live = [x for x in current if x["status"] == "CURRENT_SUPPORTED_NEGATIVE"]
    assert len(live) == 1 and live[0]["member"]["id"] == "UniProtKB:Q8L4R0"
    loss = next(
        x
        for x in docs["PTHR30188"]["node_assessments"]
        if x["assessment"] == "LOSS_SUPPORTED"
    )
    assert loss["node_id"] == "PANTHER:PTN001575509"
    control = copy.deepcopy(docs["PTHR30188"])
    ta = next(
        t
        for t in control["term_assessments"]
        if t["assessed_term"]["id"] == "GO:0005886"
    )
    ta["member_exceptions"] = [
        next(
            x["original_exception"]
            for x in archive
            if x["family"] == "PTHR30188" and x["term"] == "GO:0005886"
        )
    ]
    violations = check_member_exceptions(control, {})
    assert any(
        x.kind == "EXCEPTION_OUTSIDE_SCOPE" and x.verdict.value == "CONFLICT"
        for x in violations
    )
    trees = json.loads((HERE / "trees-compact.json").read_text())
    for f, t in trees.items():
        assert t == compact_tree(
            json.loads(gzip.decompress((HERE / f"{f}-tree.json.gz").read_bytes()))
        )
    plant = trees["PTHR30188"]["under"]["PTN001575509"]
    assert len(plant) == 50 and {
        trees["PTHR30188"]["leaves"][n]["subfamily"] for n in plant
    } == {"PTHR30188:SF4", "PTHR30188:SF14"}
    source_hashes = dict(protected)
    validator, _ = build_supporting_text_validator(ROOT / "publications")
    ledger = []
    for f, d in sorted(docs.items()):
        for ref, q in sorted(set(quotes(d))):
            if ref.startswith("file:"):
                source = resolve_local_source(ref, ROOT)
                assert source and quote_matches(q, source), (f, ref, q)
            else:
                result = validator.validate(q, ref)
                assert result.is_valid and not result.skipped, (
                    f,
                    ref,
                    result.message,
                    q,
                )
                source = ROOT / "publications" / (ref.replace(":", "_") + ".md")
            source_hashes[str(source.relative_to(ROOT))] = sha(source)
            ledger.append(
                {
                    "family": f,
                    "reference": ref,
                    "supporting_text": q,
                    "source_sha256": sha(source),
                }
            )
    result = {
        "status": "PASS",
        "original_PAINT_payloads": len(nodes),
        "unrelated_node_objects_exact": unchanged,
        "old_histories_exact": len(histories),
        "protected_files_exact": len(protected),
        "quotes_checked": len(ledger),
        "original_member_exception_objects_exact": len(archive),
        "current_TGD1_negative_retained": True,
        "production_exception_control": [str(x) for x in violations],
        "production_limit": "The current member ledger is not consumed by family_gene_crosscheck. The original LOSS_SUPPORTED PAINT node remains live; production cannot express an isolated member exception under UNRESOLVED.",
        "node_changes": nodes,
        "inputs_sha256": dict(sorted(source_hashes.items())),
    }
    (HERE / "quotes.json").write_text(
        json.dumps(ledger, indent=2, sort_keys=True) + "\n"
    )
    (HERE / "preservation.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print({k: v for k, v in result.items() if not isinstance(v, (dict, list))})


if __name__ == "__main__":
    main()
