"""Additive PR6175 capacity closure using the preserved production-compiler oracle.

Run from repository root with uv run python <this file>. All outputs stay here.
"""

import hashlib
import importlib.util
import json
import subprocess
from dataclasses import asdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
AUDIT = HERE.parents[1]
OLD = AUDIT / "capacity-consultation"
MODULE = ROOT / "modules/bacterial_isc_iron_sulfur_cluster_assembly.yaml"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_yaml(path):
    return yaml.safe_load(path.read_text())


def payload(row):
    return {k: v for k, v in row.items() if k != "review"}


def main():
    prior = json.loads((HERE / "prior-artifacts.json").read_text())
    for name, digest in prior["immutable_prior_artifacts"].items():
        assert sha(ROOT / name) == digest, name
    baseline = json.loads((HERE.parent / "baseline.json").read_text())
    row_count = 0
    for name, old in baseline["reviews"].items():
        new = load_yaml(ROOT / name)
        assert [payload(r) for r in old["existing_annotations"]] == [
            payload(r) for r in new["existing_annotations"]
        ], name
        assert new["status"] == "COMPLETE", name
        row_count += len(new["existing_annotations"])
        for a, b in zip(
            old["existing_annotations"], new["existing_annotations"], strict=True
        ):
            if a["review"]["action"] == "NEW":
                assert b["review"]["action"] == "NEW", name
    for name, digest in baseline["protected_files_sha256"].items():
        assert sha(ROOT / name) == digest, name
    # Verify released reviewer manifests before taking a new current-input snapshot.
    releases = json.loads((HERE / "released-review-manifests.json").read_text())
    release_hashes = {}
    for name, snapshot in releases.items():
        entries = snapshot["document"]["files"]
        assert isinstance(entries, dict)
        for source, digest in entries.items():
            assert sha(ROOT / source) == digest, source
        release_hashes[name] = snapshot["sha256"]
    ledger = load_yaml(OLD / "evidence-ledger.yaml")
    allowed = {
        f"genes/{org}/{gene}/{gene}-ai-review.yaml"
        for org, genes in [
            ("ECOLI", ["hscA", "hscB", "iscS"]),
            ("PSEPK", ["hscA", "hscB"]),
            ("AZOVI", ["iscS", "iscU", "iscA", "hscA", "hscB", "fdx"]),
        ]
        for gene in genes
    }
    changed_inputs = []
    for name, old_hash in ledger["source_sha256"].items():
        new_hash = sha(ROOT / name)
        if new_hash != old_hash:
            assert name in allowed, name
            changed_inputs.append(
                {"path": name, "published_sha256": old_hash, "round1_sha256": new_hash}
            )
            ledger["source_sha256"][name] = new_hash
    # Role tiers, functions, sources and interface bundles remain original decisions.
    (HERE / "evidence-ledger.yaml").write_text(
        yaml.safe_dump(ledger, sort_keys=False, width=100)
    )
    spec = importlib.util.spec_from_file_location(
        "isc_preserved_capacity", OLD / "check_capacity.py"
    )
    old_checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old_checker)
    old_checker.HERE = (
        HERE  # Only its ledger/output location changes, not the oracle or compiler.
    )
    result = old_checker.run()
    original = load_yaml(AUDIT / "root-capacity-results.yaml")
    fields = [
        "name",
        "classification",
        "compiler_satisfied",
        "optional_carrier_supported",
    ]
    assert [{k: x[k] for k in fields} for x in result["tests"]] == [
        {k: x[k] for k in fields} for x in original["tests"]
    ]
    published = subprocess.run(
        [
            "git",
            "show",
            prior["published_head"]
            + ":modules/bacterial_isc_iron_sulfur_cluster_assembly.yaml",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    old_module = yaml.safe_load(published.stdout)
    new_module = load_yaml(MODULE)
    old_description = old_module.pop("description")
    new_description = new_module.pop("description")
    assert old_module == new_module, (
        "Unexpected module change beyond scoped description"
    )
    circuit = old_checker.compile_module(load_yaml(MODULE))
    assert (
        json.loads(json.dumps([asdict(a) for a in old_checker.iter_atoms(circuit)]))
        == original["compiler_atoms"]
    )
    extra = []
    for org in ledger["panels"]:
        for label, functions, expected in [
            ("folding_without_ATP_hydrolysis", ["GO:0044183", "GO:0140662"], False),
            ("ATP_binding_without_hydrolysis", ["GO:0005524"], False),
            ("dedicated_ATPase_without_folding", ["GO:0016887"], True),
        ]:
            panel = old_checker.candidates(ledger, org)
            next(m for m in panel if m["role"] == "hscA")["functions"] = functions
            output = old_checker.Oracle(ledger, org, panel).evaluate(circuit)
            assert output["compiler_satisfied"] is expected, (org, label)
            extra.append({"name": org + "_" + label, "expected": expected, **output})
    for context in [
        "anaerobic_alternative_reductant",
        "scaffold_suppressor_alternative",
    ]:
        # Even a full canonical panel is not positive evidence for an excluded alternative context.
        output = old_checker.Oracle(
            ledger, "ECOLI", old_checker.candidates(ledger, "ECOLI"), context=context
        ).evaluate(circuit)
        assert (
            output["compiler_satisfied"]
            and output["classification"] == "OUTSIDE_CANONICAL_PROFILE"
        )
        extra.append({"name": "full_panel_does_not_validate_" + context, **output})
    for org in ledger["panels"]:
        accession = ledger["panels"][org]["hscA"]
        review = load_yaml(ROOT / ledger["members"][accession]["review_path"])
        core_ids = {
            c["molecular_function"]["id"]
            for c in review["core_functions"]
            if c.get("molecular_function")
        }
        assert "GO:0016887" in core_ids
        assert not core_ids & {"GO:0044183", "GO:0140662"}
        for row in review["existing_annotations"]:
            if row.get("retired"):
                continue
            if row["term"]["id"] in {
                "GO:0044183",
                "GO:0140662",
                "GO:0006457",
                "GO:0042026",
            }:
                assert row["review"]["action"] not in {
                    "ACCEPT",
                    "KEEP_AS_NON_CORE",
                    "NEW",
                }

    # Role-tier and donor-interface evidence are independent. No new direct AZOVI donor assay is inferred.
    donor = next(
        e
        for e in ledger["interfaces"]
        if e["organism"] == "AZOVI" and e["edge"] == "ferredoxin_donor"
    )
    assert (
        donor["tier"] == "QUALIFIED_INFERENCE"
        and donor["mechanism_source_panel"] == "ECOLI"
    )
    assert "PMID:16964969" not in donor["sources"]
    (HERE / "capacity-results.yaml").write_text(
        yaml.safe_dump(result, sort_keys=False, width=100)
    )
    (HERE / "additional-controls.yaml").write_text(
        yaml.safe_dump(extra, sort_keys=False, width=100)
    )
    closure = {
        "status": "PASS",
        "original_scenarios": result["test_count"],
        "additional_scenarios": len(extra),
        "total_scenarios": result["test_count"] + len(extra),
        "gate_sensitivities": result["sensitivity_count"],
        "model_mutations": len(result["mutation_checks"]),
        "ordered_rows_preserved": row_count,
        "protected_sources_preserved": len(baseline["protected_files_sha256"]),
        "prior_artifacts_preserved": len(prior["immutable_prior_artifacts"]),
        "original_outcomes_unchanged": True,
        "compiler_atoms_unchanged": True,
        "module_sha256": sha(MODULE),
        "family_review_sha256": {
            name: sha(ROOT / name) for name in baseline["families"]
        },
        "engine_sha256": result["production_engine_sha256"],
        "published_description": old_description,
        "round1_description": new_description,
        "released_review_manifests": release_hashes,
        "updated_input_hash_chain": changed_inputs,
        "ledger_science_unchanged": "Only authorized released review hashes changed; role/interface tiers and sources unchanged.",
        "limits": result["limits"]
        + [
            "Classification alternatives encode one HscA role, not a biologically different pathway.",
            "The compiler Boolean result alone is not evidence for an out-of-scope biological context.",
            "No canonical atom requires generic folding; the historical retired proposal is not a capacity input.",
        ],
    }
    (HERE / "closure.json").write_text(json.dumps(closure, indent=2) + "\n")
    print(
        {
            k: closure[k]
            for k in [
                "status",
                "total_scenarios",
                "gate_sensitivities",
                "model_mutations",
                "ordered_rows_preserved",
            ]
        }
    )


if __name__ == "__main__":
    main()
