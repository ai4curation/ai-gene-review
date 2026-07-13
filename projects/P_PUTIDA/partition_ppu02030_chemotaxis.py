#!/usr/bin/env python3
"""Partition KEGG ppu02030 bacterial chemotaxis into curation-scale buckets."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BATCH_TSV = ROOT / "projects/P_PUTIDA/batches/ppu02030_bacterial_chemotaxis_boundary.tsv"
OUT_TSV = ROOT / "projects/P_PUTIDA/batches/ppu02030_bacterial_chemotaxis_partition.tsv"
OUT_MD = ROOT / "projects/P_PUTIDA/batches/ppu02030_bacterial_chemotaxis_partition.md"
GENE_ROOT = ROOT / "genes/PSEPK"


BUCKETS = {
    "known_named_mcp_receptor_panel": {
        "label": "Known or named MCP receptor panel",
        "module": "chemotaxis_receptor_panel_boundary",
        "action": "NEW_SUBMODULE",
        "note": "Reviewed or named methyl-accepting chemotaxis receptors; ligand specificity should be checked gene-by-gene.",
        "genes": ["mcpH", "ctpL", "mcpU", "mcpG", "mcpA", "pcaY", "mcpP", "mcpS", "mcpQ"],
    },
    "orphan_mcp_aerotaxis_receptors": {
        "label": "Orphan MCP/aerotaxis receptors",
        "module": "orphan_mcp_aerotaxis_receptors_boundary",
        "action": "NEW_SUBMODULE",
        "note": "Predicted MCP, sensory-box, or aerotaxis receptors curated as a first-pass boundary module while ligand specificity remains unresolved.",
        "genes": [
            "PP_0317",
            "PP_0584",
            "PP_0779",
            "PP_1819",
            "PP_1940",
            "PP_2111",
            "ctpH",
            "PP_2257",
            "PP_2823",
            "PP_3414",
            "PP_3557",
            "PP_4521",
            "PP_5021",
        ],
    },
    "periplasmic_binding_transport_spillovers": {
        "label": "Periplasmic binding/transport spillovers",
        "module": "dipeptide_ribose_binding_transport_boundary",
        "action": "EXISTING_OR_REUSE",
        "note": "Dipeptide, ribose, and sugar-binding proteins that enter the chemotaxis map through ligand-binding/transport context.",
        "genes": ["dppA-I", "dppA-II", "dppA-III", "rbsB", "PP_2757", "PP_2758", "dppA-IV"],
    },
    "chemotaxis_core_che_cluster": {
        "label": "Core Che signal-transduction cluster",
        "module": "bacterial_chemotaxis_core_boundary",
        "action": "NEW_SUBMODULE",
        "note": "CheW/CheA/CheY/CheZ/CheB core signal transduction and adaptation cluster.",
        "genes": ["PP_4332", "PP_4333", "cheB1", "cheA", "cheZ", "cheY"],
    },
    "chemotaxis_adaptation_accessory": {
        "label": "Chemotaxis adaptation/accessory proteins",
        "module": "chemotaxis_adaptation_accessory_boundary",
        "action": "NEW_SUBMODULE",
        "note": "CheV-like proteins, methylesterase/methyltransferase entries, and accessory response-regulator-like chemotaxis proteins outside the core cluster.",
        "genes": ["PP_0802", "PP_2128", "PP_3759", "cheR3", "cheR2", "PP_4393"],
    },
}


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


def main() -> None:
    rows = list(csv.DictReader(BATCH_TSV.open(), delimiter="\t"))
    row_by_gene = {row["suggested_review_name"]: row for row in rows}

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

    fields = [
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
    with OUT_TSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for row in rows:
            gene = row["suggested_review_name"]
            bucket_id = assigned[gene]
            info = BUCKETS[bucket_id]
            writer.writerow(
                {
                    "gene": gene,
                    "ordered_locus": row["ordered_locus"],
                    "uniprot_accession": row["uniprot_accession"],
                    "protein_name": row["protein_name"],
                    "partition_bucket": bucket_id,
                    "partition_label": info["label"],
                    "proposed_module": info["module"],
                    "recommended_action": info["action"],
                    "notes": info["note"],
                    "review_status": review_status(gene),
                    "curation_status": curation_status(gene),
                    "asta_research_status": asta_research_status(gene),
                }
            )

    counts = Counter(assigned.values())
    examples = defaultdict(list)
    for gene, bucket_id in assigned.items():
        if len(examples[bucket_id]) < 8:
            examples[bucket_id].append(gene)

    lines = [
        "---",
        'title: "PSEPK ppu02030 Bacterial chemotaxis partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK ppu02030: Bacterial chemotaxis partition",
        "",
        "KEGG ppu02030 is a bacterial chemotaxis umbrella. The PSEPK primary",
        "set mixes receptor panels, core Che signal transduction, accessory",
        "adaptation proteins, and periplasmic binding proteins that belong first",
        "to transport modules.",
        "",
        "## Outputs",
        "",
        f"- Source batch: `{BATCH_TSV.relative_to(ROOT)}`",
        f"- Partition table: `{OUT_TSV.relative_to(ROOT)}`",
        "",
        "## Partition Summary",
        "",
        "| Bucket | Genes | Proposed module | Action | Example genes |",
        "|---|---:|---|---|---|",
    ]
    for bucket_id, info in BUCKETS.items():
        lines.append(
            f"| `{bucket_id}` | {counts[bucket_id]} | `{info['module']}` | "
            f"{info['action']} | {', '.join(f'`{g}`' for g in examples[bucket_id])} |"
        )
    lines.extend(
        [
            "",
            "## Working Decisions",
            "",
            "- Do not curate all 41 primary genes as one bacterial-chemotaxis PR.",
            "- Keep dipeptide, ribose, and sugar-binding proteins with transport",
            "  modules unless there is direct receptor-level chemotaxis evidence.",
            "- Treat orphan MCP/aerotaxis receptors as a boundary receptor panel:",
            "  ligand specificity remains unresolved, but the bucket is now curated",
            "  and represented by `modules/orphan_mcp_aerotaxis_receptors_boundary.yaml`.",
            "- The strongest new chemotaxis-specific batches are the core Che cluster,",
            "  named receptor panel, and adaptation/accessory group.",
            "",
            "## Completed Sub-batches",
            "",
            "- `chemotaxis_core_che_cluster`: six genes present, Asta-backed,",
            "  first-pass curated, validated, and rendered; new module",
            "  `modules/bacterial_chemotaxis_core_boundary.yaml` created,",
            "  validated, and rendered. Asta retrieval was checked for all six genes, but the",
            "  new PP_4332/PP_4333/cheB1 decisions rely mainly on UniProt, GOA,",
            "  domain, and local cluster evidence because Asta did not return",
            "  curation-changing organism-specific papers for these proteins.",
            "- `chemotaxis_adaptation_accessory`: six genes present, Asta-backed,",
            "  first-pass curated, validated, and rendered; new module",
            "  `modules/chemotaxis_adaptation_accessory_boundary.yaml` created,",
            "  validated, and rendered. CheR2 is retained as the receptor",
            "  methyltransferase supported by UniProt and PMID:23677992, CheR3 is",
            "  kept as a broad unresolved methyltransferase candidate, and PP_3759",
            "  is retained as a methylesterase while response-regulator",
            "  over-propagation is removed.",
            "- `known_named_mcp_receptor_panel`: nine genes present, Asta-backed,",
            "  first-pass curated, validated, and rendered; new module",
            "  `modules/chemotaxis_receptor_panel_boundary.yaml` created,",
            "  validated, and rendered. The panel captures characterized purine,",
            "  amino-acid, polyamine, GABA, short-chain carboxylate, TCA/citrate,",
            "  and aromatic-acid receptors, while CtpL remains a ligand-unresolved",
            "  named MCP candidate.",
            "- `orphan_mcp_aerotaxis_receptors`: thirteen genes present,",
            "  Asta-backed, first-pass curated, validated, and rendered; new module",
            "  `modules/orphan_mcp_aerotaxis_receptors_boundary.yaml` created,",
            "  validated, and rendered. Ligand specificity remains unresolved for",
            "  the generic orphan MCPs, and PP_2111 SNARE-derived electronic",
            "  annotations were removed.",
            "",
            "## Next Steps",
            "",
            "- Treat ppu02030 chemotaxis sub-batches as complete for this first",
            "  pass: core Che signaling, adaptation/accessory proteins, named",
            "  receptor panel, and orphan MCP/aerotaxis receptor boundary are all",
            "  curated.",
            "- Keep `periplasmic_binding_transport_spillovers` with transport modules",
            "  unless direct receptor-level chemotaxis evidence is selected.",
            "- Run real Falcon module/pathway commands only after a concrete submodule",
            "  is selected; current Edison Falcon access failure mode is HTTP 402.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {OUT_TSV.relative_to(ROOT)}")
    print(f"Wrote {OUT_MD.relative_to(ROOT)}")
    for bucket_id, info in BUCKETS.items():
        print(f"{bucket_id}\t{counts[bucket_id]}\t{info['module']}")


if __name__ == "__main__":
    main()
