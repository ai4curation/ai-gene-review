"""Validate the exact post-freeze prose correction and generate helper histories."""

import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FAMILIES = ["PTHR43023", "PTHR30188", "PTHR33371"]
FILES = [f"interpro/panther/{f}/{f}-review.yaml" for f in FAMILIES]


def run(name, args):
    result = subprocess.run(
        args, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    (HERE / (name + ".log")).write_text(result.stdout)
    print(name, result.returncode, flush=True)
    assert result.returncode == 0, result.stdout[-2000:]
    return {"check": name, "command": args, "exit_code": 0}


def main():
    commands = [
        ("preservation", ["uv", "run", "python", str(HERE / "check.py")]),
        (
            "schema",
            [
                "uv",
                "run",
                "linkml-validate",
                "--schema",
                "src/ai_gene_review/schema/family_review.yaml",
                "--target-class",
                "FamilyReview",
                *FILES,
            ],
        ),
        (
            "terms",
            [
                "uv",
                "run",
                "linkml-term-validator",
                "validate-data",
                *FILES,
                "-s",
                "src/ai_gene_review/schema/family_review.yaml",
                "-t",
                "FamilyReview",
                "--labels",
                "-c",
                "conf/oak_config.yaml",
            ],
        ),
        (
            "references",
            [
                "scripts/run_reference_validator.sh",
                "validate",
                "data",
                *FILES,
                "--schema",
                "src/ai_gene_review/schema/family_review.yaml",
                "--target-class",
                "FamilyReview",
                "--config",
                "conf/reference_validator_config.yaml",
            ],
        ),
        (
            "grounding",
            [
                "uv",
                "run",
                "python",
                "-m",
                "ai_gene_review.validation.family_residue_validator",
                *FILES,
            ],
        ),
        (
            "crosscheck",
            [
                "uv",
                "run",
                "python",
                "-m",
                "ai_gene_review.validation.family_gene_crosscheck",
                *FILES,
            ],
        ),
        ("ruff", ["uv", "run", "ruff", "check", str(HERE)]),
    ]
    results = [run(n, c) for n, c in commands]
    (HERE / "checks.json").write_text(json.dumps(results, indent=2) + "\n")
    if (HERE / "histories.json").exists():
        return
    histories = []
    for family in FAMILIES:
        args = [
            "just",
            "new-history",
            "--kind",
            "other",
            "--slug",
            family + "-family-review",
            "--path",
            f"interpro/panther/{family}/{family}-review.yaml",
            "--event",
            "EDIT",
            "--outcome",
            "changed",
            "--actor-name",
            "codex",
            "--agent-tool",
            "codex",
            "--summary",
            "Align inherited Mla family prose with adjudicated activity scope",
            "--details",
            "Additive prose-only consistency correction after the initial family handoff. Narrow universal partner architecture and remove residual secondary-substrate exclusion/pruning claims. All PAINT objects, scope enums, terms, references, evidence and representative members are unchanged. Exact changed-field and old/new-hash receipt is in analysis/module_audits/bacterial_mla_intermembrane_phospholipid_transport/family-consultation/prose-followup; original handoff and proofs remain byte-identical. Focused schema, term, quote, grounding, family/gene, preservation and Ruff checks pass.",
            "--sections",
            "coherence_reason,subfamilies,term_assessments",
        ]
        result = subprocess.run(
            args, cwd=ROOT, text=True, capture_output=True, check=True
        )
        path = re.search(r"history/other/[^\s]+\.yaml", result.stdout)[0]
        check = run("history-" + family, ["just", "validate-history", path])
        histories.append({"path": path, "check": check})
    (HERE / "histories.json").write_text(json.dumps(histories, indent=2) + "\n")


if __name__ == "__main__":
    main()
