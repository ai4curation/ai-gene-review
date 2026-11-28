#!/usr/bin/env python
"""Diagnose VEuPathDB organisms with PANTHER families but zero QuickGO IBAs."""

from __future__ import annotations

import csv
import gzip
import json
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import yaml


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
    expected_state: str
    species_taxon_id: int | None = None
    nearest_paint_reference: str = ""
    go_mnemonics: tuple[str, ...] = field(default_factory=tuple)

    def all_go_mnemonics(self) -> tuple[str, ...]:
        return (self.mnemonic, *self.go_mnemonics)


PROBES: tuple[Probe, ...] = (
    Probe(
        "PlasmoDB",
        "Plasmodium vivax Sal-1",
        "PLAVS",
        126793,
        "zero",
        5855,
        "PLAF7 / Plasmodium falciparum 3D7",
    ),
    Probe(
        "PlasmoDB",
        "Plasmodium berghei ANKA",
        "PLABA",
        5823,
        "zero",
        5821,
        "PLAF7 / Plasmodium falciparum 3D7",
    ),
    Probe(
        "ToxoDB",
        "Toxoplasma gondii ME49",
        "TOXGM",
        508771,
        "zero",
        5811,
        go_mnemonics=("TOXGO",),
    ),
    Probe(
        "CryptoDB",
        "Cryptosporidium parvum Iowa II",
        "CRYPI",
        353152,
        "zero",
        5807,
    ),
    Probe(
        "TriTrypDB",
        "Trypanosoma cruzi",
        "TRYCR",
        5693,
        "zero",
        5693,
        "TRYB2 / Trypanosoma brucei TREU927",
    ),
    Probe(
        "TriTrypDB",
        "Leishmania donovani",
        "LEIDO",
        5661,
        "zero",
        5661,
        "LEIMA / Leishmania major Friedlin",
    ),
    Probe(
        "PiroplasmaDB",
        "Babesia bovis T2Bo",
        "BABBO",
        5865,
        "zero",
        5865,
    ),
    Probe(
        "PiroplasmaDB",
        "Babesia microti strain RI",
        "BABMR",
        1133968,
        "zero",
        5868,
    ),
    Probe(
        "PiroplasmaDB",
        "Theileria annulata strain Ankara",
        "THEAN",
        5874,
        "zero",
        5874,
    ),
    Probe(
        "PiroplasmaDB",
        "Theileria parva strain Muguga",
        "THEPA",
        5875,
        "zero",
        5875,
    ),
    Probe(
        "MicrosporidiaDB",
        "Encephalitozoon cuniculi GB-M1",
        "ENCCU",
        284813,
        "zero",
        6035,
    ),
    Probe(
        "MicrosporidiaDB",
        "Encephalitozoon intestinalis ATCC 50506",
        "ENCIT",
        876142,
        "zero",
        58839,
    ),
    Probe(
        "MicrosporidiaDB",
        "Enterocytozoon bieneusi H348",
        "ENTBH",
        481877,
        "zero",
        31281,
    ),
    Probe(
        "MicrosporidiaDB",
        "Nematocida parisii ERTm3",
        "NEMP3",
        935791,
        "zero",
        586133,
    ),
    Probe(
        "FungiDB",
        "Nakaseomyces glabratus CBS 138",
        "CANGA",
        284593,
        "zero",
        5478,
        "CANAL / Candida albicans SC5314",
    ),
    Probe(
        "FungiDB",
        "Cryptococcus neoformans H99",
        "CRYN9",
        235443,
        "zero",
        5207,
        "CRYNJ/CRYD1 / Cryptococcus deneoformans JEC21",
    ),
    Probe(
        "VectorBase",
        "Aedes aegypti",
        "AEDAE",
        7159,
        "zero",
        7159,
        "ANOGA / Anopheles gambiae PEST",
    ),
    Probe(
        "VectorBase",
        "Ixodes scapularis Wikel",
        "IXOSC",
        6945,
        "under_exported",
        6945,
    ),
    Probe(
        "PlasmoDB",
        "Plasmodium falciparum 3D7",
        "PLAF7",
        36329,
        "paint_reference",
        5833,
    ),
    Probe(
        "TriTrypDB",
        "Trypanosoma brucei TREU927",
        "TRYB2",
        185431,
        "paint_reference",
        go_mnemonics=("TRYBB",),
    ),
    Probe(
        "TriTrypDB",
        "Leishmania major Friedlin",
        "LEIMA",
        5664,
        "paint_reference",
    ),
    Probe(
        "VectorBase",
        "Anopheles gambiae PEST",
        "ANOGA",
        7165,
        "paint_reference",
    ),
    Probe(
        "FungiDB",
        "Candida albicans SC5314",
        "CANAL",
        237561,
        "paint_reference",
    ),
    Probe(
        "FungiDB",
        "Cryptococcus deneoformans JEC21",
        "CRYD1",
        214684,
        "paint_reference",
    ),
)

IBA_DIAGNOSIS_FIELDS = (
    "category",
    "expected_state",
    "site",
    "organism",
    "mnemonic",
    "go_mnemonics",
    "taxon_id",
    "species_taxon_id",
    "quickgo_iba_exact_hits",
    "quickgo_iba_species_descendant_hits",
    "in_go_reference_species",
    "in_panther_supported_genomes",
    "panther_short_name",
    "panther_sequence_file",
    "go_gaf_files",
    "go_gpad_files",
    "go_gpi_files",
    "go_gaf_iba_total_rows",
    "go_gaf_iba_rows_by_file",
    "nearest_paint_reference",
    "paint_leaf_gaf_rows",
    "paint_leaf_gaf_accessions",
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


def directory_filenames(url: str) -> set[str]:
    parser = LinkParser()
    parser.feed(get(url).decode())
    names: set[str] = set()
    for href in parser.hrefs:
        name = Path(urllib.parse.urlparse(href).path).name
        if name:
            names.add(name)
    return names


def parse_reference_species(text: str) -> dict[int, dict[str, str | int]]:
    records = yaml.safe_load(text)
    return {
        int(record["taxon_id"].removeprefix("NCBITaxon:")): record
        for record in records
    }


def supported_genomes() -> dict[int, dict[str, str | int]]:
    data = get_json(PANTHER_SUPPORTED_GENOMES_URL)
    genomes = data["search"]["output"]["genomes"]["genome"]
    return {int(genome["taxon_id"]): genome for genome in genomes}


def quickgo_iba_hits(taxon_id: int, taxon_usage: str = "exact") -> int:
    data = get_json(
        QUICKGO_URL,
        {
            "taxonId": taxon_id,
            "taxonUsage": taxon_usage,
            "evidenceCode": "ECO:0000318",
            "geneProductType": "protein",
            "limit": 1,
        },
    )
    return int(data["numberOfHits"])


@dataclass
class PaintGafSummary:
    row_counts: Counter[int]
    accessions: dict[int, set[str]]
    header_date: str


def paint_gaf_summary() -> PaintGafSummary:
    row_counts: Counter[int] = Counter()
    accessions: dict[int, set[str]] = defaultdict(set)
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
                    row_counts[taxon_id] += 1
                    accessions[taxon_id].add(fields[1])
    return PaintGafSummary(row_counts, accessions, header_date)


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


def files_for_mnemonics(files: set[str], mnemonics: tuple[str, ...]) -> list[str]:
    return sorted(
        name for name in files if any(name.startswith(f"{m}-") for m in mnemonics)
    )


def csv_list(values: list[str]) -> str:
    return ",".join(values)


def format_file_counts(counts: dict[str, int]) -> str:
    return "; ".join(f"{filename}={counts[filename]}" for filename in sorted(counts))


def write_tsv(
    rows: list[dict[str, str | int]], path: Path, fieldnames: tuple[str, ...] | None = None
) -> None:
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=fieldnames or list(rows[0]),
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def write_paint_taxa(
    path: Path,
    paint: PaintGafSummary,
    go_reference: dict[int, dict[str, str | int]],
    panther_genomes: dict[int, dict[str, str | int]],
) -> None:
    rows = []
    for taxon_id in sorted(paint.row_counts):
        go_ref = go_reference.get(taxon_id, {})
        panther = panther_genomes.get(taxon_id, {})
        rows.append(
            {
                "taxon_id": taxon_id,
                "panther_short_name": panther.get("short_name", ""),
                "go_reference_mnemonic": go_ref.get(
                    "reference_proteome_short_name", ""
                ),
                "panther_name": panther.get("name", ""),
                "organism": go_ref.get("organism") or panther.get("long_name", ""),
                "paint_leaf_gaf_rows": paint.row_counts[taxon_id],
                "paint_leaf_gaf_accessions": len(paint.accessions[taxon_id]),
            }
        )
    write_tsv(rows, path)


def row_category(
    go_ref: dict[str, str | int] | None,
    panther: dict[str, str | int] | None,
    paint_rows: int,
    quickgo_exact: int,
    quickgo_species_descendants: int | str,
) -> str:
    species_control_passes = (
        quickgo_species_descendants == "" or quickgo_species_descendants > 0
    )
    if go_ref and panther and paint_rows > 0 and 0 < quickgo_exact * 10 < paint_rows:
        return "under_exported"
    if go_ref and panther and paint_rows > 0 and quickgo_exact > 0:
        return "paint_reference" if species_control_passes else "contradiction"
    if (
        not go_ref
        and not panther
        and paint_rows == 0
        and quickgo_exact == 0
        and quickgo_species_descendants == 0
    ):
        return "zero"
    return "contradiction"


def sequence_file_for(
    panther: dict[str, str | int] | None, sequence_files: set[str]
) -> str:
    if not panther:
        return ""
    expected_file = f"PTHR{PANTHER_RELEASE}_{panther['name']}"
    return expected_file if expected_file in sequence_files else ""


def zero_diagnosis(row: dict[str, str | int]) -> str:
    clauses = ["Absent from the GO/PANTHER PAINT reference taxon set"]
    if row["go_gaf_files"]:
        clauses.append("GO per-mnemonic exports exist but carry no IBA rows")
    else:
        clauses.append("GO has no per-mnemonic export for the probed mnemonic(s)")
    if row["nearest_paint_reference"]:
        clauses.append(f"nearest included reference: {row['nearest_paint_reference']}")
    else:
        clauses.append("no close PAINT reference in this VEuPathDB panel")
    return "; ".join(clauses) + "."


def validate_expectations(rows: list[dict[str, str | int]]) -> None:
    errors = [
        (
            f"{row['mnemonic']} expected {row['expected_state']} but measured "
            f"{row['category']}"
        )
        for row in rows
        if row["category"] != row["expected_state"]
    ]
    if errors:
        raise SystemExit("Contradictory zero-IBA diagnosis:\n- " + "\n- ".join(errors))


def write_report(
    rows: list[dict[str, str | int]], metadata: dict[str, str], path: Path
) -> None:
    zero_rows = [row for row in rows if row["category"] == "zero"]
    reference_rows = [row for row in rows if row["category"] == "paint_reference"]
    under_exported_rows = [row for row in rows if row["category"] == "under_exported"]

    lines = [
        "---",
        "autolink_gene_symbols: false",
        "---",
        "",
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
            "- QuickGO annotation search for exact taxon and "
            "species-plus-descendant IBA (`ECO:0000318`) annotation counts."
        ),
        f"- Retrieval date: {metadata['retrieved_date']}.",
        "",
        "## Diagnosis",
        "",
        (
            f"All {len(zero_rows)} zero-IBA organisms in the coverage panel are "
            "absent from the PAINT leaf-GAF taxon inventory, which contains "
            f"{metadata['paint_taxa']} taxa total. They are also absent from "
            "GO's PAINT reference-species list and the PANTHER supported-genomes "
            "API. Their exact taxon and "
            "species-plus-descendant QuickGO IBA queries both returned zero "
            "annotations."
        ),
        "",
        (
            "Their nonzero PANTHER family coverage in UniProtKB comes from "
            "family/subfamily sequence classification and does not imply that the "
            "taxon is a PAINT reference leaf eligible for a PTN-backed IBA export. "
            f"The PANTHER per-species sequence-classification directory has "
            f"matching files for {metadata['panther_sequence_file_matches']} of "
            f"{metadata['panther_supported_genomes']} supported-genome API "
            "entries; none of these zero-IBA taxa has a supported-genome entry."
        ),
        "",
        "| Site | Taxon | Mnemonic | QuickGO exact IBA | "
        "QuickGO species+desc IBA | GO ref? | PANTHER ref? | PAINT rows | "
        "GO GAFs | Diagnosis |",
        "|---|---|---:|---:|---:|---|---|---:|---|---|",
    ]
    for row in zero_rows:
        lines.append(
            f"| {row['site']} | {row['organism']} | `{row['mnemonic']}` | "
            f"{row['quickgo_iba_exact_hits']} | "
            f"{row['quickgo_iba_species_descendant_hits']} | "
            f"{row['in_go_reference_species']} | "
            f"{row['in_panther_supported_genomes']} | "
            f"{row['paint_leaf_gaf_rows']} | "
            f"`{row['go_gaf_files'] or 'none'}` | "
            f"{zero_diagnosis(row)} |"
        )

    lines.extend(
        [
            "",
            "## PAINT-covered QuickGO export gap",
            "",
            (
                "The full PAINT leaf-GAF inventory also reveals a distinct "
                "VectorBase lead: Ixodes is a PAINT reference taxon, but only a "
                "small fraction of its PAINT rows appear in QuickGO."
            ),
            "",
            "| Site | Taxon | Mnemonic | QuickGO exact IBA | PAINT rows | "
            "GO GAF IBA rows by file |",
            "|---|---|---:|---:|---:|---|",
        ]
    )
    for row in under_exported_rows:
        lines.append(
            f"| {row['site']} | {row['organism']} | `{row['mnemonic']}` | "
            f"{row['quickgo_iba_exact_hits']} | {row['paint_leaf_gaf_rows']} | "
            f"{row['go_gaf_iba_rows_by_file']} |"
        )

    lines.extend(
        [
            "",
            "## PAINT-bearing controls",
            "",
            (
                "The sibling reference genomes below carry rows in the same data "
                "sources, which rules out a blanket PAINT export failure for "
                "VEuPathDB-relevant clades."
            ),
            "",
            "| Site | PAINT taxon | PANTHER short name | Sequence file | "
            "PAINT rows | GO GAF IBA rows by file | GO GAFs |",
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
            f"{row['quickgo_iba_exact_hits']} exact QuickGO IBA annotations and "
            f"{row['paint_leaf_gaf_rows']} PAINT leaf-GAF rows.",
            f"Species taxon `{row['species_taxon_id']}` and its descendants had "
            f"{row['quickgo_iba_species_descendant_hits']} QuickGO IBA annotations.",
        ]
        if row["go_gaf_files"]:
            clauses.append(
                f"GO has `{row['go_gaf_files']}` GAF export(s) for the probed "
                f"mnemonic(s) with no IBA rows "
                f"(`{row['go_gaf_iba_rows_by_file']}`)."
            )
        else:
            clauses.append("GO has no per-mnemonic GAF for the probed mnemonic(s).")
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
                "eukaryotic pathogen and vector proteomes for GO review. "
                "The following VEuPathDB organisms have UniProtKB proteins with "
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
                "the PANTHER supported-genomes API, and the PANTHER PAINT "
                f"leaf GAF snapshot {PAINT_SNAPSHOT}. Querying each exact taxon "
                "and its species taxon with `taxonUsage=descendants` in QuickGO "
                "also returns zero IBA rows, so this does not look like a "
                "strain-only query mismatch."
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
            "",
            (
                "A separate VectorBase export lead is worth checking too: "
                "Ixodes scapularis (`IXOSC`, taxon `6945`) is present in the "
                f"same PAINT leaf GAF with {under_exported_rows[0]['paint_leaf_gaf_rows']} "
                "IBA rows, but the exact QuickGO query currently returns only "
                f"{under_exported_rows[0]['quickgo_iba_exact_hits']} IBA rows."
            ),
        ]
    )
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    out_dir = Path(__file__).resolve().parent
    retrieved_date = datetime.now(timezone.utc).date().isoformat()

    panther_genomes = supported_genomes()
    go_reference = parse_reference_species(get(GO_REFERENCE_SPECIES_URL).decode())
    sequence_files = directory_filenames(PANTHER_SEQUENCE_BASE)
    gaf_files = directory_filenames(f"{GO_RELEASE_BASE}/annotations/gaf/index.html")
    gpad_files = directory_filenames(f"{GO_RELEASE_BASE}/annotations/gpad/index.html")
    gpi_files = directory_filenames(f"{GO_RELEASE_BASE}/annotations/gpi/index.html")
    paint = paint_gaf_summary()
    expected_sequence_files = {
        f"PTHR{PANTHER_RELEASE}_{panther['name']}"
        for panther in panther_genomes.values()
    }

    quickgo_exact = {
        taxon_id: quickgo_iba_hits(taxon_id)
        for taxon_id in {probe.taxon_id for probe in PROBES}
    }
    quickgo_species_descendants = {
        taxon_id: quickgo_iba_hits(taxon_id, "descendants")
        for taxon_id in {
            probe.species_taxon_id
            for probe in PROBES
            if probe.species_taxon_id is not None
        }
    }

    rows: list[dict[str, str | int]] = []
    for probe in PROBES:
        panther = panther_genomes.get(probe.taxon_id)
        go_ref = go_reference.get(probe.taxon_id)
        probe_gaf = files_for_mnemonics(gaf_files, probe.all_go_mnemonics())
        go_gaf_iba_rows_by_file = {
            filename: gaf_iba_count(filename) for filename in probe_gaf
        }
        quickgo_species_hits: str | int = ""
        if probe.species_taxon_id is not None:
            quickgo_species_hits = quickgo_species_descendants[probe.species_taxon_id]
        paint_rows = paint.row_counts[probe.taxon_id]
        category = row_category(
            go_ref,
            panther,
            paint_rows,
            quickgo_exact[probe.taxon_id],
            quickgo_species_hits,
        )
        rows.append(
            {
                "category": category,
                "expected_state": probe.expected_state,
                "site": probe.site,
                "organism": probe.organism,
                "mnemonic": probe.mnemonic,
                "go_mnemonics": csv_list(list(probe.all_go_mnemonics())),
                "taxon_id": probe.taxon_id,
                "species_taxon_id": probe.species_taxon_id or "",
                "quickgo_iba_exact_hits": quickgo_exact[probe.taxon_id],
                "quickgo_iba_species_descendant_hits": quickgo_species_hits,
                "in_go_reference_species": "yes" if go_ref else "no",
                "in_panther_supported_genomes": "yes" if panther else "no",
                "panther_short_name": panther.get("short_name", "") if panther else "",
                "panther_sequence_file": sequence_file_for(panther, sequence_files),
                "go_gaf_files": csv_list(probe_gaf),
                "go_gpad_files": csv_list(
                    files_for_mnemonics(gpad_files, probe.all_go_mnemonics())
                ),
                "go_gpi_files": csv_list(
                    files_for_mnemonics(gpi_files, probe.all_go_mnemonics())
                ),
                "go_gaf_iba_total_rows": sum(go_gaf_iba_rows_by_file.values()),
                "go_gaf_iba_rows_by_file": format_file_counts(
                    go_gaf_iba_rows_by_file
                ),
                "paint_leaf_gaf_rows": paint_rows,
                "paint_leaf_gaf_accessions": len(paint.accessions[probe.taxon_id]),
                "nearest_paint_reference": probe.nearest_paint_reference,
            }
        )

    validate_expectations(rows)
    write_tsv(rows, out_dir / "iba_zero_diagnosis.tsv", IBA_DIAGNOSIS_FIELDS)
    write_paint_taxa(
        out_dir / "paint_leaf_taxa.tsv",
        paint,
        go_reference,
        panther_genomes,
    )
    write_report(
        rows,
        {
            "paint_gaf_date": paint.header_date,
            "paint_taxa": str(len(paint.row_counts)),
            "panther_sequence_file_matches": str(
                len(expected_sequence_files & sequence_files)
            ),
            "panther_supported_genomes": str(len(panther_genomes)),
            "retrieved_date": retrieved_date,
        },
        out_dir / "iba_zero_diagnosis.md",
    )


if __name__ == "__main__":
    main()
