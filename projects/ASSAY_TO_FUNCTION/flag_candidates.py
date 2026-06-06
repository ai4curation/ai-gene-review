#!/usr/bin/env python3
"""Flag re-review candidates by applying the ASSAY_TO_FUNCTION rubric to the
mined (annotation, source-paper-readout) matches.

Consumes ``reports/paper_readout_matches.tsv`` (produced by ``mine_papers.py``)
and emits a prioritized worklist. We only flag annotations that are still
*standing* (not already downgraded by a curator) and that are *thematically
aligned* to a phenotypic, high-convergence ("hub") readout, so precision stays
high.

Two rubric signatures:

  TIER 1  MF aspect from a hub readout. A state readout cannot license a
          molecular-function term. Exception: a transcriptional reporter
          supporting a bona fide DNA-binding-TF activity term (legitimate).

  TIER 2  A core call (action ACCEPT) on a hub-aligned BP/CC annotation. The
          rubric default for hub readouts is non-core; verify the gene is in
          the recognized machinery for the process, else demote.

These are *re-review candidates*, not asserted errors.

Usage:
    uv run python projects/ASSAY_TO_FUNCTION/flag_candidates.py
"""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

# Actions where the annotation still stands as written (curator has not already
# removed/demoted/refined it).
STANDING = {"ACCEPT", "UNREVIEWED", "UNDECIDED", "PENDING", ""}

# A transcriptional reporter legitimately supports these MF terms for genuine
# transcription factors -> do NOT flag those as Tier 1.
TF_LEGIT_MF = re.compile(
    r"DNA-binding transcription (factor|repressor|activator) activity"
    r"|cis-regulatory region (sequence-specific )?(DNA )?binding"
    r"|transcription factor binding"
    r"|sequence-specific DNA binding",
    re.IGNORECASE,
)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--matches", type=Path,
        default=Path("projects/ASSAY_TO_FUNCTION/reports/paper_readout_matches.tsv"))
    ap.add_argument(
        "--out", type=Path,
        default=Path("projects/ASSAY_TO_FUNCTION/reports/flagged_candidates.tsv"))
    args = ap.parse_args()

    if not args.matches.exists():
        raise SystemExit(f"missing {args.matches}; run mine_papers.py first")

    # One annotation can match several readout classes; keep the strongest
    # (lowest tier number) flag per unique annotation.
    best: dict[tuple[str, str, str, str], dict[str, str]] = {}

    with args.matches.open(newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["aligned"] != "True":
                continue
            if r["proximity"] != "phenotypic" or r["convergence"] != "high":
                continue
            action = (r["action"] or "").strip()
            if action not in STANDING:
                continue

            aspect = r["aspect"]
            readout = r["readout_class"]
            label = r["go_label"]

            tier = reason = None
            if aspect == "MF":
                if readout == "TRANSCRIPTIONAL_REPORTER" and TF_LEGIT_MF.search(label):
                    pass  # legitimate TF-activity MF from a reporter
                elif "binding" in label.lower():
                    # Ligand/ion/protein-binding MF is a direct molecular
                    # activity established by binding assays (IPI/IDA), not
                    # "licensed" by a state readout -- calibration finding from
                    # the Tier-1 re-review (Calm2, HRC were false positives).
                    pass
                else:
                    tier, reason = 1, (
                        f"regulatory MF term from {readout}; a reporter/state "
                        "readout alone does not establish molecular activity -- "
                        "verify direct (e.g. DNA-binding) evidence")
            if tier is None and action == "ACCEPT" and aspect in ("BP", "CC"):
                tier, reason = 2, (
                    f"core (ACCEPT) {aspect} call aligned to {readout}; rubric "
                    "default is non-core unless gene is in the machinery")
            if tier is None:
                continue

            # Dedupe per annotation (organism+gene+term); the same annotation
            # may be supported by several papers / matched by several readouts.
            key = (r["organism"], r["gene"], r["go_id"])
            row = {
                "tier": str(tier), "reason": reason,
                "organism": r["organism"], "gene": r["gene"], "pmid": r["pmid"],
                "go_id": r["go_id"], "go_label": label, "aspect": aspect,
                "action": action or "UNREVIEWED", "readout_class": readout,
            }
            prev = best.get(key)
            if prev is None or int(row["tier"]) < int(prev["tier"]):
                best[key] = row

    rows = sorted(best.values(),
                  key=lambda x: (x["tier"], x["readout_class"], x["gene"]))

    fields = ["tier", "reason", "organism", "gene", "pmid", "go_id",
              "go_label", "aspect", "action", "readout_class"]
    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    t1 = [r for r in rows if r["tier"] == "1"]
    t2 = [r for r in rows if r["tier"] == "2"]
    print(f"Flagged {len(rows)} re-review candidates "
          f"(Tier 1: {len(t1)}, Tier 2: {len(t2)}).")

    print("\n## Tier 1 — MF from a hub readout (highest priority)")
    by_class = Counter(r["readout_class"] for r in t1)
    for cls, n in by_class.most_common():
        print(f"  {cls:<26} {n}")
    for r in t1[:15]:
        print(f"    {r['gene']:<12} {r['go_id']:<12} {r['go_label'][:42]:<42}"
              f" [{r['readout_class']}] {r['action']}")

    print("\n## Tier 2 — core call on a hub-aligned BP/CC annotation")
    by_class2 = Counter(r["readout_class"] for r in t2)
    for cls, n in by_class2.most_common():
        print(f"  {cls:<26} {n}")

    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
