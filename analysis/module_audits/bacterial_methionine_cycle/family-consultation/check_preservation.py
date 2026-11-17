"""Check immutable inputs, PAINT identity/order, exact quotations and boundary cases."""

import csv
import hashlib
import json
import subprocess
from pathlib import Path

import yaml

from ai_gene_review.etl.panther_trees import compact_tree
from ai_gene_review.validation.local_source_text import (
    quote_matches,
    resolve_local_source,
)
from ai_gene_review.validation.supporting_text import build_supporting_text_validator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FAMILIES = [
    "PTHR11964",
    "PTHR23420",
    "PTHR46832",
    "PTHR35799",
    "PTHR45833",
    "PTHR30519",
]
TARGETED = {
    "PTHR11964": {"GO:0004478", "GO:0006556"},
    "PTHR23420": {"GO:0004013", "GO:0033353"},
    "PTHR46832": {"GO:0008782", "GO:0008930"},
    "PTHR45833": {"GO:0008705"},
    "PTHR30519": {"GO:0003871", "GO:0008705", "GO:0071265"},
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def quotes(x):
    if isinstance(x, dict):
        if x.get("supporting_text"):
            yield x["reference_id"], x["supporting_text"]
        for v in x.values():
            yield from quotes(v)
    elif isinstance(x, list):
        for v in x:
            yield from quotes(v)


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    root = json.loads((HERE.parent / "baseline.json").read_text())
    inputs = {
        **root["protected_files_sha256"],
        **{
            p: h
            for p, h in baseline["existing_files_sha256"].items()
            if not p.endswith("-review.yaml")
        },
    }
    for p, h in inputs.items():
        assert sha(ROOT / p) == h, ("protected source", p)
    old_history = subprocess.check_output(
        [
            "git",
            "ls-tree",
            "-r",
            "--name-only",
            root["head"],
            "--",
            *["history/other/" + f for f in FAMILIES],
        ],
        cwd=ROOT,
        text=True,
    ).splitlines()
    for p in old_history:
        expected = hashlib.sha256(
            subprocess.check_output(["git", "show", root["head"] + ":" + p], cwd=ROOT)
        ).hexdigest()
        assert sha(ROOT / p) == expected, p
        inputs[p] = expected
    docs = {
        f: yaml.safe_load((ROOT / f"interpro/panther/{f}/{f}-review.yaml").read_text())
        for f in FAMILIES
    }
    old_count = unchanged = 0
    ledger = []
    for p, old in baseline["reviews"].items():
        a = old["document"]
        f = a["family_id"].split(":")[1]
        b = docs[f]
        for key in ["family_id", "family_name", "reference_protein"]:
            assert a[key] == b[key], (f, key)
        for x, y in zip(a["subfamilies"], b["subfamilies"], strict=True):
            if f in {"PTHR23420", "PTHR30519"} and x["subfamily_id"].endswith(":SF0"):
                assert {k: v for k, v in x.items() if k != "description"} == {
                    k: v for k, v in y.items() if k != "description"
                }
            else:
                assert x == y, (f, "unrelated subfamily changed")
        assert all(r in b["references"] for r in a["references"])
        assert len(b["node_assessments"]) >= len(a["node_assessments"])
        for x, y in zip(a["node_assessments"], b["node_assessments"]):
            mutable = {"assessment", "assessment_reason", "supported_by"}
            assert {k: v for k, v in x.items() if k not in mutable} == {
                k: v for k, v in y.items() if k not in mutable
            }, (f, x["node_id"])
            old_count += 1
            if x["asserted_term"]["id"] not in TARGETED[f]:
                assert x == y, (f, "unrelated node changed")
                unchanged += 1
            elif x != y:
                ledger.append(
                    {
                        "family": f,
                        "node": x["node_id"],
                        "term": x["asserted_term"]["id"],
                        "old": x["assessment"],
                        "new": y["assessment"],
                        "reason": y["assessment_reason"],
                    }
                )
    raw_additions = 0
    for f, d in docs.items():
        old_n = len(
            baseline["reviews"]
            .get(f"interpro/panther/{f}/{f}-review.yaml", {})
            .get("document", {})
            .get("node_assessments", [])
        )
        raw = list(
            csv.DictReader(
                (ROOT / f"interpro/panther/{f}/{f}-paint.tsv").open(), delimiter="\t"
            )
        )
        assert len(d["node_assessments"]) == len(raw), f
        for n in d["node_assessments"][old_n:]:
            r = next(
                r
                for r in raw
                if "PANTHER:" + r["node"] == n["node_id"]
                and r["go_id"] == n["asserted_term"]["id"]
            )
            assert n["evidence"] == r["evidence"] and n["negated"] == (
                r["negated"] == "true"
            )
            assert n["paint_snapshot"] == r["date"]
            assert [s["id"] for s in n["seeds"]] == r["seeds"].split("|")
            assert n.get("node_taxon", {}).get("id") == (
                "NCBITaxon:" + r["taxon"][6:] if r["taxon"][6:] else None
            )
            raw_additions += 1
    trees = json.loads((HERE / "trees-compact.json").read_text())
    for f in FAMILIES:
        assert (
            compact_tree(json.loads((HERE / (f + "-tree.json")).read_text()))
            == trees[f]
        )
    loss = next(n for n in docs["PTHR23420"]["node_assessments"] if n.get("negated"))
    assert loss["assessment"] == "LOSS_SUPPORTED"
    lt = trees["PTHR23420"]
    assert {"PTHR23420:SF0", "PTHR23420:SF2", "PTHR23420:SF3"} == {
        lt["leaves"][p]["subfamily"] for p in lt["under"]["PTN001158976"]
    }
    assert docs["PTHR30519"]["term_assessments"][0]["scope"] == "UNRESOLVED"
    assert docs["PTHR45833"]["term_assessments"][0]["scope"] == "UNRESOLVED"
    assert docs["PTHR35799"]["term_assessments"][1]["scope"] == "UNRESOLVED"
    validator, _ = build_supporting_text_validator()
    quote_ledger = []
    for f, d in docs.items():
        for ref, q in sorted(set(quotes(d))):
            if ref.startswith("file:"):
                source = resolve_local_source(ref, ROOT)
                assert source and quote_matches(q, source), (f, ref, q)
            else:
                result = validator.validate(q, ref)
                assert result.is_valid and not result.skipped, (f, ref, result.message)
                source = ROOT / "publications" / (ref.replace(":", "_") + ".md")
            inputs[str(source.relative_to(ROOT))] = sha(source)
            quote_ledger.append(
                {
                    "family": f,
                    "reference": ref,
                    "supporting_text": q,
                    "sha256": sha(source),
                }
            )
    result = {
        "status": "PASS",
        "old_PAINT_payloads_preserved": old_count,
        "unrelated_nodes_exact": unchanged,
        "additive_raw_nodes": raw_additions,
        "old_histories_exact": len(old_history),
        "protected_sources": len(root["protected_files_sha256"]),
        "current_loss_retained": True,
        "judgment_changes": ledger,
        "quotes": quote_ledger,
        "inputs_sha256": dict(sorted(inputs.items())),
    }
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print({k: v for k, v in result.items() if not isinstance(v, (dict, list))})


if __name__ == "__main__":
    main()
