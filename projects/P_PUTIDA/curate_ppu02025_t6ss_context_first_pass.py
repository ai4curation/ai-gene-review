#!/usr/bin/env python3
"""First-pass curation for the ppu02025 T6SS/biofilm-context bucket."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path("genes") / SPECIES
BATCH = Path("projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.tsv")

GO_REF_TITLES = {
    "GO_REF:0000003": "Gene Ontology annotation based on Enzyme Commission mapping",
}

TSSK = {"PP_2617", "PP_3093", "PP_4080"}
TSSG = {"PP_2620", "PP_3096", "PP_4078"}
TSSC = {"PP_2623", "puuD"}
TSSB = {"PP_2624", "PP_3100", "PP_4074"}
TSSA = {"PP_3088"}
TAGF = {"PP_5561"}


def read_rows() -> dict[str, dict[str, str]]:
    with BATCH.open(newline="", encoding="utf-8") as handle:
        rows = {
            row["gene"]: row
            for row in csv.DictReader(handle, delimiter="\t")
            if row["partition_bucket"] == "t6ss_biofilm_context"
        }
    if not rows:
        raise ValueError("No t6ss_biofilm_context rows found")
    return rows


def first_line(gene: str, filename: str, predicate) -> str:
    path = ROOT / gene / filename
    for line in path.read_text(encoding="utf-8").splitlines():
        if predicate(line):
            return line
    raise ValueError(f"No matching line in {path}")


def goa_support(gene: str, term_id: str) -> dict[str, str]:
    line = first_line(gene, f"{gene}-goa.tsv", lambda line: term_id in line)
    return {"reference_id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv", "supporting_text": line}


def uniprot_de_support(gene: str) -> dict[str, str]:
    line = first_line(gene, f"{gene}-uniprot.txt", lambda line: line.startswith("DE   "))
    return {"reference_id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt", "supporting_text": line}


def uniprot_domain_support(gene: str, token: str) -> dict[str, str]:
    line = first_line(gene, f"{gene}-uniprot.txt", lambda line: token in line)
    return {"reference_id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt", "supporting_text": line}


def asta_support(gene: str) -> dict[str, str]:
    line = first_line(
        gene,
        f"{gene}-deep-research-asta.md",
        lambda line: line.startswith("- **Protein Description:** "),
    )
    return {
        "reference_id": f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md",
        "supporting_text": line,
    }


def unique_references(existing: list[dict], gene: str) -> list[dict]:
    refs: list[dict] = []
    seen: set[str] = set()
    for ref in existing:
        ref_id = ref.get("id")
        if not ref_id or ref_id in seen:
            continue
        if ref_id in GO_REF_TITLES:
            ref = {"id": ref_id, "title": GO_REF_TITLES[ref_id], "findings": []}
        refs.append(ref)
        seen.add(ref_id)

    for ref in [
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
            "title": f"UniProtKB entry for {gene}",
            "findings": [
                {
                    "statement": (
                        "UniProt identity, protein name, family, domain, and GO metadata "
                        "used for first-pass pathway curation."
                    )
                }
            ],
        },
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
            "title": f"QuickGO GOA annotations for {gene}",
            "findings": [{"statement": "GOA table containing the annotations reviewed in this file."}],
        },
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md",
            "title": f"Asta retrieval report for {gene}",
            "findings": [
                {
                    "statement": (
                        "Asta retrieval used as fast gene-level context; no unsupported "
                        "hypotheses were imported."
                    )
                }
            ],
        },
    ]:
        local_name = ref["id"].split("/")[-1]
        if ref["id"] not in seen and (ROOT / gene / local_name).exists():
            refs.append(ref)
            seen.add(ref["id"])
    return refs


def product(row: dict[str, str]) -> str:
    return row["protein_name"].rstrip(".")


def description_for(gene: str, row: dict[str, str]) -> str:
    locus = row["ordered_locus"]
    name = product(row)
    if gene in TSSK:
        return (
            f"{gene} ({locus}) encodes {name}, a predicted type VI secretion system "
            "TssK-family baseplate component. TssK-like proteins are part of the "
            "baseplate machinery that helps organize sheath and tube assembly in "
            "contractile type VI secretion systems."
        )
    if gene in TSSG:
        return (
            f"{gene} ({locus}) encodes {name}, a predicted TssG-family baseplate "
            "component of a type VI secretion system. It is associated with T6SS "
            "baseplate assembly rather than with a resolved secreted effector activity."
        )
    if gene in TSSC:
        prefix = (
            "despite an EC-derived uricase product name, "
            if gene == "puuD"
            else ""
        )
        return (
            f"{gene} ({locus}) encodes {name}; {prefix}its InterPro/Pfam/PANTHER "
            "profile supports a TssC/VipB-family type VI secretion contractile sheath "
            "large-subunit role. The protein is predicted to act as a secretion-apparatus "
            "component rather than as a standalone metabolic enzyme."
        )
    if gene in TSSB:
        return (
            f"{gene} ({locus}) encodes {name}, a predicted TssB/VipA-family small "
            "subunit of the type VI secretion contractile sheath. It likely acts with "
            "TssC/VipB-family partners in sheath assembly or dynamics."
        )
    if gene in TSSA:
        return (
            f"{gene} ({locus}) encodes {name}, an ImpA/TssA-like type VI secretion "
            "system component. It is likely involved in T6SS sheath/baseplate assembly "
            "or initiation, although its precise apparatus role remains unresolved."
        )
    if gene in TAGF:
        return (
            f"{gene} ({locus}) encodes {name}, a TagF-family type VI secretion "
            "system-associated accessory protein. TagF-family proteins are associated "
            "with T6SS regulation or assembly rather than direct effector activity."
        )
    return (
        f"{gene} ({locus}) encodes {name}. It is included in the ppu02025 T6SS "
        "biofilm-context bucket, and its precise type VI secretion apparatus role "
        "remains unresolved."
    )


def core_description(gene: str) -> str:
    if gene in TSSK:
        return "Predicted TssK-family type VI secretion baseplate component."
    if gene in TSSG:
        return "Predicted TssG-family type VI secretion baseplate component."
    if gene in TSSC:
        return "Predicted TssC/VipB-family type VI secretion contractile sheath large subunit."
    if gene in TSSB:
        return "Predicted TssB/VipA-family type VI secretion contractile sheath small subunit."
    if gene in TSSA:
        return "Predicted ImpA/TssA-like type VI secretion assembly component."
    if gene in TAGF:
        return "Predicted TagF-family type VI secretion-associated accessory protein."
    return "Predicted type VI secretion-system component with unresolved precise molecular activity."


def curated_existing_annotation(gene: str, ann: dict) -> None:
    term = ann["term"]
    term_id = term["id"]
    if gene == "puuD" and term_id == "GO:0004846":
        ann["review"] = {
            "summary": (
                "The EC-derived urate oxidase activity annotation is likely a product-name/EC "
                "over-propagation for this locus."
            ),
            "action": "REMOVE",
            "reason": (
                "The only GOA row is an IEA UniProtKB-EC mapping from the unreviewed "
                "EC 1.7.3.3 product name, while UniProt family/domain evidence places "
                "the protein in the TssC/VipB type VI secretion sheath family. This "
                "supports treating PP_3099/puuD as a T6SS sheath component rather than "
                "as a urate oxidase enzyme."
            ),
            "supported_by": [
                goa_support(gene, "GO:0004846"),
                uniprot_de_support(gene),
                uniprot_domain_support(gene, "IPR010269"),
                uniprot_domain_support(gene, "PF05943"),
                asta_support(gene),
            ],
        }
        return
    ann["review"] = {
        "summary": f"{term.get('label', term_id)} was reviewed for the ppu02025 T6SS context.",
        "action": "UNDECIDED",
        "reason": "No explicit first-pass decision rule was available for this annotation.",
        "supported_by": [goa_support(gene, term_id), asta_support(gene)],
    }


def curate_gene(gene: str, row: dict[str, str]) -> None:
    path = ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = description_for(gene, row)

    annotations = data.get("existing_annotations", []) or []
    for ann in annotations:
        curated_existing_annotation(gene, ann)

    core_support = [uniprot_de_support(gene), asta_support(gene)]
    if gene in TSSK:
        core_support.append(uniprot_domain_support(gene, "T6SS_TssK"))
    elif gene in TSSG:
        core_support.append(uniprot_domain_support(gene, "T6SS_TssG"))
    elif gene in TSSC:
        core_support.append(uniprot_domain_support(gene, "IPR010269"))
    elif gene in TSSB:
        core_support.append(uniprot_domain_support(gene, "T6SS_TssB1"))
    elif gene in TSSA:
        core_support.append(uniprot_domain_support(gene, "TssA-like"))
    elif gene in TAGF:
        core_support.append(uniprot_domain_support(gene, "TagF"))

    data["core_functions"] = [
        {
            "description": core_description(gene),
            "supported_by": core_support,
        }
    ]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": (
                f"Which P. putida KT2440 T6SS locus and surface-associated phenotype "
                f"depends directly on {gene}, and is this gene required for secretion "
                "or only for apparatus assembly/regulation?"
            )
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Create a targeted {gene} perturbation and assay Hcp/VgrG secretion, "
                "T6SS-dependent interbacterial competition, and surface-growth or "
                "biofilm phenotypes under conditions where the neighboring T6SS locus "
                "is expressed."
            ),
            "experiment_type": "gene perturbation with secretion proteomics and surface-phenotype assay",
        }
    ]
    data["references"] = unique_references(data.get("references", []) or [], gene)
    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    rows = read_rows()
    for gene, row in rows.items():
        curate_gene(gene, row)


if __name__ == "__main__":
    main()
