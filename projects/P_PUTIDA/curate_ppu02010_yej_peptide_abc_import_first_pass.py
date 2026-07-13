#!/usr/bin/env python3
"""First-pass curation for ppu02010 Yej/DppA-family peptide ABC import candidates."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"

NUCLEOTIDE_BINDING = {"id": "GO:0000166", "label": "nucleotide binding"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
MEMBRANE = {"id": "GO:0016020", "label": "membrane"}
PERIPLASM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}
PERIPLASMIC_SPACE = {"id": "GO:0042597", "label": "periplasmic space"}
PROTEIN_TRANSPORT = {"id": "GO:0015031", "label": "protein transport"}
PEPTIDE_TRANSPORT = {"id": "GO:0015833", "label": "peptide transport"}
MICROCIN_TRANSPORT = {"id": "GO:0042884", "label": "microcin transport"}
DIPEPTIDE_TRANSPORT = {"id": "GO:0042938", "label": "dipeptide transport"}
PEPTIDE_TRANSPORTER_ACTIVITY = {
    "id": "GO:1904680",
    "label": "peptide transmembrane transporter activity",
}
DIPEPTIDE_TRANSPORTER_ACTIVITY = {
    "id": "GO:0071916",
    "label": "dipeptide transmembrane transporter activity",
}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}


GENES: dict[str, dict] = {
    "PP_3076": {
        "accession": "Q88IC3",
        "cluster": "C42",
        "kind": "permease",
        "locus": "partial PP_3076-PP_3078 Yej-like peptide ABC import candidate",
        "description": (
            "PP_3076 encodes a predicted multi-pass inner-membrane permease component of a "
            "PP_3076-PP_3078 Yej-like peptide ABC import candidate. Its MetI-like permease "
            "domain, YejE-like PANTHER subfamily assignment, membrane localization, and "
            "adjacent YejB-like permease plus periplasmic peptide-binding component support "
            "a peptide-transporter role."
        ),
        "product": "Full=ABC transporter permease protein",
        "asta": "Protein Description:** SubName: Full=ABC transporter permease protein",
        "domain": "InterPro; IPR000515; MetI-like.",
        "location": "Cell inner membrane",
        "family": "Belongs to the binding-protein-dependent transport system",
        "panther": "INNER MEMBRANE ABC TRANSPORTER PERMEASE PROTEIN YEJE",
    },
    "PP_3077": {
        "accession": "Q88IC2",
        "cluster": "C42",
        "kind": "permease",
        "locus": "partial PP_3076-PP_3078 Yej-like peptide ABC import candidate",
        "description": (
            "PP_3077 encodes a predicted YejB-like multi-pass inner-membrane permease in "
            "the PP_3076-PP_3078 peptide ABC import candidate. Its oligopeptide transporter "
            "product name, MetI-like permease domain, membrane localization, and neighboring "
            "YejE-like permease and periplasmic binding component support peptide import."
        ),
        "product": "Full=Oligopeptide transport system permease protein YejB",
        "asta": "Protein Description:** RecName: Full=Oligopeptide transport system permease protein YejB",
        "domain": "InterPro; IPR000515; MetI-like.",
        "location": "Cell inner membrane",
        "family": "Belongs to the binding-protein-dependent transport system",
        "panther": "INNER MEMBRANE ABC TRANSPORTER PERMEASE PROTEIN YEJB",
    },
    "PP_3078": {
        "accession": "Q88IC1",
        "cluster": "C42",
        "kind": "binding",
        "locus": "partial PP_3076-PP_3078 Yej-like peptide ABC import candidate",
        "description": (
            "PP_3078 encodes a predicted periplasmic SBP_5-family substrate-binding "
            "component of the PP_3076-PP_3078 Yej-like peptide ABC import candidate. "
            "Its periplasmic localization, peptide/nickel-binding SBP_5 domains, peptide "
            "transport keyword, and adjacent Yej-family permeases support a peptide-binding "
            "role in an ABC importer."
        ),
        "product": "Full=ABC transporter, periplasmic binding protein",
        "asta": "Protein Description:** SubName: Full=ABC transporter, periplasmic binding protein",
        "domain": "InterPro; IPR039424; SBP_5.",
        "other_domain": "InterPro; IPR030678; Peptide/Ni-bd.",
        "location": "SUBCELLULAR LOCATION: Periplasm",
        "keyword": "Peptide transport {ECO:0000256|ARBA:ARBA00022856}",
    },
    "PP_4146": {
        "accession": "Q88FF1",
        "cluster": "C54",
        "kind": "binding",
        "locus": "complete PP_4146-PP_4150 Yej/Dpp-like peptide ABC import candidate",
        "description": (
            "PP_4146 encodes a predicted signal-peptide-bearing periplasmic peptide-binding "
            "component of the PP_4146-PP_4150 Yej/Dpp-like peptide ABC import candidate. "
            "Its SBP_5 domains, peptide-ABC-transporter product name, periplasmic localization, "
            "and neighboring YejA/YejB/YejE/YejF-like components support substrate capture for "
            "peptide uptake."
        ),
        "product": "Full=Peptide ABC transporter, periplamic peptide-binding protein",
        "asta": "Protein Description:** SubName: Full=Peptide ABC transporter, periplamic peptide-binding protein",
        "domain": "InterPro; IPR039424; SBP_5.",
        "other_domain": "InterPro; IPR030678; Peptide/Ni-bd.",
        "location": "SUBCELLULAR LOCATION: Periplasm",
        "signal": "FT   SIGNAL          1..19",
        "keyword": "Peptide transport {ECO:0000256|ARBA:ARBA00022856}",
    },
    "yejA": {
        "accession": "Q88FF0",
        "cluster": "C54",
        "kind": "binding",
        "locus": "complete PP_4146-PP_4150 Yej/Dpp-like peptide ABC import candidate",
        "description": (
            "yejA encodes a predicted signal-peptide-bearing periplasmic peptide-binding "
            "component of the PP_4146-PP_4150 Yej/Dpp-like ABC import candidate. Its "
            "microcin C transporter binding-protein product name, SBP_5 domains, periplasmic "
            "localization, and neighboring permease and ATP-binding components support "
            "peptide substrate capture."
        ),
        "product": "Full=Microcin C transporter-periplasmic binding protein",
        "asta": "Protein Description:** SubName: Full=Microcin C transporter-periplasmic binding protein",
        "domain": "InterPro; IPR039424; SBP_5.",
        "other_domain": "InterPro; IPR030678; Peptide/Ni-bd.",
        "location": "SUBCELLULAR LOCATION: Periplasm",
        "signal": "FT   SIGNAL          1..25",
        "keyword": "Peptide transport {ECO:0000256|ARBA:ARBA00022856}",
    },
    "PP_4148": {
        "accession": "Q88FE9",
        "cluster": "C54",
        "kind": "permease",
        "locus": "complete PP_4146-PP_4150 Yej/Dpp-like peptide ABC import candidate",
        "description": (
            "PP_4148 encodes a predicted YejB-like multi-pass inner-membrane permease of "
            "the PP_4146-PP_4150 Yej/Dpp-like peptide ABC import candidate. Its oligopeptide "
            "transporter product name, MetI-like permease domain, and location between "
            "periplasmic binding components and YejF support peptide-transporter channel function."
        ),
        "product": "Full=Oligopeptide transport system permease protein YejB",
        "asta": "Protein Description:** RecName: Full=Oligopeptide transport system permease protein YejB",
        "domain": "InterPro; IPR000515; MetI-like.",
        "location": "Cell inner membrane",
        "family": "Belongs to the binding-protein-dependent transport system",
        "panther": "INNER MEMBRANE ABC TRANSPORTER PERMEASE PROTEIN YEJB",
    },
    "PP_4149": {
        "accession": "Q88FE8",
        "cluster": "C54",
        "kind": "permease",
        "locus": "complete PP_4146-PP_4150 Yej/Dpp-like peptide ABC import candidate",
        "description": (
            "PP_4149 encodes a predicted YejE-like multi-pass inner-membrane permease of "
            "the PP_4146-PP_4150 Yej/Dpp-like peptide ABC import candidate. Its MetI-like "
            "permease domain, YejE-like PANTHER subfamily assignment, and membrane localization "
            "support a peptide-transporter channel role with PP_4148 and YejF."
        ),
        "product": "Full=Inner membrane ABC transporter permease protein",
        "asta": "Protein Description:** SubName: Full=Inner membrane ABC transporter permease protein",
        "domain": "InterPro; IPR000515; MetI-like.",
        "location": "Cell inner membrane",
        "family": "Belongs to the binding-protein-dependent transport system",
        "panther": "INNER MEMBRANE ABC TRANSPORTER PERMEASE PROTEIN YEJE",
    },
    "yejF": {
        "accession": "Q88FE7",
        "cluster": "C54",
        "kind": "atpase",
        "locus": "complete PP_4146-PP_4150 Yej/Dpp-like peptide ABC import candidate",
        "description": (
            "yejF encodes the predicted ATP-binding energy-coupling component of the "
            "PP_4146-PP_4150 Yej/Dpp-like peptide ABC import candidate. Its ABC ATPase "
            "domains, EC 7.4.2.9 annotation, and UniProt function text for di/tripeptide "
            "uptake support ATP hydrolysis-driven peptide import with the adjacent binding "
            "and permease components."
        ),
        "product": "Full=ABC-type dipeptide transporter",
        "asta": "Protein Description:** RecName: Full=ABC-type dipeptide transporter",
        "function": "Part of the ABC transporter DppABCDF involved in the uptake",
        "domain": "InterPro; IPR003439; ABC_transporter-like_ATP-bd.",
        "other_domain": "InterPro; IPR013563; Oligopep_ABC_C.",
        "location": "Cell inner membrane",
    },
    "dppA-IV": {
        "accession": "Q88C98",
        "cluster": "C72",
        "kind": "dpp_binding",
        "locus": "DppA-family dipeptide-binding singleton",
        "description": (
            "dppA-IV encodes a predicted signal-peptide-bearing periplasmic DppA-family "
            "dipeptide-binding protein. Its periplasmic dipeptide transport product name, "
            "SBP_5 domains, signal peptide, and D,D-dipeptide-binding PANTHER subfamily "
            "support substrate capture for dipeptide ABC uptake."
        ),
        "product": "Full=Periplasmic dipeptide transport protein",
        "asta": "Protein Description:** SubName: Full=Periplasmic dipeptide transport protein",
        "domain": "InterPro; IPR039424; SBP_5.",
        "other_domain": "InterPro; IPR023765; SBP_5_CS.",
        "signal": "FT   SIGNAL          1..21",
        "panther": "D,D-DIPEPTIDE-BINDING PERIPLASMIC PROTEIN DDPA-RELATED",
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
        "review": {"summary": summary, "action": "NEW", "reason": reason, "supported_by": support},
    }


def base_support(gene: str) -> list[dict]:
    cfg = GENES[gene]
    support = [support_uniprot(gene, cfg["product"]), support_asta(gene, cfg["asta"])]
    for key in ("domain", "other_domain", "location", "signal", "family", "panther", "function", "keyword"):
        if key in cfg:
            support.append(support_uniprot(gene, cfg[key]))
    return support


def neighbor_support(gene: str) -> list[dict]:
    cfg = GENES[gene]
    if cfg["cluster"] == "C42":
        return [support_uniprot("PP_3078", GENES["PP_3078"]["product"]), support_uniprot("PP_3077", GENES["PP_3077"]["product"])]
    if cfg["cluster"] == "C54":
        return [support_uniprot("yejF", GENES["yejF"]["function"]), support_uniprot("PP_4148", GENES["PP_4148"]["product"])]
    return []


def curate_existing_annotation(gene: str, annotation: dict) -> dict:
    cfg = GENES[gene]
    term_id = annotation["term"]["id"]
    label = annotation["term"]["label"]
    support = base_support(gene)

    if cfg["kind"] == "permease":
        mapping = {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass bacterial inner-membrane ABC permease.",
                "ACCEPT",
                "UniProt predicts a cell-inner-membrane permease with multiple transmembrane helices.",
                [support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["domain"]), support_asta(gene, cfg["asta"])],
                None,
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation and UniProt cell-inner-membrane placement are the more informative retained locations.",
                [support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["product"])],
                None,
            ),
            "GO:0042884": (
                "Microcin transport is plausible Yej-family context but should not be treated as the core PSEPK transporter function.",
                "KEEP_AS_NON_CORE",
                "The Yej-family permease context supports peptide transport; direct PSEPK evidence for microcin C transport is not available in this first-pass evidence set.",
                support + neighbor_support(gene),
                None,
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this peptide-import permease component.",
                "ACCEPT",
                "The protein is a binding-protein-dependent ABC transporter permease in a local peptide-import candidate locus.",
                support + neighbor_support(gene),
                None,
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to peptide transport for this permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The protein is best represented as contributing to peptide transmembrane transporter activity in an ABC import system.",
                support + neighbor_support(gene),
                None,
            ),
        }
    elif cfg["kind"] == "binding":
        mapping = {
            "GO:0015031": (
                "Protein transport is broad and less informative than peptide transport for this SBP_5-family substrate-binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "The product, keyword, and SBP_5 domains support peptide substrate capture rather than a generic protein-transport role.",
                support,
                None,
            ),
            "GO:0015833": (
                "Peptide transport is appropriate process context for this Yej/DppA-family substrate-binding component.",
                "ACCEPT",
                "The protein is a periplasmic SBP_5-family binding component in a peptide ABC import candidate locus.",
                support + neighbor_support(gene),
                None,
            ),
            "GO:0030288": (
                "Outer membrane-bounded periplasmic space localization is appropriate for this periplasmic substrate-binding protein.",
                "ACCEPT",
                "UniProt places the protein in the periplasm and records SBP_5 substrate-binding domains.",
                [support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["domain"]), support_asta(gene, cfg["asta"])],
                None,
            ),
            "GO:0042597": (
                "Periplasmic space localization is correct but less specific than the Gram-negative outer membrane-bounded periplasmic space term already present.",
                "MARK_AS_OVER_ANNOTATED",
                "GO:0030288 captures the expected bacterial periplasmic compartment more specifically.",
                [support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["domain"])],
                None,
            ),
            "GO:0042884": (
                "Microcin transport is plausible Yej-family context but should remain non-core without direct PSEPK substrate evidence.",
                "KEEP_AS_NON_CORE",
                "Yej-family systems can transport toxic peptides, but the stronger local evidence supports a broader peptide ABC import role.",
                support + neighbor_support(gene),
                None,
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this periplasmic binding component.",
                "ACCEPT",
                "The protein is a predicted substrate-binding component of a local peptide ABC importer.",
                support + neighbor_support(gene),
                None,
            ),
            "GO:0055085": (
                "Transmembrane transport is correct only as transporter-system context and is less precise for a soluble periplasmic binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "The adjacent permeases supply the membrane channel, while this protein contributes substrate capture.",
                support + neighbor_support(gene),
                None,
            ),
            "GO:1904680": (
                "Peptide transmembrane transporter activity is appropriate as a system-level activity for this substrate-binding component.",
                "ACCEPT",
                "The protein is periplasmic and contributes substrate capture to the peptide ABC importer rather than forming the membrane channel itself.",
                support + neighbor_support(gene),
                None,
            ),
        }
    elif cfg["kind"] == "dpp_binding":
        mapping = {
            "GO:0015031": (
                "Protein transport is broad and less informative than dipeptide transport for this DppA-family binding protein.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name and D,D-dipeptide-binding family support dipeptide substrate capture.",
                support,
                None,
            ),
            "GO:0015833": (
                "Peptide transport is broad but acceptable non-core context for this DppA-family binding protein.",
                "KEEP_AS_NON_CORE",
                "The more specific dipeptide transport annotation captures the likely primary process.",
                support,
                None,
            ),
            "GO:0030288": (
                "Outer membrane-bounded periplasmic space localization is appropriate for this signal-peptide-bearing binding protein.",
                "ACCEPT",
                "The protein has a signal peptide and SBP_5-family substrate-binding architecture.",
                [support_uniprot(gene, cfg["signal"]), support_uniprot(gene, cfg["domain"]), support_asta(gene, cfg["asta"])],
                None,
            ),
            "GO:0042938": (
                "Dipeptide transport is appropriate process context for this DppA-family binding component.",
                "ACCEPT",
                "The product name and D,D-dipeptide-binding PANTHER subfamily support a dipeptide transport role.",
                support,
                None,
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this DppA-family substrate-binding component.",
                "ACCEPT",
                "DppA-family binding proteins contribute substrate capture to peptide ABC importers.",
                support,
                None,
            ),
            "GO:0055085": (
                "Transmembrane transport is correct only as transporter-system context and is less precise for a periplasmic binding protein.",
                "MARK_AS_OVER_ANNOTATED",
                "This protein is the substrate-binding component; the membrane channel is supplied by permease subunits.",
                support,
                None,
            ),
            "GO:1904680": (
                "Peptide transmembrane transporter activity is broad and should be narrowed to contribution to dipeptide transporter activity.",
                "MODIFY",
                "The product name and D,D-dipeptide-binding family support a dipeptide ABC transporter binding role.",
                support,
                [go_term(DIPEPTIDE_TRANSPORTER_ACTIVITY)],
            ),
        }
    else:
        mapping = {
            "GO:0000166": (
                "Nucleotide binding is true but less informative than ATP binding and ATP hydrolysis for this ABC ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The ABC ATP-binding domains and EC 7.4.2.9 annotation support ATP-dependent transporter energy coupling.",
                [support_uniprot(gene, cfg["domain"]), support_uniprot(gene, cfg["product"])],
                None,
            ),
            "GO:0005524": (
                "ATP binding is appropriate for this ABC ATP-binding subunit but is not the most informative core activity.",
                "KEEP_AS_NON_CORE",
                "ATP binding supports the ATP hydrolysis cycle captured by GO:0016887.",
                [support_uniprot(gene, cfg["domain"]), support_uniprot(gene, cfg["product"])],
                None,
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this ABC transporter energy-coupling subunit.",
                "ACCEPT",
                "UniProt places the transporter ATP-binding component at the cell inner membrane.",
                [support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["product"])],
                None,
            ),
            "GO:0015833": (
                "Peptide transport is appropriate process context for this YejF/DppF-like ABC ATPase.",
                "ACCEPT",
                "UniProt function text links this ATP-binding subunit to di/tripeptide uptake by an ABC transporter.",
                support + [support_uniprot("yejA", GENES["yejA"]["product"]), support_uniprot("PP_4148", GENES["PP_4148"]["product"])],
                None,
            ),
            "GO:0016887": (
                "ATP hydrolysis activity is appropriate for this ABC ATP-binding energy-coupling subunit.",
                "ACCEPT",
                "The ABC ATP-binding domains and EC 7.4.2.9 annotation support ATP hydrolysis by the transporter ATPase.",
                support,
                None,
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to peptide ABC import for this ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The ATPase energizes transport but does not itself form the membrane channel.",
                support + [support_uniprot("PP_4148", GENES["PP_4148"]["product"])],
                None,
            ),
        }

    summary, action, reason, extra_support, proposed = mapping[term_id]
    annotation["review"] = review(gene, term_id, label, summary, action, reason, extra_support, proposed)
    return annotation


def added_annotations(gene: str) -> list[dict]:
    cfg = GENES[gene]
    support = base_support(gene) + neighbor_support(gene)
    if cfg["kind"] == "permease":
        return [
            new_annotation(
                gene,
                PEPTIDE_TRANSPORTER_ACTIVITY,
                "contributes_to",
                f"{gene} should be represented as contributing the membrane channel to peptide transmembrane transporter activity.",
                "The protein is a MetI-like multi-pass ABC permease in a Yej/Dpp-like peptide import candidate locus.",
                support,
            ),
            new_annotation(
                gene,
                PEPTIDE_TRANSPORT,
                "involved_in",
                f"{gene} should be represented in peptide transport.",
                "The permease product, peptide transport keyword/family context, and local binding-protein components support peptide ABC import.",
                support,
            ),
        ]
    if cfg["kind"] == "binding":
        return []
    if cfg["kind"] == "dpp_binding":
        return [
            new_annotation(
                gene,
                DIPEPTIDE_TRANSPORTER_ACTIVITY,
                "contributes_to",
                f"{gene} should be represented as contributing substrate recognition to dipeptide transmembrane transporter activity.",
                "The protein is a signal-peptide-bearing DppA-family substrate-binding component.",
                support,
            )
        ]
    return [
        new_annotation(
            gene,
            ABC_COMPLEX,
            "part_of",
            "yejF should be represented as part of the Yej/Dpp-like peptide ABC transporter complex.",
            "The protein is an ABC ATP-binding energy-coupling subunit adjacent to Yej-family binding and permease components.",
            support,
        )
    ]


def core_function(gene: str) -> dict:
    cfg = GENES[gene]
    support = base_support(gene) + neighbor_support(gene)
    if cfg["kind"] == "permease":
        return {
            "description": f"Predicted multi-pass membrane permease component of the {cfg['cluster']} Yej/Dpp-like peptide ABC import candidate.",
            "contributes_to_molecular_function": go_term(PEPTIDE_TRANSPORTER_ACTIVITY),
            "directly_involved_in": [go_term(PEPTIDE_TRANSPORT)],
            "locations": [go_term(PLASMA_MEMBRANE)],
            "in_complex": go_term(ABC_COMPLEX),
            "supported_by": support,
        }
    if cfg["kind"] == "binding":
        return {
            "description": f"Predicted periplasmic peptide-binding component of the {cfg['cluster']} Yej/Dpp-like peptide ABC import candidate.",
            "contributes_to_molecular_function": go_term(PEPTIDE_TRANSPORTER_ACTIVITY),
            "directly_involved_in": [go_term(PEPTIDE_TRANSPORT)],
            "locations": [go_term(PERIPLASM)],
            "in_complex": go_term(ABC_COMPLEX),
            "supported_by": support,
        }
    if cfg["kind"] == "dpp_binding":
        return {
            "description": "Predicted periplasmic DppA-family dipeptide-binding component for peptide ABC uptake.",
            "contributes_to_molecular_function": go_term(DIPEPTIDE_TRANSPORTER_ACTIVITY),
            "directly_involved_in": [go_term(DIPEPTIDE_TRANSPORT)],
            "locations": [go_term(PERIPLASM)],
            "in_complex": go_term(ABC_COMPLEX),
            "supported_by": support,
        }
    return {
        "description": "Predicted ATP-binding energy-coupling component of the PP_4146-PP_4150 Yej/Dpp-like peptide ABC importer.",
        "molecular_function": go_term(ATP_HYDROLYSIS),
        "directly_involved_in": [go_term(PEPTIDE_TRANSPORT)],
        "locations": [go_term(PLASMA_MEMBRANE)],
        "in_complex": go_term(ABC_COMPLEX),
        "supported_by": support,
    }


def suggested_question(gene: str) -> str:
    cfg = GENES[gene]
    if cfg["cluster"] == "C42":
        return "Which ATP-binding component partners with the PP_3076-PP_3078 Yej-like peptide ABC import candidate, and what peptide substrate range does it recognize?"
    if cfg["cluster"] == "C54":
        return "Does the PP_4146-PP_4150 Yej/Dpp-like locus primarily import nutritional peptides, toxic peptides such as microcin/phaseolotoxin-like substrates, or both?"
    return "Which transporter complex uses dppA-IV as a periplasmic dipeptide-binding component in KT2440?"


def suggested_experiment(gene: str) -> dict:
    cfg = GENES[gene]
    if cfg["cluster"] == "C54":
        return {
            "description": "Measure uptake and growth phenotypes for PP_4146/yejA/PP_4148/PP_4149/yejF mutants with representative dipeptides, tripeptides, and toxic peptide analogs.",
            "experiment_type": "targeted Yej/Dpp-like peptide transporter mutant uptake/growth assay",
        }
    if cfg["cluster"] == "C42":
        return {
            "description": "Identify the ATPase partner for PP_3076-PP_3078 and test peptide uptake phenotypes in permease and binding-protein mutants.",
            "experiment_type": "targeted peptide transporter partner and uptake assay",
        }
    return {
        "description": "Measure purified dppA-IV ligand binding and mutant uptake phenotypes across representative D- and L-dipeptides.",
        "experiment_type": "DppA-family binding-protein ligand specificity assay",
    }


def curate_gene(gene: str) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
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
    doc["suggested_questions"] = [{"question": suggested_question(gene)}]
    doc["suggested_experiments"] = [suggested_experiment(gene)]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {gene}")


def binding_annoton(gene: str, term: dict = PEPTIDE_TRANSPORTER_ACTIVITY) -> dict:
    return {
        "id": f"{gene}_peptide_binding_component",
        "label": f"{gene}: peptide substrate-binding component",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {"preferred_term": term["label"], "term": go_term(term)},
        "processes": [{"preferred_term": PEPTIDE_TRANSPORT["label"], "term": go_term(PEPTIDE_TRANSPORT)}],
        "locations": [{"preferred_term": PERIPLASM["label"], "term": go_term(PERIPLASM)}],
        "role_description": "Predicted periplasmic SBP_5-family peptide substrate-binding component.",
    }


def dpp_binding_annoton(gene: str) -> dict:
    return {
        "id": f"{gene.replace('-', '_')}_dipeptide_binding_component",
        "label": f"{gene}: DppA-family dipeptide-binding component",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {"preferred_term": DIPEPTIDE_TRANSPORTER_ACTIVITY["label"], "term": go_term(DIPEPTIDE_TRANSPORTER_ACTIVITY)},
        "processes": [{"preferred_term": DIPEPTIDE_TRANSPORT["label"], "term": go_term(DIPEPTIDE_TRANSPORT)}],
        "locations": [{"preferred_term": PERIPLASM["label"], "term": go_term(PERIPLASM)}],
        "role_description": "Predicted periplasmic DppA-family dipeptide substrate-binding component.",
    }


def permease_annoton(gene: str) -> dict:
    return {
        "id": f"{gene}_peptide_permease",
        "label": f"{gene}: peptide ABC permease",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {"preferred_term": PEPTIDE_TRANSPORTER_ACTIVITY["label"], "term": go_term(PEPTIDE_TRANSPORTER_ACTIVITY)},
        "processes": [{"preferred_term": PEPTIDE_TRANSPORT["label"], "term": go_term(PEPTIDE_TRANSPORT)}],
        "locations": [{"preferred_term": PLASMA_MEMBRANE["label"], "term": go_term(PLASMA_MEMBRANE)}],
        "role_description": "Predicted multi-pass membrane permease component of a peptide ABC importer.",
    }


def atpase_annoton(gene: str) -> dict:
    return {
        "id": f"{gene}_peptide_abc_atpase",
        "label": f"{gene}: peptide ABC ATP-binding subunit",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {"preferred_term": ATP_HYDROLYSIS["label"], "term": go_term(ATP_HYDROLYSIS)},
        "processes": [{"preferred_term": PEPTIDE_TRANSPORT["label"], "term": go_term(PEPTIDE_TRANSPORT)}],
        "locations": [{"preferred_term": PLASMA_MEMBRANE["label"], "term": go_term(PLASMA_MEMBRANE)}],
        "role_description": "Predicted ATP-binding energy-coupling subunit of a Yej/Dpp-like peptide ABC importer.",
    }


def write_module() -> None:
    module = {
        "id": "MODULE:yej_dpp_like_peptide_abc_import_boundary",
        "title": "Yej/Dpp-like peptide ABC import boundary",
        "description": (
            "Boundary module for Yej/DppA-family peptide ABC import candidates from the KEGG "
            "ppu02010 ABC-transporter umbrella map in Pseudomonas putida KT2440. It captures "
            "the complete PP_4146-PP_4150 Yej/Dpp-like importer candidate, the partial "
            "PP_3076-PP_3078 Yej-like candidate, and the dppA-IV DppA-family singleton."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02010",
                "title": "ABC transporters - Pseudomonas putida KT2440",
                "statement": (
                    "KEGG ppu02010 contributes the PP_3076-PP_3078, PP_4146-PP_4150, and "
                    "dppA-IV peptide ABC transporter candidates."
                ),
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.tsv",
                "title": "PSEPK ppu02010 ABC-transporter partition batch",
                "statement": (
                    "The ppu02010 partition batch records C42, C54, and C72 as remaining "
                    "Yej/DppA-family peptide or microcin-associated ABC-transporter candidates."
                ),
            },
            {
                "source_id": "UniProtKB:Q88FE7",
                "title": "yejF ABC-type dipeptide transporter ATPase",
                "statement": "UniProt describes yejF as an ABC-type dipeptide transporter with EC 7.4.2.9 and di/tripeptide uptake function text.",
            },
            {
                "source_id": "UniProtKB:Q88FF0",
                "title": "yejA microcin C transporter periplasmic binding protein",
                "statement": "UniProt names yejA as a microcin C transporter periplasmic binding protein with SBP_5 domains.",
            },
            {
                "source_id": "UniProtKB:Q88C98",
                "title": "dppA-IV periplasmic dipeptide transport protein",
                "statement": "UniProt names dppA-IV as a periplasmic dipeptide transport protein with DppA-family SBP_5 features.",
            },
        ],
        "module": {
            "id": "yej_dpp_like_peptide_abc_import_boundary",
            "label": "Yej/Dpp-like peptide ABC import boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                {"preferred_term": PEPTIDE_TRANSPORT["label"], "term": go_term(PEPTIDE_TRANSPORT)},
                {"preferred_term": DIPEPTIDE_TRANSPORT["label"], "term": go_term(DIPEPTIDE_TRANSPORT)},
                {"preferred_term": MICROCIN_TRANSPORT["label"], "term": go_term(MICROCIN_TRANSPORT)},
                {"preferred_term": PEPTIDE_TRANSPORTER_ACTIVITY["label"], "term": go_term(PEPTIDE_TRANSPORTER_ACTIVITY)},
                {"preferred_term": DIPEPTIDE_TRANSPORTER_ACTIVITY["label"], "term": go_term(DIPEPTIDE_TRANSPORTER_ACTIVITY)},
                {"preferred_term": ABC_COMPLEX["label"], "term": go_term(ABC_COMPLEX)},
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": PERIPLASM["label"],
                        "term": go_term(PERIPLASM),
                        "description": "Location of predicted peptide substrate-binding components.",
                    },
                    {
                        "preferred_term": "bacterial plasma membrane",
                        "term": go_term(PLASMA_MEMBRANE),
                        "description": "Location of Yej/Dpp-like permease and ATPase components.",
                    },
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "partial PP_3076-PP_3078 Yej-like peptide ABC import candidate",
                    "node": {
                        "id": "pp3076_pp3078_yej_like_peptide_import",
                        "label": "PP_3076-PP_3078 Yej-like peptide ABC import candidate",
                        "module_type": "TRANSPORT_STEP",
                        "description": "PP_3076 and PP_3077 are predicted permeases and PP_3078 is the matched periplasmic peptide-binding component; the ATP-binding partner is not resolved in this locus.",
                        "concepts": [
                            {"preferred_term": PEPTIDE_TRANSPORT["label"], "term": go_term(PEPTIDE_TRANSPORT)},
                            {"preferred_term": MICROCIN_TRANSPORT["label"], "term": go_term(MICROCIN_TRANSPORT)},
                            {"preferred_term": PEPTIDE_TRANSPORTER_ACTIVITY["label"], "term": go_term(PEPTIDE_TRANSPORTER_ACTIVITY)},
                            {"preferred_term": ABC_COMPLEX["label"], "term": go_term(ABC_COMPLEX)},
                        ],
                        "annotons": [permease_annoton("PP_3076"), permease_annoton("PP_3077"), binding_annoton("PP_3078")],
                    },
                },
                {
                    "order": 2,
                    "role": "complete PP_4146-PP_4150 Yej/Dpp-like peptide ABC import candidate",
                    "node": {
                        "id": "pp4146_pp4150_yej_dpp_like_peptide_import",
                        "label": "PP_4146-PP_4150 Yej/Dpp-like peptide ABC import candidate",
                        "module_type": "TRANSPORT_STEP",
                        "description": "PP_4146 and yejA are predicted periplasmic peptide-binding components, PP_4148 and PP_4149 are permeases, and yejF is the ATP-binding component.",
                        "concepts": [
                            {"preferred_term": PEPTIDE_TRANSPORT["label"], "term": go_term(PEPTIDE_TRANSPORT)},
                            {"preferred_term": DIPEPTIDE_TRANSPORT["label"], "term": go_term(DIPEPTIDE_TRANSPORT)},
                            {"preferred_term": MICROCIN_TRANSPORT["label"], "term": go_term(MICROCIN_TRANSPORT)},
                            {"preferred_term": PEPTIDE_TRANSPORTER_ACTIVITY["label"], "term": go_term(PEPTIDE_TRANSPORTER_ACTIVITY)},
                            {"preferred_term": ABC_COMPLEX["label"], "term": go_term(ABC_COMPLEX)},
                        ],
                        "annotons": [
                            binding_annoton("PP_4146"),
                            binding_annoton("yejA"),
                            permease_annoton("PP_4148"),
                            permease_annoton("PP_4149"),
                            atpase_annoton("yejF"),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "dppA-IV DppA-family dipeptide-binding singleton",
                    "node": {
                        "id": "dppa_iv_dipeptide_binding_singleton",
                        "label": "dppA-IV DppA-family dipeptide-binding singleton",
                        "module_type": "TRANSPORT_STEP",
                        "description": "dppA-IV is a predicted periplasmic DppA-family dipeptide-binding component whose partner permease/ATPase assignment remains unresolved.",
                        "concepts": [
                            {"preferred_term": DIPEPTIDE_TRANSPORT["label"], "term": go_term(DIPEPTIDE_TRANSPORT)},
                            {"preferred_term": DIPEPTIDE_TRANSPORTER_ACTIVITY["label"], "term": go_term(DIPEPTIDE_TRANSPORTER_ACTIVITY)},
                            {"preferred_term": ABC_COMPLEX["label"], "term": go_term(ABC_COMPLEX)},
                        ],
                        "annotons": [dpp_binding_annoton("dppA-IV")],
                    },
                },
            ],
        },
        "notes": (
            "Microcin transport annotations are retained as non-core Yej-family context because direct "
            "PSEPK substrate evidence is not available. PP_3076-PP_3078 and dppA-IV remain partial "
            "or singleton candidates pending partner assignment."
        ),
    }
    path = Path("modules/yej_dpp_like_peptide_abc_import_boundary.yaml")
    path.write_text(yaml.safe_dump(module, sort_keys=False, width=1000))
    print(f"wrote {path}")


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
    write_module()


if __name__ == "__main__":
    main()
