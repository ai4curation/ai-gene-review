"""Compare module family functions with curated PANTHER and Pfam assessments.

Family membership and representative gene reviews do not establish a function
throughout a family. This check reads the family review's explicit term scope.
PANTHER/PAINT identifier, membership, and ancestral-node checks remain separate.
Only asserted molecular functions are compared: prose, substrate refinements,
taxon context, and residue prerequisites are not inferred by this checker.
"""

from __future__ import annotations

import re
from collections.abc import Callable, Iterator
from pathlib import Path
from typing import Any

import yaml


SubclassPredicate = Callable[[str, str], bool]
_PANTHER_ID = re.compile(r"PANTHER:(PTHR\d{5})(?::SF\d+)?\Z")
_PFAM_ID = re.compile(r"Pfam:(PF\d{5})\Z", re.IGNORECASE)


def _family_claims(data: dict[str, Any]) -> Iterator[tuple[dict, dict]]:
    """Yield asserted and required functions together with their family descriptor."""
    from ai_gene_review.module_qc import as_list, iter_nodes

    def walk(
        assertion: dict, *, include_unasserted: bool = True
    ) -> Iterator[tuple[dict, dict]]:
        selector = assertion.get("participant") or {}
        family = selector.get("family")
        if isinstance(family, dict):
            functions: list[dict] = []
            for function in (
                assertion.get("function"),
                selector.get("required_function"),
            ):
                if not isinstance(function, dict):
                    continue
                term_id = (function.get("term") or {}).get("id")
                if any(
                    (term_id and term_id == (existing.get("term") or {}).get("id"))
                    or function == existing
                    for existing in functions
                ):
                    continue
                functions.append(function)
            for index, function in enumerate(functions):
                assertion_id = assertion.get("id")
                if index:
                    assertion_id = f"{assertion_id}:required_function"
                yield {**assertion, "id": assertion_id, "function": function}, family
            if not functions and include_unasserted:
                yield assertion, family
        complex_descriptor = selector.get("protein_complex") or {}
        for unit in as_list(complex_descriptor.get("active_units")):
            if isinstance(unit, dict):
                # A complex's overall activity is not asserted on all subunits.
                # Still descend to nested units even if this unit has no function.
                yield from walk(unit, include_unasserted=False)

    for node in iter_nodes(data):
        for annoton in as_list(node.get("annotons")):
            if isinstance(annoton, dict):
                yield from walk(annoton)


def _family_terms(family: dict) -> list[dict]:
    """Read direct and plural family IDs once each, retaining ungrounded families."""
    terms = [family.get("term"), *(family.get("family_terms") or [])]
    by_id = {
        term["id"]: term for term in terms if isinstance(term, dict) and term.get("id")
    }
    return list(by_id.values()) or [{}]


def _matches(child: str, parent: str, subclass_of: SubclassPredicate | None) -> bool:
    """Use exact IDs or an explicit subclass predicate, never label similarity.

    >>> _matches("GO:0008745", "GO:0008745", None)
    True
    >>> _matches("GO:0008745", "GO:0016787", None)
    False
    """
    return child == parent or bool(subclass_of and subclass_of(child, parent))


def _panther_verdicts(
    review: dict,
    family_id: str,
    function_id: str,
    subclass_of: SubclassPredicate | None,
) -> list[tuple[str, str, str]]:
    """Assess positive scope and exclusions in their respective GO directions."""
    verdicts = []
    subfamily_id = family_id if ":SF" in family_id else None
    for assessment in review.get("term_assessments") or []:
        assessed_id = (assessment.get("assessed_term") or {}).get("id")
        if not assessed_id:
            continue
        supports = _matches(assessed_id, function_id, subclass_of)
        restricts = _matches(function_id, assessed_id, subclass_of)
        scope = assessment.get("scope")
        reason = assessment.get("scope_reason") or "No scope rationale supplied."
        if scope == "NOT_APPLICABLE" and restricts:
            verdicts.append(
                (
                    "FAMILY_CONFLICT",
                    "error",
                    f"Family review marks {assessed_id} NOT_APPLICABLE to any member. {reason}",
                )
            )
        elif scope == "FAMILY_WIDE" and supports:
            verdicts.append(
                (
                    "FAMILY_SUPPORTED",
                    "info",
                    f"Family review supports {assessed_id} FAMILY_WIDE. {reason}",
                )
            )
        elif scope == "SUBFAMILY_ONLY":
            allowed = {
                term.get("id")
                for term in assessment.get("applicable_subfamilies") or []
            }
            allowed.discard(None)
            if subfamily_id in allowed and supports:
                verdicts.append(
                    (
                        "FAMILY_SUPPORTED",
                        "info",
                        f"Family review supports {assessed_id} for {subfamily_id}. {reason}",
                    )
                )
            elif restricts:
                if subfamily_id and allowed and subfamily_id not in allowed:
                    verdicts.append(
                        (
                            "FAMILY_CONFLICT",
                            "error",
                            f"{subfamily_id} is outside the reviewed SUBFAMILY_ONLY scope "
                            f"for {assessed_id}: {', '.join(sorted(allowed))}. {reason}",
                        )
                    )
                else:
                    verdicts.append(
                        (
                            "FAMILY_SCOPE_RESTRICTED",
                            "warning",
                            f"{assessed_id} is SUBFAMILY_ONLY; this family grounding does "
                            f"not establish the allowed subfamily scope. {reason}",
                        )
                    )
        elif scope == "RESIDUE_DETERMINED" and restricts:
            site = assessment.get("determined_by_site") or "unspecified site"
            verdicts.append(
                (
                    "FAMILY_SCOPE_RESTRICTED",
                    "warning",
                    f"{assessed_id} requires member-level assessment of residue site "
                    f"{site}; a family identifier does not establish that condition. {reason}",
                )
            )
        elif scope == "UNRESOLVED" and (supports or restricts):
            verdicts.append(
                (
                    "FAMILY_FUNCTION_UNREVIEWED",
                    "warning",
                    f"Family review leaves {assessed_id} UNRESOLVED. {reason}",
                )
            )
    return verdicts


def _pfam_verdicts(
    review: dict,
    function_id: str,
    subclass_of: SubclassPredicate | None,
) -> list[tuple[str, str, str]]:
    """Require an enables assertion, without lifting scope to a parent InterPro entry.

    Pfam's required relation has no schema default. A contributes-to assertion
    supplies evidence of participation in an activity, not independent enabling.
    """
    verdicts = []
    for annotation in review.get("proposed_annotations") or []:
        assessed_id = (annotation.get("term") or {}).get("id")
        if not assessed_id or annotation.get("aspect") != "molecular_function":
            continue
        status = annotation.get("status")
        reason = annotation.get("rationale") or "No rationale supplied."
        if status == "REJECTED" and _matches(function_id, assessed_id, subclass_of):
            verdicts.append(
                (
                    "FAMILY_SCOPE_RESTRICTED",
                    "warning",
                    f"Pfam review rejects the family-wide mapping to {assessed_id}; "
                    f"this does not establish that every member lacks the activity. {reason}",
                )
            )
        elif _matches(assessed_id, function_id, subclass_of):
            relation_id = (annotation.get("relation") or {}).get("id")
            if status in {"ACCEPTED", "PROPOSED"} and relation_id != "RO:0002327":
                relation_description = (
                    "contributes to (RO:0002326)"
                    if relation_id == "RO:0002326"
                    else relation_id or "missing relation identifier"
                )
                verdicts.append(
                    (
                        "FAMILY_SCOPE_RESTRICTED",
                        "warning",
                        f"Pfam review relates the family to {assessed_id} using "
                        f"{relation_description}; this cannot establish independent "
                        f"enabling (RO:0002327). {reason}",
                    )
                )
            elif status == "ACCEPTED":
                verdicts.append(
                    (
                        "FAMILY_SUPPORTED",
                        "info",
                        f"Pfam review has ACCEPTED {assessed_id}. {reason}",
                    )
                )
            elif status == "PROPOSED":
                verdicts.append(
                    (
                        "FAMILY_FUNCTION_PROPOSED",
                        "warning",
                        f"Pfam review has only PROPOSED {assessed_id}; curator acceptance "
                        f"is still pending. {reason}",
                    )
                )
    return verdicts


def module_family_function_findings(
    data: dict[str, Any],
    *,
    family_reviews_dir: Path = Path("interpro/panther"),
    pfam_reviews_dir: Path = Path("interpro/pfam"),
    subclass_of: SubclassPredicate | None = None,
) -> list[dict[str, Any]]:
    """Return one compliance finding per asserted family/function pair.

    Structured PANTHER reviews are resolved through the parent family for both
    PTHR and PTHR:SF identifiers. Pfam reviews apply to direct Pfam identifiers
    only; their InterPro parent is not assumed to have the same scope. Other
    family identifiers explicitly report unavailable review coverage.

    Conflicts and scope restrictions take priority over positive assertions so
    contradictory review entries remain visible. A support finding means the
    module agrees with the current review, whose own status may still be DRAFT.
    Both direct functions and participant required_function constraints are
    checked, deduplicating equal term IDs. No complex-wide function is assigned
    to a unit lacking its own function or required_function assertion.
    """
    findings = []
    cache: dict[Path, dict] = {}
    priority = {
        "FAMILY_CONFLICT": 0,
        "FAMILY_SCOPE_RESTRICTED": 1,
        "FAMILY_SUPPORTED": 2,
        "FAMILY_FUNCTION_PROPOSED": 3,
        "FAMILY_FUNCTION_UNREVIEWED": 4,
    }

    for assertion, family in _family_claims(data):
        function = assertion.get("function") or {}
        function_term = function.get("term") or {}
        function_id = function_term.get("id")
        for term in _family_terms(family):
            family_id = term.get("id")
            row = {
                "annoton_id": assertion.get("id"),
                "participant_id": family_id,
                "participant_label": family.get("preferred_term")
                or term.get("label")
                or family_id,
                "function_id": function_id,
                "function_label": function.get("preferred_term")
                or function_term.get("label")
                or function_id,
                "scope": "family",
            }
            path = None
            expected_id = None
            kind = None
            if family_id and (match := _PANTHER_ID.fullmatch(family_id)):
                accession = match.group(1)
                path = family_reviews_dir / accession / f"{accession}-review.yaml"
                expected_id, kind = f"PANTHER:{accession}", "panther"
            elif family_id and (match := _PFAM_ID.fullmatch(family_id)):
                accession = match.group(1).upper()
                path = pfam_reviews_dir / accession / f"{accession}-review.yaml"
                expected_id, kind = accession, "pfam"

            if not function_id or not function_id.startswith("GO:"):
                verdict = (
                    "NO_FUNCTION_ID",
                    "warning",
                    "The family function has no GO identifier for comparison; prose is not matched.",
                )
            elif not family_id:
                verdict = (
                    "FAMILY_ID_MISSING",
                    "warning",
                    "The family has no identifier linking it to a curated family review.",
                )
            elif path is None or not path.is_file():
                verdict = (
                    "FAMILY_REVIEW_MISSING",
                    "warning",
                    f"No supported structured family review is available for {family_id}.",
                )
            else:
                row["review_path"] = str(path)
                if path not in cache:
                    cache[path] = yaml.safe_load(path.read_text()) or {}
                review = cache[path]
                row["review_status"] = review.get("review_status")
                actual_id = review.get("family_id" if kind == "panther" else "pfam_id")
                if actual_id != expected_id:
                    verdict = (
                        "FAMILY_REVIEW_ID_MISMATCH",
                        "error",
                        f"Family review identifies {actual_id!r}, expected {expected_id}.",
                    )
                else:
                    verdicts = (
                        _panther_verdicts(review, family_id, function_id, subclass_of)
                        if kind == "panther"
                        else _pfam_verdicts(review, function_id, subclass_of)
                    )
                    verdict = (
                        min(verdicts, key=lambda v: priority[v[0]])
                        if verdicts
                        else (
                            "FAMILY_FUNCTION_UNREVIEWED",
                            "warning",
                            f"The family review has no applicable adjudication supporting or excluding {function_id}.",
                        )
                    )
            row.update(zip(("status", "severity", "message"), verdict))
            findings.append(row)
    return findings
