#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_4841-PP_4845 UrtABCDE importer."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"


def goa_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-goa.tsv"


def uniprot_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-uniprot.txt"


def asta_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md"


def support_goa(gene: str, term_id: str, label: str) -> dict:
    return {"reference_id": goa_ref(gene), "supporting_text": f"{term_id}\t{label}"}


def support_uniprot(gene: str, text: str) -> dict:
    return {"reference_id": uniprot_ref(gene), "supporting_text": text}


def support_asta(gene: str, text: str) -> dict:
    return {"reference_id": asta_ref(gene), "supporting_text": text}


def ensure_reference(doc: dict, ref_id: str, title: str, supporting_text: str | None = None) -> None:
    refs = doc.setdefault("references", [])
    for ref in refs:
        if ref.get("id") == ref_id:
            if supporting_text and not ref.get("findings"):
                ref["findings"] = [{"supporting_text": supporting_text}]
            return
    ref = {"id": ref_id, "title": title, "findings": []}
    if supporting_text:
        ref["findings"].append({"supporting_text": supporting_text})
    refs.append(ref)


def review(
    gene: str,
    term_id: str,
    label: str,
    summary: str,
    action: str,
    reason: str,
    *,
    proposed: list[dict] | None = None,
    extra_support: list[dict] | None = None,
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if extra_support:
        supported_by.extend(extra_support)
    result = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if proposed:
        result["proposed_replacement_terms"] = deepcopy(proposed)
    return result


def new_annotation(
    term: dict,
    qualifier: str,
    original_reference_id: str,
    summary: str,
    reason: str,
    supported_by: list[dict],
) -> dict:
    return {
        "term": deepcopy(term),
        "evidence_type": "IEA",
        "original_reference_id": original_reference_id,
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": supported_by,
        },
    }


UREA_TRANSPORT = {"id": "GO:0015840", "label": "urea transport"}
UREA_BINDING = {"id": "GO:0033219", "label": "urea binding"}
UREA_TRANSPORTER = {
    "id": "GO:0015204",
    "label": "urea transmembrane transporter activity",
}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
ABC_COMPLEX = {
    "id": "GO:0043190",
    "label": "ATP-binding cassette (ABC) transporter complex",
}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}


GENES = {
    "urtA": {
        "kind": "binding",
        "accession": "Q88DI4",
        "description": (
            "urtA encodes the signal-peptide-bearing periplasmic substrate-binding "
            "component of the PP_4841-PP_4845 UrtABCDE urea ABC uptake system. "
            "The product name and UrtA-specific InterPro domain support urea "
            "recognition, while the existing amino-acid transport annotation is "
            "treated as a broad family-transfer artifact."
        ),
        "product_text": "Full=Urea ABC transporter, periplasmic protein",
        "asta_text": "Protein Description:** SubName: Full=Urea ABC transporter, periplasmic protein",
        "signal_text": "FT   SIGNAL          1..27",
        "domain_text": "InterPro; IPR017777; ABC_urea-bd_UrtA.",
    },
    "urtB": {
        "kind": "permease_b",
        "accession": "Q88DI3",
        "description": (
            "urtB encodes a multi-pass inner-membrane permease component of the "
            "PP_4841-PP_4845 UrtABCDE urea ABC uptake system. UniProt names the "
            "protein as a urea ABC transporter, places it in the cell inner "
            "membrane, and assigns a UrtB-specific transporter domain."
        ),
        "product_text": "Full=Urea ABC transporter",
        "asta_text": "Protein Description:** SubName: Full=Urea ABC transporter",
        "location_text": "Cell inner membrane",
        "family_text": "Belongs to the binding-protein-dependent transport system",
        "domain_text": "InterPro; IPR017779; ABC_UrtB_bac.",
    },
    "urtC": {
        "kind": "permease_c",
        "accession": "Q88DI2",
        "description": (
            "urtC encodes the second multi-pass inner-membrane permease component "
            "of the PP_4841-PP_4845 UrtABCDE urea ABC uptake system. The local "
            "product name and UrtC-specific InterPro domain support a urea "
            "transporter role; branched-chain amino-acid annotations are likely "
            "spillover from LivM-like family features."
        ),
        "product_text": "Full=Urea ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Urea ABC transporter, permease protein",
        "location_text": "Cell inner membrane",
        "domain_text": "InterPro; IPR017778; ABC_transptr_urea_perm_UrtC.",
    },
    "urtD": {
        "kind": "atpase_d",
        "accession": "Q88DI1",
        "description": (
            "urtD encodes an ATP-binding energy-coupling subunit of the "
            "PP_4841-PP_4845 UrtABCDE urea ABC uptake system. The protein is an "
            "ABC transporter ATP-binding component with a UrtD-specific domain, "
            "supporting ATP hydrolysis coupled to urea import by the complex."
        ),
        "product_text": "Full=Urea ABC transporter, ATP-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Urea ABC transporter, ATP-binding protein",
        "domain_text": "InterPro; IPR017781; ABC_transptr_urea_ATP-bd_UrtD.",
        "ft_domain_text": "FT   DOMAIN          45..285",
    },
    "urtE": {
        "kind": "atpase_e",
        "accession": "Q88DI0",
        "description": (
            "urtE encodes the second ATP-binding energy-coupling subunit of the "
            "PP_4841-PP_4845 UrtABCDE urea ABC uptake system. Its ABC ATPase "
            "domain and UrtE-specific InterPro assignment support ATP hydrolysis "
            "coupled to urea import, while amino-acid/BCAA transport annotations "
            "are likely over-propagated from related amino-acid transporter "
            "families."
        ),
        "product_text": "Full=Urea ABC transporter, ATP-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Urea ABC transporter, ATP-binding protein",
        "family_text": "Belongs to the ABC transporter superfamily.",
        "domain_text": "InterPro; IPR017780; ABC_transptr_urea_ATP-bd_UrtE.",
        "ft_domain_text": "FT   DOMAIN          2..232",
    },
}


def binding_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["product_text"])
    asta = support_asta(gene, cfg["asta_text"])
    mapping = {
        "GO:0006865": (
            "Amino acid transport is not the right substrate-level process for this UrtA urea-binding component.",
            "MODIFY",
            "The product name and UrtA-specific InterPro domain support urea import rather than amino-acid transport.",
            [UREA_TRANSPORT],
            [product, support_uniprot(gene, cfg["domain_text"]), asta],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def permease_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["product_text"])
    asta = support_asta(gene, cfg["asta_text"])
    mapping = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this predicted inner-membrane Urt permease.",
            "ACCEPT",
            "UniProt places the Urt permease in the cell inner membrane.",
            None,
            [support_uniprot(gene, cfg["location_text"])],
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than plasma membrane for this bacterial inner-membrane permease.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also has a plasma-membrane annotation and UniProt predicts a cell inner-membrane protein.",
            None,
            [support_uniprot(gene, cfg["location_text"])],
        ),
        "GO:0022857": (
            "Generic transmembrane transporter activity is correct but should be replaced by urea transmembrane transporter activity.",
            "MODIFY",
            "The local Urt product name and Urt-specific domain support a urea transporter role.",
            [UREA_TRANSPORTER],
            [product, support_uniprot(gene, cfg["domain_text"]), asta],
        ),
        "GO:0055085": (
            "Transmembrane transport is correct but broad relative to the urea-import context.",
            "MODIFY",
            "Urea transport better captures the expected substrate and process for this Urt permease.",
            [UREA_TRANSPORT],
            [product, support_uniprot(gene, cfg["domain_text"]), asta],
        ),
        "GO:0015658": (
            "Branched-chain amino acid transporter activity is likely over-propagated from Liv-like family features rather than the UrtC substrate context.",
            "MODIFY",
            "The product name and UrtC-specific domain support urea transmembrane transporter activity.",
            [UREA_TRANSPORTER],
            [product, support_uniprot(gene, cfg["domain_text"]), asta],
        ),
        "GO:0015803": (
            "Branched-chain amino acid transport is likely a family-transfer artifact for this UrtC permease.",
            "MODIFY",
            "The local UrtABCDE locus supports urea transport rather than branched-chain amino acid transport.",
            [UREA_TRANSPORT],
            [product, support_uniprot(gene, cfg["domain_text"]), asta],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def atpase_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["product_text"])
    asta = support_asta(gene, cfg["asta_text"])
    domain = support_uniprot(gene, cfg["domain_text"])
    ft_domain = support_uniprot(gene, cfg["ft_domain_text"])
    mapping = {
        "GO:0000166": (
            "Nucleotide binding is true but too broad for this ABC ATP-binding component.",
            "MARK_AS_OVER_ANNOTATED",
            "The same record has the more informative ATP binding and ATP hydrolysis annotations.",
            None,
            [domain, ft_domain],
        ),
        "GO:0005524": (
            "ATP binding is correct for this ABC transporter nucleotide-binding component.",
            "ACCEPT",
            "The protein has an ABC ATP-binding domain and is named as a urea ABC transporter ATP-binding protein.",
            None,
            [product, domain, ft_domain],
        ),
        "GO:0005886": (
            "Plasma membrane localization is appropriate as a complex-associated annotation for this UrtD ATPase.",
            "ACCEPT",
            "The ATPase acts as part of the membrane UrtABCDE ABC transporter complex.",
            None,
            [product, domain],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is the core mechanistic activity for this Urt ABC ATPase subunit.",
            "ACCEPT",
            "ATP hydrolysis by the UrtD/UrtE ATPase pair is expected to energize urea import by the UrtABCDE transporter.",
            None,
            [product, domain, ft_domain, asta],
        ),
        "GO:0015658": (
            "Branched-chain amino acid transporter activity is likely over-propagated from related amino-acid ABC transporter families.",
            "MODIFY",
            "The local product name and UrtE-specific domain support contribution to urea transmembrane transporter activity instead.",
            [UREA_TRANSPORTER],
            [product, domain, asta],
        ),
        "GO:0015803": (
            "Branched-chain amino acid transport is likely a family-transfer artifact for this UrtE ATPase.",
            "MODIFY",
            "The local UrtABCDE locus supports urea transport rather than branched-chain amino acid transport.",
            [UREA_TRANSPORT],
            [product, domain, asta],
        ),
        "GO:0015807": (
            "L-amino acid transport is likely over-broad family transfer for this UrtE ATPase.",
            "MODIFY",
            "The local UrtABCDE locus supports urea transport as the more accurate process.",
            [UREA_TRANSPORT],
            [product, domain, asta],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def add_new_annotations(doc: dict, gene: str, cfg: dict) -> None:
    existing_ids = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}
    additions: list[dict] = []
    product = support_uniprot(gene, cfg["product_text"])
    asta = support_asta(gene, cfg["asta_text"])

    if cfg["kind"] == "binding":
        if UREA_BINDING["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    UREA_BINDING,
                    "enables",
                    uniprot_ref(gene),
                    "Urea binding is a useful missing molecular-function annotation for UrtA.",
                    "UrtA is the periplasmic substrate-binding component and has a UrtA-specific urea-binding domain.",
                    [product, support_uniprot(gene, cfg["domain_text"]), asta],
                )
            )
        if PERIPLASM["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    PERIPLASM,
                    "located_in",
                    uniprot_ref(gene),
                    "Outer membrane-bounded periplasmic-space localization is a useful missing annotation for UrtA.",
                    "UrtA is named as a periplasmic urea ABC transporter component and carries a signal peptide.",
                    [product, support_uniprot(gene, cfg["signal_text"])],
                )
            )
        if UREA_TRANSPORT["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    UREA_TRANSPORT,
                    "involved_in",
                    uniprot_ref(gene),
                    "Urea transport is a useful missing process annotation for UrtA.",
                    "The UrtA substrate-binding component is part of the PP_4841-PP_4845 UrtABCDE urea ABC importer.",
                    [product, support_uniprot(gene, cfg["domain_text"]), asta],
                )
            )
        if ABC_COMPLEX["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    ABC_COMPLEX,
                    "part_of",
                    uniprot_ref(gene),
                    "ABC transporter complex membership is a useful missing annotation for UrtA.",
                    "UrtA is the periplasmic substrate-binding component of the PP_4841-PP_4845 UrtABCDE ABC transporter.",
                    [product, support_uniprot(gene, cfg["domain_text"]), asta],
                )
            )

    if cfg["kind"].startswith("permease") and ABC_COMPLEX["id"] not in existing_ids:
        additions.append(
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                uniprot_ref(gene),
                f"ABC transporter complex membership is a useful missing annotation for {gene}.",
                f"{gene} is a UrtABCDE permease component in a binding-protein-dependent ABC transport system.",
                [product, support_uniprot(gene, cfg["domain_text"]), asta],
            )
        )

    if cfg["kind"].startswith("atpase"):
        if UREA_TRANSPORT["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    UREA_TRANSPORT,
                    "involved_in",
                    uniprot_ref(gene),
                    f"Urea transport is a useful missing process annotation for {gene}.",
                    f"{gene} is an ATP-binding energy-coupling component of the UrtABCDE urea ABC transporter.",
                    [product, support_uniprot(gene, cfg["domain_text"]), asta],
                )
            )
        if ABC_COMPLEX["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    ABC_COMPLEX,
                    "part_of",
                    uniprot_ref(gene),
                    f"ABC transporter complex membership is a useful missing annotation for {gene}.",
                    f"{gene} is one of the ATP-binding subunits of the UrtABCDE ABC transporter.",
                    [product, support_uniprot(gene, cfg["domain_text"]), asta],
                )
            )

    doc.setdefault("existing_annotations", []).extend(additions)


def build_core_function(gene: str, cfg: dict) -> dict:
    product = support_uniprot(gene, cfg["product_text"])
    asta = support_asta(gene, cfg["asta_text"])
    if cfg["kind"] == "binding":
        return {
            "description": "Periplasmic urea-binding substrate-recognition component of the predicted UrtABCDE importer.",
            "molecular_function": deepcopy(UREA_BINDING),
            "directly_involved_in": [deepcopy(UREA_TRANSPORT)],
            "locations": [deepcopy(PERIPLASM)],
            "in_complex": deepcopy(ABC_COMPLEX),
            "supported_by": [
                product,
                support_uniprot(gene, cfg["signal_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                asta,
            ],
        }
    if cfg["kind"].startswith("permease"):
        return {
            "description": "Multi-pass permease component contributing to the predicted UrtABCDE urea uptake system.",
            "contributes_to_molecular_function": deepcopy(UREA_TRANSPORTER),
            "directly_involved_in": [deepcopy(UREA_TRANSPORT)],
            "locations": [deepcopy(PLASMA_MEMBRANE)],
            "in_complex": deepcopy(ABC_COMPLEX),
            "supported_by": [
                product,
                support_uniprot(gene, cfg["location_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                asta,
            ],
        }
    core = {
        "description": "ATP-binding energy-coupling subunit catalyzing ATP hydrolysis for the predicted UrtABCDE urea uptake system.",
        "molecular_function": deepcopy(ATP_HYDROLYSIS),
        "contributes_to_molecular_function": deepcopy(UREA_TRANSPORTER),
        "directly_involved_in": [deepcopy(UREA_TRANSPORT)],
        "in_complex": deepcopy(ABC_COMPLEX),
        "supported_by": [
            support_goa(gene, "GO:0016887", "ATP hydrolysis activity"),
            product,
            support_uniprot(gene, cfg["domain_text"]),
            support_uniprot(gene, cfg["ft_domain_text"]),
            asta,
        ],
    }
    if gene == "urtD":
        core["locations"] = [deepcopy(PLASMA_MEMBRANE)]
    return core


def curate_gene(gene: str) -> None:
    cfg = GENES[gene]
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]
    doc["existing_annotations"] = [
        ann
        for ann in doc.get("existing_annotations", [])
        if not (
            ann.get("original_reference_id") == uniprot_ref(gene)
            and ann.get("review", {}).get("action") == "NEW"
        )
    ]

    for ann in doc.get("existing_annotations", []):
        term = ann["term"]
        term_id = term["id"]
        label = term["label"]
        if cfg["kind"] == "binding":
            ann["review"] = binding_review(gene, cfg, term_id, label)
        elif cfg["kind"].startswith("permease"):
            ann["review"] = permease_review(gene, cfg, term_id, label)
        else:
            ann["review"] = atpase_review(gene, cfg, term_id, label)

    add_new_annotations(doc, gene, cfg)
    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(
        doc,
        uniprot_ref(gene),
        f"UniProtKB entry for {gene} ({cfg['accession']})",
        cfg["product_text"],
    )
    ensure_reference(
        doc,
        asta_ref(gene),
        f"Asta retrieval report for {gene} ({cfg['accession']})",
        cfg["asta_text"],
    )
    doc["core_functions"] = [build_core_function(gene, cfg)]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "Does PP_4841-PP_4845 function as a high-affinity UrtABCDE urea importer "
                "in P. putida KT2440, and under which nitrogen or nickel/urease-related "
                "conditions is the locus expressed?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Measure urea uptake, growth on urea as nitrogen source, and urease-linked "
                "physiology for urtA, urtB, urtC, urtD, and urtE mutants or complemented strains."
            ),
            "experiment_type": "targeted transporter mutant substrate-uptake and growth assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=False))
    print(f"curated {path}")


def main() -> None:
    for gene in GENES:
        curate_gene(gene)


if __name__ == "__main__":
    main()
