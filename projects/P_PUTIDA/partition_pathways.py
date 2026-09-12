#!/usr/bin/env python3
"""Partition PSEPK genes into pathway and unknown buckets."""

from __future__ import annotations

import argparse
import csv
import re
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_GENE_LIST = Path("projects/P_PUTIDA/data/psepk_gene_list.tsv")
DEFAULT_OUTPUT_DIR = Path("projects/P_PUTIDA/data")
KEGG_LINK_URL = "https://rest.kegg.jp/link/pathway/ppu"
KEGG_LIST_URL = "https://rest.kegg.jp/list/pathway/ppu"

# KEGG overview maps are useful context but too broad to drive curation batches.
OVERVIEW_PATHWAYS = {
    "ppu01100",  # Metabolic pathways
    "ppu01110",  # Biosynthesis of secondary metabolites
    "ppu01120",  # Microbial metabolism in diverse environments
    "ppu01200",  # Carbon metabolism
    "ppu01210",  # 2-Oxocarboxylic acid metabolism
    "ppu01212",  # Fatty acid metabolism
    "ppu01230",  # Biosynthesis of amino acids
    "ppu01232",  # Nucleotide metabolism
    "ppu01240",  # Biosynthesis of cofactors
    "ppu01250",  # Biosynthesis of nucleotide sugars
}

FUNCTIONAL_MODULES = [
    (
        "module:chromosome_partition_cell_cycle",
        "Chromosome partitioning, segregation, and cell cycle",
        [
            r"\bchromosome[- ]partition",
            r"\bchromosome segregation\b",
            r"\bcell cycle\b",
            r"\bpar[ab]\b",
        ],
    ),
    (
        "module:motility_chemotaxis_biofilm",
        "Motility, chemotaxis, pili, and biofilm",
        [
            r"\bflagell",
            r"\bchemotaxis\b",
            r"\bchemoreceptor\b",
            r"\bmethyl-accepting chemotaxis\b",
            r"\bpilus\b",
            r"\bpili\b",
            r"\bfimbria",
            r"\bbiofilm\b",
            r"\balginate\b",
        ],
    ),
    (
        "module:regulation_signal_transduction",
        "Regulation and signal transduction",
        [
            r"\btranscriptional regulator\b",
            r"\btranscription regulator\b",
            r"\btranscriptional repressor\b",
            r"\btranscriptional activator\b",
            r"\bresponse regulator\b",
            r"\bsigma factor\b",
            r"\bsensor histidine kinase\b",
            r"\btwo-component\b",
            r"\bdna-binding transcription\b",
        ],
    ),
    (
        "module:transport_membrane_efflux",
        "Transport, membrane proteins, and efflux",
        [
            r"\btransporter\b",
            r"\btransport\b",
            r"\bpermease\b",
            r"\bimporter\b",
            r"\bexporter\b",
            r"\befflux\b",
            r"\bantiporter\b",
            r"\bsymporter\b",
            r"\bporin\b",
            r"\btonb\b",
            r"\bouter membrane receptor\b",
            r"\babc\b",
            r"\bmembrane protein\b",
            r"\btransmembrane\b",
        ],
    ),
    (
        "module:translation_rna_processing",
        "Translation, ribosome, and RNA processing",
        [
            r"\bribosomal\b",
            r"\bribosome\b",
            r"\btrna\b",
            r"\brrna\b",
            r"\brna polymerase\b",
            r"\bribonuclease\b",
            r"\brna-binding\b",
            r"\baminoacyl-trna\b",
        ],
    ),
    (
        "module:dna_replication_repair_recombination",
        "DNA replication, repair, and recombination",
        [
            r"\bdna replication\b",
            r"\bdna repair\b",
            r"\brecombin",
            r"\bexcinuclease\b",
            r"\bmismatch repair\b",
            r"\bdna polymerase\b",
            r"\bdna gyrase\b",
            r"\btopoisomerase\b",
            r"\bhelicase\b",
            r"\bnuclease\b",
        ],
    ),
    (
        "module:protein_folding_targeting_turnover",
        "Protein folding, targeting, and turnover",
        [
            r"\bchaperone\b",
            r"\bchaperonin\b",
            r"\bfoldase\b",
            r"\bprotease\b",
            r"\bpeptidase\b",
            r"\bprotein export\b",
            r"\bprotein transport\b",
            r"\bsignal recognition particle\b",
            r"\bsec-dependent\b",
            r"\btat\b",
        ],
    ),
    (
        "module:cell_envelope_division",
        "Cell envelope, wall biogenesis, and division",
        [
            r"\bcell division\b",
            r"\bseptum\b",
            r"\bcell wall\b",
            r"\bpeptidoglycan\b",
            r"\blipopolysaccharide\b",
            r"\blipid a\b",
            r"\blipoprotein\b",
            r"\bcapsule\b",
            r"\bouter membrane\b",
        ],
    ),
    (
        "module:stress_detoxification",
        "Stress response and detoxification",
        [
            r"\bstress\b",
            r"\bheat shock\b",
            r"\bcold shock\b",
            r"\bperoxidase\b",
            r"\bcatalase\b",
            r"\bsuperoxide\b",
            r"\bglutathione\b",
            r"\bdetox",
            r"\bresistance\b",
        ],
    ),
    (
        "module:mobile_genetic_elements",
        "Mobile genetic elements and phage-related proteins",
        [
            r"\btransposase\b",
            r"\btransposon\b",
            r"\btniq\b",
            r"\bintegrase\b",
            r"\bphage\b",
            r"\bprophage\b",
            r"\bplasmid\b",
        ],
    ),
]

UNKNOWN_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"\buncharacterized\b",
        r"\bhypothetical\b",
        r"\bunknown function\b",
        r"\bprotein of unknown function\b",
        r"\bUPF\d+\b",
        r"\bDUF\d+\b",
    ]
]


def split_semicolon(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def fetch_url(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8")


def clean_pathway_name(name: str) -> str:
    return re.sub(r"\s+-\s+Pseudomonas putida KT2440$", "", name).strip()


def parse_kegg_links(text: str) -> dict[str, set[str]]:
    gene_to_pathways: dict[str, set[str]] = defaultdict(set)
    for line in text.splitlines():
        if not line.strip():
            continue
        gene_id, pathway_id = line.split("\t", 1)
        gene_to_pathways[gene_id].add(pathway_id.replace("path:", ""))
    return gene_to_pathways


def parse_kegg_names(text: str) -> dict[str, str]:
    names: dict[str, str] = {}
    for line in text.splitlines():
        if not line.strip():
            continue
        pathway_id, name = line.split("\t", 1)
        names[pathway_id] = clean_pathway_name(name)
    return names


def pathway_area(pathway_id: str, pathway_name: str) -> str:
    name = pathway_name.casefold()
    if pathway_id in OVERVIEW_PATHWAYS:
        return "overview"
    if any(
        token in name
        for token in [
            "glycolysis",
            "gluconeogenesis",
            "citrate cycle",
            "pentose phosphate",
            "pyruvate",
            "glyoxylate",
            "carbon fixation",
            "propanoate",
            "butanoate",
        ]
    ):
        return "central_carbon"
    if any(
        token in name
        for token in [
            "benzoate",
            "xylene",
            "toluene",
            "styrene",
            "aminobenzoate",
            "nitrotoluene",
            "naphthalene",
            "chlorocyclohexane",
            "chlorobenzene",
            "dioxin",
            "caprolactam",
            "fluorobenzoate",
            "ethylbenzene",
            "aromatic",
        ]
    ):
        return "aromatic_and_xenobiotic_catabolism"
    if any(
        token in name
        for token in [
            "amino acid",
            "alanine",
            "aspartate",
            "glutamate",
            "glycine",
            "serine",
            "threonine",
            "cysteine",
            "methionine",
            "valine",
            "leucine",
            "isoleucine",
            "lysine",
            "arginine",
            "proline",
            "histidine",
            "phenylalanine",
            "tyrosine",
            "tryptophan",
            "taurine",
        ]
    ):
        return "amino_acid_metabolism"
    if any(token in name for token in ["purine", "pyrimidine", "nucleotide"]):
        return "nucleotide_metabolism"
    if any(
        token in name
        for token in [
            "cofactor",
            "vitamin",
            "riboflavin",
            "thiamine",
            "folate",
            "porphyrin",
            "chlorophyll",
            "ubiquinone",
            "terpenoid",
            "pantothenate",
            "nicotinate",
            "lipoic acid",
        ]
    ):
        return "cofactors_vitamins_redox"
    if any(
        token in name
        for token in [
            "fatty acid",
            "glycerolipid",
            "glycerophospholipid",
            "lipopolysaccharide",
            "peptidoglycan",
            "amino sugar",
            "nucleotide sugar",
            "beta-lactam",
        ]
    ):
        return "lipid_cell_envelope_metabolism"
    if any(
        token in name
        for token in [
            "oxidative phosphorylation",
            "nitrogen metabolism",
            "sulfur metabolism",
            "methane metabolism",
        ]
    ):
        return "energy_respiration_inorganic_metabolism"
    if any(
        token in name
        for token in [
            "chemotaxis",
            "flagellar",
            "two-component",
            "secretion",
            "quorum",
            "biofilm",
            "abc transporters",
            "phosphotransferase system",
        ]
    ):
        return "transport_motility_signaling"
    return "other_kegg_pathway"


def row_text(row: dict[str, str]) -> str:
    return " ".join(
        [
            row.get("protein_name", ""),
            row.get("keywords", ""),
            row.get("go_ids", ""),
        ]
    )


def is_unknown_function(row: dict[str, str]) -> bool:
    text = row_text(row)
    return any(pattern.search(text) for pattern in UNKNOWN_PATTERNS)


def functional_module(row: dict[str, str]) -> tuple[str, str, str] | None:
    text = row_text(row)
    for bucket_id, label, patterns in FUNCTIONAL_MODULES:
        if any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns):
            return bucket_id, label, "matched functional keyword pattern"
    return None


def domain_only_orphan(row: dict[str, str]) -> bool:
    return any(
        row.get(column, "").strip()
        for column in ["interpro_ids", "pfam_ids", "panther_ids"]
    )


def choose_primary_pathway(pathways: list[str], pathway_counts: Counter[str]) -> str:
    return sorted(pathways, key=lambda pathway: (pathway_counts[pathway], pathway))[0]


def make_gene_key(row: dict[str, str]) -> str:
    locus = row.get("ordered_locus", "")
    if locus:
        return f"ppu:{locus}"
    for kegg_id in split_semicolon(row.get("kegg_ids", "")):
        if kegg_id.startswith("ppu:"):
            return kegg_id
    return ""


def write_tsv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, delimiter="\t", fieldnames=fieldnames, extrasaction="ignore"
        )
        writer.writeheader()
        writer.writerows(rows)


def partition(args: argparse.Namespace) -> dict[str, int]:
    args.output_dir.mkdir(parents=True, exist_ok=True)

    with args.gene_list.open(newline="", encoding="utf-8") as handle:
        genes = list(csv.DictReader(handle, delimiter="\t"))

    kegg_links_text = fetch_url(KEGG_LINK_URL)
    kegg_names_text = fetch_url(KEGG_LIST_URL)
    (args.output_dir / "psepk_kegg_gene_pathway_links.tsv").write_text(
        kegg_links_text, encoding="utf-8"
    )
    (args.output_dir / "psepk_kegg_pathway_names.tsv").write_text(
        kegg_names_text, encoding="utf-8"
    )

    gene_to_pathways = parse_kegg_links(kegg_links_text)
    pathway_names = parse_kegg_names(kegg_names_text)
    specific_pathway_counts: Counter[str] = Counter()
    for pathways in gene_to_pathways.values():
        for pathway_id in pathways:
            if pathway_id not in OVERVIEW_PATHWAYS:
                specific_pathway_counts[pathway_id] += 1

    membership_rows: list[dict[str, str]] = []
    partition_rows: list[dict[str, str]] = []
    unknown_rows: list[dict[str, str]] = []
    orphan_rows: list[dict[str, str]] = []

    for row in genes:
        gene_key = make_gene_key(row)
        all_pathways = sorted(gene_to_pathways.get(gene_key, set()))
        specific_pathways = [
            pathway_id for pathway_id in all_pathways if pathway_id not in OVERVIEW_PATHWAYS
        ]
        overview_pathways = [
            pathway_id for pathway_id in all_pathways if pathway_id in OVERVIEW_PATHWAYS
        ]
        unipathways = split_semicolon(row.get("unipathway_ids", ""))

        primary_pathway = (
            choose_primary_pathway(specific_pathways, specific_pathway_counts)
            if specific_pathways
            else ""
        )

        for pathway_id in specific_pathways + overview_pathways:
            membership_rows.append(
                {
                    "suggested_review_name": row["suggested_review_name"],
                    "ordered_locus": row["ordered_locus"],
                    "uniprot_accession": row["uniprot_accession"],
                    "membership_source": "KEGG",
                    "pathway_id": pathway_id,
                    "pathway_name": pathway_names.get(pathway_id, ""),
                    "pathway_scope": "overview"
                    if pathway_id in OVERVIEW_PATHWAYS
                    else "specific",
                    "module_area": pathway_area(
                        pathway_id, pathway_names.get(pathway_id, "")
                    ),
                    "is_primary_partition": "true"
                    if pathway_id == primary_pathway
                    else "false",
                }
            )
        for unipathway_id in unipathways:
            membership_rows.append(
                {
                    "suggested_review_name": row["suggested_review_name"],
                    "ordered_locus": row["ordered_locus"],
                    "uniprot_accession": row["uniprot_accession"],
                    "membership_source": "UniPathway",
                    "pathway_id": unipathway_id,
                    "pathway_name": f"UniPathway {unipathway_id}",
                    "pathway_scope": "specific",
                    "module_area": "unipathway",
                    "is_primary_partition": "false",
                }
            )

        if primary_pathway:
            bucket_id = f"kegg:{primary_pathway}"
            bucket_label = pathway_names.get(primary_pathway, primary_pathway)
            bucket_type = "kegg_pathway"
            bucket_source = "KEGG"
            module_area = pathway_area(primary_pathway, bucket_label)
            assignment_reason = "assigned to narrowest specific KEGG pathway by gene count"
        elif unipathways:
            bucket_id = f"unipathway:{unipathways[0]}"
            bucket_label = f"UniPathway {unipathways[0]}"
            bucket_type = "unipathway"
            bucket_source = "UniPathway"
            module_area = "unipathway"
            assignment_reason = "no specific KEGG pathway; UniPathway cross-reference present"
        elif is_unknown_function(row):
            bucket_id = "unknown:function_unknown"
            bucket_label = "Unknown or uncharacterized proteins"
            bucket_type = "unknown"
            bucket_source = "UniProt protein name/keywords"
            module_area = "unknown"
            assignment_reason = "unknown-function wording and no specific pathway assignment"
        else:
            module = functional_module(row)
            if module:
                bucket_id, bucket_label, assignment_reason = module
                bucket_type = "functional_module"
                bucket_source = "UniProt protein name/keywords"
                module_area = bucket_id.replace("module:", "")
            elif row.get("ec_numbers", "").strip():
                bucket_id = "orphan:enzyme_with_ec"
                bucket_label = "Orphan enzymes with EC numbers"
                bucket_type = "orphan"
                bucket_source = "UniProt EC metadata"
                module_area = "orphan_enzyme"
                assignment_reason = "no pathway assignment but EC number is present"
            elif domain_only_orphan(row):
                bucket_id = "orphan:domain_only_no_pathway"
                bucket_label = "Domain-family orphans without pathway assignment"
                bucket_type = "orphan"
                bucket_source = "InterPro/Pfam/PANTHER metadata"
                module_area = "domain_family_orphan"
                assignment_reason = "no pathway or functional-module assignment; domain xref present"
            else:
                bucket_id = "unknown:unassigned_no_pathway_signal"
                bucket_label = "Unassigned genes with minimal pathway signal"
                bucket_type = "unknown"
                bucket_source = "metadata absence"
                module_area = "unknown"
                assignment_reason = "no specific pathway, UniPathway, EC, or recognized module signal"

        partition_row = {
            **row,
            "gene_key": gene_key,
            "primary_bucket_id": bucket_id,
            "primary_bucket_label": bucket_label,
            "primary_bucket_type": bucket_type,
            "primary_bucket_source": bucket_source,
            "primary_module_area": module_area,
            "assignment_reason": assignment_reason,
            "specific_kegg_pathway_ids": ";".join(specific_pathways),
            "specific_kegg_pathway_names": ";".join(
                pathway_names.get(pathway_id, "") for pathway_id in specific_pathways
            ),
            "overview_kegg_pathway_ids": ";".join(overview_pathways),
            "unipathway_ids": ";".join(unipathways),
        }
        partition_rows.append(partition_row)
        if bucket_type == "unknown":
            unknown_rows.append(partition_row)
        elif bucket_type == "orphan":
            orphan_rows.append(partition_row)

    bucket_counts: dict[str, dict[str, str | int | list[str]]] = {}
    for row in partition_rows:
        bucket_id = row["primary_bucket_id"]
        if bucket_id not in bucket_counts:
            bucket_counts[bucket_id] = {
                "bucket_id": bucket_id,
                "bucket_label": row["primary_bucket_label"],
                "bucket_type": row["primary_bucket_type"],
                "bucket_source": row["primary_bucket_source"],
                "module_area": row["primary_module_area"],
                "gene_count": 0,
                "reviewed_count": 0,
                "unreviewed_count": 0,
                "with_ec_count": 0,
                "example_genes": [],
            }
        bucket = bucket_counts[bucket_id]
        bucket["gene_count"] = int(bucket["gene_count"]) + 1
        if row["reviewed"] == "reviewed":
            bucket["reviewed_count"] = int(bucket["reviewed_count"]) + 1
        else:
            bucket["unreviewed_count"] = int(bucket["unreviewed_count"]) + 1
        if row.get("ec_numbers", "").strip():
            bucket["with_ec_count"] = int(bucket["with_ec_count"]) + 1
        examples = bucket["example_genes"]
        if isinstance(examples, list) and len(examples) < 12:
            examples.append(row["suggested_review_name"])

    bucket_rows = []
    for bucket in bucket_counts.values():
        row = dict(bucket)
        row["example_genes"] = ";".join(row["example_genes"])  # type: ignore[index]
        bucket_rows.append(row)  # type: ignore[arg-type]
    bucket_rows.sort(
        key=lambda row: (
            row["bucket_type"] != "kegg_pathway",
            row["module_area"],
            -int(row["gene_count"]),
            row["bucket_id"],
        )
    )

    partition_fields = list(genes[0].keys()) + [
        "gene_key",
        "primary_bucket_id",
        "primary_bucket_label",
        "primary_bucket_type",
        "primary_bucket_source",
        "primary_module_area",
        "assignment_reason",
        "specific_kegg_pathway_ids",
        "specific_kegg_pathway_names",
        "overview_kegg_pathway_ids",
    ]
    membership_fields = [
        "suggested_review_name",
        "ordered_locus",
        "uniprot_accession",
        "membership_source",
        "pathway_id",
        "pathway_name",
        "pathway_scope",
        "module_area",
        "is_primary_partition",
    ]
    bucket_fields = [
        "bucket_id",
        "bucket_label",
        "bucket_type",
        "bucket_source",
        "module_area",
        "gene_count",
        "reviewed_count",
        "unreviewed_count",
        "with_ec_count",
        "example_genes",
    ]

    write_tsv(
        args.output_dir / "psepk_pathway_partition.tsv",
        partition_rows,
        partition_fields,
    )
    write_tsv(
        args.output_dir / "psepk_pathway_membership.tsv",
        membership_rows,
        membership_fields,
    )
    write_tsv(
        args.output_dir / "psepk_pathway_buckets.tsv",
        bucket_rows,
        bucket_fields,
    )
    write_tsv(
        args.output_dir / "psepk_unknown_bucket.tsv",
        unknown_rows,
        partition_fields,
    )
    write_tsv(
        args.output_dir / "psepk_orphan_bucket.tsv",
        orphan_rows,
        partition_fields,
    )

    manifest = args.output_dir / "psepk_pathway_partition.manifest.txt"
    manifest.write_text(
        "\n".join(
            [
                f"generated_utc: {datetime.now(timezone.utc).isoformat()}",
                f"gene_list: {args.gene_list.as_posix()}",
                f"kegg_link_url: {KEGG_LINK_URL}",
                f"kegg_list_url: {KEGG_LIST_URL}",
                "primary_assignment: specific KEGG pathway with the smallest organism-specific gene count; UniPathway fallback; functional module heuristics; unknown/orphan buckets",
                f"overview_pathways_excluded_from_primary: {','.join(sorted(OVERVIEW_PATHWAYS))}",
                f"genes: {len(genes)}",
                f"membership_rows: {len(membership_rows)}",
                f"primary_buckets: {len(bucket_rows)}",
                f"unknown_rows: {len(unknown_rows)}",
                f"orphan_rows: {len(orphan_rows)}",
                "",
            ]
        ),
        encoding="utf-8",
    )

    return {
        "genes": len(genes),
        "membership_rows": len(membership_rows),
        "primary_buckets": len(bucket_rows),
        "unknown_rows": len(unknown_rows),
        "orphan_rows": len(orphan_rows),
        "kegg_primary_rows": sum(
            1 for row in partition_rows if row["primary_bucket_type"] == "kegg_pathway"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Partition PSEPK genes into pathway and unknown buckets."
    )
    parser.add_argument("--gene-list", type=Path, default=DEFAULT_GENE_LIST)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    stats = partition(args)
    print(
        "Wrote pathway partition for "
        f"{stats['genes']} genes: {stats['primary_buckets']} buckets, "
        f"{stats['membership_rows']} memberships, {stats['unknown_rows']} unknowns, "
        f"{stats['orphan_rows']} orphans."
    )


if __name__ == "__main__":
    main()
