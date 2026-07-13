#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_0958-PP_0962 Mla/Ttg2 system."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"
MODULE_PATH = Path("modules/mla_phospholipid_transport_boundary.yaml")


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
    data = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if proposed:
        data["proposed_replacement_terms"] = deepcopy(proposed)
    return data


def new_annotation(
    term: dict,
    qualifier: str,
    gene: str,
    summary: str,
    reason: str,
    supported_by: list[dict],
) -> dict:
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


NUCLEOTIDE_BINDING = {"id": "GO:0000166", "label": "nucleotide binding"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
LIPID_TRANSPORT = {"id": "GO:0006869", "label": "lipid transport"}
PHOSPHOLIPID_TRANSPORT = {"id": "GO:0015914", "label": "phospholipid transport"}
PHOSPHOLIPID_BINDING = {"id": "GO:0005543", "label": "phospholipid binding"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}
ABC_COMPLEX = {
    "id": "GO:0043190",
    "label": "ATP-binding cassette (ABC) transporter complex",
}


COMMON_MLAFEDB_TEXT = {
    "function": "Part of the ABC transporter complex MlaFEDB, which is",
    "pathway": "involved in a phospholipid transport pathway that maintains lipid",
    "asymmetry": "asymmetry in the outer membrane by retrograde trafficking of",
    "substrate": "phospholipids from the outer membrane to the inner membrane.",
    "subunit_a": "The complex is composed of two ATP-binding proteins (MlaF),",
    "subunit_b": "two transmembrane proteins (MlaE), two cytoplasmic solute-binding",
    "subunit_c": "proteins (MlaB) and six periplasmic solute-binding proteins (MlaD).",
}


GENES = {
    "mlaF": {
        "kind": "atpase",
        "accession": "Q88P94",
        "description": (
            "mlaF encodes the ATP-binding nucleotide-binding subunit of the MlaFEDB "
            "ABC transporter system. The protein provides ATP-dependent energy "
            "coupling for retrograde phospholipid trafficking from the outer membrane "
            "to the inner membrane, a process that contributes to outer-membrane lipid "
            "asymmetry."
        ),
        "product_text": "Full=Intermembrane phospholipid transport system ATP-binding protein MlaF",
        "asta_text": "Protein Description:** RecName: Full=Intermembrane phospholipid transport system ATP-binding protein MlaF",
        "domain_text": "InterPro; IPR003439; ABC_transporter-like_ATP-bd.",
        "ft_domain_text": "FT   DOMAIN          9..245",
        "family_text": "Belongs to the ABC transporter superfamily. MlaF family.",
        "energy_text": "Responsible for energy coupling to the transport system.",
    },
    "mlaE": {
        "kind": "permease",
        "accession": "Q88P93",
        "description": (
            "mlaE encodes the multi-pass inner-membrane permease subunit of the "
            "MlaFEDB ABC transporter system. It is the predicted membrane "
            "translocation component of the phospholipid transport pathway that "
            "retrogradely moves phospholipids from the outer membrane to the inner "
            "membrane to help maintain outer-membrane lipid asymmetry."
        ),
        "product_text": "Full=Intermembrane phospholipid transport system permease protein MlaE",
        "asta_text": "Protein Description:** RecName: Full=Intermembrane phospholipid transport system permease protein MlaE",
        "domain_text": "InterPro; IPR053408; MlaE_Permease.",
        "location_text": "Cell inner membrane",
        "topology_text": "FT   TRANSMEM        21..42",
        "translocation_text": "responsible for the translocation of the substrate across the membrane.",
    },
    "mlaD": {
        "kind": "binding",
        "accession": "Q88P92",
        "description": (
            "mlaD encodes an Mce/MlaD-domain phospholipid-binding component of the "
            "MlaFEDB phospholipid transport system. It is inferred to function as a "
            "periplasmic solute-binding component in the ABC transporter assembly that "
            "supports retrograde phospholipid trafficking and outer-membrane lipid "
            "asymmetry."
        ),
        "product_text": "Full=Phospholipid ABC transporter binding protein",
        "asta_text": "Protein Description:** SubName: Full=Phospholipid ABC transporter binding protein",
        "domain_text": "InterPro; IPR052336; MlaD_Phospholipid_Transporter.",
        "mce_domain_text": "InterPro; IPR003399; Mce/MlaD.",
        "panther_text": "PANTHER; PTHR33371:SF4; INTERMEMBRANE PHOSPHOLIPID TRANSPORT SYSTEM BINDING PROTEIN MLAD; 1.",
    },
    "ttg2D": {
        "kind": "mlac",
        "accession": "Q88P91",
        "description": (
            "ttg2D encodes a signal-peptide-containing MlaC/Ttg2D-family protein in "
            "the PP_0958-PP_0962 Mla/Ttg2 locus. Its protein-level evidence and "
            "MlaC-family phospholipid transport annotations support a periplasmic "
            "phospholipid-binding role in the bacterial outer-membrane lipid transport "
            "system, despite the legacy product name toluene tolerance protein."
        ),
        "product_text": "Full=Toluene tolerance protein",
        "asta_text": "Protein Description:** SubName: Full=Toluene tolerance protein",
        "domain_text": "InterPro; IPR008869; MlaC/ttg2D.",
        "panther_text": "PANTHER; PTHR36573; INTERMEMBRANE PHOSPHOLIPID TRANSPORT SYSTEM BINDING PROTEIN MLAC; 1.",
        "pdb_text": "Architectures of lipid transport systems for the bacterial outer",
        "signal_text": "FT   SIGNAL          1..22",
        "chain_text": "FT   CHAIN           23..215",
    },
    "ttg2E": {
        "kind": "stas",
        "accession": "Q88P90",
        "description": (
            "ttg2E encodes a small predicted STAS-domain protein adjacent to the "
            "PP_0958-PP_0961 Mla/Ttg2 phospholipid transport locus. The current "
            "record supports STAS-domain membership but does not establish a direct "
            "molecular activity, substrate, localization, or required role in the Mla "
            "transport system."
        ),
        "product_text": "Full=Toluene-tolerance protein",
        "asta_text": "Protein Description:** SubName: Full=Toluene-tolerance protein",
        "domain_text": "InterPro; IPR002645; STAS_dom.",
        "ft_domain_text": "FT   DOMAIN          13..100",
    },
}


def common_mla_support(gene: str) -> list[dict]:
    return [
        support_uniprot(gene, COMMON_MLAFEDB_TEXT["function"]),
        support_uniprot(gene, COMMON_MLAFEDB_TEXT["pathway"]),
        support_uniprot(gene, COMMON_MLAFEDB_TEXT["asymmetry"]),
        support_uniprot(gene, COMMON_MLAFEDB_TEXT["substrate"]),
    ]


def subunit_support(gene: str) -> list[dict]:
    return [
        support_uniprot(gene, COMMON_MLAFEDB_TEXT["subunit_a"]),
        support_uniprot(gene, COMMON_MLAFEDB_TEXT["subunit_b"]),
        support_uniprot(gene, COMMON_MLAFEDB_TEXT["subunit_c"]),
    ]


def mlaF_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    mapping = {
        "GO:0000166": (
            "Nucleotide binding is true but too broad for the MlaF ABC ATP-binding subunit.",
            "MODIFY",
            "MlaF has an ABC transporter nucleotide-binding domain and already has the more informative ATP-binding annotation.",
            [ATP_BINDING],
            [
                support_uniprot(gene, cfg["product_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_uniprot(gene, cfg["ft_domain_text"]),
            ],
        ),
        "GO:0005524": (
            "ATP binding is appropriate for MlaF.",
            "ACCEPT",
            "MlaF is named as the ATP-binding protein of the MlaFEDB transporter and carries an ABC transporter ATP-binding domain.",
            None,
            [
                support_uniprot(gene, cfg["product_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_uniprot(gene, cfg["ft_domain_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        ),
        "GO:0006869": (
            "Lipid transport captures the broad MlaFEDB pathway but should be narrowed to phospholipid transport.",
            "MODIFY",
            "UniProt describes MlaFEDB as a phospholipid transport pathway for retrograde trafficking of phospholipids between membranes.",
            [PHOSPHOLIPID_TRANSPORT],
            common_mla_support(gene) + [support_asta(gene, cfg["asta_text"])],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is the core mechanistic activity of MlaF.",
            "ACCEPT",
            "MlaF is the ATP-binding energy-coupling subunit of the MlaFEDB transporter and carries the ABC transporter ATP-binding domain.",
            None,
            [
                support_uniprot(gene, cfg["energy_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_uniprot(gene, cfg["ft_domain_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def mlaE_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    mapping = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for the MlaE inner-membrane permease.",
            "ACCEPT",
            "UniProt places MlaE in the cell inner membrane and predicts transmembrane helices.",
            None,
            [
                support_uniprot(gene, cfg["location_text"]),
                support_uniprot(gene, cfg["topology_text"]),
            ],
        ),
        "GO:0015914": (
            "Phospholipid transport is appropriate for MlaE.",
            "ACCEPT",
            "MlaE is the predicted permease subunit of MlaFEDB, a pathway for retrograde phospholipid trafficking.",
            None,
            common_mla_support(gene)
            + [
                support_uniprot(gene, cfg["translocation_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        ),
        "GO:0043190": (
            "ABC transporter complex membership is appropriate for MlaE.",
            "ACCEPT",
            "UniProt describes MlaE as a transmembrane subunit of the MlaFEDB ABC transporter complex.",
            None,
            common_mla_support(gene) + subunit_support(gene),
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def mlaD_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    mapping = {
        "GO:0005543": (
            "Phospholipid binding is appropriate for MlaD.",
            "ACCEPT",
            "The MlaD product name and MlaD phospholipid transporter domain support a phospholipid-binding role.",
            None,
            [
                support_uniprot(gene, cfg["product_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_uniprot(gene, cfg["mce_domain_text"]),
                support_uniprot(gene, cfg["panther_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        ),
        "GO:0015914": (
            "Phospholipid transport is appropriate for MlaD as a MlaFEDB solute-binding component.",
            "ACCEPT",
            "MlaD is a MlaD phospholipid transporter-domain protein and UniProt describes MlaD as a periplasmic solute-binding component of MlaFEDB.",
            None,
            [
                support_uniprot(gene, cfg["domain_text"]),
                support_uniprot(gene, cfg["panther_text"]),
                support_uniprot("mlaF", COMMON_MLAFEDB_TEXT["subunit_c"]),
            ],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def add_new_annotations(doc: dict, gene: str, cfg: dict) -> None:
    term_ids = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}

    if gene == "mlaF" and ABC_COMPLEX["id"] not in term_ids:
        doc.setdefault("existing_annotations", []).append(
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                gene,
                "ABC transporter complex membership is a useful missing annotation for MlaF.",
                "UniProt describes MlaF as the ATP-binding subunit of the MlaFEDB ABC transporter complex.",
                common_mla_support(gene) + subunit_support(gene) + [support_asta(gene, cfg["asta_text"])],
            )
        )

    if gene == "mlaD":
        if ABC_COMPLEX["id"] not in term_ids:
            doc.setdefault("existing_annotations", []).append(
                new_annotation(
                    ABC_COMPLEX,
                    "part_of",
                    gene,
                    "ABC transporter complex membership is a useful missing annotation for MlaD.",
                    "UniProt describes MlaD as a periplasmic solute-binding subunit of the MlaFEDB ABC transporter complex.",
                    [
                        support_uniprot("mlaF", COMMON_MLAFEDB_TEXT["function"]),
                        support_uniprot("mlaF", COMMON_MLAFEDB_TEXT["subunit_c"]),
                        support_uniprot(gene, cfg["panther_text"]),
                    ],
                )
            )
        if PERIPLASM["id"] not in term_ids:
            doc.setdefault("existing_annotations", []).append(
                new_annotation(
                    PERIPLASM,
                    "located_in",
                    gene,
                    "Periplasmic localization is a useful missing annotation for MlaD.",
                    "UniProt describes MlaD as a periplasmic solute-binding component of MlaFEDB.",
                    [support_uniprot("mlaF", COMMON_MLAFEDB_TEXT["subunit_c"])],
                )
            )

    if gene == "ttg2D":
        new_terms = [
            (
                PHOSPHOLIPID_BINDING,
                "enables",
                "Phospholipid binding is a useful missing annotation for Ttg2D/MlaC.",
                "Ttg2D carries MlaC/ttg2D domains and belongs to the MlaC phospholipid transport system binding-protein family.",
                [
                    support_uniprot(gene, cfg["domain_text"]),
                    support_uniprot(gene, cfg["panther_text"]),
                    support_uniprot(gene, cfg["pdb_text"]),
                    support_asta(gene, cfg["asta_text"]),
                ],
            ),
            (
                PHOSPHOLIPID_TRANSPORT,
                "involved_in",
                "Phospholipid transport is a useful missing process annotation for Ttg2D/MlaC.",
                "The MlaC/ttg2D family assignment and PANTHER family name place Ttg2D in an intermembrane phospholipid transport system.",
                [
                    support_uniprot(gene, cfg["domain_text"]),
                    support_uniprot(gene, cfg["panther_text"]),
                    support_uniprot(gene, cfg["pdb_text"]),
                ],
            ),
            (
                PERIPLASM,
                "located_in",
                "Periplasmic localization is a useful missing annotation for Ttg2D.",
                "Ttg2D has a predicted N-terminal signal peptide followed by the mature chain, consistent with a periplasmic MlaC-family carrier.",
                [
                    support_uniprot(gene, cfg["signal_text"]),
                    support_uniprot(gene, cfg["chain_text"]),
                    support_uniprot(gene, cfg["domain_text"]),
                ],
            ),
        ]
        for term, qualifier, summary, reason, support in new_terms:
            if term["id"] not in term_ids:
                doc.setdefault("existing_annotations", []).append(
                    new_annotation(term, qualifier, gene, summary, reason, support)
                )


def set_core_functions(doc: dict, gene: str, cfg: dict) -> None:
    if cfg["kind"] == "atpase":
        core = {
            "description": "ATP-hydrolyzing energy-coupling subunit of the MlaFEDB phospholipid transport system.",
            "molecular_function": deepcopy(ATP_HYDROLYSIS),
            "directly_involved_in": [deepcopy(PHOSPHOLIPID_TRANSPORT)],
            "in_complex": deepcopy(ABC_COMPLEX),
            "supported_by": [
                support_goa(gene, ATP_HYDROLYSIS["id"], ATP_HYDROLYSIS["label"]),
                support_goa(gene, LIPID_TRANSPORT["id"], LIPID_TRANSPORT["label"]),
                support_uniprot(gene, COMMON_MLAFEDB_TEXT["function"]),
                support_uniprot(gene, COMMON_MLAFEDB_TEXT["pathway"]),
                support_uniprot(gene, COMMON_MLAFEDB_TEXT["substrate"]),
                support_uniprot(gene, cfg["energy_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    elif cfg["kind"] == "permease":
        core = {
            "description": "Inner-membrane permease component of the MlaFEDB phospholipid transport system.",
            "directly_involved_in": [deepcopy(PHOSPHOLIPID_TRANSPORT)],
            "locations": [deepcopy(PLASMA_MEMBRANE)],
            "in_complex": deepcopy(ABC_COMPLEX),
            "supported_by": [
                support_goa(gene, PHOSPHOLIPID_TRANSPORT["id"], PHOSPHOLIPID_TRANSPORT["label"]),
                support_goa(gene, PLASMA_MEMBRANE["id"], PLASMA_MEMBRANE["label"]),
                support_goa(gene, ABC_COMPLEX["id"], ABC_COMPLEX["label"]),
                support_uniprot(gene, COMMON_MLAFEDB_TEXT["function"]),
                support_uniprot(gene, COMMON_MLAFEDB_TEXT["pathway"]),
                support_uniprot(gene, COMMON_MLAFEDB_TEXT["substrate"]),
                support_uniprot(gene, cfg["translocation_text"]),
                support_uniprot(gene, cfg["location_text"]),
            ],
        }
    elif cfg["kind"] == "binding":
        core = {
            "description": "MlaD-domain phospholipid-binding component of the MlaFEDB phospholipid transport system.",
            "molecular_function": deepcopy(PHOSPHOLIPID_BINDING),
            "directly_involved_in": [deepcopy(PHOSPHOLIPID_TRANSPORT)],
            "locations": [deepcopy(PERIPLASM)],
            "in_complex": deepcopy(ABC_COMPLEX),
            "supported_by": [
                support_goa(gene, PHOSPHOLIPID_BINDING["id"], PHOSPHOLIPID_BINDING["label"]),
                support_goa(gene, PHOSPHOLIPID_TRANSPORT["id"], PHOSPHOLIPID_TRANSPORT["label"]),
                support_uniprot(gene, cfg["product_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_uniprot(gene, cfg["panther_text"]),
                support_uniprot("mlaF", COMMON_MLAFEDB_TEXT["subunit_c"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    elif cfg["kind"] == "mlac":
        core = {
            "description": "Periplasmic MlaC/Ttg2D-family phospholipid-binding protein in the bacterial outer-membrane lipid transport system.",
            "molecular_function": deepcopy(PHOSPHOLIPID_BINDING),
            "directly_involved_in": [deepcopy(PHOSPHOLIPID_TRANSPORT)],
            "locations": [deepcopy(PERIPLASM)],
            "supported_by": [
                support_uniprot(gene, cfg["domain_text"]),
                support_uniprot(gene, cfg["panther_text"]),
                support_uniprot(gene, cfg["pdb_text"]),
                support_uniprot(gene, cfg["signal_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    else:
        doc["core_functions"] = []
        doc["proposed_new_terms"] = []
        doc["suggested_questions"] = [
            {
                "question": (
                    "Does the STAS-domain protein Ttg2E have a required accessory role in the "
                    "PP_0958-PP_0961 Mla/Ttg2 phospholipid transport locus, and if so what "
                    "partner or regulatory activity does it provide?"
                )
            }
        ]
        doc["suggested_experiments"] = [
            {
                "description": (
                    "Compare phospholipid transport, outer-membrane permeability, and solvent "
                    "tolerance phenotypes in ttg2E deletion and complementation strains alongside "
                    "mlaF, mlaE, mlaD, and ttg2D mutants."
                ),
                "experiment_type": "targeted Mla/Ttg2 accessory-gene mutant phenotyping",
            }
        ]
        return

    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "Does the PP_0958-PP_0962 Mla/Ttg2 locus operate as a canonical retrograde "
                "phospholipid transport system in P. putida KT2440, and how does the adjacent "
                "Ttg2E STAS-domain protein affect that activity?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Measure outer-membrane phospholipid asymmetry, periplasmic phospholipid binding, "
                "and solvent-envelope stress phenotypes in single and combined mutants of mlaF, "
                "mlaE, mlaD, ttg2D, and ttg2E."
            ),
            "experiment_type": "targeted Mla/Ttg2 phospholipid transport and envelope-stress assay",
        }
    ]


def curate_gene(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    doc["status"] = "DRAFT" if cfg["kind"] == "stas" else "COMPLETE"
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
    if gene in {"mlaD"}:
        ensure_reference(
            doc,
            uniprot_ref("mlaF"),
            "UniProtKB entry for mlaF (Q88P94)",
            COMMON_MLAFEDB_TEXT["subunit_c"],
        )

    for ann in doc.get("existing_annotations", []):
        term_id = ann["term"]["id"]
        label = ann["term"]["label"]
        if cfg["kind"] == "atpase":
            ann["review"] = mlaF_review(gene, cfg, term_id, label)
        elif cfg["kind"] == "permease":
            ann["review"] = mlaE_review(gene, cfg, term_id, label)
        elif cfg["kind"] == "binding":
            ann["review"] = mlaD_review(gene, cfg, term_id, label)

    add_new_annotations(doc, gene, cfg)
    set_core_functions(doc, gene, cfg)
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000, allow_unicode=False), encoding="utf-8")
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
    locations: list[dict] | None = None,
) -> dict:
    data = {
        "id": f"{gene}_mla_phospholipid_transport",
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": role_description,
    }
    if function:
        data["function"] = term_ref(function)
    if processes:
        data["processes"] = [term_ref(process) for process in processes]
    if locations:
        data["locations"] = [term_ref(location) for location in locations]
    return data


def build_module() -> dict:
    return {
        "id": "MODULE:mla_phospholipid_transport_boundary",
        "title": "Mla/Ttg2 phospholipid transport and outer-membrane lipid asymmetry boundary",
        "description": (
            "Boundary module for the Pseudomonas putida KT2440 PP_0958-PP_0962 "
            "Mla/Ttg2 locus from the broad KEGG ppu02010 ABC-transporter map. "
            "MlaF, MlaE, and MlaD form the supported MlaFEDB phospholipid "
            "transport system; Ttg2D is a periplasmic MlaC-family phospholipid "
            "binding protein with protein-level structural evidence; and Ttg2E "
            "is a neighboring STAS-domain accessory candidate whose direct role "
            "is unresolved."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02010",
                "title": "ABC transporters - Pseudomonas putida KT2440",
                "statement": (
                    "KEGG ppu02010 contributes the PP_0958-PP_0962 mlaF/mlaE/mlaD/"
                    "ttg2D/ttg2E locus as a coherent Mla/Ttg2 phospholipid-transport "
                    "sub-batch within the broad ABC-transporter umbrella map."
                ),
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.tsv",
                "title": "PSEPK ppu02010 ABC-transporter partition batch",
                "statement": (
                    "The ppu02010 partition batch records cluster C20 as mlaF, mlaE, "
                    "mlaD, ttg2D, and ttg2E after first-pass curation."
                ),
            },
            {
                "source_id": "UniProtKB:Q88P94",
                "title": "MlaF intermembrane phospholipid transport ATP-binding protein",
                "statement": (
                    "UniProt names MlaF as the ATP-binding protein of MlaFEDB and "
                    "describes the complex as a phospholipid transport pathway for "
                    "retrograde trafficking from the outer membrane to the inner membrane."
                ),
            },
            {
                "source_id": "UniProtKB:Q88P93",
                "title": "MlaE intermembrane phospholipid transport permease",
                "statement": (
                    "UniProt names MlaE as the permease protein of MlaFEDB, places it "
                    "in the cell inner membrane, and describes it as probably responsible "
                    "for substrate translocation across the membrane."
                ),
            },
            {
                "source_id": "UniProtKB:Q88P92",
                "title": "MlaD phospholipid ABC transporter binding protein",
                "statement": (
                    "UniProt and domain annotations name MlaD as a phospholipid ABC "
                    "transporter binding protein with Mce/MlaD and MlaD phospholipid "
                    "transporter domains."
                ),
            },
            {
                "source_id": "UniProtKB:Q88P91",
                "title": "Ttg2D MlaC/Ttg2D-family protein",
                "statement": (
                    "UniProt records Ttg2D as a protein-level, signal-peptide-containing "
                    "MlaC/ttg2D-family protein with structural evidence from lipid "
                    "transport system studies."
                ),
            },
            {
                "source_id": "UniProtKB:Q88P90",
                "title": "Ttg2E STAS-domain protein",
                "statement": (
                    "UniProt records Ttg2E as a small predicted STAS-domain protein; "
                    "the current first-pass evidence does not establish its direct "
                    "molecular role."
                ),
            },
        ],
        "module": {
            "id": "mla_phospholipid_transport_boundary",
            "label": "Mla/Ttg2 phospholipid transport and outer-membrane lipid asymmetry boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                concept(
                    PHOSPHOLIPID_TRANSPORT,
                    "Retrograde transport of phospholipids from the outer membrane toward the inner membrane.",
                ),
                concept(
                    LIPID_TRANSPORT,
                    "Broader lipid-transport context represented by the original MlaF GOA term.",
                ),
                concept(
                    PHOSPHOLIPID_BINDING,
                    "Phospholipid binding by MlaD/Ttg2D solute-binding components.",
                ),
                concept(
                    ATP_HYDROLYSIS,
                    "ATP hydrolysis by the MlaF energy-coupling subunit.",
                ),
                concept(
                    ABC_COMPLEX,
                    "MlaFEDB ABC transporter complex membership represented for MlaF/MlaE/MlaD.",
                ),
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": "bacterial plasma membrane",
                        "term": deepcopy(PLASMA_MEMBRANE),
                        "description": "MlaE is an inner-membrane permease and the MlaFEDB complex is an inner-membrane ABC transporter.",
                    },
                    {
                        "preferred_term": "periplasmic space",
                        "term": deepcopy(PERIPLASM),
                        "description": "MlaD and Ttg2D/MlaC-family proteins provide periplasmic solute-binding or carrier roles.",
                    },
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "Mla/Ttg2 phospholipid transport and lipid-asymmetry maintenance",
                    "node": {
                        "id": "PP_0958_PP_0962_mla_ttg2_phospholipid_transport",
                        "label": "PP_0958-PP_0962 Mla/Ttg2 phospholipid transport locus",
                        "module_type": "TRANSPORT_STEP",
                        "description": (
                            "The PP_0958-PP_0962 locus encodes MlaF, MlaE, MlaD, "
                            "Ttg2D, and Ttg2E. MlaF supplies ATP-dependent energy "
                            "coupling, MlaE is the membrane permease, MlaD is a "
                            "MlaD-domain phospholipid-binding component, Ttg2D is "
                            "a MlaC-family periplasmic carrier candidate, and Ttg2E "
                            "is retained as an unresolved STAS-domain accessory candidate."
                        ),
                        "concepts": [
                            term_ref(PHOSPHOLIPID_TRANSPORT),
                            term_ref(PHOSPHOLIPID_BINDING),
                        ],
                        "annotons": [
                            annoton(
                                "mlaF",
                                "mlaF: MlaFEDB ATP-binding energy-coupling subunit",
                                "ATP-hydrolyzing MlaF subunit that energizes MlaFEDB phospholipid transport.",
                                function=ATP_HYDROLYSIS,
                                processes=[PHOSPHOLIPID_TRANSPORT],
                            ),
                            annoton(
                                "mlaE",
                                "mlaE: MlaFEDB inner-membrane permease",
                                "Multi-pass inner-membrane permease probably responsible for substrate translocation.",
                                processes=[PHOSPHOLIPID_TRANSPORT],
                                locations=[PLASMA_MEMBRANE],
                            ),
                            annoton(
                                "mlaD",
                                "mlaD: MlaD phospholipid-binding component",
                                "MlaD-domain phospholipid-binding component of the MlaFEDB phospholipid transport system.",
                                function=PHOSPHOLIPID_BINDING,
                                processes=[PHOSPHOLIPID_TRANSPORT],
                                locations=[PERIPLASM],
                            ),
                            annoton(
                                "ttg2D",
                                "ttg2D: MlaC/Ttg2D-family periplasmic carrier candidate",
                                "Signal-peptide-containing MlaC-family phospholipid-binding protein associated with bacterial outer-membrane lipid transport systems.",
                                function=PHOSPHOLIPID_BINDING,
                                processes=[PHOSPHOLIPID_TRANSPORT],
                                locations=[PERIPLASM],
                            ),
                            annoton(
                                "ttg2E",
                                "ttg2E: unresolved STAS-domain accessory candidate",
                                "Neighboring STAS-domain protein retained in the locus boundary; current evidence does not establish a direct molecular function.",
                            ),
                        ],
                    },
                }
            ],
        },
        "notes": (
            "This boundary module was created from the ppu02010 ABC-transporter "
            "partition work. The module should remain distinct from glycerophospholipid "
            "biosynthesis modules, which describe phospholipid synthesis and turnover "
            "rather than Mla/Ttg2 envelope transport and lipid-asymmetry maintenance."
        ),
    }


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    MODULE_PATH.write_text(
        yaml.safe_dump(build_module(), sort_keys=False, width=1000, allow_unicode=False),
        encoding="utf-8",
    )
    print(f"wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
