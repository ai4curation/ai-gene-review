"""Evidence checks for PredictionReview sidecars, after LinkML shape validation.

Literature titles and quotations use the shared reference validator. Local file
excerpts allow layout whitespace and explicit ellipses. Missing source text is an
error: an offline run must not certify evidence it cannot inspect. The CLI can
fetch missing PMID caches using the repository's publication fetcher.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re

import yaml

from ai_gene_review.validation.supporting_text import build_supporting_text_validator
from ai_gene_review.validation.validation_report import ValidationReport, ValidationSeverity


SCORES = {"COR": 2, "CNN": 2, "LSP": 2, "UNC": 1, "PLI": 0, "NPI": 0, "REP": 0}


def source_path(reference_id: str, root: Path) -> Path | None:
    """Resolve supported reference identifiers without network access."""
    if reference_id.startswith("file:"):
        relative = reference_id.removeprefix("file:")
        gene_path = root / "genes" / relative
        return gene_path if gene_path.is_file() else root / relative
    if reference_id.startswith("PMID:"):
        return root / "publications" / f"PMID_{reference_id[5:]}.md"
    if reference_id.startswith("DOI:"):
        return root / "publications" / f"DOI_{reference_id[4:].replace('/', '_')}.md"
    return None


def local_quote_matches(quote: str, text: str) -> bool:
    r"""Match literal excerpt segments, ignoring only layout whitespace.

    >>> local_quote_matches('DOMAIN 40..259 ... Binding domain.', 'DOMAIN  40..259\nBinding domain.')
    True
    >>> local_quote_matches('DOMAIN 41..260', 'DOMAIN 40..259')
    False
    """
    normalized = " ".join(text.split())
    parts = [" ".join(part.split()) for part in re.split(r"\.{3}|…", quote)]
    offset = 0
    for part in filter(None, parts):
        match = normalized.find(part, offset)
        if match < 0:
            return False
        offset = match + len(part)
    return any(parts)


def validate_prediction_evidence(
    path: Path, project_root: Path, *, require_excerpts: bool = False,
) -> ValidationReport:
    """Check sidecar evidence, cached publication titles, and assessment scores."""
    data = yaml.safe_load(path.read_text())
    report = ValidationReport(file_path=path, is_valid=True)
    report.metadata["verified_quotes"] = 0
    report.metadata["verified_titles"] = 0
    root = project_root.resolve()
    validator, _ = build_supporting_text_validator(root / "publications")

    def error(message: str, location: str) -> None:
        report.add_issue(ValidationSeverity.ERROR, message, path=location)

    references = {ref["id"]: ref for ref in data.get("references", [])}
    texts: dict[str, str] = {}
    for ref_id, ref in references.items():
        source = source_path(ref_id, root)
        if source is None:
            report.add_issue(ValidationSeverity.WARNING, f"Unsupported source: {ref_id}")
            continue
        if not source.is_file():
            error(f"Source unavailable: {ref_id} ({source}); fetch the publication cache if needed",
                  "references")
            continue
        texts[ref_id] = source.read_text()
        if ref_id.startswith(("PMID:", "DOI:")):
            if validator is None:
                error("Reference validation dependency unavailable", "references")
                continue
            result = validator.validate_title(ref_id, ref["title"])
            if not result.is_valid:
                error(f"Publication title mismatch: {ref_id}: {result.message}", "references")
            else:
                report.metadata["verified_titles"] += 1

    for source in data.get("source_documents", []):
        if not (root / source).is_file():
            error(f"Source document unavailable: {source}", "source_documents")

    for i, prediction in enumerate(data.get("predictions", [])):
        review = prediction.get("review") or {}
        location = f"predictions[{i}].review"
        if not review:
            report.add_issue(ValidationSeverity.WARNING, "Prediction has no assessment", path=location)
            continue
        assessment = review.get("assessment")
        if not isinstance(assessment, str) or review.get("confidence_score") != SCORES.get(assessment):
            error("Assessment and confidence_score disagree", location)
        for j, support in enumerate(review.get("supported_by", [])):
            ref_id = support["reference_id"]
            support_path = f"{location}.supported_by[{j}]"
            if ref_id not in references:
                error(f"Supporting source not listed in references: {ref_id}", support_path)
                continue
            quote = support.get("supporting_text")
            if not quote:
                severity = ValidationSeverity.ERROR if require_excerpts else ValidationSeverity.WARNING
                report.add_issue(severity, f"No supporting excerpt: {ref_id}",
                                 path=support_path)
                continue
            if ref_id not in texts:
                continue  # Source availability already reported above.
            if ref_id.startswith("file:"):
                matched = local_quote_matches(quote, texts[ref_id])
            elif validator is not None:
                matched = validator.validate(quote, ref_id).is_valid
            else:
                matched = False
            if matched:
                report.metadata["verified_quotes"] += 1
            else:
                error(f"Supporting text does not match source: {ref_id}", support_path)
    return report


def main() -> int:
    """Validate supplied sidecars, optionally fetching missing publication caches."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path, nargs="+")
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--fetch", action="store_true", help="Fetch missing PMID caches")
    parser.add_argument("--require-excerpts", action="store_true",
                        help="Fail if a supporting source has no excerpt")
    parser.add_argument("--report", type=Path, help="Write detailed JSON validation results")
    args = parser.parse_args()
    if args.fetch:
        from ai_gene_review.etl.publication import cache_publication

        pmids: set[str] = set()
        for path in args.files:
            data = yaml.safe_load(path.read_text())
            pmids.update(ref["id"] for ref in data.get("references", [])
                         if ref["id"].startswith("PMID:"))
        for pmid in sorted(pmids):
            cache = source_path(pmid, args.project_root)
            if cache is not None and not cache.is_file():
                cache_publication(pmid, args.project_root / "publications")
    reports = [validate_prediction_evidence(path, args.project_root,
                                           require_excerpts=args.require_excerpts)
               for path in args.files]
    for report in reports:
        print(f"{report.file_path}: {report.error_count} errors, {report.warning_count} warnings; "
              f"{report.metadata['verified_titles']} titles, "
              f"{report.metadata['verified_quotes']} quotes verified")
        for issue in report.issues:
            print(issue)
    if args.report:
        import json

        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps([r.model_dump(mode="json") for r in reports], indent=2) + "\n")
    return int(any(not report.is_valid for report in reports))


if __name__ == "__main__":
    raise SystemExit(main())
