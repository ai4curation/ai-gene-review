#!/usr/bin/env python3
"""Mine behaviour annotations across the gene-review corpus.

The Gene Ontology ``behavior`` branch (GO:0007610) is a textbook over-annotation
trap: a gene knockout or genetic interaction perturbs an organismal behaviour
(locomotion, feeding, mating, circadian rhythm, ...) and the gene is then
annotated to that behaviour term even though its *molecular* function lives many
causal steps upstream. A tubulin, a lysosomal peptidase, or a ciliary scaffold
is not "for" locomotion in the way an MF term is "for" catalysis.

This script does two passes and is fully reproducible (nothing about the
results is hard-coded; if no behaviour annotations are found the report says so):

1. **Source pass** over ``genes/**/*-goa.tsv`` -- every GOA annotation whose GO
   aspect is biological_process and whose term name contains "behavio(u)r".
   This is the raw over-annotation surface, broken down by evidence code.

2. **Review pass** over ``genes/**/*-ai-review.yaml`` -- for each behaviour
   annotation that a reviewer has already adjudicated, record the ``action``
   they took (ACCEPT / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE / ...).
   This measures how the corpus actually treats behaviour terms.

Usage:
    uv run python projects/BEHAVIOR/mine_behavior.py \
        --genes-dir genes --out-dir projects/BEHAVIOR/reports
"""
from __future__ import annotations

import argparse
import csv
import glob
import os
import re
from collections import Counter, defaultdict
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    raise SystemExit("PyYAML required: `uv run python ...` or `pip install pyyaml`")

BEHAVIOR_RE = re.compile(r"behaviou?r", re.IGNORECASE)

# Reviewer actions, grouped by how strongly they signal over-annotation.
# A behaviour term kept as the *core* function of the gene would be the surprise;
# the expected, defensible outcomes are non-core retention or outright removal.
DOWNGRADE = {"KEEP_AS_NON_CORE", "MARK_AS_OVER_ANNOTATED", "REMOVE"}
KEPT_CORE = {"ACCEPT"}
NOT_REVIEWED = {"UNREVIEWED", "UNDECIDED", "PENDING", "NONE", ""}
# NEW proposes a brand-new annotation rather than adjudicating an existing one as
# core-vs-not, so it is excluded from the downgrade-rate denominator (it would
# otherwise dilute the rate without being a downgrade *or* a kept-core call).
NEW_PROPOSED = {"NEW"}


def source_pass(genes_dir: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in glob.glob(os.path.join(genes_dir, "**", "*-goa.tsv"), recursive=True):
        with open(path, newline="") as fh:
            reader = csv.DictReader(fh, delimiter="\t")
            for r in reader:
                aspect = (r.get("GO ASPECT") or "").strip()
                name = (r.get("GO NAME") or "").strip()
                if aspect != "biological_process" or not BEHAVIOR_RE.search(name):
                    continue
                parts = path.split(os.sep)
                rows.append(
                    {
                        "species": parts[1] if len(parts) > 1 else "?",
                        "gene": (r.get("SYMBOL") or "").strip(),
                        "term_id": (r.get("GO TERM") or "").strip(),
                        "term_label": name,
                        "evidence": (r.get("GO EVIDENCE CODE") or "").strip(),
                        "reference": (r.get("REFERENCE") or "").strip(),
                    }
                )
    return rows


def review_pass(genes_dir: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in glob.glob(os.path.join(genes_dir, "**", "*-ai-review.yaml"), recursive=True):
        try:
            with open(path) as fh:
                doc = yaml.safe_load(fh)
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        gene = doc.get("gene_symbol", "?")
        species = path.split(os.sep)[1] if len(path.split(os.sep)) > 1 else "?"
        for ann in doc.get("existing_annotations") or []:
            term = ann.get("term") or {}
            label = term.get("label") or ""
            if not BEHAVIOR_RE.search(label):
                continue
            review = ann.get("review") or {}
            rows.append(
                {
                    "species": species,
                    "gene": gene,
                    "term_id": term.get("id", ""),
                    "term_label": label,
                    "evidence": ann.get("evidence_type", ""),
                    "action": review.get("action", "") or "NONE",
                    "reason": (review.get("reason") or review.get("summary") or "").strip(),
                }
            )
    return rows


def write_csv(rows: list[dict[str, str]], path: str, fields: list[str]) -> None:
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--genes-dir", default="genes")
    ap.add_argument("--out-dir", default="projects/BEHAVIOR/reports")
    args = ap.parse_args()
    os.makedirs(args.out_dir, exist_ok=True)

    src = source_pass(args.genes_dir)
    rev = review_pass(args.genes_dir)

    write_csv(src, os.path.join(args.out_dir, "behavior_source_annotations.csv"),
              ["species", "gene", "term_id", "term_label", "evidence", "reference"])
    write_csv(rev, os.path.join(args.out_dir, "behavior_review_actions.csv"),
              ["species", "gene", "term_id", "term_label", "evidence", "action", "reason"])

    src_ev = Counter(r["evidence"] for r in src)
    rev_act = Counter(r["action"] for r in rev)
    n_down = sum(rev_act[a] for a in DOWNGRADE)
    n_core = sum(rev_act[a] for a in KEPT_CORE)
    n_new = sum(rev_act[a] for a in NEW_PROPOSED)
    # Denominator = existing annotations adjudicated as core-vs-not (excludes NEW
    # proposed terms and not-yet-reviewed annotations).
    adjudicated = n_down + n_core

    lines: list[str] = []
    lines.append("# Behaviour annotation mining report\n")
    lines.append("*Auto-generated by `projects/BEHAVIOR/mine_behavior.py`. Do not edit by hand.*\n")

    lines.append("\n## 1. Source annotations (from `*-goa.tsv`)\n")
    lines.append(f"- Behaviour annotations in corpus GOA files: **{len(src)}**")
    lines.append(f"- Distinct genes carrying a behaviour term: **{len({(r['species'], r['gene']) for r in src})}**")
    lines.append(f"- Distinct behaviour terms used: **{len({r['term_id'] for r in src})}**\n")
    lines.append("Evidence-code distribution:\n")
    lines.append("| Evidence | Count |")
    lines.append("|---|---|")
    for ev, c in src_ev.most_common():
        lines.append(f"| {ev or '(blank)'} | {c} |")

    lines.append("\nMost-used behaviour terms:\n")
    lines.append("| Term | ID | Count |")
    lines.append("|---|---|---|")
    term_ct = Counter((r["term_label"], r["term_id"]) for r in src)
    for (lbl, tid), c in term_ct.most_common(15):
        lines.append(f"| {lbl} | {tid} | {c} |")

    lines.append("\n## 2. Reviewer actions (from `*-ai-review.yaml`)\n")
    lines.append(f"- Behaviour annotations in reviews: **{len(rev)}**")
    if adjudicated:
        pct = 100.0 * n_down / adjudicated
        lines.append(
            f"- Of behaviour annotations adjudicated as core-vs-not (**{adjudicated}** "
            f"= {n_down} downgraded + {n_core} kept core; excludes {n_new} NEW proposed "
            f"terms and any not-yet-reviewed), **{n_down}/{adjudicated} ({pct:.0f}%)** "
            f"were downgraded (non-core / over-annotated / removed); only **{n_core}** "
            f"were ACCEPTed as a core function.\n"
        )
    lines.append("Action distribution:\n")
    lines.append("| Action | Count |")
    lines.append("|---|---|")
    for act, c in rev_act.most_common():
        lines.append(f"| {act} | {c} |")

    report = "\n".join(lines) + "\n"
    with open(os.path.join(args.out_dir, "REPORT.md"), "w") as fh:
        fh.write(report)
    print(report)


if __name__ == "__main__":
    main()
