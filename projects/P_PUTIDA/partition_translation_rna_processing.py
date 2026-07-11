#!/usr/bin/env python3
"""Partition the PSEPK translation/RNA-processing functional bucket."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PARTITION_TSV = ROOT / "projects/P_PUTIDA/data/psepk_pathway_partition.tsv"
BATCH_DIR = ROOT / "projects/P_PUTIDA/batches"
OUT_TSV = BATCH_DIR / "module_translation_rna_processing_partition.tsv"
OUT_MD = BATCH_DIR / "module_translation_rna_processing_partition.md"
GENE_ROOT = ROOT / "genes/PSEPK"
SOURCE_BUCKET = "module:translation_rna_processing"


BUCKETS = {
    "rrna_modification_methyltransferase_pseudouridine": {
        "label": "rRNA modification methyltransferase and pseudouridine enzymes",
        "module": "rrna_modification_ribosome_maturation_boundary",
        "action": "NEW_SUBMODULE",
        "status": "QUEUED",
        "note": (
            "Rsm/Rlm/Rlu/Rsu-family rRNA methyltransferase and pseudouridine synthase "
            "entries, including dual rRNA/tRNA enzymes where the rRNA role is the "
            "dominant product-name signal. Curate site-specific RNA modification terms "
            "where GOA/domain support is strong, and keep broad RNA binding non-core."
        ),
        "genes": [
            "rsmG",
            "rsmB",
            "rsmA",
            "rluD",
            "rsmC",
            "rlmN",
            "rlmF",
            "rsmI",
            "rsmH",
            "rsuA",
            "rsmJ",
            "rlmAA",
            "rlmD",
            "rluC",
            "rlmL",
            "PP_2110",
            "rlmM",
            "PP_4306",
            "rluB",
            "rlmG",
            "rlmE",
            "rlmH",
            "rlmB",
            "rlmJ",
            "rsmE",
            "PP_5019",
            "PP_5114",
            "rlmI",
            "PP_1191",
        ],
    },
    "ribosome_assembly_maturation_hibernation": {
        "label": "Ribosome assembly, maturation, hibernation, and ribosomal-protein modification",
        "module": "bacterial_ribosome_maturation_regulation_boundary",
        "action": "NEW_SUBMODULE",
        "status": "QUEUED",
        "note": (
            "Ribosome biogenesis GTPases, maturation factors, hibernation/silencing "
            "factors, ribosomal-protein modifiers, and low-information ribosomal "
            "subunit interface/S2p fragments. Keep these separate from the already "
            "completed 30S/50S structural ribosome modules."
        ),
        "genes": [
            "yigZ",
            "der",
            "darP",
            "hpf",
            "rimI",
            "rimO",
            "era",
            "rimM",
            "prmB",
            "PP_1910",
            "PP_2956",
            "ycaO",
            "PP_3810",
            "rbfA",
            "rimP",
            "ybeY",
            "PP_4996",
            "typA",
            "rsfS",
            "prmA",
            "rmf",
            "PP_4885",
            "PP_5700",
            "PP_5726",
        ],
    },
    "trna_modification_processing": {
        "label": "tRNA modification and processing enzymes",
        "module": "trna_modification_processing_boundary",
        "action": "NEW_SUBMODULE",
        "status": "QUEUED",
        "note": (
            "Mnm/Cmo/Tsa/Trm/Dus/Tru/Mia/Ttc/Til/Cca tRNA-modification and tRNA "
            "processing enzymes. Curate explicit tRNA modification reactions where "
            "supported; avoid generic transferase or RNA-binding terms as core calls."
        ),
        "genes": [
            "mnmG",
            "mnmE",
            "tsaC",
            "tsaD",
            "cca",
            "cmoM",
            "selU",
            "trmJ",
            "tadA",
            "cmoB",
            "trmD",
            "tsaB",
            "tilS",
            "truD",
            "yfiP",
            "ttcA",
            "rluA",
            "mnmC",
            "trhO",
            "dusC",
            "truA",
            "dusA",
            "trmK",
            "PP_4520",
            "trmA",
            "truB",
            "dusB",
            "miaA",
            "tsaE",
            "trmL",
        ],
    },
    "ribonuclease_rna_decay_processing_helicases": {
        "label": "Ribonucleases, RNA decay/processing, and RNA helicases",
        "module": "rna_decay_processing_boundary",
        "action": "NEW_SUBMODULE",
        "status": "QUEUED",
        "note": (
            "RNase P/G/T/Z/D/PH, YbeY, DEAD-box RNA helicases, and RraA-like "
            "ribonuclease-regulator spillovers. Separate catalytic nuclease/helicase "
            "roles from rRNA/tRNA/ribosome-assembly process context."
        ),
        "genes": [
            "rnpA",
            "rng",
            "rnt",
            "PP_1840",
            "PP_2084",
            "rnz",
            "PP_4462",
            "srmB",
            "rnd",
            "PP_4720",
            "dbpA",
            "rph",
        ],
    },
    "aminoacyl_trna_charging_editing_quality_control": {
        "label": "Aminoacyl-tRNA charging, editing, amidotransferase, and quality-control enzymes",
        "module": "aminoacyl_trna_quality_control_boundary",
        "action": "NEW_SUBMODULE",
        "status": "QUEUED",
        "note": (
            "Aminoacyl-tRNA synthetase fragments or specialized synthetases, GatCAB-like "
            "amidotransferase subunits, YbaK/Dtd/YcfH deacylases, and Aat tRNA-protein "
            "transferase context. Curate aminoacylation/editing functions precisely."
        ),
        "genes": [
            "PP_0201",
            "PP_0782",
            "PP_0784",
            "ybaK",
            "PP_1091",
            "ycfH",
            "PP_4228",
            "gluQ",
            "dtd",
            "PP_5664",
            "aat",
        ],
    },
    "translation_factors_ribosome_rescue": {
        "label": "Translation factors, ribosome rescue, and translational regulation",
        "module": "translation_factor_ribosome_rescue_boundary",
        "action": "NEW_SUBMODULE",
        "status": "QUEUED",
        "note": (
            "Initiation/elongation/recycling factors, ribosome rescue proteins, "
            "translation throttles, and ribosome-associated stress factors. Keep "
            "translation regulation/rescue distinct from structural ribosome modules."
        ),
        "genes": ["hslR", "selB", "ettA", "ychF", "pth", "lepA", "frr", "arfB", "infA", "smpB"],
    },
    "transcription_rna_polymerase_spillovers": {
        "label": "Transcription and RNA-polymerase spillovers",
        "module": "transcription_rna_polymerase_spillover_boundary",
        "action": "ROUTE_OUT_OF_TRANSLATION",
        "status": "QUEUED",
        "note": (
            "Nus antitermination factors, RapA, DksA, an ECF sigma factor, and an "
            "RNA-polymerase subunit fragment/candidate. Route these to transcription "
            "or regulatory modules rather than translation/RNA-processing modules."
        ),
        "genes": ["nusB", "rapA", "PP_2266", "PP_4553", "dksA", "nusA"],
    },
    "nonribosomal_peptide_synthetase_spillovers": {
        "label": "Non-ribosomal peptide synthetase spillovers",
        "module": "siderophore_biosynthesis_boundary",
        "action": "REUSE_OR_EXTEND_EXISTING",
        "status": "QUEUED",
        "note": (
            "Pyoverdine/ferribactin NRPS genes entered this bucket by the string "
            "'non-ribosomal'. They should be routed to siderophore/pyoverdine "
            "biosynthesis context, not translation."
        ),
        "genes": ["pvdD", "pvdJ", "pvdI", "pvdL"],
    },
    "low_information_rna_binding_or_enzyme_spillovers": {
        "label": "Low-information RNA-binding or enzyme spillovers",
        "module": "translation_rna_processing_spillover_boundary",
        "action": "DEFER_LOW_EVIDENCE",
        "status": "QUEUED",
        "note": (
            "ProQ/FinO and zinc-alcohol-dehydrogenase-like RNA-binding or regulatory "
            "spillovers with weak pathway specificity. Keep core functions narrow "
            "and do not force them into rRNA/tRNA processing without stronger evidence."
        ),
        "genes": ["PP_2182", "PP_2953"],
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


def derived_bucket_status(info: dict[str, object], rows: list[dict[str, str]]) -> str:
    if rows and all(
        row["review_status"] == "PRESENT"
        and row["curation_status"] == "CURATED"
        and row["asta_research_status"] == "PRESENT"
        for row in rows
    ):
        return "COMPLETE"
    return str(info["status"])


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

    by_bucket: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_bucket[row["partition_bucket"]].append(row)

    bucket_statuses = {
        bucket_id: derived_bucket_status(BUCKETS[bucket_id], by_bucket[bucket_id])
        for bucket_id in BUCKET_ORDER
    }
    for row in rows:
        row["bucket_status"] = bucket_statuses[row["partition_bucket"]]

    write_rows(OUT_TSV, rows)

    lines = [
        "---",
        'title: "PSEPK translation/RNA processing functional bucket partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK translation/RNA processing functional bucket partition",
        "",
        f"Source bucket: `{SOURCE_BUCKET}`",
        "",
        "The UniProt keyword/name bucket is heterogeneous. This partition separates true rRNA/tRNA processing, "
        "ribosome maturation, translation-factor, RNA decay, aminoacyl-tRNA quality-control, transcription spillover, "
        "NRPS spillover, and low-information side contexts before gene-level curation.",
        "",
        "| Split | Genes | Module target | Action | Review files | Curated | Asta |",
        "|---|---:|---|---|---:|---:|---:|",
    ]
    for bucket_id in BUCKET_ORDER:
        info = BUCKETS[bucket_id]
        bucket_rows = by_bucket[bucket_id]
        present = sum(1 for row in bucket_rows if row["review_status"] == "PRESENT")
        curated = sum(1 for row in bucket_rows if row["curation_status"] == "CURATED")
        asta = sum(1 for row in bucket_rows if row["asta_research_status"] == "PRESENT")
        lines.append(
            f"| `{bucket_id}` | {len(bucket_rows)} | `{info['module']}` | {info['action']} | {present} | {curated} | {asta} |"
        )

        batch_base = f"module_translation_rna_processing_{bucket_id}"
        write_rows(BATCH_DIR / f"{batch_base}.tsv", bucket_rows)
        write_batch_md(
            BATCH_DIR / f"{batch_base}.md",
            f"PSEPK translation/RNA processing: {info['label']}",
            bucket_rows,
            info["note"],
        )

    lines.extend(["", "## Split details", ""])
    for bucket_id in BUCKET_ORDER:
        info = BUCKETS[bucket_id]
        counts = Counter(row["curation_status"] for row in by_bucket[bucket_id])
        lines.extend(
            [
                f"### {info['label']}",
                "",
                f"- Split id: `{bucket_id}`",
                f"- Proposed module: `{info['module']}`",
                f"- Recommended action: `{info['action']}`",
                f"- Status: `{bucket_statuses[bucket_id]}`",
                f"- Curation status counts: {dict(counts)}",
                f"- Genes: {', '.join('`' + row['gene'] + '`' for row in by_bucket[bucket_id])}",
                f"- Notes: {info['note']}",
                "",
            ]
        )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT_TSV} and {OUT_MD}")
    for bucket_id in BUCKET_ORDER:
        print(f"{bucket_id}: {len(by_bucket[bucket_id])}")


if __name__ == "__main__":
    main()
