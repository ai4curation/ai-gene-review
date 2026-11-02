"""Batching must retain every input and propagate failures from every phase."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    "recipe,failed_phase",
    [
        ("validate-families", ""),
        ("validate-families", "linkml-validate"),
        ("validate-families", "linkml-term-validator"),
        ("validate-families", "references"),
        ("validate-families", "ai_gene_review.validation.family_residue_validator"),
        ("validate-families", "ai_gene_review.validation.family_gene_crosscheck"),
        ("validate-families", "ai_gene_review.validation.gene_residue_claims"),
        ("validate-modules", ""),
        ("validate-modules", "linkml-validate"),
        ("validate-modules", "ai_gene_review.validation.module_validator"),
    ],
)
def test_batch_recipe_retains_files_and_failure(tmp_path, recipe, failed_phase):
    just = shutil.which("just")
    if just is None:
        pytest.skip("just is not installed")
    for filename in ("justfile", "project.justfile"):
        shutil.copyfile(ROOT / filename, tmp_path / filename)
    paths = (
        ["interpro/panther/PTHR10000/PTHR10000-review.yaml",
         "interpro/panther/with spaces/PTHR10001-review.yaml"]
        if recipe == "validate-families"
        else ["modules/first.yaml", "modules/with spaces/second.yml"]
    )
    for name in paths:
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("{}\n")

    # Exercise the actual recipe, replacing only its external validators. Later
    # successful phases must never erase an earlier phase's failure.
    stub = f"""#!{sys.executable}
import json, os, sys
args = sys.argv[1:]
with open(os.environ['BATCH_CALLS'], 'a') as out:
    out.write(json.dumps(args) + '\\n')
phase = os.environ['FAILED_PHASE']
sys.exit(1 if phase and phase in args else 0)
"""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    uv = bin_dir / "uv"
    uv.write_text(stub)
    uv.chmod(0o755)
    wrapper = tmp_path / "scripts/run_reference_validator.sh"
    wrapper.parent.mkdir()
    wrapper.write_text('#!/usr/bin/env bash\nexec uv references "$@"\n')
    wrapper.chmod(0o755)
    log = tmp_path / "calls.jsonl"
    result = subprocess.run(
        [just, recipe], cwd=tmp_path, capture_output=True, text=True,
        env={**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
             "BATCH_CALLS": str(log), "FAILED_PHASE": failed_phase},
        timeout=30,
    )
    assert (result.returncode != 0) == bool(failed_phase), result.stderr
    calls = [json.loads(line) for line in log.read_text().splitlines()]
    phases = ["linkml-validate"]
    if recipe == "validate-families":
        phases += ["linkml-term-validator", "references"]
        assert any("ai_gene_review.validation.gene_residue_claims" in c for c in calls)
    else:
        phases += ["ai_gene_review.validation.module_validator"]
    for phase in phases:
        batch = [c for c in calls if phase in c]
        assert len(batch) == 1, calls
        for path in paths:
            assert path in batch[0], batch


@pytest.mark.parametrize("phase", ["schema", "terms"])
def test_real_validators_reject_invalid_later_file(tmp_path, phase):
    """The upstream batch CLI must inspect inputs after a valid first file."""
    data = {
        "family_id": "PANTHER:PTHR10000",
        "family_name": "Test family",
        "functional_coherence": "MOSTLY_COHERENT",
        "review_status": "COMPLETE",
        "term_assessments": [{
            "assessed_term": {"id": "GO:0003674", "label": "molecular_function"},
            "scope": "FAMILY_WIDE", "scope_reason": "Test fixture",
        }],
    }
    good = tmp_path / "good.yaml"
    bad = tmp_path / "bad.yaml"
    good.write_text(yaml.safe_dump(data))
    schema = ROOT / "src/ai_gene_review/schema/family_review.yaml"
    if phase == "schema":
        data["unexpected_field"] = "must be rejected by closed schema"
        command = [str(Path(sys.executable).with_name("linkml-validate")),
                   "--schema", str(schema), "--target-class", "FamilyReview"]
    else:
        data["term_assessments"][0]["assessed_term"]["label"] = "wrong label"
        # A tiny local ontology keeps this regression deterministic and offline.
        obo = tmp_path / "go.obo"
        obo.write_text("format-version: 1.2\nontology: go\n\n[Term]\n"
                       "id: GO:0003674\nname: molecular_function\n")
        config = tmp_path / "oak.yaml"
        config.write_text(yaml.safe_dump({"ontology_adapters": {"GO": f"simpleobo:{obo}"}}))
        command = [str(Path(sys.executable).with_name("linkml-term-validator")),
                   "validate-data", "-s", str(schema), "-t", "FamilyReview",
                   "--labels", "--no-cache", "-c", str(config)]
    bad.write_text(yaml.safe_dump(data))
    good_result = subprocess.run(command + [str(good)], cwd=tmp_path,
                                 capture_output=True, text=True, timeout=60)
    assert good_result.returncode == 0, good_result.stdout + good_result.stderr
    batch_result = subprocess.run(command + [str(good), str(bad)], cwd=tmp_path,
                                  capture_output=True, text=True, timeout=60)
    assert batch_result.returncode != 0, batch_result.stdout + batch_result.stderr
    expected = "unexpected_field" if phase == "schema" else "wrong label"
    assert expected in batch_result.stdout + batch_result.stderr
