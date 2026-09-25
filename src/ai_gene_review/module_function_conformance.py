"""Compare module molecular-function assertions with curated gene/family reviews.

A protein accession join alone says nothing about the activity assigned to that
protein. These checks compare GO molecular-function terms, preserving review
polarity, contribution qualifiers, and isoform/context limitations. Missing
coverage is advisory; only an applicable retained NOT is a gene contradiction.
Descriptor prose, reaction substrates, and biological context are not inferred
from labels. Family representative agreement never establishes family-wide scope.
"""

from __future__ import annotations

from collections import Counter
from functools import cached_property, lru_cache
from operator import eq
from pathlib import Path
from typing import Any, Callable, Iterator

import yaml
from yaml import CSafeLoader

from ai_gene_review.module_qc import (
    as_list,
    base_accession,
    index_gene_reviews,
    iter_nodes,
)

SubclassPredicate = Callable[[str, str], bool]
_RETAINED = {"ACCEPT", "KEEP_AS_NON_CORE", "NEW"}
_DISPUTED = {"REMOVE", "MODIFY", "MARK_AS_OVER_ANNOTATED"}


def _term_id(holder: Any) -> str | None:
    """Read a direct Term id, accepting only strings."""
    value = holder.get("id") if isinstance(holder, dict) else None
    return value if isinstance(value, str) else None


def _function_id(function: dict[str, Any]) -> str | None:
    """Only GO identifiers can be compared to gene-review molecular functions."""
    curie = _term_id(function.get("term"))
    return curie if curie and curie.startswith("GO:") else None


class GoSubclassPredicate:
    """Lazy GO is-a lookup with a cached failure and explicit degraded-state report."""

    def __init__(self, adapter_string: str | None):
        self.adapter_string = adapter_string
        self.failure: str | None = None

    @cached_property
    def adapter(self) -> Any:
        """Cache either the external adapter or its failed construction once."""
        if self.adapter_string is None:
            return None
        from oaklib import get_adapter

        try:
            return get_adapter(self.adapter_string)
        except Exception as error:  # External ontology construction can fail.
            self.failure = f"GO adapter could not be loaded ({type(error).__name__})."
            return None

    @lru_cache(maxsize=8192)
    def ancestors(self, curie: str) -> frozenset[str]:
        """Use only is-a edges; stop remote retries after an external failure."""
        if self.failure or self.adapter is None:
            return frozenset()
        try:
            return frozenset(
                self.adapter.ancestors(curie, predicates=["rdfs:subClassOf"])
            )
        except Exception as error:  # External ontology queries can also fail.
            self.failure = f"GO ancestor lookup failed ({type(error).__name__})."
            return frozenset()

    def __call__(self, child: str, parent: str) -> bool:
        return child == parent or parent in self.ancestors(child)


@lru_cache(maxsize=8)
def go_subclass_predicate(
    adapter_string: str | None = "sqlite:obo:go",
) -> GoSubclassPredicate:
    """Share a lazy GO predicate across modules; failures remain visible and cached."""
    return GoSubclassPredicate(adapter_string)


def _uses(
    data: dict[str, Any],
) -> Iterator[tuple[str, dict[str, Any], dict[str, Any], str]]:
    """Yield annoton and explicit complex-unit functions, never inherited unit MFs."""

    def participant_uses(identifier: str, function: Any, participant: Any, scope: str):
        if not isinstance(participant, dict):
            participant = {}
        if isinstance(function, dict) and function:
            yield identifier, function, participant, scope
        required = participant.get("required_function")
        if isinstance(required, dict) and required:
            same = required == function or (
                isinstance(function, dict)
                and _function_id(required) is not None
                and _function_id(required) == _function_id(function)
            )
            if not same:
                required_id = (
                    f"{identifier}:required_function" if function else identifier
                )
                yield required_id, required, participant, scope
        complex_holder = participant.get("protein_complex")
        if isinstance(complex_holder, dict):
            for number, unit in enumerate(as_list(complex_holder.get("active_units"))):
                if isinstance(unit, dict):
                    unit_id = str(unit.get("id") or f"unit-{number}")
                    yield from participant_uses(
                        f"{identifier}/{unit_id}",
                        unit.get("function"),
                        unit.get("participant"),
                        "complex_unit",
                    )

    for node in iter_nodes(data):
        for number, annoton in enumerate(as_list(node.get("annotons"))):
            if isinstance(annoton, dict):
                participant = annoton.get("participant") or {}
                yield from participant_uses(
                    str(annoton.get("id") or f"{node.get('id')}/{number}"),
                    annoton.get("function"),
                    participant,
                    "gene",
                )


def _gene_holders(
    participant: dict[str, Any], scope: str
) -> Iterator[tuple[dict[str, Any], str]]:
    """Select actual participants and family exemplars, not homolog/ortholog donors."""
    selector_type = participant.get("selector_type")
    for key, expected in [("gene", "GENE"), ("gene_product", "GENE_PRODUCT")]:
        if selector_type not in (None, expected):
            continue
        holder = participant.get(key)
        if isinstance(holder, dict):
            yield holder, scope
    family = participant.get("family")
    if selector_type in (None, "FAMILY") and isinstance(family, dict):
        for member in as_list(family.get("representative_members")):
            if isinstance(member, dict):
                yield member, "family_representative"


def _supports(
    reviewed: str | None, requested: str, subclass_of: SubclassPredicate
) -> bool:
    """A reviewed specific function supports its ancestors, never the reverse."""
    return bool(
        reviewed and (reviewed == requested or subclass_of(reviewed, requested))
    )


def _isoform(curie: str) -> str | None:
    """Keep an explicitly selected isoform while using its base accession for joins."""
    accession = curie.removeprefix("UniProtKB:")
    return accession if "-" in accession else None


def _assess_review(
    review: dict[str, Any], curie: str, function_id: str, subclass_of: SubclassPredicate
) -> tuple[str, str, str]:
    """Assess one GO function against the review without interpreting free text."""
    target_isoform = _isoform(curie)
    core = as_list(review.get("core_functions"))
    core_support = any(
        _supports(_term_id(c.get("molecular_function")), function_id, subclass_of)
        for c in core
        if isinstance(c, dict)
    )
    contributes = any(
        _supports(
            _term_id(c.get("contributes_to_molecular_function")),
            function_id,
            subclass_of,
        )
        for c in core
        if isinstance(c, dict)
    )
    positive: set[str] = set()
    disputed = False
    scoped = False
    for ann in as_list(review.get("existing_annotations")):
        if not isinstance(ann, dict) or ann.get("retired"):
            continue
        assessment = ann.get("review") or {}
        action = assessment.get("action")
        ann_term = _term_id(ann.get("term"))
        ann_isoform = ann.get("isoform")
        contribution = ann.get("qualifier") == "contributes_to"
        terms = (
            [_term_id(t) for t in as_list(assessment.get("proposed_replacement_terms"))]
            if action == "MODIFY"
            else [ann_term]
        )
        if ann.get("negated"):
            # A NOT on an ancestor excludes descendants; NOT on one child does
            # not exclude other activities under the same broad parent.
            relevant_terms = [
                term
                for term in terms
                if term and (term == function_id or subclass_of(function_id, term))
            ]
            if relevant_terms and (action in _RETAINED or action == "MODIFY"):
                if (
                    ann.get("extensions")
                    or contribution
                    or (
                        ann_isoform != target_isoform
                        and (ann_isoform or target_isoform)
                    )
                ):
                    scoped = True
                else:
                    return (
                        "CONTRADICTED",
                        "error",
                        f"The review retains a NOT annotation for {', '.join(relevant_terms)}, incompatible with this function. "
                        "Resolve the module/review disagreement; any simultaneous core assertion also needs review.",
                    )
            continue
        matches = any(_supports(term, function_id, subclass_of) for term in terms)
        if target_isoform and ann_isoform != target_isoform:
            scoped |= matches
            continue
        if matches and (action in _RETAINED or action == "MODIFY"):
            if contribution:
                contributes = True
            elif ann.get("extensions"):
                scoped = True
            else:
                positive.add(action)
        if ann_term == function_id and action in _DISPUTED:
            disputed = True
    if core_support and (not target_isoform or positive):
        return (
            "CORE_SUPPORTED",
            "info",
            "The GO molecular function is reflected in core_functions (exact term or a reviewed subclass).",
        )
    if positive:
        if positive == {"KEEP_AS_NON_CORE"}:
            return (
                "NON_CORE_SUPPORTED",
                "info",
                "The review explicitly retains this function as non-core; promotion into core_functions is not implied.",
            )
        return (
            "ANNOTATION_SUPPORTED",
            "warning",
            "A retained annotation or curated replacement supports this function, but core_functions does not yet reflect it.",
        )
    if contributes:
        return (
            "CONTRIBUTES_ONLY",
            "warning",
            "The review records contribution to this activity, not independent enabling. Check whether the module participant should be a complex.",
        )
    if scoped or (core_support and target_isoform):
        return (
            "CONTEXT_REQUIRED",
            "warning",
            "Related evidence is isoform- or context-limited. It cannot automatically support or refute this particular assertion.",
        )
    if disputed:
        return (
            "REVIEW_DISAGREEMENT",
            "warning",
            "The review removes, modifies, or marks this term over-annotated and provides no retained/core support. Review the rationale; rejection of an evidence row alone is not a biological NOT.",
        )
    return (
        "FUNCTION_UNREVIEWED",
        "warning",
        "No retained annotation or core molecular function supports this GO assertion. Missing or broader evidence is a coverage gap, not proof the activity is absent.",
    )


def gene_function_findings(
    data: dict[str, Any],
    *,
    gene_index: dict[str, Path] | None = None,
    genes_dir: Path = Path("genes"),
    subclass_of: SubclassPredicate | None = None,
) -> list[dict[str, Any]]:
    """Join each asserted participant/function to its own gene review.

    Direct calls default to exact GO matching. Supply an is-a predicate to
    accept reviewed subclasses. File fixtures can be passed as ``gene_index``;
    no network or LLM interpretation is required.
    """
    if gene_index is None:
        gene_index = index_gene_reviews(genes_dir)
    if subclass_of is None:
        subclass_of = eq
    review_cache: dict[Path, dict[str, Any]] = {}
    rows: list[dict[str, Any]] = []
    for annoton_id, function, participant, scope in _uses(data):
        function_id = _function_id(function)
        function_label = (
            function.get("preferred_term")
            or (function.get("term") or {}).get("label")
            or function_id
            or "Unspecified function"
        )
        holders = list(_gene_holders(participant, scope))
        if not holders:
            # Family rows (including missing exemplars) are assessed separately.
            if participant.get("family") is not None:
                continue
            kind = participant.get("selector_type") or "UNSPECIFIED"
            rows.append(
                {
                    "annoton_id": annoton_id,
                    "participant_id": None,
                    "participant_label": kind,
                    "function_id": function_id,
                    "function_label": function_label,
                    "scope": scope,
                    "status": "PARTICIPANT_UNCHECKED",
                    "severity": "info",
                    "message": "No direct UniProt participant to compare. Abstract selectors and complex-wide activities cannot be inferred from donor or subunit gene reviews.",
                }
            )
            continue
        for holder, row_scope in holders:
            curie = _term_id(holder.get("term"))
            row = {
                "annoton_id": annoton_id,
                "participant_id": curie,
                "participant_label": holder.get("preferred_term")
                or (holder.get("term") or {}).get("label")
                or curie
                or "Ungrounded protein",
                "function_id": function_id,
                "function_label": function_label,
                "scope": row_scope,
            }
            review_path = (
                gene_index.get(base_accession(curie) or "")
                if curie and curie.startswith("UniProtKB:")
                else None
            )
            if not curie or not curie.startswith("UniProtKB:"):
                assessment = (
                    "PARTICIPANT_ID_MISSING",
                    "info",
                    "The participant lacks a UniProt identifier for joining a gene review.",
                )
            elif review_path is None:
                assessment = (
                    "REVIEW_MISSING",
                    "info",
                    "No ai-review exists for this protein; its function and core-function coverage cannot yet be checked."
                    + (
                        " The module function also lacks a GO identifier."
                        if function_id is None
                        else ""
                    ),
                )
            elif function_id is None:
                assessment = (
                    "NO_FUNCTION_ID",
                    "warning",
                    "A gene review exists, but this function lacks a GO identifier. Free-text chemistry is not automatically compared.",
                )
            else:
                path = Path(review_path)
                if path not in review_cache:
                    review_cache[path] = (
                        yaml.load(path.read_text(encoding="utf-8"), Loader=CSafeLoader)
                        or {}
                    )
                assessment = _assess_review(
                    review_cache[path], curie, function_id, subclass_of
                )
            if row_scope == "family_representative" and assessment[0] == "CONTRADICTED":
                assessment = (
                    "CONTRADICTED",
                    "warning",
                    "This representative has a retained NOT for the assigned activity. "
                    "Review the exemplar selection or family scope; this does not establish "
                    "that the entire family lacks the function.",
                )
            row.update(zip(("status", "severity", "message"), assessment))
            if review_path is not None:
                row["review_path"] = Path(review_path).as_posix()
            rows.append(row)
    return rows


def module_function_conformance(
    data: dict[str, Any],
    *,
    gene_index: dict[str, Path] | None = None,
    genes_dir: Path = Path("genes"),
    family_reviews_dir: Path = Path(__file__).resolve().parents[2] / "interpro/panther",
    pfam_reviews_dir: Path = Path(__file__).resolve().parents[2] / "interpro/pfam",
    subclass_of: SubclassPredicate | None = None,
) -> dict[str, Any]:
    """Collect gene, representative, and curated family functional compliance."""
    from ai_gene_review.module_family_conformance import module_family_function_findings

    if subclass_of is None:
        subclass_of = go_subclass_predicate()
    rows = gene_function_findings(
        data, gene_index=gene_index, genes_dir=genes_dir, subclass_of=subclass_of
    )
    rows.extend(
        module_family_function_findings(
            data,
            family_reviews_dir=family_reviews_dir,
            pfam_reviews_dir=pfam_reviews_dir,
            subclass_of=subclass_of,
        )
    )
    if isinstance(subclass_of, GoSubclassPredicate) and subclass_of.failure:
        for row in rows:
            if row["severity"] == "warning":
                row["message"] += (
                    " Ontology unavailable: non-exact support could not be checked."
                )
        rows.append(
            {
                "annoton_id": (data.get("module") or {}).get("id") or "module",
                "participant_id": None,
                "participant_label": "GO ontology",
                "function_id": None,
                "function_label": "GO is-a lookup",
                "scope": "infrastructure",
                "status": "ONTOLOGY_UNAVAILABLE",
                "severity": "warning",
                "message": subclass_of.failure
                + " Only exact GO matches were checked after the failure; "
                "coverage gaps may reflect unavailable subsumption. No further lookup attempts will be made in this run.",
            }
        )
    return {
        "rows": rows,
        "counts": dict(Counter(row["status"] for row in rows)),
        "total": len(rows),
        "core_supported": sum(row["status"] == "CORE_SUPPORTED" for row in rows),
        "conflicts": sum(row["severity"] == "error" for row in rows),
        # Coverage remains a gap in the QC summary even when it is not a CI warning.
        "gaps": sum(
            row["severity"] == "warning"
            or row["status"]
            in {
                "REVIEW_MISSING",
                "FAMILY_REVIEW_MISSING",
                "FAMILY_ID_MISSING",
                "PARTICIPANT_ID_MISSING",
            }
            for row in rows
        ),
    }
