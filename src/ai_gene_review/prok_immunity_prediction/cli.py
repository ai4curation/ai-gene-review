"""CLI for the prokaryotic immunity prediction project."""

from __future__ import annotations

import json
from pathlib import Path

import typer

from ai_gene_review.prok_immunity_prediction.evaluation import (
    evaluate_predictions,
    normalize_benchmark_table,
)
from ai_gene_review.prok_immunity_prediction.pipeline import run_pipeline

app = typer.Typer(help="Predict prokaryotic immunity genes with PLM embeddings and defense databases.")


@app.command("run")
def run_command(
    input_path: Path = typer.Option(..., "--input", "-i", exists=True, dir_okay=False),
    output_dir: Path = typer.Option(..., "--output-dir", "-o"),
    family_config: Path = typer.Option(..., "--family-config", exists=True, dir_okay=False),
    organism_code: str = typer.Option(..., "--organism", "-g"),
    taxon_id: str = typer.Option("NCBITaxon:2", "--taxon-id"),
    gff_path: Path | None = typer.Option(None, "--gff", exists=True, dir_okay=False),
    embedder: str = typer.Option("esm2", "--embedder"),
    model_name: str = typer.Option("facebook/esm2_t6_8M_UR50D", "--model-name"),
    prodigal_mode: str = typer.Option("single", "--prodigal-mode"),
    defense_finder_dir: Path | None = typer.Option(None, "--defense-finder-dir", exists=True),
    padloc_dir: Path | None = typer.Option(None, "--padloc-dir", exists=True),
    casfinder_dir: Path | None = typer.Option(None, "--casfinder-dir", exists=True),
    run_external: bool = typer.Option(True, "--run-external/--skip-external"),
    export_aigr_root: Path | None = typer.Option(None, "--export-aigr-root"),
    family_threshold: float = typer.Option(0.55, "--family-threshold"),
    novel_threshold: float = typer.Option(0.62, "--novel-threshold"),
    neighborhood_window: int = typer.Option(10, "--neighborhood-window"),
) -> None:
    """Run the full immunity-gene prediction workflow."""
    summary = run_pipeline(
        input_path=input_path,
        output_dir=output_dir,
        family_config_path=family_config,
        organism_code=organism_code,
        taxon_id=taxon_id,
        gff_path=gff_path,
        embedder_name=embedder,
        model_name=model_name,
        prodigal_mode=prodigal_mode,
        defense_finder_dir=defense_finder_dir,
        padloc_dir=padloc_dir,
        casfinder_dir=casfinder_dir,
        run_external=run_external,
        export_aigr_root=export_aigr_root,
        family_threshold=family_threshold,
        novel_threshold=novel_threshold,
        neighborhood_window=neighborhood_window,
    )
    typer.echo(json.dumps(summary, indent=2))


@app.command("evaluate")
def evaluate_command(
    predictions: Path = typer.Option(..., "--predictions", exists=True, dir_okay=False),
    benchmark: Path = typer.Option(..., "--benchmark", exists=True, dir_okay=False),
    output: Path = typer.Option(..., "--output", "-o"),
) -> None:
    """Evaluate predictions against a normalized Mordret-style benchmark."""
    metrics = evaluate_predictions(predictions, benchmark, output)
    typer.echo(json.dumps(metrics, indent=2))


@app.command("normalize-benchmark")
def normalize_benchmark_command(
    input_path: Path = typer.Option(..., "--input", exists=True, dir_okay=False),
    output_path: Path = typer.Option(..., "--output", "-o"),
    protein_id_column: str = typer.Option(..., "--protein-id-column"),
    label_column: str = typer.Option(..., "--label-column"),
    family_column: str | None = typer.Option(None, "--family-column"),
    novel_column: str | None = typer.Option(None, "--novel-column"),
) -> None:
    """Normalize a raw Mordret supplement table into project format."""
    normalized = normalize_benchmark_table(
        input_path=input_path,
        output_path=output_path,
        protein_id_column=protein_id_column,
        label_column=label_column,
        family_column=family_column,
        novel_column=novel_column,
    )
    typer.echo(str(normalized))


def main() -> None:
    """Entrypoint used by `python -m`."""
    app()


if __name__ == "__main__":
    main()
