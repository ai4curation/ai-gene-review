"""Checks for decomposed precomposed ("X involved in Y") annotations.

A MODIFY that replaces a precomposed term such as GO:0061740 *protein targeting
to lysosome involved in chaperone-mediated autophagy* by its genus X should say
where the context Y went, in ``review.decomposed_into``: a GO-CAM, a module, the
review's core functions, or a deliberate ``context_dropped``. See ``projects/INVOLVED_IN_PRECOMPOSITION.md``.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Iterator

import yaml

from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)

INVOLVED_IN = " involved in "
CATEGORY = "Decomposition"

#: term id -> its is_a ancestors (not part_of: the context Y is a part_of ancestor)
IsAAncestors = Callable[[str], frozenset[str]]
#: term id -> its label and exact/related synonyms
TermNames = Callable[[str], frozenset[str]]


def genus_label(term_label: str) -> str | None:
    """The X half of an "X involved in Y" label, or None.

    >>> genus_label("protein targeting to lysosome involved in chaperone-mediated autophagy")
    'protein targeting to lysosome'
    >>> genus_label("obsolete proteolysis involved in protein catabolic process")
    'proteolysis'
    >>> genus_label("protein binding") is None
    True
    """
    if INVOLVED_IN not in term_label:
        return None
    return term_label.removeprefix("obsolete ").split(INVOLVED_IN, 1)[0]


def _ids(node: Any) -> Iterator[str]:
    """Every string ``id`` value in a nested YAML structure."""
    if isinstance(node, dict):
        if isinstance(node.get("id"), str):
            yield node["id"]
        for value in node.values():
            yield from _ids(value)
    elif isinstance(node, list):
        for item in node:
            yield from _ids(item)


@lru_cache(maxsize=None)
def module_element_ids(path: Path) -> frozenset[str]:
    """Ids of the nodes, parts and annotons a module defines.

    Grounding ids (GO, UniProt and other CURIEs) are excluded, so an element
    reference cannot pass by naming a term the module merely cites.
    """
    return frozenset(i for i in _ids(yaml.safe_load(path.read_text())) if ":" not in i)


@lru_cache(maxsize=None)
def gocam_activity_ids(path: Path) -> frozenset[str]:
    """Activity ids of a cached GO-CAM (``gocams/<id>/<id>-src.yaml``)."""
    doc = yaml.safe_load(path.read_text()) or {}
    return frozenset(a["id"] for a in doc.get("activities") or [] if "id" in a)


@lru_cache(maxsize=1)
def _go_adapter() -> Any:
    from oaklib import get_adapter

    return get_adapter("sqlite:obo:go")


@lru_cache(maxsize=None)
def go_is_a_ancestors(term_id: str) -> frozenset[str]:
    """is_a ancestors of a GO term (empty for obsolete or unknown terms)."""
    from oaklib.datamodels.vocabulary import IS_A

    return frozenset(
        _go_adapter().ancestors(term_id, predicates=[IS_A], reflexive=False)
    )


@lru_cache(maxsize=None)
def go_names(term_id: str) -> frozenset[str]:
    """Label and synonyms of a GO term, so a genus matches across label drift."""
    adapter = _go_adapter()
    label = adapter.label(term_id)
    return frozenset(filter(None, [label, *adapter.entity_aliases(term_id)]))


def is_genus_replacement(
    term: dict[str, Any],
    replacement: dict[str, Any],
    is_a_ancestors: IsAAncestors | None = None,
    names: TermNames | None = None,
) -> bool:
    """Whether a MODIFY replacement is the genus X (or a broader is_a ancestor) of an
    "X involved in Y" term.

    With ontology lookups, a replacement that is an is_a ancestor of the term, or
    whose label or synonym equals the label-derived genus, counts. Without them,
    only an exact label match counts.

    >>> t = {"id": "GO:1", "label": "negative regulation of cell proliferation involved in x"}
    >>> r = {"id": "GO:2", "label": "negative regulation of cell population proliferation"}
    >>> is_genus_replacement(t, r)
    False
    >>> is_genus_replacement(t, r, names=lambda i: frozenset({r["label"], "negative regulation of cell proliferation"}))
    True
    >>> is_genus_replacement(t, r, is_a_ancestors=lambda i: frozenset({"GO:2"}))
    True
    """
    genus = genus_label(str(term.get("label", "")))
    if not genus:
        return False
    rid = str(replacement.get("id", ""))
    if is_a_ancestors is not None and rid in is_a_ancestors(str(term.get("id", ""))):
        return True
    known = {str(replacement.get("label", ""))}
    if names is not None and rid.startswith("GO:"):
        known |= names(rid)
    return genus in known


def _issue(
    report: ValidationReport,
    severity: ValidationSeverity,
    message: str,
    path: str,
    suggestion: str,
    check_type: str,
) -> None:
    report.add_issue(
        severity,
        message,
        path=path,
        suggestion=suggestion,
        validation_category=CATEGORY,
        check_type=check_type,
    )


def check_decomposition(
    data: dict[str, Any],
    report: ValidationReport,
    root: Path,
    is_a_ancestors: IsAAncestors | None = None,
    names: TermNames | None = None,
) -> None:
    """Check the decomposition slots of every existing-annotation review.

    * ``decomposed_into`` only with MODIFY.
    * modules resolve to ``modules/<module>.yaml``, elements to an id inside it.
    * GO-CAM models resolve to a cached ``gocams/<id>/`` folder, and activities
      to an activity of that model.
    * ``decomposed_into`` is not empty.
    * ``context_dropped`` cannot be combined with somewhere the context went.
    * a MODIFY of an "X involved in Y" term to exactly X with no
      ``decomposed_into`` drops Y silently (warning). "Exactly X" is judged by
      :func:`is_genus_replacement`, using GO when ``is_a_ancestors``/``names``
      are given (as ``just validate`` does) and the label alone otherwise.
    """
    for i, ann in enumerate(data.get("existing_annotations") or []):
        if not isinstance(ann, dict) or not isinstance(ann.get("review"), dict):
            continue
        review = ann["review"]
        base = f"existing_annotations[{i}].review"
        action = review.get("action")
        dec = review.get("decomposed_into") or {}
        if "decomposed_into" in review and not any(dec.values()):
            _issue(
                report,
                ValidationSeverity.ERROR,
                "decomposed_into is empty",
                f"{base}.decomposed_into",
                "Name a GO-CAM, a module element, in_core_functions or context_dropped",
                "decomposition_empty",
            )

        if dec and action != "MODIFY":
            _issue(
                report,
                ValidationSeverity.ERROR,
                f"decomposed_into used with action {action}",
                base,
                "decomposed_into qualifies a MODIFY's replacement; use MODIFY or drop it",
                "decomposition_requires_modify",
            )

        for j, assoc in enumerate(dec.get("module_associations") or []):
            module = assoc.get("module", "")
            mpath = root / "modules" / f"{module}.yaml"
            apath = f"{base}.decomposed_into.module_associations[{j}]"
            if not mpath.is_file():
                _issue(
                    report,
                    ValidationSeverity.ERROR,
                    f"Module '{module}' not found at modules/{module}.yaml",
                    apath,
                    "Use the module file stem, or create the module first",
                    "decomposition_module_not_found",
                )
                continue
            element = assoc.get("element")
            if element and element not in module_element_ids(mpath):
                _issue(
                    report,
                    ValidationSeverity.ERROR,
                    f"Element '{element}' not found in modules/{module}.yaml",
                    apath,
                    "Use the id of a node, part or annoton in that module",
                    "decomposition_element_not_found",
                )

        for j, assoc in enumerate(dec.get("gocam_associations") or []):
            model = str(assoc.get("model", "")).removeprefix("gomodel:")
            gpath = f"{base}.decomposed_into.gocam_associations[{j}]"
            src = root / "gocams" / model / f"{model}-src.yaml"
            if not src.is_file():
                _issue(
                    report,
                    ValidationSeverity.ERROR,
                    f"GO-CAM model '{model}' is not cached under gocams/",
                    gpath,
                    "Cite a model present in gocams/index.tsv",
                    "decomposition_gocam_not_found",
                )
                continue
            activity = assoc.get("activity")
            if activity and activity not in gocam_activity_ids(src):
                _issue(
                    report,
                    ValidationSeverity.ERROR,
                    f"Activity '{activity}' not found in GO-CAM {model}",
                    gpath,
                    "Use an activity id from the cached model's activities",
                    "decomposition_activity_not_found",
                )

        carried = bool(
            dec.get("module_associations")
            or dec.get("gocam_associations")
            or dec.get("in_core_functions")
        )
        if dec.get("context_dropped") and carried:
            _issue(
                report,
                ValidationSeverity.ERROR,
                "decomposed_into.context_dropped is set but the context is also carried",
                f"{base}.decomposed_into",
                "Either drop the context or record where it went, not both",
                "decomposition_contradictory",
            )

        term = ann.get("term") or {}
        genus = genus_label(str(term.get("label", "")))
        to_genus = any(
            is_genus_replacement(term, t, is_a_ancestors, names)
            for t in review.get("proposed_replacement_terms") or []
            if isinstance(t, dict)
        )
        if (
            action == "MODIFY"
            and to_genus
            and not carried
            and not dec.get("context_dropped")
        ):
            _issue(
                report,
                ValidationSeverity.WARNING,
                f"MODIFY to the genus '{genus}' of a precomposed term drops its 'involved in' context silently",
                base,
                "Add decomposed_into: gocam_associations, module_associations, "
                "in_core_functions, or context_dropped with a reason",
                "decomposition_context_dropped_silently",
            )
