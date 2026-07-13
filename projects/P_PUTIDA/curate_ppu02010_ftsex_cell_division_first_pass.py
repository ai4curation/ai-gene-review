#!/usr/bin/env python3
"""First-pass curation for the ppu02010 FtsEX cell-division ABC-like system."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"
MODULE_PATH = Path("modules/ftsex_cell_division_boundary.yaml")


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


NUCLEOTIDE_BINDING = {"id": "GO:0000166", "label": "nucleotide binding"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
MEMBRANE = {"id": "GO:0016020", "label": "membrane"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
TRANSPORTER_ACTIVITY = {"id": "GO:0022857", "label": "transmembrane transporter activity"}
CELL_DIVISION_SITE = {"id": "GO:0032153", "label": "cell division site"}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
CELL_DIVISION = {"id": "GO:0051301", "label": "cell division"}
TRANS_MEMBRANE_TRANSPORT = {"id": "GO:0055085", "label": "transmembrane transport"}


GENES = {
    "ftsX": {
        "accession": "Q88CS1",
        "kind": "membrane",
        "description": (
            "ftsX encodes the multi-pass inner-membrane component of the FtsEX "
            "ABC-like cell-division complex. UniProt identifies FtsX as part of "
            "FtsEX, places it in the cell inner membrane, and assigns FtsX-specific "
            "cell-division domains and PANTHER family membership. The supported "
            "core role is participation in cell division at the membrane/division "
            "site rather than transport of a defined substrate."
        ),
        "product": "Full=Cell division protein FtsX",
        "asta": "- **Protein Description:** RecName: Full=Cell division protein FtsX",
        "function": "Part of the ABC transporter FtsEX involved in cellular",
        "subunit": "Forms a membrane-associated complex with FtsE.",
        "location": "Cell inner membrane",
        "topology": "Multi-pass membrane protein",
        "domain": "InterPro; IPR004513; FtsX.",
        "ecd_domain": "InterPro; IPR040690; FtsX_ECD.",
        "panther": "PANTHER; PTHR47755; CELL DIVISION PROTEIN FTSX; 1.",
    },
    "ftsE": {
        "accession": "Q88CS0",
        "kind": "atpase",
        "description": (
            "ftsE encodes the cytoplasmic-side ATP-binding component of the FtsEX "
            "ABC-like cell-division complex. UniProt describes FtsE as part of "
            "FtsEX, important for septal-ring assembly or stability, and forming "
            "a membrane-associated complex with FtsX. Its core molecular activity "
            "is ATP hydrolysis coupled to FtsEX cell-division function, not a "
            "specific transported-substrate reaction."
        ),
        "product": "Full=Cell division ATP-binding protein FtsE",
        "asta": "- **Protein Description:** RecName: Full=Cell division ATP-binding protein FtsE",
        "function": "Part of the ABC transporter FtsEX involved in cellular",
        "septal_ring": "division. Important for assembly or stability of the septal ring.",
        "subunit": "Forms a membrane-associated complex with FtsX.",
        "location": "Cell inner membrane",
        "side": "Cytoplasmic side",
        "abc_domain": "InterPro; IPR003439; ABC_transporter-like_ATP-bd.",
        "ftse_domain": "InterPro; IPR005286; Cell_div_FtsE.",
        "panther": "PANTHER; PTHR24220:SF470; CELL DIVISION ATP-BINDING PROTEIN FTSE; 1.",
    },
}


def ftsx_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    function_support = [
        support_uniprot(gene, cfg["product"]),
        support_uniprot(gene, cfg["function"]),
        support_uniprot(gene, cfg["subunit"]),
        support_uniprot(gene, cfg["domain"]),
        support_uniprot(gene, cfg["panther"]),
        support_asta(gene, cfg["asta"]),
    ]
    mapping = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for the FtsX inner-membrane component.",
            "ACCEPT",
            "UniProt places FtsX in the cell inner membrane as a multi-pass membrane protein.",
            None,
            [support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["topology"])],
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than plasma membrane for FtsX.",
            "MARK_AS_OVER_ANNOTATED",
            "The record has a more specific plasma membrane annotation, and UniProt places FtsX in the cell inner membrane.",
            None,
            [support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["topology"])],
        ),
        "GO:0032153": (
            "Cell division site localization is appropriate for FtsX.",
            "ACCEPT",
            "FtsX is an FtsEX cell-division component and belongs to the FtsX cell-division protein family.",
            None,
            function_support,
        ),
        "GO:0051301": (
            "Cell division is the core process annotation for FtsX.",
            "ACCEPT",
            "UniProt describes FtsX as part of the FtsEX complex involved in cellular division.",
            None,
            function_support,
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def ftse_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    division_support = [
        support_uniprot(gene, cfg["product"]),
        support_uniprot(gene, cfg["function"]),
        support_uniprot(gene, cfg["septal_ring"]),
        support_uniprot(gene, cfg["subunit"]),
        support_uniprot(gene, cfg["ftse_domain"]),
        support_uniprot(gene, cfg["panther"]),
        support_asta(gene, cfg["asta"]),
    ]
    atp_support = [
        support_uniprot(gene, cfg["product"]),
        support_uniprot(gene, cfg["abc_domain"]),
        support_uniprot(gene, cfg["ftse_domain"]),
        support_asta(gene, cfg["asta"]),
    ]
    mapping = {
        "GO:0000166": (
            "Nucleotide binding is true but too broad for this FtsE ABC ATP-binding subunit.",
            "MODIFY",
            "ATP binding is the more specific nucleotide-binding annotation already present on the record.",
            [ATP_BINDING],
            [support_uniprot(gene, cfg["abc_domain"]), support_uniprot(gene, cfg["product"])],
        ),
        "GO:0005524": (
            "ATP binding is appropriate for FtsE.",
            "ACCEPT",
            "FtsE is the ATP-binding component of the FtsEX ABC-like division complex.",
            None,
            atp_support,
        ),
        "GO:0005886": (
            "Plasma membrane localization is appropriate for membrane-associated FtsE.",
            "ACCEPT",
            "UniProt places FtsE at the cell inner membrane on the cytoplasmic side, where it complexes with FtsX.",
            None,
            [support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["side"]), support_uniprot(gene, cfg["subunit"])],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is the core mechanistic activity for FtsE.",
            "ACCEPT",
            "FtsE has ABC ATP-binding and FtsE cell-division domains and functions as the ATPase component of FtsEX.",
            None,
            atp_support,
        ),
        "GO:0022857": (
            "Transmembrane transporter activity is likely an over-broad ABC-family inference for FtsE.",
            "MARK_AS_OVER_ANNOTATED",
            "The supported FtsE role is ATP hydrolysis in the FtsEX cell-division complex; the current record does not identify a transported substrate.",
            None,
            division_support + [support_uniprot(gene, cfg["abc_domain"])],
        ),
        "GO:0051301": (
            "Cell division is the core process annotation for FtsE.",
            "ACCEPT",
            "UniProt describes FtsE as part of FtsEX involved in cellular division and important for septal-ring assembly or stability.",
            None,
            division_support,
        ),
        "GO:0055085": (
            "Transmembrane transport is likely an over-broad ABC-family process inference for FtsE.",
            "MARK_AS_OVER_ANNOTATED",
            "FtsE is supported as an FtsEX cell-division ATPase, but no transported substrate or transport process is established in the local evidence.",
            None,
            division_support,
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def add_new_annotations(doc: dict, gene: str, cfg: dict) -> None:
    existing = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}
    if ABC_COMPLEX["id"] not in existing:
        partner = "FtsE" if gene == "ftsX" else "FtsX"
        doc.setdefault("existing_annotations", []).append(
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                gene,
                f"ABC transporter complex membership is a useful missing annotation for {gene}.",
                f"{gene} forms the FtsEX ABC-like cell-division complex with {partner}.",
                [
                    support_uniprot(gene, cfg["function"]),
                    support_uniprot(gene, cfg["subunit"]),
                    support_uniprot(gene, cfg["product"]),
                ],
            )
        )


def set_core_functions(doc: dict, gene: str, cfg: dict) -> None:
    if cfg["kind"] == "membrane":
        core = {
            "description": "Multi-pass inner-membrane FtsEX component involved in bacterial cell division.",
            "directly_involved_in": [deepcopy(CELL_DIVISION)],
            "locations": [deepcopy(PLASMA_MEMBRANE), deepcopy(CELL_DIVISION_SITE)],
            "in_complex": deepcopy(ABC_COMPLEX),
            "supported_by": [
                support_goa(gene, CELL_DIVISION["id"], CELL_DIVISION["label"]),
                support_goa(gene, CELL_DIVISION_SITE["id"], CELL_DIVISION_SITE["label"]),
                support_goa(gene, PLASMA_MEMBRANE["id"], PLASMA_MEMBRANE["label"]),
                support_uniprot(gene, cfg["function"]),
                support_uniprot(gene, cfg["subunit"]),
                support_uniprot(gene, cfg["location"]),
                support_uniprot(gene, cfg["domain"]),
                support_asta(gene, cfg["asta"]),
            ],
        }
    else:
        core = {
            "description": "ATP-hydrolyzing FtsEX component involved in septal-ring assembly or stability during cell division.",
            "molecular_function": deepcopy(ATP_HYDROLYSIS),
            "directly_involved_in": [deepcopy(CELL_DIVISION)],
            "locations": [deepcopy(PLASMA_MEMBRANE)],
            "in_complex": deepcopy(ABC_COMPLEX),
            "supported_by": [
                support_goa(gene, ATP_HYDROLYSIS["id"], ATP_HYDROLYSIS["label"]),
                support_goa(gene, CELL_DIVISION["id"], CELL_DIVISION["label"]),
                support_goa(gene, PLASMA_MEMBRANE["id"], PLASMA_MEMBRANE["label"]),
                support_uniprot(gene, cfg["function"]),
                support_uniprot(gene, cfg["septal_ring"]),
                support_uniprot(gene, cfg["subunit"]),
                support_uniprot(gene, cfg["abc_domain"]),
                support_asta(gene, cfg["asta"]),
            ],
        }

    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "Does P. putida FtsEX directly regulate septal peptidoglycan hydrolases, "
                "and what partner proteins connect FtsEX ATP hydrolysis to divisome "
                "assembly or daughter-cell separation?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Measure septal-ring assembly, cell morphology, and division-site localization "
                "after ftsE or ftsX depletion or ATPase-motif mutation."
            ),
            "experiment_type": "cell-division localization and depletion assay",
        },
        {
            "description": (
                "Test physical and functional interactions between FtsEX and candidate septal "
                "peptidoglycan hydrolases or hydrolase activators in P. putida."
            ),
            "experiment_type": "FtsEX partner interaction and hydrolase-activation assay",
        },
    ]


def curate_gene(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
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
    ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['accession']})", cfg["product"])
    ensure_reference(doc, asta_ref(gene), f"Asta retrieval report for {gene} ({cfg['accession']})", cfg["asta"])

    for ann in doc.get("existing_annotations", []):
        term_id = ann["term"]["id"]
        label = ann["term"]["label"]
        if cfg["kind"] == "membrane":
            ann["review"] = ftsx_review(gene, cfg, term_id, label)
        else:
            ann["review"] = ftse_review(gene, cfg, term_id, label)

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
        "id": f"{gene}_ftsex_cell_division",
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
        "id": "MODULE:ftsex_cell_division_boundary",
        "title": "FtsEX cell-division ABC-like boundary",
        "description": (
            "Boundary module for the Pseudomonas putida KT2440 FtsEX cell-division "
            "ABC-like system from the KEGG ppu02010 ABC-transporter umbrella map. "
            "The module captures FtsX as the inner-membrane component and FtsE as "
            "the ATP-hydrolyzing component, while explicitly separating this cell "
            "division/septal-ring system from conventional transported-substrate "
            "ABC import or export modules."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02010",
                "title": "ABC transporters - Pseudomonas putida KT2440",
                "statement": "KEGG ppu02010 contributes ftsX and ftsE as ABC-transporter map members.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.tsv",
                "title": "PSEPK ppu02010 ABC-transporter partition batch",
                "statement": "The ppu02010 partition records C66 as the ftsX/ftsE cell-division ABC-like pair.",
            },
            {
                "source_id": "UniProtKB:Q88CS1",
                "title": "FtsX cell division protein",
                "statement": "UniProt describes FtsX as part of the FtsEX ABC transporter involved in cellular division and as an inner-membrane protein forming a complex with FtsE.",
            },
            {
                "source_id": "UniProtKB:Q88CS0",
                "title": "FtsE cell division ATP-binding protein",
                "statement": "UniProt describes FtsE as part of the FtsEX ABC transporter involved in cellular division and important for septal-ring assembly or stability.",
            },
        ],
        "module": {
            "id": "ftsex_cell_division_boundary",
            "label": "FtsEX cell-division ABC-like boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                concept(CELL_DIVISION, "Cell-division process supported for both FtsX and FtsE."),
                concept(CELL_DIVISION_SITE, "Division-site localization supported for FtsX."),
                concept(ATP_HYDROLYSIS, "FtsE ATPase activity that energizes FtsEX conformational function."),
                concept(ABC_COMPLEX, "FtsEX ABC-like complex membership."),
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": "bacterial plasma membrane",
                        "term": deepcopy(PLASMA_MEMBRANE),
                        "description": "FtsX is a multi-pass inner-membrane protein and FtsE is membrane-associated on the cytoplasmic side.",
                    },
                    {
                        "preferred_term": "cell division site",
                        "term": deepcopy(CELL_DIVISION_SITE),
                        "description": "FtsEX acts in the divisome/septal-ring context.",
                    },
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "FtsEX ABC-like cell-division complex",
                    "node": {
                        "id": "ftsex_cell_division_complex",
                        "label": "FtsEX cell-division ABC-like complex",
                        "module_type": "PROTEIN_COMPLEX",
                        "description": (
                            "FtsX is the multi-pass membrane component and FtsE is the ATP-binding "
                            "component of an ABC-like complex involved in cell division and septal-ring "
                            "assembly or stability. Transporter terms are retained only as broad "
                            "ABC-family context unless a transported substrate is established."
                        ),
                        "annotons": [
                            annoton(
                                "ftsX",
                                "ftsX: FtsEX membrane component",
                                "Multi-pass inner-membrane FtsEX component involved in cell division.",
                                processes=[CELL_DIVISION],
                                locations=[PLASMA_MEMBRANE, CELL_DIVISION_SITE],
                            ),
                            annoton(
                                "ftsE",
                                "ftsE: FtsEX ATPase component",
                                "ATP-hydrolyzing cytoplasmic-side FtsEX component involved in septal-ring assembly or stability.",
                                function=ATP_HYDROLYSIS,
                                processes=[CELL_DIVISION],
                                locations=[PLASMA_MEMBRANE],
                            ),
                        ],
                    },
                }
            ],
        },
        "notes": (
            "This module is a boundary record for an ABC-family cell-division system, "
            "not evidence that FtsEX imports or exports a defined substrate in P. putida."
        ),
    }


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    MODULE_PATH.write_text(yaml.safe_dump(build_module(), sort_keys=False, width=1000, allow_unicode=False), encoding="utf-8")
    print(f"wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
