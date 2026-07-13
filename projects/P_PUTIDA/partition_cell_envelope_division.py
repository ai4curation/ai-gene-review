#!/usr/bin/env python3
"""Partition the PSEPK cell-envelope/division functional bucket."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PARTITION_TSV = ROOT / "projects/P_PUTIDA/data/psepk_pathway_partition.tsv"
BATCH_DIR = ROOT / "projects/P_PUTIDA/batches"
OUT_TSV = BATCH_DIR / "module_cell_envelope_division_partition.tsv"
OUT_MD = BATCH_DIR / "module_cell_envelope_division_partition.md"
GENE_ROOT = ROOT / "genes/PSEPK"
SOURCE_BUCKET = "module:cell_envelope_division"


BUCKETS = {
    "lpt_outer_membrane_lps_transport_context": {
        "label": "Lpt outer-membrane LPS transport context",
        "module": "lpt_lps_transport_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "LptD/LptE outer-membrane LPS-assembly components already curated as context for the Lpt/LPS transport boundary.",
    },
    "lps_core_lipid_a_biosynthesis_context": {
        "label": "LPS core and lipid-A biosynthesis context",
        "module": "lipopolysaccharide_biosynthesis",
        "action": "NEXT_SUBMODULE",
        "status": "CURATED",
        "note": "LPS-core and lipid-A acyltransferase candidates curated against the existing lipopolysaccharide biosynthesis module.",
    },
    "maltose_acetyltransferase_lipid_a_keyword_spillover": {
        "label": "Maltose acetyltransferase lipid-A-keyword spillover",
        "module": "",
        "action": "COMPLETED_REASSIGN_OR_KEEP_OUT",
        "status": "CURATED",
        "note": "maa entered through lipid-A/fold-level keyword spillover, but first-pass review supports maltose O-acetyltransferase activity rather than LPS/lipid-A biosynthesis.",
    },
    "peptidoglycan_turnover_remodeling_candidates": {
        "label": "Peptidoglycan turnover and remodeling candidates",
        "module": "peptidoglycan_biosynthesis",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "Murein amidases, lytic transglycosylases, endopeptidase/PBP-like enzymes, and peptidoglycan-binding/remodeling candidates; all 11 are first-pass curated and represented in the peptidoglycan biosynthesis/remodeling module.",
    },
    "cell_division_regulatory_spillovers": {
        "label": "Cell-division regulatory spillovers",
        "module": "divisome_z_ring_septation_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "SulA and ZapE-family candidates enter through broad cell-division terms and are first-pass curated as divisome/septation regulatory or candidate side context.",
    },
    "vacj_phospholipid_asymmetry_context": {
        "label": "VacJ phospholipid asymmetry context",
        "module": "mla_phospholipid_transport_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "VacJ/MlaA-family lipoprotein context is first-pass curated with the outer-membrane phospholipid-asymmetry/Mla boundary.",
    },
    "apbe_fmn_transferase_spillover": {
        "label": "ApbE/FMN-transferase envelope spillover",
        "module": "ccm_heme_export_cytochrome_c_maturation_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "Membrane/lipoprotein keyword spillover for ApbE-like FAD:protein FMN transferase context; PP_2150 is first-pass curated in the Ccm/cytochrome-redox boundary module as related envelope flavoprotein maturation context.",
    },
    "outer_membrane_barrel_channel_autotransporter_context": {
        "label": "Outer-membrane barrels, channels, and autotransporters",
        "module": "transport_envelope_spillover_boundary",
        "action": "NEW_OR_REUSE_BOUNDARY",
        "status": "CURATED",
        "note": "OmpA/MotB-domain proteins, Tsx channels, autotransporters, and an N4-receptor-like outer-membrane subunit; all 8 are first-pass curated and represented in the transport/envelope spillover boundary module.",
    },
    "named_outer_membrane_lipoprotein_families": {
        "label": "Named outer-membrane lipoprotein families",
        "module": "transport_envelope_spillover_boundary",
        "action": "NEW_OR_REUSE_BOUNDARY",
        "status": "CURATED",
        "note": "Named or family-resolved outer-membrane lipoproteins such as SlyB, OprI, Blc, OsmE, YaiW, UxpA, and Lppl-like proteins; all 9 are first-pass curated and represented in the transport/envelope spillover boundary module.",
    },
    "domain_resolved_lipoprotein_spillovers": {
        "label": "Domain-resolved lipoprotein spillovers",
        "module": "transport_envelope_spillover_boundary",
        "action": "NEW_OR_REUSE_BOUNDARY",
        "status": "CURATED",
        "note": "Lipoprotein/name-keyword entries with InterPro/Pfam/GO signal but no compact pathway assignment; all 30 are first-pass curated and represented in the transport/envelope spillover boundary module.",
    },
    "generic_lipoprotein_signal_spillovers": {
        "label": "Generic lipoprotein/signal-peptide spillovers",
        "module": "transport_envelope_spillover_boundary",
        "action": "NEW_OR_REUSE_BOUNDARY",
        "status": "CURATED",
        "note": "Generic lipoprotein or signal-peptide entries with little functional signal; all 30 are first-pass curated as broad membrane/envelope context in the transport/envelope spillover boundary module.",
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


def norm(value: str) -> str:
    return (value or "").casefold()


def has_any(text: str, terms: tuple[str, ...]) -> bool:
    lowered = norm(text)
    return any(term in lowered for term in terms)


def ids(row: dict[str, str], field: str) -> set[str]:
    return {part.strip() for part in row.get(field, "").split(";") if part.strip()}


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


def assign_bucket(row: dict[str, str]) -> str:
    gene = row["suggested_review_name"]
    product = row["protein_name"]
    go = ids(row, "go_ids")
    interpro = ids(row, "interpro_ids")
    pfam = ids(row, "pfam_ids")
    keywords = row.get("keywords", "")

    if gene in {"lptD", "lptE"}:
        return "lpt_outer_membrane_lps_transport_context"

    if gene == "maa":
        return "maltose_acetyltransferase_lipid_a_keyword_spillover"

    if gene in {"PP_3016", "PP_3134"} or has_any(
        product + " " + keywords,
        ("lipopolysaccharide core", "lipid a"),
    ):
        return "lps_core_lipid_a_biosynthesis_context"

    peptidoglycan_go = {
        "GO:0000270",
        "GO:0008745",
        "GO:0008932",
        "GO:0008933",
        "GO:0009002",
        "GO:0009252",
        "GO:0009253",
        "GO:0009254",
        "GO:0016998",
        "GO:0071555",
    }
    if go & peptidoglycan_go or has_any(
        product + " " + keywords,
        (
            "n-acetylmuramoyl",
            "murein",
            "peptidoglycan",
            "cell wall hydrolase",
            "cell wall assembly",
            "d-alanyl-d-alanine",
            "csiv",
            "rlpa",
            "cell wall biogenesis/degradation",
        ),
    ):
        return "peptidoglycan_turnover_remodeling_candidates"

    if gene in {"sulA", "PP_2199", "PP_2352"} or has_any(product, ("cell division", "zape")):
        return "cell_division_regulatory_spillovers"

    if gene == "vacJ":
        return "vacj_phospholipid_asymmetry_context"

    if gene == "PP_2150" or has_any(product, ("fmn transferase", "flavin transferase")):
        return "apbe_fmn_transferase_spillover"

    if has_any(
        product,
        (
            "ompa",
            "motb domain",
            "autotransporter",
            "nucleoside-specific outer membrane channel",
            "bacteriophage n4 receptor",
        ),
    ) or pfam & {"PF00691", "PF03502", "PF03797", "PF18883"}:
        return "outer_membrane_barrel_channel_autotransporter_context"

    if gene in {"uxpA", "slyB", "oprI", "yaiW", "PP_3236", "PP_4032", "PP_4855", "PP_5037", "PP_5226"} or has_any(
        product,
        (
            "outer membrane lipoprotein",
            "major outer membrane lipoprotein",
            "lipoprotein opri",
            "osmotically-inducible lipoprotein",
            "lipoprotein required for swarming",
            "lppl family",
        ),
    ):
        return "named_outer_membrane_lipoprotein_families"

    if go or interpro or pfam:
        return "domain_resolved_lipoprotein_spillovers"

    return "generic_lipoprotein_signal_spillovers"


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


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


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

    rows = [make_row(source, assign_bucket(source)) for source in source_rows]
    if len({row["gene"] for row in rows}) != len(rows):
        raise SystemExit("Duplicate gene rows in partition output")

    write_rows(OUT_TSV, rows)

    by_bucket: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_bucket[row["partition_bucket"]].append(row)

    counts = Counter(row["partition_bucket"] for row in rows)
    examples: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        if len(examples[row["partition_bucket"]]) < 8:
            examples[row["partition_bucket"]].append(row["gene"])

    lines = [
        "---",
        'title: "PSEPK cell-envelope/division functional-bucket partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK cell-envelope/division functional-bucket partition",
        "",
        "The `module:cell_envelope_division` bucket is a UniProt",
        "name/keyword umbrella. It mixes Lpt/LPS outer-membrane assembly,",
        "lipid-A/LPS-core biosynthesis, peptidoglycan turnover, cell-division",
        "regulatory spillovers, VacJ/MlaA phospholipid-asymmetry context,",
        "ApbE-like envelope flavinylation, outer-membrane barrels/channels,",
        "and many domain-resolved or generic lipoprotein spillovers.",
        "",
        "## Outputs",
        "",
        f"- Source table: `{PARTITION_TSV.relative_to(ROOT)}`",
        f"- Full partition table: `{OUT_TSV.relative_to(ROOT)}`",
        "",
        "## Partition Summary",
        "",
        "| Bucket | Genes | Proposed module | Action | Status | Example genes |",
        "|---|---:|---|---|---|---|",
    ]
    for bucket_id in BUCKET_ORDER:
        info = BUCKETS[bucket_id]
        module = info["module"] or "(none)"
        example_text = ", ".join(f"`{gene}`" for gene in examples[bucket_id])
        lines.append(
            f"| `{bucket_id}` | {counts[bucket_id]} | `{module}` | "
            f"{info['action']} | {info['status']} | {example_text} |"
        )

    lines.extend(
        [
            "",
            "## Working Decisions",
            "",
            "- Do not curate the 98-gene functional bucket as one satisfiable module.",
            "- Treat LptD/LptE as already curated Lpt/LPS-transport context.",
            "- The first follow-up batch is the LPS-core/lipid-A split: PP_3016",
            "  and PP_3134 connect to the existing `lipopolysaccharide_biosynthesis`",
            "  module, while maa is recorded separately as a lipid-A-keyword spillover",
            "  whose first-pass review supports maltose O-acetyltransferase activity.",
            "- The cell-division regulatory spillover split is complete: sulA,",
            "  PP_2199, and PP_2352 connect to the existing",
            "  `divisome_z_ring_septation_boundary` module as SulA regulatory",
            "  context and candidate ZapE-like ATPases.",
            "- The VacJ/MlaA singleton split is complete: vacJ connects to the",
            "  existing `mla_phospholipid_transport_boundary` module as MlaA-family",
            "  lipoprotein context for intermembrane phospholipid transfer.",
            "- The ApbE/FMNylylation singleton split is complete: PP_2150 connects",
            "  to the existing `ccm_heme_export_cytochrome_c_maturation_boundary`",
            "  module as related envelope flavoprotein maturation context rather",
            "  than as a CcmABCD heme-export component.",
            "- The peptidoglycan turnover/remodeling split is complete: amiD,",
            "  ampD, rlpA/Q88PC1, mltF, PP_1325, PP_2147, PP_3562, pbpG,",
            "  rlpA/Q88DM1, PP_4971, and PP_5354 connect to the existing",
            "  `peptidoglycan_biosynthesis` module as turnover, remodeling,",
            "  binding, or cell-wall assembly candidates.",
            "- The outer-membrane barrel/channel/autotransporter, named",
            "  lipoprotein-family, domain-resolved lipoprotein, and generic",
            "  lipoprotein/signal-peptide splits are complete and represented in",
            "  the existing `transport_envelope_spillover_boundary` module.",
            "- The generic lipoprotein/signal-peptide set remains low-specificity",
            "  in the module: all 30 entries are broad membrane/envelope candidates",
            "  without pathway, partner, or molecular-function assignments.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    for bucket_id in BUCKET_ORDER:
        info = BUCKETS[bucket_id]
        bucket_rows = by_bucket[bucket_id]
        stem = f"module_cell_envelope_division_{bucket_id}"
        write_rows(BATCH_DIR / f"{stem}.tsv", bucket_rows)
        write_batch_md(
            BATCH_DIR / f"{stem}.md",
            f"PSEPK cell-envelope/division: {info['label']}",
            bucket_rows,
            info["note"],
        )

    print(f"Wrote {OUT_TSV.relative_to(ROOT)} with {len(rows)} rows")
    for bucket_id in BUCKET_ORDER:
        print(f"{bucket_id}: {counts[bucket_id]}")


if __name__ == "__main__":
    main()
