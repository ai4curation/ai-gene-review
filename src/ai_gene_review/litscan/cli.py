"""Typer sub-app for litscan jobs (registered on the main CLI as ``litscan``)."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated

from ai_gene_review.litscan import gene_gap, module_member

litscan_app = typer.Typer(help="Literature-scan jobs for genes and modules.")


@litscan_app.command("module-member")
def module_member_cmd(
    days: Annotated[
        int,
        typer.Option(
            help="Look back this many days (ignored if a date range is given)."
        ),
    ] = 90,
    date_from: Annotated[str, typer.Option(help="Start date YYYY-MM-DD.")] = "",
    date_to: Annotated[str, typer.Option(help="End date YYYY-MM-DD.")] = "",
    max_records: Annotated[
        int, typer.Option(help="Max papers fetched per module.")
    ] = 40,
    max_terms: Annotated[
        int, typer.Option(help="Max distinctive query terms per module.")
    ] = 10,
    modules_dir: Annotated[Path, typer.Option(help="Modules directory.")] = Path(
        "modules"
    ),
    output_dir: Annotated[
        Optional[Path], typer.Option(help="Packet output directory.")
    ] = None,
) -> None:
    """Scan recent literature for candidate new members of curated modules."""
    out = output_dir or Path("reports/litscan/module-member")
    packet = module_member.run(
        modules_dir,
        days=days,
        date_from=date_from,
        date_to=date_to,
        max_records=max_records,
        max_terms=max_terms,
    )
    json_path, md_path = module_member.write_packet(packet, out)
    typer.echo(
        f"Scanned {packet['module_count']} modules "
        f"({packet['date_from']}..{packet['date_to']}); "
        f"{packet['total_records']} candidate papers.\n"
        f"Wrote {md_path} and {json_path}"
    )


@litscan_app.command("gene-gap")
def gene_gap_cmd(
    days: Annotated[
        int,
        typer.Option(
            help="Look back this many days (ignored if a date range is given)."
        ),
    ] = 7,
    date_from: Annotated[str, typer.Option(help="Start date YYYY-MM-DD.")] = "",
    date_to: Annotated[str, typer.Option(help="End date YYYY-MM-DD.")] = "",
    config: Annotated[
        Path, typer.Option(help="GeneGapScanConfig YAML.")
    ] = gene_gap.DEFAULT_CONFIG,
    ledger: Annotated[
        Optional[Path],
        typer.Option(
            help="JSON list of existing issues ({number, title, state, body}); "
            "papers they name are not proposed again."
        ),
    ] = None,
    include_preprints: Annotated[
        bool, typer.Option(help="Also scan Europe PMC preprints (SRC:PPR).")
    ] = False,
    max_issues: Annotated[
        Optional[int], typer.Option(help="Lower the configured issue cap.")
    ] = None,
    genes_dir: Annotated[Path, typer.Option(help="Gene review directory.")] = Path(
        "genes"
    ),
    output_dir: Annotated[
        Path, typer.Option(help="Packet output directory.")
    ] = gene_gap.DEFAULT_OUTPUT,
) -> None:
    """Rank recent papers by the function-knowledge gap they could close.

    Writes a JSON + markdown packet and ready-to-file issue bodies; never writes
    to GitHub, so every run is a dry run until the workflow publishes the selected
    issue bodies.
    """
    if bool(date_from) != bool(date_to):
        raise typer.BadParameter("--date-from and --date-to go together")
    start, end = (
        (date_from, date_to) if date_from else gene_gap.default_date_range(days)
    )
    if days < 1 or (max_issues is not None and max_issues < 0):
        raise typer.BadParameter("days must be positive and max-issues nonnegative")
    try:
        if dt.date.fromisoformat(start) > dt.date.fromisoformat(end):
            raise typer.BadParameter("date-from must be on or before date-to")
    except ValueError as exc:
        raise typer.BadParameter("use ISO dates (YYYY-MM-DD)") from exc
    cfg = gene_gap.load_config(config)
    if max_issues is not None:
        cfg["limits"]["max_issues"] = min(max_issues, cfg["limits"]["max_issues"])
    issues = json.loads(ledger.read_text()) if ledger else []
    packet = gene_gap.run(
        cfg,
        date_from=start,
        date_to=end,
        genes_dir=genes_dir,
        ledger=issues,
        include_preprints=include_preprints,
        config_path=str(config),
        log=lambda msg: typer.echo(msg, err=True),
    )
    json_path, md_path = gene_gap.write_packet(packet, output_dir)
    eligible = sum(1 for c in packet["candidates"] if c.get("issue_eligible"))
    typer.echo(
        f"{start}..{end}: {packet['paper_count']} papers, "
        f"{len(packet['candidates'])} ranked candidates, {eligible} issue bodies.\n"
        f"Wrote {md_path} and {json_path}"
    )


@litscan_app.command("rescore-gene-gap")
def rescore_gene_gap_cmd(
    packet: Annotated[Path, typer.Argument(help="GeneGapPacket JSON to rescore.")],
    output_dir: Annotated[
        Path,
        typer.Option(
            help="Directory for the rescored packet; must not hold the input packet."
        ),
    ],
    config: Annotated[
        Path, typer.Option(help="GeneGapScanConfig YAML.")
    ] = gene_gap.DEFAULT_CONFIG,
) -> None:
    """Re-apply the scoring config to an existing packet, offline.

    Use it to calibrate weights: every candidate keeps its earlier rank as
    previous_rank. Only the packet's own candidates are re-ranked.
    """
    data = json.loads(packet.read_text())
    target = output_dir / f"{data['date_to']}-{gene_gap.JOB}.json"
    if (
        target.resolve() == packet.resolve()
        or output_dir.resolve() == packet.parent.resolve()
    ):
        raise typer.BadParameter(
            "--output-dir must differ from the input packet's directory: writing "
            "there would replace the packet and the issue bodies that were filed"
        )
    problem = gene_gap.rescore_problem(data)
    if problem:
        raise typer.BadParameter(problem)
    rescored = gene_gap.rescore_packet(data, gene_gap.load_config(config))
    rescored["config_path"] = str(config)
    json_path, md_path = gene_gap.write_packet(rescored, output_dir)
    for cand in rescored["candidates"]:
        typer.echo(
            f"{cand['previous_rank']:>3} -> {cand['rank']:>3}  {cand['score']:>3}  "
            f"{cand['gene']['symbol']}  {cand['paper']['reference_id']}"
        )
    typer.echo(f"Wrote {md_path} and {json_path}")


@litscan_app.command("validate-gene-gap")
def validate_gene_gap_cmd(
    paths: Annotated[
        list[Path], typer.Argument(help="Config YAML or packet JSON files.")
    ],
) -> None:
    """Validate gene-gap configs (GeneGapScanConfig) and packets (GeneGapPacket)."""
    problems = gene_gap.validate_files(paths)
    for problem in problems:
        typer.echo(problem, err=True)
    typer.echo(f"Checked {len(paths)} files; {len(problems)} problems.")
    if problems:
        raise typer.Exit(1)
