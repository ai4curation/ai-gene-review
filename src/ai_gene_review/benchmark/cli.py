"""``ai-gene-review benchmark`` commands: build, check, export, score, validate."""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Annotated, Any, Optional

import typer
import yaml

from ai_gene_review.benchmark.build import build_from_reviews, build_goa, load_context
from ai_gene_review.benchmark.checks import report_markdown, run_checks, validate_schema
from ai_gene_review.benchmark.run import (
    export,
    peptalk_verdicts,
    read_jsonl,
    review_verdicts,
    score,
    score_markdown,
)
from ai_gene_review.benchmark.sources import DEFAULT_CACHE

benchmark_app = typer.Typer(
    help="Time-split protein annotation benchmarks (see docs/benchmarks.md)."
)

CacheOpt = Annotated[
    Path, typer.Option(help="Cache folder for GO releases and UniProt responses.")
]
GenesOpt = Annotated[
    Path, typer.Option(help="Folder of gene reviews, used to attach review actions.")
]


def isoformat_dates(value: Any) -> Any:
    """Replace YAML-parsed dates with ISO strings, recursively (the schema's dates are strings).

    >>> isoformat_dates({"d": date(2025, 6, 1), "l": [date(2026, 1, 2)]})
    {'d': '2025-06-01', 'l': ['2026-01-02']}
    """
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: isoformat_dates(v) for k, v in value.items()}
    if isinstance(value, list):
        return [isoformat_dates(v) for v in value]
    return value


def load_yaml(path: Path) -> dict:
    """Read a YAML mapping, with dates as ISO strings."""
    return isoformat_dates(yaml.safe_load(path.read_text()))


def dump_yaml(data: dict, path: Path) -> None:
    """Write YAML keeping key order."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100)
    )


def require_valid(data: dict, target_class: str, path: Path) -> None:
    """Exit with the schema problems if a document does not validate."""
    problems = validate_schema(data, target_class)
    if problems:
        for problem in problems:
            typer.echo(f"{path}: {problem}", err=True)
        raise typer.Exit(1)


def benchmark_path(out_dir: Path, benchmark_id: str) -> Path:
    """Conventional path of a benchmark file in its folder."""
    return out_dir / f"{benchmark_id}.yaml"


@benchmark_app.command("build")
def build_cmd(
    spec_path: Annotated[Path, typer.Argument(help="BenchmarkSpec YAML.")],
    out_dir: Annotated[
        Path, typer.Option("--out-dir", "-o", help="Folder for the benchmark.")
    ] = Path("benchmarks"),
    reviews: Annotated[
        Optional[list[Path]], typer.Option(help="Review YAMLs for REVIEW_DERIVED mode.")
    ] = None,
    genes_dir: GenesOpt = Path("genes"),
    cache: CacheOpt = DEFAULT_CACHE,
) -> None:
    """Draw a benchmark from a spec and write <out-dir>/<id>.yaml."""
    spec = load_yaml(spec_path)
    require_valid(spec, "BenchmarkSpec", spec_path)
    ctx, sources = load_context(spec, cache)
    if spec.get("mode", "GOA_TIME_SPLIT") == "REVIEW_DERIVED":
        if not reviews:
            raise typer.BadParameter("REVIEW_DERIVED mode needs --reviews")
        benchmark = build_from_reviews(spec, ctx, sources, reviews, genes_dir, cache)
    else:
        benchmark = build_goa(spec, ctx, sources, cache, genes_dir)
    path = benchmark_path(out_dir, spec["id"])
    require_valid(benchmark, "Benchmark", path)
    dump_yaml(benchmark, path)
    n_targets = sum(len(i["target_annotations"]) for i in benchmark["items"])
    typer.echo(f"wrote {path}: {len(benchmark['items'])} items, {n_targets} targets")


@benchmark_app.command("check")
def check_cmd(
    benchmark_file: Annotated[Path, typer.Argument(help="Benchmark YAML.")],
    uniprot: Annotated[
        bool, typer.Option(help="Fetch current UniProt entries for the leakage check.")
    ] = True,
    genes_dir: GenesOpt = Path("genes"),
    cache: CacheOpt = DEFAULT_CACHE,
    strict: Annotated[bool, typer.Option(help="Exit 1 if any check FAILs.")] = True,
) -> None:
    """Run the deterministic checks; write <id>-check-report.yaml and .md beside the benchmark."""
    benchmark = load_yaml(benchmark_file)
    ctx, _ = load_context(benchmark["spec"], cache)
    report = run_checks(benchmark, ctx, genes_dir, uniprot=uniprot)
    stem = benchmark_file.with_name(f"{benchmark['id']}-check-report")
    require_valid(report, "CheckReport", stem.with_suffix(".yaml"))
    dump_yaml(report, stem.with_suffix(".yaml"))
    stem.with_suffix(".md").write_text(report_markdown(report))
    for row in report["summary"]:
        typer.echo(
            f"{row['check']:20} pass {row['passed']:4}  info {row['info']:4}  "
            f"warn {row['warned']:4}  fail {row['failed']:4}"
        )
    failed = sum(row["failed"] for row in report["summary"])
    if strict and failed:
        raise typer.Exit(1)


@benchmark_app.command("validate")
def validate_cmd(
    path: Annotated[Path, typer.Argument(help="YAML document.")],
    target_class: Annotated[
        str, typer.Option("--class", "-C", help="Schema class.")
    ] = "Benchmark",
) -> None:
    """Validate a benchmark document (Benchmark, BenchmarkSpec, CheckReport, AgentEvaluation, ...)."""
    require_valid(load_yaml(path), target_class, path)
    typer.echo(f"{path}: valid {target_class}")


@benchmark_app.command("export")
def export_cmd(
    benchmark_file: Annotated[Path, typer.Argument(help="Benchmark YAML.")],
    out_dir: Annotated[
        Optional[Path],
        typer.Option("--out-dir", "-o", help="Default: <benchmark folder>/run-inputs."),
    ] = None,
    cache: CacheOpt = DEFAULT_CACHE,
) -> None:
    """Write FASTA, peptalk claims TSV, and per-protein baseline GOA files for the conditions."""
    benchmark = load_yaml(benchmark_file)
    ctx, _ = load_context(benchmark["spec"], cache)
    written, skipped = export(
        benchmark, ctx, out_dir or benchmark_file.parent / "run-inputs"
    )
    typer.echo(f"wrote {len(written)} files, starting {written[0]}")
    if skipped:
        typer.echo(
            f"skipped {len(skipped)} item(s) with no pinned sequence: {', '.join(skipped)}",
            err=True,
        )


@benchmark_app.command("score")
def score_cmd(
    benchmark_file: Annotated[Path, typer.Argument(help="Benchmark YAML.")],
    peptalk: Annotated[
        Optional[list[Path]],
        typer.Option(help="peptalk ask JSONL output (repeatable)."),
    ] = None,
    reviews_dir: Annotated[
        Optional[Path],
        typer.Option(
            help="Genes folder of reviews made under the AGENT_REVIEW condition."
        ),
    ] = None,
    review_condition: Annotated[
        str, typer.Option(help="Condition name for --reviews-dir verdicts.")
    ] = "agent-review",
    output: Annotated[
        Optional[Path],
        typer.Option(
            "--output", "-o", help="Default: <id>-scores.yaml beside the benchmark."
        ),
    ] = None,
    cache: CacheOpt = DEFAULT_CACHE,
) -> None:
    """Tally verdicts per condition, role (target, NOT target, decoy, shuffled) and item."""
    benchmark = load_yaml(benchmark_file)
    verdicts = peptalk_verdicts(benchmark, read_jsonl(peptalk or []))
    inputs = [str(p) for p in peptalk or []]
    if reviews_dir:
        ctx, _ = load_context(benchmark["spec"], cache)
        verdicts.update(review_verdicts(benchmark, ctx, reviews_dir, review_condition))
        inputs.append(str(reviews_dir))
    report = score(benchmark, verdicts, inputs)
    path = output or benchmark_file.with_name(f"{benchmark['id']}-scores.yaml")
    require_valid(report, "ScoreReport", path)
    dump_yaml(report, path)
    path.with_suffix(".md").write_text(score_markdown(report))
    typer.echo(score_markdown(report))
