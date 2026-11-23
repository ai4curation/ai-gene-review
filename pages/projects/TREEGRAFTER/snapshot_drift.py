#!/usr/bin/env python3
"""Diff the current TreeGrafter review sidecar against an earlier committed one.

Reads ``treegrafter_review.tsv`` as committed at ``--base`` (via ``git show``)
and as currently on disk (or ``--current PATH``), joins on ``(file, term_id)``
and reports what drifted: annotations added / dropped, actions that changed,
and rows that crossed into or out of the down-graded population
(REMOVE / MODIFY / MARK_AS_OVER_ANNOTATED) the failure-mode analysis is built on.

Writes ``treegrafter_snapshot_drift.tsv`` (one row per added, dropped or
changed annotation) next to this script, or into ``--out-dir``.

The default ``--base`` is ``e3350f43d``, the commit on ``main`` that carries
the frozen 2026-09-06 snapshot of the sidecars.

Run:
  python3 projects/TREEGRAFTER/snapshot_drift.py [--base REV] [--out-dir DIR]
"""
from __future__ import annotations

import argparse
import csv
import io
import os
import subprocess
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
REL = "projects/TREEGRAFTER/treegrafter_review.tsv"
DOWNGRADE = {"REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY"}


def _index(text: str) -> dict:
    return {(r["file"], r["term_id"]): r
            for r in csv.DictReader(io.StringIO(text), delimiter="\t")}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--base", default="e3350f43d", help="git revision of the old sidecar")
    ap.add_argument("--current", default=os.path.join(ROOT, REL),
                    help="current treegrafter_review.tsv (default: working tree)")
    ap.add_argument("--out-dir", default=HERE)
    args = ap.parse_args()

    old = _index(subprocess.run(["git", "-C", ROOT, "show", f"{args.base}:{REL}"],
                                check=True, capture_output=True, text=True).stdout)
    with open(args.current) as fh:
        new = _index(fh.read())

    rows = []
    for key in sorted(set(old) | set(new)):
        o, n = old.get(key), new.get(key)
        a_old = o["action"] if o else ""
        a_new = n["action"] if n else ""
        if a_old == a_new:
            continue
        kind = "added" if not o else "dropped" if not n else "changed"
        r = n or o
        rows.append({
            "kind": kind, "file": key[0], "gene": r["gene"], "term_id": key[1],
            "term_label": r["term_label"], "aspect": r.get("aspect", ""),
            "old_action": a_old, "new_action": a_new,
            "downgrade_transition": (
                "leaves" if a_old in DOWNGRADE and a_new not in DOWNGRADE else
                "enters" if a_new in DOWNGRADE and a_old not in DOWNGRADE else ""),
        })

    os.makedirs(args.out_dir, exist_ok=True)
    out = os.path.join(args.out_dir, "treegrafter_snapshot_drift.tsv")
    fields = ["kind", "file", "gene", "term_id", "term_label", "aspect",
              "old_action", "new_action", "downgrade_transition"]
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    od = {k for k, r in old.items() if r["action"] in DOWNGRADE}
    nd = {k for k, r in new.items() if r["action"] in DOWNGRADE}
    kinds = Counter(r["kind"] for r in rows)
    print(f"base {args.base}: {len(old)} annotations / {len({k[0] for k in old})} files; "
          f"current: {len(new)} / {len({k[0] for k in new})}")
    print(f"added {kinds['added']}, dropped {kinds['dropped']}, action changed {kinds['changed']}")
    print(f"down-graded: {len(od)} -> {len(nd)}; left the down-graded set: {len(od - nd)}; "
          f"entered: {len(nd - od)} ({len(nd - set(old))} of them newly added rows)")
    print("changed actions (old -> new):")
    for (a, b), c in Counter((r["old_action"], r["new_action"]) for r in rows
                             if r["kind"] == "changed").most_common():
        print(f"  {a:24s} -> {b:24s} {c}")
    print(f"Wrote {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main()
