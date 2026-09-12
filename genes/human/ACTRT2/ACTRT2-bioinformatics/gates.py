"""Run every ACTRT2 gate that lives in this folder, so none of them is merely available.

Two of the checks here existed but nothing invoked them, which is its own defect - a lint that is
not run is documentation. This is the single entry point:

    uv run python gates.py

It does NOT re-run analyze_actrt2.py (that makes ~200 live API calls); it checks the committed
outputs instead. The repository-level gates - `just validate human ACTRT2`, the quote checker and
the cache/go/terms.csv checks - are outside this folder and are listed at the end so the full
sequence is discoverable from one place.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

CHECKS = [
    (["python", "audit_claims.py", "--selftest"], "claim lint self-test (does the lint fire?)"),
    (["python", "audit_claims.py"], "claim lint (are corrected claims still corrected?)"),
    (["python", "source_entities.py", "verify"], "source_entities match the GOA WITH/FROM field"),
]

REPO_GATES = [
    "uv run python <scratchpad>/checkquotes.py genes/human/ACTRT2/ACTRT2-ai-review.yaml",
    "just validate human ACTRT2",
    'base=$(git merge-base origin/main HEAD); git diff $base HEAD -- cache/go/terms.csv | grep "^-GO:"   # must be empty',
    "cut -d, -f1 cache/go/terms.csv | sort | uniq -d   # only GO:0001675, GO:0009566",
]


def main() -> int:
    failed = []
    for cmd, label in CHECKS:
        print(f"\n=== {label} ===")
        r = subprocess.run(["uv", "run", *cmd], cwd=HERE)
        if r.returncode != 0:
            failed.append(label)
    print()
    if failed:
        print(f"FAILED ({len(failed)}): " + "; ".join(failed))
        return 1
    print(f"all {len(CHECKS)} in-folder gates pass")
    print("\nrepository-level gates, to be run from the repo root:")
    for g in REPO_GATES:
        print("  " + g)
    return 0


if __name__ == "__main__":
    sys.exit(main())
