"""Enforce the ND (No biological Data available) action policy.

``projects/NO_DATA.md`` sets one rule for ND rows: an ND that follows the
evidence-code guideline -- no literature on this gene product, in this
species, identifies a function in that aspect -- is ``ACCEPT``. IBA, ISO, ISS
or IEA rows in the same aspect do not change that, because they are not
literature on the gene. The rule rewards adherence to the evidence-code
guidelines: removing a correct ND "because an IBA covers the aspect" penalises
an annotation that did exactly what GORULE:0000054 describes.

The optional ``review.nd_case`` records which case of the project's taxonomy
applies, and the checks here keep action, case and knowledge gaps consistent:

- ``KEEP_AS_NON_CORE``, ``MARK_AS_OVER_ANNOTATED`` and ``TOO_GENERAL`` are never
  the right action for an ND row (it is either correct or stale);
- ``REMOVE``/``MODIFY`` need ``nd_case`` ``STALE`` or ``ONTOLOGY_BLOCKED``, the two
  cases where literature on the gene exists;
- ``ACCEPT`` contradicts those two cases, and contradicts a proposed
  replacement term;
- ``NEW`` proposes an ND, which only the contributing group can assert about
  its own search; a ``knowledge_gaps`` entry is the way to record the gap;
- ``TRUE_GAP`` and ``EXISTENCE`` need a ``BIOLOGY`` knowledge gap whose
  ``dark_aspect`` matches the ND aspect (or ``WHOLLY_DARK``);
- ``ACCEPT`` needs evidence that the literature was searched: a cited
  publication (PMID, DOI, PMC), or a quote from the gene's own deep-research
  or notes file recording the search. The UniProt record or the protein's
  existence level is not a search;
- ``nd_case`` on a non-ND row is a mistake.

Severity is WARNING, like the protein-binding policy: the checks guide
re-review and do not block legacy files.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Set, Tuple

#: ND annotations are only made to the three root terms (GORULE:0000011).
ROOT_ASPECT = {
    "GO:0003674": "MF",
    "GO:0008150": "BP",
    "GO:0005575": "CC",
}

#: ``KnowledgeGap.dark_aspect`` values that satisfy a gap for each ND aspect.
MATCHING_DARK_ASPECTS = {
    "MF": {"MF_DARK", "WHOLLY_DARK"},
    "BP": {"BP_DARK", "WHOLLY_DARK"},
    "CC": {"CC_DARK", "WHOLLY_DARK"},
}

#: Cases in which literature on the gene identifies a function, so the ND is wrong.
LITERATURE_CASES = frozenset({"STALE", "ONTOLOGY_BLOCKED"})

#: Cases that must be paired with a BIOLOGY knowledge gap.
GAP_CASES = frozenset({"TRUE_GAP", "EXISTENCE"})

#: Actions that describe a true-but-peripheral or overreaching claim; an ND is neither.
NON_ND_ACTIONS = frozenset({"KEEP_AS_NON_CORE", "MARK_AS_OVER_ANNOTATED", "TOO_GENERAL"})

#: Reference id prefixes that are literature.
LITERATURE_PREFIXES = ("PMID:", "DOI:", "PMC:", "PMCID:")

#: Gene-folder files that record a literature search: deep research (including
#: ``-deep-research-manual.md``) and the reviewer's notes, where CLAUDE.md says a
#: search goes when deep research fails. A negative search has no paper to cite.
SEARCH_RECORD_MARKERS = ("-deep-research", "-notes.md")


def _gaps(data: Dict[str, Any], review: Dict[str, Any]) -> List[Dict[str, Any]]:
    """All knowledge gaps visible to one ND row: its own, the gene's, its core functions'."""
    gaps: List[Dict[str, Any]] = []
    for source in [review, data, *(data.get("core_functions") or [])]:
        if isinstance(source, dict):
            gaps.extend(g for g in source.get("knowledge_gaps") or [] if isinstance(g, dict))
    return gaps


def _ref_dir(reference_id: str) -> Optional[str]:
    """The ``ORG/FOLDER`` of a ``file:`` reference, in either accepted path form.

    >>> _ref_dir("file:CANAL/CEK1/CEK1-notes.md")
    'CANAL/CEK1'
    >>> _ref_dir("file:genes/CANAL/CEK1/CEK1-notes.md")
    'CANAL/CEK1'
    >>> _ref_dir("PMID:1") is None
    True
    """
    if not reference_id.startswith("file:"):
        return None
    parts = reference_id.removeprefix("file:").strip().removeprefix("genes/").split("/")
    return "/".join(parts[:2]) if len(parts) >= 3 else None


def _own_folders(data: Dict[str, Any]) -> Set[str]:
    """Folder names taken to be the review's own when its path is unknown.

    Only for callers with no review file, such as data built in memory: the
    validator and the compliance analyzer pass the review's real folder, which
    is exact. The gene symbol, the accession, and ``SYMBOL__ACCESSION`` (an
    alternative-ORF peptide that shares its host's symbol). References are not
    scanned, since a review may cite an ortholog's files.

    >>> sorted(_own_folders({"gene_symbol": "rad51", "id": "P36601"}))
    ['P36601', 'rad51', 'rad51__P36601']
    >>> sorted(_own_folders({"id": "P1"}))
    ['P1']
    """
    symbol, accession = data.get("gene_symbol"), data.get("id")
    folders = {f for f in (symbol, accession) if f}
    if symbol and accession:
        folders.add(f"{symbol}__{accession}")
    return folders


def cites_search(
    review: Dict[str, Any], data: Dict[str, Any], gene_dir: Optional[str] = None
) -> bool:
    """Whether an ND review cites the literature search; shared by the warning and the score.

    A publication (PMID, DOI, PMC) counts wherever it is cited. A file recording
    the search (deep research or notes) counts only when it is the gene's own and
    is quoted in ``supporting_text``, the field the verbatim local-quote check
    reads (``supporting_text_fulltext`` is never checked, so it does not count);
    a nonblank quote need not be about the search, so this narrows the loophole
    rather than closing it. ``gene_dir`` (``ORG/FOLDER``, from the review's path)
    makes the own-folder test exact; without it, ``_own_folders`` is used.

    >>> gene = {"gene_symbol": "X", "id": "P1"}
    >>> cites_search({"supported_by": [{"reference_id": "PMID:1"}]}, gene)
    True
    >>> cites_search({"additional_reference_ids": ["DOI:10.1/x"]}, gene)
    True
    >>> quoted = {"reference_id": "file:DROME/X/X-notes.md", "supporting_text": "0 records"}
    >>> cites_search({"supported_by": [quoted]}, gene)
    True
    >>> cites_search({"supported_by": [dict(quoted, reference_id="file:genes/DROME/X/X-notes.md")]}, gene)
    True
    >>> cites_search({"supported_by": [{"reference_id": "file:DROME/X/X-notes.md"}]}, gene)
    False
    >>> cites_search({"additional_reference_ids": ["file:human/X/X-deep-research-falcon.md"]}, gene)
    False
    >>> cites_search({"supported_by": [dict(quoted, reference_id="file:DROME/Y/Y-notes.md")]}, gene)
    False
    >>> cites_search({"supported_by": [quoted]}, gene, gene_dir="DROME/Y")
    False
    >>> cites_search({"supported_by": [{"reference_id": "file:human/X/X-uniprot.txt",
    ...                                 "supporting_text": "PE   1: Evidence at protein level;"}]}, gene)
    False
    """
    support = [s for s in review.get("supported_by") or [] if isinstance(s, dict)]
    ids = [s.get("reference_id") for s in support] + list(review.get("additional_reference_ids") or [])
    if any(isinstance(i, str) and i.startswith(LITERATURE_PREFIXES) for i in ids):
        return True
    folders = None if gene_dir else _own_folders(data)

    def own(reference_id: str) -> bool:
        ref_dir = _ref_dir(reference_id)
        if not ref_dir:
            return False
        return ref_dir == gene_dir if gene_dir else ref_dir.split("/")[1] in folders

    return any(
        isinstance(s.get("reference_id"), str)
        and any(m in s["reference_id"] for m in SEARCH_RECORD_MARKERS)
        and own(s["reference_id"])
        and has_text(s.get("supporting_text"))
        for s in support
    )


def has_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _has_matching_gap(gaps: List[Dict[str, Any]], aspect: str | None) -> bool:
    wanted = MATCHING_DARK_ASPECTS.get(aspect or "", {"WHOLLY_DARK"})
    return any(
        "BIOLOGY" in (g.get("gap_kind") or []) and g.get("dark_aspect") in wanted
        for g in gaps
    )


def iter_nd_policy_violations(
    data: Dict[str, Any], gene_dir: Optional[str] = None
) -> Iterator[Tuple[int, str, str, str]]:
    """Yield ``(index, field, message, suggestion)`` for each ND policy violation.

    A guideline-conformant ND that cites the literature search is accepted:

        >>> search = [{"reference_id": "PMID:1"}]
        >>> nd = {"term": {"id": "GO:0003674"}, "evidence_type": "ND",
        ...       "review": {"action": "ACCEPT", "nd_case": "INFERABLE", "supported_by": search}}
        >>> list(iter_nd_policy_violations({"existing_annotations": [nd]}))
        []

    Without the search it is reported:

        >>> nd["review"] = {"action": "ACCEPT", "nd_case": "INFERABLE"}
        >>> [v[:2] for v in iter_nd_policy_violations({"existing_annotations": [nd]})]
        [(0, 'supported_by')]

    Keeping it as non-core is reported:

        >>> nd["review"] = {"action": "KEEP_AS_NON_CORE"}
        >>> [v[:2] for v in iter_nd_policy_violations({"existing_annotations": [nd]})]
        [(0, 'action')]

    So is removing it without saying that literature exists:

        >>> nd["review"] = {"action": "REMOVE"}
        >>> [v[:2] for v in iter_nd_policy_violations({"existing_annotations": [nd]})]
        [(0, 'nd_case')]

        >>> nd["review"] = {"action": "REMOVE", "nd_case": "STALE"}
        >>> list(iter_nd_policy_violations({"existing_annotations": [nd]}))
        []

    A true gap needs a matching BIOLOGY knowledge gap:

        >>> nd["review"] = {"action": "ACCEPT", "nd_case": "TRUE_GAP", "supported_by": search}
        >>> [v[:2] for v in iter_nd_policy_violations({"existing_annotations": [nd]})]
        [(0, 'nd_case')]
        >>> doc = {"existing_annotations": [nd], "knowledge_gaps": [
        ...     {"gap_statement": "x", "gap_kind": ["BIOLOGY"], "dark_aspect": "MF_DARK"}]}
        >>> list(iter_nd_policy_violations(doc))
        []
    """
    annotations = data.get("existing_annotations")
    if not isinstance(annotations, list):
        return
    for index, annotation in enumerate(annotations):
        if not isinstance(annotation, dict):
            continue
        review = annotation.get("review")
        if not isinstance(review, dict):
            continue
        action = review.get("action")
        nd_case = review.get("nd_case")
        if annotation.get("evidence_type") != "ND":
            if nd_case:
                yield (
                    index,
                    "nd_case",
                    f"nd_case {nd_case} is set on a {annotation.get('evidence_type')} row",
                    "nd_case applies only to ND (No biological Data available) rows; remove it",
                )
            continue
        term = annotation.get("term")
        term_id = term.get("id") if isinstance(term, dict) else None
        aspect = ROOT_ASPECT.get(term_id) if isinstance(term_id, str) else None

        if action in NON_ND_ACTIONS:
            yield (
                index,
                "action",
                f"ND row uses action {action}; an ND is either correct or stale",
                "ACCEPT the ND if no literature on this gene product, in this species, "
                "identifies a function in this aspect (inferred rows such as IBA/ISO do "
                "not count); otherwise REMOVE it with nd_case: STALE",
            )
        elif action == "NEW":
            yield (
                index,
                "action",
                "ND row is proposed as NEW; an ND is the contributing group's statement "
                "about its own literature search",
                "Record the unknown as a knowledge_gaps entry (gap_kind BIOLOGY, with a "
                "matching dark_aspect) instead of proposing an ND annotation",
            )
        elif action in ("REMOVE", "MODIFY") and nd_case not in LITERATURE_CASES:
            yield (
                index,
                "nd_case",
                f"ND row uses action {action} without nd_case STALE or ONTOLOGY_BLOCKED",
                "An ND is wrong only when literature on this gene product, in this "
                "species, identifies a function in this aspect. If so, set nd_case "
                "(STALE, or ONTOLOGY_BLOCKED when no fitting term existed) and quote the "
                "paper in supported_by; if not, the ND follows the guideline: ACCEPT it",
            )
        elif action == "ACCEPT" and nd_case in LITERATURE_CASES:
            yield (
                index,
                "nd_case",
                f"ND row is ACCEPTed but nd_case {nd_case} says literature exists",
                "Use REMOVE (STALE) or MODIFY (ONTOLOGY_BLOCKED), or correct nd_case",
            )

        if action == "ACCEPT" and not cites_search(review, data, gene_dir):
            yield (
                index,
                "supported_by",
                "ND row is ACCEPTed without evidence that the literature was searched",
                "Cite the search in supported_by: quote the gene's own deep-research or "
                "notes file where it records the queries and their result (when a search "
                "finds nothing there is no paper to cite), or cite the publications that "
                "were checked (PMID, DOI). The UniProt record or the protein's existence "
                "level does not show that the literature has no function to annotate",
            )

        if action == "ACCEPT" and review.get("proposed_replacement_terms"):
            yield (
                index,
                "proposed_replacement_terms",
                "ND row is ACCEPTed but still proposes replacement terms",
                "An accepted ND keeps the root term. Put an inferred term on its own NEW "
                "row, or REMOVE/MODIFY the ND with nd_case STALE if literature on this "
                "gene product identifies it",
            )

        if nd_case in GAP_CASES and not _has_matching_gap(_gaps(data, review), aspect):
            wanted = " or ".join(sorted(MATCHING_DARK_ASPECTS.get(aspect or "", {"WHOLLY_DARK"})))
            yield (
                index,
                "nd_case",
                f"nd_case {nd_case} has no matching BIOLOGY knowledge gap",
                f"Add a knowledge_gaps entry with gap_kind [BIOLOGY] and dark_aspect "
                f"{wanted} (on the review, the gene or a core function)",
            )


def review_gene_dir(yaml_file: Optional[Path]) -> Optional[str]:
    """``ORG/FOLDER`` of a review file under the project's ``genes/``, else None."""
    if yaml_file is None:
        return None
    from ai_gene_review.validation.goa_support import _gene_dir
    from ai_gene_review.validation.local_source_text import PROJECT_ROOT

    return _gene_dir(Path(yaml_file), PROJECT_ROOT)


def check_nd_policy(data: Dict[str, Any], report, yaml_file: Optional[Path] = None) -> None:
    """Add a warning for each ND policy violation in *data*."""
    from ai_gene_review.validation.validation_report import ValidationSeverity

    gene_dir = review_gene_dir(yaml_file)
    for index, field, message, suggestion in iter_nd_policy_violations(data, gene_dir):
        report.add_issue(
            ValidationSeverity.WARNING,
            message,
            path=f"existing_annotations[{index}].review.{field}",
            suggestion=suggestion,
            validation_category="BestPractices",
            check_type="nd_policy",
        )
