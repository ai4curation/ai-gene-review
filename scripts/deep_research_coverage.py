#!/usr/bin/env python3
"""Report and backfill gene deep-research provider coverage."""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence, TextIO

import yaml


RESEARCH_FILE_RE = re.compile(r"^(?P<gene>.+)-deep-research-(?P<provider>.+)\.md$")
FRONTMATTER_DELIMITER = "---"
TOP_LEVEL_FIELD_RE = re.compile(r"^(?P<key>id|gene_symbol):\s*(?P<value>.*)$")


@dataclass(frozen=True)
class GeneInfo:
    organism: str
    gene: str
    review_path: Path
    gene_symbol: str
    uniprot_id: str

    @property
    def key(self) -> str:
        return f"{self.organism}/{self.gene}"

    @property
    def gene_dir(self) -> Path:
        return self.review_path.parent


@dataclass(frozen=True)
class ResearchReport:
    organism: str
    gene: str
    filename_gene: str
    provider: str
    path: Path
    citation_files: tuple[Path, ...]
    citation_file_count: int
    citation_count: int | None
    end_time: str
    mtime: float


@dataclass(frozen=True)
class CoverageRow:
    gene_info: GeneInfo
    reports: tuple[ResearchReport, ...]

    @property
    def organism(self) -> str:
        return self.gene_info.organism

    @property
    def gene(self) -> str:
        return self.gene_info.gene

    @property
    def key(self) -> str:
        return self.gene_info.key

    @property
    def providers(self) -> tuple[str, ...]:
        return tuple(sorted({report.provider for report in self.reports}))

    @property
    def provider_count(self) -> int:
        return len(self.providers)

    @property
    def report_count(self) -> int:
        return len(self.reports)

    @property
    def citation_file_count(self) -> int:
        return sum(report.citation_file_count for report in self.reports)

    @property
    def latest_report(self) -> ResearchReport | None:
        if not self.reports:
            return None
        return max(self.reports, key=lambda report: report.mtime)

    def reports_for_provider(self, provider: str) -> tuple[ResearchReport, ...]:
        return tuple(report for report in self.reports if report.provider == provider)

    def has_provider(self, provider: str) -> bool:
        return bool(self.reports_for_provider(provider))


@dataclass(frozen=True)
class RunAttempt:
    organism: str
    gene: str
    provider: str
    status: str
    returncode: int | str
    duration_seconds: float
    output_file: str
    command: str
    detail: str


def normalize_provider(provider: str) -> str:
    return provider.strip().lower()


def parse_optional_int(value: object) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return None
    return None


def parse_frontmatter(path: Path) -> Mapping[str, object]:
    try:
        with path.open("r", encoding="utf-8", errors="ignore") as handle:
            first_line = handle.readline()
            if first_line.strip() != FRONTMATTER_DELIMITER:
                return {}
            lines: list[str] = []
            for line in handle:
                if line.strip() == FRONTMATTER_DELIMITER:
                    break
                lines.append(line.rstrip("\n"))
            else:
                return {}
    except OSError:
        return {}

    try:
        parsed = yaml.safe_load("\n".join(lines)) or {}
    except yaml.YAMLError:
        return {}
    return parsed if isinstance(parsed, Mapping) else {}


def parse_gene_review_metadata(path: Path) -> tuple[str, str]:
    values: dict[str, str] = {}
    try:
        with path.open("r", encoding="utf-8", errors="ignore") as handle:
            for line in handle:
                if line.startswith((" ", "\t", "-")):
                    continue
                match = TOP_LEVEL_FIELD_RE.match(line.rstrip("\n"))
                if not match:
                    continue
                raw_value = match.group("value").strip()
                if not raw_value:
                    continue
                try:
                    parsed_value = yaml.safe_load(raw_value)
                except yaml.YAMLError:
                    parsed_value = raw_value
                values[match.group("key")] = str(parsed_value).strip()
                if "id" in values and "gene_symbol" in values:
                    break
    except OSError:
        values = {}
    gene_symbol = values.get("gene_symbol") or path.parent.name
    uniprot_id = values.get("id") or ""
    return gene_symbol, uniprot_id


def parse_research_filename(path: Path) -> tuple[str, str] | None:
    """Return filename gene and provider for a provider-named research file."""
    name = path.name
    if name.endswith(".citations.md") or name.endswith("-citations.md"):
        return None
    match = RESEARCH_FILE_RE.match(name)
    if not match:
        return None

    provider = normalize_provider(match.group("provider"))
    if provider in {"manual", "citations"} or provider.endswith("-citations"):
        return None
    return match.group("gene"), provider


def discover_citation_files(research_path: Path) -> tuple[Path, ...]:
    """Find citation sidecars used by current and older deep-research wrappers."""
    candidates = (
        Path(f"{research_path}.citations.md"),
        research_path.with_name(f"{research_path.stem}-citations.md"),
    )
    return tuple(path for path in candidates if path.exists() and path.stat().st_size > 0)


def list_gene_reviews(
    genes_root: Path,
    *,
    organisms: set[str] | None = None,
    genes: set[str] | None = None,
    only: set[str] | None = None,
) -> tuple[GeneInfo, ...]:
    reviews: list[GeneInfo] = []
    for review_path in sorted(genes_root.glob("*/*/*-ai-review.yaml")):
        try:
            organism_dir = review_path.parent.parent
            gene_dir = review_path.parent
            organism = organism_dir.name
            gene = gene_dir.name
        except IndexError:
            continue
        expected_name = f"{gene}-ai-review.yaml"
        if review_path.name != expected_name:
            continue
        key = f"{organism}/{gene}"
        if organisms and organism not in organisms:
            continue
        if genes and gene not in genes:
            continue
        if only and key not in only and gene not in only:
            continue
        gene_symbol, uniprot_id = parse_gene_review_metadata(review_path)
        reviews.append(
            GeneInfo(
                organism=organism,
                gene=gene,
                review_path=review_path,
                gene_symbol=gene_symbol,
                uniprot_id=uniprot_id,
            )
        )
    return tuple(reviews)


def collect_reports_for_gene(gene_info: GeneInfo) -> tuple[ResearchReport, ...]:
    reports: list[ResearchReport] = []
    for path in sorted(gene_info.gene_dir.glob("*-deep-research-*.md")):
        parsed = parse_research_filename(path)
        if parsed is None:
            continue
        if not path.exists() or path.stat().st_size == 0:
            continue
        filename_gene, provider = parsed
        frontmatter = parse_frontmatter(path)
        citation_files = discover_citation_files(path)
        reports.append(
            ResearchReport(
                organism=gene_info.organism,
                gene=gene_info.gene,
                filename_gene=filename_gene,
                provider=provider,
                path=path,
                citation_files=citation_files,
                citation_file_count=len(citation_files),
                citation_count=parse_optional_int(frontmatter.get("citation_count")),
                end_time=str(frontmatter.get("end_time") or ""),
                mtime=path.stat().st_mtime,
            )
        )
    return tuple(reports)


def build_coverage(
    genes_root: Path,
    *,
    organisms: set[str] | None = None,
    genes: set[str] | None = None,
    only: set[str] | None = None,
) -> tuple[CoverageRow, ...]:
    return tuple(
        CoverageRow(gene_info=gene_info, reports=collect_reports_for_gene(gene_info))
        for gene_info in list_gene_reviews(
            genes_root, organisms=organisms, genes=genes, only=only
        )
    )


def tsv_value(value: object) -> str:
    return str(value).replace("\t", " ").replace("\n", " ").strip()


def status_header(target_provider: str | None) -> list[str]:
    header = [
        "organism",
        "gene",
        "gene_symbol",
        "uniprot_id",
        "providers",
        "provider_count",
        "report_count",
        "citation_file_count",
        "latest_provider",
        "latest_end_time",
        "latest_file",
        "review_file",
    ]
    if target_provider:
        header.extend(
            [
                "target_provider",
                "has_target_provider",
                "target_provider_reports",
                "target_provider_citation_files",
            ]
        )
    return header


def status_record(row: CoverageRow, target_provider: str | None) -> list[str]:
    latest = row.latest_report
    record = [
        row.organism,
        row.gene,
        row.gene_info.gene_symbol,
        row.gene_info.uniprot_id,
        ",".join(row.providers),
        row.provider_count,
        row.report_count,
        row.citation_file_count,
        latest.provider if latest else "",
        latest.end_time if latest else "",
        latest.path.as_posix() if latest else "",
        row.gene_info.review_path.as_posix(),
    ]
    if target_provider:
        provider_reports = row.reports_for_provider(target_provider)
        record.extend(
            [
                target_provider,
                "yes" if provider_reports else "no",
                len(provider_reports),
                sum(report.citation_file_count for report in provider_reports),
            ]
        )
    return [tsv_value(value) for value in record]


def matches_filters(
    row: CoverageRow,
    *,
    organisms: set[str] | None,
    genes: set[str] | None,
    only: set[str] | None,
) -> bool:
    if organisms and row.organism not in organisms:
        return False
    if genes and row.gene not in genes:
        return False
    if only and row.key not in only and row.gene not in only:
        return False
    return True


def filter_rows(
    rows: Sequence[CoverageRow],
    *,
    missing_provider: str | None = None,
    organisms: set[str] | None = None,
    genes: set[str] | None = None,
    only: set[str] | None = None,
) -> list[CoverageRow]:
    selected: list[CoverageRow] = []
    for row in rows:
        if not matches_filters(row, organisms=organisms, genes=genes, only=only):
            continue
        if missing_provider and row.has_provider(missing_provider):
            continue
        selected.append(row)
    return selected


def provider_summary(rows: Sequence[CoverageRow]) -> dict[str, dict[str, int]]:
    summary: dict[str, dict[str, int]] = {}
    for row in rows:
        for provider in row.providers:
            provider_reports = row.reports_for_provider(provider)
            bucket = summary.setdefault(
                provider, {"genes": 0, "reports": 0, "citation_files": 0}
            )
            bucket["genes"] += 1
            bucket["reports"] += len(provider_reports)
            bucket["citation_files"] += sum(
                report.citation_file_count for report in provider_reports
            )
    return summary


def write_status(
    all_rows: Sequence[CoverageRow],
    displayed_rows: Sequence[CoverageRow],
    *,
    target_provider: str | None,
    missing_provider: str | None,
    out: TextIO,
    include_summary: bool,
) -> None:
    provider = target_provider or missing_provider
    writer = csv.writer(out, delimiter="\t", lineterminator="\n")
    writer.writerow(status_header(provider))
    for row in displayed_rows:
        writer.writerow(status_record(row, provider))

    if not include_summary:
        return

    with_research = [row for row in all_rows if row.provider_count > 0]
    print("# summary", file=out)
    print(f"# genes_total\t{len(all_rows)}", file=out)
    print(f"# rows_displayed\t{len(displayed_rows)}", file=out)
    print(f"# genes_with_research\t{len(with_research)}", file=out)
    print(f"# genes_without_research\t{len(all_rows) - len(with_research)}", file=out)
    print(f"# reports_total\t{sum(row.report_count for row in all_rows)}", file=out)
    print(
        f"# citation_files_total\t{sum(row.citation_file_count for row in all_rows)}",
        file=out,
    )
    if provider:
        missing = [row for row in all_rows if not row.has_provider(provider)]
        print(f"# target_provider\t{provider}", file=out)
        print(f"# target_provider_missing\t{len(missing)}", file=out)
    print("# provider\tgenes\treports\tcitation_files", file=out)
    for provider_name, counts in sorted(provider_summary(all_rows).items()):
        print(
            "# provider\t"
            f"{provider_name}\t{counts['genes']}\t{counts['reports']}\t"
            f"{counts['citation_files']}",
            file=out,
        )


def build_research_command(
    provider: str,
    organism: str,
    gene: str,
    extra_args: Sequence[str] = (),
) -> list[str]:
    return ["just", f"deep-research-{provider}", organism, gene, *extra_args]


def shell_join(parts: Sequence[str]) -> str:
    return " ".join(subprocess.list2cmdline([part]) for part in parts)


def expected_output_file(genes_root: Path, organism: str, gene: str, provider: str) -> Path:
    return genes_root / organism / gene / f"{gene}-deep-research-{provider}.md"


def verify_output(
    genes_root: Path, organism: str, gene: str, provider: str
) -> tuple[Path, bool]:
    output_file = expected_output_file(genes_root, organism, gene, provider)
    ok = output_file.exists() and output_file.stat().st_size > 0
    return output_file, ok


def tail_detail(result: subprocess.CompletedProcess[str]) -> str:
    text = (result.stderr or result.stdout or "").strip()
    if not text:
        return ""
    return text.splitlines()[-1][:500]


def build_backfill_attempts(
    rows: Sequence[CoverageRow],
    *,
    provider: str,
    genes_root: Path,
    max_genes: int | None = None,
    organisms: set[str] | None = None,
    genes: set[str] | None = None,
    only: set[str] | None = None,
    extra_args: Sequence[str] = (),
) -> list[RunAttempt]:
    candidates = filter_rows(
        rows,
        missing_provider=provider,
        organisms=organisms,
        genes=genes,
        only=only,
    )
    if max_genes is not None:
        candidates = candidates[:max_genes]

    attempts: list[RunAttempt] = []
    for row in candidates:
        command = build_research_command(provider, row.organism, row.gene, extra_args)
        output_file = expected_output_file(genes_root, row.organism, row.gene, provider)
        attempts.append(
            RunAttempt(
                organism=row.organism,
                gene=row.gene,
                provider=provider,
                status="DRY_RUN",
                returncode=0,
                duration_seconds=0.0,
                output_file=output_file.as_posix(),
                command=shell_join(command),
                detail="",
            )
        )
    return attempts


def write_attempt_report(
    attempts: Sequence[RunAttempt], output_dir: Path, provider: str
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    path = output_dir / f"deep_research_missing_{provider}_{timestamp}.tsv"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "organism",
                "gene",
                "provider",
                "status",
                "returncode",
                "duration_seconds",
                "output_file",
                "command",
                "detail",
            ]
        )
        for attempt in attempts:
            writer.writerow(
                [
                    attempt.organism,
                    attempt.gene,
                    attempt.provider,
                    attempt.status,
                    attempt.returncode,
                    f"{attempt.duration_seconds:.2f}",
                    attempt.output_file,
                    attempt.command,
                    attempt.detail,
                ]
            )
    return path


def run_backfill(
    rows: Sequence[CoverageRow],
    *,
    provider: str,
    genes_root: Path,
    output_dir: Path,
    max_genes: int | None,
    organisms: set[str] | None,
    genes: set[str] | None,
    only: set[str] | None,
    execute: bool,
    timeout_seconds: int,
    stop_on_error: bool,
    extra_args: Sequence[str],
) -> int:
    attempts = build_backfill_attempts(
        rows,
        provider=provider,
        genes_root=genes_root,
        max_genes=max_genes,
        organisms=organisms,
        genes=genes,
        only=only,
        extra_args=extra_args,
    )

    mode = "execute" if execute else "dry-run"
    print(f"provider={provider}")
    print(f"mode={mode}")
    print(f"candidate_genes={len(attempts)}")

    if not execute:
        for index, attempt in enumerate(attempts, start=1):
            print(f"[{index}/{len(attempts)}] {attempt.organism}/{attempt.gene}: {attempt.command}")
        report_path = write_attempt_report(attempts, output_dir, provider)
        print(f"summary: dry_run={len(attempts)} failures=0 report={report_path}")
        return 0

    completed: list[RunAttempt] = []
    failures = 0
    for index, attempt in enumerate(attempts, start=1):
        print(f"[{index}/{len(attempts)}] {attempt.organism}/{attempt.gene}: {attempt.command}")
        command = build_research_command(
            provider, attempt.organism, attempt.gene, extra_args
        )
        started = time.monotonic()
        try:
            result = subprocess.run(
                command,
                check=False,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
            )
            duration = time.monotonic() - started
            output_file, verified = verify_output(
                genes_root, attempt.organism, attempt.gene, provider
            )
            if result.returncode == 0 and verified:
                status = "OK"
            elif result.returncode == 0:
                status = "MISSING_OUTPUT"
                failures += 1
            else:
                status = f"ERROR_{result.returncode}"
                failures += 1
            completed_attempt = RunAttempt(
                organism=attempt.organism,
                gene=attempt.gene,
                provider=provider,
                status=status,
                returncode=result.returncode,
                duration_seconds=duration,
                output_file=output_file.as_posix(),
                command=attempt.command,
                detail=tail_detail(result),
            )
        except subprocess.TimeoutExpired:
            duration = time.monotonic() - started
            failures += 1
            completed_attempt = RunAttempt(
                organism=attempt.organism,
                gene=attempt.gene,
                provider=provider,
                status="TIMEOUT",
                returncode="timeout",
                duration_seconds=duration,
                output_file=attempt.output_file,
                command=attempt.command,
                detail=f"timeout after {timeout_seconds}s",
            )

        completed.append(completed_attempt)
        print(
            f"    status={completed_attempt.status} "
            f"duration={completed_attempt.duration_seconds:.1f}s "
            f"detail={completed_attempt.detail}"
        )
        if failures and stop_on_error:
            break

    report_path = write_attempt_report(completed, output_dir, provider)
    ok_count = sum(1 for attempt in completed if attempt.status == "OK")
    print(f"summary: ok={ok_count} failures={failures} report={report_path}")
    return 1 if failures else 0


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--genes-root", default="genes", type=Path)
    parser.add_argument("--organism", nargs="+", default=None)
    parser.add_argument("--gene", nargs="+", default=None)
    parser.add_argument(
        "--only",
        nargs="+",
        default=None,
        help="Limit to gene keys like human/TP53 or bare gene directory names.",
    )


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    if argv is None:
        argv = sys.argv[1:]
    if not argv or argv[0].startswith("-"):
        argv = ["status", *argv]

    backfill_args: list[str] = []
    if argv and argv[0] in {"backfill", "run-missing"} and "--" in argv:
        separator_index = list(argv).index("--")
        backfill_args = list(argv[separator_index + 1 :])
        argv = [*argv[:separator_index]]

    parser = argparse.ArgumentParser(
        description="Report and backfill gene deep-research provider coverage."
    )
    subparsers = parser.add_subparsers(dest="command")

    status_parser = subparsers.add_parser(
        "status",
        aliases=["report"],
        help="Print one TSV row per gene with deep-research provider coverage.",
    )
    add_common_args(status_parser)
    status_parser.add_argument(
        "--provider",
        help="Add target-provider columns using this deep-research provider slug.",
    )
    status_parser.add_argument(
        "--missing-provider",
        help="Only show genes missing this deep-research provider slug.",
    )
    status_parser.add_argument(
        "--no-summary",
        action="store_true",
        help="Only print the TSV table, without comment-prefixed summary lines.",
    )

    backfill_parser = subparsers.add_parser(
        "backfill",
        aliases=["run-missing"],
        help="Plan or run deep research for genes missing a provider.",
    )
    add_common_args(backfill_parser)
    backfill_parser.add_argument(
        "provider", help="Provider slug, e.g. falcon or openscientist."
    )
    backfill_parser.add_argument("--output-dir", default="reports", type=Path)
    backfill_parser.add_argument("--max-genes", type=int, default=None)
    backfill_parser.add_argument(
        "--execute",
        "--run",
        dest="execute",
        action="store_true",
        help="Actually run just deep-research-<provider>; default is dry-run.",
    )
    backfill_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Explicitly keep dry-run mode. This is the default.",
    )
    backfill_parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=5400,
        help="Per-gene timeout for the just command when --execute is used.",
    )
    backfill_parser.add_argument(
        "--stop-on-error",
        action="store_true",
        help="Stop after the first failed provider run when --execute is used.",
    )

    args = parser.parse_args(argv)
    if (
        args.command in {"status", "report"}
        and args.provider
        and args.missing_provider
        and normalize_provider(args.provider) != normalize_provider(args.missing_provider)
    ):
        parser.error("--provider and --missing-provider must match when both are set")
    if getattr(args, "dry_run", False) and getattr(args, "execute", False):
        parser.error("--dry-run cannot be combined with --execute/--run")
    args.backfill_args = backfill_args
    return args


def args_to_set(values: Sequence[str] | None, *, normalize: bool = False) -> set[str] | None:
    if not values:
        return None
    if normalize:
        return {value.strip() for value in values if value.strip()}
    return set(values)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    organisms = args_to_set(args.organism)
    genes = args_to_set(args.gene)
    only = args_to_set(args.only)
    rows = build_coverage(
        args.genes_root, organisms=organisms, genes=genes, only=only
    )

    if args.command in {"status", "report"}:
        provider = normalize_provider(args.provider) if args.provider else None
        missing_provider = (
            normalize_provider(args.missing_provider) if args.missing_provider else None
        )
        displayed = filter_rows(
            rows,
            missing_provider=missing_provider,
            organisms=organisms,
            genes=genes,
            only=only,
        )
        write_status(
            rows,
            displayed,
            target_provider=provider,
            missing_provider=missing_provider,
            out=sys.stdout,
            include_summary=not args.no_summary,
        )
        return 0

    if args.command in {"backfill", "run-missing"}:
        return run_backfill(
            rows,
            provider=normalize_provider(args.provider),
            genes_root=args.genes_root,
            output_dir=args.output_dir,
            max_genes=args.max_genes,
            organisms=organisms,
            genes=genes,
            only=only,
            execute=args.execute,
            timeout_seconds=args.timeout_seconds,
            stop_on_error=args.stop_on_error,
            extra_args=args.backfill_args,
        )

    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
