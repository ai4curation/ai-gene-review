#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_3801-PP_3803 Znu-like importer."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"
MODULE_PATH = Path("modules/zinc_import_boundary.yaml")

ZINC_TRANSPORT = {"id": "GO:0006829", "label": "zinc ion transport"}
ZINC_TRANSMEMBRANE = {"id": "GO:0071577", "label": "zinc ion transmembrane transport"}
ZINC_ACTIVITY = {"id": "GO:0015633", "label": "ABC-type zinc transporter activity"}
ZINC_BINDING = {"id": "GO:0008270", "label": "zinc ion binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0042597", "label": "periplasmic space"}

LOCUS = "PP_3801-PP_3803"

GENES = {
    "PP_3801": {
        "accession": "Q88GC3",
        "kind": "binding",
        "description": (
            "PP_3801 encodes a predicted ZnuA-like high-affinity zinc-binding "
            "substrate-binding component. Its ZnuA/PsaA-like domains, zinc-transport "
            "keywords, signal peptide, and adjacent PP_3802/PP_3803 metal-import ABC "
            "ATPase/permease genes support a periplasmic substrate-recognition role "
            "in a second Znu-like zinc/cation ABC import system in KT2440."
        ),
        "uniprot_product": "Full=High-affinity zinc uptake system protein ZnuA",
        "asta_product": "Protein Description:** RecName: Full=High-affinity zinc uptake system protein ZnuA",
        "family": "Belongs to the bacterial solute-binding protein 9 family.",
        "znu_domain": "InterPro; IPR006127; ZnuA-like.",
        "pfam": "Pfam; PF01297; ZnuA; 1.",
        "keyword": "Zinc transport",
        "signal": "FT   SIGNAL          1..20",
    },
    "PP_3802": {
        "accession": "Q88GC2",
        "kind": "atpase",
        "description": (
            "PP_3802 encodes the predicted ATP-binding energy-coupling component of "
            "the adjacent PP_3801-PP_3803 Znu-like cation ABC importer. Its ABC "
            "transporter ATP-binding domain, metal-ion-import ABC family assignment, "
            "and colocalization between the PP_3801 ZnuA-like binding component and "
            "PP_3803 cation permease support ATP hydrolysis-driven metal/zinc import."
        ),
        "uniprot_product": "Full=Cation ABC transporter, ATP-binding protein",
        "asta_product": "Protein Description:** SubName: Full=Cation ABC transporter, ATP-binding protein",
        "abc_domain": "InterPro; IPR003439; ABC_transporter-like_ATP-bd.",
        "metal_domain": "InterPro; IPR050153; Metal_Ion_Import_ABC.",
        "panther": "METAL TRANSPORT SYSTEM ATP-BINDING PROTEIN",
    },
    "PP_3803": {
        "accession": "Q88GC1",
        "kind": "permease",
        "description": (
            "PP_3803 encodes the predicted multi-pass membrane permease component of "
            "the adjacent PP_3801-PP_3803 Znu-like cation ABC importer. UniProt places "
            "the protein in the cell membrane, records ABC-3/TroCD permease domains, "
            "and TreeGrafter associates the family with zinc response, supporting a "
            "membrane-channel role in zinc/cation import with PP_3801 and PP_3802."
        ),
        "uniprot_product": "Full=Cation ABC transporter, permease protein",
        "asta_product": "Protein Description:** SubName: Full=Cation ABC transporter, permease protein",
        "location": "Cell membrane",
        "family": "Belongs to the ABC-3 integral membrane protein family.",
        "domain": "InterPro; IPR001626; ABC_TroCD.",
        "funfam": "Zinc ABC transporter permease",
        "panther": "METAL TRANSPORT SYSTEM MEMBRANE PROTEIN",
    },
}


def term(t: dict) -> dict:
    return {"id": t["id"], "label": t["label"]}


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
    gene: str,
    go_term: dict,
    qualifier: str,
    summary: str,
    reason: str,
    support: list[dict],
) -> dict:
    return {
        "term": term(go_term),
        "evidence_type": "IEA",
        "original_reference_id": uniprot_ref(gene),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": support,
        },
    }


def curation_for_annotation(gene: str, annotation: dict) -> dict:
    cfg = GENES[gene]
    term_id = annotation["term"]["id"]
    label = annotation["term"]["label"]
    product = support_uniprot(gene, cfg["uniprot_product"])
    asta = support_asta(gene, cfg["asta_product"])

    if gene == "PP_3801":
        mapping = {
            "GO:0007155": (
                "Cell adhesion is an adhesin-domain spillover and is not supported as the core role of this ZnuA-like substrate-binding protein.",
                "REMOVE",
                "The product name, ZnuA-like domain, zinc-transport keyword, and locus context support zinc/cation uptake rather than cell adhesion.",
                None,
                [product, support_uniprot(gene, cfg["znu_domain"]), support_uniprot(gene, cfg["keyword"])],
            ),
            "GO:0030001": (
                "Metal ion transport is directionally correct but less precise than zinc ion transport for this ZnuA-like component.",
                "MARK_AS_OVER_ANNOTATED",
                "UniProt names PP_3801 as a high-affinity zinc uptake system protein and records zinc-transport keywords.",
                None,
                [product, support_uniprot(gene, cfg["keyword"]), asta],
            ),
            "GO:0046872": (
                "Metal ion binding is too broad for this ZnuA-like substrate-binding component and should be narrowed to zinc ion binding.",
                "MODIFY",
                "The ZnuA/PsaA-like family assignment and zinc-transport keyword support zinc-specific substrate binding at first pass.",
                [term(ZINC_BINDING)],
                [product, support_uniprot(gene, cfg["znu_domain"]), support_uniprot(gene, cfg["pfam"]), asta],
            ),
        }
    elif gene == "PP_3802":
        mapping = {
            "GO:0000166": (
                "Nucleotide binding is true but less informative than ATP binding for this ABC ATPase component.",
                "MARK_AS_OVER_ANNOTATED",
                "The more specific ATP-binding and ATP-hydrolysis annotations capture the expected chemistry of this ABC transporter ATP-binding subunit.",
                None,
                [product, support_uniprot(gene, cfg["abc_domain"])],
            ),
            "GO:0005524": (
                "ATP binding is appropriate for this predicted ABC transporter ATP-binding subunit.",
                "ACCEPT",
                "UniProt names the protein as a cation ABC transporter ATP-binding protein and records an ABC transporter ATP-binding domain.",
                None,
                [product, support_uniprot(gene, cfg["abc_domain"]), asta],
            ),
            "GO:0016887": (
                "ATP hydrolysis is correct mechanistic chemistry for the energy-coupling subunit but is less specific than the transporter activity.",
                "KEEP_AS_NON_CORE",
                "PP_3802 is an ABC transporter ATP-binding component in a predicted metal/zinc import locus; ATP hydrolysis powers the transport cycle.",
                None,
                [product, support_uniprot(gene, cfg["metal_domain"]), support_uniprot(gene, cfg["panther"]), asta],
            ),
        }
    else:
        mapping = {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass cation ABC transporter permease.",
                "ACCEPT",
                "UniProt places PP_3803 in the cell membrane and predicts multiple transmembrane helices.",
                None,
                [product, support_uniprot(gene, cfg["location"]), asta],
            ),
            "GO:0010043": (
                "Response to zinc ion is indirect and less precise than zinc/cation transmembrane transport for this permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The protein is a cation ABC transporter permease; the zinc-response annotation is best treated as family-context spillover from a metal-import transporter.",
                None,
                [product, support_uniprot(gene, cfg["funfam"]), support_uniprot(gene, cfg["panther"])],
            ),
            "GO:0016020": (
                "Membrane is correct but less specific than plasma membrane for this bacterial multi-pass permease.",
                "MARK_AS_OVER_ANNOTATED",
                "UniProt places PP_3803 in the cell membrane and GOA already includes the more specific plasma membrane term.",
                None,
                [product, support_uniprot(gene, cfg["location"])],
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this permease component.",
                "ACCEPT",
                "PP_3803 has ABC-3/TroCD permease domains and sits next to the ZnuA-like binding component PP_3801 and ATPase PP_3802.",
                None,
                [product, support_uniprot(gene, cfg["domain"]), support_uniprot(gene, cfg["family"]), asta],
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to zinc/cation transmembrane transport for this locus.",
                "MARK_AS_OVER_ANNOTATED",
                "The permease is a metal-transport-system membrane protein in a Znu-like cation ABC import locus.",
                None,
                [product, support_uniprot(gene, cfg["funfam"]), support_uniprot(gene, cfg["panther"])],
            ),
        }

    summary, action, reason, proposed, support = mapping[term_id]
    annotation["review"] = review(
        gene,
        term_id,
        label,
        summary,
        action,
        reason,
        proposed=proposed,
        extra_support=support,
    )
    return annotation


def added_annotations(gene: str) -> list[dict]:
    cfg = GENES[gene]
    if gene == "PP_3801":
        return [
            new_annotation(
                gene,
                ZINC_TRANSPORT,
                "involved_in",
                "Zinc ion transport is the substrate-specific process for this ZnuA-like binding component.",
                "UniProt names PP_3801 as a high-affinity zinc uptake system protein and records zinc-transport keywords.",
                [
                    support_uniprot(gene, cfg["uniprot_product"]),
                    support_uniprot(gene, cfg["keyword"]),
                    support_asta(gene, cfg["asta_product"]),
                ],
            ),
            new_annotation(
                gene,
                PERIPLASM,
                "located_in",
                "Periplasmic localization is expected for a signal-peptide-bearing bacterial ZnuA-like solute-binding component.",
                "PP_3801 has an N-terminal signal peptide and belongs to the bacterial solute-binding protein 9 family.",
                [
                    support_uniprot(gene, cfg["signal"]),
                    support_uniprot(gene, cfg["family"]),
                ],
            ),
            new_annotation(
                gene,
                ABC_COMPLEX,
                "part_of",
                "PP_3801 should be represented as the substrate-binding component of the adjacent Znu-like ABC transporter complex.",
                "The ZnuA-like binding protein is adjacent to a cation ABC ATPase and permease pair in the ppu02010 C50 locus.",
                [
                    support_uniprot(gene, cfg["uniprot_product"]),
                    support_uniprot("PP_3802", GENES["PP_3802"]["uniprot_product"]),
                    support_uniprot("PP_3803", GENES["PP_3803"]["uniprot_product"]),
                ],
            ),
        ]
    if gene == "PP_3802":
        return [
            new_annotation(
                gene,
                ZINC_ACTIVITY,
                "enables",
                "PP_3802 is predicted to provide ATP-dependent transporter activity for the adjacent Znu-like cation importer.",
                "The protein has ABC ATP-binding and metal-ion-import ABC domains and sits between PP_3801/ZnuA-like and PP_3803/permease components.",
                [
                    support_uniprot(gene, cfg["abc_domain"]),
                    support_uniprot(gene, cfg["metal_domain"]),
                    support_uniprot(gene, cfg["panther"]),
                    support_asta(gene, cfg["asta_product"]),
                ],
            ),
            new_annotation(
                gene,
                ZINC_TRANSMEMBRANE,
                "involved_in",
                "PP_3802 is predicted to energize zinc/cation transmembrane import by the C50 ABC transporter.",
                "The neighboring PP_3801 binding component is ZnuA-like, while PP_3802 is a metal-import ABC ATPase.",
                [
                    support_uniprot(gene, cfg["metal_domain"]),
                    support_uniprot("PP_3801", GENES["PP_3801"]["uniprot_product"]),
                    support_asta(gene, cfg["asta_product"]),
                ],
            ),
            new_annotation(
                gene,
                ABC_COMPLEX,
                "part_of",
                "PP_3802 should be represented as the ATP-binding component of the PP_3801-PP_3803 ABC transporter complex.",
                "The protein is an ABC transporter ATP-binding protein in a three-gene Znu-like import locus.",
                [
                    support_uniprot(gene, cfg["uniprot_product"]),
                    support_uniprot(gene, cfg["abc_domain"]),
                ],
            ),
        ]
    return [
        new_annotation(
            gene,
            ZINC_ACTIVITY,
            "contributes_to",
            "PP_3803 is predicted to contribute the membrane permease component to ABC-type zinc/cation transporter activity.",
            "The protein has ABC-3/TroCD permease domains and a zinc ABC transporter permease FunFam assignment.",
            [
                support_uniprot(gene, cfg["domain"]),
                support_uniprot(gene, cfg["funfam"]),
                support_asta(gene, cfg["asta_product"]),
            ],
        ),
        new_annotation(
            gene,
            ZINC_TRANSMEMBRANE,
            "involved_in",
            "PP_3803 is predicted to mediate zinc/cation movement across the bacterial plasma membrane as the permease component.",
            "PP_3803 is a multi-pass cation ABC transporter permease with metal-transport-system family support.",
            [
                support_uniprot(gene, cfg["uniprot_product"]),
                support_uniprot(gene, cfg["funfam"]),
                support_uniprot(gene, cfg["panther"]),
            ],
        ),
    ]


def core_function(gene: str) -> dict:
    cfg = GENES[gene]
    if gene == "PP_3801":
        return {
            "description": "Predicted periplasmic ZnuA-like zinc-binding component of the PP_3801-PP_3803 cation ABC importer.",
            "molecular_function": term(ZINC_BINDING),
            "directly_involved_in": [term(ZINC_TRANSPORT)],
            "locations": [term(PERIPLASM)],
            "in_complex": term(ABC_COMPLEX),
            "supported_by": [
                support_uniprot(gene, cfg["uniprot_product"]),
                support_uniprot(gene, cfg["znu_domain"]),
                support_uniprot(gene, cfg["keyword"]),
                support_asta(gene, cfg["asta_product"]),
            ],
        }
    if gene == "PP_3802":
        return {
            "description": "Predicted ATP-binding energy-coupling component of the PP_3801-PP_3803 Znu-like cation ABC importer.",
            "molecular_function": term(ZINC_ACTIVITY),
            "directly_involved_in": [term(ZINC_TRANSMEMBRANE)],
            "in_complex": term(ABC_COMPLEX),
            "supported_by": [
                support_uniprot(gene, cfg["uniprot_product"]),
                support_uniprot(gene, cfg["abc_domain"]),
                support_uniprot(gene, cfg["metal_domain"]),
                support_asta(gene, cfg["asta_product"]),
            ],
        }
    return {
        "description": "Predicted multi-pass membrane permease component of the PP_3801-PP_3803 Znu-like cation ABC importer.",
        "contributes_to_molecular_function": term(ZINC_ACTIVITY),
        "directly_involved_in": [term(ZINC_TRANSMEMBRANE)],
        "locations": [term(PLASMA_MEMBRANE)],
        "in_complex": term(ABC_COMPLEX),
        "supported_by": [
            support_uniprot(gene, cfg["uniprot_product"]),
            support_uniprot(gene, cfg["location"]),
            support_uniprot(gene, cfg["funfam"]),
            support_asta(gene, cfg["asta_product"]),
        ],
    }


def curate_gene(gene: str) -> None:
    path = Path(f"genes/{SPECIES}/{gene}/{gene}-ai-review.yaml")
    doc = yaml.safe_load(path.read_text())
    cfg = GENES[gene]
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]
    doc["existing_annotations"] = [
        curation_for_annotation(gene, deepcopy(annotation))
        for annotation in doc.get("existing_annotations", [])
    ]
    doc["existing_annotations"].extend(added_annotations(gene))
    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(
        doc,
        uniprot_ref(gene),
        f"UniProtKB entry for {gene} ({cfg['accession']})",
        cfg["uniprot_product"],
    )
    ensure_reference(
        doc,
        asta_ref(gene),
        f"Asta retrieval report for {gene} ({cfg['accession']})",
        cfg["asta_product"],
    )
    # Cross-locus support is used for the inferred ABC-complex role.
    for other, other_cfg in GENES.items():
        if other != gene:
            ensure_reference(
                doc,
                uniprot_ref(other),
                f"UniProtKB entry for {other} ({other_cfg['accession']})",
                other_cfg["uniprot_product"],
            )
    doc["core_functions"] = [core_function(gene)]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "Does the PP_3801-PP_3803 Znu-like locus function as a second zinc-specific "
                "importer in KT2440, or does it prefer another transition-metal substrate?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Measure metal uptake and growth phenotypes for PP_3801, PP_3802, and PP_3803 "
                "deletion mutants under zinc and related transition-metal limitation, then "
                "complement the full locus to confirm substrate specificity."
            ),
            "experiment_type": "targeted ABC-transporter mutant uptake and growth assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=88))


def extend_module() -> None:
    doc = yaml.safe_load(MODULE_PATH.read_text())
    doc["description"] = (
        "Boundary module for Znu-like high-affinity zinc/cation ABC importers from "
        "the KEGG ppu02010 ABC transporter umbrella map in Pseudomonas putida KT2440. "
        "The module includes the curated PP_0117-PP_0120 ZnuABC importer and the "
        "newly curated PP_3801-PP_3803 Znu-like cation importer candidate. It keeps "
        "zinc/cation import separate from adjacent methionine, phosphonate, and other "
        "ABC-transporter neighborhoods."
    )
    evidence = doc.setdefault("evidence", [])
    existing_sources = {entry.get("source_id") for entry in evidence}
    new_evidence = [
        {
            "source_id": "UniProtKB:Q88GC3",
            "title": "PP_3801 ZnuA-like high-affinity zinc uptake system protein",
            "statement": (
                "UniProt names PP_3801 as a high-affinity zinc uptake system protein "
                "ZnuA, records ZnuA-like/PsaA-like domains, and flags zinc transport."
            ),
        },
        {
            "source_id": "UniProtKB:Q88GC2",
            "title": "PP_3802 cation ABC transporter ATP-binding protein",
            "statement": (
                "UniProt names PP_3802 as a cation ABC transporter ATP-binding protein "
                "with ABC-transporter and metal-ion-import ATPase domains."
            ),
        },
        {
            "source_id": "UniProtKB:Q88GC1",
            "title": "PP_3803 cation ABC transporter permease protein",
            "statement": (
                "UniProt names PP_3803 as a cation ABC transporter permease, places it "
                "in the cell membrane, and records ABC-3/TroCD permease features."
            ),
        },
    ]
    evidence.extend(entry for entry in new_evidence if entry["source_id"] not in existing_sources)

    parts = doc["module"].setdefault("parts", [])
    parts = [part for part in parts if part.get("node", {}).get("id") != "pp3801_pp3803_znu_like_import"]
    parts.append(
        {
            "order": 2,
            "role": "Znu-like cation/zinc ABC import candidate",
            "node": {
                "id": "pp3801_pp3803_znu_like_import",
                "label": "PP_3801-PP_3803 Znu-like cation/zinc ABC import",
                "module_type": "TRANSPORT_STEP",
                "description": (
                    "PP_3801, PP_3802, and PP_3803 form a predicted second Znu-like "
                    "metal ABC importer. PP_3801 is the ZnuA-like substrate-binding "
                    "component, PP_3802 is the ATP-binding energy-coupling subunit, "
                    "and PP_3803 is the multi-pass membrane permease. Exact substrate "
                    "specificity remains to be tested."
                ),
                "concepts": [
                    {"preferred_term": "zinc ion transport", "term": term(ZINC_TRANSPORT)},
                    {
                        "preferred_term": "zinc ion transmembrane transport",
                        "term": term(ZINC_TRANSMEMBRANE),
                    },
                    {
                        "preferred_term": "ATP-binding cassette (ABC) transporter complex",
                        "term": term(ABC_COMPLEX),
                    },
                ],
                "annotons": [
                    {
                        "id": "PP_3801_znu_like_binding_component",
                        "label": "PP_3801: ZnuA-like zinc/cation-binding component",
                        "participant": {"selector_type": "GENE", "gene": {"preferred_term": "PP_3801"}},
                        "function": {"preferred_term": "zinc ion binding", "term": term(ZINC_BINDING)},
                        "processes": [
                            {"preferred_term": "zinc ion transport", "term": term(ZINC_TRANSPORT)}
                        ],
                        "locations": [
                            {"preferred_term": "periplasmic space", "term": term(PERIPLASM)}
                        ],
                        "role_description": (
                            "Predicted signal-peptide-bearing periplasmic ZnuA-like "
                            "substrate-binding component."
                        ),
                    },
                    {
                        "id": "PP_3802_znu_like_abc_atpase",
                        "label": "PP_3802: cation ABC ATP-binding subunit",
                        "participant": {"selector_type": "GENE", "gene": {"preferred_term": "PP_3802"}},
                        "function": {
                            "preferred_term": "ABC-type zinc transporter activity",
                            "term": term(ZINC_ACTIVITY),
                        },
                        "processes": [
                            {
                                "preferred_term": "zinc ion transmembrane transport",
                                "term": term(ZINC_TRANSMEMBRANE),
                            }
                        ],
                        "role_description": (
                            "Predicted ATP-binding energy-coupling subunit of the "
                            "PP_3801-PP_3803 Znu-like importer."
                        ),
                    },
                    {
                        "id": "PP_3803_znu_like_abc_permease",
                        "label": "PP_3803: cation ABC transporter permease",
                        "participant": {"selector_type": "GENE", "gene": {"preferred_term": "PP_3803"}},
                        "function": {
                            "preferred_term": "ABC-type zinc transporter activity",
                            "term": term(ZINC_ACTIVITY),
                        },
                        "processes": [
                            {
                                "preferred_term": "zinc ion transmembrane transport",
                                "term": term(ZINC_TRANSMEMBRANE),
                            }
                        ],
                        "locations": [
                            {"preferred_term": "plasma membrane", "term": term(PLASMA_MEMBRANE)}
                        ],
                        "role_description": (
                            "Predicted multi-pass membrane permease component of the "
                            "PP_3801-PP_3803 Znu-like importer."
                        ),
                    },
                ],
            },
        }
    )
    doc["module"]["parts"] = parts
    doc["notes"] = (
        "This boundary module was created from the mixed C02 PP_0112-PP_0120 "
        "ppu02010 neighborhood and extended with the C50 PP_3801-PP_3803 Znu-like "
        "locus. PP_0120 is kept under its current review folder name rather than "
        "renamed znuA until local gene-symbol reconciliation is handled separately. "
        "The PP_3801-PP_3803 locus is retained as a substrate-specific zinc/cation "
        "candidate pending direct uptake evidence."
    )
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=88))


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
        print(f"curated {gene}")
    extend_module()
    print(f"updated {MODULE_PATH}")


if __name__ == "__main__":
    main()
