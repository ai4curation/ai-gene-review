"""Typer sub-app for sequence-only reads (registered on the main CLI as ``sequence-read``)."""

from __future__ import annotations

from functools import partial
from pathlib import Path

import typer
from typing_extensions import Annotated

from ai_gene_review.sequence_read import core, render, runner

sequence_read_app = typer.Typer(
    help="Optional sequence-only reads of a protein by a frontier language model."
)


@sequence_read_app.command("run")
def run_cmd(
    organism: Annotated[str, typer.Argument(help="Organism folder, e.g. human.")],
    gene: Annotated[str, typer.Argument(help="Gene folder, e.g. PTEN.")],
    model: Annotated[str, typer.Option(help="Model id.")] = core.DEFAULT_MODEL,
    effort: Annotated[str, typer.Option(help="Effort level.")] = core.DEFAULT_EFFORT,
    controls: Annotated[
        bool,
        typer.Option(help="Ask the shuffled and catalytic/decoy control questions."),
    ] = True,
    interpro: Annotated[
        bool, typer.Option(help="Fetch Pfam boundaries from the InterPro API.")
    ] = True,
    claude_bin: Annotated[
        str, typer.Option(help="The claude command-line tool to call.")
    ] = "claude",
    force: Annotated[
        bool, typer.Option(help="Replace an existing run for this model and effort.")
    ] = False,
    genes_root: Annotated[Path, typer.Option(help="Genes directory.")] = Path("genes"),
) -> None:
    """Ask the model the FEAT and PSEUDO questions about the gene's UniProt sequence.

    Each call is billed to the account the claude tool is signed in to (3 to 5
    calls per gene). Writes a run file and re-renders RESULTS.md.
    """
    gdir = runner.gene_dir(organism, gene, genes_root)
    up = gdir / f"{gene}-uniprot.txt"
    if not up.exists():
        raise typer.BadParameter(
            f"{up} not found; run `just fetch-gene {organism} {gene}` first"
        )
    out = runner.output_dir(organism, gene, genes_root)
    path = runner.run_path(out, model, effort)
    if path.exists() and not force:
        raise typer.BadParameter(f"{path} exists; pass --force to replace it")
    record = core.read_uniprot(up)
    pfam = core.fetch_pfam_locations(record.accession) if interpro else None
    caller = partial(core.call_model, claude_bin, model, effort)
    body = runner.run_read(record, caller, pfam, controls=controls)
    runner.write_run(
        organism,
        gene,
        record,
        body,
        model,
        effort,
        core.cli_version(claude_bin),
        path,
    )
    results = render.render(out, gene)
    n_bad = sum(1 for c in body["calls"] if not core.usable(c))
    typer.echo(
        f"{len(body['calls'])} calls ({n_bad} unusable). Wrote {path} and {results}"
    )


@sequence_read_app.command("render")
def render_cmd(
    organism: Annotated[str, typer.Argument(help="Organism folder.")],
    gene: Annotated[str, typer.Argument(help="Gene folder.")],
    genes_root: Annotated[Path, typer.Option(help="Genes directory.")] = Path("genes"),
) -> None:
    """Re-render RESULTS.md from the gene's existing run files (no model calls)."""
    path = render.render(runner.output_dir(organism, gene, genes_root), gene)
    typer.echo(f"Wrote {path}")
