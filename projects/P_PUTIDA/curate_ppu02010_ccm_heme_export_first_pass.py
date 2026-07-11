#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_4324-PP_4327 CcmABCD system."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"
MODULE_PATH = Path("modules/ccm_heme_export_cytochrome_c_maturation_boundary.yaml")


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


def new_annotation(term: dict, qualifier: str, gene: str, summary: str, reason: str, supported_by: list[dict]) -> dict:
    return {
        "term": deepcopy(term),
        "evidence_type": "IEA",
        "original_reference_id": uniprot_ref(gene),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": supported_by,
        },
    }


HEME_TRANSPORT = {"id": "GO:0015886", "label": "heme transport"}
HEME_TRANSMEMBRANE_TRANSPORT = {"id": "GO:0035351", "label": "heme transmembrane transport"}
CYTOCHROME_COMPLEX_ASSEMBLY = {"id": "GO:0017004", "label": "cytochrome complex assembly"}
CYTOCHROME_C_BIOSYNTHESIS = {"id": "GO:1903607", "label": "cytochrome c biosynthetic process"}
HEME_TRANSMEMBRANE_TRANSPORTER = {
    "id": "GO:0015232",
    "label": "heme transmembrane transporter activity",
}
ABC_HEME_TRANSPORTER = {"id": "GO:0015439", "label": "ABC-type heme transporter activity"}
HEME_BINDING = {"id": "GO:0020037", "label": "heme binding"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
TRANSMEMBRANE_TRANSPORTER = {"id": "GO:0022857", "label": "transmembrane transporter activity"}
TRANSMM_TRANSPORT = {"id": "GO:0055085", "label": "transmembrane transport"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
MEMBRANE = {"id": "GO:0016020", "label": "membrane"}
ABC_COMPLEX = {
    "id": "GO:0043190",
    "label": "ATP-binding cassette (ABC) transporter complex",
}


GENES = {
    "ccmD": {
        "kind": "accessory_membrane",
        "accession": "Q88EX8",
        "description": (
            "ccmD encodes a small inner-membrane CcmD/CycX/HelD-family protein in "
            "the Ccm heme-handling system for cytochrome c maturation. The protein "
            "is required for moving heme to the periplasmic side of the cell "
            "envelope during c-type cytochrome biogenesis and is predicted to "
            "contain a single transmembrane segment."
        ),
        "product_text": "Full=Heme exporter protein D",
        "asta_text": "Protein Description:** RecName: Full=Heme exporter protein D",
        "function_text": "Required for the export of heme to the periplasm for the",
        "biogenesis_text": "biogenesis of c-type cytochromes.",
        "location_text": "Cell inner membrane",
        "topology_text": "FT   TRANSMEM        20..40",
        "family_text": "Belongs to the CcmD/CycX/HelD family.",
        "domain_text": "InterPro; IPR052075; Heme_exporter_D.",
    },
    "ccmC": {
        "kind": "heme_membrane",
        "accession": "Q88EX7",
        "description": (
            "ccmC encodes a multi-pass inner-membrane CcmC/CycZ/HelC-family heme "
            "exporter and cytochrome c-type biogenesis protein. It contributes to "
            "heme handling across the inner membrane and supports cytochrome "
            "c-type biogenesis through conserved CcmC/CcsA-family domains."
        ),
        "product_text": "Full=Heme exporter protein C",
        "asta_text": "Protein Description:** RecName: Full=Heme exporter protein C",
        "function_text": "Required for the export of heme to the periplasm for the",
        "biogenesis_text": "biogenesis of c-type cytochromes.",
        "location_text": "Cell inner membrane",
        "topology_text": "Multi-pass membrane protein",
        "family_text": "Belongs to the CcmC/CycZ/HelC family.",
        "domain_text": "InterPro; IPR003557; Cyt_c_biogenesis_CcmC.",
        "assembly_domain_text": "InterPro; IPR002541; Cyt_c_assembly.",
    },
    "ccmB": {
        "kind": "heme_membrane",
        "accession": "Q88EX6",
        "description": (
            "ccmB encodes a multi-pass inner-membrane CcmB/CycW/HelB-family "
            "component of the CcmAB heme-handling ABC system required for c-type "
            "cytochrome biogenesis. It is the predicted membrane translocation "
            "component paired with the CcmA ATP-binding energy-coupling subunit."
        ),
        "product_text": "Full=Heme exporter protein B",
        "asta_text": "Protein Description:** RecName: Full=Heme exporter protein B",
        "function_text": "Required for the export of heme to the periplasm for the",
        "biogenesis_text": "biogenesis of c-type cytochromes.",
        "location_text": "Cell inner membrane",
        "topology_text": "Multi-pass membrane protein",
        "family_text": "Belongs to the CcmB/CycW/HelB family.",
        "domain_text": "InterPro; IPR003544; Cyt_c_biogenesis_CcmB.",
    },
    "ccmA": {
        "kind": "atpase",
        "accession": "Q88EX5",
        "description": (
            "ccmA encodes the ATP-binding nucleotide-binding subunit of the CcmAB "
            "ABC transporter complex involved in cytochrome c-type biogenesis. It "
            "hydrolyzes ATP at the inner membrane to energize the CcmAB "
            "heme-handling system, although the exact direct transport role of "
            "CcmA is unresolved in the reviewed UniProt annotation."
        ),
        "product_text": "Full=Cytochrome c biogenesis ATP-binding export protein CcmA",
        "asta_text": "Protein Description:** RecName: Full=Cytochrome c biogenesis ATP-binding export protein CcmA",
        "function_text": "Part of the ABC transporter complex CcmAB involved in the",
        "biogenesis_text": "biogenesis of c-type cytochromes; once thought to export heme, this",
        "uncertain_text": "does not seem to be the case, but its exact role is uncertain.",
        "energy_text": "Responsible for energy coupling to the transport system.",
        "catalytic_text": "Reaction=heme b(in) + ATP + H2O = heme b(out) + ADP + phosphate + H(+);",
        "subunit_text": "The complex is composed of two ATP-binding proteins (CcmA) and",
        "subunit_b_text": "two transmembrane proteins (CcmB).",
        "location_text": "Cell inner membrane",
        "topology_text": "Peripheral membrane protein",
        "family_text": "Belongs to the ABC transporter superfamily. CcmA exporter",
        "domain_text": "InterPro; IPR005895; ABC_transptr_haem_export_CcmA.",
        "ft_domain_text": "FT   DOMAIN          3..205",
    },
}


def ccmD_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["product_text"])
    function = support_uniprot(gene, cfg["function_text"])
    biogenesis = support_uniprot(gene, cfg["biogenesis_text"])
    asta = support_asta(gene, cfg["asta_text"])
    mapping = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for the predicted inner-membrane CcmD protein.",
            "ACCEPT",
            "UniProt places CcmD in the cell inner membrane and predicts a transmembrane segment.",
            None,
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["topology_text"])],
        ),
        "GO:0015886": (
            "Heme transport is a correct process annotation for CcmD.",
            "ACCEPT",
            "UniProt describes CcmD as required for export of heme to the periplasm during c-type cytochrome biogenesis.",
            None,
            [product, function, biogenesis, asta],
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than the plasma-membrane annotation for this inner-membrane protein.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also carries a plasma-membrane annotation and UniProt places CcmD in the cell inner membrane.",
            None,
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["topology_text"])],
        ),
        "GO:0017004": (
            "Cytochrome complex assembly is appropriate for CcmD's c-type cytochrome biogenesis role.",
            "ACCEPT",
            "CcmD is a CcmD-family heme exporter component required for c-type cytochrome biogenesis.",
            None,
            [product, function, biogenesis, support_uniprot(gene, cfg["family_text"])],
        ),
        "GO:1903607": (
            "Cytochrome c biosynthetic process is the specific biological process for CcmD.",
            "ACCEPT",
            "The CcmD function line directly links heme export to the biogenesis of c-type cytochromes.",
            None,
            [function, biogenesis, support_uniprot(gene, cfg["domain_text"]), asta],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def heme_membrane_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["product_text"])
    function = support_uniprot(gene, cfg["function_text"])
    biogenesis = support_uniprot(gene, cfg["biogenesis_text"])
    domain = support_uniprot(gene, cfg["domain_text"])
    assembly_domain = support_uniprot(gene, cfg.get("assembly_domain_text", cfg["domain_text"]))
    asta = support_asta(gene, cfg["asta_text"])
    mapping = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this predicted inner-membrane Ccm component.",
            "ACCEPT",
            "UniProt places the protein in the cell inner membrane as a multi-pass membrane protein.",
            None,
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["topology_text"])],
        ),
        "GO:0015232": (
            "Heme transmembrane transporter activity is appropriate for this Ccm heme-handling membrane component.",
            "ACCEPT",
            "The product name, Ccm-family domain, and function annotation support a role in heme movement across the inner membrane.",
            None,
            [product, function, domain, asta],
        ),
        "GO:0015886": (
            "Heme transport is the correct first-pass process for this Ccm membrane component.",
            "ACCEPT",
            "UniProt describes the protein as required for export of heme to the periplasm for c-type cytochrome biogenesis.",
            None,
            [function, biogenesis, domain, asta],
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than plasma membrane for this bacterial inner-membrane protein.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also has a plasma-membrane annotation and UniProt places the protein in the cell inner membrane.",
            None,
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["topology_text"])],
        ),
        "GO:0017004": (
            "Cytochrome complex assembly is appropriate for this Ccm heme-handling component.",
            "ACCEPT",
            "Heme delivery/export by Ccm components is required for c-type cytochrome biogenesis and assembly.",
            None,
            [function, biogenesis, domain],
        ),
        "GO:1903607": (
            "Cytochrome c biosynthetic process is appropriate for this Ccm component.",
            "ACCEPT",
            "The protein is required for heme export to the periplasm for c-type cytochrome biogenesis.",
            None,
            [function, biogenesis, domain, asta],
        ),
        "GO:0020037": (
            "Heme binding is plausible for CcmC as a heme-handling membrane component.",
            "ACCEPT",
            "The CcmC product and CcmC/CcsA-family domains support heme binding as part of the heme-handling step.",
            None,
            [product, assembly_domain, domain],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def atpase_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["product_text"])
    function = support_uniprot(gene, cfg["function_text"])
    biogenesis = support_uniprot(gene, cfg["biogenesis_text"])
    uncertain = support_uniprot(gene, cfg["uncertain_text"])
    energy = support_uniprot(gene, cfg["energy_text"])
    catalytic = support_uniprot(gene, cfg["catalytic_text"])
    domain = support_uniprot(gene, cfg["domain_text"])
    asta = support_asta(gene, cfg["asta_text"])
    mapping = {
        "GO:0005524": (
            "ATP binding is correct for the CcmA ABC ATP-binding subunit.",
            "ACCEPT",
            "CcmA has an ABC transporter nucleotide-binding domain and is named as an ATP-binding export protein.",
            None,
            [product, support_uniprot(gene, cfg["ft_domain_text"]), domain],
        ),
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this inner-membrane-associated CcmA ATPase.",
            "ACCEPT",
            "UniProt places CcmA at the cell inner membrane as a peripheral membrane protein.",
            None,
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["topology_text"])],
        ),
        "GO:0015439": (
            "ABC-type heme transporter activity is appropriate as the complex-level activity supported for CcmA.",
            "ACCEPT",
            "CcmA is the ATP-binding energy-coupling subunit of CcmAB; UniProt still carries EC-linked heme export while noting the exact CcmA role is uncertain.",
            None,
            [function, biogenesis, uncertain, energy, catalytic, domain],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is the core mechanistic activity of CcmA.",
            "ACCEPT",
            "CcmA is responsible for energy coupling to the CcmAB transport system and carries the ABC transporter ATP-binding domain.",
            None,
            [energy, catalytic, support_uniprot(gene, cfg["ft_domain_text"]), asta],
        ),
        "GO:0017004": (
            "Cytochrome complex assembly is appropriate for CcmA's CcmAB role.",
            "ACCEPT",
            "UniProt places CcmA in the CcmAB complex involved in c-type cytochrome biogenesis.",
            None,
            [function, biogenesis, energy],
        ),
        "GO:0022857": (
            "Generic transmembrane transporter activity is correct but less informative than ABC-type heme transporter activity for CcmA.",
            "MODIFY",
            "The CcmA record supports the CcmAB ABC heme-transporter context, while also noting uncertainty about CcmA's exact direct role.",
            [ABC_HEME_TRANSPORTER],
            [function, uncertain, energy, catalytic, domain],
        ),
        "GO:0035351": (
            "Heme transmembrane transport is appropriate for CcmA as a CcmAB energy-coupling subunit.",
            "ACCEPT",
            "CcmA is part of the CcmAB system involved in the heme-handling step for c-type cytochrome biogenesis.",
            None,
            [function, biogenesis, energy, catalytic],
        ),
        "GO:0055085": (
            "Transmembrane transport is correct but broad relative to heme transmembrane transport for the CcmAB system.",
            "MODIFY",
            "Heme transmembrane transport is the more specific process already supported for CcmA.",
            [HEME_TRANSMEMBRANE_TRANSPORT],
            [function, biogenesis, energy, catalytic],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def set_core_functions(doc: dict, gene: str, cfg: dict) -> None:
    if cfg["kind"] == "accessory_membrane":
        core = {
            "description": "Small inner-membrane CcmD-family component required for heme movement to the periplasm during c-type cytochrome biogenesis.",
            "directly_involved_in": [
                deepcopy(HEME_TRANSPORT),
                deepcopy(CYTOCHROME_C_BIOSYNTHESIS),
            ],
            "locations": [deepcopy(PLASMA_MEMBRANE)],
            "supported_by": [
                support_goa(gene, HEME_TRANSPORT["id"], HEME_TRANSPORT["label"]),
                support_goa(gene, CYTOCHROME_C_BIOSYNTHESIS["id"], CYTOCHROME_C_BIOSYNTHESIS["label"]),
                support_uniprot(gene, cfg["function_text"]),
                support_uniprot(gene, cfg["biogenesis_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    elif cfg["kind"] == "heme_membrane":
        core = {
            "description": "Multi-pass Ccm membrane component contributing to heme transport for c-type cytochrome biogenesis.",
            "contributes_to_molecular_function": deepcopy(HEME_TRANSMEMBRANE_TRANSPORTER),
            "directly_involved_in": [
                deepcopy(HEME_TRANSPORT),
                deepcopy(CYTOCHROME_COMPLEX_ASSEMBLY),
            ],
            "locations": [deepcopy(PLASMA_MEMBRANE)],
            "supported_by": [
                support_goa(gene, HEME_TRANSMEMBRANE_TRANSPORTER["id"], HEME_TRANSMEMBRANE_TRANSPORTER["label"]),
                support_goa(gene, HEME_TRANSPORT["id"], HEME_TRANSPORT["label"]),
                support_uniprot(gene, cfg["function_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
        if gene == "ccmC":
            core["molecular_function"] = deepcopy(HEME_BINDING)
            core["supported_by"].append(support_goa(gene, HEME_BINDING["id"], HEME_BINDING["label"]))
    else:
        core = {
            "description": "ATP-hydrolyzing energy-coupling subunit of the CcmAB heme-handling ABC system for c-type cytochrome biogenesis.",
            "molecular_function": deepcopy(ATP_HYDROLYSIS),
            "contributes_to_molecular_function": deepcopy(ABC_HEME_TRANSPORTER),
            "directly_involved_in": [
                deepcopy(HEME_TRANSMEMBRANE_TRANSPORT),
                deepcopy(CYTOCHROME_COMPLEX_ASSEMBLY),
            ],
            "locations": [deepcopy(PLASMA_MEMBRANE)],
            "in_complex": deepcopy(ABC_COMPLEX),
            "supported_by": [
                support_goa(gene, ATP_HYDROLYSIS["id"], ATP_HYDROLYSIS["label"]),
                support_goa(gene, ABC_HEME_TRANSPORTER["id"], ABC_HEME_TRANSPORTER["label"]),
                support_goa(gene, HEME_TRANSMEMBRANE_TRANSPORT["id"], HEME_TRANSMEMBRANE_TRANSPORT["label"]),
                support_uniprot(gene, cfg["function_text"]),
                support_uniprot(gene, cfg["energy_text"]),
                support_uniprot(gene, cfg["catalytic_text"]),
                support_uniprot(gene, cfg["subunit_text"]),
                support_uniprot(gene, cfg["subunit_b_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }

    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "What is the exact mechanistic role of CcmA in the P. putida KT2440 CcmABCD "
                "heme-handling step, given the reviewed UniProt note that CcmA was once thought "
                "to export heme but its precise role remains uncertain?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Measure c-type cytochrome maturation, periplasmic heme availability, and "
                "respiratory cytochrome profiles in ccmA, ccmB, ccmC, and ccmD mutants or "
                "conditional-depletion strains."
            ),
            "experiment_type": "targeted Ccm mutant cytochrome c maturation and heme-handling assay",
        }
    ]


def add_new_annotations(doc: dict, gene: str, cfg: dict) -> None:
    if cfg["kind"] != "atpase":
        return
    term_ids = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}
    if ABC_COMPLEX["id"] in term_ids:
        return
    doc.setdefault("existing_annotations", []).append(
        new_annotation(
            ABC_COMPLEX,
            "part_of",
            gene,
            "ABC transporter complex membership is a useful missing annotation for CcmA.",
            "Reviewed UniProt states that CcmA is part of the CcmAB ABC transporter complex composed of CcmA ATP-binding and CcmB transmembrane subunits.",
            [
                support_uniprot(gene, cfg["function_text"]),
                support_uniprot(gene, cfg["subunit_text"]),
                support_uniprot(gene, cfg["subunit_b_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        )
    )


def curate_gene(gene: str, cfg: dict) -> None:
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

    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['accession']})", cfg["product_text"])
    ensure_reference(doc, asta_ref(gene), f"Asta retrieval report for {gene} ({cfg['accession']})", cfg["asta_text"])

    for ann in doc.get("existing_annotations", []):
        term_id = ann["term"]["id"]
        label = ann["term"]["label"]
        if cfg["kind"] == "accessory_membrane":
            ann["review"] = ccmD_review(gene, cfg, term_id, label)
        elif cfg["kind"] == "heme_membrane":
            ann["review"] = heme_membrane_review(gene, cfg, term_id, label)
        else:
            ann["review"] = atpase_review(gene, cfg, term_id, label)

    add_new_annotations(doc, gene, cfg)
    set_core_functions(doc, gene, cfg)
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000, allow_unicode=False))
    print(f"curated {path}")


def term_ref(term: dict) -> dict:
    return {"preferred_term": term["label"], "term": deepcopy(term)}


def concept(term: dict, description: str) -> dict:
    data = term_ref(term)
    data["description"] = description
    return data


def annoton(
    gene: str,
    label: str,
    role_description: str,
    *,
    function: dict | None = None,
    processes: list[dict] | None = None,
) -> dict:
    data = {
        "id": f"{gene}_ccm_heme_export",
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "processes": [term_ref(process) for process in processes or []],
        "locations": [term_ref(PLASMA_MEMBRANE)],
        "role_description": role_description,
    }
    if function:
        data["function"] = term_ref(function)
    return data


def build_module() -> dict:
    return {
        "id": "MODULE:ccm_heme_export_cytochrome_c_maturation_boundary",
        "title": "CcmABCD heme export and cytochrome c maturation boundary",
        "description": (
            "Boundary module for the Pseudomonas putida KT2440 PP_4324-PP_4327 "
            "CcmD-C-B-A heme-handling system from the KEGG ppu02010 "
            "ABC-transporter umbrella map. CcmB and CcmC are multi-pass "
            "inner-membrane heme-handling components, CcmD is a small "
            "inner-membrane CcmD-family protein, and CcmA is the ATP-binding "
            "energy-coupling subunit of CcmAB. The module records the heme "
            "transport/export step required for c-type cytochrome biogenesis, "
            "while noting that UniProt flags CcmA's exact direct role as uncertain."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02010",
                "title": "ABC transporters - Pseudomonas putida KT2440",
                "statement": (
                    "KEGG ppu02010 contributes the PP_4324-PP_4327 ccmD/ccmC/ccmB/ccmA "
                    "locus as a coherent Ccm heme-handling ABC-transporter sub-batch "
                    "within the broad ABC-transporter umbrella map."
                ),
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.tsv",
                "title": "PSEPK ppu02010 ABC-transporter partition batch",
                "statement": (
                    "The ppu02010 partition batch records cluster C58 as ccmD, ccmC, "
                    "ccmB, and ccmA after first-pass curation."
                ),
            },
            {
                "source_id": "UniProtKB:Q88EX8",
                "title": "CcmD heme exporter protein D",
                "statement": (
                    "UniProt names CcmD as heme exporter protein D, places it in the "
                    "cell inner membrane, and describes it as required for heme export "
                    "to the periplasm for c-type cytochrome biogenesis."
                ),
            },
            {
                "source_id": "UniProtKB:Q88EX7",
                "title": "CcmC heme exporter protein C",
                "statement": (
                    "UniProt names CcmC as heme exporter protein C and a cytochrome "
                    "c-type biogenesis protein, places it in the cell inner membrane as "
                    "a multi-pass membrane protein, and carries CcmC/CcsA-family "
                    "cytochrome c biogenesis domains."
                ),
            },
            {
                "source_id": "UniProtKB:Q88EX6",
                "title": "CcmB heme exporter protein B",
                "statement": (
                    "UniProt names CcmB as heme exporter protein B, places it in the "
                    "cell inner membrane as a multi-pass membrane protein, and carries "
                    "CcmB cytochrome c biogenesis domains."
                ),
            },
            {
                "source_id": "UniProtKB:Q88EX5",
                "title": "CcmA cytochrome c biogenesis ATP-binding export protein",
                "statement": (
                    "Reviewed UniProt/HAMAP annotation names CcmA as the cytochrome c "
                    "biogenesis ATP-binding export protein, states that it is part of "
                    "the CcmAB ABC transporter complex, and notes that CcmA is "
                    "responsible for energy coupling while its exact direct role is "
                    "uncertain."
                ),
            },
        ],
        "module": {
            "id": "ccm_heme_export_cytochrome_c_maturation_boundary",
            "label": "CcmABCD heme export and cytochrome c maturation boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                concept(HEME_TRANSPORT, "Heme transport/export process represented by CcmD/CcmC/CcmB."),
                concept(HEME_TRANSMEMBRANE_TRANSPORT, "Inner-membrane heme transmembrane transport represented on CcmA."),
                concept(HEME_TRANSMEMBRANE_TRANSPORTER, "Complex-level heme transmembrane transporter activity represented on CcmB/CcmC."),
                concept(ABC_HEME_TRANSPORTER, "ABC-type heme transporter activity represented on CcmA."),
                concept(ATP_HYDROLYSIS, "ATP hydrolysis by the CcmA ATP-binding energy-coupling subunit."),
                concept(CYTOCHROME_COMPLEX_ASSEMBLY, "C-type cytochrome maturation and cytochrome complex assembly role of the Ccm system."),
                concept(CYTOCHROME_C_BIOSYNTHESIS, "Specific c-type cytochrome biogenesis process represented on CcmB/CcmD."),
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": "bacterial plasma membrane",
                        "term": deepcopy(PLASMA_MEMBRANE),
                        "description": (
                            "CcmB, CcmC, and CcmD are predicted inner-membrane proteins; "
                            "CcmA is an inner-membrane-associated peripheral ATPase."
                        ),
                    }
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "CcmABCD heme handling for c-type cytochrome biogenesis",
                    "node": {
                        "id": "ccmABCD_heme_export_cytochrome_c_maturation",
                        "label": "PP_4324-PP_4327 CcmABCD heme export and cytochrome c maturation",
                        "module_type": "TRANSPORT_STEP",
                        "description": (
                            "The PP_4324-PP_4327 locus encodes the CcmD-C-B-A heme-handling "
                            "system required for c-type cytochrome maturation. CcmC and CcmB "
                            "provide membrane heme-handling components, CcmD is a small "
                            "CcmD-family membrane protein, and CcmA supplies ATP-dependent "
                            "energy coupling to CcmAB."
                        ),
                        "concepts": [
                            term_ref(HEME_TRANSPORT),
                            term_ref(HEME_TRANSMEMBRANE_TRANSPORT),
                            term_ref(CYTOCHROME_COMPLEX_ASSEMBLY),
                        ],
                        "annotons": [
                            annoton(
                                "ccmD",
                                "ccmD: CcmD heme export accessory membrane protein",
                                "Small inner-membrane CcmD-family protein required for heme movement to the periplasm during c-type cytochrome biogenesis.",
                                processes=[HEME_TRANSPORT, CYTOCHROME_C_BIOSYNTHESIS],
                            ),
                            annoton(
                                "ccmC",
                                "ccmC: CcmC heme-handling membrane protein",
                                "Multi-pass CcmC/CcsA-family membrane component contributing to heme transport for c-type cytochrome biogenesis.",
                                function=HEME_TRANSMEMBRANE_TRANSPORTER,
                                processes=[HEME_TRANSPORT, CYTOCHROME_COMPLEX_ASSEMBLY],
                            ),
                            annoton(
                                "ccmB",
                                "ccmB: CcmB membrane component of CcmAB",
                                "Multi-pass CcmB-family membrane component contributing to heme transport for c-type cytochrome biogenesis.",
                                function=HEME_TRANSMEMBRANE_TRANSPORTER,
                                processes=[HEME_TRANSPORT, CYTOCHROME_C_BIOSYNTHESIS],
                            ),
                            annoton(
                                "ccmA",
                                "ccmA: CcmAB ATP-binding energy-coupling subunit",
                                "ATP-hydrolyzing CcmAB subunit that energizes the heme-handling step for c-type cytochrome biogenesis.",
                                function=ATP_HYDROLYSIS,
                                processes=[HEME_TRANSMEMBRANE_TRANSPORT, CYTOCHROME_COMPLEX_ASSEMBLY],
                            ),
                        ],
                    },
                }
            ],
        },
        "notes": (
            "This boundary module was created from the ppu02010 ABC-transporter "
            "partition work. It should remain distinct from porphyrin/heme "
            "biosynthesis modules and from terminal oxidase assembly modules; this "
            "locus represents the Ccm heme-handling/export step needed for c-type "
            "cytochrome maturation."
        ),
    }


def write_module() -> None:
    MODULE_PATH.parent.mkdir(parents=True, exist_ok=True)
    MODULE_PATH.write_text(yaml.safe_dump(build_module(), sort_keys=False, width=1000, allow_unicode=False))
    print(f"wrote {MODULE_PATH}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    write_module()


if __name__ == "__main__":
    main()
