#!/usr/bin/env python3
"""Partition the transport ion/metal antiporter sub-bucket."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BATCH_DIR = ROOT / "projects/P_PUTIDA/batches"
SOURCE_TSV = BATCH_DIR / "module_transport_membrane_efflux_ion_metal_transporters_and_antiporters.tsv"
OUT_TSV = BATCH_DIR / "module_transport_membrane_efflux_ion_metal_partition.tsv"
OUT_MD = BATCH_DIR / "module_transport_membrane_efflux_ion_metal_partition.md"
GENE_ROOT = ROOT / "genes/PSEPK"


BUCKETS = {
    "monovalent_cation_antiporters_potassium_systems": {
        "label": "Monovalent cation antiporters and potassium systems",
        "module": "monovalent_cation_antiporter_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 26 monovalent cation and "
            "potassium-system genes. The validated boundary module separates Trk/"
            "Kup potassium uptake, NhaA/NhaB/NhaP sodium/proton antiporters, Kef "
            "potassium/proton antiporters, Mrp multicomponent antiporter subunits, "
            "K/Na/Ca exchanger and potassium-channel candidates, and conservative "
            "side candidates including the NhaC-like PP_3556 and DASS-related yfbS."
        ),
        "genes": [
            "trkA",
            "kefB-I",
            "PP_0928",
            "nhaA1",
            "kup",
            "PP_1467",
            "PP_1587",
            "mrpG",
            "mrpF",
            "mrpE",
            "mrpD",
            "mrpC",
            "mrpAB",
            "PP_3293",
            "kefB-II",
            "yfbS",
            "trkH-I",
            "nhaA2",
            "nhaB",
            "PP_4304",
            "trkH-II",
            "nhaP",
            "nhaP2",
            "kefB-III",
            "PP_5355",
            "PP_3556",
        ],
    },
    "p_type_metal_atpases": {
        "label": "P-type metal ATPases",
        "module": "p_type_metal_atpase_transport_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all five P-type metal ATPases. "
            "The validated boundary module separates CadA-family zinc/cadmium "
            "export ATPases, CadA-II copper export, MgtA magnesium import, and "
            "PP_4261 as an unresolved type-IB copper/cation ATPase candidate."
        ),
        "genes": ["cadA-I", "cadA-II", "mgtA", "PP_4261", "cadA-III"],
    },
    "transition_metal_magnesium_cobalt_transporters": {
        "label": "Transition-metal, magnesium, and cobalt transporters",
        "module": "transition_metal_magnesium_cobalt_transport_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 15 transition-metal, magnesium, "
            "and cobalt transporter-family entries. The validated boundary module "
            "separates CDF/ZIP zinc and mixed-metal transporters, CbiM/CbtA cobalt "
            "components, CorA/MgtE magnesium-cobalt transporters, NiCoT/Rcn nickel-"
            "cobalt efflux/response context, and CorC/CNNM-UPF0053 low-resolution "
            "metal-transporter candidates."
        ),
        "genes": [
            "PP_0026",
            "PP_0629",
            "PP_0683",
            "PP_0947",
            "PP_1227",
            "PP_1836",
            "PP_1843",
            "cmaX",
            "PP_2955",
            "PP_2968",
            "cbtA",
            "PP_3928",
            "mgtE",
            "corC",
            "PP_5322",
        ],
    },
    "chromate_fluoride_and_other_inorganic_channels": {
        "label": "Chromate, fluoride, and other inorganic channels",
        "module": "inorganic_ion_channel_resistance_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for the three inorganic-channel/"
            "resistance entries. The validated boundary module separates PP_2556 "
            "CHR-family chromate transport, reviewed FluC fluoride channel/"
            "detoxification context, and PP_4986 as an HlyIII-family pore-forming "
            "candidate with unresolved physiological substrate."
        ),
        "genes": ["PP_2556", "fluC", "PP_4986"],
    },
    "sodium_solute_symporters_and_mate_efflux": {
        "label": "Sodium-solute symporters and MATE efflux",
        "module": "sodium_solute_symporter_mate_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 14 sodium-solute/MATE "
            "transport-family entries. The validated boundary module separates "
            "AGCS amino-acid:sodium symport, GltS glutamate:sodium symport, "
            "ArcD arginine-ornithine antiport, ActP acetate transport, PutP "
            "sodium/proline symport, TcyP cystine transport, MATE xenobiotic "
            "efflux, PP_4524 broad SSF context, PP_3331 low-confidence symporter "
            "context, and PP_0670 as an ACR3 arsenite/antimonite transporter "
            "outlier."
        ),
        "genes": [
            "PP_0496",
            "PP_0569",
            "PP_0670",
            "gltS",
            "arcD-I",
            "arcD-II",
            "actP-I",
            "actP-II",
            "actP-III",
            "PP_3331",
            "PP_4524",
            "putP",
            "tcyP",
            "norM",
        ],
    },
    "membrane_redox_electron_transfer_spillovers": {
        "label": "Membrane redox and electron-transfer spillovers",
        "module": "membrane_redox_electron_transfer_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 25 membrane redox/electron-transfer "
            "spillover entries. The validated boundary module separates cytochromes, "
            "heme/copper proteins, ferredoxin/iron-sulfur proteins, Ccm proteins, "
            "flavoprotein redox components, Hmp/MsrQ detoxification or repair nodes, "
            "CumA/azurin, and the OFeT/FTR1-like iron transporter from ion-transport "
            "assertions where appropriate."
        ),
        "genes": [
            "PP_0111",
            "PP_0125",
            "cc",
            "PP_0180",
            "hmp",
            "cumA",
            "PP_1083",
            "fdxA",
            "PP_1841",
            "PP_2010",
            "PP_2675",
            "PP_2886",
            "PP_3332",
            "PP_3543",
            "PP_4203",
            "PP_4259",
            "PP_4289",
            "ccmE",
            "msrQ",
            "PP_4870",
            "PP_4970",
            "yceJ",
            "yfhL",
            "PP_5267",
            "ccmH",
        ],
    },
    "membrane_metalloenzymes_and_envelope_side_nodes": {
        "label": "Membrane metalloenzymes and envelope side nodes",
        "module": "transport_membrane_enzyme_spillover_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 14 membrane metalloenzyme/"
            "envelope side-node entries. The validated boundary module separates "
            "membrane protease/metalloprotease context, membrane lipid/cell-wall "
            "glycosylation side nodes, TamB envelope assembly context, and "
            "CopD/CycZ-like copper/cytochrome side nodes that should not be curated "
            "as ion transporters."
        ),
        "genes": [
            "PP_0093",
            "PP_0144",
            "PP_1124",
            "PP_1526",
            "rseP",
            "htpX",
            "wbpL",
            "PP_1838",
            "PP_2893",
            "PP_2974",
            "ybhN",
            "PP_4263",
            "ypfJ",
            "ftsH",
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
    gene = source["gene"]
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
    source_rows = list(csv.DictReader(SOURCE_TSV.open(encoding="utf-8"), delimiter="\t"))
    row_by_gene = {row["gene"]: row for row in source_rows}

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

    counts = Counter(row["partition_bucket"] for row in rows)
    examples: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        if len(examples[row["partition_bucket"]]) < 8:
            examples[row["partition_bucket"]].append(row["gene"])

    lines = [
        "---",
        'title: "PSEPK transport ion/metal sub-bucket partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK transport ion/metal sub-bucket partition",
        "",
        "The parent `ion_metal_transporters_and_antiporters` split contains true",
        "cation homeostasis systems plus metal-binding redox proteins, proteases,",
        "and membrane enzyme side nodes. This deeper partition separates those",
        "contexts before first-pass curation.",
        "",
        "## Outputs",
        "",
        f"- Source table: `{SOURCE_TSV.relative_to(ROOT)}`",
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
            "- Do not curate the 102-gene ion/metal bucket as one satisfiable module.",
            "- The monovalent cation antiporter and potassium-system split is complete",
            "  and represented in `modules/monovalent_cation_antiporter_boundary.yaml`.",
            "- The P-type metal ATPase split is complete and represented in",
            "  `modules/p_type_metal_atpase_transport_boundary.yaml`.",
            "- The chromate/fluoride/inorganic-channel split is complete and represented in",
            "  `modules/inorganic_ion_channel_resistance_boundary.yaml`.",
            "- The transition-metal/Mg/Co transporter split is complete and represented in",
            "  `modules/transition_metal_magnesium_cobalt_transport_boundary.yaml`.",
            "- The membrane redox/electron-transfer spillover split is complete and represented in",
            "  `modules/membrane_redox_electron_transfer_boundary.yaml`.",
            "- Route cytochromes, heme proteins, ferredoxins, and Ccm proteins toward",
            "  membrane redox/electron-transfer context rather than ion transport.",
            "- Treat metalloproteases, metal-dependent transferases/sulfatases, TamB,",
            "  and phospholipid-modification entries as membrane/enzyme side nodes.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    for bucket_id in BUCKET_ORDER:
        info = BUCKETS[bucket_id]
        bucket_rows = by_bucket[bucket_id]
        stem = f"module_transport_membrane_efflux_ion_metal_{bucket_id}"
        write_rows(BATCH_DIR / f"{stem}.tsv", bucket_rows)
        write_batch_md(
            BATCH_DIR / f"{stem}.md",
            f"PSEPK transport ion/metal: {info['label']}",
            bucket_rows,
            info["note"],
        )

    print(f"Wrote {OUT_TSV.relative_to(ROOT)} with {len(rows)} rows")
    for bucket_id in BUCKET_ORDER:
        print(f"{bucket_id}: {counts[bucket_id]}")


if __name__ == "__main__":
    main()
