#!/usr/bin/env python3
"""Partition the PSEPK chromosome/cell-cycle functional bucket."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PARTITION_TSV = ROOT / "projects/P_PUTIDA/data/psepk_pathway_partition.tsv"
OUT_TSV = ROOT / "projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_partition.tsv"
OUT_MD = ROOT / "projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_partition.md"
MIN_TSV = ROOT / "projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_min_system.tsv"
MIN_MD = ROOT / "projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_min_system.md"
DIV_TSV = ROOT / "projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_divisome.tsv"
DIV_MD = ROOT / "projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_divisome.md"
XER_TSV = ROOT / "projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_xer_ftsk.tsv"
XER_MD = ROOT / "projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_xer_ftsk.md"
TOL_TSV = ROOT / "projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_tol_pal.tsv"
TOL_MD = ROOT / "projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_tol_pal.md"
PAR_TSV = ROOT / "projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_partition_condensation.tsv"
PAR_MD = ROOT / "projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_partition_condensation.md"
SPILL_TSV = ROOT / "projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_spillovers.tsv"
SPILL_MD = ROOT / "projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_spillovers.md"
GENE_ROOT = ROOT / "genes/PSEPK"
SOURCE_BUCKET = "module:chromosome_partition_cell_cycle"


BUCKETS = {
    "chromosome_partition_condensation_boundary": {
        "label": "Chromosome partition and condensation boundary",
        "module": "chromosome_partition_condensation_boundary",
        "action": "COMPLETED_SUBMODULE",
        "note": "ParB/PP_0002 origin partition candidates, MksEF-like candidates, ParA-family side ATPases, and Smc-ScpAB condensation/segregation machinery; first-pass reviews and module are complete with PP_0002 promoted from unknown.",
        "genes": [
            "parB",
            "PP_0693",
            "PP_0694",
            "PP_2161",
            "PP_2412",
            "PP_3700",
            "smc",
            "PP_4334",
            "PP_4497",
            "scpA",
            "PP_5070",
        ],
    },
    "chromosome_dimer_resolution_and_dna_translocation_boundary": {
        "label": "Chromosome dimer resolution and DNA translocation",
        "module": "chromosome_dimer_resolution_dna_translocation_boundary",
        "action": "COMPLETED_SUBMODULE",
        "note": "XerC/XerD recombinases, FtsK DNA translocase, and a phage-integrase-family side candidate; first-pass reviews and module are complete.",
        "genes": ["xerD", "PP_2841", "ftsK", "xerC"],
    },
    "divisome_z_ring_and_septation_boundary": {
        "label": "Divisome, Z-ring, and septation boundary",
        "module": "divisome_z_ring_septation_boundary",
        "action": "COMPLETED_SUBMODULE",
        "note": "FtsZ/FtsA/ZipA/FtsQLB/DedD/Zap proteins and EngB-like septation context; first-pass reviews and a boundary module are complete.",
        "genes": [
            "engB",
            "PP_1309",
            "zapE",
            "ftsL",
            "ftsQ",
            "ftsA",
            "ftsZ",
            "ftsB",
            "dedD",
            "zipA",
            "PP_5090",
            "PP_5202",
        ],
    },
    "min_system_septum_site_selection_boundary": {
        "label": "MinCDE septum-site selection",
        "module": "min_system_septum_site_selection_boundary",
        "action": "COMPLETED_SUBMODULE",
        "note": "MinC, MinD, and MinE form a coherent septum-site-selection boundary module; first-pass reviews and module are complete.",
        "genes": ["minE", "minD", "minC"],
    },
    "tol_pal_cell_division_envelope_coordination_boundary": {
        "label": "Tol-Pal envelope/division coordination",
        "module": "tol_pal_cell_division_envelope_coordination_boundary",
        "action": "COMPLETED_SUBMODULE",
        "note": "TolQ/TolR/TolB/Pal/CpoB envelope coordination and division-associated outer-membrane constriction context; first-pass reviews and module are complete with TolA promoted from the transport/membrane bucket.",
        "genes": ["tolQ", "tolR", "tolB", "pal", "cpoB"],
    },
    "side_spillover_general_cell_cycle_terms": {
        "label": "General cell-cycle keyword spillovers",
        "module": "",
        "action": "COMPLETED_REASSIGN_OR_KEEP_OUT",
        "note": "DNA ligase and trigger factor enter through broad cell-cycle/cell-division keywords; first-pass reviews are complete and route PP_1105 to DNA ligase/repair context and tig to chaperone/protein-folding context.",
        "genes": ["PP_1105", "tig"],
    },
}

PROMOTED_TOL_PAL_GENES = {
    "tolA": "Promoted from module:transport_membrane_efflux as the missing core Tol-Pal connector component; chromatin/nucleosome electronic spillovers removed.",
}

PROMOTED_CHROMOSOME_PARTITION_GENES = {
    "PP_0002": "Promoted from unknown:function_unknown as the origin-proximal Soj/ParA-like DNA-partitioning ATPase candidate adjacent to parB.",
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


def make_row(source: dict[str, str], bucket_id: str, note_override: str | None = None) -> dict[str, str]:
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
        "notes": note_override or info["note"],
        "review_status": review_status(gene),
        "curation_status": curation_status(gene),
        "asta_research_status": asta_research_status(gene),
    }


def main() -> None:
    source_rows = [
        row
        for row in csv.DictReader(PARTITION_TSV.open(encoding="utf-8"), delimiter="\t")
        if row["primary_bucket_id"] == SOURCE_BUCKET
    ]
    all_rows_by_gene = {
        row["suggested_review_name"]: row
        for row in csv.DictReader(PARTITION_TSV.open(encoding="utf-8"), delimiter="\t")
    }
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

    rows: list[dict[str, str]] = []
    for source in source_rows:
        gene = source["suggested_review_name"]
        bucket_id = assigned[gene]
        rows.append(make_row(source, bucket_id))

    write_rows(OUT_TSV, rows)
    min_rows = [row for row in rows if row["partition_bucket"] == "min_system_septum_site_selection_boundary"]
    write_rows(MIN_TSV, min_rows)
    div_rows = [row for row in rows if row["partition_bucket"] == "divisome_z_ring_and_septation_boundary"]
    write_rows(DIV_TSV, div_rows)
    xer_rows = [
        row
        for row in rows
        if row["partition_bucket"] == "chromosome_dimer_resolution_and_dna_translocation_boundary"
    ]
    write_rows(XER_TSV, xer_rows)
    tol_rows = [row for row in rows if row["partition_bucket"] == "tol_pal_cell_division_envelope_coordination_boundary"]
    for gene, note in PROMOTED_TOL_PAL_GENES.items():
        tol_rows.append(make_row(all_rows_by_gene[gene], "tol_pal_cell_division_envelope_coordination_boundary", note))
    write_rows(TOL_TSV, tol_rows)
    par_rows = [row for row in rows if row["partition_bucket"] == "chromosome_partition_condensation_boundary"]
    for gene, note in PROMOTED_CHROMOSOME_PARTITION_GENES.items():
        par_rows.append(make_row(all_rows_by_gene[gene], "chromosome_partition_condensation_boundary", note))
    write_rows(PAR_TSV, par_rows)
    spill_rows = [row for row in rows if row["partition_bucket"] == "side_spillover_general_cell_cycle_terms"]
    write_rows(SPILL_TSV, spill_rows)

    counts = Counter(assigned.values())
    examples: dict[str, list[str]] = defaultdict(list)
    for gene, bucket_id in assigned.items():
        if len(examples[bucket_id]) < 8:
            examples[bucket_id].append(gene)

    lines = [
        "---",
        'title: "PSEPK chromosome/cell-cycle functional-bucket partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK chromosome/cell-cycle functional-bucket partition",
        "",
        "The `module:chromosome_partition_cell_cycle` bucket is a functional",
        "umbrella assembled from UniProt names and keywords. It mixes chromosome",
        "partition/condensation proteins, divisome/septation proteins, the MinCDE",
        "septum-site-selection system, Tol-Pal envelope/division coordination,",
        "DNA dimer resolution/translocation, and two broad keyword spillovers.",
        "",
        "## Outputs",
        "",
        f"- Source table: `{PARTITION_TSV.relative_to(ROOT)}`",
        f"- Full partition table: `{OUT_TSV.relative_to(ROOT)}`",
        f"- Completed Min-system batch: `{MIN_TSV.relative_to(ROOT)}`",
        f"- Completed divisome/Z-ring batch: `{DIV_TSV.relative_to(ROOT)}`",
        f"- Completed Xer/FtsK batch: `{XER_TSV.relative_to(ROOT)}`",
        f"- Completed Tol-Pal batch: `{TOL_TSV.relative_to(ROOT)}`",
        f"- Completed chromosome partition/condensation batch: `{PAR_TSV.relative_to(ROOT)}`",
        f"- Completed broad spillover batch: `{SPILL_TSV.relative_to(ROOT)}`",
        "",
        "## Partition Summary",
        "",
        "| Bucket | Genes | Proposed module | Action | Example genes |",
        "|---|---:|---|---|---|",
    ]
    for bucket_id, info in BUCKETS.items():
        module = info["module"] or "(none)"
        lines.append(
            f"| `{bucket_id}` | {counts[bucket_id]} | `{module}` | "
            f"{info['action']} | {', '.join(f'`{g}`' for g in examples[bucket_id])} |"
        )
    lines.extend(
        [
            "",
            "## Working Decisions",
            "",
            "- Do not curate the 37-gene functional bucket as one satisfiable module.",
            "- Treat MinCDE as the first completed sub-batch because minC, minD,",
            "  and minE are adjacent, coherent, Asta-backed, and have direct",
            "  septum-site-selection GO evidence.",
            "- Keep Tol-Pal, divisome/Z-ring, chromosome partition/condensation,",
            "  and Xer/FtsK DNA-resolution/translocation as separate sub-batches.",
            "- Keep PP_1105 and tig out of this module unless future evidence ties",
            "  them directly to a cell-cycle mechanism beyond broad keyword context.",
            "",
            "## Completed Sub-batches",
            "",
            "- `min_system_septum_site_selection_boundary`: minC, minD, and minE",
            "  are fetched, Asta-backed, first-pass curated, validated, and",
            "  represented in `modules/min_system_septum_site_selection_boundary.yaml`.",
            "- `divisome_z_ring_and_septation_boundary`: engB, PP_1309, zapE,",
            "  ftsL, ftsQ, ftsA, ftsZ, ftsB, dedD, zipA, PP_5090, and PP_5202",
            "  are fetched or reused, Asta-backed, first-pass curated, validated,",
            "  and represented in `modules/divisome_z_ring_septation_boundary.yaml`.",
            "- `chromosome_dimer_resolution_dna_translocation_boundary`: xerC,",
            "  xerD, ftsK, and PP_2841 are fetched, Asta-backed, first-pass",
            "  curated, validated, and represented in",
            "  `modules/chromosome_dimer_resolution_dna_translocation_boundary.yaml`.",
            "- `tol_pal_cell_division_envelope_coordination_boundary`: tolQ,",
            "  tolR, tolA, tolB, pal, and cpoB are fetched, Asta-backed,",
            "  first-pass curated, validated, and represented in",
            "  `modules/tol_pal_cell_division_envelope_coordination_boundary.yaml`.",
            "- `chromosome_partition_condensation_boundary`: parB, PP_0002,",
            "  PP_0693, PP_0694, PP_2161, PP_2412, PP_3700, smc, PP_4334,",
            "  PP_4497, scpA, and PP_5070 are fetched, Asta-backed,",
            "  first-pass curated, validated, and represented in",
            "  `modules/chromosome_partition_condensation_boundary.yaml`.",
            "- `side_spillover_general_cell_cycle_terms`: PP_1105 and tig are",
            "  fetched or reused, Asta-backed, first-pass curated, validated,",
            "  and intentionally kept outside a chromosome/cell-cycle module.",
            "",
            "## Next Steps",
            "",
            "- No primary genes remain in this functional bucket for first-pass",
            "  curation; future work should revisit unresolved candidate roles",
            "  only as deeper biology questions.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    min_lines = [
        "---",
        'title: "PSEPK MinCDE septum-site-selection batch"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "genes: [minC, minD, minE]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK MinCDE septum-site-selection batch",
        "",
        "This completed sub-batch covers the MinCDE division-site-selection",
        "system from the larger `module:chromosome_partition_cell_cycle`",
        "functional bucket.",
        "",
        "## Outputs",
        "",
        f"- Batch table: `{MIN_TSV.relative_to(ROOT)}`",
        "- Module: `modules/min_system_septum_site_selection_boundary.yaml`",
        "",
        "## Gene Status",
        "",
        "| Gene | Ordered locus | UniProt | Curation | Asta |",
        "|---|---|---|---|---|",
    ]
    for row in min_rows:
        min_lines.append(
            f"| `{row['gene']}` | `{row['ordered_locus']}` | `{row['uniprot_accession']}` | "
            f"{row['curation_status']} | {row['asta_research_status']} |"
        )
    min_lines.extend(
        [
            "",
            "## Curation Notes",
            "",
            "- minC is curated as the septum-site-selection inhibitor that regulates",
            "  cell septum assembly by preventing inappropriate polar FtsZ/septum",
            "  formation.",
            "- minD is curated as the ParA/MinD-family ATPase at the cytoplasmic side",
            "  of the plasma membrane that negatively regulates cell division at",
            "  incorrect sites.",
            "- minE is curated as the topological specificity factor that permits",
            "  division at internal sites while retaining polar inhibition.",
        ]
    )
    MIN_MD.write_text("\n".join(min_lines) + "\n", encoding="utf-8")

    div_lines = [
        "---",
        'title: "PSEPK divisome/Z-ring/septation batch"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "genes: [engB, PP_1309, zapE, ftsL, ftsQ, ftsA, ftsZ, ftsB, dedD, zipA, PP_5090, PP_5202]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK divisome/Z-ring/septation batch",
        "",
        "This completed sub-batch covers the FtsZ ring, membrane anchors,",
        "FtsB-FtsL-FtsQ subcomplex, Z-ring accessory proteins, EngB septation",
        "context, and SPOR-domain peptidoglycan-binding septal factors from the",
        "larger `module:chromosome_partition_cell_cycle` functional bucket.",
        "",
        "## Outputs",
        "",
        f"- Batch table: `{DIV_TSV.relative_to(ROOT)}`",
        "- Module: `modules/divisome_z_ring_septation_boundary.yaml`",
        "",
        "## Gene Status",
        "",
        "| Gene | Ordered locus | UniProt | Curation | Asta |",
        "|---|---|---|---|---|",
    ]
    for row in div_rows:
        div_lines.append(
            f"| `{row['gene']}` | `{row['ordered_locus']}` | `{row['uniprot_accession']}` | "
            f"{row['curation_status']} | {row['asta_research_status']} |"
        )
    div_lines.extend(
        [
            "",
            "## Curation Notes",
            "",
            "- ftsZ remains the central Z-ring GTPase from the existing curated review.",
            "- ftsA and zipA are retained as membrane/Z-ring anchoring factors.",
            "- ftsB, ftsL, and ftsQ are retained as the FtsB-FtsL-FtsQ divisome",
            "  subcomplex.",
            "- PP_5202 is retained as a ZapA-family Z-ring factor, and the",
            "  TreeGrafter septin-ring assembly annotation is removed as a bacterial",
            "  Z-ring/septation over-propagation.",
            "- dedD and PP_5090 are retained as SPOR/RlpA-like peptidoglycan-binding",
            "  septal or cell-division boundary factors.",
        ]
    )
    DIV_MD.write_text("\n".join(div_lines) + "\n", encoding="utf-8")

    xer_lines = [
        "---",
        'title: "PSEPK Xer/FtsK chromosome dimer resolution batch"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "genes: [xerC, xerD, ftsK, PP_2841]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK Xer/FtsK chromosome dimer resolution batch",
        "",
        "This completed sub-batch covers the XerC/XerD chromosome dimer",
        "resolution system, the FtsK septal DNA translocase, and one related",
        "integrase-family side candidate from the larger",
        "`module:chromosome_partition_cell_cycle` functional bucket.",
        "",
        "## Outputs",
        "",
        f"- Batch table: `{XER_TSV.relative_to(ROOT)}`",
        "- Module: `modules/chromosome_dimer_resolution_dna_translocation_boundary.yaml`",
        "",
        "## Gene Status",
        "",
        "| Gene | Ordered locus | UniProt | Curation | Asta |",
        "|---|---|---|---|---|",
    ]
    for row in xer_rows:
        xer_lines.append(
            f"| `{row['gene']}` | `{row['ordered_locus']}` | `{row['uniprot_accession']}` | "
            f"{row['curation_status']} | {row['asta_research_status']} |"
        )
    xer_lines.extend(
        [
            "",
            "## Curation Notes",
            "",
            "- xerC and xerD are curated as the core cytoplasmic tyrosine",
            "  recombinase subunits that resolve chromosome dimers and support",
            "  chromosome segregation.",
            "- ftsK is curated as the septal membrane DNA translocase that couples",
            "  cell division with chromosome segregation and activates XerCD-mediated",
            "  chromosome unlinking.",
            "- PP_2841 is retained as a predicted tyrosine recombinase/integrase-family",
            "  boundary candidate, not as a core XerCD-FtsK chromosome dimer",
            "  resolution component.",
            "- Falcon module research was attempted for the completed module, but",
            "  Edison returned HTTP 402 before producing",
            "  `modules/chromosome_dimer_resolution_dna_translocation_boundary-deep-research-falcon.md`.",
        ]
    )
    XER_MD.write_text("\n".join(xer_lines) + "\n", encoding="utf-8")

    tol_lines = [
        "---",
        'title: "PSEPK Tol-Pal envelope/division coordination batch"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "genes: [tolQ, tolR, tolA, tolB, pal, cpoB]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK Tol-Pal envelope/division coordination batch",
        "",
        "This completed sub-batch covers the TolQ/TolR/TolA/TolB/Pal",
        "envelope-spanning Tol-Pal machinery and the adjacent CpoB",
        "periplasmic envelope-constriction coordinator. TolA was promoted",
        "from `module:transport_membrane_efflux` because it is a missing core",
        "Tol-Pal component needed for module satisfiability.",
        "",
        "## Outputs",
        "",
        f"- Batch table: `{TOL_TSV.relative_to(ROOT)}`",
        "- Module: `modules/tol_pal_cell_division_envelope_coordination_boundary.yaml`",
        "",
        "## Gene Status",
        "",
        "| Gene | Ordered locus | UniProt | Curation | Asta |",
        "|---|---|---|---|---|",
    ]
    for row in tol_rows:
        tol_lines.append(
            f"| `{row['gene']}` | `{row['ordered_locus']}` | `{row['uniprot_accession']}` | "
            f"{row['curation_status']} | {row['asta_research_status']} |"
        )
    tol_lines.extend(
        [
            "",
            "## Curation Notes",
            "",
            "- tolQ and tolR are retained as inner-membrane Tol-Pal",
            "  energy-coupling components involved in cell division; broad protein",
            "  transport/import and generic transporter annotations are non-core or",
            "  over-propagated.",
            "- tolA was promoted from the transport/membrane bucket as the missing",
            "  core Tol-Pal connector. Nucleosome, nucleosome assembly, DNA binding,",
            "  and structural constituent of chromatin annotations were removed as",
            "  H1/H5-like InterPro over-propagations.",
            "- tolB and pal form the periplasmic/outer-membrane Tol-Pal arm; Pal's",
            "  core molecular function remains peptidoglycan binding.",
            "- cpoB is retained as an adjacent periplasmic coordinator of",
            "  peptidoglycan synthesis and outer-membrane constriction during",
            "  FtsZ-dependent cytokinesis, not as a Tol-Pal core subunit.",
            "- Falcon module research was attempted for the completed module, but",
            "  Edison returned HTTP 402 before producing",
            "  `modules/tol_pal_cell_division_envelope_coordination_boundary-deep-research-falcon.md`.",
        ]
    )
    TOL_MD.write_text("\n".join(tol_lines) + "\n", encoding="utf-8")

    par_lines = [
        "---",
        'title: "PSEPK chromosome partition/condensation batch"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "genes: [parB, PP_0002, PP_0693, PP_0694, PP_2161, PP_2412, PP_3700, smc, PP_4334, PP_4497, scpA, PP_5070]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK chromosome partition/condensation batch",
        "",
        "This completed sub-batch covers the ParB/PP_0002 origin-region",
        "partition candidates, MksEF-like condensation candidates, ParA-family",
        "side ATPases, and the Smc-ScpA-ScpB condensin machinery. PP_0002 was",
        "promoted from `unknown:function_unknown` because it is immediately",
        "adjacent to parB and carries Soj/ParA-like DNA-partitioning ATPase",
        "signatures.",
        "",
        "## Outputs",
        "",
        f"- Batch table: `{PAR_TSV.relative_to(ROOT)}`",
        "- Module: `modules/chromosome_partition_condensation_boundary.yaml`",
        "",
        "## Gene Status",
        "",
        "| Gene | Ordered locus | UniProt | Curation | Asta |",
        "|---|---|---|---|---|",
    ]
    for row in par_rows:
        par_lines.append(
            f"| `{row['gene']}` | `{row['ordered_locus']}` | `{row['uniprot_accession']}` | "
            f"{row['curation_status']} | {row['asta_research_status']} |"
        )
    par_lines.extend(
        [
            "",
            "## Curation Notes",
            "",
            "- parB is retained as the origin-region ParB/Spo0J-family DNA-binding",
            "  chromosome partition protein; the sporulation process annotation is",
            "  removed as an inappropriate family-level spillover for P. putida.",
            "- PP_0002 is promoted as the missing Soj/ParA-like DNA-partitioning",
            "  ATPase candidate next to parB, but its KT2440 role remains",
            "  experimentally unresolved.",
            "- PP_0693 and PP_0694 are treated as MksF/MksE-like condensin",
            "  candidates rather than canonical ParA ATPases.",
            "- PP_2412, PP_3700, PP_4334, and PP_5070 remain candidate ParA-family",
            "  partition ATPases; the review avoids assigning all of them to the",
            "  core chromosomal ParAB system without partner/context evidence.",
            "- smc, scpA, and PP_4497 form the strongest Smc-ScpA-ScpB",
            "  condensation/segregation submodule. The smc sister-chromatid",
            "  cohesion annotation is modified toward chromosome organization and",
            "  chromosome condensation.",
            "- Falcon module research was attempted for the completed module, but",
            "  Edison returned HTTP 402 before producing",
            "  `modules/chromosome_partition_condensation_boundary-deep-research-falcon.md`.",
        ]
    )
    PAR_MD.write_text("\n".join(par_lines) + "\n", encoding="utf-8")

    spill_lines = [
        "---",
        'title: "PSEPK chromosome/cell-cycle broad spillovers"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "genes: [PP_1105, tig]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK chromosome/cell-cycle broad spillovers",
        "",
        "This completed spillover batch covers the two genes that entered",
        "`module:chromosome_partition_cell_cycle` only through broad cell-cycle",
        "or cell-division keywords. They are reviewed here to close the",
        "functional bucket, but neither is represented in a chromosome/cell-cycle",
        "module.",
        "",
        "## Outputs",
        "",
        f"- Batch table: `{SPILL_TSV.relative_to(ROOT)}`",
        "- Module: none; both genes are routed to more appropriate pathway contexts.",
        "",
        "## Gene Status",
        "",
        "| Gene | Ordered locus | UniProt | Curation | Asta | Routing |",
        "|---|---|---|---|---|---|",
    ]
    routing = {
        "PP_1105": "DNA ligase / DNA repair and DNA metabolism",
        "tig": "Trigger factor chaperone / cotranslational protein folding",
    }
    for row in spill_rows:
        spill_lines.append(
            f"| `{row['gene']}` | `{row['ordered_locus']}` | `{row['uniprot_accession']}` | "
            f"{row['curation_status']} | {row['asta_research_status']} | {routing[row['gene']]} |"
        )
    spill_lines.extend(
        [
            "",
            "## Curation Notes",
            "",
            "- PP_1105 is an ATP-dependent DNA ligase (EC 6.5.1.1). Its",
            "  supported core role is DNA ligase chemistry in DNA repair and",
            "  related DNA metabolism, not a chromosome/cell-cycle module role.",
            "- tig encodes trigger factor, the ribosome-associated FKBP-type",
            "  PPIase/chaperone for de novo cotranslational protein folding.",
            "  The existing review keeps the broad protein-transport term as",
            "  non-core and removes protein unfolding as mis-aspected.",
            "- No module-level Falcon run is needed for this spillover bucket",
            "  because the two genes are deliberately reassigned or kept out.",
        ]
    )
    SPILL_MD.write_text("\n".join(spill_lines) + "\n", encoding="utf-8")

    print(f"Wrote {OUT_TSV.relative_to(ROOT)}")
    print(f"Wrote {OUT_MD.relative_to(ROOT)}")
    print(f"Wrote {MIN_TSV.relative_to(ROOT)}")
    print(f"Wrote {MIN_MD.relative_to(ROOT)}")
    print(f"Wrote {DIV_TSV.relative_to(ROOT)}")
    print(f"Wrote {DIV_MD.relative_to(ROOT)}")
    print(f"Wrote {XER_TSV.relative_to(ROOT)}")
    print(f"Wrote {XER_MD.relative_to(ROOT)}")
    print(f"Wrote {TOL_TSV.relative_to(ROOT)}")
    print(f"Wrote {TOL_MD.relative_to(ROOT)}")
    print(f"Wrote {PAR_TSV.relative_to(ROOT)}")
    print(f"Wrote {PAR_MD.relative_to(ROOT)}")
    print(f"Wrote {SPILL_TSV.relative_to(ROOT)}")
    print(f"Wrote {SPILL_MD.relative_to(ROOT)}")
    for bucket_id, info in BUCKETS.items():
        print(f"{bucket_id}\t{counts[bucket_id]}\t{info['module']}")


if __name__ == "__main__":
    main()
