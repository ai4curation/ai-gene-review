"""Shared exact-evidence loading for BioReason prediction review tools."""

from collections import defaultdict
import re
from pathlib import Path

import yaml


POSITIVE_ACTIONS = {"ACCEPT", "KEEP_AS_NON_CORE"}
NEGATIVE_ACTIONS = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
NEGATED_ACTION_PREFIX = "NOT:"
PROVENANCE_LIMITED_NEGATIVE = "PROVENANCE_LIMITED_NEGATIVE"
INVALID_REFERENCE_CORRECTNESS = {"MISCITED", "WRONG_IDENTIFIER"}
GO_ID_RE = re.compile(r"GO:\d{7}")


def load_aigr_term_actions(
    review_file: Path, *, preserve_negated: bool = True
) -> dict[str, set[str]]:
    """Return exact AIGR action evidence grouped by GO ID.

    A negative action attached to an explicitly miscited or wrongly identified
    reference may reject that source rather than the biological term. Preserve
    that distinction with a sentinel instead of treating it as either a biological
    refutation or no evidence. The sentinel lets initial assessors return UNC while
    leaving manually adjudicated predictions intact.

    Negated annotations are preserved by default as ``NOT:<action>`` so a retained
    NOT assertion cannot be mistaken for positive support for the same GO term.

    Reference-level correctness is necessarily coarser than a finding review. It is
    used here only for negative actions whose annotation cites that exact reference.
    """
    actions: dict[str, set[str]] = defaultdict(set)
    if not review_file.exists():
        return actions

    with review_file.open() as handle:
        document = yaml.safe_load(handle) or {}

    invalid_source_references = {
        reference_id
        for reference in (document.get("references") or [])
        if isinstance(reference, dict)
        if (reference_id := reference.get("id"))
        and (reference.get("reference_review") or {}).get("correctness")
        in INVALID_REFERENCE_CORRECTNESS
    }
    for annotation in document.get("existing_annotations") or []:
        go_id = (annotation.get("term") or {}).get("id", "")
        action = (annotation.get("review") or {}).get("action", "")
        if not GO_ID_RE.fullmatch(go_id) or not action:
            continue
        if (
            action in NEGATIVE_ACTIONS
            and annotation.get("original_reference_id") in invalid_source_references
        ):
            actions[go_id].add(PROVENANCE_LIMITED_NEGATIVE)
            continue
        if preserve_negated and annotation.get("negated"):
            action = f"{NEGATED_ACTION_PREFIX}{action}"
        actions[go_id].add(action)
    return actions
