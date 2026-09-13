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
  * a curated override table, ``failure_mode_curated.tsv`` (file, gene,
    term_id, mode, note), which always wins (``mode_source = curated``). Rows
    the heuristic cannot place are written with mode 0 (UNCLASSIFIED) so they
    are visible rather than silently binned.

All joins are keyed on ``(file, term_id)``, never ``(gene, term_id)``: gene
symbols are not unique across the corpus (``mdh`` in METEA and PSEPK, ``ALB``
in CANLF and FELCA, the two PSEPK ``dapF`` paralogs Q88CF3/Q88GD4), so a
symbol-keyed join silently pulls ``aspect``/``reason`` from another organism's
gene and lets one curated override apply to several unrelated rows.

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
    r"mis-?(plac|annotat|assign|graft)|wrong[- ](enzyme|subfamily|paralog|"
    r"family member|substrate)|different enzyme|"
    r"is (actually |in fact )?an? [\w\-]+ (synthetase|reductase|dehydrogenase|"
    r"transferase|ligase|deaminase|oxidase|kinase|hydrolase|isomerase|lyase)|"
    r"paralog (transfer|swap|over-?annotation|mis-?assignment)|"
    r"crosses [\w\s.]*paralogs|substrate[- ]class error|"
    r"distinct (enzyme|activity|substrate|subfamil)|not (a |an )?[\w\-]+ (synthase|"
    r"dehydrogenase|reductase|ligase|transferase|lipase|deaminase)|"
    # "acts on X ... not Y" is a substrate contrast; a bare "acts on" is not
    # (e.g. "MutS acts on duplex DNA, but this generic binding term ...").
    r"(substrate|specificity) (differs|is different)|acts on [^.]{0,150}?\bnot\b|"
    r"instead of", re.I)
# Explicit statements that the term came down from the family/pathway level.
# This IS mode 1's operational definition, so it is tested before RE_MISPLACE:
# otherwise a reason such as "family-level pathway propagation rather than
# paralog-specific evidence" lands in mode 4 on the words "rather than".
RE_FAMILY_LEVEL = re.compile(
    r"(pathway[- ])?(super)?family[- ]level|at the (pathway[- ])?family level|"
    r"broad family [\w\s-]*label", re.I)
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
# Binding terms that carry no functional information whatever the reviewer's
# reason says. This is an explicit allowlist, NOT /binding$/: terms such as
# "ubiquinone binding", "double-stranded DNA binding" or "metal ion binding"
# name a real ligand, so being down-graded on them is a granularity or
# placement story and has to be decided from the reviewer's reason instead.
LOW_INFO_BINDING = {
    "binding",
    "protein binding",
    "identical protein binding",
    "small molecule binding",
}


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
    if label.strip().lower() in LOW_INFO_BINDING:
        return 3, "uninformative binding term"
    if RE_CONTEXT.search(text):
        return 3, "host lacks pathway/process"
    if RE_FAMILY_LEVEL.search(text):
        return 1, "family-level propagation stated"
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
                curated[(r["file"], r["term_id"])] = (int(r["mode"]), r.get("note", ""))
    reasons = load_reasons()
    aspect_for = {}
    with open(REVIEW_TSV) as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            aspect_for[(r["file"], r["term_id"])] = r.get("aspect", "")

    rows = []
    seen_curated = set()
    with open(PLACEMENT) as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            key = (r["file"], r["propagated_term_id"])
            aspect = aspect_for.get(key, "")
            reason, summary = reasons.get(key, ("", ""))
            text = f"{reason} {summary}"
            if key in curated:
                seen_curated.add(key)
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

    orphans = sorted(set(curated) - seen_curated)
    if orphans:
        print(f"WARNING: {len(orphans)} curated override(s) match no placement row "
              f"(stale after a re-run?):")
        for f, t in orphans:
            print(f"  {t}  {f}")

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
