#!/usr/bin/env python3
"""Partition the PSEPK regulation/signal-transduction functional bucket."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PARTITION_TSV = ROOT / "projects/P_PUTIDA/data/psepk_pathway_partition.tsv"
BATCH_DIR = ROOT / "projects/P_PUTIDA/batches"
OUT_TSV = BATCH_DIR / "module_regulation_signal_transduction_partition.tsv"
OUT_MD = BATCH_DIR / "module_regulation_signal_transduction_partition.md"
GENE_ROOT = ROOT / "genes/PSEPK"
SOURCE_BUCKET = "module:regulation_signal_transduction"
PREFIX = {"benR": "BenR"}


BUCKETS = {
    "lysr_transcriptional_regulators": {
        "label": "LysR-family transcriptional regulators",
        "module": "lysr_transcriptional_regulator_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "Large LysR-family transcription-factor expansion. First-pass curation "
            "is complete for all 107 genes; the split is represented in the LysR "
            "transcriptional regulator boundary module. Existing pcaQ, galR, and "
            "catR curated anchor reviews were preserved and given Asta retrieval "
            "provenance, 104 new reviews were Asta-backed, generic LysR paralogs "
            "were curated to DNA-binding transcription-regulator core functions, "
            "and direct pathway-process annotations on regulator genes were marked "
            "as pathway-association over-annotation unless a specific activator "
            "review supports positive transcription regulation. Regulons, effectors, "
            "and regulatory direction remain unresolved for generic paralogs."
        ),
    },
    "two_component_sensors_response_regulators": {
        "label": "Two-component sensors and response regulators",
        "module": "orphan_two_component_regulators_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "Histidine kinases, receiver-domain response regulators, and hybrid "
            "two-component proteins. First-pass curation is complete for all "
            "48 genes; the existing orphan/generic two-component regulator "
            "boundary module was extended with a ColRS anchor branch plus "
            "generic sensor kinase, DNA-binding response-regulator, and "
            "receiver-only/noncanonical response-regulator groups. Side "
            "annotations for transporter-like regions, HD-GYP phosphodiesterase "
            "domains, osmosensory labels, ATP/nucleotide binding, and localization "
            "were kept non-core or marked over-annotated unless gene-specific "
            "evidence supports a pathway claim."
        ),
    },
    "low_information_or_named_transcriptional_regulators": {
        "label": "Low-information or named transcriptional regulators",
        "module": "transcriptional_regulator_spillover_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "Named regulators and transcription-factor-like proteins that do not fall "
            "cleanly into one of the dominant families. First-pass curation is complete "
            "for all 32 genes; the split is represented in the transcriptional regulator "
            "spillover boundary module. Existing HexR curation was preserved as an anchor, "
            "31 new reviews were Asta-backed, conservative NEW transcription-regulator "
            "molecular-function rows were added only where product/domain evidence supports "
            "them, and PP_1762, PP_2738, PP_4528, PP_5232, and PP_5343 remain no-core "
            "unresolved."
        ),
    },
    "arac_xyls_transcriptional_regulators": {
        "label": "AraC/XylS-family transcriptional regulators",
        "module": "arac_xyls_transcriptional_regulator_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "AraC/XylS-family transcription regulators. First-pass curation is "
            "complete for all 40 genes; the split is represented in the AraC/XylS "
            "transcriptional regulator boundary module. Existing curated ada and "
            "BenR reviews were preserved as anchor cases, 38 new reviews were "
            "Asta-backed, DNA-binding transcription factor activity is kept as the "
            "shared core function, and target regulons, effector ligands, regulatory "
            "direction, and possible PP_4602 kinase side context remain unresolved "
            "unless already supported by gene-specific evidence."
        ),
    },
    "gntr_transcriptional_regulators": {
        "label": "GntR-family transcriptional regulators",
        "module": "gntr_transcriptional_regulator_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "GntR-family transcription regulators. First-pass curation is complete "
            "for all 29 genes; the split is represented in the GntR-family "
            "transcriptional regulator boundary module. The curation separates "
            "FadR/GntR C-terminal, UTRA/HutC-like, and PLP/aminotransferase-domain "
            "regulator candidates, keeps DNA-binding transcription factor activity "
            "as the shared core function, and leaves effector ligands, target "
            "regulons, regulatory direction, and PLP-domain substrate chemistry "
            "unresolved."
        ),
    },
    "merr_arsr_marr_metal_redox_regulators": {
        "label": "MerR/ArsR/MarR metal, redox, and stress regulators",
        "module": "metal_redox_stress_transcription_regulator_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "MerR-, ArsR-, and MarR-family regulators. First-pass curation is "
            "complete for all 25 genes; the split is represented in the metal, "
            "redox, and stress transcription regulator boundary module. arsR1 and "
            "arsR2 retain named arsenite/arsenic-efflux regulatory context from "
            "UniProt and PMID:27208139, soxR is kept as a redox-sensitive SoxR-like "
            "MerR regulator candidate, generic paralogs are curated to DNA-binding "
            "transcription regulator core functions without inferring regulons or "
            "ligands, and five weak no-GOA product-name-only records remain no-core "
            "unresolved."
        ),
    },
    "tetr_acrr_transcriptional_regulators": {
        "label": "TetR/AcrR-family transcriptional regulators",
        "module": "tetr_acrr_transcriptional_regulator_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "TetR/AcrR-family regulators. First-pass curation is complete for all "
            "25 genes; the split is represented in the TetR/AcrR transcriptional "
            "regulator boundary module. ttgR retains its existing curated repressor "
            "review, PP_2144 preserves curator-supported PsrA-like promoter-binding "
            "activator/repressor annotations, PP_2597 remains no-core unresolved, "
            "and sparse GOA-only DNA-binding rows are curated to sharper "
            "transcription-regulator core functions without inferring regulons, "
            "ligands, substrates, or regulatory direction."
        ),
    },
    "small_family_metabolic_transcriptional_regulators": {
        "label": "Small-family metabolic transcriptional regulators",
        "module": "metabolic_transcriptional_regulator_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "AsnC/Lrp, LacI, DeoR, IclR, RpiR, Crp/Fnr, and other compact metabolic "
            "regulator families. First-pass curation is complete for all 21 genes; "
            "the split is represented in the metabolic transcriptional regulator "
            "boundary module, with regulons and effector ligands left unresolved "
            "unless supported by gene-specific evidence."
        ),
    },
    "xre_cro_phage_toxin_antitoxin_regulators": {
        "label": "XRE/Cro phage and toxin-antitoxin regulators",
        "module": "phage_regulation_toxin_antitoxin_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "XRE/Cro/C1-like regulators and MqsRA-like toxin-antitoxin components. "
            "First-pass curation is complete for all 28 genes; the existing phage "
            "regulation/toxin-antitoxin boundary module was extended with MqsRA/HigA, "
            "LexA-like, Cro/C1-cupin, simple Cro/C1, and non-phage regulatory "
            "spillover groups. PP_5680 remains no-core unresolved, and RodZ/CdaR/PucR/"
            "LuxR/PuuR-like spillovers are not forced into phage-specific biology."
        ),
    },
    "sigma54_enhancer_binding_regulators": {
        "label": "Sigma-54 enhancer-binding regulators and LuxR-like EBPs",
        "module": "sigma54_enhancer_binding_regulator_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "AAA+ sigma-54 enhancer-binding regulators and related LuxR-like DNA-binding "
            "regulators. First-pass curation is complete for all 16 genes; the split "
            "is represented in the sigma-54 enhancer-binding regulator boundary module. "
            "ATP binding is retained as non-core cofactor context for sigma-54 activators, "
            "LuxR/GerE regulators are kept generic pending regulon evidence, and PP_5473 "
            "remains no-core unresolved."
        ),
    },
    "sigma_anti_sigma_and_sigma_factors": {
        "label": "Sigma, ECF sigma, anti-sigma, and anti-anti-sigma factors",
        "module": "sigma_anti_sigma_regulation_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "Sigma factors and anti-sigma regulators. First-pass curation is complete "
            "for all 16 genes; the split is represented in the sigma/anti-sigma "
            "regulation boundary module, preserving existing RpoS, PvdS, and RpoH "
            "curation decisions while adding Asta-backed first-pass reviews for the "
            "remaining sigma, anti-sigma, and anti-anti-sigma genes."
        ),
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


def ids(row: dict[str, str], field: str) -> set[str]:
    return {part.strip() for part in row.get(field, "").split(";") if part.strip()}


def has_any(text: str, terms: tuple[str, ...]) -> bool:
    lowered = norm(text)
    return any(term in lowered for term in terms)


def review_prefix(gene: str) -> str:
    return PREFIX.get(gene, gene)


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{review_prefix(gene)}-{suffix}"


def review_status(gene: str) -> str:
    return "PRESENT" if gene_file(gene, "ai-review.yaml").exists() else "MISSING"


def curation_status(gene: str) -> str:
    path = gene_file(gene, "ai-review.yaml")
    if not path.exists():
        return "MISSING"
    text = path.read_text(encoding="utf-8")
    if "action: PENDING" in text or "TODO: Review" in text or "TODO: Add description" in text:
        return "PENDING"
    return "CURATED"


def asta_research_status(gene: str) -> str:
    return "PRESENT" if gene_file(gene, "deep-research-asta.md").exists() else "MISSING"


def assign_bucket(row: dict[str, str]) -> str:
    gene = row["suggested_review_name"]
    product = row["protein_name"]
    go = ids(row, "go_ids")
    interpro = ids(row, "interpro_ids")
    pfam = ids(row, "pfam_ids")

    if (
        "GO:0016987" in go
        or has_any(product, ("sigma factor", "anti-sigma", "sigma-70", "sigma-24"))
    ) and gene not in {"PP_0051", "PP_0601", "PP_0872", "PP_0873", "PP_3611", "PP_4321"}:
        return "sigma_anti_sigma_and_sigma_factors"

    if (
        go & {"GO:0000155", "GO:0000156", "GO:0000160"}
        or pfam & {"PF00072", "PF00512", "PF02518", "PF07730", "PF07568"}
        or interpro & {"IPR001789", "IPR003594", "IPR004358", "IPR005467", "IPR011006"}
        or has_any(product, ("response regulator", "sensor histidine kinase", "two-component"))
    ):
        return "two_component_sensors_response_regulators"

    if (
        has_any(product, ("xre", "cro/ci", "cro-c1", "toxin", "antitoxin"))
        or pfam & {"PF01381", "PF07883", "PF13556", "PF15723", "PF15731"}
        or gene in {"mqsR", "mqsA"}
    ):
        return "xre_cro_phage_toxin_antitoxin_regulators"

    if pfam & {"PF00126", "PF03466"} or {"IPR000847", "IPR005119"} <= interpro or "lysr" in norm(product):
        return "lysr_transcriptional_regulators"

    if pfam & {"PF12833", "PF00165"} or "arac" in norm(product):
        return "arac_xyls_transcriptional_regulators"

    if pfam & {"PF00392", "PF07729"} or "gntr" in norm(product):
        return "gntr_transcriptional_regulators"

    if pfam & {"PF00440"} or "tetr" in norm(product):
        return "tetr_acrr_transcriptional_regulators"

    if (
        pfam & {"PF00376", "PF01022", "PF01047", "PF12802"}
        or has_any(product, ("merr", "arsr", "marr"))
    ):
        return "merr_arsr_marr_metal_redox_regulators"

    if (
        pfam
        & {
            "PF01037",
            "PF08220",
            "PF11960",
            "PF13463",
            "PF00325",
            "PF00532",
            "PF02082",
            "PF01325",
        }
        or has_any(
            product,
            (
                "asnc",
                "laci",
                "deor",
                "iclr",
                "rpir",
                "crp/fnr",
                "crp",
                "fnr",
                "nrd regulator",
                "rbs operon repressor",
            ),
        )
    ):
        return "small_family_metabolic_transcriptional_regulators"

    if (
        pfam & {"PF00158", "PF02954", "PF08448", "PF00196"}
        or has_any(product, ("sigma-54", "sigma54", "luxr family"))
    ):
        return "sigma54_enhancer_binding_regulators"

    if (
        has_any(product, ("dna-binding", "transcriptional regulator", "transcriptional repressor"))
        or go & {"GO:0003700", "GO:0000976", "GO:0003677", "GO:0043565", "GO:0006355", "GO:0006351"}
    ):
        return "low_information_or_named_transcriptional_regulators"

    return "low_information_or_named_transcriptional_regulators"


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
        'title: "PSEPK regulation/signal-transduction functional-bucket partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK regulation/signal-transduction functional-bucket partition",
        "",
        "The `module:regulation_signal_transduction` bucket is a UniProt",
        "name/domain umbrella. It mixes hundreds of transcription factors,",
        "two-component-system proteins, sigma-factor regulators, phage-like",
        "regulatory proteins, toxin-antitoxin components, and low-information",
        "DNA-binding proteins. It is not satisfiable as one biological module.",
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
            "- Do not curate the 387-gene functional bucket as one satisfiable module.",
            "- Treat most rows as transcription-factor family batches until gene-level",
            "  evidence supports a pathway-specific regulon assignment.",
            "- Reuse existing boundary modules for ECF sigma/anti-sigma regulators,",
            "  orphan two-component regulators, phage/toxin-antitoxin regulators,",
            "  and metal/redox/stress regulators where the gene-level evidence fits.",
            "- Use the small-family metabolic-regulator split as the first follow-up",
            "  batch because it is compact and contains several named metabolic",
            "  regulators while still exercising the same GOA-overannotation pattern",
            "  seen in the larger LysR/AraC/GntR/TetR expansions. This split is now",
            "  complete and represented in `modules/metabolic_transcriptional_regulator_boundary.yaml`.",
            "- For generic transcription-factor paralogs, broad DNA-binding or",
            "  transcription-regulator terms can be core, but broad parent biological",
            "  process terms such as `DNA-templated transcription` should usually be",
            "  non-core or over-annotated unless there is gene-specific evidence.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    for bucket_id in BUCKET_ORDER:
        info = BUCKETS[bucket_id]
        bucket_rows = by_bucket[bucket_id]
        stem = f"module_regulation_signal_transduction_{bucket_id}"
        write_rows(BATCH_DIR / f"{stem}.tsv", bucket_rows)
        write_batch_md(
            BATCH_DIR / f"{stem}.md",
            f"PSEPK regulation/signal transduction: {info['label']}",
            bucket_rows,
            info["note"],
        )

    print(f"Wrote {OUT_TSV.relative_to(ROOT)} with {len(rows)} rows")
    for bucket_id in BUCKET_ORDER:
        print(f"{bucket_id}: {counts[bucket_id]}")


if __name__ == "__main__":
    main()
