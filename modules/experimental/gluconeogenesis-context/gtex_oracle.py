#!/usr/bin/env python
"""GTEx v8 expression oracle: median TPM per tissue for a set of gene symbols.

For each gene symbol this resolves the versioned GENCODE id via the GTEx
``reference/gene`` endpoint, then fetches per-tissue median expression from
``expression/medianGeneExpression`` (dataset ``gtex_v8``). The assembled
gene x tissue matrix is cached to a TSV so downstream resolution is reproducible
and offline.

This is a real API client (GTEx is a public, programmatic resource); it does not
fabricate values and does not merely point at a website.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

import requests

API = "https://gtexportal.org/api/v2"
DATASET = "gtex_v8"
CACHE = Path(__file__).parent / "cache" / "gtex_medians.tsv"

# GTEx v8 is built on GENCODE v26, which predates some HGNC symbol updates.
# Map current symbols to the symbol/alias GTEx indexes them under.
ALIASES = {"G6PC1": "G6PC"}


def resolve_gencode_id(symbol: str) -> str | None:
    """Resolve a gene symbol to its versioned GENCODE id in GTEx (alias-aware)."""
    for query in [symbol, ALIASES.get(symbol)]:
        if not query:
            continue
        r = requests.get(f"{API}/reference/gene", params={"geneId": query}, timeout=30)
        r.raise_for_status()
        rows = r.json().get("data", [])
        for row in rows:
            if row.get("geneSymbol", "").upper() in {symbol.upper(), query.upper()}:
                return row.get("gencodeId")
        if rows:
            return rows[0].get("gencodeId")
    return None


def median_expression(gencode_id: str) -> dict[str, float]:
    """Return {tissueSiteDetailId: median TPM} for a GENCODE id."""
    r = requests.get(
        f"{API}/expression/medianGeneExpression",
        params={"datasetId": DATASET, "gencodeId": gencode_id, "format": "json"},
        timeout=30,
    )
    r.raise_for_status()
    return {row["tissueSiteDetailId"]: float(row["median"]) for row in r.json().get("data", [])}


def build_matrix(symbols: list[str]) -> tuple[list[str], dict[str, dict[str, float]]]:
    """Fetch a gene x tissue median-TPM matrix for the given symbols."""
    matrix: dict[str, dict[str, float]] = {}
    tissues: set[str] = set()
    for sym in symbols:
        gid = resolve_gencode_id(sym)
        if not gid:
            print(f"  WARN: no GENCODE id for {sym}", file=sys.stderr)
            matrix[sym] = {}
            continue
        expr = median_expression(gid)
        matrix[sym] = expr
        tissues.update(expr)
        print(f"  {sym} ({gid}): {len(expr)} tissues", file=sys.stderr)
        time.sleep(0.2)
    return sorted(tissues), matrix


def write_cache(tissues: list[str], matrix: dict[str, dict[str, float]], path: Path = CACHE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as fh:
        fh.write("gene\t" + "\t".join(tissues) + "\n")
        for gene, expr in matrix.items():
            fh.write(gene + "\t" + "\t".join(f"{expr.get(t, ''):}" for t in tissues) + "\n")


def load_cache(path: Path = CACHE) -> tuple[list[str], dict[str, dict[str, float]]]:
    lines = path.read_text().splitlines()
    tissues = lines[0].split("\t")[1:]
    matrix: dict[str, dict[str, float]] = {}
    for line in lines[1:]:
        cells = line.split("\t")
        gene = cells[0]
        matrix[gene] = {t: float(v) for t, v in zip(tissues, cells[1:]) if v != ""}
    return tissues, matrix


def get_matrix(symbols: list[str], refresh: bool = False) -> tuple[list[str], dict[str, dict[str, float]]]:
    """Return the cached matrix, fetching from GTEx if missing or ``refresh``."""
    if CACHE.exists() and not refresh:
        return load_cache()
    tissues, matrix = build_matrix(symbols)
    write_cache(tissues, matrix)
    return tissues, matrix


if __name__ == "__main__":
    syms = sys.argv[1:] or ["PC", "PCK1", "PCK2", "FBP1", "FBP2", "G6PC1", "G6PC2", "G6PC3", "SLC37A4"]
    tissues, matrix = get_matrix(syms, refresh=True)
    print(f"cached {len(matrix)} genes x {len(tissues)} tissues -> {CACHE}")
