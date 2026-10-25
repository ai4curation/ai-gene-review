"""Checks for decomposed precomposed ("X involved in Y") annotations.

A MODIFY that replaces a precomposed term such as GO:0061740 *protein targeting
to lysosome involved in chaperone-mediated autophagy* by its genus X should say
where the context Y went, in ``review.decomposed_into``: a GO-CAM, a module, the
review's core functions, or a deliberate ``context_dropped``. See ``projects/INVOLVED_IN_PRECOMPOSITION.md``.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any, Iterator

import yaml

from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)

INVOLVED_IN = " involved in "
CATEGORY = "Decomposition"


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
    """Ids of all nodes, parts and annotons (and other id-bearing objects) in a module."""
    return frozenset(_ids(yaml.safe_load(path.read_text())))


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
    data: dict[str, Any], report: ValidationReport, root: Path
) -> None:
    """Check the decomposition slots of every existing-annotation review.

    * ``decomposed_into`` only with MODIFY.
    * modules resolve to ``modules/<module>.yaml``, elements to an id inside it.
    * GO-CAM models resolve to a cached ``gocams/<id>/`` folder.
    * ``context_dropped`` cannot be combined with somewhere the context went.
    * a MODIFY of an "X involved in Y" term to exactly X with no
      ``decomposed_into`` drops Y silently (warning).
    """
    for i, ann in enumerate(data.get("existing_annotations") or []):
        if not isinstance(ann, dict) or not isinstance(ann.get("review"), dict):
            continue
        review = ann["review"]
        base = f"existing_annotations[{i}].review"
        action = review.get("action")
        dec = review.get("decomposed_into") or {}

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
            if not (root / "gocams" / model).is_dir():
                _issue(
                    report,
                    ValidationSeverity.ERROR,
                    f"GO-CAM model '{model}' is not cached under gocams/",
                    f"{base}.decomposed_into.gocam_associations[{j}]",
                    "Cite a model present in gocams/index.tsv",
                    "decomposition_gocam_not_found",
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

        genus = genus_label(str((ann.get("term") or {}).get("label", "")))
        replacements = [
            str(t.get("label", ""))
            for t in review.get("proposed_replacement_terms") or []
            if isinstance(t, dict)
        ]
        if (
            action == "MODIFY"
            and genus
            and genus in replacements
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
