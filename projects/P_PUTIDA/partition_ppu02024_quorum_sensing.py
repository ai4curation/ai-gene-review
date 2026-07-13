#!/usr/bin/env python3
"""Partition KEGG ppu02024 into curation-scale submodules.

KEGG "Quorum sensing" for PSEPK is an umbrella of transporters, response
regulators, efflux proteins, and surface-context genes. KT2440 does not present
as a simple LuxI/LuxR autoinducer-synthesis module in this primary bucket, so
this script routes genes to smaller modules or side-context buckets.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BATCH_TSV = ROOT / "projects/P_PUTIDA/batches/ppu02024_quorum_sensing_boundary.tsv"
OUT_TSV = ROOT / "projects/P_PUTIDA/batches/ppu02024_quorum_sensing_partition.tsv"
OUT_MD = ROOT / "projects/P_PUTIDA/batches/ppu02024_quorum_sensing_partition.md"
GENE_ROOT = ROOT / "genes/PSEPK"


BUCKETS = {
    "fur_iron_regulation_spillover": {
        "label": "Fur/iron regulation spillover",
        "module": "iron_homeostasis_regulation_boundary",
        "action": "SIDE_CONTEXT",
        "note": "Fur-family iron regulation context; not quorum-signal synthesis or reception.",
        "genes": ["fur__Q88RL0"],
    },
    "polyamine_abc_import": {
        "label": "Polyamine ABC import",
        "module": "polyamine_transport_boundary",
        "action": "EXISTING_OR_REUSE",
        "note": "Putrescine/spermidine/polyamine import systems; plausible quorum/biofilm context but best curated as transport.",
        "genes": [
            "potA",
            "PP_0412",
            "PP_0413",
            "PP_0414",
            "ydcV",
            "ydcU",
            "ydcT",
            "ydcS",
            "PP_2870",
            "PP_3814",
            "PP_3815",
            "PP_3816",
            "PP_3817",
        ],
    },
    "branched_chain_amino_acid_abc_import": {
        "label": "Branched-chain amino-acid ABC import",
        "module": "branched_chain_amino_acid_abc_import_boundary",
        "action": "EXISTING_OR_REUSE",
        "note": "Liv/Bra-like amino-acid import systems already routed through ABC-transporter submodules.",
        "genes": [
            "PP_0615",
            "PP_0616",
            "PP_0617",
            "PP_0618",
            "PP_0619",
            "livF-I",
            "livG",
            "livM",
            "livH",
            "livK",
            "PP_2748",
            "PP_2749",
            "PP_2750",
            "PP_2751",
            "PP_2752",
            "PP_2753",
            "PP_2767",
            "PP_2768",
            "PP_2769",
            "PP_2770",
            "livF-II",
            "braF",
            "braE",
            "braD",
            "PP_4867",
        ],
    },
    "surface_adhesion_singleton": {
        "label": "Surface adhesion singleton",
        "module": "surface_adhesion_boundary",
        "action": "DEFER",
        "note": "Surface-adhesion protein that may fit a biofilm/surface module rather than quorum sensing.",
        "genes": ["PP_0806"],
    },
    "phosphonate_abc_import": {
        "label": "Phosphonate/AEP ABC import",
        "module": "phosphonate_phosphinate_metabolism",
        "action": "EXISTING_OR_REUSE",
        "note": "2-aminoethylphosphonate ABC import context; route to phosphonate uptake/catabolism.",
        "genes": ["PP_1722", "PP_1723", "PP_1724", "PP_1726"],
    },
    "rnd_multidrug_efflux": {
        "label": "RND multidrug efflux",
        "module": "rnd_multidrug_efflux_boundary",
        "action": "NEW_SUBMODULE",
        "note": "MFP/RND efflux pair; resistance/export context rather than quorum sensing.",
        "genes": ["PP_2064", "PP_2065"],
    },
    "qsebc_like_two_component_regulation": {
        "label": "QseBC-like two-component regulation",
        "module": "qsebc_like_two_component_regulation_boundary",
        "action": "NEW_SUBMODULE",
        "note": "QseB/KdpE-like response regulators and paired sensor kinases; the closest ppu02024 regulatory signal bucket.",
        "genes": ["PP_2713", "PP_2714", "kdpE", "PP_4224", "qseB"],
    },
    "peptide_opine_glutathione_abc_import": {
        "label": "Peptide/opine/glutathione ABC import",
        "module": "peptide_opine_glutathione_abc_import_boundary",
        "action": "NEW_SUBMODULE",
        "note": "Dipeptide and Gsi/opine-like import systems; transport context rather than quorum sensing.",
        "genes": ["PP_3220", "PP_3221", "PP_3222", "PP_3223", "gsiA", "PP_4454", "gsiC", "PP_4458"],
    },
    "dmt_transporter_singleton": {
        "label": "DMT transporter singleton",
        "module": "dmt_transporter_boundary",
        "action": "DEFER",
        "note": "DMT-family transporter singleton with no clear quorum-sensing role in this first pass.",
        "genes": ["PP_3609"],
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
        'title: "PSEPK ppu02024 Quorum sensing partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK ppu02024: Quorum sensing partition",
        "",
        "KEGG ppu02024 is an umbrella map in PSEPK. The primary 60-gene set",
        "does not define a single LuxI/LuxR quorum-sensing module; it is mostly",
        "transport, response-regulator, efflux, and surface-context genes.",
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
            "- Do not curate all 60 primary genes as one quorum-sensing PR.",
            "- The largest component is branched-chain amino-acid ABC import, already",
            "  represented by a transport submodule; keep it out of a quorum-sensing",
            "  core module.",
            "- Polyamine import is biologically adjacent to signaling and biofilm",
            "  behavior, but should still be curated as transport unless direct",
            "  regulatory evidence changes the module boundary.",
            "- The clearest signaling sub-batch is the QseBC-like two-component group",
            "  (`PP_2713`, `PP_2714`, `kdpE`, `PP_4224`, `qseB`).",
            "- Fur, DMT transporter, surface adhesion, RND efflux, phosphonate import,",
            "  and peptide/opine/glutathione import are side/boundary contexts.",
            "",
            "## Completed Sub-batches",
            "",
            "- `rnd_multidrug_efflux`: two genes present, Asta-backed,",
            "  first-pass curated, validated, and rendered; new module",
            "  `modules/rnd_multidrug_efflux_boundary.yaml` created, validated,",
            "  and rendered. PP_2064 is treated as the membrane-fusion/adaptor",
            "  component that contributes to pump-level efflux activity, while",
            "  PP_2065 is retained as the inner-membrane RND xenobiotic",
            "  transporter.",
            "- `qsebc_like_two_component_regulation`: five genes present,",
            "  Asta-backed, first-pass curated, validated, and rendered; new",
            "  module `modules/qsebc_like_two_component_regulation_boundary.yaml`",
            "  created, validated, and rendered. PP_2714-PP_2713 and",
            "  PP_4224-qseB are treated as predicted local sensor kinase/response",
            "  regulator pairs, while kdpE remains an unresolved KdpE-like",
            "  response activator side branch.",
            "- `phosphonate_abc_import`: four genes present, Asta-backed,",
            "  first-pass curated, validated, and rendered; existing module",
            "  `modules/phosphonate_phosphinate_metabolism.yaml` extended,",
            "  validated, and rendered. PP_1722-PP_1726 are treated as a",
            "  second AEP/phosphonate ABC import candidate with substrate",
            "  range and direct PhnW handoff left as a knowledge gap.",
            "- `peptide_opine_glutathione_abc_import`: eight genes present,",
            "  Asta-backed, first-pass curated, validated, and rendered; new",
            "  module `modules/peptide_opine_glutathione_abc_import_boundary.yaml`",
            "  created, validated, and rendered. PP_3220-PP_3223 are treated",
            "  as a dipeptide-like ABC importer, while gsiA/PP_4454/gsiC/",
            "  PP_4458 are treated as a mixed Gsi/opine-like ABC import",
            "  boundary with substrate range unresolved.",
            "- `polyamine_abc_import`: thirteen genes present, Asta-backed,",
            "  first-pass curated, validated, and rendered; existing module",
            "  `modules/polyamine_transport_boundary.yaml` extended,",
            "  validated, and rendered. PP_0411-PP_0414, ydcV/ydcU/ydcT/",
            "  ydcS, and PP_3814-PP_3817 are treated as polyamine ABC",
            "  import candidates, while PP_2870 remains a binding-protein",
            "  singleton with unresolved transporter partners.",
            "- `fur_iron_regulation_spillover`: one gene present,",
            "  Asta-backed, first-pass curated, validated, and rendered;",
            "  new module `modules/iron_homeostasis_regulation_boundary.yaml`",
            "  created, validated, and rendered. PP_0119/fur__Q88RL0 is",
            "  treated as a Fur-family iron-homeostasis transcription",
            "  regulator side context, distinct from direct quorum sensing.",
            "- `surface_adhesion_singleton`: one gene present, Asta-backed,",
            "  first-pass curated, validated, and rendered; new module",
            "  `modules/surface_adhesion_boundary.yaml` created, validated,",
            "  and rendered. PP_0806 is treated as a large BapA/Bap-like",
            "  surface-adhesion/biofilm-boundary protein.",
            "- `dmt_transporter_singleton`: one gene present, Asta-backed,",
            "  first-pass curated, validated, and rendered; new module",
            "  `modules/dmt_transporter_boundary.yaml` created, validated,",
            "  and rendered. PP_3609 is treated as a DMT/YdcZ-family",
            "  membrane transporter with unresolved substrate.",
            "",
            "## Next Steps",
            "",
            "- The ppu02024 partition is first-pass complete at 60/60 primary",
            "  review folders and 60/60 Asta reports. Do not curate ppu02024",
            "  as one satisfiable quorum-sensing module; maintain the nine",
            "  boundary buckets instead.",
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
