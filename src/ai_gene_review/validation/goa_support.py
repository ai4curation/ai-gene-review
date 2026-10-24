"""Reject GOA files as support.

``GENE-goa.tsv`` is the list of annotations under review: it says what is
annotated, never why it is true. Citing it in any ``supported_by`` list cites
an annotation as evidence for itself, so it is an error whatever the review
action. Another gene's GOA file is rejected too: that a paralog or partner
carries a term is the state of its annotation, not evidence about this gene;
cite the evidence behind that annotation instead. Listing a GOA file under
``references`` (to describe what was fetched) is not a claim of support and is
not checked; neither are ``references[].findings``, where a quoted GAF row is a
statement about the GOA table itself. That is the one place a GOA quote can
still appear, so keep such findings descriptive. Only dict items are inspected;
the schema makes every ``supported_by`` item a mapping.

Prediction reviews (``*-predictions*.yaml``) are checked too, by
``prediction_evidence``. There the prediction, not the GOA row, is under review,
but ``supported_by`` still has to show the predicted term is true or false; that
it is already in GOA (a CNN or LSP assessment) is stated in the summary.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any, Iterator, List, Optional, Sequence, Tuple

import yaml

from ai_gene_review.validation.local_source_text import PROJECT_ROOT
from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)

GOA_SUPPORT_CHECK = "supporting_text_goa_file"


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


def is_goa_file(reference_id: Any) -> bool:
    """Whether ``reference_id`` names any gene's GOA file.

    >>> is_goa_file("file:PSEPK/coaE/coaE-goa.tsv")
    True
    >>> is_goa_file("file:PSEPK/coaD/coaD-uniprot.txt")
    False
    >>> is_goa_file("GO_REF:0000120")
    False
    """
    if not isinstance(reference_id, str) or not reference_id.startswith("file:"):
        return False
    return reference_id.split(":", 1)[1].strip().endswith("-goa.tsv")


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


def goa_support_paths(
    data: Any, yaml_file: Optional[Path], project_root: Path = PROJECT_ROOT
) -> List[Tuple[str, bool]]:
    """``(path, is_own)`` for every support item citing a GOA file.

    ``is_own`` says whether it is the review's own GOA file (False when the
    review's location is unknown).
    """
    gene_dir = _gene_dir(yaml_file, project_root) if yaml_file is not None else None
    return [
        (path, gene_dir is not None and is_self_goa(ref, gene_dir))
        for path, ref in iter_supports(data)
        if is_goa_file(ref)
    ]


def validate_goa_support(
    data: Any,
    report: ValidationReport,
    yaml_file: Optional[Path],
    project_root: Path = PROJECT_ROOT,
) -> None:
    """Error on every citation of a ``-goa.tsv`` file as support."""
    for path, own in goa_support_paths(data, yaml_file, project_root):
        if own:
            message = (
                "Supporting text cites this gene's own GOA file, which records the annotation "
                "under review rather than evidence for it"
            )
        else:
            message = (
                "Supporting text cites another gene's GOA file, which records that gene's "
                "annotation rather than evidence for it"
            )
        report.add_issue(
            ValidationSeverity.ERROR,
            message,
            path=path,
            suggestion=(
                "Cite the publication or curated UniProt statement behind the annotation, or "
                "your own analysis; if nothing independent supports the row, use UNDECIDED"
            ),
            validation_category="BestPractices",
            check_type=GOA_SUPPORT_CHECK,
        )


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Check files for GOA support citations; exit 1 if any are found.

    For files no fuller validator covers, such as BioReason/GO-GPT prediction
    sidecars (see ``validate-prediction-terms``).
    """
    parser = argparse.ArgumentParser(description="Reject GOA files cited as support.")
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)
    failed = False
    for path in args.files:
        report = ValidationReport(file_path=path, is_valid=True)
        validate_goa_support(yaml.safe_load(path.read_text()), report, path)
        for issue in report.issues:
            print(f"{path}: {issue.path}: {issue.message}")
            if issue.suggestion:
                print(f"  {issue.suggestion}")
        failed = failed or not report.is_valid
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
