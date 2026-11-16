"""Report which ontology terms the committed term-validator cache cannot answer.

``linkml-term-validator`` (LTV) checks term ids and labels cache-first: labels come
from ``cache/<prefix>/terms.csv`` and dynamic-enum memberships from
``cache/enums/*.csv``, and only a miss goes to the ontology service. When every
term a file uses is in the committed cache, its term check needs no network, so
an ontology-service outage cannot affect it (ai4curation/ai-gene-review#5731).

This tool measures that coverage. It runs LTV with ``--offline`` on the given
files, which resolves only from the cache and reports each miss as an error,
and sorts the misses into two kinds:

* a **label miss**: ``Term 'X' not found in offline cache``;
* an **enum-membership miss**: ``Cannot validate 'X' against dynamic enum 'E'
  offline``.

Any other error or warning is a real finding about the data (a wrong label, a
term outside its enum, ...) and is listed separately as ``other_findings`` with
its severity: it is not a coverage gap, and the online validators still report it
in CI.

``--warm`` first runs LTV online on the same files, which fills the cache with
whatever the service can answer, and then measures coverage offline, so the
report shows what is still missing after warming. Warming writes to the
committed ``cache/``; review and commit the result like any other change.

Usage::

    uv run python -m ai_gene_review.tools.ontology_cache_coverage genes/human/TP53
    uv run python -m ai_gene_review.tools.ontology_cache_coverage --warm --check FILES...

Gene reviews (``*-ai-review.yaml``), prediction reviews
(``*-predictions-review.yaml``) and PANTHER family reviews
(``interpro/panther/**/PTHR*-review.yaml``) are the document kinds CI checks with
LTV, so those are the kinds this tool recognises.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from ai_gene_review.cli import _tool_command

PROJECT_ROOT = Path(__file__).resolve().parents[3]
GENE_SCHEMA = Path("src/ai_gene_review/schema/gene_review.yaml")
FAMILY_SCHEMA = Path("src/ai_gene_review/schema/family_review.yaml")
OAK_CONFIG = Path("conf/oak_config.yaml")

LABEL_MISS = re.compile(r"Term '(?P<curie>[^']+)' not found in offline cache")
ENUM_MISS = re.compile(
    r"Cannot validate '(?P<curie>[^']+)' against dynamic enum '(?P<enum>[^']+)' offline"
)
FILE_HEADER = re.compile(r"^(?:❌|✅) (?P<name>\S+\.ya?ml)(?: - \d+ issue\(s\):)?\s*$")
FINDING_LINE = re.compile(
    r"^\s*(?:❌ (?P<error>ERROR)|⚠️\s+(?P<warn>WARN)): (?P<message>.+)$"
)


@dataclass(frozen=True)
class DocumentKind:
    """A document kind LTV validates: its schema and target class."""

    schema: Path
    target_class: str


GENE_REVIEW = DocumentKind(GENE_SCHEMA, "GeneReview")
PREDICTION_REVIEW = DocumentKind(GENE_SCHEMA, "PredictionReview")
FAMILY_REVIEW = DocumentKind(FAMILY_SCHEMA, "FamilyReview")


def document_kind(path: Path) -> DocumentKind | None:
    """Return the LTV document kind for a file, or None if CI does not term-check it.

    >>> document_kind(Path("genes/human/TP53/TP53-ai-review.yaml")).target_class
    'GeneReview'
    >>> document_kind(Path("genes/9PSED/X/X-dashboard-predictions-review.yaml")).target_class
    'PredictionReview'
    >>> document_kind(Path("interpro/panther/PTHR1/PTHR1-review.yaml")).target_class
    'FamilyReview'
    >>> document_kind(Path("modules/il10_signaling.yaml")) is None
    True
    """
    name = path.name
    if name.endswith("-predictions-review.yaml"):
        return PREDICTION_REVIEW
    if name.endswith("-ai-review.yaml"):
        return GENE_REVIEW
    if (
        name.startswith("PTHR")
        and name.endswith("-review.yaml")
        and "panther" in path.parts
    ):
        return FAMILY_REVIEW
    return None


def expand_inputs(inputs: list[Path]) -> dict[DocumentKind, list[Path]]:
    """Group the given files, and the recognised files under given directories, by kind."""
    grouped: dict[DocumentKind, list[Path]] = defaultdict(list)
    for item in inputs:
        if item.is_dir():
            candidates = sorted(item.rglob("*.yaml"))
        elif item.is_file():
            candidates = [item]
        else:
            raise FileNotFoundError(f"Input does not exist: {item}")
        for candidate in candidates:
            kind = document_kind(candidate)
            if kind is not None and candidate not in grouped[kind]:
                grouped[kind].append(candidate)
    return dict(grouped)


@dataclass
class CoverageReport:
    """Cache misses and other term findings from an offline LTV run."""

    files_checked: int = 0
    label_misses: dict[str, set[str]] = field(default_factory=lambda: defaultdict(set))
    enum_misses: dict[tuple[str, str], set[str]] = field(
        default_factory=lambda: defaultdict(set)
    )
    other_findings: list[tuple[str, str, str]] = field(default_factory=list)
    unattributed_output: list[str] = field(default_factory=list)

    @property
    def covered(self) -> bool:
        """True when the cache answered every term check."""
        return not self.label_misses and not self.enum_misses

    def to_dict(self) -> dict:
        """Return a plain, deterministically ordered mapping for YAML output."""
        return {
            "files_checked": self.files_checked,
            "covered": self.covered,
            "missing_labels": [
                {"curie": curie, "files": sorted(files)}
                for curie, files in sorted(self.label_misses.items())
            ],
            "missing_enum_memberships": [
                {"curie": curie, "enum": enum, "files": sorted(files)}
                for (curie, enum), files in sorted(self.enum_misses.items())
            ],
            "other_findings": [
                {"file": path, "severity": severity, "message": message}
                for path, severity, message in sorted(self.other_findings)
            ],
        }


def parse_offline_output(
    output: str, files: list[Path], report: CoverageReport
) -> None:
    """Add the misses and errors in one offline LTV run's output to ``report``.

    LTV names each file in a multi-file run; a single-file run names none, so its
    issues belong to that file.

    >>> report = CoverageReport()
    >>> out = '''
    ... ❌ X-predictions-review.yaml - 2 issue(s):
    ...   ❌ ERROR: Cannot validate 'NCBITaxon:1' against dynamic enum 'NCBITaxonEnum' offline: enum closure not materialized
    ...   ❌ ERROR: Term 'NCBITaxon:1' not found in offline cache
    ... ✅ Y-predictions-review.yaml
    ... '''
    >>> parse_offline_output(out, [Path("a/X-predictions-review.yaml"), Path("b/Y-predictions-review.yaml")], report)
    >>> report.to_dict()["missing_labels"]
    [{'curie': 'NCBITaxon:1', 'files': ['a/X-predictions-review.yaml']}]
    >>> report.to_dict()["missing_enum_memberships"][0]["enum"]
    'NCBITaxonEnum'
    """
    by_name: dict[str, list[str]] = defaultdict(list)
    for path in files:
        by_name[path.name].append(path.as_posix())
    current = [files[0].as_posix()] if len(files) == 1 else []
    for line in output.splitlines():
        header = FILE_HEADER.match(line)
        if header:
            current = by_name.get(header.group("name"), [header.group("name")])
            continue
        finding = FINDING_LINE.match(line)
        if not finding:
            continue
        severity = finding.group("error") or finding.group("warn")
        message = finding.group("message").strip()
        if not current:
            report.unattributed_output.append(message)
            continue
        if match := LABEL_MISS.search(message):
            report.label_misses[match.group("curie")].update(current)
        elif match := ENUM_MISS.search(message):
            report.enum_misses[(match.group("curie"), match.group("enum"))].update(
                current
            )
        else:
            report.other_findings.extend((path, severity, message) for path in current)


def ltv_command(kind: DocumentKind, files: list[Path], offline: bool) -> list[str]:
    """Build the LTV ``validate-data`` command for one batch of same-kind files."""
    command = [
        *_tool_command("linkml-term-validator"),
        "validate-data",
        *[path.as_posix() for path in files],
        "-s",
        kind.schema.as_posix(),
        "-t",
        kind.target_class,
        "--labels",
        "-c",
        OAK_CONFIG.as_posix(),
    ]
    if offline:
        command.append("--offline")
    return command


def run_ltv(kind: DocumentKind, files: list[Path], offline: bool) -> str:
    """Run LTV from the project root and return its combined output."""
    completed = subprocess.run(
        ltv_command(kind, files, offline),
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return "\n".join(part for part in (completed.stdout, completed.stderr) if part)


def relative_to_root(path: Path) -> Path:
    """Express ``path`` relative to the project root, as LTV runs from there."""
    resolved = path.resolve()
    if resolved.is_relative_to(PROJECT_ROOT):
        return resolved.relative_to(PROJECT_ROOT)
    return resolved


def measure_coverage(
    grouped: dict[DocumentKind, list[Path]], warm: bool
) -> CoverageReport:
    """Optionally warm the cache online, then measure coverage offline."""
    report = CoverageReport()
    for kind, files in grouped.items():
        rel = [relative_to_root(path) for path in files]
        if warm:
            run_ltv(kind, rel, offline=False)
        parse_offline_output(run_ltv(kind, rel, offline=True), rel, report)
        report.files_checked += len(rel)
    return report


def main(argv: list[str] | None = None) -> int:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("inputs", nargs="+", type=Path, help="Files or directories")
    parser.add_argument(
        "--warm",
        action="store_true",
        help="Run the validator online first, filling the committed cache/",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 when any term check needs the ontology service",
    )
    parser.add_argument("-o", "--output", type=Path, help="Write the YAML report here")
    args = parser.parse_args(argv)

    grouped = expand_inputs(args.inputs)
    if not grouped:
        print("No gene, prediction or family review files found.", file=sys.stderr)
        return 0
    report = measure_coverage(grouped, warm=args.warm)
    text = yaml.safe_dump(report.to_dict(), sort_keys=False, allow_unicode=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    for message in report.unattributed_output:
        print(f"Unattributed validator error: {message}", file=sys.stderr)
    missing = len(report.label_misses) + len(report.enum_misses)
    print(
        f"{report.files_checked} files; {missing} cache misses; "
        f"{len(report.other_findings)} other term findings",
        file=sys.stderr,
    )
    return 1 if args.check and not report.covered else 0


if __name__ == "__main__":
    raise SystemExit(main())
