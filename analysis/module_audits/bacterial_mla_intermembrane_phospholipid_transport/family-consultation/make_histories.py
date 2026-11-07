"""Scaffold and validate append-only family histories with the repository helper."""

import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FAMILIES = [
    "PTHR30035",
    "PTHR36573",
    "PTHR43023",
    "PTHR30188",
    "PTHR33371",
    "PTHR35849",
]


def main():
    output = HERE / "histories.json"
    if output.exists():
        raise RuntimeError("Histories already scaffolded; do not generate duplicates")
    records = []
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
            "Reconcile Mla family scope with actual phylogeny, target roles and source limits",
            "--details",
            "Official reference trees/MSAs and current UniProt classifications distinguish positive Mla roles from broad ABC/MCE/STAS relatives. Preserve original PAINT payloads and unrelated judgments; withdraw unsupported substrate-loss exclusions, retain the genuine TGD1 plant localization loss with a current member ledger, and separate classification from activity licensing. Exact exceptions, source hashes, focused checks and preservation proof are in analysis/module_audits/bacterial_mla_intermembrane_phospholipid_transport/family-consultation. No raw/provider/publication sources changed.",
            "--sections",
            "summary,subfamilies,node_assessments,term_assessments,references,notes",
        ]
        result = subprocess.run(
            args, cwd=ROOT, text=True, capture_output=True, check=True
        )
        path = re.search(r"history/other/[^\s]+\.yaml", result.stdout)[0]
        validate = subprocess.run(
            ["just", "validate-history", path], cwd=ROOT, text=True, capture_output=True
        )
        records.append(
            {
                "family": family,
                "path": path,
                "validation_exit_code": validate.returncode,
                "validation_output": validate.stdout + validate.stderr,
            }
        )
        assert validate.returncode == 0, records[-1]
    output.write_text(json.dumps(records, indent=2) + "\n")
    print([r["path"] for r in records])


if __name__ == "__main__":
    main()
