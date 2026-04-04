"""Wrappers for DefenseFinder, PADLOC, and CasFinder."""

from __future__ import annotations

import csv
import shutil
import subprocess
from pathlib import Path

from ai_gene_review.prok_immunity_prediction.models import ExternalHit, PreparedProteome


def run_defense_finder(prepared: PreparedProteome, output_dir: Path) -> list[ExternalHit]:
    """Run DefenseFinder when available and parse hits."""
    executable = shutil.which("defense-finder")
    if executable is None:
        return []
    output_dir.mkdir(parents=True, exist_ok=True)
    command = [
        executable,
        "run",
        str(prepared.faa_path),
        "-o",
        str(output_dir),
    ]
    subprocess.run(command, check=True)
    return parse_defense_finder(output_dir)


def run_padloc(prepared: PreparedProteome, output_dir: Path) -> list[ExternalHit]:
    """Run PADLOC when available and parse hits."""
    executable = shutil.which("padloc")
    if executable is None or prepared.gff_path is None:
        return []
    output_dir.mkdir(parents=True, exist_ok=True)
    command = [
        executable,
        "--faa",
        str(prepared.faa_path),
        "--gff",
        str(prepared.gff_path),
        "--outdir",
        str(output_dir),
    ]
    subprocess.run(command, check=True)
    return parse_padloc(output_dir)


def run_casfinder(prepared: PreparedProteome, output_dir: Path) -> list[ExternalHit]:
    """Run CasFinder models via MacSyFinder when available and parse hits."""
    executable = shutil.which("macsyfinder")
    if executable is None:
        return []
    output_dir.mkdir(parents=True, exist_ok=True)
    command = [
        executable,
        "--db-type",
        "ordered_replicon",
        "--sequence-db",
        str(prepared.faa_path),
        "--models",
        "CasFinder",
        "all",
        "--out-dir",
        str(output_dir),
    ]
    subprocess.run(command, check=True)
    return parse_casfinder(output_dir)


def parse_defense_finder(output_dir: Path) -> list[ExternalHit]:
    """Parse DefenseFinder output tables."""
    systems_path = output_dir / "defense_finder_systems.tsv"
    genes_path = output_dir / "defense_finder_genes.tsv"
    hits: list[ExternalHit] = []
    if systems_path.exists():
        with systems_path.open("r", encoding="utf-8") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            for row in reader:
                proteins = split_protein_list(row.get("protein_in_syst", ""))
                system = row.get("type", "") or row.get("subtype", "")
                subtype = row.get("subtype") or None
                for protein_id in proteins:
                    hits.append(
                        ExternalHit(
                            database="DefenseFinder",
                            protein_id=protein_id,
                            system=system,
                            subtype=subtype,
                            raw_label=subtype or system,
                            details=row,
                        )
                    )
    if hits or not genes_path.exists():
        return hits

    with genes_path.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            protein_id = first_present(
                row,
                ("hit_id", "gene", "gene_name", "protein", "protein_id"),
            )
            if not protein_id:
                continue
            system = first_present(row, ("type", "subtype", "sys_id")) or "DefenseFinder_hit"
            hits.append(
                ExternalHit(
                    database="DefenseFinder",
                    protein_id=protein_id,
                    system=system,
                    subtype=row.get("subtype") or None,
                    raw_label=row.get("subtype") or system,
                    details=row,
                )
            )
    return hits


def parse_padloc(output_dir: Path) -> list[ExternalHit]:
    """Parse PADLOC output CSV."""
    candidate_paths = sorted(output_dir.glob("*_padloc.csv"))
    if not candidate_paths:
        return []
    hits: list[ExternalHit] = []
    for path in candidate_paths:
        with path.open("r", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                protein_id = first_present(row, ("target.name", "target_name", "protein_id"))
                system = first_present(row, ("system", "protein.name", "protein_name"))
                if not protein_id or not system:
                    continue
                hits.append(
                    ExternalHit(
                        database="PADLOC",
                        protein_id=protein_id,
                        system=system,
                        subtype=row.get("protein.name") or row.get("protein_name") or None,
                        raw_label=system,
                        details=row,
                    )
                )
    return hits


def parse_casfinder(output_dir: Path) -> list[ExternalHit]:
    """Parse CasFinder best-solution predictions."""
    path = output_dir / "best_solution.tsv"
    if not path.exists():
        return []
    hits: list[ExternalHit] = []
    with path.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            system = first_present(row, ("subtype", "type", "model_fqn", "system"))
            if not system:
                continue
            proteins = split_protein_list(first_present(row, ("proteins", "genes", "gene_names")) or "")
            if not proteins:
                protein_name = first_present(row, ("protein", "protein_id", "hit_id"))
                proteins = [protein_name] if protein_name else []
            for protein_id in proteins:
                hits.append(
                    ExternalHit(
                        database="CasFinder",
                        protein_id=protein_id,
                        system="CRISPR-Cas",
                        subtype=system,
                        raw_label=system,
                        details=row,
                    )
                )
    return hits


def gather_cross_reference_hits(
    prepared: PreparedProteome,
    output_dir: Path,
    defense_finder_dir: Path | None = None,
    padloc_dir: Path | None = None,
    casfinder_dir: Path | None = None,
    run_missing: bool = True,
) -> list[ExternalHit]:
    """Collect cross-reference hits from supplied directories or local runs."""
    hits: list[ExternalHit] = []

    if defense_finder_dir:
        hits.extend(parse_defense_finder(defense_finder_dir))
    elif run_missing:
        hits.extend(run_defense_finder(prepared, output_dir / "defensefinder"))

    if padloc_dir:
        hits.extend(parse_padloc(padloc_dir))
    elif run_missing:
        hits.extend(run_padloc(prepared, output_dir / "padloc"))

    if casfinder_dir:
        hits.extend(parse_casfinder(casfinder_dir))
    elif run_missing:
        hits.extend(run_casfinder(prepared, output_dir / "casfinder"))

    return hits


def split_protein_list(raw_value: str) -> list[str]:
    """Split common list encodings seen in tool outputs."""
    if not raw_value:
        return []
    cleaned = raw_value.replace("[", "").replace("]", "")
    tokens = [token.strip() for token in cleaned.replace(";", ",").split(",")]
    return [token for token in tokens if token]


def first_present(row: dict[str, str], keys: tuple[str, ...]) -> str | None:
    """Return the first non-empty key value from a dictionary."""
    for key in keys:
        value = row.get(key)
        if value:
            return value
    return None
