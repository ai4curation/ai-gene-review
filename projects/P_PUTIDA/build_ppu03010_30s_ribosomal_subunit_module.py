#!/usr/bin/env python3
"""Build the ppu03010 bacterial 30S ribosomal subunit module."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path(__file__).resolve().parents[2]
BATCH = ROOT / "projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_partition.tsv"
OUT = ROOT / "modules/bacterial_30s_ribosomal_subunit_boundary.yaml"

BUCKET = "bacterial_30s_ribosomal_subunit"
CLUSTER_GENES = {
    "rpsL",
    "rpsG",
    "rpsJ",
    "rpsS",
    "rpsC",
    "rpsQ",
    "rpsN",
    "rpsH",
    "rpsE",
    "rpsM",
    "rpsK",
    "rpsD",
}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def term(term_id: str, label: str) -> dict[str, str]:
    return {"id": term_id, "label": label}


def descriptor(preferred_term: str, term_id: str | None = None, label: str | None = None, description: str | None = None) -> dict:
    out: dict[str, object] = {"preferred_term": preferred_term}
    if description:
        out["description"] = description
    if term_id and label:
        out["term"] = term(term_id, label)
    return out


def read_rows() -> list[dict[str, str]]:
    with BATCH.open(newline="", encoding="utf-8") as handle:
        return [
            row
            for row in csv.DictReader(handle, delimiter="\t")
            if row["partition_bucket"] == BUCKET
        ]


def annoton(row: dict[str, str]) -> dict:
    gene = row["gene"]
    product = row["protein_name"].rstrip(".")
    return {
        "id": f"{gene}_30s_structural_component",
        "label": f"{gene}: {product}",
        "participant": {
            "selector_type": "GENE",
            "gene": {"preferred_term": gene},
        },
        "function": descriptor(
            "structural constituent of ribosome",
            "GO:0003735",
            "structural constituent of ribosome",
            "Structural role in the bacterial 30S small ribosomal subunit.",
        ),
        "processes": [
            descriptor(
                "translation",
                "GO:0006412",
                "translation",
                "Protein synthesis carried out by the assembled ribosome.",
            )
        ],
        "locations": [
            descriptor(
                "small ribosomal subunit",
                "GO:0015935",
                "small ribosomal subunit",
                "30S small-subunit cellular-component context.",
            ),
            descriptor(
                "ribosome",
                "GO:0005840",
                "ribosome",
                "Whole ribosome context for translation.",
            ),
        ],
        "role_description": f"{gene} encodes {product}, curated as a 30S small-subunit structural protein.",
        "evidence": [
            {
                "source_id": f"file:PSEPK/{gene}/{gene}-ai-review.yaml",
                "title": f"Curated {gene} review",
                "statement": f"The first-pass review curates {gene} as a 30S ribosomal protein supporting translation.",
            }
        ],
    }


def part_node(node_id: str, label: str, description: str, rows: list[dict[str, str]]) -> dict:
    return {
        "id": node_id,
        "label": label,
        "module_type": "CELLULAR_COMPONENT",
        "description": description,
        "annotons": [annoton(row) for row in rows],
    }


def build_module(rows: list[dict[str, str]]) -> dict:
    cluster = [row for row in rows if row["gene"] in CLUSTER_GENES]
    distributed = [row for row in rows if row["gene"] not in CLUSTER_GENES]

    return {
        "id": "MODULE:bacterial_30s_ribosomal_subunit_boundary",
        "title": "Bacterial 30S ribosomal subunit boundary",
        "description": (
            "Boundary module for the KEGG ppu03010 30S ribosomal-protein subset in "
            "Pseudomonas putida KT2440. This module covers the 21 protein-coding "
            "small-subunit participants selected from the organism-specific ribosome map; "
            "large-subunit proteins are tracked separately in the planned 50S module."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu03010",
                "title": "Ribosome - Pseudomonas putida KT2440",
                "statement": (
                    "KEGG ppu03010 provides the organism-specific ribosome protein set "
                    "that was partitioned into 30S and 50S curation batches."
                ),
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_partition.tsv",
                "title": "ppu03010 bacterial ribosome partition table",
                "statement": (
                    "The partition table assigns rpsU, rpsL, rpsG, rpsJ, rpsS, rpsC, "
                    "rpsQ, rpsN, rpsH, rpsE, rpsM, rpsK, rpsD, rpsT, rpsI, rpsP, rpsB, "
                    "rpsA, rpsO, rpsR, and rpsF to the bacterial 30S ribosomal subunit bucket."
                ),
            },
            {
                "source_id": "file:projects/P_PUTIDA/curate_ppu03010_30s_ribosomal_subunit_first_pass.py",
                "title": "ppu03010 30S first-pass curation script",
                "statement": (
                    "The script applies the light first-pass annotation decisions to all 21 "
                    "30S ribosomal-protein reviews and preserves term-specific GOA evidence."
                ),
            },
        ],
        "notes": (
            "This is a protein-participant boundary module, not a full biochemical model of "
            "bacterial translation. The 16S rRNA molecule and initiation/elongation/release "
            "factors are outside this ppu03010 protein sub-batch unless they appear in a later "
            "curation bucket."
        ),
        "module": {
            "id": "bacterial_30s_ribosomal_subunit_boundary",
            "label": "Bacterial 30S ribosomal subunit boundary",
            "module_type": "CELLULAR_COMPONENT",
            "description": (
                "Curated 30S small ribosomal subunit protein boundary for the PSEPK ppu03010 "
                "ribosome pathway batch."
            ),
            "concepts": [
                descriptor(
                    "small ribosomal subunit",
                    "GO:0015935",
                    "small ribosomal subunit",
                    "The 30S small subunit component represented by this module.",
                ),
                descriptor(
                    "ribosome",
                    "GO:0005840",
                    "ribosome",
                    "Whole ribosome context for translation.",
                ),
                descriptor(
                    "structural constituent of ribosome",
                    "GO:0003735",
                    "structural constituent of ribosome",
                    "Shared molecular role of the 30S ribosomal proteins.",
                ),
                descriptor(
                    "translation",
                    "GO:0006412",
                    "translation",
                    "Protein synthesis process supported by the assembled 30S subunit.",
                ),
                descriptor(
                    "ribosomal RNA binding",
                    "GO:0019843",
                    "rRNA binding",
                    "Specific rRNA-contact activity retained for many individual 30S proteins.",
                ),
            ],
            "context": {
                "taxa": [
                    descriptor(
                        "Pseudomonas putida KT2440",
                        "NCBITaxon:160488",
                        "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)",
                    )
                ],
                "cellular_components": [
                    descriptor("small ribosomal subunit", "GO:0015935", "small ribosomal subunit"),
                    descriptor("ribosome", "GO:0005840", "ribosome"),
                ],
            },
            "parts": [
                {
                    "order": 1,
                    "role": "S10-spc-alpha-region 30S core proteins",
                    "node": part_node(
                        "s10_spc_alpha_region_30s_proteins",
                        "S10-spc-alpha-region 30S proteins",
                        (
                            "Conserved 30S ribosomal proteins from the major ribosomal-protein "
                            "cluster in the ppu03010 partition."
                        ),
                        cluster,
                    ),
                },
                {
                    "order": 2,
                    "role": "Distributed 30S proteins",
                    "node": part_node(
                        "distributed_30s_proteins",
                        "Distributed 30S proteins",
                        (
                            "Small-subunit ribosomal proteins encoded outside the main S10-spc-alpha "
                            "cluster, including S1, S2, S6/S18, S15, S16, S20, and S21."
                        ),
                        distributed,
                    ),
                },
            ],
        },
    }


def main() -> None:
    rows = read_rows()
    if len(rows) != 21:
        raise SystemExit(f"Expected 21 30S rows, found {len(rows)}")
    data = build_module(rows)
    OUT.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
