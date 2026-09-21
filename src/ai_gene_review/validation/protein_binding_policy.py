"""Enforce the generic-protein-binding action policy for ``GO:0005515``.

``.claude/skills/annotation-reviewer/SKILL.md`` ("Quality Standards") states:

    **Generic protein binding is not over-annotation.** Do not use
    ``MARK_AS_OVER_ANNOTATED`` for ``GO:0005515``: its problem is lack of functional
    information, not a claim that exceeds the evidence. Use ``MODIFY`` when the cited
    paper supports a more informative molecular function... Otherwise, generally use
    ``REMOVE``, explaining that the generic annotation is uninformative; removal does not
    mean the reported interaction is false.

    Apply this policy to new reviews and to annotations touched during re-review. Older
    untouched reviews may retain legacy actions; migrate those when they are re-reviewed.

Nothing enforced it. Two reviews merged with deviations that four rounds of human-facing
review did not catch, and a grep for ``0005515`` in the compliance module returned nothing.

Severity is WARNING, deliberately. A repo-wide census found **11,967** non-compliant rows
across 1,595 files, which the policy's own carve-out sanctions as legacy. CI runs
``validate-all`` whenever validation infrastructure changes, so an error would fail every
such run before any of the backlog could be migrated. Scoped to files touched since the
policy landed the real, actionable count is 19 files / 124 rows -- and ``just validate``
already runs per gene, so an author sees only their own.
"""

from __future__ import annotations

from typing import Any, Dict, Iterator, Tuple

PROTEIN_BINDING = "GO:0005515"

#: Actions the policy permits on a bare ``GO:0005515`` row.
#:
#: ``NEW`` is deliberately absent. Every other flagged action mislabels an annotation GOA
#: already made; ``NEW`` *proposes a fresh* bare protein-binding annotation, which the root
#: ``CLAUDE.md`` rules out ("Avoid the term ``protein binding``... Instead find a more
#: informative MF term"). The legacy-backlog argument does not apply either: three rows
#: repo-wide do this.
COMPLIANT_ACTIONS = frozenset({"MODIFY", "REMOVE", "UNDECIDED", "PENDING"})

#: Why each non-compliant action is wrong, phrased so the message is actionable.
NON_COMPLIANT_REASONS = {
    "MARK_AS_OVER_ANNOTATED": (
        "the policy excludes this action for GO:0005515 by name -- the problem is lack of "
        "functional information, not a claim exceeding the evidence"
    ),
    "KEEP_AS_NON_CORE": (
        "keeping a bare protein-binding row preserves an annotation that carries no "
        "functional information"
    ),
    "ACCEPT": (
        "accepting a bare protein-binding row endorses an annotation that carries no "
        "functional information"
    ),
    "NEW": (
        "proposing a new bare protein-binding annotation adds one that carries no "
        "functional information; CLAUDE.md asks for a more informative MF term instead"
    ),
}


def iter_protein_binding_violations(
    data: Dict[str, Any],
) -> Iterator[Tuple[int, str, str]]:
    """Yield ``(index, action, explanation)`` for each non-compliant ``GO:0005515`` row.

    Compliant actions pass:

        >>> doc = {"existing_annotations": [
        ...     {"term": {"id": "GO:0005515"}, "review": {"action": "REMOVE"}}]}
        >>> list(iter_protein_binding_violations(doc))
        []

    The action the policy names explicitly is reported:

        >>> doc = {"existing_annotations": [
        ...     {"term": {"id": "GO:0005515"},
        ...      "review": {"action": "MARK_AS_OVER_ANNOTATED"}}]}
        >>> idx, action, _ = next(iter(iter_protein_binding_violations(doc)))
        >>> idx, action
        (0, 'MARK_AS_OVER_ANNOTATED')

    Other terms are untouched -- the policy is about generic protein binding only:

        >>> doc = {"existing_annotations": [
        ...     {"term": {"id": "GO:0005096"},
        ...      "review": {"action": "MARK_AS_OVER_ANNOTATED"}}]}
        >>> list(iter_protein_binding_violations(doc))
        []
    """
    annotations = data.get("existing_annotations")
    if not isinstance(annotations, list):
        return
    for index, annotation in enumerate(annotations):
        if not isinstance(annotation, dict):
            continue
        term = annotation.get("term")
        if not isinstance(term, dict) or term.get("id") != PROTEIN_BINDING:
            continue
        review = annotation.get("review")
        if not isinstance(review, dict):
            continue
        action = review.get("action")
        if not isinstance(action, str) or action in COMPLIANT_ACTIONS:
            continue
        explanation = NON_COMPLIANT_REASONS.get(
            action, "this action is not permitted for a bare protein-binding row"
        )
        yield index, action, explanation


def check_protein_binding_policy(data: Dict[str, Any], report) -> None:
    """Add a warning for each non-compliant ``GO:0005515`` action in *data*."""
    from ai_gene_review.validation.validation_report import ValidationSeverity

    for index, action, explanation in iter_protein_binding_violations(data):
        report.add_issue(
            ValidationSeverity.WARNING,
            f"GO:0005515 uses action {action}: {explanation}",
            path=f"existing_annotations[{index}].review.action",
            suggestion=(
                "Use MODIFY with an evidence-backed replacement term when the cited paper "
                "supports a more informative molecular function; otherwise REMOVE, noting "
                "that removal does not mean the interaction is false. Use UNDECIDED when "
                "the evidence cannot be adjudicated."
            ),
            validation_category="BestPractices",
            check_type="protein_binding_policy",
        )
