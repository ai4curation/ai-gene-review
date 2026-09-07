#!/usr/bin/env python3
"""Assign every down-graded TreeGrafter annotation to one of the four failure
modes described on failure-modes.md.

  1  GRANULARITY      right family, but the propagated term is the broad
                      family-level (or a sibling) term; the subfamily is more
                      specific / divergent
  2  PSEUDOENZYME     right fold family, catalytic activity lost or co-opted
  3  GENERIC_CONTEXT  low-information CC term, uninformative binding term, or a
                      process/pathway term out of context for the host
  4  MISPLACEMENT     genuine within-superfamily mis-placement: a functionally
                      distinct enzyme / substrate class

Two layers:

  * a keyword heuristic over the GO aspect and the reviewer's ``review.reason``
    / ``review.summary`` text (``mode_source = heuristic``), and
  * a curated override table, ``failure_mode_curated.tsv`` (gene, term_id,
    mode, note), which always wins (``mode_source = curated``). Rows the
    heuristic cannot place are written with mode 0 (UNCLASSIFIED) so they are
    visible rather than silently binned.

Reads treegrafter_placement.tsv (from analyze_placement.py) and the gene
review YAMLs; writes treegrafter_failure_modes.tsv and prints mode x action
counts.

Run:
  uv run --with pyyaml projects/TREEGRAFTER/classify_failure_modes.py
"""
from __future__ import annotations

import csv
import os
import re
from collections import Counter, defaultdict

import yaml

LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PLACEMENT = os.path.join(HERE, "treegrafter_placement.tsv")
REVIEW_TSV = os.path.join(HERE, "treegrafter_review.tsv")
CURATED = os.path.join(HERE, "failure_mode_curated.tsv")
OUT = os.path.join(HERE, "treegrafter_failure_modes.tsv")

MODES = {0: "UNCLASSIFIED", 1: "GRANULARITY", 2: "PSEUDOENZYME",
         3: "GENERIC_CONTEXT", 4: "MISPLACEMENT"}

RE_PSEUDO = re.compile(
    r"pseudo-?enzyme|pseudoenzyme|(lost|loss of|lacks?|lacking|absent|missing|no)\s+"
    r"(the\s+)?(catalytic|active[- ]site|essential)\s+(residue|cys|his|asp|ser|lys|trp|"
    r"triad|motif)|catalytically (inactive|dead)|non-?catalytic|inactive (enzyme|"
    r"homolog|paralog)|structural (protein|role)|crystallin", re.I)
RE_MISPLACE = re.compile(
    r"mis-?plac|wrong (enzyme|subfamily|paralog|family member)|different enzyme|"
    r"is (actually |in fact )?an? [\w\-]+ (synthetase|reductase|dehydrogenase|"
    r"transferase|ligase|deaminase|oxidase|kinase|hydrolase|isomerase|lyase)|"
    r"paralog|distinct (enzyme|activity|substrate)|not (a|an) [\w\-]+ (synthase|"
    r"dehydrogenase|reductase|ligase|transferase|lipase|deaminase)|"
    r"(substrate|specificity) (differs|is different)|acts on|instead of|rather than", re.I)
RE_CONTEXT = re.compile(
    r"not (present|found|encoded|a (process|pathway)) in|absent (from|in) (this|the) "
    r"(organism|species|bacterium|genome)|(organism|bacterium|species|genome) (does not|"
    r"doesn't|lacks|has no)|no [\w\s-]*pathway in|plant[- ]type|plant-specific|"
    r"eukaryot\w+[- ]specific|mammal\w*[- ]specific|not (relevant|applicable) (to|in) "
    r"(bacteria|prokaryot|this)|does not (make|synthesi[sz]e|produce) ", re.I)
RE_GENERIC = re.compile(
    r"too (general|broad|generic|coarse|unspecific|non-?specific)|overly (general|broad)|"
    r"uninformative|low[- ]information|generic|non-?specific|parent term|"
    r"more specific (term|child)|(better|more precise|specific) term|granular|"
    r"family[- ]level|sibling", re.I)
RE_BINDING = re.compile(r"\b(identical protein binding|protein binding|binding)$", re.I)


def load_reasons() -> dict:
    """{(file, term_id): (reason, summary)} for every down-graded TG row."""
    wanted = defaultdict(set)
    with open(REVIEW_TSV) as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            wanted[r["file"]].add(r["term_id"])
    out = {}
    for rel, terms in wanted.items():
        try:
            with open(os.path.join(ROOT, rel)) as fh:
                doc = yaml.load(fh, Loader=LOADER)
        except Exception:  # noqa: BLE001
            continue
        for ann in (doc or {}).get("existing_annotations") or []:
            if not isinstance(ann, dict):
                continue
            tid = (ann.get("term") or {}).get("id", "")
            if tid in terms and ann.get("original_reference_id") == "GO_REF:0000118":
                rv = ann.get("review") or {}
                out[(rel, tid)] = ((rv.get("reason") or "").strip(),
                                   (rv.get("summary") or "").strip())
    return out


def heuristic(aspect: str, label: str, text: str):
    """Return (mode, matched_rule)."""
    if RE_PSEUDO.search(text):
        return 2, "pseudo-enzyme keywords"
    if aspect == "cellular_component":
        return 3, "CC term"
    if RE_BINDING.search(label):
        return 3, "uninformative binding term"
    if RE_CONTEXT.search(text):
        return 3, "host lacks pathway/process"
    if RE_MISPLACE.search(text):
        return 4, "mis-placement keywords"
    if RE_GENERIC.search(text):
        return 1, "granularity keywords"
    return 0, ""


def main() -> None:
    curated = {}
    if os.path.exists(CURATED):
        with open(CURATED) as fh:
            for r in csv.DictReader(fh, delimiter="\t"):
                curated[(r["gene"], r["term_id"])] = (int(r["mode"]), r.get("note", ""))
    reasons = load_reasons()
    file_for = {}
    with open(REVIEW_TSV) as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            file_for[(r["gene"], r["term_id"])] = (r["file"], r.get("aspect", ""))

    rows = []
    with open(PLACEMENT) as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            key = (r["gene"], r["propagated_term_id"])
            rel, aspect = file_for.get(key, ("", ""))
            reason, summary = reasons.get((rel, r["propagated_term_id"]), ("", ""))
            text = f"{reason} {summary}"
            if key in curated:
                mode, note = curated[key]
                source = "curated"
            else:
                mode, note = heuristic(aspect, r["propagated_term_label"], text)
                source = "heuristic" if mode else "none"
            rows.append({
                **r, "aspect": aspect, "mode": mode, "mode_label": MODES[mode],
                "mode_source": source, "mode_note": note,
                "reviewer_reason": (reason or summary)[:300].replace("\n", " "),
            })

    fields = list(rows[0].keys()) if rows else []
    with open(OUT, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    by_mode = Counter(r["mode_label"] for r in rows)
    print(f"Down-graded TreeGrafter annotations: {len(rows)}")
    for m, n in sorted(by_mode.items(), key=lambda kv: -kv[1]):
        print(f"  {m:16s} {n:4d}  ({100 * n / len(rows):4.1f}%)")
    print("\nmode x action:")
    for (m, a), n in sorted(Counter((r["mode_label"], r["action"]) for r in rows).items()):
        print(f"  {m:16s} {a:24s} {n}")
    print(f"\nby source: {dict(Counter(r['mode_source'] for r in rows))}")
    print(f"Wrote {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
