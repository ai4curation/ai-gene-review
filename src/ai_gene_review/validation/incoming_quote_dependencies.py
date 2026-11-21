"""Check quotes that cite local source files changed by the current diff.

The full quote validators walk every curated record. This check answers a
smaller CI question: if a PR edits, deletes, or renames a source that existing
``supporting_text`` quotes cite, do those incoming quotes still match?
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import yaml

from ai_gene_review.validation.local_source_text import (
    PROJECT_ROOT,
    load_local_quote_baseline,
    local_prefix,
    quote_digest,
)
from ai_gene_review.validation.quote_check import (
    DEFAULT_GLOBS,
    EXCLUDED_PARTS,
    FAILURES,
    Outcome,
    Quote,
    QuoteResult,
    check_quote,
    iter_quotes,
    load_baseline,
)
from ai_gene_review.validation.supporting_text import build_supporting_text_validator


@dataclass(frozen=True)
class SourceChange:
    """One path-level source change in a git diff."""

    status: str
    old_path: Path
    new_path: Path | None = None

    def paths(self) -> tuple[Path, ...]:
        """Return every path whose citations can be affected by this change."""
        if self.new_path is None or self.new_path == self.old_path:
            return (self.old_path,)
        return (self.old_path, self.new_path)


@dataclass(frozen=True)
class IncomingQuoteResult:
    """A result for one quote affected by a changed source file."""

    record_path: Path
    changed_source: Path
    result: QuoteResult

    @property
    def blocking(self) -> bool:
        return self.result.blocking


@dataclass(frozen=True)
class IncomingQuoteParseError:
    """A candidate citing file that could not be parsed."""

    record_path: Path
    changed_source: Path
    message: str

    @property
    def blocking(self) -> bool:
        return True


IncomingIssue = IncomingQuoteResult | IncomingQuoteParseError


def _repo_relative(path: Path, project_root: Path) -> Path:
    """Return *path* relative to *project_root* without requiring it to exist."""
    path = Path(path)
    if not path.is_absolute():
        return path
    return path.resolve(strict=False).relative_to(project_root.resolve(strict=False))


def _excluded(path: Path) -> bool:
    return any(part in EXCLUDED_PARTS for part in path.parts)


def normalize_reference_id(reference_id: str | None) -> str | None:
    """Return the canonical key used to match a quote to a changed source."""
    if reference_id is None:
        return None
    prefix, sep, identifier = reference_id.partition(":")
    if not sep:
        return reference_id.strip()
    return f"{prefix.strip().upper()}:{identifier.strip()}"


def _ref_mentioned(normalized_ref: str, text_lower: str) -> bool:
    """Cheap, over-matching prefilter for a normalised reference id."""
    prefix, sep, identifier = normalized_ref.partition(":")
    if not sep:
        return normalized_ref.lower() in text_lower
    return f"{prefix.lower()}:" in text_lower and identifier.lower() in text_lower


def _doi_reference_from_cache(path: Path) -> str | None:
    """Return the DOI reference id for an existing DOI cache when recorded."""
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    data = yaml.safe_load(text[3:end])
    ref = data.get("reference_id") if isinstance(data, dict) else None
    if isinstance(ref, str) and ref.upper().startswith("DOI:"):
        return ref
    return None


def _doi_reference_ids_from_filename(path: Path) -> set[str]:
    """Return DOI reference ids that could map to *path*'s cache filename.

    DOI cache names replace "/" with "_". Actual underscores are not escaped,
    so a deleted file's name may have either meaning at an underscore position.
    """
    ids = {""}
    for char in path.stem.removeprefix("DOI_"):
        replacements = ("/", "_") if char == "_" else (char,)
        ids = {prefix + replacement for prefix in ids for replacement in replacements}
    return {f"DOI:{identifier}" for identifier in ids}


def reference_ids_for_source(path: Path, project_root: Path = PROJECT_ROOT) -> set[str]:
    """Return reference ids that can resolve to a changed source path.

    ``file:`` references have two legal spellings for gene-local sources:
    ``file:ORG/GENE/name`` and ``file:genes/ORG/GENE/name``. Literature and
    Reactome caches are cited by CURIE rather than by direct file path.
    """
    rel = _repo_relative(path, project_root)
    if _excluded(rel):
        return set()
    rel_posix = rel.as_posix()
    refs = {f"file:{rel_posix}"}

    if rel.parts[:1] == ("genes",) and len(rel.parts) > 1:
        refs.add(f"file:{Path(*rel.parts[1:]).as_posix()}")

    if len(rel.parts) == 2 and rel.parts[0] == "reactome" and rel.suffix == ".md":
        refs.add(f"Reactome:{rel.stem}")

    if len(rel.parts) == 2 and rel.parts[0] == "publications" and rel.suffix == ".md":
        if rel.name.startswith("PMID_"):
            refs.add(f"PMID:{rel.stem.removeprefix('PMID_')}")
        elif rel.name.startswith("DOI_"):
            doi_ref = _doi_reference_from_cache(project_root / rel)
            refs.update(_doi_reference_ids_from_filename(rel))
            if doi_ref:
                refs.add(doi_ref)

    return refs


def default_citing_files(project_root: Path = PROJECT_ROOT) -> list[Path]:
    """Return curated YAML files whose quotes are checked by repo validators."""
    files = {
        path
        for pattern in DEFAULT_GLOBS
        for path in project_root.glob(pattern)
        if not _excluded(path)
    }
    files.update(
        path
        for path in project_root.glob("genes/*/*/*-ai-review.yaml")
        if not _excluded(path)
    )
    return sorted(files)


def parse_name_status_z(output: bytes) -> list[SourceChange]:
    """Parse ``git diff --name-status -z --find-renames`` output."""
    fields = output.split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()
    changes: list[SourceChange] = []
    i = 0
    while i < len(fields):
        status = fields[i].decode()
        i += 1
        if status.startswith(("R", "C")):
            old = Path(fields[i].decode())
            new = Path(fields[i + 1].decode())
            i += 2
            changes.append(SourceChange(status, old, new))
        else:
            path = Path(fields[i].decode())
            i += 1
            changes.append(SourceChange(status, path))
    return changes


def diff_source_changes(base: str, head: str = "HEAD") -> list[SourceChange]:
    """Read path changes from git."""
    output = subprocess.check_output(
        ["git", "diff", "--name-status", "--find-renames", "-z", base, head, "--"]
    )
    return parse_name_status_z(output)


def _source_index(
    changes: Iterable[SourceChange], project_root: Path
) -> dict[str, set[Path]]:
    by_ref: dict[str, set[Path]] = defaultdict(set)
    for change in changes:
        for path in change.paths():
            rel = _repo_relative(path, project_root)
            for ref in reference_ids_for_source(rel, project_root):
                normalized = normalize_reference_id(ref)
                if normalized:
                    by_ref[normalized].add(rel)
    return dict(by_ref)


def _missing_changed_cache_result(
    quote: Quote, changed_sources: Iterable[Path], project_root: Path
) -> QuoteResult | None:
    for source in sorted(changed_sources):
        if (
            len(source.parts) == 2
            and source.parts[0] in {"publications", "reactome"}
            and not (project_root / source).is_file()
        ):
            return QuoteResult(
                quote,
                Outcome.UNRESOLVED,
                f"{quote.reference_id} does not resolve to deleted cache {source}",
            )
    return None


def _baseline_marked(
    quote: Quote,
    result: QuoteResult,
    key: str | None,
    baseline: Mapping,
    local_baseline: Mapping[str, set[str]],
) -> QuoteResult:
    if result.outcome not in FAILURES or not key or not quote.reference_id:
        return result
    digest = quote_digest(quote.reference_id, quote.text)
    if local_prefix(quote.reference_id) is not None and digest in local_baseline.get(
        key, set()
    ):
        return QuoteResult(quote, result.outcome, result.detail, baselined=True)

    known = baseline.get(key, {})
    if digest not in known.get(result.outcome.value, set()):
        return result
    return QuoteResult(quote, result.outcome, result.detail, baselined=True)


def check_incoming_quotes(
    changes: Sequence[SourceChange],
    *,
    project_root: Path = PROJECT_ROOT,
    citing_files: Sequence[Path] | None = None,
    baseline: Mapping | None = None,
    local_baseline: Mapping[str, set[str]] | None = None,
) -> list[IncomingIssue]:
    """Recheck only quotes that cite one of *changes*' source paths."""
    by_ref = _source_index(changes, project_root)
    if not by_ref:
        return []

    baseline = (
        load_baseline(project_root / "conf" / "quote_check_baseline.yaml")
        if baseline is None
        else baseline
    )
    local_baseline = (
        load_local_quote_baseline(project_root / "conf" / "local_quote_baseline.yaml")
        if local_baseline is None
        else local_baseline
    )
    refs = set(by_ref)
    validator, _ = build_supporting_text_validator(project_root / "publications")
    issues: list[IncomingIssue] = []

    for path in citing_files or default_citing_files(project_root):
        rel = _repo_relative(path, project_root)
        if _excluded(rel):
            continue
        text = path.read_text(encoding="utf-8")
        if "supporting_text" not in text:
            continue
        text_lower = text.lower()
        matched_refs = {ref for ref in refs if _ref_mentioned(ref, text_lower)}
        if not matched_refs:
            continue

        changed_sources = sorted(
            {source for ref in matched_refs for source in by_ref[ref]}
        )
        try:
            data = yaml.safe_load(text)
        except yaml.YAMLError as exc:
            issues.extend(
                IncomingQuoteParseError(rel, source, f"not valid YAML: {exc}")
                for source in changed_sources
            )
            continue

        key = rel.as_posix()
        for quote in iter_quotes(data):
            matched_ref = normalize_reference_id(quote.reference_id)
            if matched_ref not in matched_refs:
                continue
            changed_sources = by_ref[matched_ref]
            result = _missing_changed_cache_result(
                quote, changed_sources, project_root
            ) or check_quote(quote, project_root, validator)
            if result.outcome is Outcome.VERIFIED:
                continue
            result = _baseline_marked(quote, result, key, baseline, local_baseline)
            for source in sorted(changed_sources):
                issues.append(IncomingQuoteResult(rel, source, result))

    return issues


def format_issue(issue: IncomingIssue) -> str:
    """Format one incoming-citation issue for CLI output."""
    if isinstance(issue, IncomingQuoteParseError):
        return f"ERROR {issue.record_path}: changed source {issue.changed_source}: {issue.message}"

    q = issue.result.quote
    if issue.result.blocking:
        tag = "ERROR"
    elif issue.result.baselined:
        tag = "WARN (baselined)"
    else:
        tag = "UNCHECKED"
    return (
        f"{tag} {issue.record_path}: {q.path} [{q.reference_id}] "
        f"changed source {issue.changed_source}: {issue.result.detail}"
    )


def main(argv: Sequence[str] | None = None) -> int:
    """Run the incoming local-source quote check."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("base", help="Base commit for git diff")
    parser.add_argument(
        "head", nargs="?", default="HEAD", help="Head commit for git diff"
    )
    args = parser.parse_args(argv)

    issues = check_incoming_quotes(diff_source_changes(args.base, args.head))
    for issue in issues:
        print(format_issue(issue))
    blocking = sum(1 for issue in issues if issue.blocking)
    print(
        f"Incoming local-source quotes: {len(issues) - blocking} warning/unchecked; "
        f"{blocking} blocking"
    )
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
