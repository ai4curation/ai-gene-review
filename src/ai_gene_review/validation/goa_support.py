"""Reject the gene's own GOA file as support.

``GENE-goa.tsv`` is the list of annotations under review: it says what is
annotated, never why it is true. Citing it in any ``supported_by`` list cites
an annotation as evidence for itself, so it is an error whatever the review
action. Listing the file under ``references`` (to describe what was fetched)
is not a claim of support and is not checked.

Only the review's own GOA file is checked. Another gene's GOA rows are a
different (and weaker) kind of argument, handled separately.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterator, List, Optional, Tuple

from ai_gene_review.validation.local_source_text import PROJECT_ROOT
from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)

SELF_GOA_CHECK = "supporting_text_self_goa"


def _gene_dir(yaml_file: Path, project_root: Path) -> Optional[str]:
    """The review's folder relative to ``genes/``, e.g. ``PSEPK/coaD``.

    >>> _gene_dir(PROJECT_ROOT / "genes/PSEPK/coaD/coaD-ai-review.yaml", PROJECT_ROOT)
    'PSEPK/coaD'
    """
    try:
        return yaml_file.resolve().parent.relative_to((project_root / "genes").resolve()).as_posix()
    except ValueError:
        return None


def is_self_goa(reference_id: Any, gene_dir: str) -> bool:
    """Whether ``reference_id`` names the GOA file in ``gene_dir``.

    >>> is_self_goa("file:PSEPK/coaD/coaD-goa.tsv", "PSEPK/coaD")
    True
    >>> is_self_goa("file:genes/PSEPK/coaD/coaD-goa.tsv", "PSEPK/coaD")
    True
    >>> is_self_goa("file:PSEPK/coaE/coaE-goa.tsv", "PSEPK/coaD")
    False
    >>> is_self_goa("file:PSEPK/coaD/coaD-uniprot.txt", "PSEPK/coaD")
    False
    """
    if not isinstance(reference_id, str) or not reference_id.startswith("file:"):
        return False
    identifier = reference_id.split(":", 1)[1].strip()
    if identifier.startswith("genes/"):
        identifier = identifier[len("genes/"):]
    parent, _, name = identifier.rpartition("/")
    return parent == gene_dir and name.endswith("-goa.tsv")


def iter_supports(data: Any) -> Iterator[Tuple[str, Any]]:
    """Yield ``(path, reference_id)`` for every ``supported_by`` item in the document."""

    def walk(node: Any, path: str) -> Iterator[Tuple[str, Any]]:
        if isinstance(node, dict):
            supported_by = node.get("supported_by")
            if isinstance(supported_by, list):
                for i, item in enumerate(supported_by):
                    if isinstance(item, dict):
                        prefix = f"{path}.supported_by[{i}]" if path else f"supported_by[{i}]"
                        yield prefix, item.get("reference_id")
            for key, value in node.items():
                yield from walk(value, f"{path}.{key}" if path else str(key))
        elif isinstance(node, list):
            for i, value in enumerate(node):
                yield from walk(value, f"{path}[{i}]")

    yield from walk(data, "")


def self_goa_paths(data: Any, yaml_file: Path, project_root: Path = PROJECT_ROOT) -> List[str]:
    """Paths of support items that cite the review's own GOA file."""
    gene_dir = _gene_dir(yaml_file, project_root)
    if gene_dir is None:
        return []
    return [path for path, ref in iter_supports(data) if is_self_goa(ref, gene_dir)]


def validate_self_goa_support(
    data: Any,
    report: ValidationReport,
    yaml_file: Optional[Path],
    project_root: Path = PROJECT_ROOT,
) -> None:
    """Error on every citation of the review's own ``-goa.tsv`` as support."""
    if yaml_file is None:
        return
    for path in self_goa_paths(data, yaml_file, project_root):
        report.add_issue(
            ValidationSeverity.ERROR,
            "Supporting text cites this gene's own GOA file, which records the annotation "
            "under review rather than evidence for it",
            path=path,
            suggestion=(
                "Cite the annotation's publication, a curated UniProt statement, or your own "
                "analysis; if nothing independent supports the row, use UNDECIDED"
            ),
            validation_category="BestPractices",
            check_type=SELF_GOA_CHECK,
        )
