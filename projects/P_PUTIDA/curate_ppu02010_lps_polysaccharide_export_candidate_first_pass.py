#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_1778-PP_1779 export candidate."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"
MODULE_PATH = Path("modules/lpt_lps_transport_boundary.yaml")


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
LPS_TRANSPORT = {"id": "GO:0015920", "label": "lipopolysaccharide transport"}
POLYSACCHARIDE_TRANSPORT = {"id": "GO:0015774", "label": "polysaccharide transport"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
TRANS_MEMBRANE_TRANSPORT = {"id": "GO:0055085", "label": "transmembrane transport"}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
ABC_TRANSPORTER = {"id": "GO:0140359", "label": "ABC-type transporter activity"}


GENES = {
    "PP_1778": {
        "accession": "Q88LZ8",
        "kind": "permease",
        "description": (
            "PP_1778 encodes a predicted multi-pass inner-membrane ABC-2 permease "
            "component of a PP_1778-PP_1779 envelope polysaccharide/LPS ABC export "
            "candidate. Its ABC-2 transport domain, CtrC/capsule-polysaccharide-export "
            "PANTHER subfamily assignment, inner-membrane localization, and GOA "
            "lipopolysaccharide-transport annotation support a role in envelope "
            "glycoconjugate export, with exact substrate specificity still unresolved."
        ),
        "product": "Full=Transport permease protein",
        "asta": "Protein Description:** RecName: Full=Transport permease protein",
        "location": "Cell inner membrane",
        "topology": "Multi-pass membrane protein",
        "domain": "InterPro; IPR000412; ABC_2_transport.",
        "tm_domain": "FT   DOMAIN          32..256",
        "panther": "CAPSULE POLYSACCHARIDE EXPORT INNER-MEMBRANE PROTEIN CTRC",
        "keyword": "Polysaccharide transport",
    },
    "PP_1779": {
        "accession": "Q88LZ7",
        "kind": "atpase",
        "description": (
            "PP_1779 encodes a predicted ATP-binding energy-coupling subunit of a "
            "PP_1778-PP_1779 envelope polysaccharide/LPS ABC export candidate. The "
            "protein has ABC ATP-binding and Wzt/TagH-like bacterial polysaccharide "
            "export domains, and the source protein name specifies a lipopolysaccharide "
            "ABC export system. The exact exported substrate should be treated as a "
            "candidate LPS, O-antigen, capsule, or related envelope-polysaccharide "
            "substrate until experimentally resolved."
        ),
        "product": "Full=Lipopolysaccharide ABC export system, ATP-binding protein",
        "asta": "Protein Description:** SubName: Full=Lipopolysaccharide ABC export system, ATP-binding protein",
        "abc_domain": "InterPro; IPR003439; ABC_transporter-like_ATP-bd.",
        "abc_signature": "InterPro; IPR017871; ABC_transporter-like_CS.",
        "tagh_domain": "InterPro; IPR015860; ABC_transpr_TagH-like.",
        "polysaccharide_domain": "InterPro; IPR050683; Bact_Polysacc_Export_ATP-bd.",
        "wzt_domain": "InterPro; IPR029439; Wzt_C.",
        "ft_domain": "FT   DOMAIN          4..244",
    },
}


def pp1778_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["product"])
    domain = support_uniprot(gene, cfg["domain"])
    panther = support_uniprot(gene, cfg["panther"])
    keyword = support_uniprot(gene, cfg["keyword"])
    asta = support_asta(gene, cfg["asta"])
    mapping = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this predicted inner-membrane ABC-2 permease.",
            "ACCEPT",
            "UniProt places PP_1778 in the cell inner membrane as a multi-pass membrane protein.",
            None,
            [support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["topology"])],
        ),
        "GO:0015920": (
            "Lipopolysaccharide transport is appropriate as a first-pass process annotation for this envelope polysaccharide-export permease candidate.",
            "ACCEPT",
            "TreeGrafter assigns lipopolysaccharide transport, while UniProt domains and keywords support bacterial envelope polysaccharide export.",
            None,
            [product, domain, panther, keyword, asta],
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than the plasma membrane annotation.",
            "MARK_AS_OVER_ANNOTATED",
            "The record has a more specific plasma membrane annotation, and UniProt places PP_1778 in the cell inner membrane.",
            None,
            [support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["topology"])],
        ),
        "GO:0043190": (
            "ABC transporter complex membership is appropriate for the predicted PP_1778 permease.",
            "ACCEPT",
            "PP_1778 carries an ABC-2 transport permease domain and is adjacent to the PP_1779 ABC ATP-binding export component.",
            None,
            [product, domain, support_uniprot(gene, cfg["tm_domain"])],
        ),
        "GO:0055085": (
            "Transmembrane transport is correct but too broad for this LPS/polysaccharide export candidate.",
            "MODIFY",
            "The supported process is envelope glycoconjugate export, represented first-pass by the more specific lipopolysaccharide transport annotation.",
            [LPS_TRANSPORT],
            [product, panther, keyword, asta],
        ),
        "GO:0140359": (
            "ABC-type transporter activity is appropriate for the predicted ABC-2 permease component.",
            "ACCEPT",
            "The ABC-2 transmembrane domain supports contribution to ABC transporter activity; the core function records this as a component contribution.",
            None,
            [product, domain, support_uniprot(gene, cfg["tm_domain"]), asta],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def pp1779_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["product"])
    abc_domain = support_uniprot(gene, cfg["abc_domain"])
    abc_signature = support_uniprot(gene, cfg["abc_signature"])
    tagh_domain = support_uniprot(gene, cfg["tagh_domain"])
    polysaccharide_domain = support_uniprot(gene, cfg["polysaccharide_domain"])
    wzt_domain = support_uniprot(gene, cfg["wzt_domain"])
    asta = support_asta(gene, cfg["asta"])
    mapping = {
        "GO:0000166": (
            "Nucleotide binding is true but too broad for this ABC ATP-binding subunit.",
            "MODIFY",
            "The record also has ATP binding, which is the more specific nucleotide-binding annotation for this ABC ATPase.",
            [ATP_BINDING],
            [abc_domain, support_uniprot(gene, cfg["ft_domain"])],
        ),
        "GO:0005524": (
            "ATP binding is appropriate for the PP_1779 ABC ATP-binding component.",
            "ACCEPT",
            "PP_1779 carries an ABC transporter ATP-binding domain and is named as an ATP-binding protein.",
            None,
            [product, abc_domain, support_uniprot(gene, cfg["ft_domain"])],
        ),
        "GO:0016020": (
            "Membrane association is appropriate but broad for this ABC export ATP-binding component.",
            "ACCEPT",
            "The annotation derives from the TagH-like ABC-export domain context; no more specific subcellular location is currently supported for the ATP-binding subunit itself.",
            None,
            [product, tagh_domain],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is the core mechanistic activity of the PP_1779 ABC ATP-binding component.",
            "ACCEPT",
            "ABC ATP-binding and ABC-transporter signature domains support ATP hydrolysis-driven energy coupling.",
            None,
            [product, abc_domain, abc_signature, asta],
        ),
        "GO:0055085": (
            "Transmembrane transport is correct but too broad for the PP_1778-PP_1779 export candidate.",
            "MODIFY",
            "The product name and Wzt/TagH-like bacterial polysaccharide export domains support LPS or related envelope-polysaccharide export rather than generic transport.",
            [LPS_TRANSPORT],
            [product, polysaccharide_domain, wzt_domain, asta],
        ),
        "GO:0140359": (
            "ABC-type transporter activity is appropriate for this predicted ATP-binding export component.",
            "ACCEPT",
            "PP_1779 carries ABC ATPase and TagH/Wzt-like export domains consistent with an ABC transporter energy-coupling subunit.",
            None,
            [product, abc_domain, tagh_domain, polysaccharide_domain, asta],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def add_new_annotations(doc: dict, gene: str, cfg: dict) -> None:
    existing = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}
    if gene == "PP_1779" and LPS_TRANSPORT["id"] not in existing:
        doc.setdefault("existing_annotations", []).append(
            new_annotation(
                LPS_TRANSPORT,
                "involved_in",
                gene,
                "Lipopolysaccharide transport is a useful missing process annotation for PP_1779.",
                "The source protein name specifies a lipopolysaccharide ABC export system, and Wzt/TagH-like domains support bacterial envelope-polysaccharide export.",
                [
                    support_uniprot(gene, cfg["product"]),
                    support_uniprot(gene, cfg["polysaccharide_domain"]),
                    support_uniprot(gene, cfg["wzt_domain"]),
                ],
            )
        )
    if gene == "PP_1779" and ABC_COMPLEX["id"] not in existing:
        doc.setdefault("existing_annotations", []).append(
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                gene,
                "ABC transporter complex membership is a useful missing annotation for PP_1779.",
                "PP_1779 is an ABC ATP-binding export component adjacent to the PP_1778 ABC-2 permease.",
                [
                    support_uniprot(gene, cfg["product"]),
                    support_uniprot(gene, cfg["abc_domain"]),
                    support_uniprot(gene, cfg["tagh_domain"]),
                ],
            )
        )


def set_core_functions(doc: dict, gene: str, cfg: dict) -> None:
    if cfg["kind"] == "permease":
        core = {
            "description": "Multi-pass inner-membrane permease component of the PP_1778-PP_1779 LPS/polysaccharide ABC export candidate.",
            "contributes_to_molecular_function": deepcopy(ABC_TRANSPORTER),
            "directly_involved_in": [deepcopy(LPS_TRANSPORT)],
            "locations": [deepcopy(PLASMA_MEMBRANE)],
            "in_complex": deepcopy(ABC_COMPLEX),
            "supported_by": [
                support_goa(gene, LPS_TRANSPORT["id"], LPS_TRANSPORT["label"]),
                support_goa(gene, ABC_COMPLEX["id"], ABC_COMPLEX["label"]),
                support_goa(gene, PLASMA_MEMBRANE["id"], PLASMA_MEMBRANE["label"]),
                support_uniprot(gene, cfg["product"]),
                support_uniprot(gene, cfg["panther"]),
                support_uniprot(gene, cfg["keyword"]),
                support_uniprot(gene, cfg["location"]),
                support_asta(gene, cfg["asta"]),
            ],
        }
    else:
        core = {
            "description": "ATP-hydrolyzing energy-coupling subunit of the PP_1778-PP_1779 LPS/polysaccharide ABC export candidate.",
            "molecular_function": deepcopy(ATP_HYDROLYSIS),
            "directly_involved_in": [deepcopy(LPS_TRANSPORT)],
            "locations": [deepcopy(MEMBRANE)],
            "in_complex": deepcopy(ABC_COMPLEX),
            "supported_by": [
                support_goa(gene, ATP_HYDROLYSIS["id"], ATP_HYDROLYSIS["label"]),
                support_uniprot(gene, cfg["product"]),
                support_uniprot(gene, cfg["abc_domain"]),
                support_uniprot(gene, cfg["polysaccharide_domain"]),
                support_uniprot(gene, cfg["wzt_domain"]),
                support_asta(gene, cfg["asta"]),
            ],
        }

    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "Is PP_1778-PP_1779 an LPS exporter, a capsule/O-antigen/polysaccharide "
                "exporter, or another Wzt/KpsT-like envelope-glycoconjugate exporter "
                "distinct from canonical LptBFG/MsbA?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Compare LPS, O-antigen/capsular polysaccharide profiles, cell-envelope "
                "permeability, and surface-polysaccharide phenotypes in PP_1778 and "
                "PP_1779 deletion or depletion mutants."
            ),
            "experiment_type": "envelope polysaccharide/LPS export phenotype assay",
        },
        {
            "description": (
                "Reconstitute PP_1778-PP_1779 or assay membrane vesicles with candidate "
                "LPS-core, O-antigen, capsule, or polysialic-acid-like substrates to "
                "resolve transporter specificity."
            ),
            "experiment_type": "ABC transporter substrate-specificity assay",
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
        if cfg["kind"] == "permease":
            ann["review"] = pp1778_review(gene, cfg, term_id, label)
        else:
            ann["review"] = pp1779_review(gene, cfg, term_id, label)

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
        "id": f"{gene}_lps_polysaccharide_export_candidate",
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


def ensure_module_evidence(module_doc: dict) -> None:
    evidence = module_doc.setdefault("evidence", [])
    additions = [
        {
            "source_id": "UniProtKB:Q88LZ8",
            "title": "PP_1778 ABC-2 transport permease",
            "statement": "UniProt places PP_1778 in the ABC-2 integral membrane protein family and records lipopolysaccharide/polysaccharide transport context.",
        },
        {
            "source_id": "UniProtKB:Q88LZ7",
            "title": "PP_1779 lipopolysaccharide ABC export ATP-binding protein",
            "statement": "UniProt names PP_1779 as a lipopolysaccharide ABC export ATP-binding protein with Wzt/TagH-like bacterial polysaccharide export domains.",
        },
    ]
    existing = {entry.get("source_id") for entry in evidence}
    for entry in additions:
        if entry["source_id"] not in existing:
            evidence.append(entry)


def ensure_module_candidate_part() -> None:
    module_doc = yaml.safe_load(MODULE_PATH.read_text(encoding="utf-8"))
    ensure_module_evidence(module_doc)

    description = module_doc.get("description", "")
    candidate_sentence = (
        " It also records PP_1778-PP_1779 as a separate unresolved LPS/polysaccharide "
        "ABC export candidate, not as part of the canonical LptBFG/MsbA route."
    )
    if "PP_1778-PP_1779" not in description:
        module_doc["description"] = description.rstrip(".") + "." + candidate_sentence

    module = module_doc["module"]
    concepts = module.setdefault("concepts", [])
    if POLYSACCHARIDE_TRANSPORT["id"] not in {c.get("term", {}).get("id") for c in concepts}:
        concepts.append(
            concept(
                POLYSACCHARIDE_TRANSPORT,
                "Broader envelope polysaccharide-export context for the unresolved PP_1778-PP_1779 candidate.",
            )
        )

    parts = module.setdefault("parts", [])
    candidate_id = "pp1778_pp1779_lps_polysaccharide_export_candidate"
    for part in parts:
        if part.get("node", {}).get("id") == candidate_id:
            break
    else:
        next_order = max((part.get("order", 0) for part in parts), default=0) + 1
        parts.append(
            {
                "order": next_order,
                "role": "PP_1778-PP_1779 LPS/polysaccharide ABC export candidate",
                "node": {
                    "id": candidate_id,
                    "label": "PP_1778-PP_1779 LPS/polysaccharide ABC export candidate",
                    "module_type": "TRANSPORT_STEP",
                    "description": (
                        "PP_1778 is an ABC-2 multi-pass permease and PP_1779 is a Wzt/KpsT/TagH-like "
                        "ATP-binding protein. Product, domain, and GOA evidence support an envelope "
                        "glycoconjugate export candidate, but this node is kept separate from LptBFG/MsbA "
                        "until its exact LPS, O-antigen, capsule, or related polysaccharide substrate is resolved."
                    ),
                    "concepts": [
                        term_ref(LPS_TRANSPORT),
                        term_ref(POLYSACCHARIDE_TRANSPORT),
                        term_ref(ABC_COMPLEX),
                    ],
                    "annotons": [
                        annoton(
                            "PP_1778",
                            "PP_1778: LPS/polysaccharide export permease candidate",
                            "Predicted multi-pass inner-membrane permease of the PP_1778-PP_1779 export candidate.",
                            function=ABC_TRANSPORTER,
                            processes=[LPS_TRANSPORT, POLYSACCHARIDE_TRANSPORT],
                            locations=[PLASMA_MEMBRANE],
                        ),
                        annoton(
                            "PP_1779",
                            "PP_1779: LPS/polysaccharide export ATPase candidate",
                            "Predicted ATP-hydrolyzing energy-coupling subunit of the PP_1778-PP_1779 export candidate.",
                            function=ATP_HYDROLYSIS,
                            processes=[LPS_TRANSPORT, POLYSACCHARIDE_TRANSPORT],
                            locations=[MEMBRANE],
                        ),
                    ],
                },
            }
        )

    notes = module_doc.get("notes", "")
    candidate_note = (
        " PP_1778-PP_1779 is represented as a separate Wzt/KpsT/TagH-like LPS or "
        "polysaccharide ABC export candidate, not merged into the canonical LptBFG/MsbA system."
    )
    if "Wzt/KpsT/TagH-like" not in notes:
        module_doc["notes"] = notes.rstrip() + candidate_note

    MODULE_PATH.write_text(yaml.safe_dump(module_doc, sort_keys=False, width=1000, allow_unicode=False), encoding="utf-8")
    print(f"extended {MODULE_PATH}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    ensure_module_candidate_part()


if __name__ == "__main__":
    main()
