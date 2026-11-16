"""Verify current Lol closure with exact additive supersession and source quotes."""

import hashlib
import importlib.util
import json
from pathlib import Path

import yaml

from ai_gene_review.validation.local_source_text import (
    quote_matches,
    resolve_local_source,
)
from ai_gene_review.validation.supporting_text import build_supporting_text_validator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FOLLOWUP = HERE.parent
AUDIT = FOLLOWUP.parent
OLD = AUDIT / "capacity-consultation"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    release_path = FOLLOWUP / "handoff.json"
    assert sha(release_path) == baseline["followup_handoff_sha256"]
    release = json.loads(release_path.read_text())
    inputs = {}
    for field in ["files", "source_dependencies", "original_receipts_preserved"]:
        for name, expected in release[field].items():
            assert sha(ROOT / name) == expected, (field, name)
            inputs[name] = expected
    assert len(release["source_dependencies"]) == 278
    inputs[str(release_path.relative_to(ROOT))] = sha(release_path)
    for name, expected in baseline["historical_receipts"].items():
        assert sha(ROOT / name) == expected, name
    changes = json.loads((FOLLOWUP / "preservation-supersession.json").read_text())[
        "updated_files"
    ]
    changes = dict(changes)
    for name, before in baseline["files"].items():
        changes[name] = {"before_sha256": before, "after_sha256": sha(ROOT / name)}
    module_path = ROOT / "modules/bacterial_lol_lipoprotein_trafficking.yaml"
    current = yaml.safe_load(module_path.read_text())
    expected = baseline["module_document"]
    labels = json.loads((FOLLOWUP / "module-record-labels.json").read_text())

    def names(node):
        if isinstance(node, dict):
            if node.get("id", "").startswith("UniProtKB:"):
                node["label"] = labels[node["id"]]["name"]
            for value in node.values():
                names(value)
        elif isinstance(node, list):
            for value in node:
                names(value)

    names(expected)
    assert current == expected, "Change beyond source-name labels"
    historical = json.loads((OLD / "handoff.json").read_text())
    relocations = json.loads(
        (FOLLOWUP / "historical-source-copy-receipt.json").read_text()
    )
    superseded = []
    for name, expected_hash in historical["input_sha256"].items():
        physical = relocations.get(name, {}).get("durable_path", name)
        actual = sha(ROOT / physical)
        if actual != expected_hash:
            assert name in changes, ("Unapproved original-capacity input delta", name)
            assert changes[name]["before_sha256"] == expected_hash, (
                "Unexpected intermediate revision",
                name,
            )
            assert actual == changes[name]["after_sha256"]
            superseded.append(
                {
                    "path": name,
                    "original_capacity_sha256": expected_hash,
                    "current_sha256": actual,
                }
            )
        inputs[physical] = actual
    # Reuse the original quotation traversal and the production matching helpers, not its old-manifest assertions.
    spec = importlib.util.spec_from_file_location(
        "lol_original_closure", OLD / "check_closure.py"
    )
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    members = json.loads((HERE / "original-rerun/member-closure.json").read_text())
    paths = [module_path, OLD / "boundary-evidence.yaml"] + [
        ROOT / m["path"] for m in members.values()
    ]
    validator, _ = build_supporting_text_validator(ROOT / "publications")
    quotes = []
    for path in paths:
        inputs[str(path.relative_to(ROOT))] = sha(path)
        seen = set()
        for ref, quote in helper.quotations(yaml.safe_load(path.read_text())):
            if (ref, quote) in seen:
                continue
            seen.add((ref, quote))
            result = validator.validate(quote, ref, path=str(path))
            valid, skipped = result.is_valid, result.skipped
            if ref.startswith("file:"):
                source = resolve_local_source(ref, ROOT)
                valid = bool(source and quote_matches(quote, source))
                skipped = False
            else:
                assert ref.startswith("PMID:"), ref
                source = ROOT / "publications" / (ref.replace(":", "_") + ".md")
            assert valid and not skipped, (str(path), ref, quote, result.message)
            assert source and source.is_file(), ref
            inputs[str(source.relative_to(ROOT))] = sha(source)
            quotes.append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "reference": ref,
                    "quotation": quote,
                    "valid": True,
                }
            )
    history = (HERE / "history-command.log").read_text().splitlines()
    history = [line.strip() for line in history if line.startswith("history/")]
    assert len(history) == 1, history
    for name in [
        *baseline["files"],
        history[0],
        str(ROOT.joinpath("src/ai_gene_review/module_logic.py").relative_to(ROOT)),
    ]:
        inputs[name] = sha(ROOT / name)
    manifest_supersessions = []
    for name, digest in baseline["historical_receipts"].items():
        old_manifest = json.loads((ROOT / name).read_text())
        entries = []
        for field in [
            "files",
            "files_sha256",
            "input_closure",
            "input_sha256",
            "source_dependencies",
        ]:
            if not isinstance(old_manifest.get(field), dict):
                continue
            for path, recorded in old_manifest[field].items():
                if (
                    path in changes
                    and changes[path]["before_sha256"] != changes[path]["after_sha256"]
                ):
                    entries.append(
                        {
                            "field": field,
                            "path": path,
                            "recorded_sha256": recorded,
                            **changes[path],
                        }
                    )
        if entries:
            manifest_supersessions.append(
                {
                    "manifest": name,
                    "manifest_sha256_preserved": digest,
                    "entries": entries,
                }
            )
    receipt = {
        "status": "PASS",
        "verified_gene_release": {
            "path": str(release_path.relative_to(ROOT)),
            "sha256": sha(release_path),
        },
        "all_followup_source_dependencies_checked": 278,
        "historical_receipts_preserved": baseline["historical_receipts"],
        "module_label_only": True,
        "historical_manifest_supersessions": manifest_supersessions,
        "module_updates": {n: changes[n] for n in baseline["files"]},
        "gene_updates": {n: v for n, v in changes.items() if n.startswith("genes/")},
        "original_capacity_input_supersessions": superseded,
        "original_capacity_handoff": {
            "path": str((OLD / "handoff.json").relative_to(ROOT)),
            "sha256": sha(OLD / "handoff.json"),
        },
        "member_count": len(members),
        "quote_count": len(quotes),
        "quotations": quotes,
        "source_dependencies": inputs,
        "module_history": history[0],
        "source_qualifier_uncertainty": "Fjoh_2111 retains ACCEPT and its literal broad positive-within qualifier. SUSPECTED/CHECK asks for relation precision, without claiming a confirmed error. Capacity uses source-supported inferred carrier activity, not the qualifier as an activity oracle.",
        "dependency_hold": "PR6186 merge dependency remains unchanged.",
    }
    (HERE / "current-closure.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        json.dumps(
            {
                "status": "PASS",
                "followup_dependencies": 278,
                "current_inputs": len(inputs),
                "original_capacity_inputs_superseded": len(superseded),
                "quotes": len(quotes),
                "members": len(members),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
