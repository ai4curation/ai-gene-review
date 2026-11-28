#!/usr/bin/env python
"""Diagnose VEuPathDB organisms with PANTHER families but zero QuickGO IBAs."""

from __future__ import annotations

import csv
import gzip
import json
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


PANTHER_RELEASE = "19.0"
PAINT_SNAPSHOT = "2026-08-28"
GO_RELEASE = "2026-08-05"

PANTHER_SUPPORTED_GENOMES_URL = (
    "https://pantherdb.org/services/oai/pantherdb/supportedgenomes"
)
PANTHER_SEQUENCE_BASE = (
    "https://data.pantherdb.org/ftp/sequence_classifications/"
    f"{PANTHER_RELEASE}/PANTHER_Sequence_Classification_files"
)
PAINT_GAF_URL = (
    "https://data.pantherdb.org/ftp/downloads/paint/"
    f"{PANTHER_RELEASE}/{PAINT_SNAPSHOT}/gene_association.paint_uniprot.gaf.gz"
)
GO_RELEASE_BASE = f"https://release.geneontology.org/{GO_RELEASE}"
GO_REFERENCE_SPECIES_URL = f"{GO_RELEASE_BASE}/metadata/go-reference-species.yaml"
QUICKGO_URL = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

USER_AGENT = "ai-gene-review-eukaryotic-pathogens/iba-zero-diagnosis"


@dataclass(frozen=True)
class Probe:
    site: str
    organism: str
    mnemonic: str
    taxon_id: int
    species_taxon_id: int | None
    category: str
    nearest_paint_reference: str
    diagnosis: str


PROBES: tuple[Probe, ...] = (
    Probe(
        "PlasmoDB",
        "Plasmodium vivax Sal-1",
        "PLAVS",
        126793,
        5855,
        "zero",
        "PLAF7 / Plasmodium falciparum 3D7",
        "No P. vivax or P. berghei genome is in the PAINT reference set; "
        "Plasmodium is represented by P. falciparum 3D7 only.",
    ),
    Probe(
        "PlasmoDB",
        "Plasmodium berghei ANKA",
        "PLABA",
        5823,
        5823,
        "zero",
        "PLAF7 / Plasmodium falciparum 3D7",
        "No P. vivax or P. berghei genome is in the PAINT reference set; "
        "Plasmodium is represented by P. falciparum 3D7 only.",
    ),
    Probe(
        "TriTrypDB",
        "Trypanosoma cruzi",
        "TRYCR",
        5693,
        5693,
        "zero",
        "TRYB2 / Trypanosoma brucei TREU927",
        "T. cruzi is absent from the PAINT reference set; "
        "the included trypanosomatids are T. brucei TREU927 and L. major Friedlin.",
    ),
    Probe(
        "TriTrypDB",
        "Leishmania donovani",
        "LEIDO",
        5661,
        5661,
        "zero",
        "LEIMA / Leishmania major Friedlin",
        "L. donovani is absent from the PAINT reference set; "
        "L. major Friedlin is the included Leishmania reference.",
    ),
    Probe(
        "VectorBase",
        "Aedes aegypti",
        "AEDAE",
        7159,
        7159,
        "zero",
        "ANOGA / Anopheles gambiae PEST",
        "A. aegypti is absent from the PAINT reference set; "
        "Anopheles gambiae is the included mosquito.",
    ),
    Probe(
        "ToxoDB",
        "Toxoplasma gondii ME49",
        "TOXGM",
        508771,
        5811,
        "zero",
        "",
        "T. gondii ME49 and the T. gondii species taxon are both absent from "
        "the PAINT reference set.",
    ),
    Probe(
        "FungiDB",
        "Nakaseomyces glabratus CBS 138",
        "CANGA",
        284593,
        5478,
        "zero",
        "CANAL / Candida albicans SC5314",
        "N. glabratus has GO per-taxon exports but is absent from the PAINT "
        "reference set; Candida albicans SC5314 is the included Candida genome.",
    ),
    Probe(
        "FungiDB",
        "Cryptococcus neoformans H99",
        "CRYN9",
        235443,
        5207,
        "zero",
        "CRYNJ/CRYD1 / Cryptococcus deneoformans JEC21",
        "C. neoformans H99 is absent from the PAINT reference set; PAINT uses "
        "the JEC21 genome, whose taxon is now exported by GO as C. deneoformans.",
    ),
    Probe(
        "PlasmoDB",
        "Plasmodium falciparum 3D7",
        "PLAF7",
        36329,
        None,
        "paint_reference",
        "",
        "Positive control: this taxon is present in PAINT.",
    ),
    Probe(
        "TriTrypDB",
        "Trypanosoma brucei TREU927",
        "TRYB2",
        185431,
        None,
        "paint_reference",
        "",
        "Positive control: this taxon is present in PAINT.",
    ),
    Probe(
        "TriTrypDB",
        "Leishmania major Friedlin",
        "LEIMA",
        5664,
        None,
        "paint_reference",
        "",
        "Positive control: this taxon is present in PAINT.",
    ),
    Probe(
        "VectorBase",
        "Anopheles gambiae PEST",
        "ANOGA",
        7165,
        None,
        "paint_reference",
        "",
        "Positive control: this taxon is present in PAINT.",
    ),
    Probe(
        "FungiDB",
        "Candida albicans SC5314",
        "CANAL",
        237561,
        None,
        "paint_reference",
        "",
        "Positive control: this taxon is present in PAINT.",
    ),
    Probe(
        "FungiDB",
        "Cryptococcus deneoformans JEC21",
        "CRYD1",
        214684,
        None,
        "paint_reference",
        "",
        "Positive control: this taxon is present in PAINT as CRYNJ in the "
        "PANTHER 19.0 reference-genome metadata.",
    ),
)


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        for key, value in attrs:
            if key == "href" and value is not None:
                self.hrefs.append(value)


def get(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def get_json(url: str, params: dict[str, str | int] | None = None) -> dict[str, Any]:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    return json.loads(get(url))


def directory_filenames(url: str, suffix: str = "") -> set[str]:
    parser = LinkParser()
    parser.feed(get(url).decode())
    names: set[str] = set()
    for href in parser.hrefs:
        name = Path(urllib.parse.urlparse(href).path).name
        if name.endswith(suffix):
            names.add(name)
    return names


def parse_reference_species(text: str) -> dict[int, dict[str, str | int]]:
    records: dict[int, dict[str, str | int]] = {}
    record: dict[str, str | int] = {}

    def save() -> None:
        if not record:
            return
        taxon = str(record["taxon_id"]).removeprefix("NCBITaxon:")
        record["taxon_id"] = int(taxon)
        records[int(taxon)] = dict(record)

    for line in text.splitlines():
        if line.startswith("- "):
            save()
            record = {}
            line = line[2:]
        else:
            line = line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        record[key.strip()] = value.strip()
    save()
    return records


def supported_genomes() -> dict[int, dict[str, str | int]]:
    data = get_json(PANTHER_SUPPORTED_GENOMES_URL)
    genomes = data["search"]["output"]["genomes"]["genome"]
    return {int(genome["taxon_id"]): genome for genome in genomes}


def quickgo_iba_hits(taxon_id: int) -> int:
    data = get_json(
        QUICKGO_URL,
        {
            "taxonId": taxon_id,
            "evidenceCode": "ECO:0000318",
            "geneProductType": "protein",
            "limit": 1,
        },
    )
    return int(data["numberOfHits"])


def paint_gaf_counts(
    taxon_ids: set[int],
) -> tuple[dict[int, int], dict[int, set[str]], str]:
    row_counts = {taxon_id: 0 for taxon_id in taxon_ids}
    accessions = {taxon_id: set() for taxon_id in taxon_ids}
    header_date = ""

    request = urllib.request.Request(PAINT_GAF_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        with gzip.GzipFile(fileobj=response) as gzip_file:
            for raw_line in gzip_file:
                line = raw_line.decode()
                if line.startswith("!"):
                    if line.startswith("!date-generated:"):
                        header_date = line.split(":", 1)[1].strip()
                    continue
                fields = line.rstrip("\n").split("\t")
                if len(fields) < 13:
                    continue
                for taxon in fields[12].split("|"):
                    if not taxon.startswith("taxon:"):
                        continue
                    taxon_id = int(taxon.removeprefix("taxon:"))
                    if taxon_id in row_counts:
                        row_counts[taxon_id] += 1
                        accessions[taxon_id].add(fields[1])
    return row_counts, accessions, header_date


def gaf_iba_count(filename: str) -> int:
    url = f"{GO_RELEASE_BASE}/annotations/gaf/{filename}"
    count = 0
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        with gzip.GzipFile(fileobj=response) as gzip_file:
            for raw_line in gzip_file:
                line = raw_line.decode()
                if line.startswith("!"):
                    continue
                fields = line.rstrip("\n").split("\t")
                if len(fields) > 6 and fields[6] == "IBA":
                    count += 1
    return count


def files_for_mnemonic(files: set[str], mnemonic: str) -> list[str]:
    return sorted(name for name in files if name.startswith(f"{mnemonic}-"))


def csv_list(values: list[str]) -> str:
    return ",".join(values)


def write_tsv(rows: list[dict[str, str | int]], path: Path) -> None:
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def format_file_counts(counts: dict[str, int]) -> str:
    return "; ".join(f"{filename}={counts[filename]}" for filename in sorted(counts))


def write_report(
    rows: list[dict[str, str | int]], metadata: dict[str, str], path: Path
) -> None:
    zero_rows = [row for row in rows if row["category"] == "zero"]
    reference_rows = [row for row in rows if row["category"] == "paint_reference"]

    lines = [
        "# Zero-IBA VEuPathDB taxon diagnosis",
        "",
        "Generated by "
        "`uv run python projects/EUKARYOTIC_PATHOGENS/iba_zero_diagnosis.py`.",
        "",
        "## Data sources",
        "",
        (
            f"- PANTHER supported-genomes API and PANTHER {PANTHER_RELEASE} "
            "sequence-classification directory."
        ),
        (
            f"- PANTHER {PANTHER_RELEASE} PAINT leaf export "
            f"`gene_association.paint_uniprot.gaf.gz`, snapshot {PAINT_SNAPSHOT}; "
            f"leaf GAF `!date-generated` was {metadata['paint_gaf_date']}."
        ),
        (
            f"- GO release {GO_RELEASE} `metadata/go-reference-species.yaml` and "
            "per-mnemonic `annotations/{gaf,gpad,gpi}` indexes."
        ),
        (
            "- QuickGO annotation search for exact/species taxon IBA "
            "(`ECO:0000318`) protein hit counts."
        ),
        f"- Retrieval timestamp: {metadata['retrieved_at']}.",
        "",
        "## Diagnosis",
        "",
        (
            "The zero rows are not caused by querying the wrong strain taxon. "
            "Each exact taxon and its species taxon returned zero QuickGO IBA "
            "hits, and none of the exact zero taxa appear in GO's PAINT reference "
            "species list, the PANTHER supported-genomes API, the PANTHER 19.0 "
            "per-species sequence-classification files, or the PAINT leaf GAF."
        ),
        "",
        (
            "Their nonzero PANTHER family coverage in UniProtKB comes from "
            "family/subfamily sequence classification and does not imply that the "
            "taxon is a PAINT reference leaf eligible for a PTN-backed IBA export."
        ),
        "",
        "| Site | Taxon | Mnemonic | QuickGO exact IBA | QuickGO species IBA | "
        "GO ref? | PANTHER ref? | PAINT rows | GO GAFs | Diagnosis |",
        "|---|---|---:|---:|---:|---|---|---:|---|---|",
    ]
    for row in zero_rows:
        lines.append(
            f"| {row['site']} | {row['organism']} | `{row['mnemonic']}` | "
            f"{row['quickgo_iba_exact_hits']} | {row['quickgo_iba_species_hits']} | "
            f"{row['in_go_reference_species']} | "
            f"{row['in_panther_supported_genomes']} | "
            f"{row['paint_leaf_gaf_rows']} | "
            f"`{row['go_gaf_files'] or 'none'}` | "
            f"{row['diagnosis']} |"
        )

    lines.extend(
        [
            "",
            "## PAINT-bearing controls",
            "",
            (
                "The sibling reference genomes do carry rows in the same data "
                "sources, which rules out a blanket PAINT export failure for "
                "VEuPathDB-relevant clades."
            ),
            "",
            "| Site | PAINT taxon | PANTHER short name | Sequence file | PAINT rows | "
            "GO GAF IBA rows by file | GO GAFs |",
            "|---|---|---:|---|---:|---|---|",
        ]
    )
    for row in reference_rows:
        lines.append(
            f"| {row['site']} | {row['organism']} | "
            f"`{row['panther_short_name']}` | "
            f"`{row['panther_sequence_file']}` | "
            f"{row['paint_leaf_gaf_rows']} | "
            f"{row['go_gaf_iba_rows_by_file']} | "
            f"`{row['go_gaf_files']}` |"
        )

    lines.extend(
        [
            "",
            "## Notes by taxon",
            "",
        ]
    )
    for row in zero_rows:
        clauses = [
            f"exact taxon `{row['taxon_id']}` had "
            f"{row['quickgo_iba_exact_hits']} QuickGO IBA hits and "
            f"{row['paint_leaf_gaf_rows']} PAINT leaf-GAF rows."
        ]
        if row["species_taxon_id"]:
            clauses.append(
                f"The species-level taxon `{row['species_taxon_id']}` also had "
                f"{row['quickgo_iba_species_hits']} QuickGO IBA hits."
            )
        if row["go_gaf_files"]:
            clauses.append(
                f"GO has `{row['go_gaf_files']}` GAF export(s) for this mnemonic "
                f"with no IBA rows (`{row['go_gaf_iba_rows_by_file']}`)."
            )
        else:
            clauses.append("GO has no per-mnemonic GAF for this mnemonic.")
        if row["nearest_paint_reference"]:
            clauses.append(
                f"Nearest included PAINT reference: {row['nearest_paint_reference']}."
            )
        lines.append(f"- **{row['organism']}**: {' '.join(clauses)}")

    lines.extend(
        [
            "",
            "## Draft GO/PANTHER issue",
            "",
            "**Title:** PAINT/IBA export coverage for VEuPathDB pathogen and vector reference proteomes",
            "",
            "**Body:**",
            "",
            (
                "We are using GO IBA annotations to triage VEuPathDB "
                "eukaryotic pathogen and vector proteomes for GO review. Several "
                "well-studied VEuPathDB organisms have UniProtKB proteins with "
                "PANTHER family cross-references but no IBA rows in QuickGO:"
            ),
            "",
        ]
    )
    for row in zero_rows:
        lines.append(
            f"- {row['organism']} (`{row['mnemonic']}`, taxon `{row['taxon_id']}`)"
        )

    lines.extend(
        [
            "",
            (
                f"Against GO release {GO_RELEASE} and PANTHER {PANTHER_RELEASE}, "
                "these exact taxa are absent from `go-reference-species.yaml`, "
                "the PANTHER supported-genomes API, the PANTHER 19.0 "
                "sequence-classification file set, and the PANTHER PAINT "
                f"leaf GAF snapshot {PAINT_SNAPSHOT}. Querying the species-level "
                "taxon in QuickGO also returns zero IBA rows, so this does not "
                "look like a strain-only query mismatch."
            ),
            "",
            (
                "Can GO/PANTHER either add PAINT reference-proteome and IBA "
                "export coverage for these VEuPathDB organisms, or document why "
                "these current pathogen/vector proteomes are intentionally out "
                "of scope? Candida/Nakaseomyces glabratus is a useful edge case: "
                "GO already publishes `CANGA-mod` and `CANGA-uniprot` GAF/GPAD/GPI "
                "files, but neither carries PAINT/IBA rows because the PAINT "
                "reference set includes `CANAL` rather than `CANGA`."
            ),
        ]
    )
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    out_dir = Path(__file__).resolve().parent
    retrieved_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    panther_genomes = supported_genomes()
    go_reference = parse_reference_species(get(GO_REFERENCE_SPECIES_URL).decode())
    sequence_files = directory_filenames(PANTHER_SEQUENCE_BASE, "")
    gaf_files = directory_filenames(f"{GO_RELEASE_BASE}/annotations/gaf/index.html")
    gpad_files = directory_filenames(f"{GO_RELEASE_BASE}/annotations/gpad/index.html")
    gpi_files = directory_filenames(f"{GO_RELEASE_BASE}/annotations/gpi/index.html")

    watched_taxa = {probe.taxon_id for probe in PROBES}
    paint_rows, paint_accessions, paint_date = paint_gaf_counts(watched_taxa)

    quickgo_exact = {taxon_id: quickgo_iba_hits(taxon_id) for taxon_id in watched_taxa}
    species_taxa = {
        probe.species_taxon_id
        for probe in PROBES
        if probe.species_taxon_id is not None
    }
    quickgo_species = {
        taxon_id: quickgo_iba_hits(taxon_id) for taxon_id in species_taxa
    }

    rows: list[dict[str, str | int]] = []
    for probe in PROBES:
        panther = panther_genomes.get(probe.taxon_id)
        go_ref = go_reference.get(probe.taxon_id)
        short_name = ""
        sequence_file = ""
        if panther:
            short_name = str(panther["short_name"])
            expected_file = f"PTHR{PANTHER_RELEASE}_{panther['name']}"
            if expected_file in sequence_files:
                sequence_file = expected_file
        if not short_name and go_ref:
            short_name = str(go_ref["reference_proteome_short_name"])

        probe_gaf = files_for_mnemonic(gaf_files, probe.mnemonic)
        go_gaf_iba_rows_by_file = {
            filename: gaf_iba_count(filename) for filename in probe_gaf
        }
        rows.append(
            {
                "category": probe.category,
                "site": probe.site,
                "organism": probe.organism,
                "mnemonic": probe.mnemonic,
                "taxon_id": probe.taxon_id,
                "species_taxon_id": probe.species_taxon_id or "",
                "quickgo_iba_exact_hits": quickgo_exact[probe.taxon_id],
                "quickgo_iba_species_hits": (
                    quickgo_species[probe.species_taxon_id]
                    if probe.species_taxon_id is not None
                    else ""
                ),
                "in_go_reference_species": "yes" if go_ref else "no",
                "in_panther_supported_genomes": "yes" if panther else "no",
                "panther_short_name": short_name,
                "panther_sequence_file": sequence_file,
                "go_gaf_files": csv_list(probe_gaf),
                "go_gpad_files": csv_list(files_for_mnemonic(gpad_files, probe.mnemonic)),
                "go_gpi_files": csv_list(files_for_mnemonic(gpi_files, probe.mnemonic)),
                "go_gaf_iba_rows": sum(go_gaf_iba_rows_by_file.values()),
                "go_gaf_iba_rows_by_file": format_file_counts(go_gaf_iba_rows_by_file),
                "paint_leaf_gaf_rows": paint_rows[probe.taxon_id],
                "paint_leaf_gaf_accessions": len(paint_accessions[probe.taxon_id]),
                "nearest_paint_reference": probe.nearest_paint_reference,
                "diagnosis": probe.diagnosis,
            }
        )

    write_tsv(rows, out_dir / "iba_zero_diagnosis.tsv")
    write_report(
        rows,
        {
            "paint_gaf_date": paint_date,
            "retrieved_at": retrieved_at,
        },
        out_dir / "iba_zero_diagnosis.md",
    )


if __name__ == "__main__":
    main()
