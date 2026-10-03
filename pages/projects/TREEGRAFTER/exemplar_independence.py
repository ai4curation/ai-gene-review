#!/usr/bin/env python3
"""Check whether the OpenScientist / Falcon exemplar verdicts are independent of
the reviewer judgement they are compared against.

For each exemplar in ``graft_check.EXEMPLARS`` this reads the gene's review
YAML and reports, for the propagated TreeGrafter (GO_REF:0000118) annotation:

  * the current reviewer ``action`` (the "held-out" judgement), and
  * whether that annotation's ``review.supported_by`` (or the review's
    top-level ``references``) cites the blinded ``*-hypotheses/`` OpenScientist
    or Falcon reports, or a Falcon deep-research file.

If the review cites the report, the reviewer action is not held out from the
report: agreement between them is partly by construction.

Writes ``exemplar_independence.tsv`` next to this script (or ``--out-dir``).

Run:
  uv run --with pyyaml projects/TREEGRAFTER/exemplar_independence.py
"""
from __future__ import annotations

import argparse
import csv
import glob
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from graft_check import EXEMPLARS  # noqa: E402

LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
AGENT_REF = re.compile(r"(openscientist|falcon)", re.I)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out-dir", default=HERE)
    out = os.path.join(os.path.abspath(ap.parse_args().out_dir), "exemplar_independence.tsv")

    rows = []
    for gene, org, acc, _term, term_id, _expected in EXEMPLARS:
        paths = (glob.glob(os.path.join(ROOT, "genes", org, gene, "*-ai-review.yaml"))
                 or glob.glob(os.path.join(ROOT, "genes", org, acc, "*-ai-review.yaml")))
        if not paths:
            rows.append({"gene": gene, "organism": org, "term_id": term_id,
                         "current_action": "REVIEW_NOT_FOUND"})
            continue
        with open(paths[0]) as fh:
            doc = yaml.load(fh, Loader=LOADER) or {}
        top_refs = [r.get("id", "") for r in doc.get("references") or []
                    if isinstance(r, dict) and AGENT_REF.search(r.get("id", ""))]
        action, cited = "ANNOTATION_NOT_FOUND", []
        for ann in doc.get("existing_annotations") or []:
            if ann.get("retired"):
                continue  # dropped from GOA at a later refresh; not a live annotation
            if ((ann.get("term") or {}).get("id") == term_id
                    and ann.get("original_reference_id") == "GO_REF:0000118"):
                rv = ann.get("review") or {}
                action = rv.get("action") or "UNREVIEWED"
                cited = sorted({s.get("reference_id", "") for s in rv.get("supported_by") or []
                                if isinstance(s, dict)
                                and AGENT_REF.search(s.get("reference_id", ""))})
        rows.append({
            "gene": gene, "organism": org, "term_id": term_id,
            "review_file": os.path.relpath(paths[0], ROOT),
            "current_action": action,
            "annotation_cites_agent_report": "yes" if cited else "no",
            "n_top_level_agent_refs": len(top_refs),
            "cited_reports": " | ".join(cited),
        })

    fields = ["gene", "organism", "term_id", "review_file", "current_action",
              "annotation_cites_agent_report", "n_top_level_agent_refs", "cited_reports"]
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", restval="")
        w.writeheader()
        w.writerows(rows)
    n_cite = sum(r.get("annotation_cites_agent_report") == "yes" for r in rows)
    for r in rows:
        print(f"  {r['gene']:28s} {r['term_id']}  {r['current_action']:24s} "
              f"cites_agent_report={r.get('annotation_cites_agent_report', '')}")
    print(f"{n_cite}/{len(rows)} exemplar annotations cite an OpenScientist/Falcon report "
          f"in their own supported_by")
    print(f"Wrote {os.path.relpath(out, ROOT)}")

    # Corpus-wide: how many reviewed TreeGrafter annotations cite an agent report?
    by_file: dict = {}
    with open(os.path.join(HERE, "treegrafter_review.tsv")) as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            by_file.setdefault(r["file"], set()).add(r["term_id"])
    n_all = n_cite_all = n_down = n_cite_down = 0
    down = {"REMOVE", "MODIFY", "MARK_AS_OVER_ANNOTATED"}
    for rel, terms in by_file.items():
        with open(os.path.join(ROOT, rel)) as fh:
            doc = yaml.load(fh, Loader=LOADER) or {}
        for ann in doc.get("existing_annotations") or []:
            if (ann.get("retired")
                    or ann.get("original_reference_id") != "GO_REF:0000118"
                    or (ann.get("term") or {}).get("id") not in terms):
                continue
            rv = ann.get("review") or {}
            cites = any(isinstance(s, dict) and AGENT_REF.search(s.get("reference_id", ""))
                        for s in rv.get("supported_by") or [])
            n_all += 1
            n_cite_all += cites
            if rv.get("action") in down:
                n_down += 1
                n_cite_down += cites
    print(f"corpus: {n_cite_all}/{n_all} reviewed TreeGrafter annotations cite an "
          f"OpenScientist/Falcon file in supported_by; {n_cite_down}/{n_down} of the down-graded ones")


if __name__ == "__main__":
    main()
