#!/usr/bin/env python3
"""First-pass curation for ppu02010 ferric/iron ABC import clusters."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"
MODULE_PATH = Path("modules/ferric_iron_abc_import_boundary.yaml")

ABC_FERRIC_IRON_ACTIVITY = {
    "id": "GO:0015408",
    "label": "ABC-type ferric iron transporter activity",
}
FERRIC_IRON_BINDING = {"id": "GO:0008199", "label": "ferric iron binding"}
IRON_TRANSPORT = {"id": "GO:0006826", "label": "iron ion transport"}
IRON_TRANSMEMBRANE = {"id": "GO:0034755", "label": "iron ion transmembrane transport"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
ABC_COMPLEX = {
    "id": "GO:0043190",
    "label": "ATP-binding cassette (ABC) transporter complex",
}
PERIPLASM = {
    "id": "GO:0030288",
    "label": "outer membrane-bounded periplasmic space",
}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}

GENES = {
    "PP_4881": {
        "accession": "Q88DE5",
        "cluster": "C63",
        "kind": "binding",
        "description": (
            "PP_4881 encodes a predicted periplasmic iron-binding substrate-binding "
            "component of a PP_4881-PP_4882 iron ABC import locus. Its iron "
            "ABC-transporter product name, ferric-binding domain, signal peptide, and "
            "iron-utilization PANTHER subfamily support ferric/iron substrate binding, "
            "while the neighboring PP_4882 permease supports transporter-locus context."
        ),
        "product": "Full=Iron ABC transporter, periplasmic iron-binding protein",
        "asta": "Protein Description:** SubName: Full=Iron ABC transporter, periplasmic iron-binding protein",
        "domain": "InterPro; IPR026045; Ferric-bd.",
        "family": "Belongs to the bacterial solute-binding protein 1 family.",
        "panther": "IRON-UTILIZATION PERIPLASMIC PROTEIN",
        "keyword": "Iron {ECO:0000256|PIRSR:PIRSR002825-1}",
        "signal": "FT   SIGNAL          1..28",
    },
    "PP_4882": {
        "accession": "Q88DE4",
        "cluster": "C63",
        "kind": "permease",
        "description": (
            "PP_4882 encodes the predicted multi-pass inner-membrane permease of the "
            "PP_4881-PP_4882 iron ABC import locus. Its iron ABC-transporter "
            "product name, cell-inner-membrane localization, binding-protein-dependent "
            "permease family assignment, and Fe(3+) transport PANTHER subfamily support "
            "a membrane-channel role in iron import."
        ),
        "product": "Full=Iron ABC transporter, permease protein",
        "asta": "Protein Description:** SubName: Full=Iron ABC transporter, permease protein",
        "location": "Cell inner membrane",
        "family": "Belongs to the binding-protein-dependent transport system",
        "domain": "InterPro; IPR000515; MetI-like.",
        "panther": "FE(3+)-TRANSPORT SYSTEM PERMEASE PROTEIN FBPB 2",
    },
    "PP_5135": {
        "accession": "Q88CP5",
        "cluster": "C67",
        "kind": "binding",
        "description": (
            "PP_5135 encodes the predicted periplasmic substrate-binding component "
            "of the PP_5135-PP_5137 FbpABC-like ferric/iron ABC importer. The "
            "ferric-binding domain, iron keyword, signal peptide, and adjacent "
            "PP_5136 permease plus fbpC ATPase support ferric/iron import."
        ),
        "product": "Full=ABC transporter, periplasmic binding protein",
        "asta": "Protein Description:** SubName: Full=ABC transporter, periplasmic binding protein",
        "domain": "InterPro; IPR026045; Ferric-bd.",
        "other_domain": "InterPro; IPR017663; ABC_2-AEP-bd.",
        "keyword": "Iron {ECO:0000256|PIRSR:PIRSR002825-1}",
        "signal": "FT   SIGNAL          1..21",
    },
    "PP_5136": {
        "accession": "Q88CP4",
        "cluster": "C67",
        "kind": "permease",
        "description": (
            "PP_5136 encodes the predicted multi-pass membrane permease component "
            "of the PP_5135-PP_5137 FbpABC-like ferric/iron ABC importer. Its "
            "binding-protein-dependent permease domains and placement between the "
            "PP_5135 ferric-binding protein and fbpC ATPase support iron-transporter "
            "permease function."
        ),
        "product": "Full=ABC transporter, permease protein",
        "asta": "Protein Description:** SubName: Full=ABC transporter, permease protein",
        "location": "Cell membrane",
        "family": "Belongs to the binding-protein-dependent transport system",
        "domain": "InterPro; IPR000515; MetI-like.",
        "other_domain": "InterPro; IPR017664; AminoethylPonate_ABC_perm-1.",
    },
    "fbpC": {
        "accession": "Q88CP3",
        "cluster": "C67",
        "kind": "atpase",
        "description": (
            "fbpC (PP_5137) encodes the predicted ATP-binding energy-coupling "
            "component of the PP_5135-PP_5137 FbpABC-like ferric/iron ABC importer. "
            "Its ferric-iron ABC transporter product name and ABC ATPase domains "
            "support ATP hydrolysis-driven ferric/iron import with PP_5135 and PP_5136."
        ),
        "product": "Full=Ferric iron ABC transporter, ATP-binding protein",
        "asta": "Protein Description:** SubName: Full=Ferric iron ABC transporter, ATP-binding protein",
        "abc_domain": "InterPro; IPR003439; ABC_transporter-like_ATP-bd.",
        "importer_domain": "InterPro; IPR050093; ABC_SmlMolc_Importer.",
        "atp_keyword": "ATP-binding {ECO:0000256|ARBA:ARBA00022840",
        "membrane_keyword": "Cell inner membrane",
    },
    "PP_5195": {
        "accession": "Q88CI6",
        "cluster": "C71",
        "kind": "permease",
        "description": (
            "PP_5195 encodes a predicted multi-pass membrane permease of a "
            "PP_5195-fbpA iron ABC import locus. Its iron ABC-transporter product name, "
            "cell-membrane localization, binding-protein-dependent permease family, and "
            "iron-utilization PANTHER support a membrane-channel role with fbpA."
        ),
        "product": "Full=Iron ABC transporter, permease protein",
        "asta": "Protein Description:** SubName: Full=Iron ABC transporter, permease protein",
        "location": "Cell membrane",
        "family": "Belongs to the binding-protein-dependent transport system",
        "domain": "InterPro; IPR000515; MetI-like.",
        "panther": "IRON UTILIZATION PROTEIN",
    },
    "fbpA": {
        "accession": "Q88CI5",
        "cluster": "C71",
        "kind": "binding",
        "description": (
            "fbpA (PP_5196) encodes a predicted periplasmic iron(III)-binding "
            "substrate-binding component of the PP_5195-fbpA iron ABC import "
            "locus. Its iron(III) ABC-transporter product name, ferric-binding domain, "
            "iron keyword, signal peptide, and iron-utilization PANTHER subfamily support "
            "ferric/iron binding."
        ),
        "product": "Full=Iron(III) iron ABC transporter, periplasmic iron-binding protein",
        "asta": "Protein Description:** SubName: Full=Iron(III) iron ABC transporter, periplasmic iron-binding protein",
        "domain": "InterPro; IPR026045; Ferric-bd.",
        "family": "Belongs to the bacterial solute-binding protein 1 family.",
        "panther": "IRON-UTILIZATION PERIPLASMIC PROTEIN",
        "keyword": "Iron {ECO:0000256|PIRSR:PIRSR002825-1}",
        "signal": "FT   SIGNAL          1..22",
    },
}


def go_term(term: dict) -> dict:
    return {"id": term["id"], "label": term["label"]}


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
    extra_support: list[dict] | None = None,
    proposed: list[dict] | None = None,
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if extra_support:
        supported_by.extend(extra_support)
    result = {"summary": summary, "action": action, "reason": reason, "supported_by": supported_by}
    if proposed:
        result["proposed_replacement_terms"] = deepcopy(proposed)
    return result


def new_annotation(gene: str, term: dict, qualifier: str, summary: str, reason: str, support: list[dict]) -> dict:
    return {
        "term": go_term(term),
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


def binding_support(gene: str) -> list[dict]:
    cfg = GENES[gene]
    support = [support_uniprot(gene, cfg["product"]), support_uniprot(gene, cfg["domain"]), support_asta(gene, cfg["asta"])]
    for key in ("keyword", "panther", "family"):
        if key in cfg:
            support.append(support_uniprot(gene, cfg[key]))
    return support


def permease_support(gene: str) -> list[dict]:
    cfg = GENES[gene]
    support = [
        support_uniprot(gene, cfg["product"]),
        support_uniprot(gene, cfg["location"]),
        support_uniprot(gene, cfg["domain"]),
        support_asta(gene, cfg["asta"]),
    ]
    for key in ("panther", "family", "other_domain"):
        if key in cfg:
            support.append(support_uniprot(gene, cfg[key]))
    return support


def atpase_support(gene: str) -> list[dict]:
    cfg = GENES[gene]
    return [
        support_uniprot(gene, cfg["product"]),
        support_uniprot(gene, cfg["abc_domain"]),
        support_uniprot(gene, cfg["importer_domain"]),
        support_asta(gene, cfg["asta"]),
    ]


def curate_existing_annotation(gene: str, annotation: dict) -> dict:
    cfg = GENES[gene]
    term_id = annotation["term"]["id"]
    label = annotation["term"]["label"]

    if cfg["kind"] == "binding":
        mapping = {
            "GO:0030288": (
                "Periplasmic localization is appropriate for this signal-peptide-bearing iron ABC substrate-binding protein.",
                "ACCEPT",
                "The protein is a predicted periplasmic binding component with a signal peptide and ferric-binding domain.",
                [support_uniprot(gene, cfg["product"]), support_uniprot(gene, cfg["signal"]), support_uniprot(gene, cfg["domain"])],
                None,
            ),
            "GO:0015888": (
                "Thiamine transport is not supported for this locus and appears to be a TreeGrafter/PANTHER family spillover.",
                "REMOVE",
                "PP_5135 has a ferric-binding domain and iron keyword and sits next to an FbpC ferric-iron ABC ATPase; the locus context supports iron import rather than thiamine transport.",
                [support_uniprot(gene, cfg["domain"]), support_uniprot(gene, cfg["keyword"]), support_uniprot("fbpC", GENES["fbpC"]["product"])],
                None,
            ),
            "GO:0030975": (
                "Thiamine binding is not supported for this PP_5135 substrate-binding component.",
                "REMOVE",
                "The fetched UniProt/domain evidence supports ferric/iron binding, while the thiamine term is inherited from a broad thiamine-binding-periplasmic-protein-related family.",
                [support_uniprot(gene, cfg["domain"]), support_uniprot(gene, cfg["keyword"]), support_uniprot(gene, cfg["product"])],
                None,
            ),
            "GO:0030976": (
                "Thiamine pyrophosphate binding is not supported for this PP_5135 substrate-binding component.",
                "REMOVE",
                "The protein is a predicted ferric/iron ABC substrate-binding component, not a thiamine-pyrophosphate-binding enzyme or transporter.",
                [support_uniprot(gene, cfg["domain"]), support_uniprot(gene, cfg["keyword"]), support_uniprot(gene, cfg["product"])],
                None,
            ),
        }
    elif cfg["kind"] == "permease":
        mapping = {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass bacterial ABC transporter permease.",
                "ACCEPT",
                "UniProt places the protein in the cell or inner membrane and predicts a multi-pass membrane permease.",
                [support_uniprot(gene, cfg["product"]), support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["domain"])],
                None,
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial ABC permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The same GOA set or UniProt subcellular annotation supports the more specific plasma-membrane/cell-membrane localization.",
                [support_uniprot(gene, cfg["product"]), support_uniprot(gene, cfg["location"])],
                None,
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this permease component.",
                "ACCEPT",
                "The protein is a binding-protein-dependent ABC transporter permease in an iron-import locus.",
                permease_support(gene),
                None,
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to iron ion transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name and locus context support an iron ABC import permease rather than an unspecified transporter.",
                permease_support(gene),
                None,
            ),
        }
    else:
        mapping = {
            "GO:0000166": (
                "Nucleotide binding is true but less informative than ATP binding for this ABC ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The more specific ATP-binding and ATP-hydrolysis annotations capture the expected chemistry of the transporter ATPase.",
                [support_uniprot(gene, cfg["product"]), support_uniprot(gene, cfg["abc_domain"])],
                None,
            ),
            "GO:0005524": (
                "ATP binding is appropriate for this ferric-iron ABC transporter ATP-binding subunit.",
                "ACCEPT",
                "UniProt names fbpC as a ferric iron ABC transporter ATP-binding protein and records an ABC ATPase domain.",
                atpase_support(gene),
                None,
            ),
            "GO:0015697": (
                "Quaternary ammonium group transport is not supported for this ferric-iron ABC ATPase.",
                "REMOVE",
                "The product name and adjacent PP_5135 ferric-binding component support iron import; the quaternary-ammonium process is automated family spillover.",
                [support_uniprot(gene, cfg["product"]), support_uniprot("PP_5135", GENES["PP_5135"]["domain"])],
                None,
            ),
            "GO:0016887": (
                "ATP hydrolysis is correct mechanistic chemistry but is less specific than ABC-type ferric iron transporter activity.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers the ABC transporter cycle, while GO:0015408 captures the substrate-specific transporter activity.",
                atpase_support(gene),
                None,
            ),
            "GO:0022857": (
                "Generic transmembrane transporter activity should be narrowed to ABC-type ferric iron transporter activity.",
                "MODIFY",
                "The protein is named as a ferric iron ABC transporter ATP-binding subunit and belongs to an FbpABC-like iron-import locus.",
                atpase_support(gene),
                [go_term(ABC_FERRIC_IRON_ACTIVITY)],
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this ATP-binding component.",
                "ACCEPT",
                "fbpC is the ATP-binding subunit of the PP_5135-PP_5137 ferric/iron ABC transporter candidate.",
                atpase_support(gene),
                None,
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to iron ion transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name and locus context support ferric/iron ABC import rather than unspecified transmembrane transport.",
                atpase_support(gene),
                None,
            ),
        }

    summary, action, reason, extra_support, proposed = mapping[term_id]
    annotation["review"] = review(gene, term_id, label, summary, action, reason, extra_support, proposed)
    return annotation


def added_annotations(gene: str) -> list[dict]:
    cfg = GENES[gene]
    if cfg["kind"] == "binding":
        support = binding_support(gene)
        return [
            new_annotation(
                gene,
                FERRIC_IRON_BINDING,
                "enables",
                "Ferric iron binding is the substrate-recognition role expected for this periplasmic iron ABC binding component.",
                "The protein has a ferric-binding domain, iron keyword/product context, and a signal peptide.",
                support,
            ),
            new_annotation(
                gene,
                IRON_TRANSPORT,
                "involved_in",
                "Iron ion transport is the substrate-specific process for this iron ABC substrate-binding component.",
                "The binding protein is part of a predicted iron ABC import locus.",
                support,
            ),
            new_annotation(
                gene,
                ABC_COMPLEX,
                "part_of",
                "The binding protein should be represented as part of an ABC importer complex candidate.",
                "The gene sits in an iron ABC transporter locus with matching permease and, for C67, ATPase components.",
                support,
            ),
        ]
    if cfg["kind"] == "permease":
        support = permease_support(gene)
        return [
            new_annotation(
                gene,
                ABC_FERRIC_IRON_ACTIVITY,
                "contributes_to",
                "The permease is predicted to contribute the membrane channel to ABC-type ferric/iron transporter activity.",
                "The product name, membrane localization, and binding-protein-dependent permease domains support iron ABC import context.",
                support,
            ),
            new_annotation(
                gene,
                IRON_TRANSMEMBRANE,
                "involved_in",
                "The permease is predicted to mediate iron ion movement across the bacterial plasma membrane.",
                "The permease is part of a predicted iron ABC import locus.",
                support,
            ),
        ]
    support = atpase_support(gene)
    return [
        new_annotation(
            gene,
            ABC_FERRIC_IRON_ACTIVITY,
            "enables",
            "fbpC is predicted to provide ATP-dependent ferric/iron ABC transporter activity for the PP_5135-PP_5137 locus.",
            "The protein is named as a ferric iron ABC transporter ATP-binding protein with ABC ATPase domains.",
            support,
        ),
        new_annotation(
            gene,
            IRON_TRANSMEMBRANE,
            "involved_in",
            "fbpC is predicted to energize iron ion transmembrane import by the PP_5135-PP_5137 ABC transporter.",
            "The ATPase is adjacent to a ferric-binding protein and a binding-protein-dependent permease.",
            support + [support_uniprot("PP_5135", GENES["PP_5135"]["domain"])],
        ),
        new_annotation(
            gene,
            PLASMA_MEMBRANE,
            "located_in",
            "fbpC is predicted to associate with the bacterial plasma membrane as the ATP-binding subunit of the iron ABC importer.",
            "UniProt records cell-inner-membrane context for this ABC transporter ATP-binding component.",
            [support_uniprot(gene, cfg["product"]), support_uniprot(gene, cfg["membrane_keyword"])],
        ),
    ]


def core_function(gene: str) -> dict:
    cfg = GENES[gene]
    if cfg["kind"] == "binding":
        return {
            "description": f"Predicted periplasmic ferric/iron-binding component of the {cfg['cluster']} iron ABC import locus.",
            "molecular_function": go_term(FERRIC_IRON_BINDING),
            "directly_involved_in": [go_term(IRON_TRANSPORT)],
            "locations": [go_term(PERIPLASM)],
            "in_complex": go_term(ABC_COMPLEX),
            "supported_by": binding_support(gene),
        }
    if cfg["kind"] == "permease":
        return {
            "description": f"Predicted multi-pass membrane permease component of the {cfg['cluster']} iron ABC import locus.",
            "contributes_to_molecular_function": go_term(ABC_FERRIC_IRON_ACTIVITY),
            "directly_involved_in": [go_term(IRON_TRANSMEMBRANE)],
            "locations": [go_term(PLASMA_MEMBRANE)],
            "in_complex": go_term(ABC_COMPLEX),
            "supported_by": permease_support(gene),
        }
    return {
        "description": "Predicted ATP-binding energy-coupling component of the PP_5135-PP_5137 ferric/iron ABC importer.",
        "molecular_function": go_term(ABC_FERRIC_IRON_ACTIVITY),
        "directly_involved_in": [go_term(IRON_TRANSMEMBRANE)],
        "locations": [go_term(PLASMA_MEMBRANE)],
        "in_complex": go_term(ABC_COMPLEX),
        "supported_by": atpase_support(gene),
    }


def curate_gene(gene: str) -> None:
    path = Path(f"genes/{SPECIES}/{gene}/{gene}-ai-review.yaml")
    doc = yaml.safe_load(path.read_text())
    cfg = GENES[gene]
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]
    source_annotations = [
        annotation
        for annotation in doc.get("existing_annotations", [])
        if annotation.get("review", {}).get("action") != "NEW"
    ]
    doc["existing_annotations"] = [curate_existing_annotation(gene, deepcopy(annotation)) for annotation in source_annotations]
    doc["existing_annotations"].extend(added_annotations(gene))
    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['accession']})", cfg["product"])
    ensure_reference(doc, asta_ref(gene), f"Asta retrieval report for {gene} ({cfg['accession']})", cfg["asta"])
    for other in GENES:
        if other != gene:
            ensure_reference(
                doc,
                uniprot_ref(other),
                f"UniProtKB entry for {other} ({GENES[other]['accession']})",
                GENES[other]["product"],
            )
    doc["core_functions"] = [core_function(gene)]
    doc["proposed_new_terms"] = []
    if cfg["cluster"] in {"C63", "C71"}:
        question = (
            f"What ATP-binding component partners with the partial {cfg['cluster']} "
            "iron ABC import locus, and is the substrate ferric iron, ferric-chelate, "
            "or another iron complex?"
        )
    else:
        question = (
            "Does the PP_5135-PP_5137 FbpABC-like locus import free ferric iron, "
            "a ferric chelate, or another iron compound in KT2440?"
        )
    doc["suggested_questions"] = [{"question": question}]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Measure iron uptake and growth phenotypes for the matched transporter "
                "deletion mutants under iron limitation, then complement the full locus "
                "to resolve substrate specificity and missing-partner assignments."
            ),
            "experiment_type": "targeted ABC-transporter mutant uptake and growth assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=88))


def binding_annoton(gene: str) -> dict:
    return {
        "id": f"{gene}_ferric_iron_binding_component",
        "label": f"{gene}: ferric/iron substrate-binding component",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {"preferred_term": "ferric iron binding", "term": go_term(FERRIC_IRON_BINDING)},
        "processes": [{"preferred_term": "iron ion transport", "term": go_term(IRON_TRANSPORT)}],
        "locations": [{"preferred_term": "outer membrane-bounded periplasmic space", "term": go_term(PERIPLASM)}],
        "role_description": "Predicted signal-peptide-bearing periplasmic ferric/iron substrate-binding component.",
    }


def permease_annoton(gene: str) -> dict:
    return {
        "id": f"{gene}_iron_abc_permease",
        "label": f"{gene}: iron ABC transporter permease",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {
            "preferred_term": "ABC-type ferric iron transporter activity",
            "term": go_term(ABC_FERRIC_IRON_ACTIVITY),
        },
        "processes": [{"preferred_term": "iron ion transmembrane transport", "term": go_term(IRON_TRANSMEMBRANE)}],
        "locations": [{"preferred_term": "plasma membrane", "term": go_term(PLASMA_MEMBRANE)}],
        "role_description": "Predicted multi-pass membrane permease component of an iron ABC importer.",
    }


def atpase_annoton(gene: str) -> dict:
    return {
        "id": f"{gene}_ferric_iron_abc_atpase",
        "label": f"{gene}: ferric iron ABC ATP-binding subunit",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {
            "preferred_term": "ABC-type ferric iron transporter activity",
            "term": go_term(ABC_FERRIC_IRON_ACTIVITY),
        },
        "processes": [{"preferred_term": "iron ion transmembrane transport", "term": go_term(IRON_TRANSMEMBRANE)}],
        "locations": [{"preferred_term": "plasma membrane", "term": go_term(PLASMA_MEMBRANE)}],
        "role_description": "Predicted ATP-binding energy-coupling subunit of the FbpABC-like iron importer.",
    }


def module_part(order: int, role: str, node_id: str, label: str, description: str, annotons: list[dict]) -> dict:
    return {
        "order": order,
        "role": role,
        "node": {
            "id": node_id,
            "label": label,
            "module_type": "TRANSPORT_STEP",
            "description": description,
            "concepts": [
                {"preferred_term": "iron ion transport", "term": go_term(IRON_TRANSPORT)},
                {"preferred_term": "iron ion transmembrane transport", "term": go_term(IRON_TRANSMEMBRANE)},
                {
                    "preferred_term": "ABC-type ferric iron transporter activity",
                    "term": go_term(ABC_FERRIC_IRON_ACTIVITY),
                },
                {
                    "preferred_term": "ATP-binding cassette (ABC) transporter complex",
                    "term": go_term(ABC_COMPLEX),
                },
            ],
            "annotons": annotons,
        },
    }


def write_module() -> None:
    doc = {
        "id": "MODULE:ferric_iron_abc_import_boundary",
        "title": "Ferric/iron ABC import boundary",
        "description": (
            "Boundary module for ferric/iron ABC import loci from the KEGG ppu02010 "
            "ABC-transporter umbrella map in Pseudomonas putida KT2440. It captures "
            "the complete PP_5135-PP_5137 FbpABC-like importer and two partial "
            "binding/permease candidate loci, PP_4881-PP_4882 and PP_5195-fbpA, "
            "whose ATPase partners remain unresolved."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02010",
                "title": "ABC transporters - Pseudomonas putida KT2440",
                "statement": (
                    "KEGG ppu02010 contributes the PP_4881-PP_4882, PP_5135-PP_5137, "
                    "and PP_5195-fbpA iron ABC transporter candidates. This is a "
                    "substrate-specific partition of the broad ABC transporter map."
                ),
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.tsv",
                "title": "PSEPK ppu02010 ABC-transporter partition batch",
                "statement": (
                    "The ppu02010 partition batch records C63, C67, and C71 as "
                    "metal/cobalamin/siderophore or general ABC clusters with iron "
                    "transporter product names."
                ),
            },
            {
                "source_id": "UniProtKB:Q88CP3",
                "title": "fbpC ferric iron ABC transporter ATP-binding protein",
                "statement": (
                    "UniProt names fbpC as a ferric iron ABC transporter ATP-binding "
                    "protein and records ABC ATPase domains."
                ),
            },
            {
                "source_id": "UniProtKB:Q88CP5",
                "title": "PP_5135 ferric-binding substrate-binding component",
                "statement": (
                    "UniProt records a ferric-binding domain and iron keyword for the "
                    "PP_5135 periplasmic binding component."
                ),
            },
            {
                "source_id": "UniProtKB:Q88DE5",
                "title": "PP_4881 iron ABC periplasmic binding protein",
                "statement": (
                    "UniProt names PP_4881 as an iron ABC transporter periplasmic "
                    "iron-binding protein with a ferric-binding domain."
                ),
            },
            {
                "source_id": "UniProtKB:Q88CI5",
                "title": "fbpA iron(III) ABC periplasmic binding protein",
                "statement": (
                    "UniProt names fbpA as an iron(III) ABC transporter periplasmic "
                    "iron-binding protein with a ferric-binding domain."
                ),
            },
        ],
        "module": {
            "id": "ferric_iron_abc_import_boundary",
            "label": "Ferric/iron ABC import boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                {"preferred_term": "iron ion transport", "term": go_term(IRON_TRANSPORT)},
                {"preferred_term": "iron ion transmembrane transport", "term": go_term(IRON_TRANSMEMBRANE)},
                {"preferred_term": "ferric iron binding", "term": go_term(FERRIC_IRON_BINDING)},
                {
                    "preferred_term": "ABC-type ferric iron transporter activity",
                    "term": go_term(ABC_FERRIC_IRON_ACTIVITY),
                },
                {
                    "preferred_term": "ATP-binding cassette (ABC) transporter complex",
                    "term": go_term(ABC_COMPLEX),
                },
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": "outer membrane-bounded periplasmic space",
                        "term": go_term(PERIPLASM),
                        "description": "Location of predicted ferric/iron substrate-binding components.",
                    },
                    {
                        "preferred_term": "bacterial plasma membrane",
                        "term": go_term(PLASMA_MEMBRANE),
                        "description": "Location of permease and ATPase components of the ABC importers.",
                    },
                ]
            },
            "parts": [
                module_part(
                    1,
                    "partial PP_4881-PP_4882 iron ABC import candidate",
                    "pp4881_pp4882_partial_iron_import",
                    "PP_4881-PP_4882 partial iron ABC import candidate",
                    (
                        "PP_4881 is a ferric/iron substrate-binding component and "
                        "PP_4882 is a matched membrane permease; the ATP-binding "
                        "component is not resolved in this locus."
                    ),
                    [binding_annoton("PP_4881"), permease_annoton("PP_4882")],
                ),
                module_part(
                    2,
                    "complete PP_5135-PP_5137 FbpABC-like iron import",
                    "pp5135_pp5137_fbpabc_like_iron_import",
                    "PP_5135-PP_5137 FbpABC-like ferric/iron ABC import",
                    (
                        "PP_5135, PP_5136, and fbpC form the strongest complete "
                        "FbpABC-like ferric/iron ABC importer candidate in this pass."
                    ),
                    [binding_annoton("PP_5135"), permease_annoton("PP_5136"), atpase_annoton("fbpC")],
                ),
                module_part(
                    3,
                    "partial PP_5195-fbpA iron ABC import candidate",
                    "pp5195_fbpa_partial_iron_import",
                    "PP_5195-fbpA partial iron ABC import candidate",
                    (
                        "PP_5195 is an iron ABC permease candidate and fbpA is a "
                        "ferric/iron substrate-binding component; the ATP-binding "
                        "component is not resolved in this locus."
                    ),
                    [permease_annoton("PP_5195"), binding_annoton("fbpA")],
                ),
            ],
        },
        "notes": (
            "The C67 PP_5135-PP_5137 locus is modeled as complete. C63 and C71 are "
            "kept as partial candidates because the local ATPase partner is not obvious "
            "from the ppu02010 neighborhood. PP_5135 thiamine terms and fbpC "
            "quaternary-ammonium transport are treated as automated spillovers."
        ),
    }
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=88))


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
        print(f"curated {gene}")
    write_module()
    print(f"wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
