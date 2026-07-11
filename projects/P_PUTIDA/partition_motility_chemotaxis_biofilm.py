#!/usr/bin/env python3
"""Partition the PSEPK motility/chemotaxis/biofilm functional bucket."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PARTITION_TSV = ROOT / "projects/P_PUTIDA/data/psepk_pathway_partition.tsv"
OUT_TSV = ROOT / "projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_partition.tsv"
OUT_MD = ROOT / "projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_partition.md"
GENE_ROOT = ROOT / "genes/PSEPK"
SOURCE_BUCKET = "module:motility_chemotaxis_biofilm"


BUCKETS = {
    "type_iv_pilus_biogenesis_boundary": {
        "label": "Type IV pilus biogenesis and assembly",
        "module": "type_iv_pilus_biogenesis_boundary",
        "action": "NEW_SUBMODULE",
        "status": "CURATED",
        "note": "Type IV pilus assembly, alignment, outer-membrane secretin, and envelope platform candidates curated as a dedicated T4P biogenesis boundary rather than as generic motility.",
        "genes": [
            "PP_0608",
            "PP_0609",
            "PP_0610",
            "pilE",
            "pilC",
            "pilF",
            "PP_3480",
            "PP_3481",
            "pilQ",
            "PP_5081",
            "pilN",
            "PP_5083",
        ],
    },
    "fimbrial_type1_surface_adhesion_extension": {
        "label": "Fimbrial/type-I-pilus surface adhesion extension",
        "module": "pili_surface_adhesion_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "Fimbrial structural/subunit candidates adjacent to the already curated FimD/PP_1890 chaperone-usher pair; extend or reuse the existing pili/surface-adhesion boundary.",
        "genes": ["PP_1888", "fimI"],
    },
    "hcp_t6ss_product_name_spillover": {
        "label": "Hcp/T6SS product-name spillover",
        "module": "bacterial_secretion_system_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "PP_0655 enters the motility bucket through a generic fimbrial-protein-related product name, but Hcp1-like/T6SS_Hcp domains route it to the bacterial secretion-system boundary.",
        "genes": ["PP_0655"],
    },
    "alginate_envelope_and_lyase_context": {
        "label": "Alginate envelope/export and lyase context",
        "module": "alginate_biosynthesis_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "Alginate-biosynthesis efficiency, export-domain, and alginate-lyase-domain side candidates curated into the existing alginate biosynthesis boundary as context rather than generic motility genes.",
        "genes": ["glmP", "PP_1754", "PP_3350", "PP_3464", "PP_3774"],
    },
    "orphan_mcp_chemotaxis_receptor_candidates": {
        "label": "Orphan MCP chemotaxis receptor candidates",
        "module": "orphan_mcp_aerotaxis_receptors_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "Methyl-accepting chemotaxis transducer candidates with unresolved ligand specificity; curated into the orphan MCP/aerotaxis receptor boundary.",
        "genes": ["PP_2310", "PP_3950", "PP_4888"],
    },
    "sensory_c_di_gmp_pde_spillover": {
        "label": "Sensory c-di-GMP phosphodiesterase spillover",
        "module": "c_di_gmp_turnover_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "PP_2599 entered via a chemotaxis sensory-transducer product name, but GAF/HAMP/HD/PDEase/HD-GYP and cyclic-di-GMP phosphodiesterase-family evidence route it to the c-di-GMP turnover boundary.",
        "genes": ["PP_2599"],
    },
    "dna_binding_response_regulator_spillover": {
        "label": "DNA-binding response-regulator spillover",
        "module": "orphan_two_component_regulators_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "PP_2403 entered through a CheY-like product name, but OmpR/PhoB DNA-binding response-regulator evidence routes it to the orphan/generic two-component-regulator boundary.",
        "genes": ["PP_2403"],
    },
    "chey_like_membrane_accessory_spillovers": {
        "label": "CheY-like and membrane accessory spillovers",
        "module": "chemotaxis_adaptation_accessory_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "PP_3757 is a compact CheY-like receiver-domain candidate; PP_3771 and PP_4331 are low-confidence membrane accessory candidates retained without process-level chemotaxis assertions.",
        "genes": ["PP_3757", "PP_3771", "PP_4331"],
    },
    "outer_membrane_flagellation_name_spillover": {
        "label": "Outer-membrane flagellation-name spillover",
        "module": "transport_envelope_spillover_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "ycfJ entered through a regulator-of-flagellation product name, but outer-membrane lipoprotein/surface-antigen-family evidence routes it to transport/envelope spillover context.",
        "genes": ["ycfJ"],
    },
    "flagellar_export_localization_accessory_spillovers": {
        "label": "Flagellar export/localization/accessory spillovers",
        "module": "flagellar_export_assembly_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "PP_4328, PP_4329, PP_4342, flhF, and PP_4377 are flagellar hook-control, short FlhB-family exporter, FlhG/FleN-family ATPase, FlhF GTPase, and FlaG accessory spillovers routed into the export/assembly boundary.",
        "genes": ["PP_4328", "PP_4329", "PP_4342", "flhF", "PP_4377"],
    },
    "c_di_gmp_flagellar_brake_spillover": {
        "label": "c-di-GMP flagellar brake spillover",
        "module": "flagellar_motor_switch_stator_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": "ycgR is a PilZ-domain c-di-GMP-binding flagellar brake routed to the motor/switch/stator boundary rather than c-di-GMP turnover.",
        "genes": ["ycgR"],
    },
}

FIELDS = [
    "gene",
    "ordered_locus",
    "uniprot_accession",
    "protein_name",
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


def make_row(source: dict[str, str], bucket_id: str) -> dict[str, str]:
    info = BUCKETS[bucket_id]
    gene = source["suggested_review_name"]
    return {
        "gene": gene,
        "ordered_locus": source["ordered_locus"],
        "uniprot_accession": source["uniprot_accession"],
        "protein_name": source["protein_name"],
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

    rows = [make_row(source, assigned[source["suggested_review_name"]]) for source in source_rows]
    write_rows(OUT_TSV, rows)

    counts = Counter(row["partition_bucket"] for row in rows)
    examples: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        if len(examples[row["partition_bucket"]]) < 8:
            examples[row["partition_bucket"]].append(row["gene"])

    lines = [
        "---",
        'title: "PSEPK motility, chemotaxis, pili, and biofilm functional-bucket partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK motility, chemotaxis, pili, and biofilm functional-bucket partition",
        "",
        "The `module:motility_chemotaxis_biofilm` bucket is a UniProt",
        "name/keyword umbrella. It mixes type IV pilus biogenesis, fimbrial",
        "surface-adhesion subunits, alginate envelope/export side candidates,",
        "orphan MCP receptors, a sensory c-di-GMP phosphodiesterase spillover,",
        "a DNA-binding response-regulator spillover, CheY-like/membrane",
        "accessory spillovers, outer-membrane flagellation-name spillover,",
        "flagellar export/localization/accessory spillovers, and c-di-GMP",
        "flagellar brake context.",
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
    for bucket_id, info in BUCKETS.items():
        lines.append(
            f"| `{bucket_id}` | {counts[bucket_id]} | `{info['module']}` | "
            f"{info['action']} | {info['status']} | {', '.join(f'`{g}`' for g in examples[bucket_id])} |"
        )
    lines.extend(
        [
            "",
            "## Working Decisions",
            "",
            "- Do not curate the 35-gene functional bucket as one satisfiable module.",
            "- Reuse completed chemotaxis, flagellar, alginate, and pili/surface-adhesion modules where the functional bucket is a keyword spillover.",
            "- Completed `type_iv_pilus_biogenesis_boundary`: the 12-gene T4P assembly set is curated into `modules/type_iv_pilus_biogenesis_boundary.yaml`, with pilD and pilT retained as explicit hole-filling gaps.",
            "- Completed `fimbrial_type1_surface_adhesion_extension`: PP_1888 and fimI extend the existing FimD/PP_1890 chaperone-usher context in `modules/pili_surface_adhesion_boundary.yaml`.",
            "- Completed `hcp_t6ss_product_name_spillover`: PP_0655 was initially pulled in by a generic fimbrial-protein-related product name, but its Hcp/T6SS domains route it to `modules/bacterial_secretion_system_boundary.yaml`.",
            "- Completed `alginate_envelope_and_lyase_context`: glmP, PP_1754, PP_3350, PP_3464, and PP_3774 are curated into `modules/alginate_biosynthesis_boundary.yaml` as alginate efficiency, export-domain, and lyase-domain boundary context.",
            "- Completed `orphan_mcp_chemotaxis_receptor_candidates`: PP_2310, PP_3950, and PP_4888 are curated into `modules/orphan_mcp_aerotaxis_receptors_boundary.yaml` as ligand-unresolved MCP receptor/transducer candidates.",
            "- Completed `sensory_c_di_gmp_pde_spillover`: PP_2599 was initially pulled in by a chemotaxis sensory-transducer product name, but HD-GYP/HD-PDEase/cyclic-di-GMP phosphodiesterase-family evidence routes it to `modules/c_di_gmp_turnover_boundary.yaml`.",
            "- Completed `dna_binding_response_regulator_spillover`: PP_2403 was initially pulled in by a CheY-like product name, but OmpR/PhoB DNA-binding response-regulator evidence routes it to `modules/orphan_two_component_regulators_boundary.yaml`.",
            "- Completed `chey_like_membrane_accessory_spillovers`: PP_3757, PP_3771, and PP_4331 are curated into `modules/chemotaxis_adaptation_accessory_boundary.yaml` as one compact CheY-like response-regulator candidate and two conservative membrane accessory candidates.",
            "- Completed `outer_membrane_flagellation_name_spillover`: ycfJ is routed to `modules/transport_envelope_spillover_boundary.yaml` as an outer-membrane lipoprotein/surface-antigen-family protein.",
            "- Completed `flagellar_export_localization_accessory_spillovers`: PP_4328, PP_4329, PP_4342, flhF, and PP_4377 are curated into `modules/flagellar_export_assembly_boundary.yaml` as hook-control, export-gate, FlhG/FleN-family, FlhF, and FlaG accessory context.",
            "- Completed `c_di_gmp_flagellar_brake_spillover`: ycgR is routed to `modules/flagellar_motor_switch_stator_boundary.yaml` as a PilZ-domain c-di-GMP-dependent motor brake.",
            "- All 35 motility/chemotaxis/biofilm functional-bucket genes are now first-pass curated.",
            "- Run real Falcon module/pathway commands only after selecting a concrete module; current Edison Falcon access failure mode is HTTP 402.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    for bucket_id, info in BUCKETS.items():
        bucket_rows = [row for row in rows if row["partition_bucket"] == bucket_id]
        stem = f"module_motility_chemotaxis_biofilm_{bucket_id}"
        tsv_path = ROOT / "projects/P_PUTIDA/batches" / f"{stem}.tsv"
        md_path = ROOT / "projects/P_PUTIDA/batches" / f"{stem}.md"
        write_rows(tsv_path, bucket_rows)
        write_batch_md(md_path, f"PSEPK {info['label']}", bucket_rows, info["note"])

    print(f"Wrote {OUT_TSV.relative_to(ROOT)}")
    print(f"Wrote {OUT_MD.relative_to(ROOT)}")
    for bucket_id, info in BUCKETS.items():
        print(f"{bucket_id}\t{counts[bucket_id]}\t{info['module']}\t{info['status']}")


if __name__ == "__main__":
    main()
