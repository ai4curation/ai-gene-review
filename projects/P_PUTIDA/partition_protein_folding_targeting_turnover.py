#!/usr/bin/env python3
"""Partition the PSEPK protein folding/targeting/turnover functional bucket."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PARTITION_TSV = ROOT / "projects/P_PUTIDA/data/psepk_pathway_partition.tsv"
BATCH_DIR = ROOT / "projects/P_PUTIDA/batches"
OUT_TSV = BATCH_DIR / "module_protein_folding_targeting_turnover_partition.tsv"
OUT_MD = BATCH_DIR / "module_protein_folding_targeting_turnover_partition.md"
GENE_ROOT = ROOT / "genes/PSEPK"
SOURCE_BUCKET = "module:protein_folding_targeting_turnover"


BUCKETS = {
    "chaperone_folding_holdase_foldase": {
        "label": "Chaperone, holdase, and foldase systems",
        "module": "bacterial_chaperone_protein_folding_boundary",
        "action": "NEXT_SUBMODULE",
        "status": "QUEUED",
        "note": (
            "Core and accessory bacterial protein-folding factors: Hsp33, SurA, "
            "FKBP/PPiases, HscAB, GroES, ClpB-like disaggregase, DnaJ-like and "
            "GrpE/CbpA/CbpM co-chaperone context, plus cold-shock nucleic-acid "
            "chaperone side context. Curate as bacterial proteostasis/folding, "
            "not as a eukaryotic ER-processing or integrated-stress-response module."
        ),
        "genes": [
            "hslO",
            "surA",
            "clpB",
            "slyD",
            "hscB",
            "hscA",
            "groES",
            "PP_1548",
            "cspA-II",
            "PP_3316",
            "grpE",
            "cbpM",
            "cbpA",
        ],
    },
    "atp_dependent_protease_turnover": {
        "label": "ATP-dependent protease and protein-turnover systems",
        "module": "bacterial_atp_dependent_protein_turnover_boundary",
        "action": "NEW_SUBMODULE",
        "status": "QUEUED",
        "note": (
            "Lon, Clp, HslUV, and related AAA+ protease/unfoldase or adaptor "
            "components. Curate proteolysis, ATP hydrolysis/unfoldase, and complex "
            "membership conservatively; do not assume every ATPase subunit has the "
            "peptidase catalytic activity."
        ),
        "genes": [
            "PP_0680",
            "sspB",
            "lon-I",
            "clpP",
            "clpX",
            "lon-II",
            "PP_3045",
            "PP_3267",
            "clpA",
            "clpS",
            "PP_4814",
            "hslV",
            "hslU",
        ],
    },
    "cofactor_metal_maturation_chaperones": {
        "label": "Cofactor, metal, and enzyme-maturation chaperones",
        "module": "cofactor_metal_maturation_chaperone_boundary",
        "action": "NEW_OR_REUSE_BOUNDARY",
        "status": "QUEUED",
        "note": (
            "Copper, heme, succinate-dehydrogenase flavin, urease nickel-insertion, "
            "and G3E-family metal/chaperone candidates. Route to their real enzyme "
            "or metal-homeostasis modules where possible rather than treating them "
            "as generic protein-folding factors."
        ),
        "genes": [
            "PP_0588",
            "sdhE",
            "ureD",
            "ureE",
            "ureF",
            "ureG",
            "cobW",
            "zinU",
            "PP_4836",
            "yggW",
            "PP_5361",
            "PP_5393",
        ],
    },
    "cell_wall_envelope_peptidase_inhibitor": {
        "label": "Cell-wall, envelope, and protease-inhibitor peptidase context",
        "module": "envelope_cell_wall_peptidase_inhibitor_boundary",
        "action": "NEW_OR_REUSE_BOUNDARY",
        "status": "QUEUED",
        "note": (
            "M23/M37, NlpC/P60, M15, tail-specific/C-terminal processing "
            "proteases, cell-wall peptidase-like candidates, alpha-2-macroglobulin, "
            "ecotin, chagasin-like, and small peptidase-inhibitor entries. Separate "
            "peptidoglycan remodeling from generic protease inhibition and avoid "
            "forcing pathway outputs from family names alone."
        ),
        "genes": [
            "PP_0435",
            "yfhM",
            "PP_1026",
            "PP_1442",
            "PP_1669",
            "PP_1670",
            "prc",
            "PP_2108",
            "PP_2364",
            "eco",
            "PP_4799",
            "PP_5057",
            "ctpA",
            "PP_5092",
            "PP_5323",
            "PP_5729",
        ],
    },
    "peptide_processing_aminopeptidases": {
        "label": "Peptide processing and aminopeptidases",
        "module": "protein_turnover_peptide_processing_boundary",
        "action": "NEW_SUBMODULE",
        "status": "QUEUED",
        "note": (
            "Oligopeptidase, methionine aminopeptidase, Xaa-Pro aminopeptidase, "
            "M20/M42/M24-family peptidases, and related cytosolic peptide-turnover "
            "enzymes. Curate enzyme-level activities where supported and keep broad "
            "proteolysis as process context."
        ),
        "genes": [
            "prlC",
            "PP_0203",
            "mtfA",
            "map",
            "apeB",
            "PP_1748",
            "yegQ",
            "PP_2704",
            "ydcP",
            "PP_4752",
            "PP_4949",
            "pepP",
            "PP_5629",
        ],
    },
    "periplasmic_membrane_secreted_protease_qc": {
        "label": "Periplasmic, membrane, and secreted protease quality-control context",
        "module": "envelope_protease_quality_control_boundary",
        "action": "NEW_OR_REUSE_BOUNDARY",
        "status": "QUEUED",
        "note": (
            "Membrane M48, beta-barrel assembly-enhancing protease, subtilase, "
            "M16 zinc protease/processin peptidase, and other envelope or exported "
            "protease candidates. Use signal peptide/membrane context and domain "
            "evidence; leave substrates unresolved unless supported."
        ),
        "genes": [
            "qmcA",
            "PP_0759",
            "pmbA",
            "PP_1232",
            "PP_1499",
            "PP_4113",
            "PP_4924",
            "PP_5112",
            "PP_5115",
            "PP_5116",
            "PP_5455",
            "PP_5604",
        ],
    },
    "dna_damage_or_repair_spillover_proteases": {
        "label": "DNA-damage and repair spillover protease candidates",
        "module": "dna_bucket_architectural_rna_protein_spillover_boundary",
        "action": "REUSE_OR_EXTEND_EXISTING",
        "status": "QUEUED",
        "note": (
            "Abasic-site processing proteins and RadC-family metalloprotease-like "
            "entries. Route to DNA-repair or spillover modules only where AP-site, "
            "DNA-binding, or repair context is actually supported."
        ),
        "genes": ["PP_0758", "PP_2493", "PP_2941"],
    },
    "phage_mobile_protease_spillovers": {
        "label": "Phage and mobile-element protease spillovers",
        "module": "phage_structural_packaging_boundary",
        "action": "REUSE_OR_EXTEND_EXISTING",
        "status": "QUEUED",
        "note": (
            "Phage U35/minor-capsid protease entries that entered by protease "
            "keywords but should be evaluated in mobile-element or phage-structural "
            "context, not as host protein-turnover enzymes."
        ),
        "genes": ["PP_1566", "PP_3878"],
    },
    "low_information_peptidase_spillovers": {
        "label": "Low-information peptidase-family spillovers",
        "module": "protein_turnover_peptidase_spillover_boundary",
        "action": "DEFER_LOW_EVIDENCE",
        "status": "QUEUED",
        "note": (
            "Generic peptidase or protease-family entries with weak pathway, "
            "substrate, or catalytic specificity. Keep family-supported generic "
            "activities only where GOA/domain evidence supports them."
        ),
        "genes": [
            "PP_0831",
            "PP_2447",
            "PP_2685",
            "pfpI",
            "PP_2855",
            "PP_4583",
            "PP_4913",
        ],
    },
}

BUCKET_ORDER = list(BUCKETS)

FIELDS = [
    "gene",
    "ordered_locus",
    "uniprot_accession",
    "protein_name",
    "ec_numbers",
    "go_ids",
    "interpro_ids",
    "pfam_ids",
    "panther_ids",
    "keywords",
    "partition_bucket",
    "partition_label",
    "proposed_module",
    "recommended_action",
    "bucket_status",
    "notes",
    "review_status",
    "curation_status",
    "asta_research_status",
]


def review_status(gene: str) -> str:
    return "PRESENT" if (GENE_ROOT / gene / f"{gene}-ai-review.yaml").exists() else "MISSING"


def curation_status(gene: str) -> str:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    if not path.exists():
        return "MISSING"
    text = path.read_text(encoding="utf-8")
    if "action: PENDING" in text or "TODO: Review" in text or "TODO: Add description" in text:
        return "PENDING"
    return "CURATED"


def asta_research_status(gene: str) -> str:
    return "PRESENT" if (GENE_ROOT / gene / f"{gene}-deep-research-asta.md").exists() else "MISSING"


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def make_row(source: dict[str, str], bucket_id: str) -> dict[str, str]:
    info = BUCKETS[bucket_id]
    gene = source["suggested_review_name"]
    return {
        "gene": gene,
        "ordered_locus": source["ordered_locus"],
        "uniprot_accession": source["uniprot_accession"],
        "protein_name": source["protein_name"],
        "ec_numbers": source["ec_numbers"],
        "go_ids": source["go_ids"],
        "interpro_ids": source["interpro_ids"],
        "pfam_ids": source["pfam_ids"],
        "panther_ids": source["panther_ids"],
        "keywords": source["keywords"],
        "partition_bucket": bucket_id,
        "partition_label": info["label"],
        "proposed_module": info["module"],
        "recommended_action": info["action"],
        "bucket_status": info["status"],
        "notes": info["note"],
        "review_status": review_status(gene),
        "curation_status": curation_status(gene),
        "asta_research_status": asta_research_status(gene),
    }


def write_batch_md(path: Path, title: str, rows: list[dict[str, str]], note: str) -> None:
    lines = [
        "---",
        f'title: "{title}"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        f"# {title}",
        "",
        note,
        "",
        "| Gene | Ordered locus | UniProt | Protein | Review | Asta |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['gene']}` | `{row['ordered_locus']}` | `{row['uniprot_accession']}` | "
            f"{row['protein_name']} | {row['curation_status']} | {row['asta_research_status']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    source_rows = [
        row
        for row in csv.DictReader(PARTITION_TSV.open(encoding="utf-8"), delimiter="\t")
        if row["primary_bucket_id"] == SOURCE_BUCKET
    ]
    if not source_rows:
        raise SystemExit(f"No rows found for {SOURCE_BUCKET}")

    row_by_gene = {row["suggested_review_name"]: row for row in source_rows}
    assigned: dict[str, str] = {}
    for bucket_id, info in BUCKETS.items():
        for gene in info["genes"]:
            if gene in assigned:
                raise SystemExit(f"{gene} assigned twice: {assigned[gene]} and {bucket_id}")
            assigned[gene] = bucket_id

    missing = sorted(set(row_by_gene) - set(assigned))
    extra = sorted(set(assigned) - set(row_by_gene))
    if missing or extra:
        raise SystemExit(f"Partition mismatch; missing={missing}; extra={extra}")

    rows = [make_row(row_by_gene[gene], assigned[gene]) for gene in row_by_gene]
    write_rows(OUT_TSV, rows)

    by_bucket: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_bucket[row["partition_bucket"]].append(row)

    lines = [
        "---",
        'title: "PSEPK protein folding, targeting, and turnover partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK protein folding, targeting, and turnover partition",
        "",
        "The `module:protein_folding_targeting_turnover` bucket is a functional",
        "UniProt-name/keyword bucket, not a single satisfiable pathway. It combines",
        "core bacterial chaperone/foldase systems, ATP-dependent protein-turnover",
        "machinery, cofactor/metal insertion chaperones, envelope and cell-wall",
        "peptidases, aminopeptidases, DNA-repair and phage spillovers, and generic",
        "low-information peptidase-family records.",
        "",
        f"- Full partition table: `projects/P_PUTIDA/batches/{OUT_TSV.name}`",
        f"- Total primary genes: {len(rows)}",
        "",
        "| Bucket | Genes | Reviews | Curated | Asta | Proposed module | Status |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for bucket_id in BUCKET_ORDER:
        bucket_rows = by_bucket[bucket_id]
        info = BUCKETS[bucket_id]
        reviews = Counter(row["review_status"] for row in bucket_rows)
        curated = Counter(row["curation_status"] for row in bucket_rows)
        asta = Counter(row["asta_research_status"] for row in bucket_rows)
        lines.append(
            f"| `{bucket_id}` | {len(bucket_rows)} | {reviews.get('PRESENT', 0)}/{len(bucket_rows)} | "
            f"{curated.get('CURATED', 0)}/{len(bucket_rows)} | {asta.get('PRESENT', 0)}/{len(bucket_rows)} | "
            f"`{info['module']}` | {info['status']} |"
        )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    for bucket_id in BUCKET_ORDER:
        info = BUCKETS[bucket_id]
        bucket_rows = by_bucket[bucket_id]
        stem = f"module_protein_folding_targeting_turnover_{bucket_id}"
        write_rows(BATCH_DIR / f"{stem}.tsv", bucket_rows)
        write_batch_md(
            BATCH_DIR / f"{stem}.md",
            f"PSEPK protein folding/turnover: {info['label']}",
            bucket_rows,
            info["note"],
        )

    print(f"Wrote {OUT_TSV} and {OUT_MD}")
    for bucket_id in BUCKET_ORDER:
        print(f"{bucket_id}: {len(by_bucket[bucket_id])}")


if __name__ == "__main__":
    main()
