#!/usr/bin/env python3
"""Enforce the batch records' invariants against the live gene reviews.

Three checks, all of which the 2026-09-24 audit got wrong at least once before
they were written down (see this folder's README):

1. Each recorded ``action`` matches the live review file's action for that row.
   When an entry declares ``merged_into`` (its folder was merged away by the
   audit), the action is checked against that target and the substitution is
   reported; a missing file without ``merged_into`` is a violation rather than
   a silent skip.
2. Annotation-level ``outcome`` is ``retained`` iff ``previous_action == action``.
3. Gene-level ``outcome`` is ``changed`` iff **any** of that gene's annotations
   changed action, else ``confirmed``. This is adjudication, not file edits: a
   gene whose rationale was rewritten but whose actions all stand is
   ``confirmed``.

Also flags a non-``MODIFY`` row still carrying ``proposed_replacement_terms``.

Exits non-zero on any violation, so it can gate a future refresh.

Run:
  uv run --with pyyaml projects/TREEGRAFTER/rereview-2026-09-24/check_outcomes.py
"""
from __future__ import annotations

import glob
import os
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TREEGRAFTER_REF = "GO_REF:0000118"


def main() -> int:
    problems: list[str] = []
    preexisting: list[str] = []
    merged: list[str] = []
    genes = rows = 0
    for path in sorted(glob.glob(os.path.join(HERE, "batch-*.yaml"))):
        batch = os.path.basename(path)
        with open(path) as fh:
            doc = yaml.safe_load(fh) or {}
        for gene in doc.get("genes") or []:
            genes += 1
            name = gene.get("gene", "?")
            anns = gene.get("annotations") or []
            # A recorded gene_file that no longer exists used to fall through
            # silently (live = None -> continue), so the row's action was
            # checked against nothing while the script still printed it among
            # the rows checked and reported 0 violations. Exactly one entry is
            # in that state -- PSEPK/aroQ, whose folder this audit merged away
            # -- and that is now declared on the entry as `merged_into`, so the
            # invariant is checked against the surviving twin instead of being
            # skipped. A missing file with no `merged_into` is a violation: a
            # mistyped path must not pass the gate green.
            recorded = gene.get("gene_file", "")
            merged_into = gene.get("merged_into", "")
            check_path = merged_into or recorded
            live_path = os.path.join(ROOT, check_path)
            live = None
            if os.path.exists(live_path):
                with open(live_path) as fh:
                    live = yaml.safe_load(fh)
                if merged_into:
                    merged.append(
                        f"{batch} {name}: {recorded} was merged away; action "
                        f"checked against {merged_into}"
                    )
            else:
                problems.append(
                    f"{batch} {name}: {check_path} does not exist, so this "
                    f"entry's recorded action is verified against nothing"
                    + (" (merged_into target is missing)" if merged_into else "")
                )

            for ann in anns:
                rows += 1
                prev, act = ann.get("previous_action"), ann.get("action")
                want = "retained" if prev == act else "changed"
                if ann.get("outcome") != want:
                    problems.append(
                        f"{batch} {name} {ann.get('term_id')}: annotation outcome "
                        f"{ann.get('outcome')!r}, expected {want!r}"
                    )
                if live is None:
                    continue
                match = [
                    a for a in live.get("existing_annotations") or []
                    if (a.get("term") or {}).get("id") == ann.get("term_id")
                    and a.get("original_reference_id") == TREEGRAFTER_REF
                ]
                if not match:
                    problems.append(
                        f"{batch} {name} {ann.get('term_id')}: no live row "
                        f"(path may have been merged away)"
                    )
                    continue
                review = match[0].get("review") or {}
                if review.get("action") != act:
                    problems.append(
                        f"{batch} {name} {ann.get('term_id')}: live action "
                        f"{review.get('action')!r} != recorded {act!r}"
                    )
                if review.get("action") != "MODIFY" and review.get(
                    "proposed_replacement_terms"
                ):
                    # Only a row this audit moved is the audit's responsibility. A
                    # pre-existing REMOVE that names a better term is advisory and
                    # was left as found; report it without failing the gate.
                    note = (
                        f"{batch} {name} {ann.get('term_id')}: "
                        f"{review.get('action')} carries proposed_replacement_terms"
                    )
                    (problems if prev != act else preexisting).append(note)

            want_gene = (
                "changed"
                if any(a.get("previous_action") != a.get("action") for a in anns)
                else "confirmed"
            )
            if gene.get("outcome") != want_gene:
                problems.append(
                    f"{batch} {name}: gene outcome {gene.get('outcome')!r}, "
                    f"expected {want_gene!r}"
                )

    print(f"checked {genes} gene entries / {rows} annotation rows")
    for m in merged:
        print(f"  merged entry: {m}")
    for p in preexisting:
        print(f"  pre-existing (not this audit's): {p}")
    for p in problems:
        print(f"  VIOLATION: {p}")
    print(f"{len(problems)} violation(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
