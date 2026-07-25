"""Typer sub-app for litscan jobs (registered on the main CLI as ``litscan``)."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated

from ai_gene_review.litscan import module_member

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
