#!/usr/bin/env python3
"""Partition the PSEPK DNA replication/repair/recombination functional bucket."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PARTITION_TSV = ROOT / "projects/P_PUTIDA/data/psepk_pathway_partition.tsv"
OUT_TSV = ROOT / "projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_partition.tsv"
OUT_MD = ROOT / "projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_partition.md"
GENE_ROOT = ROOT / "genes/PSEPK"
SOURCE_BUCKET = "module:dna_replication_repair_recombination"


BUCKETS = {
    "dna_topology_topoisomerase": {
        "label": "DNA topology, gyrase, and topoisomerase",
        "module": "dna_topology_topoisomerase_boundary",
        "action": "NEW_SUBMODULE",
        "note": (
            "DNA gyrase, topoisomerase I/IV, topoisomerase side candidates, and the "
            "YacG gyrase inhibitor; curate as DNA topology rather than generic DNA repair."
        ),
        "genes": ["gyrB", "yacG", "gyrA", "topA", "PP_3831", "topB", "PP_4476", "parC", "parE"],
    },
    "replication_accessory_polymerase": {
        "label": "Replication accessory polymerase, primase, and restart factors",
        "module": "bacterial_dna_replication",
        "action": "REUSE_OR_EXTEND_EXISTING",
        "note": (
            "Replication-associated accessory candidates not already in the KEGG ppu03030 batch: "
            "Pol III chi-like context, Hda reinitiation control, primase/helicase or polymerase "
            "candidates, RarA restart, and Rep helicase."
        ),
        "genes": ["PP_0978", "hda", "PP_2270", "PP_2273", "rarA", "rep"],
    },
    "sos_translesion_alkylation_repair": {
        "label": "SOS, translesion synthesis, alkylation repair, and oxidized nucleotide sanitation",
        "module": "dna_damage_response_translesion_repair_boundary",
        "action": "NEW_SUBMODULE",
        "note": (
            "LexA/SOS regulators, DinB/PolB/ImuB/DnaE2/Y-family error-prone polymerase context, "
            "MutT-like oxidized nucleotide sanitation, and Ogt alkylation repair."
        ),
        "genes": ["dinB", "PP_1348", "lexA1", "polB", "ogt", "lexA2", "imuB", "dnaE2", "PP_5679"],
    },
    "repair_helicase_recombination_core": {
        "label": "DNA repair helicases, recombination, and double-strand break candidates",
        "module": "bacterial_homologous_recombination",
        "action": "REUSE_OR_EXTEND_EXISTING",
        "note": (
            "Lhr/DinG/SNF2/Rep-family helicases, SbcCD, RadA, RecN, RdgC, HerA-like, and other "
            "repair/recombination candidates adjacent to existing homologous-recombination modules."
        ),
        "genes": [
            "PP_0152",
            "PP_1061",
            "PP_1103",
            "PP_1106",
            "dinG",
            "rdgC",
            "PP_1410",
            "PP_1937",
            "sbcC",
            "sbcD",
            "uup",
            "PP_2146",
            "PP_2298",
            "PP_2565",
            "PP_3681",
            "PP_3691",
            "PP_4448",
            "radA",
            "recN",
            "PP_5711",
        ],
    },
    "mobile_integrase_recombinase_transposase": {
        "label": "Mobile-element integrases, recombinases, resolvases, and transposases",
        "module": "mobile_genetic_elements_boundary",
        "action": "REASSIGN_TO_MOBILE_ELEMENTS",
        "note": (
            "Phage integrases, Tyr/Ser recombinases, resolvases, and transposases are mobile-element "
            "context, not core chromosomal DNA replication/repair pathway members."
        ),
        "genes": [
            "PP_1116",
            "PP_1118",
            "PP_1532",
            "PP_1533",
            "PP_1555",
            "PP_1865",
            "PP_1960",
            "PP_1962",
            "PP_2297",
            "PP_2495",
            "PP_2501",
            "PP_2937",
            "PP_2964",
            "PP_2971",
            "tnpS",
            "PP_3026",
            "PP_3181",
            "PP_3678",
            "PP_3791",
            "PP_3889",
            "PP_3920",
            "PP_3987",
            "PP_4409",
            "PP_4415",
            "PP_5490",
        ],
    },
    "retroelement_reverse_transcriptase": {
        "label": "Retroelement reverse transcriptase candidates",
        "module": "mobile_genetic_elements_boundary",
        "action": "REASSIGN_TO_MOBILE_ELEMENTS",
        "note": (
            "RNA-directed DNA polymerase/reverse-transcriptase candidates should be reviewed as "
            "retroelement or mobile-element proteins rather than chromosomal DNA replication enzymes."
        ),
        "genes": ["PP_0635", "PP_1250", "PP_1846"],
    },
    "nuclease_dnase_toxin_side_nodes": {
        "label": "Nucleases, DNases, toxin nucleases, and broad phosphodiesterases",
        "module": "nuclease_dnase_boundary",
        "action": "NEW_SUBMODULE",
        "note": (
            "DNase, HNH/VRR-NUC/SNase/YicC, phage exonuclease, pyocin nuclease, TatD, and YoeB-like "
            "nuclease contexts; likely mixed DNA, RNA, toxin, and mobile-element side functions."
        ),
        "genes": [
            "PP_1306",
            "PP_1554",
            "PP_2276",
            "tatD",
            "endX",
            "PP_2838",
            "endA",
            "yoeB",
            "PP_3883",
            "PP_3890",
            "PP_4247",
            "PP_5086",
            "yajD",
            "PP_5295",
        ],
    },
    "architectural_rna_protein_spillovers": {
        "label": "Architectural, RNA-helicase, chaperone, and protease spillovers",
        "module": "dna_bucket_architectural_rna_protein_spillover_boundary",
        "action": "NEW_SUBMODULE",
        "note": (
            "IHF architectural proteins, CspD, DnaJ, HrpA/HrpB RNA helicases, and TldD enter through "
            "broad DNA or inhibitor keywords; retain these in a boundary module as regulation, RNA "
            "processing, protein folding, or protease context unless direct DNA-repair evidence is found."
        ),
        "genes": ["tldD", "ihfB", "ihfA", "cspD", "dnaJ", "hrpA", "hrpB"],
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
        "## Candidate Genes",
        "",
        "| Done | Gene | Locus | UniProt | Partition bucket | Review | Curation | Asta | Protein |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        done = "[x]" if row["curation_status"] == "CURATED" else "[ ]"
        lines.append(
            "| "
            + " | ".join(
                [
                    done,
                    f"`{row['gene']}`",
                    row["ordered_locus"],
                    row["uniprot_accession"],
                    f"`{row['partition_bucket']}`",
                    row["review_status"],
                    row["curation_status"],
                    row["asta_research_status"],
                    row["protein_name"].replace("|", "/"),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "Generated by `projects/P_PUTIDA/partition_dna_replication_repair_recombination.py`.",
        ]
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
        'title: "PSEPK DNA replication, repair, and recombination functional-bucket partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK DNA replication, repair, and recombination functional-bucket partition",
        "",
        "The `module:dna_replication_repair_recombination` bucket is a broad",
        "functional umbrella assembled from UniProt names and keywords. It mixes",
        "core DNA topology and repair proteins with phage/mobile-element enzymes,",
        "reverse transcriptases, toxin nucleases, RNA-helicase/protein-folding",
        "spillovers, and DNA-binding architectural proteins. It should not be",
        "curated as one pathway.",
        "",
        "## Outputs",
        "",
        f"- Partition table: `{OUT_TSV.relative_to(ROOT)}`",
        "",
        "## Partition Summary",
        "",
        "| Bucket | Genes | Proposed module | Action | Example genes |",
        "|---|---:|---|---|---|",
    ]
    for bucket_id, info in BUCKETS.items():
        module = info["module"] or "none"
        lines.append(
            f"| `{bucket_id}` | {counts[bucket_id]} | `{module}` | "
            f"{info['action']} | "
            + ", ".join(f"`{gene}`" for gene in examples[bucket_id])
            + " |"
        )
    lines.extend(
        [
            "",
            "## Working Decisions",
            "",
            "- Do not curate all 93 primary genes as one DNA replication/repair PR.",
            "- Reuse existing KEGG-derived modules for canonical bacterial DNA replication,",
            "  base excision repair, nucleotide excision repair, mismatch repair,",
            "  homologous recombination, and non-homologous end joining.",
            "- The DNA-topology/topoisomerase, replication-accessory/polymerase,",
            "  SOS/translesion/alkylation, repair-helicase/recombination, and",
            "  nuclease/DNase/toxin sub-batches, and architectural/RNA/protein",
            "  spillovers are separate from the mobile-element spillover set.",
            "- Route reverse transcriptases, phage integrases, transposases, and many",
            "  recombinases to the mobile-genetic-elements boundary unless gene-level",
            "  evidence supports direct chromosomal DNA repair.",
            "",
            "## Current Coverage",
            "",
            f"- Review status: {dict(Counter(row['review_status'] for row in rows))}",
            f"- Curation status: {dict(Counter(row['curation_status'] for row in rows))}",
            f"- Asta research status: {dict(Counter(row['asta_research_status'] for row in rows))}",
            "",
            "## Next Steps",
            "",
            "- `dna_topology_topoisomerase` is complete as a compact 9-gene first-pass",
            "  sub-batch with the new `dna_topology_topoisomerase_boundary` module.",
            "- `sos_translesion_alkylation_repair` is complete as a compact 9-gene",
            "  first-pass sub-batch with the new",
            "  `dna_damage_response_translesion_repair_boundary` module.",
            "- `repair_helicase_recombination_core` is complete as a 20-gene",
            "  first-pass sub-batch extending `bacterial_homologous_recombination`.",
            "- `nuclease_dnase_toxin_side_nodes` is complete as a 14-gene",
            "  first-pass sub-batch with the new `nuclease_dnase_boundary` module.",
            "- `replication_accessory_polymerase` is complete as a 6-gene",
            "  first-pass sub-batch extending `bacterial_dna_replication`.",
            "- `architectural_rna_protein_spillovers` is complete as a 7-gene",
            "  first-pass sub-batch with the new",
            "  `dna_bucket_architectural_rna_protein_spillover_boundary` module.",
            "- `mobile_integrase_recombinase_transposase` is complete as a 25-gene",
            "  first-pass sub-batch with the new `mobile_genetic_elements_boundary`",
            "  module.",
            "- `retroelement_reverse_transcriptase` is complete as a 3-gene",
            "  first-pass sub-batch represented in `mobile_genetic_elements_boundary`.",
            "- The full 93-gene DNA replication/repair/recombination functional bucket",
            "  now has review files, curated reviews, and Asta reports for every",
            "  partition member.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    for bucket_id, info in BUCKETS.items():
        sub_rows = [row for row in rows if row["partition_bucket"] == bucket_id]
        sub_tsv = ROOT / f"projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_{bucket_id}.tsv"
        sub_md = ROOT / f"projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_{bucket_id}.md"
        write_rows(sub_tsv, sub_rows)
        write_batch_md(sub_md, f"PSEPK DNA bucket: {info['label']}", sub_rows, info["note"])


if __name__ == "__main__":
    main()
