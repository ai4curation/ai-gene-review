"""Run focused production checks and scaffold append-only history records."""

import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CACHE = ROOT / ".cache/module-audit-logs/methionine-cycle-20261107/family-consultation"
FAMILIES = [
    "PTHR11964",
    "PTHR23420",
    "PTHR46832",
    "PTHR35799",
    "PTHR45833",
    "PTHR30519",
]
FILES = [f"interpro/panther/{f}/{f}-review.yaml" for f in FAMILIES]


def run(name, args):
    p = subprocess.run(
        args, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    (CACHE / (name + ".log")).write_text(p.stdout)
    print(name, p.returncode, flush=True)
    return {
        "check": name,
        "command": args,
        "exit_code": p.returncode,
        "log": str((CACHE / (name + ".log")).relative_to(ROOT)),
    }


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    checks = [
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
        ("ruff", ["uv", "run", "ruff", "check", str(HERE.relative_to(ROOT))]),
    ]
    out = [run(n, c) for n, c in checks]
    (HERE / "checks.json").write_text(json.dumps(out, indent=2) + "\n")
    assert all(x["exit_code"] == 0 for x in out), "Inspect failed focused checks"


if __name__ == "__main__":
    main()
