#!/usr/bin/env python3
"""
Automated review of SFT predictions against AIGR curated reviews + GOA.

For each unreviewed SFT prediction, assigns:
  CNN — term is in GOA for this gene
  COR_CANDIDATE — term not in GOA but present in AIGR core_functions or accepted annotations
  LSP — term is an ancestor of a more specific GOA term (heuristic: in GOA but AIGR review says MODIFY)
  NPI_CANDIDATE — term conflicts with AIGR (AIGR review action is REMOVE or MARK_AS_OVER_ANNOTATED)
  UNC — cannot determine from GOA + AIGR alone

COR_CANDIDATE and NPI_CANDIDATE need manual verification.
Already-reviewed predictions (without "Requires manual assessment") are preserved.
"""
import re
import sys
import yaml
import glob
from pathlib import Path
from collections import Counter


def load_goa_terms(goa_file: Path) -> set[str]:
    terms = set()
    if not goa_file.exists():
        return terms
    with open(goa_file) as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) > 4:
                m = re.match(r"GO:\d{7}", parts[4])
                if m:
                    terms.add(m.group())
    return terms


def load_aigr_term_actions(review_file: Path) -> dict[str, str]:
    """Return {GO_ID: action} from existing_annotations in AIGR review."""
    actions = {}
    if not review_file.exists():
        return actions
    with open(review_file) as f:
        doc = yaml.safe_load(f)
    for ann in doc.get("existing_annotations", []):
        go_id = ann.get("term", {}).get("id", "")
        action = ann.get("review", {}).get("action", "")
        if go_id.startswith("GO:") and action:
            # If multiple annotations for same term, prefer the strongest action
            if go_id not in actions or action in ("REMOVE", "MARK_AS_OVER_ANNOTATED"):
                actions[go_id] = action
    return actions


def load_aigr_core_terms(review_file: Path) -> set[str]:
    """Return GO IDs mentioned in core_functions."""
    terms = set()
    if not review_file.exists():
        return terms
    with open(review_file) as f:
        doc = yaml.safe_load(f)
    for cf in doc.get("core_functions", []):
        mf = cf.get("molecular_function", {})
        if mf and mf.get("id", "").startswith("GO:"):
            terms.add(mf["id"])
        for bp in cf.get("directly_involved_in", []):
            if bp.get("id", "").startswith("GO:"):
                terms.add(bp["id"])
        for cc in cf.get("occurs_in", []) + cf.get("locations", []):
            if cc.get("id", "").startswith("GO:"):
                terms.add(cc["id"])
    return terms


def auto_assess(
    go_id: str,
    goa_terms: set[str],
    aigr_actions: dict[str, str],
    aigr_core: set[str],
) -> tuple[str, int, str]:
    """Return (assessment, confidence_score, summary)."""
    in_goa = go_id in goa_terms
    aigr_action = aigr_actions.get(go_id, "")

    # Term is in GOA
    if in_goa:
        if aigr_action in ("REMOVE", "MARK_AS_OVER_ANNOTATED"):
            return (
                "CNN",
                2,
                f"In GOA but curated review recommends {aigr_action}. "
                "Prediction reproduces a known over-annotation.",
            )
        if aigr_action == "MODIFY":
            return (
                "LSP",
                2,
                "In GOA but curated review recommends MODIFY to a more appropriate term.",
            )
        return ("CNN", 2, "In GOA. Correct but not novel.")

    # Not in GOA — check AIGR
    if go_id in aigr_core:
        return (
            "COR_CANDIDATE",
            1,
            "Not in GOA but present in AIGR core functions. Candidate for COR — needs manual verification.",
        )

    if aigr_action in ("ACCEPT", "KEEP_AS_NON_CORE"):
        # Term is in AIGR existing_annotations with a positive action but not in GOA
        # This can happen if the annotation was added by the curator
        return (
            "COR_CANDIDATE",
            1,
            f"Not in GOA but AIGR review action is {aigr_action}. Candidate for COR — needs verification.",
        )

    if aigr_action in ("REMOVE", "MARK_AS_OVER_ANNOTATED"):
        return (
            "NPI_CANDIDATE",
            0,
            f"AIGR review action is {aigr_action}. Likely incorrect — needs verification.",
        )

    # No information from GOA or AIGR
    return ("UNC", 1, "Not in GOA and not addressed in AIGR review. Cannot determine.")


def main():
    stats = Counter()
    gene_count = 0
    modified_files = 0

    for f in sorted(glob.glob("genes/*/*/*-sft-predictions.yaml")):
        p = Path(f)
        org = p.parent.parent.name
        gene = p.parent.name

        with open(f) as fh:
            doc = yaml.safe_load(fh)

        goa_file = p.parent / f"{gene}-goa.tsv"
        review_file = p.parent / f"{gene}-ai-review.yaml"

        goa_terms = load_goa_terms(goa_file)
        aigr_actions = load_aigr_term_actions(review_file)
        aigr_core = load_aigr_core_terms(review_file)

        changed = False
        gene_count += 1

        for pred in doc.get("predictions", []):
            summary = pred.get("review", {}).get("summary", "")
            if "Requires manual assessment" not in summary:
                # Already reviewed — preserve
                stats[pred["review"]["assessment"]] += 1
                continue

            go_id = pred.get("predicted_term", {}).get("id", "")
            assessment, confidence, new_summary = auto_assess(
                go_id, goa_terms, aigr_actions, aigr_core
            )
            pred["review"]["assessment"] = assessment
            pred["review"]["confidence_score"] = confidence
            pred["review"]["summary"] = new_summary
            stats[assessment] += 1
            changed = True

        if changed:
            with open(f, "w") as fh:
                yaml.dump(doc, fh, default_flow_style=False, sort_keys=False, allow_unicode=True)
            modified_files += 1

    print(f"Genes processed: {gene_count}")
    print(f"Files modified: {modified_files}")
    print(f"\nAssessment distribution:")
    total = sum(stats.values())
    for k in ["CNN", "COR", "COR_CANDIDATE", "NPI", "NPI_CANDIDATE", "LSP", "UNC", "REP"]:
        if stats[k]:
            print(f"  {k}: {stats[k]} ({stats[k]/total*100:.1f}%)")
    print(f"  Total: {total}")


if __name__ == "__main__":
    main()
