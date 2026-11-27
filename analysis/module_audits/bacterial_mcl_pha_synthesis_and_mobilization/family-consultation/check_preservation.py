"""Verify original family assertions/sources and targeted scientific changes."""

import copy
import csv
import hashlib
import json
import re
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
FAMILIES = ["PTHR36837", "PTHR43194", "PTHR43433", "PTHR43798"]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def quotes(value, inherited=None):
    if isinstance(value, dict):
        ref = value.get("reference_id", inherited)
        if value.get("supporting_text"):
            yield ref, value["supporting_text"]
        for key, child in value.items():
            if key != "supporting_text":
                yield from quotes(child, ref)
    elif isinstance(value, list):
        for child in value:
            yield from quotes(child, inherited)


def main():
    before = json.loads((HERE / "baseline.json").read_text())
    root = json.loads((HERE.parent / "baseline.json").read_text())
    inputs = {}
    sources = {
        **root["protected_files_sha256"],
        **{
            p: h
            for p, h in before["existing_family_files_sha256"].items()
            if not p.endswith("-review.yaml")
        },
    }
    for path, expected in sources.items():
        assert sha(ROOT / path) == expected, path
        inputs[path] = expected
    old_history = subprocess.check_output(
        [
            "git",
            "ls-tree",
            "-r",
            "--name-only",
            before["head"],
            "--",
            *[f"history/other/{f}" for f in FAMILIES],
        ],
        cwd=ROOT,
        text=True,
    ).splitlines()
    for name in old_history:
        original = subprocess.check_output(
            ["git", "show", f"{before['head']}:{name}"], cwd=ROOT
        )
        expected = hashlib.sha256(original).hexdigest()
        assert sha(ROOT / name) == expected
        inputs[name] = expected
    docs = {
        f: yaml.safe_load((ROOT / f"interpro/panther/{f}/{f}-review.yaml").read_text())
        for f in FAMILIES
    }
    judgments = []
    unchanged_nodes = old_nodes = 0
    for path, previous in before["existing_reviews"].items():
        old = previous["document"]
        family = old["family_id"].split(":")[1]
        current = docs[family]
        for field in ["family_id", "family_name", "reference_protein"]:
            assert old[field] == current[field], (family, field)
        assert len(old["node_assessments"]) == len(current["node_assessments"])
        for a, b in zip(
            old["node_assessments"], current["node_assessments"], strict=True
        ):
            mutable = {
                "assessment",
                "assessment_reason",
                "affected_subfamilies",
                "supported_by",
            }
            assert {k: v for k, v in a.items() if k not in mutable} == {
                k: v for k, v in b.items() if k not in mutable
            }
            old_nodes += 1
            targeted = (
                family == "PTHR43194"
                and a["asserted_term"]["id"]
                in {"GO:0016787", "GO:0090499", "GO:0009102"}
            ) or (
                family == "PTHR43798"
                and a["asserted_term"]["id"] in {"GO:0047372", "GO:0046464"}
            )
            if not targeted:
                assert a == b, (family, a["node_id"], "unrelated node changed")
                unchanged_nodes += 1
            else:
                judgments.append(
                    {
                        "family": family,
                        "node": a["node_id"],
                        "term": a["asserted_term"]["id"],
                        "before": a["assessment"],
                        "after": b["assessment"],
                        "reason": b["assessment_reason"],
                    }
                )
        for a, b in zip(old["subfamilies"], current["subfamilies"], strict=True):
            assert (a["subfamily_id"], a["label"]) == (b["subfamily_id"], b["label"])
            assert all(
                m in b.get("representative_members", [])
                for m in a.get("representative_members", [])
            )
            if not a["subfamily_id"].endswith(":SF5"):
                assert a == b, "unrelated AcoC subfamily changed"
        for i, a in enumerate(old["term_assessments"]):
            b = current["term_assessments"][i]
            assert a["assessed_term"] == b["assessed_term"]
            if family == "PTHR43798" and a["assessed_term"]["id"] == "GO:0016787":
                assert a == b, "unrelated AcoC hydrolase exception changed"
        assert all(ref in current["references"] for ref in old["references"])
    # New family copies all seven raw assertions exactly; no synthetic PhaC PAINT assertions.
    raw = list(
        csv.DictReader(
            (ROOT / "interpro/panther/PTHR43433/PTHR43433-paint.tsv").open(),
            delimiter="\t",
        )
    )
    assert len(raw) == len(docs["PTHR43433"]["node_assessments"]) == 7
    for a, b in zip(raw, docs["PTHR43433"]["node_assessments"], strict=True):
        assert (
            b["node_id"] == "PANTHER:" + a["node"]
            and b["asserted_term"]["id"] == a["go_id"]
        )
        assert b["evidence"] == a["evidence"] and b["negated"] == (
            a["negated"] == "true"
        )
        assert b["paint_snapshot"] == a["date"]
        assert [x["id"] for x in b["seeds"]] == a["seeds"].split("|")
        assert b.get("node_taxon", {}).get("id") == (
            a["taxon"].replace("taxon:", "NCBITaxon:")
            if a["taxon"] != "taxon:"
            else None
        )
    assert docs["PTHR36837"]["node_assessments"] == []
    assert not (ROOT / "interpro/panther/PTHR36837/PTHR36837-paint.tsv").exists()
    assert "no node-level annotations" in (HERE / "fetch-missing-paint.log").read_text()
    archived = json.loads((HERE / "prior-term-assessments.json").read_text())
    old43194 = before["existing_reviews"][
        "interpro/panther/PTHR43194/PTHR43194-review.yaml"
    ]["document"]
    assert [x["original"] for x in archived] == old43194["term_assessments"]
    active = yaml.safe_load((HERE / "current-member-judgments.yaml").read_text())
    original = old43194["term_assessments"][0]["member_exceptions"][0]
    assert active["current_judgments"][0]["member_exception"] == original
    assert active["current_judgments"][0]["judgment"] == "DOES_NOT_HOLD"
    assert active["current_judgments"][0]["status"] == "CURRENT"
    control = copy.deepcopy(docs["PTHR43194"])
    control["term_assessments"][0]["member_exceptions"] = [original]
    failure = check_member_exceptions(control, {})
    assert len(failure) == 1 and "EXCEPTION_OUTSIDE_SCOPE" in str(failure[0])
    assert "CONFLICT" in str(failure[0])
    trees = json.loads((HERE / "trees-compact.json").read_text())
    tree_counts = {}
    for f in FAMILIES:
        source = HERE / f"{f}-tree.json"
        assert compact_tree(json.loads(source.read_text())) == trees[f]
        inputs[str(source.relative_to(ROOT))] = sha(source)
        tree_counts[f] = len(trees[f]["leaves"])
    assert len(trees["PTHR43798"]["under"]["PTN002465558"]) == 49
    assert all(v["uniprot"] != "P26495" for v in trees["PTHR43798"]["leaves"].values())
    targets = {
        "P23608": "PTHR36837:SF5",
        "Q88D25": "PTHR36837:SF5",
        "Q88D23": "PTHR36837:SF5",
        "P26494": "PTHR36837:SF5",
        "P26496": "PTHR36837:SF5",
        "O85207": "PTHR43194:SF5",
        "Q51553": "PTHR43194:SF5",
        "Q88D24": "PTHR43433:SF5",
        "P26495": "PTHR43798:SF5",
    }
    for accession, family in targets.items():
        path = HERE / f"{accession}-uniprot.json"
        record = json.loads(path.read_text())
        assert any(
            r["database"] == "PANTHER" and r["id"] == family
            for r in record["uniProtKBCrossReferences"]
        )
        inputs[str(path.relative_to(ROOT))] = sha(path)
    primary = json.loads((HERE / "primary-excerpt-proof.json").read_text())
    source = ROOT / primary["source"]
    assert sha(source) == primary["sha256"]
    normalized = re.sub(r"\s+", " ", source.read_text())
    assert all(q in normalized for q in primary["quotes"])
    inputs[primary["source"]] = sha(source)
    inputs["src/ai_gene_review/validation/family_gene_crosscheck.py"] = sha(
        ROOT / "src/ai_gene_review/validation/family_gene_crosscheck.py"
    )
    validator, _ = build_supporting_text_validator(ROOT / "publications")
    quote_ledger = []
    for f, doc in docs.items():
        assert doc["review_status"] == "COMPLETE"
        for ref, text in sorted(set(quotes(doc))):
            if ref.startswith("file:"):
                source = resolve_local_source(ref, ROOT)
                assert source and quote_matches(text, source), (f, ref, text)
            else:
                result = validator.validate(text, ref)
                assert result.is_valid and not result.skipped, (f, ref, result.message)
                source = ROOT / "publications" / (ref.replace(":", "_") + ".md")
            inputs[str(source.relative_to(ROOT))] = sha(source)
            quote_ledger.append(
                {
                    "family": f,
                    "reference": ref,
                    "supporting_text": text,
                    "source_sha256": sha(source),
                }
            )
    result = {
        "status": "PASS",
        "existing_node_payloads_preserved": old_nodes,
        "old_family_history_files_preserved": len(old_history),
        "new_nodes_match_raw": 7,
        "unrelated_nodes_exact": unchanged_nodes,
        "original_protected_sources": len(root["protected_files_sha256"]),
        "existing_family_sources": len(before["existing_family_files_sha256"]) - 2,
        "original_subfamily_labels_and_members_preserved": True,
        "exact_official_target_assignments": targets,
        "tree_leaf_counts": tree_counts,
        "paint_scope_changes": judgments,
        "AcoC_current_negative_retained": True,
        "production_enforcement_limit": str(failure[0]),
        "quote_count": len(quote_ledger),
        "quotes": quote_ledger,
        "inputs_sha256": dict(sorted(inputs.items())),
    }
    (HERE / "preservation.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    )
    print(
        json.dumps({k: v for k, v in result.items() if not isinstance(v, (dict, list))})
    )


if __name__ == "__main__":
    main()
