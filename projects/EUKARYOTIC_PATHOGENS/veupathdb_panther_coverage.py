#!/usr/bin/env python
"""Summarize PANTHER and GOA IBA coverage for VEuPathDB reference genomes."""

from __future__ import annotations

import csv
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from dataclasses import dataclass
from email.message import Message
from pathlib import Path
from typing import Iterable


VEUPATHDB_ORGANISM_URL = (
    "https://veupathdb.org/veupathdb/service/record-types/organism/"
    "searches/GenomeDataTypes/reports/standard"
)
UNIPROT_SEARCH_URL = "https://rest.uniprot.org/uniprotkb/search"
QUICKGO_SEARCH_URL = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

QUICKGO_PAGE_LIMIT = 200
UNIPROT_PAGE_SIZE = 500

IBA_EVIDENCE = ["ECO:0000318"]
EXPERIMENTAL_EVIDENCE = [
    "ECO:0000269",  # EXP
    "ECO:0000314",  # IDA
    "ECO:0000353",  # IPI
    "ECO:0000315",  # IMP
    "ECO:0000316",  # IGI
    "ECO:0000270",  # IEP
    "ECO:0006056",  # HTP
    "ECO:0007005",  # HDA
    "ECO:0007001",  # HMP
    "ECO:0007003",  # HGI
    "ECO:0007007",  # HEP
]


@dataclass(frozen=True)
class OrganismSpec:
    site: str
    clade: str
    primary_key: str
    uniprot_taxon_id: int
    repo_mnemonics: tuple[str, ...] = ()
    note: str = ""


ORGANISMS: tuple[OrganismSpec, ...] = (
    OrganismSpec("PlasmoDB", "malaria", "Plasmodium falciparum 3D7", 36329, ("PLAF7",)),
    OrganismSpec("PlasmoDB", "malaria", "Plasmodium vivax Sal-1", 126793),
    OrganismSpec("PlasmoDB", "malaria", "Plasmodium berghei ANKA", 5823),
    OrganismSpec(
        "ToxoDB",
        "coccidian apicomplexans",
        "Toxoplasma gondii ME49",
        508771,
        ("TOXGM", "TOXGO"),
        "Includes existing species-level TOXGO reviews.",
    ),
    OrganismSpec(
        "CryptoDB", "cryptosporidia", "Cryptosporidium parvum Iowa II", 353152
    ),
    OrganismSpec(
        "TriTrypDB",
        "kinetoplastids",
        "Trypanosoma brucei brucei TREU927",
        185431,
        ("TRYB2", "TRYBB"),
        "Includes existing species-level TRYBB reviews.",
    ),
    OrganismSpec(
        "TriTrypDB",
        "kinetoplastids",
        "Trypanosoma cruzi Dm28c 2014",
        5693,
        ("TRYCR",),
        "VEuPathDB strain row paired with the species-level UniProt taxon.",
    ),
    OrganismSpec(
        "TriTrypDB",
        "kinetoplastids",
        "Leishmania major strain Friedlin",
        5664,
        ("LEIMA",),
        "VEuPathDB strain row paired with the species-level UniProt taxon.",
    ),
    OrganismSpec(
        "TriTrypDB",
        "kinetoplastids",
        "Leishmania donovani BPK282A1",
        5661,
        (),
        "VEuPathDB strain row paired with the species-level UniProt taxon.",
    ),
    OrganismSpec("GiardiaDB", "diplomonads", "Giardia Assemblage A isolate WB", 184922),
    OrganismSpec("AmoebaDB", "amoebozoa", "Entamoeba histolytica HM-1:IMSS", 294381),
    OrganismSpec(
        "TrichDB", "parabasalids", "Trichomonas vaginalis G3", 412133, ("TRIVA",)
    ),
    OrganismSpec(
        "PiroplasmaDB",
        "piroplasms",
        "Babesia bovis T2Bo",
        5865,
        (),
        "VEuPathDB strain row paired with the species-level UniProt taxon.",
    ),
    OrganismSpec("PiroplasmaDB", "piroplasms", "Babesia microti strain RI", 1133968),
    OrganismSpec(
        "PiroplasmaDB",
        "piroplasms",
        "Theileria annulata strain Ankara",
        5874,
        (),
        "VEuPathDB strain row paired with the species-level UniProt taxon.",
    ),
    OrganismSpec(
        "PiroplasmaDB",
        "piroplasms",
        "Theileria parva strain Muguga",
        5875,
        (),
        "VEuPathDB strain row paired with the species-level UniProt taxon.",
    ),
    OrganismSpec(
        "MicrosporidiaDB", "microsporidia", "Encephalitozoon cuniculi GB-M1", 284813
    ),
    OrganismSpec(
        "MicrosporidiaDB",
        "microsporidia",
        "Encephalitozoon intestinalis ATCC 50506",
        876142,
    ),
    OrganismSpec(
        "MicrosporidiaDB",
        "microsporidia",
        "Enterocytozoon bieneusi H348",
        481877,
        (),
        "Exact strain taxon has only a small UniProtKB accession set; "
        "coverage is not genome-wide.",
    ),
    OrganismSpec(
        "MicrosporidiaDB", "microsporidia", "Nematocida parisii ERTm3", 935791
    ),
    OrganismSpec("FungiDB", "fungi", "Aspergillus fumigatus Af293", 330879, ("ASPFU",)),
    OrganismSpec("FungiDB", "fungi", "Candida albicans SC5314", 237561, ("CANAL",)),
    OrganismSpec(
        "FungiDB",
        "fungi",
        "Nakaseomyces glabratus CBS 138",
        284593,
        ("CANGA",),
        "Current name of Candida glabrata.",
    ),
    OrganismSpec("FungiDB", "fungi", "Cryptococcus neoformans H99", 235443),
    OrganismSpec("FungiDB", "fungi", "Cryptococcus deneoformans JEC21", 214684),
    OrganismSpec(
        "VectorBase",
        "vectors",
        "Anopheles gambiae PEST",
        7165,
        ("ANOGA",),
        "VEuPathDB PEST row paired with the species-level UniProt taxon.",
    ),
    OrganismSpec("VectorBase", "vectors", "Aedes aegypti LVP_AGWG", 7159, ("AEDAE",)),
    OrganismSpec("VectorBase", "vectors", "Ixodes scapularis Wikel", 6945),
)


def get_json(
    url: str, params: dict[str, str | int] | None = None
) -> tuple[dict, Message]:
    if params:
        url += "?" + urllib.parse.urlencode(params, doseq=False)
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "Connection": "close",
            "User-Agent": "aigr-eukaryotic-pathogen-coverage/0.1",
        },
    )
    return read_json(request)


def read_json(request: urllib.request.Request) -> tuple[dict, Message]:
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                return json.loads(response.read().decode()), response.headers
        except (TimeoutError, urllib.error.URLError) as error:
            last_error = error
            time.sleep(1 + attempt * 2)
    assert last_error is not None
    raise last_error


def get_tsv(
    url: str, params: dict[str, str | int]
) -> tuple[list[dict[str, str]], Message]:
    request_url = url + "?" + urllib.parse.urlencode(params, doseq=False)
    request = urllib.request.Request(
        request_url,
        headers={
            "Accept": "text/tab-separated-values",
            "Connection": "close",
            "User-Agent": "aigr-eukaryotic-pathogen-coverage/0.1",
        },
    )
    return read_tsv(request)


def read_tsv(request: urllib.request.Request) -> tuple[list[dict[str, str]], Message]:
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                text = response.read().decode()
                rows = list(csv.DictReader(text.splitlines(), delimiter="\t"))
                return rows, response.headers
        except (TimeoutError, urllib.error.URLError) as error:
            last_error = error
            time.sleep(1 + attempt * 2)
    assert last_error is not None
    raise last_error


def next_link(headers: Message) -> str | None:
    link = headers.get("Link")
    if not link:
        return None
    match = re.search(r"<([^>]+)>;\s*rel=\"next\"", link)
    return match.group(1) if match else None


def load_veupathdb() -> tuple[dict[str, dict], dict[str, str]]:
    attrs = [
        "primary_key",
        "species",
        "project_id",
        "genecount",
        "ncbi_tax_id",
        "URLproteinFasta",
    ]
    data, _ = get_json(
        VEUPATHDB_ORGANISM_URL,
        {
            "reportConfig": json.dumps(
                {"attributes": attrs, "tables": [], "attributeFormat": "text"},
                separators=(",", ":"),
            )
        },
    )
    by_key: dict[str, dict] = {}
    releases: dict[str, str] = {}
    for record in data["records"]:
        row = dict(record["attributes"])
        by_key[row["primary_key"]] = row
        match = re.search(r"-(\d+)_", row.get("URLproteinFasta") or "")
        if match:
            releases[row["project_id"]] = match.group(1)
    return by_key, releases


def count_repo_reviews(root: Path) -> Counter[str]:
    counts: Counter[str] = Counter()
    for path in (root / "genes").glob("*/*/*-ai-review.yaml"):
        counts[path.parts[-3]] += 1
    return counts


def uniprot_rows(taxon_id: int) -> tuple[list[dict[str, str]], dict[str, str]]:
    params = {
        "query": f"organism_id:{taxon_id}",
        "fields": "accession,id,reviewed,gene_primary,protein_name,xref_panther",
        "format": "tsv",
        "size": UNIPROT_PAGE_SIZE,
    }
    url: str | None = UNIPROT_SEARCH_URL
    rows: list[dict[str, str]] = []
    releases: dict[str, str] = {}
    while url:
        if url == UNIPROT_SEARCH_URL:
            batch, headers = get_tsv(url, params)
        else:
            request = urllib.request.Request(
                url,
                headers={
                    "Accept": "text/tab-separated-values",
                    "Connection": "close",
                    "User-Agent": "aigr-eukaryotic-pathogen-coverage/0.1",
                },
            )
            batch, headers = read_tsv(request)
        rows.extend(batch)
        releases = {
            "uniprot_release": headers.get("X-UniProt-Release", ""),
            "uniprot_release_date": headers.get("X-UniProt-Release-Date", ""),
        }
        url = next_link(headers)
    return rows, releases


def quickgo_accessions(
    taxon_id: int, evidence: Iterable[str]
) -> tuple[set[str], set[str]]:
    accessions: set[str] = set()
    ptns: set[str] = set()
    page = 1
    total = 0
    while True:
        data, _ = get_json(
            QUICKGO_SEARCH_URL,
            {
                "taxonId": taxon_id,
                "evidenceCode": ",".join(evidence),
                "limit": QUICKGO_PAGE_LIMIT,
                "page": page,
            },
        )
        results = data.get("results") or []
        total = int(data.get("numberOfHits") or total)
        for result in results:
            gene_product_id = result.get("geneProductId") or ""
            if gene_product_id.startswith("UniProtKB:"):
                accessions.add(gene_product_id.split(":", 1)[1])
            for group in result.get("withFrom") or []:
                for xref in group.get("connectedXrefs") or []:
                    if xref.get("db") == "PANTHER" and str(
                        xref.get("id", "")
                    ).startswith("PTN"):
                        ptns.add(str(xref["id"]))
        if page * QUICKGO_PAGE_LIMIT >= total or not results:
            break
        page += 1
        time.sleep(0.05)
    return accessions, ptns


def mnemonic(rows: list[dict[str, str]]) -> str:
    suffixes: Counter[str] = Counter()
    for row in rows:
        entry = row.get("Entry Name") or ""
        if "_" in entry:
            suffixes[entry.rsplit("_", 1)[1]] += 1
    return suffixes.most_common(1)[0][0] if suffixes else ""


def pct(numerator: int, denominator: int) -> str:
    if not denominator:
        return "0.0"
    return f"{100 * numerator / denominator:.1f}"


def panther_accessions(rows: list[dict[str, str]]) -> set[str]:
    return {row["Entry"] for row in rows if row.get("PANTHER")}


def write_tsv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        path.write_text("")
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_report(
    path: Path, rows: list[dict[str, object]], releases: dict[str, str]
) -> None:
    by_site: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        by_site.setdefault(str(row["site"]), []).append(row)

    lines = [
        "# Eukaryotic pathogen PANTHER/IBA coverage",
        "",
        "Generated by `uv run python projects/EUKARYOTIC_PATHOGENS/veupathdb_panther_coverage.py`.",
        "",
        "## Data sources",
        "",
        f"- VEuPathDB organism search, Release {releases.get('veupathdb_release', 'unknown')}.",
        f"- UniProtKB REST, Release {releases.get('uniprot_release', 'unknown')} "
        f"({releases.get('uniprot_release_date', 'unknown')}).",
        "- QuickGO annotation search for IBA and experimental GO annotation counts.",
        "",
        "## Coverage by site",
        "",
    ]
    for site in sorted(by_site):
        site_rows = by_site[site]
        lines.extend(
            [
                f"### {site}",
                "",
                "| Organism | Mnemonic | VEuPath genes | UniProt proteins | PANTHER | IBA | Experimental GO | Swiss-Prot | AIGR reviews |",
                "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in site_rows:
            lines.append(
                f"| {row['organism']} | `{row['uniprot_mnemonic']}` | "
                f"{row['veupathdb_gene_count']} | {row['uniprot_proteins']} | "
                f"{row['panther_family_proteins']} ({row['panther_family_pct']}%) | "
                f"{row['iba_proteins']} ({row['iba_pct']}%) | "
                f"{row['experimental_go_proteins']} | {row['reviewed_uniprot_entries']} | "
                f"{row['aigr_reviews']} |"
            )
        notes = [row for row in site_rows if row.get("note")]
        if notes:
            lines.extend(["", "**Taxon notes.**"])
            for row in notes:
                lines.append(f"- {row['organism']}: {row['note']}")
        lowest_panther = min(site_rows, key=lambda r: float(r["panther_family_pct"]))
        lowest_iba = min(site_rows, key=lambda r: float(r["iba_pct"]))
        most_exp_gap = max(site_rows, key=lambda r: int(r["experimental_without_iba"]))
        lines.extend(
            [
                "",
                "**Notable gaps.** "
                f"Lowest PANTHER coverage: {lowest_panther['organism']} "
                f"({lowest_panther['panther_family_pct']}%). "
                f"Lowest IBA coverage: {lowest_iba['organism']} "
                f"({lowest_iba['iba_pct']}%). "
                f"Largest experimental/no-IBA set: {most_exp_gap['organism']} "
                f"({most_exp_gap['experimental_without_iba']} proteins).",
                "",
            ]
        )
    path.write_text("\n".join(lines).rstrip() + "\n")


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    out_dir = Path(__file__).resolve().parent
    veupath_rows, veupath_releases = load_veupathdb()
    repo_counts = count_repo_reviews(root)
    release_info = {
        "veupathdb_release": ",".join(sorted(set(veupath_releases.values()))),
        "uniprot_release": "",
        "uniprot_release_date": "",
    }
    coverage_rows: list[dict[str, object]] = []
    candidate_rows: list[dict[str, object]] = []

    for spec in ORGANISMS:
        print(f"{spec.site}: {spec.primary_key} UniProt", file=sys.stderr, flush=True)
        veupath = veupath_rows.get(spec.primary_key)
        if not veupath:
            raise SystemExit(
                f"{spec.primary_key!r} is not in VEuPathDB organism results"
            )
        uniprot, uniprot_release = uniprot_rows(spec.uniprot_taxon_id)
        release_info.update({k: v for k, v in uniprot_release.items() if v})
        panther = panther_accessions(uniprot)
        print(
            f"{spec.site}: {spec.primary_key} QuickGO IBA", file=sys.stderr, flush=True
        )
        iba, ptns = quickgo_accessions(spec.uniprot_taxon_id, IBA_EVIDENCE)
        print(
            f"{spec.site}: {spec.primary_key} QuickGO experimental",
            file=sys.stderr,
            flush=True,
        )
        experimental, _ = quickgo_accessions(
            spec.uniprot_taxon_id, EXPERIMENTAL_EVIDENCE
        )
        reviewed = {
            row["Entry"] for row in uniprot if row.get("Reviewed") == "reviewed"
        }
        aigr_reviews = sum(repo_counts[m] for m in spec.repo_mnemonics)

        proteome_count = len(uniprot)
        coverage_rows.append(
            {
                "site": spec.site,
                "clade": spec.clade,
                "organism": spec.primary_key,
                "veupathdb_project": veupath["project_id"],
                "veupathdb_gene_count": veupath.get("genecount") or "",
                "uniprot_taxon_id": spec.uniprot_taxon_id,
                "uniprot_mnemonic": mnemonic(uniprot),
                "uniprot_proteins": proteome_count,
                "panther_family_proteins": len(panther),
                "panther_family_pct": pct(len(panther), proteome_count),
                "iba_proteins": len(iba),
                "iba_pct": pct(len(iba), proteome_count),
                "experimental_go_proteins": len(experimental),
                "experimental_without_iba": len(experimental - iba),
                "reviewed_uniprot_entries": len(reviewed),
                "reviewed_without_iba": len(reviewed - iba),
                "ptn_nodes": len(ptns),
                "aigr_reviews": aigr_reviews,
                "repo_mnemonics": ",".join(spec.repo_mnemonics),
                "note": spec.note,
            }
        )

        by_accession = {row["Entry"]: row for row in uniprot}
        flagged = (reviewed | experimental) - iba
        candidate_order = sorted(
            flagged,
            key=lambda accession: (
                accession not in reviewed,
                accession not in experimental,
                accession in panther,
                accession,
            ),
        )
        for accession in candidate_order[:50]:
            row = by_accession.get(accession, {})
            candidate_rows.append(
                {
                    "site": spec.site,
                    "organism": spec.primary_key,
                    "uniprot_mnemonic": mnemonic(uniprot),
                    "accession": accession,
                    "entry_name": row.get("Entry Name", ""),
                    "gene": row.get("Gene Names (primary)", ""),
                    "protein_name": row.get("Protein names", ""),
                    "reviewed": "yes" if accession in reviewed else "no",
                    "experimental_go": "yes" if accession in experimental else "no",
                    "has_panther_family": "yes" if accession in panther else "no",
                    "has_iba": "yes" if accession in iba else "no",
                }
            )
        time.sleep(0.1)

    write_tsv(out_dir / "coverage.tsv", coverage_rows)
    write_tsv(out_dir / "candidate_genes.tsv", candidate_rows)
    write_report(out_dir / "coverage_report.md", coverage_rows, release_info)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
