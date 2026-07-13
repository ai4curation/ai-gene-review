#!/usr/bin/env python3
"""First-pass curation for the ppu04122 MoCo sulfur-relay gap genes."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path("genes") / SPECIES


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000104": (
        "Electronic Gene Ontology annotations created by transferring manual GO annotations between "
        "related proteins based on shared sequence features"
    ),
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


GENES: dict[str, dict] = {
    "moeB": {
        "description": (
            "moeB encodes molybdopterin-synthase adenylyltransferase, the MoeB enzyme that activates the "
            "MoaD sulfur-carrier subunit by ATP-dependent C-terminal adenylylation during molybdopterin "
            "and molybdenum cofactor biosynthesis."
        ),
        "decisions": {
            "GO:0003824": (
                "MARK_AS_OVER_ANNOTATED",
                "Generic catalytic activity is true but uninformative when the EC/Rhea-backed molybdopterin-synthase adenylyltransferase activity is available.",
            ),
            "GO:0004792": (
                "REMOVE",
                "Thiosulfate-cyanide sulfurtransferase activity describes rhodanese-type sulfur transfer, not the ATP-dependent MoaD adenylylation reaction described for MoeB.",
            ),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for this soluble bacterial MoCo-biosynthesis enzyme."),
            "GO:0005829": ("KEEP_AS_NON_CORE", "cytosol is redundant bacterial soluble-enzyme localization context relative to cytoplasm."),
            "GO:0008146": (
                "REMOVE",
                "Sulfotransferase activity is not the direct MoeB reaction; MoeB activates the MoaD C-terminus by adenylylation rather than transferring a sulfate or sulfur group.",
            ),
            "GO:0008641": (
                "KEEP_AS_NON_CORE",
                "MoeB is mechanistically related to ubiquitin-like activating enzymes, but the specific MoaD adenylyltransferase term is more informative for this pathway.",
            ),
            "GO:0016779": (
                "KEEP_AS_NON_CORE",
                "Nucleotidyltransferase activity is a broad parent context for the ATP-dependent adenylyltransferase reaction.",
            ),
            "GO:0061605": (
                "ACCEPT",
                "Molybdopterin-synthase adenylyltransferase activity captures the direct MoeB reaction on the MoaD sulfur-carrier protein.",
            ),
        },
        "core": [
            {
                "description": "MoeB ATP-dependent adenylyltransferase activation of the MoaD sulfur-carrier subunit.",
                "molecular_function": term("GO:0061605", "molybdopterin-synthase adenylyltransferase activity"),
                "directly_involved_in": [term("GO:0006777", "Mo-molybdopterin cofactor biosynthetic process")],
                "locations": [term("GO:0005737", "cytoplasm")],
            }
        ],
    },
    "moaD": {
        "description": (
            "moaD encodes the molybdopterin synthase sulfur-carrier subunit. In the molybdopterin biosynthesis "
            "sulfur-relay step, MoaD is activated by MoeB and used with MoaE to insert sulfur into cyclic "
            "pyranopterin monophosphate, producing molybdopterin."
        ),
        "decisions": {
            "GO:0006777": (
                "ACCEPT",
                "Mo-molybdopterin cofactor biosynthetic process is the pathway role supported by the MoaD family assignment.",
            ),
            "GO:1990133": (
                "ACCEPT",
                "Molybdopterin adenylyltransferase complex membership captures the MoeB/MoaD activation complex context assigned by TreeGrafter.",
            ),
        },
        "core": [
            {
                "description": "MoaD sulfur-carrier subunit activated by MoeB and used by molybdopterin synthase in MoCo biosynthesis.",
                "molecular_function": term("GO:0097163", "sulfur carrier activity"),
                "directly_involved_in": [term("GO:0006777", "Mo-molybdopterin cofactor biosynthetic process")],
                "in_complex": term("GO:1990133", "molybdopterin adenylyltransferase complex"),
            }
        ],
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def goa_snippet(row: dict[str, str]) -> str:
    return f"{row['GO TERM']}\t{row['GO NAME']}"


def line_containing(path: Path, pattern: str) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if pattern in line:
            return line
    raise ValueError(f"Pattern not found in {path}: {pattern}")


def uniprot_identity_snippet(path: Path) -> str:
    for pattern in ("CC   -!- FUNCTION:", "DE   RecName: Full=", "DE   SubName: Full="):
        try:
            return line_containing(path, pattern)
        except ValueError:
            pass
    return path.read_text(encoding="utf-8").splitlines()[0]


def uniprot_go_snippet(path: Path, term_id: str) -> str | None:
    for line in path.read_text(encoding="utf-8").splitlines():
        if f"GO; {term_id};" in line:
            return line
    return None


def asta_support(gene: str) -> dict[str, str]:
    review = yaml.safe_load((ROOT / gene / f"{gene}-ai-review.yaml").read_text(encoding="utf-8"))
    return {
        "reference_id": f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md",
        "supporting_text": f"uniprot_accession: {review['id']}",
    }


def ensure_references(data: dict, gene: str, gene_dir: Path) -> None:
    references = []
    seen: set[str] = set()
    for ref in data.get("references") or []:
        ref_id = ref.get("id")
        if not ref_id or ref_id in seen:
            continue
        if ref_id in GO_REF_TITLES:
            ref = {"id": ref_id, "title": GO_REF_TITLES[ref_id], "findings": []}
        references.append(ref)
        seen.add(ref_id)

    uniprot = gene_dir / f"{gene}-uniprot.txt"
    if uniprot.exists():
        ref_id = f"file:{SPECIES}/{gene}/{gene}-uniprot.txt"
        if ref_id not in seen:
            references.append(
                {
                    "id": ref_id,
                    "title": f"UniProtKB entry for {gene}",
                    "findings": [
                        {
                            "statement": "UniProt provides protein identity, reaction, domain/family context, and GO cross-references used in this first-pass review.",
                            "supporting_text": uniprot_identity_snippet(uniprot),
                        }
                    ],
                }
            )
            seen.add(ref_id)

    goa = gene_dir / f"{gene}-goa.tsv"
    if goa.exists():
        ref_id = f"file:{SPECIES}/{gene}/{gene}-goa.tsv"
        if ref_id not in seen:
            references.append(
                {
                    "id": ref_id,
                    "title": f"QuickGO GOA annotations for {gene}",
                    "findings": [{"statement": "The fetched GOA table contains the annotations reviewed for this gene."}],
                }
            )
            seen.add(ref_id)

    asta = gene_dir / f"{gene}-deep-research-asta.md"
    if asta.exists():
        ref_id = f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md"
        if ref_id not in seen:
            references.append(
                {
                    "id": ref_id,
                    "title": f"Asta retrieval report for {gene}",
                    "findings": [
                        {
                            "statement": "Asta retrieval was generated for this first-pass review and used as lightweight identity/retrieval context.",
                            "supporting_text": asta_support(gene)["supporting_text"],
                        }
                    ],
                }
            )
    data["references"] = references


def support_for_existing(gene: str, term_id: str, row: dict[str, str] | None) -> list[dict[str, str]]:
    support: list[dict[str, str]] = []
    if row is not None:
        support.append(
            {
                "reference_id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
                "supporting_text": goa_snippet(row),
            }
        )
    uniprot = ROOT / gene / f"{gene}-uniprot.txt"
    if uniprot.exists():
        go_line = uniprot_go_snippet(uniprot, term_id)
        if go_line:
            support.append(
                {
                    "reference_id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
                    "supporting_text": go_line,
                }
            )
        else:
            support.append(
                {
                    "reference_id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
                    "supporting_text": uniprot_identity_snippet(uniprot),
                }
            )
    if (ROOT / gene / f"{gene}-deep-research-asta.md").exists():
        support.append(asta_support(gene))
    return support


def action_summary(action: str, gene: str, label: str) -> str:
    if action == "ACCEPT":
        return f"{label} is accepted for {gene} in the MoCo sulfur-relay first-pass review."
    if action == "KEEP_AS_NON_CORE":
        return f"{label} is retained for {gene} as supporting but non-core context."
    if action == "MARK_AS_OVER_ANNOTATED":
        return f"{label} is broader than the most informative MoCo sulfur-relay role for {gene}."
    if action == "REMOVE":
        return f"{label} is removed for {gene} because it does not match the curated MoeB/MoaD reaction context."
    return f"{label} was reviewed for {gene}."


def review_existing_annotation(gene: str, annotation: dict, goa_rows: list[dict[str, str]], decisions: dict[str, tuple[str, str]]) -> None:
    term_data = annotation["term"]
    term_id = term_data["id"]
    label = term_data["label"]
    row = next((item for item in goa_rows if item["GO TERM"] == term_id and item["GO NAME"] == label), None)
    action, reason = decisions.get(term_id, ("KEEP_AS_NON_CORE", "This annotation is plausible context but not the main MoCo first-pass role."))
    annotation["review"] = {
        "summary": action_summary(action, gene, label),
        "action": action,
        "reason": reason,
        "supported_by": support_for_existing(gene, term_id, row),
    }


def core_support(gene: str, core: dict, annotations: list[dict], goa_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    support: list[dict[str, str]] = []
    term_ids: set[str] = set()
    for slot in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
        if isinstance(core.get(slot), dict):
            term_ids.add(core[slot]["id"])
    for slot in ("directly_involved_in", "locations"):
        for item in core.get(slot, []) or []:
            term_ids.add(item["id"])

    for row in goa_rows:
        if row["GO TERM"] in term_ids:
            support.append(
                {
                    "reference_id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
                    "supporting_text": goa_snippet(row),
                }
            )

    for annotation in annotations:
        if annotation.get("term", {}).get("id") not in term_ids:
            continue
        for item in annotation.get("review", {}).get("supported_by") or []:
            support.append(item)

    uniprot = ROOT / gene / f"{gene}-uniprot.txt"
    if uniprot.exists():
        support.append(
            {
                "reference_id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
                "supporting_text": uniprot_identity_snippet(uniprot),
            }
        )
    if (ROOT / gene / f"{gene}-deep-research-asta.md").exists():
        support.append(asta_support(gene))

    deduped: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for item in support:
        key = (item["reference_id"], item["supporting_text"])
        if key not in seen:
            deduped.append(item)
            seen.add(key)
    return deduped


def curate_gene(gene: str, cfg: dict) -> None:
    gene_dir = ROOT / gene
    review_path = gene_dir / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(review_path.read_text(encoding="utf-8")) or {}
    goa_rows = read_tsv(gene_dir / f"{gene}-goa.tsv")

    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_references(data, gene, gene_dir)

    for annotation in data.get("existing_annotations") or []:
        review_existing_annotation(gene, annotation, goa_rows, cfg.get("decisions", {}))

    core_functions: list[dict] = []
    for core_spec in cfg.get("core", []):
        core = dict(core_spec)
        core["supported_by"] = core_support(gene, core, data.get("existing_annotations") or [], goa_rows)
        core_functions.append(core)
    data["core_functions"] = core_functions
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {"question": f"What is the precise paralog-specific contribution of {gene} to molybdopterin/MoCo biosynthesis in P. putida KT2440?"}
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Perturb {gene} and assay molybdopterin or molybdoenzyme activity, with genetic complementation to test the assigned MoCo sulfur-relay role."
            ),
            "experiment_type": "gene perturbation and molybdenum-cofactor pathway assay",
        }
    ]

    review_path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=120),
        encoding="utf-8",
    )


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
