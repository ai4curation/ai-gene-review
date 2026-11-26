"""Measure how well the wording of a removal reason predicted the re-review's verdict.

Reads each live row's review text as it stood before the re-review (``--baseline``, a
commit) and the verdict in results.tsv, and prints the table in README.md: for each
signal, the rows carrying it, the share whose action changed, and the share whose
review was edited at all. The phrase patterns are the ones reason_scan.py uses.

    uv run python projects/IBA_REVIEW/rereview-2026-11-21/reason_signal.py
"""

from __future__ import annotations

import argparse
import collections
import csv
import importlib.util
import re
import subprocess
from pathlib import Path

from ai_gene_review.yaml_utils import safe_load

HERE = Path(__file__).parent
SIGNALS = [
    ("Argues absence of evidence and cites no PAINT node", "absence_no_node"),
    ("Argues absence of evidence", "absence"),
    ("Short reason (under 45 words)", "short"),
    ("Cites no PAINT node", "no_node"),
    ("Cites a PAINT node", "node"),
    ("All rows", "all"),
]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--baseline", default="be90c8e9fc", help="commit holding the reviews before the re-review")
    args = ap.parse_args()
    spec = importlib.util.spec_from_file_location("reason_scan", HERE / "reason_scan.py")
    scan = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scan)
    absence = re.compile(scan.PHRASES["absence_of_evidence"])

    rows = [r for r in csv.DictReader(open(HERE / "results.tsv"), delimiter="\t") if r["status"] != "NOT_IN_SNAPSHOT"]
    docs: dict[str, dict] = {}
    total: collections.Counter = collections.Counter()
    changed: collections.Counter = collections.Counter()
    edited: collections.Counter = collections.Counter()
    unread = 0
    for r in rows:
        path = r["gene_file"]
        if path not in docs:
            blob = subprocess.run(["git", "show", f"{args.baseline}:{path}"], capture_output=True, text=True, check=False)
            docs[path] = safe_load(blob.stdout) if blob.returncode == 0 else {}
        review = next(
            (
                a.get("review") or {}
                for a in docs[path].get("existing_annotations") or []
                if a.get("evidence_type") == "IBA"
                and (a.get("term") or {}).get("id") == r["go_id"]
                and (a.get("review") or {}).get("action") == "REMOVE"
            ),
            None,
        )
        if review is None:
            unread += 1
            continue
        text = f"{review.get('summary', '')} {review.get('reason', '')}".lower()
        argues_absence, cites_node = bool(absence.search(text)), "ptn0" in text
        keys = ["all", "node" if cites_node else "no_node"]
        if argues_absence:
            keys.append("absence")
            if not cites_node:
                keys.append("absence_no_node")
        if len(text.split()) < 45:
            keys.append("short")
        for k in keys:
            total[k] += 1
            changed[k] += r["verdict"] == "ACTION_CHANGED"
            edited[k] += r["review_edited"] == "True"
    print("| Signal in the original reason | Rows | Changed | Edited |")
    print("|---|---:|---:|---:|")
    for label, k in SIGNALS:
        print(f"| {label} | {total[k]} | {100 * changed[k] / total[k]:.0f}% | {100 * edited[k] / total[k]:.0f}% |")
    if unread:
        print(f"\n{unread} rows had no REMOVE row at {args.baseline} and were not counted (a shallow clone does this).")


if __name__ == "__main__":
    main()
