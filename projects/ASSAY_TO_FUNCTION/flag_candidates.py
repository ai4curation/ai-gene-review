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

import yaml

# A gene whose core molecular function is a secreted signaling ligand affects
# downstream cellular processes (proliferation, apoptosis, ...) only via
# receptor signaling -- so a hub-aligned process annotation is almost always a
# downstream consequence, not a core function. This is the strongest computable
# "indirect" discriminator (calibration from the VIABILITY Tier-2 re-review:
# IL21/PDGFB/VEGFA vs the cell-cycle machinery).
SIGNALING_LIGAND_MF = re.compile(
    r"cytokine activity|growth factor activity|hormone activity"
    r"|chemokine activity|chemoattractant activity",
    re.IGNORECASE,
)

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


def gene_has_ligand_mf(genes_dir: Path, organism: str, gene: str,
                       _cache: dict[tuple[str, str], bool] = {}) -> bool:
    """True if the gene has an ACCEPTed signaling-ligand MF annotation."""
    key = (organism, gene)
    if key in _cache:
        return _cache[key]
    hits = list(genes_dir.glob(f"{organism}/{gene}/{gene}-ai-review.yaml"))
    found = False
    if hits:
        try:
            doc = yaml.safe_load(hits[0].read_text())
            for a in (doc.get("existing_annotations") or []):
                lab = (a.get("term") or {}).get("label", "")
                if SIGNALING_LIGAND_MF.search(lab):
                    found = True
                    break
        except (yaml.YAMLError, OSError):
            pass
    _cache[key] = found
    return found


def load_class_downgrade_rate(path: Path) -> dict[str, int]:
    """Per-class empirical any-downgrade rate (%) from the aligned crosstab, used
    to prioritize the Tier-2 queue: ACCEPT calls in classes the curators demote
    most often are the most suspect."""
    rate: dict[str, int] = {}
    if not path.exists():
        return rate
    with path.open(newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            pct = (r.get("pct_any_downgrade") or "").rstrip("%")
            if pct.isdigit():
                rate[r["readout_class"]] = int(pct)
    return rate


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--matches", type=Path,
        default=Path("projects/ASSAY_TO_FUNCTION/reports/paper_readout_matches.tsv"))
    ap.add_argument(
        "--aligned-crosstab", type=Path,
        default=Path("projects/ASSAY_TO_FUNCTION/reports/paper_action_crosstab_aligned.tsv"))
    ap.add_argument(
        "--target", choices=["accepted", "unreviewed", "all"], default="accepted",
        help="which standing annotations to flag (accepted = re-review queue; "
             "unreviewed = not yet adjudicated)")
    ap.add_argument("--genes-dir", type=Path, default=Path("genes"))
    ap.add_argument(
        "--out", type=Path,
        default=Path("projects/ASSAY_TO_FUNCTION/reports/flagged_candidates.tsv"))
    args = ap.parse_args()

    if not args.matches.exists():
        raise SystemExit(f"missing {args.matches}; run mine_papers.py first")

    accepted_set = {"ACCEPT"}
    unreviewed_set = {"UNREVIEWED", "UNDECIDED", "PENDING", ""}
    target = {"accepted": accepted_set, "unreviewed": unreviewed_set,
              "all": STANDING}[args.target]
    dgr = load_class_downgrade_rate(args.aligned_crosstab)

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
            if action not in target:
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
            if tier is None and aspect in ("BP", "CC"):
                tier, reason = 2, (
                    f"{action or 'standing'} {aspect} call aligned to {readout}; "
                    "rubric default is non-core unless gene is in the machinery")
            if tier is None:
                continue

            # Dedupe per annotation (organism+gene+term); the same annotation
            # may be supported by several papers / matched by several readouts.
            key = (r["organism"], r["gene"], r["go_id"])
            ligand = (tier == 2 and gene_has_ligand_mf(
                args.genes_dir, r["organism"], r["gene"]))
            row = {
                "tier": str(tier), "priority": str(dgr.get(readout, 0)),
                "discriminator": "indirect_ligand" if ligand else "",
                "reason": reason,
                "organism": r["organism"], "gene": r["gene"], "pmid": r["pmid"],
                "go_id": r["go_id"], "go_label": label, "aspect": aspect,
                "action": action or "UNREVIEWED", "readout_class": readout,
            }
            prev = best.get(key)
            if prev is None or int(row["tier"]) < int(prev["tier"]):
                best[key] = row

    # Sort: Tier 1 first; then indirect-ligand cases (strongest non-core signal);
    # then by the readout class's empirical any-downgrade rate; then gene.
    rows = sorted(best.values(),
                  key=lambda x: (int(x["tier"]), x["discriminator"] != "indirect_ligand",
                                 -int(x["priority"]), x["readout_class"], x["gene"]))

    fields = ["tier", "priority", "discriminator", "reason", "organism", "gene",
              "pmid", "go_id", "go_label", "aspect", "action", "readout_class"]
    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
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

    print("\n## Tier 2 — hub-aligned BP/CC call (ranked by class downgrade rate)")
    by_class2 = Counter(r["readout_class"] for r in t2)
    for cls, n in sorted(by_class2.items(),
                         key=lambda kv: -int(dict((r['readout_class'],
                             r['priority']) for r in t2).get(kv[0], 0))):
        print(f"  {cls:<26} {n:>4}   (class any-downgrade {dgr.get(cls,0)}%)")
    print("\n  top of queue:")
    for r in t2[:12]:
        print(f"    [{r['priority']:>2}%] {r['gene']:<12} {r['go_label'][:40]:<40}"
              f" [{r['readout_class']}]")

    ligand_rows = [r for r in t2 if r["discriminator"] == "indirect_ligand"]
    print(f"\n## Indirect-ligand subset (signaling-ligand MF -> process is "
          f"downstream): {len(ligand_rows)} strongest non-core candidates")
    for r in ligand_rows[:20]:
        print(f"    {r['gene']:<10} {r['go_label'][:44]:<44} [{r['readout_class']}]")

    print(f"\nWrote {args.out} (target={args.target})")


if __name__ == "__main__":
    main()
