#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_5177-PP_5181 Spu/Pot importer."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"
MODULE_PATH = Path("modules/polyamine_transport_boundary.yaml")

POLYAMINE_TRANSPORT = {"id": "GO:0015846", "label": "polyamine transport"}
POLYAMINE_TRANSMEMBRANE_TRANSPORT = {
    "id": "GO:1902047",
    "label": "polyamine transmembrane transport",
}
PUTRESCINE_TRANSPORT = {"id": "GO:0015847", "label": "putrescine transport"}
POLYAMINE_BINDING = {"id": "GO:0019808", "label": "polyamine binding"}
ABC_POLYAMINE_TRANSPORTER = {
    "id": "GO:0015417",
    "label": "ABC-type polyamine transporter activity",
}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
ABC_COMPLEX = {
    "id": "GO:0043190",
    "label": "ATP-binding cassette (ABC) transporter complex",
}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0042597", "label": "periplasmic space"}


SPU_GENES = {
    "spuH": {
        "accession": "Q88CK3",
        "locus": "PP_5177",
        "safe": "spuH",
        "kind": "permease",
        "cluster": "C70",
        "role": "putrescine/polyamine ABC importer permease",
        "product_text": "Full=Putrescine transport system permease protein PotI",
        "asta_text": "Protein Description:** RecName: Full=Putrescine transport system permease protein PotI",
        "location_text": "Cell inner membrane",
        "domain_text": "Bact_Polyamine_Transport",
        "description": (
            "spuH (PP_5177) encodes a predicted multi-pass inner-membrane permease subunit of the "
            "PP_5177-PP_5181 Spu/Pot spermidine/putrescine ABC importer. UniProt names it as a PotI-like "
            "putrescine transport-system permease and assigns MetI-like binding-protein-dependent transporter "
            "features, supporting a component role in polyamine transmembrane import."
        ),
    },
    "spuG": {
        "accession": "Q88CK2",
        "locus": "PP_5178",
        "safe": "spuG",
        "kind": "permease",
        "cluster": "C70",
        "role": "spermidine/putrescine ABC importer permease",
        "product_text": "Full=Spermidine/putrescine ABC transporter-inner membrane subunit",
        "asta_text": "Protein Description:** SubName: Full=Spermidine/putrescine ABC transporter-inner membrane subunit",
        "location_text": "Cell membrane",
        "domain_text": "MetI-like",
        "description": (
            "spuG (PP_5178) encodes a predicted multi-pass inner-membrane permease subunit of the "
            "PP_5177-PP_5181 Spu/Pot spermidine/putrescine ABC importer. UniProt and Asta retrieval identify "
            "it as a spermidine/putrescine ABC transporter inner-membrane subunit with MetI-like "
            "binding-protein-dependent transporter features."
        ),
    },
    "spuF": {
        "accession": "Q88CK1",
        "locus": "PP_5179",
        "safe": "spuF",
        "kind": "atpase",
        "cluster": "C70",
        "role": "spermidine/putrescine ABC importer ATP-binding subunit",
        "product_text": "Full=Spermidine/putrescine import ATP-binding protein PotA",
        "asta_text": (
            "Protein Description:** RecName: Full=Spermidine/putrescine import ATP-binding protein PotA "
            "{ECO:0000256|RuleBase:RU364083}; EC=7.6.2.11"
        ),
        "function_text": "Part of the ABC transporter complex PotABCD involved in",
        "reaction_text": "Reaction=ATP + H2O + polyamine-[polyamine-binding protein]Side 1 = ADP",
        "subunit_text": "The complex is composed of two ATP-binding proteins (PotA),",
        "family_text": "Spermidine/putrescine importer (TC 3.A.1.11.1) family.",
        "description": (
            "spuF (PP_5179) encodes the ATP-binding energy-coupling subunit of the PP_5177-PP_5181 "
            "Spu/Pot spermidine/putrescine ABC importer. UniProt names it as PotA, assigns EC 7.6.2.11 "
            "for ATP-driven polyamine import, and describes its role as energy coupling within a PotABCD-like "
            "polyamine transporter complex."
        ),
    },
    "spuE": {
        "accession": "Q88CK0",
        "locus": "PP_5180",
        "safe": "spuE",
        "kind": "binding",
        "cluster": "C70",
        "role": "spermidine/putrescine ABC importer periplasmic binding subunit",
        "product_text": "Full=Spermidine/putrescine ABC transporter-periplasmic subunit",
        "asta_text": "Protein Description:** SubName: Full=Spermidine/putrescine ABC transporter-periplasmic subunit",
        "family_text": "SPERMIDINE/PUTRESCINE-BINDING PERIPLASMIC PROTEIN",
        "domain_text": "InterPro; IPR001188; Sperm_putr-bd.",
        "description": (
            "spuE (PP_5180) encodes a predicted periplasmic substrate-binding subunit of the PP_5177-PP_5181 "
            "Spu/Pot spermidine/putrescine ABC importer. UniProt places the protein in the periplasm and "
            "assigns spermidine/putrescine-binding protein-family features, supporting polyamine substrate "
            "recognition for the importer."
        ),
    },
    "spuD": {
        "accession": "Q88CJ9",
        "locus": "PP_5181",
        "safe": "spuD",
        "kind": "binding",
        "cluster": "C70",
        "role": "spermidine/putrescine ABC importer periplasmic binding subunit",
        "product_text": "Full=Spermidine/putrescine ABC transporter-periplasmic subunit",
        "asta_text": "Protein Description:** SubName: Full=Spermidine/putrescine ABC transporter-periplasmic subunit",
        "family_text": "SPERMIDINE/PUTRESCINE-BINDING PERIPLASMIC PROTEIN",
        "domain_text": "InterPro; IPR001188; Sperm_putr-bd.",
        "description": (
            "spuD (PP_5181) encodes a predicted periplasmic substrate-binding subunit of the PP_5177-PP_5181 "
            "Spu/Pot spermidine/putrescine ABC importer. UniProt places the protein in the periplasm and "
            "assigns spermidine/putrescine-binding protein-family features, supporting polyamine substrate "
            "recognition for the importer."
        ),
    },
}

POTF_GENES = {
    "potF-I": {"accession": "Q88PH7", "locus": "PP_0873", "safe": "potF_I", "cluster": "C17"},
    "PP_2195": {"accession": "Q88KU4", "locus": "PP_2195", "safe": "PP_2195", "cluster": "C30"},
    "potF-II": {"accession": "Q88I54", "locus": "PP_3147", "safe": "potF_II", "cluster": "C43"},
    "PP_3719": {"accession": "Q88GK2", "locus": "PP_3719", "safe": "PP_3719", "cluster": "C49"},
    "potF-III": {"accession": "Q88G80", "locus": "PP_3845", "safe": "potF_III", "cluster": "C53"},
    "potF-IV": {"accession": "Q88C42", "locus": "PP_5341", "safe": "potF_IV", "cluster": "C74"},
}


def go_term(term: dict) -> dict:
    return {"id": term["id"], "label": term["label"]}


def gene_dir(gene: str) -> Path:
    return Path("genes") / SPECIES / gene


def review_path(gene: str) -> Path:
    return gene_dir(gene) / f"{gene}-ai-review.yaml"


def ref(gene: str, suffix: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{suffix}"


def support_goa(gene: str, term_id: str, label: str) -> dict:
    return {"reference_id": ref(gene, "goa.tsv"), "supporting_text": f"{term_id}\t{label}"}


def support_uniprot(gene: str, text: str) -> dict:
    return {"reference_id": ref(gene, "uniprot.txt"), "supporting_text": text}


def support_asta(gene: str, text: str) -> dict:
    return {"reference_id": ref(gene, "deep-research-asta.md"), "supporting_text": text}


def ensure_reference(doc: dict, ref_id: str, title: str, supporting_text: str | None = None) -> None:
    refs = doc.setdefault("references", [])
    for entry in refs:
        if entry.get("id") == ref_id:
            if supporting_text and not entry.get("findings"):
                entry["findings"] = [{"supporting_text": supporting_text}]
            return
    entry = {"id": ref_id, "title": title, "findings": []}
    if supporting_text:
        entry["findings"].append({"supporting_text": supporting_text})
    refs.append(entry)


def review(
    gene: str,
    term_id: str,
    label: str,
    summary: str,
    action: str,
    reason: str,
    *,
    extra_support: list[dict] | None = None,
    proposed: list[dict] | None = None,
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


def binding_complex_review(gene: str, cfg: dict) -> dict:
    return {
        "summary": "ABC transporter complex membership should be added for this Spu/Pot periplasmic binding subunit.",
        "action": "NEW",
        "reason": (
            "UniProt names this protein as a spermidine/putrescine ABC transporter periplasmic subunit, supporting "
            "membership in the PP_5177-PP_5181 Spu/Pot importer complex."
        ),
        "supported_by": [
            support_uniprot(gene, cfg["product_text"]),
            support_uniprot(gene, cfg["family_text"]),
            support_asta(gene, cfg["asta_text"]),
        ],
    }


def binding_complex_annotation(gene: str, cfg: dict) -> dict:
    return {
        "term": go_term(ABC_COMPLEX),
        "evidence_type": "IEA",
        "original_reference_id": ref(gene, "uniprot.txt"),
        "qualifier": "part_of",
        "review": binding_complex_review(gene, cfg),
    }


def permease_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["product_text"])
    asta = support_asta(gene, cfg["asta_text"])
    if term_id == "GO:0005886":
        return review(
            gene,
            term_id,
            label,
            "Plasma membrane localization is appropriate for this predicted inner-membrane polyamine-import permease.",
            "ACCEPT",
            "UniProt places the permease at the bacterial cell membrane or cell inner membrane.",
            extra_support=[support_uniprot(gene, cfg["location_text"]), product, asta],
        )
    if term_id == "GO:0016020":
        return review(
            gene,
            term_id,
            label,
            "Membrane localization is correct but less informative than plasma membrane for this bacterial permease.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also has a plasma-membrane annotation, and UniProt resolves the protein to the bacterial cell membrane.",
            extra_support=[support_uniprot(gene, cfg["location_text"]), product],
        )
    if term_id == "GO:0043190":
        return review(
            gene,
            term_id,
            label,
            "ABC transporter complex membership is appropriate for this Spu/Pot permease component.",
            "ACCEPT",
            "The product name, MetI-like transporter features, and local PP_5177-PP_5181 locus support an ABC-importer permease role.",
            extra_support=[product, support_uniprot(gene, cfg["domain_text"]), asta],
        )
    if term_id == "GO:0055085":
        return review(
            gene,
            term_id,
            label,
            "Transmembrane transport is true but broad relative to the polyamine-import context.",
            "MODIFY",
            "The PotI/Spu inner-membrane subunit annotations support polyamine transmembrane transport as the more specific process.",
            extra_support=[product, support_uniprot(gene, cfg["domain_text"]), asta],
            proposed=[go_term(POLYAMINE_TRANSMEMBRANE_TRANSPORT)],
        )
    raise ValueError(f"Unhandled permease annotation for {gene}: {term_id} {label}")


def atpase_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["product_text"])
    asta = support_asta(gene, cfg["asta_text"])
    if term_id == "GO:0000166":
        return review(
            gene,
            term_id,
            label,
            "Generic nucleotide binding is over-broad for this PotA-family ABC ATP-binding subunit.",
            "MARK_AS_OVER_ANNOTATED",
            "ATP binding and ATP hydrolysis in a polyamine ABC importer are more informative than generic nucleotide binding.",
            extra_support=[product, support_uniprot(gene, cfg["family_text"])],
        )
    if term_id == "GO:0005524":
        return review(
            gene,
            term_id,
            label,
            "ATP binding is appropriate for this ABC ATP-binding subunit but is not the most informative core activity.",
            "KEEP_AS_NON_CORE",
            "SpuF is the PotA ATP-binding energy-coupling component; ATP hydrolysis coupled to polyamine import captures the core mechanistic role more directly.",
            extra_support=[product, support_uniprot(gene, cfg["reaction_text"]), asta],
        )
    if term_id == "GO:0015417":
        return review(
            gene,
            term_id,
            label,
            "ABC-type polyamine transporter activity is appropriate as the complex-level activity to which SpuF contributes.",
            "ACCEPT",
            "UniProt assigns EC 7.6.2.11 and describes SpuF/PotA as the energy-coupling component of a spermidine/putrescine ABC importer.",
            extra_support=[product, support_uniprot(gene, cfg["function_text"]), support_uniprot(gene, cfg["reaction_text"]), asta],
        )
    if term_id == "GO:0015846":
        return review(
            gene,
            term_id,
            label,
            "Polyamine transport is appropriate biological-process context for this PotA-family ATPase.",
            "ACCEPT",
            "The EC-mapped UniProt reaction and PotABCD function statement support ATP-driven import of polyamines by the complex.",
            extra_support=[product, support_uniprot(gene, cfg["reaction_text"]), asta],
        )
    if term_id == "GO:0015847":
        return review(
            gene,
            term_id,
            label,
            "Putrescine transport is supported for this spermidine/putrescine import ATP-binding subunit.",
            "ACCEPT",
            "The product name and PotABCD-like function statement include putrescine import as part of the polyamine ABC transporter context.",
            extra_support=[product, support_uniprot(gene, cfg["function_text"]), asta],
        )
    if term_id == "GO:0016887":
        return review(
            gene,
            term_id,
            label,
            "ATP hydrolysis activity is appropriate for this ABC ATP-binding energy-coupling subunit.",
            "ACCEPT",
            "UniProt assigns the ATP-dependent polyamine-import reaction to SpuF/PotA, supporting ATP hydrolysis as its core molecular activity.",
            extra_support=[product, support_uniprot(gene, cfg["reaction_text"]), asta],
        )
    if term_id == "GO:0022857":
        return review(
            gene,
            term_id,
            label,
            "Generic transmembrane transporter activity is correct only as broad complex context.",
            "MARK_AS_OVER_ANNOTATED",
            "GOA already provides the more specific ABC-type polyamine transporter activity for this ATPase-containing complex.",
            extra_support=[product, support_uniprot(gene, cfg["reaction_text"])],
        )
    if term_id == "GO:0043190":
        return review(
            gene,
            term_id,
            label,
            "ABC transporter complex membership is appropriate for SpuF/PotA.",
            "ACCEPT",
            "UniProt describes SpuF/PotA as one of the ATP-binding proteins in a PotABCD-like spermidine/putrescine importer.",
            extra_support=[product, support_uniprot(gene, cfg["subunit_text"]), asta],
        )
    if term_id == "GO:0055085":
        return review(
            gene,
            term_id,
            label,
            "Transmembrane transport is true but broad relative to polyamine transmembrane transport.",
            "MARK_AS_OVER_ANNOTATED",
            "The record has a more specific polyamine transmembrane transport annotation for the same ATP-coupled importer context.",
            extra_support=[product, support_uniprot(gene, cfg["reaction_text"])],
        )
    if term_id == "GO:1902047":
        return review(
            gene,
            term_id,
            label,
            "Polyamine transmembrane transport is appropriate for the PotA ATP-binding component of the Spu/Pot importer.",
            "ACCEPT",
            "The EC-linked reaction explicitly describes ATP-driven movement of a polyamine from side 1 to side 2 through the transporter.",
            extra_support=[product, support_uniprot(gene, cfg["reaction_text"]), asta],
        )
    raise ValueError(f"Unhandled ATPase annotation for {gene}: {term_id} {label}")


def binding_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["product_text"])
    asta = support_asta(gene, cfg["asta_text"])
    if term_id == "GO:0015846":
        return review(
            gene,
            term_id,
            label,
            "Polyamine transport is appropriate process context for this periplasmic substrate-binding subunit.",
            "ACCEPT",
            "The product name and spermidine/putrescine-binding family assignment support a substrate-recognition role in the Spu/Pot polyamine importer.",
            extra_support=[product, support_uniprot(gene, cfg["family_text"]), asta],
        )
    if term_id == "GO:0019808":
        return review(
            gene,
            term_id,
            label,
            "Polyamine binding is appropriate for this spermidine/putrescine-binding periplasmic protein.",
            "ACCEPT",
            "UniProt, InterPro, and Asta retrieval identify this as a spermidine/putrescine-family periplasmic binding subunit.",
            extra_support=[product, support_uniprot(gene, cfg["domain_text"]), support_uniprot(gene, cfg["family_text"]), asta],
        )
    if term_id == "GO:0042597":
        return review(
            gene,
            term_id,
            label,
            "Periplasmic localization is appropriate for this substrate-binding protein.",
            "ACCEPT",
            "UniProt places the spermidine/putrescine ABC transporter binding subunit in the periplasm.",
            extra_support=[support_uniprot(gene, "Periplasm"), product],
        )
    raise ValueError(f"Unhandled binding annotation for {gene}: {term_id} {label}")


def curate_gene(gene: str, cfg: dict) -> None:
    path = review_path(gene)
    doc = yaml.safe_load(path.read_text())
    doc["status"] = "COMPLETE"
    doc["gene_symbol"] = gene
    doc["description"] = cfg["description"]

    for annotation in doc.get("existing_annotations", []):
        term = annotation.get("term", {})
        term_id = term.get("id")
        label = term.get("label")
        if cfg["kind"] == "permease":
            annotation["review"] = permease_review(gene, cfg, term_id, label)
        elif cfg["kind"] == "atpase":
            annotation["review"] = atpase_review(gene, cfg, term_id, label)
        elif cfg["kind"] == "binding":
            if term_id == ABC_COMPLEX["id"]:
                annotation["review"] = binding_complex_review(gene, cfg)
            else:
                annotation["review"] = binding_review(gene, cfg, term_id, label)
        else:
            raise ValueError(f"Unhandled gene kind for {gene}: {cfg['kind']}")

    if cfg["kind"] == "binding" and not any(
        annotation.get("term", {}).get("id") == ABC_COMPLEX["id"] for annotation in doc.get("existing_annotations", [])
    ):
        doc.setdefault("existing_annotations", []).append(binding_complex_annotation(gene, cfg))

    ensure_reference(doc, ref(gene, "goa.tsv"), f"QuickGO GOA annotations for {gene}")
    ensure_reference(
        doc,
        ref(gene, "uniprot.txt"),
        f"UniProtKB entry for {gene} ({cfg['accession']})",
        cfg["product_text"],
    )
    ensure_reference(
        doc,
        ref(gene, "deep-research-asta.md"),
        f"Asta retrieval report for {gene} ({cfg['accession']})",
        cfg["asta_text"],
    )

    if cfg["kind"] == "permease":
        doc["core_functions"] = [
            {
                "description": "Membrane permease subunit contributing to Spu/Pot polyamine ABC import.",
                "contributes_to_molecular_function": go_term(ABC_POLYAMINE_TRANSPORTER),
                "directly_involved_in": [go_term(POLYAMINE_TRANSMEMBRANE_TRANSPORT)],
                "locations": [go_term(PLASMA_MEMBRANE)],
                "in_complex": go_term(ABC_COMPLEX),
                "supported_by": [
                    support_goa(gene, "GO:0043190", ABC_COMPLEX["label"]),
                    support_uniprot(gene, cfg["product_text"]),
                    support_uniprot(gene, cfg["domain_text"]),
                    support_asta(gene, cfg["asta_text"]),
                ],
            }
        ]
    elif cfg["kind"] == "atpase":
        doc["core_functions"] = [
            {
                "description": "ATP-binding energy-coupling subunit of the Spu/Pot spermidine/putrescine ABC importer.",
                "molecular_function": go_term(ATP_HYDROLYSIS),
                "contributes_to_molecular_function": go_term(ABC_POLYAMINE_TRANSPORTER),
                "directly_involved_in": [go_term(POLYAMINE_TRANSMEMBRANE_TRANSPORT), go_term(PUTRESCINE_TRANSPORT)],
                "in_complex": go_term(ABC_COMPLEX),
                "supported_by": [
                    support_goa(gene, "GO:0016887", ATP_HYDROLYSIS["label"]),
                    support_goa(gene, "GO:0015417", ABC_POLYAMINE_TRANSPORTER["label"]),
                    support_uniprot(gene, cfg["product_text"]),
                    support_uniprot(gene, cfg["reaction_text"]),
                    support_asta(gene, cfg["asta_text"]),
                ],
            }
        ]
    else:
        doc["core_functions"] = [
            {
                "description": "Periplasmic spermidine/putrescine-family substrate-binding subunit of the Spu/Pot polyamine ABC importer.",
                "molecular_function": go_term(POLYAMINE_BINDING),
                "directly_involved_in": [go_term(POLYAMINE_TRANSPORT)],
                "locations": [go_term(PERIPLASM)],
                "in_complex": go_term(ABC_COMPLEX),
                "supported_by": [
                    support_goa(gene, "GO:0019808", POLYAMINE_BINDING["label"]),
                    support_uniprot(gene, cfg["product_text"]),
                    support_uniprot(gene, cfg["family_text"]),
                    support_asta(gene, cfg["asta_text"]),
                ],
            }
        ]

    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "What are the exact substrate preferences and division of labor of the PP_5177-PP_5181 "
                "Spu/Pot importer across putrescine, spermidine, norspermidine, and related polyamines?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                f"Measure uptake and growth phenotypes for a {gene} deletion or depletion strain with putrescine, "
                "spermidine, norspermidine, and related polyamines, and compare with complementation by the intact "
                "PP_5177-PP_5181 locus."
            ),
            "experiment_type": "targeted polyamine ABC-import mutant uptake/growth assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120))
    print(f"curated {path}")


def preferred(term: dict, preferred_term: str | None = None, description: str | None = None) -> dict:
    entry = {"preferred_term": preferred_term or term["label"], "term": go_term(term)}
    if description:
        entry["description"] = description
    return entry


def potf_annoton(gene: str, cfg: dict) -> dict:
    return {
        "id": f"{cfg['safe']}_polyamine_binding_annoton",
        "label": f"{gene}: putrescine/polyamine substrate-binding component",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": preferred(POLYAMINE_BINDING),
        "processes": [preferred(POLYAMINE_TRANSPORT)],
        "locations": [preferred(PERIPLASM)],
        "role_description": "Periplasmic putrescine/polyamine substrate-binding component with unresolved transporter partners.",
    }


def spu_annoton(gene: str, cfg: dict) -> dict:
    base = {
        "id": f"{cfg['safe']}_spu_polyamine_import_annoton",
        "label": f"{gene}: {cfg['role']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "processes": [preferred(POLYAMINE_TRANSMEMBRANE_TRANSPORT)],
        "role_description": cfg["role"].capitalize() + ".",
    }
    if cfg["kind"] == "permease":
        base["function"] = preferred(ABC_POLYAMINE_TRANSPORTER, "contributes to ABC-type polyamine transporter activity")
        base["locations"] = [preferred(PLASMA_MEMBRANE)]
    elif cfg["kind"] == "atpase":
        base["function"] = preferred(ATP_HYDROLYSIS)
    else:
        base["function"] = preferred(POLYAMINE_BINDING)
        base["processes"] = [preferred(POLYAMINE_TRANSPORT)]
        base["locations"] = [preferred(PERIPLASM)]
    return base


def module_evidence() -> list[dict]:
    evidence = [
        {
            "source_id": "KEGG:ppu02010",
            "title": "ABC transporters - Pseudomonas putida KT2440",
            "statement": (
                "KEGG ppu02010 contributes PP_5177-PP_5181 as a coherent Spu/Pot spermidine/putrescine ABC-import "
                "locus, and also contributes potF-I, PP_2195, potF-II, PP_3719, potF-III, and potF-IV as PotF-like "
                "polyamine-binding singleton or boundary components."
            ),
        },
        {
            "source_id": "file:projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.tsv",
            "title": "PSEPK ppu02010 ABC-transporter partition batch",
            "statement": (
                "The ppu02010 partition batch records cluster C70 as PP_5177/spuH, PP_5178/spuG, PP_5179/spuF, "
                "PP_5180/spuE, and PP_5181/spuD, and records the PotF-like paralogs as additional polyamine-binding "
                "boundary components."
            ),
        },
    ]
    for gene, cfg in SPU_GENES.items():
        evidence.append(
            {
                "source_id": f"UniProtKB:{cfg['accession']}",
                "title": f"{gene} {cfg['role']}",
                "statement": f"UniProt records {gene} ({cfg['locus']}) as {cfg['product_text'].removeprefix('Full=')}.",
            }
        )
    for gene, cfg in POTF_GENES.items():
        evidence.append(
            {
                "source_id": f"UniProtKB:{cfg['accession']}",
                "title": f"{gene} putrescine-binding periplasmic protein",
                "statement": (
                    f"UniProt records {gene} ({cfg['locus']}) as a putrescine-binding periplasmic protein and assigns "
                    "it to the spermidine/putrescine-binding periplasmic-protein family."
                ),
            }
        )
    return evidence


def curate_module() -> None:
    doc = {
        "id": "MODULE:polyamine_transport_boundary",
        "title": "Polyamine transport boundary",
        "description": (
            "Boundary module for Pseudomonas putida KT2440 polyamine transport components encountered during ppu02010 "
            "ABC-transporter partitioning. The module now separates the complete PP_5177-PP_5181 Spu/Pot "
            "spermidine/putrescine ABC importer from PotF-like singleton or boundary periplasmic binding proteins "
            "whose cognate permease and ATP-binding partners remain unresolved."
        ),
        "status": "DRAFT",
        "evidence": module_evidence(),
        "module": {
            "id": "polyamine_transport_boundary",
            "label": "Polyamine transport boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                preferred(
                    POLYAMINE_TRANSMEMBRANE_TRANSPORT,
                    description="ATP-dependent import of putrescine, spermidine, norspermidine, or related polyamines.",
                ),
                preferred(POLYAMINE_TRANSPORT, description="General polyamine transport context for binding components."),
                preferred(POLYAMINE_BINDING, description="Substrate recognition by periplasmic polyamine-binding proteins."),
                preferred(
                    ABC_POLYAMINE_TRANSPORTER,
                    description="Complex-level ABC-type polyamine transporter activity.",
                ),
                preferred(ATP_HYDROLYSIS, description="ATP hydrolysis by the SpuF/PotA energy-coupling subunit."),
                preferred(ABC_COMPLEX, description="Multi-component ABC transporter complex."),
            ],
            "context": {
                "cellular_components": [
                    preferred(PLASMA_MEMBRANE, "bacterial plasma membrane", "SpuH and SpuG are predicted inner-membrane permeases."),
                    preferred(PERIPLASM, "periplasmic space", "SpuD/SpuE and PotF-like components are periplasmic binding proteins."),
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "Spu/Pot spermidine/putrescine ABC import",
                    "node": {
                        "id": "spu_pot_polyamine_abc_import",
                        "label": "PP_5177-PP_5181 Spu/Pot spermidine/putrescine ABC import",
                        "module_type": "TRANSPORT_STEP",
                        "description": (
                            "The PP_5177-PP_5181 locus encodes a predicted Spu/Pot polyamine ABC importer: SpuH and "
                            "SpuG are membrane permease components, SpuF/PotA supplies ATP-dependent energy coupling, "
                            "and SpuE/SpuD are periplasmic spermidine/putrescine-family substrate-binding proteins."
                        ),
                        "concepts": [
                            preferred(POLYAMINE_TRANSMEMBRANE_TRANSPORT),
                            preferred(ABC_POLYAMINE_TRANSPORTER),
                            preferred(POLYAMINE_BINDING),
                        ],
                        "annotons": [spu_annoton(gene, SPU_GENES[gene]) for gene in ["spuH", "spuG", "spuF", "spuE", "spuD"]],
                    },
                },
                {
                    "order": 2,
                    "role": "PotF-like putrescine/polyamine binding components",
                    "node": {
                        "id": "potF_like_polyamine_binding_components",
                        "label": "PotF-like putrescine/polyamine binding components",
                        "module_type": "TRANSPORT_STEP",
                        "description": (
                            "These PotF-like proteins are periplasmic putrescine/polyamine substrate-binding components "
                            "identified as ppu02010 singletons or boundary cases. They likely contribute substrate "
                            "recognition to polyamine uptake systems, but matched permease and ATP-binding partners have "
                            "not been assigned in this first-pass partition."
                        ),
                        "concepts": [preferred(POLYAMINE_TRANSPORT), preferred(POLYAMINE_BINDING)],
                        "annotons": [potf_annoton(gene, cfg) for gene, cfg in POTF_GENES.items()],
                    },
                },
            ],
        },
        "notes": (
            "This boundary module was seeded from the C17 ppu02010 potF-I checkpoint, expanded for PotF-like singleton "
            "paralogs from C30/C43/C49/C53/C74, and now extended with the C70 PP_5177-PP_5181 Spu/Pot importer. "
            "The Spu/Pot locus is treated as a complete predicted polyamine ABC importer, while singleton PotF-like "
            "binding proteins remain component-level entries until locus, genetics, or biochemical evidence establishes "
            "their cognate permease/ATPase partners and exact substrate preferences."
        ),
    }
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120))
    print(f"updated {MODULE_PATH}")


def main() -> None:
    for gene, cfg in SPU_GENES.items():
        curate_gene(gene, cfg)
    curate_module()


if __name__ == "__main__":
    main()
