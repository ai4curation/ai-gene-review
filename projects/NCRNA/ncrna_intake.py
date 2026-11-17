"""Rank one species' GO-annotated ncRNAs (RNAcentral ids) for review.

Every figure in projects/NCRNA.md about how many RNAcentral products carry which
evidence comes from this script.

PREDICATE (stated once, applied to every count):
  * universe: all QuickGO annotations with ``geneProductType=rna`` and the
    species' NCBI taxon id, downloaded per GO aspect (a single download for
    human stops short of the hit count)
  * a row is EXPERIMENTAL when its ECO id is in EXPERIMENTAL_ECO below (the
    manual experimental codes plus their high-throughput counterparts)
  * counts are of annotation ROWS; ``experimental_references`` counts distinct
    references behind the experimental rows
  * ``rna_type`` is RNAcentral's own classification (EBI Search ``rna_type``),
    fetched only for products with at least one experimental row; ids EBI Search
    does not return are looked up in the RNAcentral API, which reports whether
    the sequence is still active

Output is YAML, one record per product, most experimental references first.

Usage:
  uv run python projects/NCRNA/ncrna_intake.py human -o projects/NCRNA/intake/human.yaml
"""

from __future__ import annotations

import csv
import io
from collections import Counter, defaultdict
from pathlib import Path
from typing import Annotated

import requests
import typer
import yaml

from ai_gene_review.etl.gene import product_type_for_rna_type, resolve_taxon_term

QUICKGO_DOWNLOAD_URL = "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch"
QUICKGO_SEARCH_URL = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
EBI_SEARCH_ENTRY_URL = "https://www.ebi.ac.uk/ebisearch/ws/rest/rnacentral/entry/"
RNACENTRAL_API_URL = "https://rnacentral.org/api/v1/rna/"
ASPECTS = ("molecular_function", "biological_process", "cellular_component")
FIELDS = "geneProductId,symbol,qualifier,goId,goAspect,evidenceCode,reference,assignedBy,name"

EXPERIMENTAL_ECO = {
    "ECO:0000269": "EXP",
    "ECO:0000314": "IDA",
    "ECO:0000315": "IMP",
    "ECO:0000316": "IGI",
    "ECO:0000353": "IPI",
    "ECO:0000270": "IEP",
    "ECO:0006056": "HTP",
    "ECO:0007005": "HDA",
    "ECO:0007001": "HMP",
    "ECO:0007003": "HGI",
    "ECO:0007007": "HEP",
}

app = typer.Typer(add_completion=False)


def download_rows(taxon_id: str) -> list[dict[str, str]]:
    """Download every RNA annotation for a taxon, one GO aspect at a time.

    Raises if the rows received do not match QuickGO's hit count for the aspect.
    """
    rows: list[dict[str, str]] = []
    for aspect in ASPECTS:
        params = {"geneProductType": "rna", "taxonId": taxon_id, "aspect": aspect}
        hits = requests.get(
            QUICKGO_SEARCH_URL,
            params={**params, "limit": "1"},
            headers={"Accept": "application/json"},
            timeout=60,
        ).json()["numberOfHits"]
        response = requests.get(
            QUICKGO_DOWNLOAD_URL,
            params={**params, "downloadLimit": str(hits + 1), "selectedFields": FIELDS},
            headers={"Accept": "text/tsv"},
            timeout=900,
        )
        response.raise_for_status()
        aspect_rows = list(csv.DictReader(io.StringIO(response.text), delimiter="\t"))
        if len(aspect_rows) != hits:
            raise ValueError(f"{aspect}: received {len(aspect_rows)} rows, QuickGO reports {hits}")
        rows.extend(aspect_rows)
    return rows


def summarise(rows: list[dict[str, str]]) -> dict[str, dict]:
    """Aggregate annotation rows per gene product.

    >>> rows = [
    ...     {"GENE PRODUCT ID": "URS1_9606", "GENE_PRODUCT_NAME": "x", "ECO ID": "ECO:0000314",
    ...      "REFERENCE": "PMID:1", "ASSIGNED BY": "BHF-UCL"},
    ...     {"GENE PRODUCT ID": "URS1_9606", "GENE_PRODUCT_NAME": "x", "ECO ID": "ECO:0000256",
    ...      "REFERENCE": "GO_REF:0000115", "ASSIGNED BY": "RNAcentral"},
    ... ]
    >>> s = summarise(rows)["URS1_9606"]
    >>> (s["rows"], s["experimental_rows"], s["experimental_references"])
    (2, 1, 1)
    """
    products: dict[str, dict] = defaultdict(
        lambda: {"rows": 0, "experimental_rows": 0, "refs": set(), "assigned_by": Counter(), "name": ""}
    )
    for row in rows:
        product = products[row["GENE PRODUCT ID"]]
        product["name"] = row["GENE_PRODUCT_NAME"]
        product["rows"] += 1
        if row["ECO ID"] in EXPERIMENTAL_ECO:
            product["experimental_rows"] += 1
            product["refs"].add(row["REFERENCE"])
            product["assigned_by"][row["ASSIGNED BY"]] += 1
    return {
        pid: {
            "description": p["name"],
            "rows": p["rows"],
            "experimental_rows": p["experimental_rows"],
            "experimental_references": len(p["refs"]),
            "experimental_assigned_by": dict(p["assigned_by"].most_common()),
        }
        for pid, p in products.items()
    }


def fetch_rna_types(ids: list[str]) -> dict[str, dict]:
    """Look up RNAcentral ``rna_type`` and gene names, 100 ids per request."""
    out: dict[str, dict] = {}
    for start in range(0, len(ids), 100):
        batch = ids[start : start + 100]
        response = requests.get(
            EBI_SEARCH_ENTRY_URL + ",".join(batch),
            params={"fields": "rna_type,gene", "format": "json"},
            timeout=120,
        )
        response.raise_for_status()
        for entry in response.json()["entries"]:
            fields = entry["fields"]
            out[entry["id"]] = {"rna_type": fields["rna_type"][0], "genes": fields["gene"], "rnacentral_active": True}
    # EBI Search indexes only active sequences. GOA can still annotate a retired
    # one, so look those up in the RNAcentral API and record that they are retired.
    for pid in ids:
        if pid not in out:
            record = requests.get(RNACENTRAL_API_URL + pid.split("_")[0], timeout=60).json()
            out[pid] = {"rna_type": record["rna_type"], "genes": [], "rnacentral_active": record["is_active"]}
    return out


def reviewed_ids(genes_dir: Path) -> dict[str, str]:
    """Map RNAcentral ids already used as a review ``id`` to their review file."""
    found = {}
    for path in genes_dir.glob("*/*/*-ai-review.yaml"):
        with path.open() as handle:
            first = handle.readline()
        if first.startswith("id: URS"):
            found[first.split(":", 1)[1].strip()] = str(path)
    return found


@app.command()
def main(
    organism: Annotated[str, typer.Argument(help="Organism, e.g. human, mouse, rat")],
    output: Annotated[Path, typer.Option("--output", "-o", help="YAML file to write")],
    genes_dir: Annotated[Path, typer.Option(help="Gene review tree")] = Path("genes"),
) -> None:
    taxon_id = resolve_taxon_term(organism)["id"].removeprefix("NCBITaxon:")
    products = summarise(download_rows(taxon_id))
    experimental = sorted(
        (pid for pid, p in products.items() if p["experimental_rows"]),
        key=lambda pid: (-products[pid]["experimental_references"], -products[pid]["experimental_rows"], pid),
    )
    types = fetch_rna_types(experimental)
    reviewed = reviewed_ids(genes_dir)
    records = []
    for pid in experimental:
        rna_type = types[pid]["rna_type"]
        records.append(
            {
                "id": pid,
                **products[pid],
                "rna_type": rna_type,
                "product_type": product_type_for_rna_type(rna_type),
                "genes": types[pid]["genes"][:8],
                "rnacentral_active": types[pid]["rnacentral_active"],
                "reviewed_in": reviewed.get(pid),
            }
        )
    by_type = Counter(r["product_type"] for r in records)
    summary = {
        "organism": organism,
        "taxon": f"NCBITaxon:{taxon_id}",
        "products_with_any_rows": len(products),
        "products_with_experimental_rows": len(records),
        "experimental_products_by_product_type": dict(by_type.most_common()),
        "experimental_products_on_retired_rnacentral_ids": sum(not r["rnacentral_active"] for r in records),
        "products": records,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(yaml.safe_dump(summary, sort_keys=False, allow_unicode=True))
    typer.echo(f"{organism}: {len(records)} of {len(products)} RNA products have experimental rows -> {output}")


if __name__ == "__main__":
    app()
