"""Typer sub-app for sequence-only reads (registered on the main CLI as ``sequence-read``)."""

from __future__ import annotations

from datetime import date
from functools import partial
from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated

from ai_gene_review.sequence_read import core, peptalk, render, runner

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
        runner.cli_route(core.cli_version(claude_bin)),
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


def _record(organism: str, gene: str, genes_root: Path) -> core.ProteinRecord:
    up = runner.gene_dir(organism, gene, genes_root) / f"{gene}-uniprot.txt"
    if not up.exists():
        raise typer.BadParameter(
            f"{up} not found; run `just fetch-gene {organism} {gene}` first"
        )
    return core.read_uniprot(up)


@sequence_read_app.command("residues")
def residues_cmd(
    organism: Annotated[str, typer.Argument(help="Organism folder.")],
    gene: Annotated[str, typer.Argument(help="Gene folder.")],
    specs: Annotated[
        list[str], typer.Argument(help="Positions (58) or claimed residues (D58).")
    ],
    note: Annotated[
        str, typer.Option(help="What the observation is, for the written block.")
    ] = "",
    write: Annotated[
        bool,
        typer.Option(
            help="Append the checked lines to sequence-read/residue-checks.md."
        ),
    ] = False,
    genes_root: Annotated[Path, typer.Option(help="Genes directory.")] = Path("genes"),
) -> None:
    """Check residues named while reading the sequence in a review (no model call).

    The in-agent mode: the reviewing agent reads the sequence alongside the
    literature and records; each residue it relies on is checked here, and with
    --write the lines go to a file the review can quote.
    """
    lines = core.residue_lines(_record(organism, gene, genes_root), specs)
    typer.echo("\n".join(lines))
    if write:
        path = runner.output_dir(organism, gene, genes_root) / "residue-checks.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        head = (
            ""
            if path.exists()
            else f"# {gene}: residues checked during an in-agent sequence read\n\n"
            "Each line is generated by `ai-gene-review sequence-read residues` from the "
            "UniProt record; the observation that prompted it is the reviewing agent's.\n"
        )
        block = (
            f"\n## {date.today().isoformat()}" + (f": {note}" if note else "") + "\n\n"
        )
        with path.open("a") as fh:
            fh.write(head + block + "\n".join(lines) + "\n")
        typer.echo(f"Appended to {path}")


@sequence_read_app.command("blind-fasta")
def blind_fasta_cmd(
    organism: Annotated[str, typer.Argument(help="Organism folder.")],
    gene: Annotated[str, typer.Argument(help="Gene folder.")],
    position: Annotated[
        Optional[int],
        typer.Option(
            help="Catalytic residue to substitute (default: UniProt ACT_SITE)."
        ),
    ] = None,
    kinase: Annotated[
        bool,
        typer.Option(help="Use the kinase substitutions (Asp to Asn, Lys to Met)."),
    ] = False,
    genes_root: Annotated[Path, typer.Option(help="Genes directory.")] = Path("genes"),
) -> None:
    """Write the FASTA files for the peptalk blind control (no model call)."""
    record = _record(organism, gene, genes_root)
    probe = peptalk.probe_for(record, position, kinase)
    out = runner.output_dir(organism, gene, genes_root)
    for p in peptalk.write_fastas(record, out, gene, probe):
        typer.echo(f"Wrote {p}")
    if probe is None:
        typer.echo("No UniProt ACT_SITE and no --position: wild type only, no probe.")


@sequence_read_app.command("import-peptalk")
def import_peptalk_cmd(
    organism: Annotated[str, typer.Argument(help="Organism folder.")],
    gene: Annotated[str, typer.Argument(help="Gene folder.")],
    files: Annotated[list[Path], typer.Argument(help="peptalk JSONL result files.")],
    position: Annotated[
        Optional[int], typer.Option(help="The --position given to blind-fasta, if any.")
    ] = None,
    kinase: Annotated[bool, typer.Option(help="As given to blind-fasta.")] = False,
    interpro: Annotated[
        bool, typer.Option(help="Fetch Pfam boundaries from the InterPro API.")
    ] = True,
    force: Annotated[bool, typer.Option(help="Replace an existing run.")] = False,
    genes_root: Annotated[Path, typer.Option(help="Genes directory.")] = Path("genes"),
) -> None:
    """Check peptalk blind-control answers and add them to RESULTS.md."""
    record = _record(organism, gene, genes_root)
    probe = peptalk.probe_for(record, position, kinase)
    pfam = core.fetch_pfam_locations(record.accession) if interpro else None
    body, model, effort, route = peptalk.import_records(
        record, peptalk.read_jsonl(files), pfam, probe
    )
    out = runner.output_dir(organism, gene, genes_root)
    path = out / f"{model}-{effort}-peptalk-blind.json"
    if path.exists() and not force:
        raise typer.BadParameter(f"{path} exists; pass --force to replace it")
    runner.write_run(organism, gene, record, body, model, effort, route, path)
    typer.echo(f"Wrote {path} and {render.render(out, gene)}")
