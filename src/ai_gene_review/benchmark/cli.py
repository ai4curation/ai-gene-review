"""``ai-gene-review benchmark`` commands: build, check, export, import, score, validate."""

from __future__ import annotations

from pathlib import Path
from enum import Enum
from typing import Annotated, Optional

import typer
import yaml

from ai_gene_review.benchmark.build import build_from_reviews, build_goa, load_context
from ai_gene_review.benchmark.checks import report_markdown, run_checks, validate_schema
from ai_gene_review.benchmark.importers import peptalk as peptalk_importer
from ai_gene_review.benchmark.importers import reviews as reviews_importer
from ai_gene_review.benchmark.predictions import (
    Verdicts,
    claims,
    read_prediction_set,
    verdicts,
    write_predictions,
)
from ai_gene_review.benchmark.run import export, score, score_markdown
from ai_gene_review.benchmark.sources import DEFAULT_CACHE, sha256
from ai_gene_review.benchmark.yaml_io import load_yaml

benchmark_app = typer.Typer(
    help="Time-split protein annotation benchmarks (see docs/benchmarks.md)."
)

CacheOpt = Annotated[
    Path, typer.Option(help="Cache folder for GO releases and UniProt responses.")
]
GenesOpt = Annotated[
    Path, typer.Option(help="Folder of gene reviews, used to attach review actions.")
]


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
    """Validate a benchmark document (Benchmark, BenchmarkSpec, CheckReport, ...).

    A ``.jsonl`` file is read as Prediction records and validated as a PredictionSet.
    """
    if path.suffix == ".jsonl":
        target_class = "PredictionSet"
    try:
        data = (
            read_prediction_set(path)
            if target_class == "PredictionSet"
            else load_yaml(path)
        )
    except (ValueError, OSError, yaml.YAMLError) as exc:
        raise typer.BadParameter(f"{path}: {exc}") from exc
    require_valid(data, target_class, path)
    typer.echo(f"{path}: valid {target_class}")


class Importer(str, Enum):
    """Native predictor outputs that ``benchmark import`` converts."""

    peptalk = "peptalk"
    reviews = "reviews"


class ExportFormat(str, Enum):
    peptalk = "peptalk"


@benchmark_app.command("export")
def export_cmd(
    benchmark_file: Annotated[Path, typer.Argument(help="Benchmark YAML.")],
    out_dir: Annotated[
        Optional[Path],
        typer.Option("--out-dir", "-o", help="Default: <benchmark folder>/run-inputs."),
    ] = None,
    for_predictor: Annotated[
        Optional[list[ExportFormat]],
        typer.Option(
            "--for",
            help="Also write a predictor's native input (peptalk: <id>-claims.peptalk.tsv).",
        ),
    ] = None,
    cache: CacheOpt = DEFAULT_CACHE,
) -> None:
    """Write generic run inputs: FASTA, <id>-claims.yaml (a ClaimSet) and baseline GOA files."""
    benchmark = load_yaml(benchmark_file)
    ctx, _ = load_context(benchmark["spec"], cache)
    target = out_dir or benchmark_file.parent / "run-inputs"
    written, skipped = export(benchmark, ctx, target)
    if ExportFormat.peptalk in (for_predictor or []):
        path = target / f"{benchmark['id']}-claims.peptalk.tsv"
        items = [i for i in benchmark["items"] if i.get("sequence")]
        path.write_text(peptalk_importer.claims_tsv(claims(items)))
        written.append(path)
    typer.echo(f"wrote {len(written)} files, starting {written[0]}")
    if skipped:
        typer.echo(
            f"skipped {len(skipped)} item(s) with no pinned sequence: {', '.join(skipped)}",
            err=True,
        )


@benchmark_app.command("import")
def import_cmd(
    benchmark_file: Annotated[Path, typer.Argument(help="Benchmark YAML.")],
    inputs: Annotated[
        list[Path],
        typer.Argument(
            help="Native outputs: peptalk JSONL files, or one genes folder."
        ),
    ],
    source: Annotated[
        Importer, typer.Option("--from", help="Format of the native outputs.")
    ],
    output: Annotated[
        Path,
        typer.Option(
            "--output",
            "-o",
            help="Predictions file (.jsonl, or .yaml for a PredictionSet).",
        ),
    ],
    condition: Annotated[
        Optional[str],
        typer.Option(help="Condition name, for reviews (default agent-review)."),
    ] = None,
    predictor: Annotated[
        Optional[str],
        typer.Option(
            help="Predictor name, for reviews (default ai-gene-review or ai-gene-review:<model>)."
        ),
    ] = None,
    model: Annotated[
        Optional[str], typer.Option(help="Model that wrote the reviews.")
    ] = None,
    cache: CacheOpt = DEFAULT_CACHE,
) -> None:
    """Convert a predictor's native output into generic Prediction records."""
    benchmark = load_yaml(benchmark_file)
    try:
        if source is Importer.peptalk:
            if any(value is not None for value in (condition, predictor, model)):
                raise typer.BadParameter(
                    "--condition, --predictor and --model apply only to reviews"
                )
            predictions = peptalk_importer.predictions(
                benchmark, peptalk_importer.read_jsonl(inputs)
            )
        else:
            if len(inputs) != 1 or not inputs[0].is_dir():
                raise typer.BadParameter("--from reviews takes one genes folder")
            ctx, _ = load_context(benchmark["spec"], cache)
            predictions = reviews_importer.predictions(
                benchmark,
                ctx,
                inputs[0],
                condition or "agent-review",
                predictor or (f"ai-gene-review:{model}" if model else "ai-gene-review"),
                model,
            )
        require_valid({"predictions": predictions}, "PredictionSet", output)
        verdicts(benchmark, predictions)
    except ValueError as exc:
        raise typer.BadParameter(str(exc)) from exc
    write_predictions(benchmark["id"], predictions, output)
    typer.echo(f"wrote {len(predictions)} predictions to {output}")


@benchmark_app.command("score")
def score_cmd(
    benchmark_file: Annotated[Path, typer.Argument(help="Benchmark YAML.")],
    predictions: Annotated[
        list[Path],
        typer.Option(
            "--predictions",
            "-p",
            help="Prediction files, .jsonl or PredictionSet .yaml (repeatable).",
        ),
    ],
    threshold: Annotated[
        Optional[float],
        typer.Option(
            help="Count a prediction with a score but no verdict as yes at or above this."
        ),
    ] = None,
    output: Annotated[
        Optional[Path],
        typer.Option(
            "--output", "-o", help="Default: <id>-scores.yaml beside the benchmark."
        ),
    ] = None,
) -> None:
    """Tally predictions per condition, predictor, role (target, NOT target, decoy, shuffled) and item."""
    benchmark = load_yaml(benchmark_file)
    answers: Verdicts = {}
    for path in predictions:
        try:
            data = read_prediction_set(path)
            require_valid(data, "PredictionSet", path)
            if data.get("benchmark_id", benchmark["id"]) != benchmark["id"]:
                raise ValueError(
                    f"expected benchmark_id {benchmark['id']}, got {data['benchmark_id']}"
                )
            found = verdicts(benchmark, data["predictions"], threshold)
            duplicate = next((key for key in found if key in answers), None)
            if duplicate:
                raise ValueError(f"duplicate prediction for {duplicate}")
            answers.update(found)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            raise typer.BadParameter(f"{path}: {exc}") from exc
    report = score(
        benchmark,
        answers,
        [f"{p} sha256:{sha256(p)}" for p in predictions],
    )
    path = output or benchmark_file.with_name(f"{benchmark['id']}-scores.yaml")
    require_valid(report, "ScoreReport", path)
    dump_yaml(report, path)
    path.with_suffix(".md").write_text(score_markdown(report))
    typer.echo(score_markdown(report))
