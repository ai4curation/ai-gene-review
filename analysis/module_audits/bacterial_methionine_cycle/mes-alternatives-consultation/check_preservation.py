"""Prove seed/source preservation and verify every source quotation in three reviews."""

import hashlib
import json
from pathlib import Path

import yaml

from ai_gene_review.validation.local_source_text import (
    quote_matches,
    resolve_local_source,
)
from ai_gene_review.validation.supporting_text import build_supporting_text_validator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def quotations(value, inherited=None):
    if isinstance(value, dict):
        ref = value.get("reference_id", value.get("id", inherited))
        if value.get("supporting_text"):
            yield ref, value["supporting_text"]
        for key, child in value.items():
            if key != "supporting_text":
                yield from quotations(child, ref)
    elif isinstance(value, list):
        for child in value:
            yield from quotations(child, inherited)


def main():
    base = json.loads((HERE / "baseline.json").read_text())
    inputs = dict(base["protected_sources_sha256"])
    for p, h in inputs.items():
        assert sha(ROOT / p) == h, p
    family_path = HERE.parent / "family-consultation/handoff.json"
    assert (
        sha(family_path)
        == "7cd8a6927d71896e9969ea868435cb2b648a31eafbba87b24faa05c2320f4563"
    )
    family = json.loads(family_path.read_text())
    for p, h in family["files"].items():
        assert sha(ROOT / p) == h, ("frozen family changed", p)
    validator, _ = build_supporting_text_validator(ROOT / "publications")
    ledger = []
    quotes = []
    preserved = 0
    docs = {}
    for key, seed in base["seeds"].items():
        org, gene = key.split("/")
        path = ROOT / f"genes/{org}/{gene}/{gene}-ai-review.yaml"
        d = yaml.safe_load(path.read_text())
        docs[key] = d
        old = seed["review"]
        assert all(
            d[k] == old[k] for k in ["id", "gene_symbol", "taxon", "product_type"]
        )
        original_rows = old.get("existing_annotations", [])
        rows = d.get("existing_annotations", [])
        assert len(rows) >= len(original_rows)
        for i, original in enumerate(original_rows):
            row = rows[i]
            assert {k: v for k, v in row.items() if k != "review"} == {
                k: v for k, v in original.items() if k != "review"
            }, (key, i)
            preserved += 1
            ledger.append(
                {
                    "gene": key,
                    "row": i,
                    "term": original["term"]["id"],
                    "before": original["review"]["action"],
                    "after": row["review"]["action"],
                    "source_payload_unchanged": True,
                }
            )
        if key == "DEHMC/cbdbA481":
            assert len(rows) == 1
            row = rows[0]
            assert (
                row["term"]["id"],
                row["evidence_type"],
                row["original_reference_id"],
                row["review"]["action"],
            ) == ("GO:0008172", "IDA", "PMID:32034217", "NEW")
            assert not row.get("retired", False)
        else:
            assert len(rows) == len(original_rows)
        assert d["status"] == "COMPLETE"
        for ref, quote in sorted(set(quotations(d))):
            if ref.startswith("file:"):
                source = resolve_local_source(ref, ROOT)
                assert source and quote_matches(quote, source), (key, ref, quote)
            else:
                source = ROOT / "publications" / (ref.replace(":", "_") + ".md")
                result = validator.validate(quote, ref)
                assert result.is_valid and not result.skipped, (
                    key,
                    ref,
                    result.message,
                )
            inputs[str(source.relative_to(ROOT))] = sha(source)
            quotes.append(
                {
                    "gene": key,
                    "reference": ref,
                    "supporting_text": quote,
                    "source_sha256": sha(source),
                }
            )
        for ref in d.get("references", []):
            assert ref.get("reference_review"), (key, ref["id"])
            if ref["id"].startswith("PMID:"):
                meta = yaml.safe_load(
                    (ROOT / "publications" / (ref["id"].replace(":", "_") + ".md"))
                    .read_text()
                    .split("---")[1]
                )
                assert ref["title"] == meta["title"]
        assert not list(
            (ROOT / f"genes/{org}/{gene}").glob("*-deep-research-falcon.md")
        ), "Failed provider must not be fabricated"
    assert not docs["ACIAD/ACIAD3524"].get("core_functions")
    assert not docs["ACIAD/ACIAD3524"].get("proposed_new_terms")
    assert (
        docs["ACIAD/ACIAD3523"]["existing_annotations"][1]["review"]["action"]
        == "ACCEPT"
    )
    assert (
        docs["ACIAD/ACIAD3523"]["core_functions"][0]["molecular_function"]["id"]
        == "GO:0008172"
    )
    children = json.loads((HERE / "s-methyltransferase-children.json").read_text())
    assert len(children["results"]) == 12
    assert all(
        "methylcobalamin" not in t["definition"]["text"].lower()
        for t in children["results"]
    )
    result = {
        "status": "PASS",
        "original_ordered_payloads": preserved,
        "original_qualifiers_and_lifecycle_unchanged": True,
        "new_annotations": 1,
        "new_process_annotations": 0,
        "historical_NEW_before": 0,
        "active_NEW_after": 1,
        "retired_NEW_after": 0,
        "protected_raw_and_publications": len(base["protected_sources_sha256"]),
        "frozen_family_files_unchanged": len(family["files"]),
        "action_ledger": ledger,
        "quotes": quotes,
        "inputs_sha256": dict(sorted(inputs.items())),
        "limits": [
            "MesX has no established molecular activity; core omission is deliberate.",
            "MesD oxygen/donor constraints include comparative assays, not purified ADP1 measurements.",
            "MesB free-methylcobalamin assay does not prove native AcsCD donor transfer.",
            "PAINT lineage lookup is unresolved for absent target leaves/family identifiers, not evidence of no loss.",
        ],
    }
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print({k: v for k, v in result.items() if not isinstance(v, (dict, list))})


if __name__ == "__main__":
    main()
