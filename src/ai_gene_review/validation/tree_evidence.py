"""Ask for the tree behind a verdict that overrules an IBA.

An IBA is a PAINT curator's placement of a function on a node of a PANTHER family tree,
made with the whole tree and the family alignment in view. ``REMOVE`` and
``MARK_AS_OVER_ANNOTATED`` argue with that placement, so the argument should rest on
where the node sits, where its seeds sit and where the gene sits -- not on the node id
and seed list alone, which is all a GOA row carries. A census of this repository found
that about 95% of overruled IBA rows had no tree or alignment artifact behind them.

``just phylo <org> <GENE>`` writes ``GENE-phylo.yaml`` with those facts for every IBA row
(see :mod:`ai_gene_review.etl.gene_phylo`). The checks here ask a review to use it:

``missing_tree_evidence``
    An IBA row with action ``REMOVE`` or ``MARK_AS_OVER_ANNOTATED`` has no ``supported_by``
    entry that quotes the gene's own ``GENE-phylo.yaml``.
``tree_evidence_other_row``
    It quotes the extract, but no quote names this row's term, so it describes another row.
``missing_residue_evidence``
    A propagated row is overruled with failure mode ``PSEUDO_OR_SUBACTIVITY_LOSS`` and
    carries neither ``residue_claims`` nor ``residue_claims_not_applicable``. "Lacks the
    catalytic residues" was wrong about the mechanism in 4 of the 17 cases checked by
    alignment; the extract's ``residue_sites`` reads curated sites off PANTHER's alignment.

Whether a quote is really in the extract is checked separately, like every other
``file:`` quote (:mod:`ai_gene_review.validation.local_source_text`).

Severity is WARNING, as for the other action policies: the checks guide re-review and do
not block legacy files. Rows that keep the claim (``ACCEPT``, ``KEEP_AS_NON_CORE``,
``MODIFY``, ``TOO_GENERAL``) and ``UNDECIDED`` rows are not asked for the tree.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterator, Optional

#: Actions that say PAINT's placement does not hold for this gene.
OVERRULING_ACTIONS = frozenset({"REMOVE", "MARK_AS_OVER_ANNOTATED"})
PHYLO_SUFFIX = "-phylo.yaml"
RESIDUE_FAILURE_MODE = "PSEUDO_OR_SUBACTIVITY_LOSS"


def phylo_reference_ids(yaml_file: Optional[Path]) -> set[str]:
    """Reference ids that name the extract of the gene a review file belongs to.

    Empty when the review is not in a ``genes/<org>/<GENE>/`` folder.

    >>> sorted(phylo_reference_ids(Path("genes/human/CIRBP/CIRBP-ai-review.yaml")))
    ['file:genes/human/CIRBP/CIRBP-phylo.yaml', 'file:human/CIRBP/CIRBP-phylo.yaml']
    """
    if yaml_file is None:
        return set()
    folder = Path(yaml_file).parent
    if folder.parent.parent.name != "genes":
        return set()
    relative = f"{folder.parent.name}/{folder.name}/{folder.name}{PHYLO_SUFFIX}"
    return {f"file:{relative}", f"file:genes/{relative}"}


def _quotes(item: dict[str, Any]) -> list[str]:
    """The quoted text of one ``supported_by`` entry (a string or a list of strings)."""
    text = item.get("supporting_text")
    if isinstance(text, str):
        return [text]
    if isinstance(text, list):
        return [str(t.get("text", "")) if isinstance(t, dict) else str(t) for t in text]
    return []


def iter_tree_evidence_violations(
    data: dict[str, Any], yaml_file: Optional[Path] = None
) -> Iterator[tuple[int, str, str, str]]:
    """Yield ``(row index, check type, message, suggestion)`` for each policy violation."""
    own = phylo_reference_ids(yaml_file)
    gene = Path(yaml_file).parent.name if own and yaml_file is not None else "GENE"
    organism = Path(yaml_file).parent.parent.name if own and yaml_file is not None else "<org>"
    for index, annotation in enumerate(data.get("existing_annotations") or []):
        if not isinstance(annotation, dict):
            continue
        review = annotation.get("review")
        if not isinstance(review, dict) or review.get("action") not in OVERRULING_ACTIONS:
            continue
        action = review["action"]
        term = annotation.get("term")
        term_id = term.get("id", "") if isinstance(term, dict) else ""
        evidence = annotation.get("evidence_type")
        propagation = review.get("propagation_review")
        propagation = propagation if isinstance(propagation, dict) else {}

        if evidence == "IBA":
            cited = [
                item
                for item in review.get("supported_by") or []
                if isinstance(item, dict)
                and (
                    str(item.get("reference_id", "")) in own
                    if own
                    else str(item.get("reference_id", "")).endswith(PHYLO_SUFFIX)
                )
            ]
            if not cited:
                yield (
                    index,
                    "missing_tree_evidence",
                    f"IBA row on {term_id} is overruled ({action}) without citing the gene's "
                    "PANTHER tree placement",
                    f"Run `just phylo {organism} {gene}`, read the row for {term_id} in "
                    f"{gene}{PHYLO_SUFFIX} (where the PAINT node sits, where its seeds sit, "
                    "how the gene compares with them in the family alignment), and quote that "
                    f"row's `summary` in supported_by with reference_id "
                    f"file:{organism}/{gene}/{gene}{PHYLO_SUFFIX}. If the tree does not "
                    "support the verdict, reconsider the verdict",
                )
            elif term_id and not any(term_id in quote for item in cited for quote in _quotes(item)):
                yield (
                    index,
                    "tree_evidence_other_row",
                    f"IBA row on {term_id} cites {gene}{PHYLO_SUFFIX}, but no quote names {term_id}",
                    f"Quote the `summary` of the {term_id} row; each summary starts with its term id",
                )

        if (
            RESIDUE_FAILURE_MODE in (propagation.get("failure_modes") or [])
            and not propagation.get("residue_claims")
            and not propagation.get("residue_claims_not_applicable")
        ):
            yield (
                index,
                "missing_residue_evidence",
                f"{evidence} row on {term_id} is overruled ({action}) for residue or sub-activity "
                "loss without a checkable residue claim",
                "Add propagation_review.residue_claims (anchor and target position and residue; "
                f"{gene}{PHYLO_SUFFIX} lists the family's curated sites read off the PANTHER "
                "alignment under residue_sites), or say in residue_claims_not_applicable why "
                "the argument is not a point-residue question",
            )


def check_tree_evidence(data: dict[str, Any], report: Any, yaml_file: Optional[Path] = None) -> None:
    """Add a WARNING to ``report`` for each tree-evidence policy violation."""
    from ai_gene_review.validation.validation_report import ValidationSeverity

    for index, check_type, message, suggestion in iter_tree_evidence_violations(data, yaml_file):
        report.add_issue(
            ValidationSeverity.WARNING,
            message,
            path=f"existing_annotations[{index}].review",
            suggestion=suggestion,
            validation_category="BestPractices",
            check_type=check_type,
        )
