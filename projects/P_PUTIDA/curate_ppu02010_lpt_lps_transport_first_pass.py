#!/usr/bin/env python3
"""First-pass curation for the Lpt/MsbA LPS transport boundary."""

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
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
CYTOPLASM = {"id": "GO:0005737", "label": "cytoplasm"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
MEMBRANE = {"id": "GO:0016020", "label": "membrane"}
OUTER_MEMBRANE = {"id": "GO:0009279", "label": "cell outer membrane"}
OUTER_MEMBRANE_ALT = {"id": "GO:0019867", "label": "outer membrane"}
PERIPLASM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}
GENERIC_PERIPLASM = {"id": "GO:0042597", "label": "periplasmic space"}
LPS_BINDING = {"id": "GO:0001530", "label": "lipopolysaccharide binding"}
LPS_TRANSPORT = {"id": "GO:0015920", "label": "lipopolysaccharide transport"}
GLYCOLIPID_TRANSFER = {"id": "GO:0017089", "label": "glycolipid transfer activity"}
GLYCOLIPID_TRANSPORT = {"id": "GO:0046836", "label": "glycolipid transport"}
LPS_TRANSFER = {"id": "GO:0140332", "label": "lipopolysaccharide transfer activity"}
OUTER_MEMBRANE_ASSEMBLY = {
    "id": "GO:0043165",
    "label": "Gram-negative-bacterium-type cell outer membrane assembly",
}
MEMBRANE_ORGANIZATION = {"id": "GO:0061024", "label": "membrane organization"}
TRANS_MEMBRANE_TRANSPORT = {"id": "GO:0055085", "label": "transmembrane transport"}
ABC_COMPLEX = {
    "id": "GO:0043190",
    "label": "ATP-binding cassette (ABC) transporter complex",
}
TRANSPORTER_COMPLEX = {"id": "GO:1990351", "label": "transporter complex"}
ABC_TRANSPORTER = {"id": "GO:0140359", "label": "ABC-type transporter activity"}
ABC_OLIGOPEPTIDE_TRANSPORTER = {"id": "GO:0015421", "label": "ABC-type oligopeptide transporter activity"}
OLIGOPEPTIDE_TRANSPORT = {"id": "GO:0035672", "label": "oligopeptide transmembrane transport"}
ATPASE_COUPLED_LIPID_TRANSPORTER = {
    "id": "GO:0034040",
    "label": "ATPase-coupled lipid transmembrane transporter activity",
}


LPT_BFG = {
    "function": "Part of the ABC transporter complex LptBFG involved in the",
    "translocation": "translocation of lipopolysaccharide (LPS) from the inner membrane to",
    "outer_membrane": "the outer membrane.",
    "subunit_a": "The LptBFG transporter is composed of two ATP-binding proteins",
    "subunit_b": "(LptB) and two transmembrane proteins (LptF and LptG).",
}


GENES = {
    "lptB": {
        "kind": "lptB",
        "accession": "Q88P99",
        "description": (
            "lptB encodes the ATP-binding energy-coupling subunit of the LptBFG "
            "ABC transporter. The LptBFG complex drives lipopolysaccharide "
            "translocation from the inner membrane toward the outer membrane as "
            "part of the Lpt transport and assembly system."
        ),
        "product_text": "Full=Lipopolysaccharide export system ATP-binding protein LptB",
        "asta_text": "Protein Description:** RecName: Full=Lipopolysaccharide export system ATP-binding protein LptB",
        "energy_text": "Probably responsible for energy coupling to the",
        "location_text": "Cell inner membrane",
        "cytoplasmic_side_text": "Cytoplasmic side",
        "domain_text": "InterPro; IPR030921; LPS_export_LptB.",
    },
    "lptA": {
        "kind": "lptA",
        "accession": "Q88P98",
        "description": (
            "lptA encodes the periplasmic LptA bridge component of the LPS transport "
            "and assembly system. It binds and transfers LPS across the periplasm, "
            "linking the inner-membrane LptBFGC machinery to the outer-membrane "
            "LptD/LptE assembly site."
        ),
        "product_text": "Full=Lipopolysaccharide export system protein LptA",
        "asta_text": "Protein Description:** RecName: Full=Lipopolysaccharide export system protein LptA",
        "bridge_text": "May form a bridge between the inner membrane and the",
        "transfer_text": "facilitating LPS transfer across the periplasm.",
        "location_text": "Periplasm",
        "domain_text": "InterPro; IPR014340; LptA.",
    },
    "lptC": {
        "kind": "lptC",
        "accession": "Q88P97",
        "description": (
            "lptC encodes the inner-membrane LptC component of the LPS transport "
            "and assembly system. It helps transfer LPS from the inner-membrane "
            "LptBFG transporter to periplasmic LptA and acts as a docking point "
            "for the periplasmic bridge."
        ),
        "product_text": "Full=Lipopolysaccharide export system protein LptC",
        "asta_text": "Protein Description:** RecName: Full=Lipopolysaccharide export system protein LptC",
        "transfer_text": "Facilitates the transfer of LPS from the inner membrane",
        "lpta_text": "to the periplasmic protein LptA. Could be a docking site for LptA.",
        "subunit_text": "Interacts with LptA and the LptBFG transporter complex.",
        "location_text": "Cell inner membrane",
        "topology_text": "Single-pass membrane protein",
        "domain_text": "InterPro; IPR026265; LptC.",
    },
    "lptD": {
        "kind": "lptD",
        "accession": "A0A140FVZ0",
        "description": (
            "lptD encodes the outer-membrane beta-barrel LptD component of the "
            "LptDE assembly site. Together with LptE, it receives LPS from the "
            "Lpt transenvelope transport system and inserts LPS at the surface of "
            "the outer membrane."
        ),
        "product_text": "Full=LPS-assembly protein LptD",
        "asta_text": "Protein Description:** RecName: Full=LPS-assembly protein LptD",
        "function_text": "Together with LptE, is involved in the assembly of",
        "surface_text": "lipopolysaccharide (LPS) at the surface of the outer membrane.",
        "binding_text": "Interacts with LptE and LptA.",
        "subunit_text": "Interacts with LptE and LptA.",
        "location_text": "Cell outer membrane",
        "domain_text": "InterPro; IPR020889; LipoPS_assembly_LptD.",
    },
    "lptE": {
        "kind": "lptE",
        "accession": "Q88DN0",
        "description": (
            "lptE encodes the outer-membrane lipoprotein partner of LptD in the "
            "LptDE LPS assembly site. It is required for proper LptD assembly, "
            "binds LPS, and may serve as an LPS recognition component at the "
            "outer membrane."
        ),
        "product_text": "Full=LPS-assembly lipoprotein LptE",
        "asta_text": "Protein Description:** RecName: Full=LPS-assembly lipoprotein LptE",
        "function_text": "Together with LptD, is involved in the assembly of",
        "surface_text": "lipopolysaccharide (LPS) at the surface of the outer membrane. Required",
        "binding_text": "recognition site at the outer membrane.",
        "subunit_text": "Interacts with LptD.",
        "location_text": "Cell outer membrane",
        "lipid_anchor_text": "Lipid-anchor",
        "domain_text": "InterPro; IPR007485; LPS_assembly_LptE.",
    },
    "PP_0982": {
        "kind": "lptF",
        "accession": "Q88P71",
        "description": (
            "PP_0982 encodes the LptF permease subunit of the LptBFG ABC "
            "transporter. It is a multi-pass inner-membrane component of the "
            "LPS translocation machinery that moves lipopolysaccharide from the "
            "inner membrane toward the outer membrane."
        ),
        "product_text": "Full=Lipopolysaccharide export system permease protein LptF",
        "asta_text": "Protein Description:** RecName: Full=Lipopolysaccharide export system permease protein LptF",
        "location_text": "Cell inner membrane",
        "topology_text": "Multi-pass membrane protein",
        "domain_text": "InterPro; IPR030922; LptF.",
    },
    "PP_0983": {
        "kind": "lptG",
        "accession": "Q88P70",
        "description": (
            "PP_0983 encodes the LptG permease subunit of the LptBFG ABC "
            "transporter. It partners with LptF and LptB in the inner-membrane "
            "LPS translocation machinery."
        ),
        "product_text": "Full=LPS export ABC transporter permease LptG",
        "asta_text": "Protein Description:** RecName: Full=LPS export ABC transporter permease LptG",
        "location_text": "Cell membrane",
        "topology_text": "Multi-pass membrane protein",
        "domain_text": "InterPro; IPR030923; LptG.",
    },
    "msbA": {
        "kind": "msbA",
        "accession": "Q88D92",
        "description": (
            "msbA encodes a homodimeric inner-membrane ATP-dependent lipid A-core "
            "flippase. The protein uses ATP hydrolysis to translocate lipid "
            "A-core oligosaccharide from the inner to the outer leaflet of the "
            "inner membrane, upstream of Lpt-mediated LPS transport to the outer "
            "membrane."
        ),
        "product_text": "Full=ATP-dependent lipid A-core flippase",
        "asta_text": "Protein Description:** RecName: Full=ATP-dependent lipid A-core flippase",
        "translocates_text": "Translocates lipid A-core from the inner to the outer leaflet of the",
        "leaflet_text": "inner membrane.",
        "reaction_text": "Reaction=ATP + H2O + lipid A-core oligosaccharideSide 1 = ADP +",
        "domain_text": "InterPro; IPR011917; ABC_transpr_lipidA.",
        "location_text": "Cell inner membrane",
        "topology_text": "Multi-pass membrane protein",
    },
}


def lpt_transport_support(gene: str) -> list[dict]:
    return [
        support_uniprot(gene, LPT_BFG["function"]),
        support_uniprot(gene, LPT_BFG["translocation"]),
        support_uniprot(gene, LPT_BFG["outer_membrane"]),
    ]


def lpt_subunit_support(gene: str) -> list[dict]:
    return [
        support_uniprot(gene, LPT_BFG["subunit_a"]),
        support_uniprot(gene, LPT_BFG["subunit_b"]),
    ]


def lptB_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    mapping = {
        "GO:0000166": (
            "Nucleotide binding is true but too broad for the LptB ABC ATP-binding subunit.",
            "MODIFY",
            "The specific ATP-binding and ATP-hydrolysis annotations capture LptB's nucleotide-dependent role more informatively.",
            [ATP_BINDING],
            [support_uniprot(gene, cfg["product_text"]), support_uniprot(gene, cfg["domain_text"])],
        ),
        "GO:0005524": (
            "ATP binding is appropriate for LptB.",
            "ACCEPT",
            "LptB is the ATP-binding component of the LptBFG ABC transporter.",
            None,
            [support_uniprot(gene, cfg["product_text"]), support_uniprot(gene, cfg["domain_text"]), support_asta(gene, cfg["asta_text"])],
        ),
        "GO:0005737": (
            "Cytoplasm is compatible with LptB's peripheral cytoplasmic-side position, but it is not the most informative core localization.",
            "KEEP_AS_NON_CORE",
            "UniProt places LptB at the cytoplasmic side of the cell inner membrane and also maps it to the cytoplasm.",
            None,
            [support_uniprot(gene, cfg["cytoplasmic_side_text"]), support_uniprot(gene, cfg["location_text"])],
        ),
        "GO:0005886": (
            "Plasma membrane localization is appropriate for LptB as an inner-membrane-associated ABC ATPase.",
            "ACCEPT",
            "UniProt places LptB at the cell inner membrane as a peripheral membrane protein.",
            None,
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["cytoplasmic_side_text"])],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is the core mechanistic activity of LptB.",
            "ACCEPT",
            "LptB is the energy-coupling subunit of LptBFG and has ABC ATPase domains.",
            None,
            [support_uniprot(gene, cfg["energy_text"]), support_uniprot(gene, cfg["domain_text"]), support_asta(gene, cfg["asta_text"])],
        ),
        "GO:0043190": (
            "ABC transporter complex membership is appropriate for LptB.",
            "ACCEPT",
            "UniProt describes LptB as part of the LptBFG ABC transporter composed of LptB, LptF, and LptG.",
            None,
            lpt_transport_support(gene) + lpt_subunit_support(gene),
        ),
        "GO:0055085": (
            "Transmembrane transport is correct but too broad for the LptBFG LPS transporter.",
            "MODIFY",
            "The supported substrate/process is lipopolysaccharide transport from the inner membrane toward the outer membrane.",
            [LPS_TRANSPORT],
            lpt_transport_support(gene),
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def lptA_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    mapping = {
        "GO:0001530": (
            "Lipopolysaccharide binding is appropriate for periplasmic LptA.",
            "ACCEPT",
            "LptA is an LPS-transfer bridge component and carries an LptA domain.",
            None,
            [support_uniprot(gene, cfg["transfer_text"]), support_uniprot(gene, cfg["domain_text"])],
        ),
        "GO:0009279": (
            "Cell outer membrane is not the best localization for LptA itself; periplasmic localization is better supported.",
            "MODIFY",
            "UniProt places LptA in the periplasm, where it bridges between inner- and outer-membrane Lpt components.",
            [PERIPLASM],
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["bridge_text"]), support_uniprot(gene, cfg["transfer_text"])],
        ),
        "GO:0015920": (
            "Lipopolysaccharide transport is appropriate for LptA.",
            "ACCEPT",
            "LptA is required for LPS translocation and facilitates LPS transfer across the periplasm.",
            None,
            [support_uniprot(gene, cfg["transfer_text"]), support_uniprot(gene, cfg["bridge_text"]), support_asta(gene, cfg["asta_text"])],
        ),
        "GO:0017089": (
            "Glycolipid transfer activity is appropriate and can be represented more specifically as LPS transfer.",
            "ACCEPT",
            "LPS is a glycolipid, and UniProt describes LptA as facilitating LPS transfer across the periplasm.",
            None,
            [support_uniprot(gene, cfg["transfer_text"]), support_uniprot(gene, cfg["domain_text"])],
        ),
        "GO:0030288": (
            "Outer membrane-bounded periplasmic space localization is appropriate for LptA.",
            "ACCEPT",
            "UniProt places LptA in the periplasm and describes periplasmic LPS transfer.",
            None,
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["transfer_text"])],
        ),
        "GO:0042597": (
            "Periplasmic space localization is correct but less specific than the Gram-negative periplasm term.",
            "MARK_AS_OVER_ANNOTATED",
            "The outer membrane-bounded periplasmic space term is the more informative localization in this Gram-negative bacterium.",
            None,
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["transfer_text"])],
        ),
        "GO:0043165": (
            "Gram-negative outer membrane assembly is appropriate for LptA's LPS delivery role.",
            "ACCEPT",
            "LptA helps transfer LPS to the outer membrane assembly machinery.",
            None,
            [support_uniprot(gene, cfg["bridge_text"]), support_uniprot(gene, cfg["transfer_text"])],
        ),
        "GO:0046836": (
            "Glycolipid transport is correct but less specific than lipopolysaccharide transport for LptA.",
            "MODIFY",
            "The supported glycolipid substrate is LPS.",
            [LPS_TRANSPORT],
            [support_uniprot(gene, cfg["transfer_text"]), support_uniprot(gene, cfg["domain_text"])],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def lptC_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    mapping = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for inner-membrane LptC.",
            "ACCEPT",
            "UniProt places LptC in the cell inner membrane as a single-pass membrane protein.",
            None,
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["topology_text"])],
        ),
        "GO:0015920": (
            "Lipopolysaccharide transport is appropriate for LptC.",
            "ACCEPT",
            "LptC transfers LPS from the inner membrane to LptA as part of the Lpt pathway.",
            None,
            [support_uniprot(gene, cfg["transfer_text"]), support_uniprot(gene, cfg["lpta_text"]), support_asta(gene, cfg["asta_text"])],
        ),
        "GO:0017089": (
            "Glycolipid transfer activity is appropriate for LptC.",
            "ACCEPT",
            "LptC transfers LPS, a glycolipid, from the inner membrane toward LptA.",
            None,
            [support_uniprot(gene, cfg["transfer_text"]), support_uniprot(gene, cfg["lpta_text"])],
        ),
        "GO:0030288": (
            "Periplasmic-space localization is compatible with the periplasmic-facing LptC domain but is not the primary core location.",
            "KEEP_AS_NON_CORE",
            "LptC is an inner-membrane protein that docks the periplasmic LptA bridge.",
            None,
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["lpta_text"])],
        ),
        "GO:0043165": (
            "Gram-negative outer membrane assembly is appropriate for LptC's LPS delivery role.",
            "ACCEPT",
            "LptC participates in transferring LPS toward the outer membrane assembly system.",
            None,
            [support_uniprot(gene, cfg["transfer_text"]), support_uniprot(gene, cfg["subunit_text"])],
        ),
        "GO:0046836": (
            "Glycolipid transport is correct but less specific than lipopolysaccharide transport for LptC.",
            "MODIFY",
            "The supported glycolipid substrate is LPS.",
            [LPS_TRANSPORT],
            [support_uniprot(gene, cfg["transfer_text"]), support_uniprot(gene, cfg["lpta_text"])],
        ),
        "GO:0140332": (
            "Lipopolysaccharide transfer activity is the best supported molecular function for LptC.",
            "ACCEPT",
            "UniProt states that LptC facilitates LPS transfer from the inner membrane to LptA.",
            None,
            [support_uniprot(gene, cfg["transfer_text"]), support_uniprot(gene, cfg["lpta_text"]), support_uniprot(gene, cfg["domain_text"])],
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def lptDE_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    support = [support_uniprot(gene, cfg["function_text"]), support_uniprot(gene, cfg["surface_text"]), support_uniprot(gene, cfg["location_text"])]
    mapping = {
        "GO:0001530": (
            "Lipopolysaccharide binding is appropriate for LptE.",
            "ACCEPT",
            "UniProt states that LptE binds LPS and may act as the LPS recognition site at the outer membrane.",
            None,
            [support_uniprot(gene, cfg["binding_text"]), support_uniprot(gene, cfg["domain_text"])],
        ),
        "GO:0009279": (
            "Cell outer membrane localization is appropriate for the LptDE assembly site.",
            "ACCEPT",
            "UniProt places this Lpt component in the cell outer membrane.",
            None,
            [support_uniprot(gene, cfg["location_text"])],
        ),
        "GO:0015920": (
            "Lipopolysaccharide transport is appropriate for the LptDE assembly component.",
            "ACCEPT",
            "The LptDE outer-membrane assembly site receives and assembles LPS at the surface of the outer membrane.",
            None,
            support + [support_asta(gene, cfg["asta_text"])],
        ),
        "GO:0019867": (
            "Outer membrane localization is appropriate but redundant with the cell outer membrane annotation.",
            "ACCEPT",
            "UniProt places this Lpt component in the cell outer membrane.",
            None,
            [support_uniprot(gene, cfg["location_text"])],
        ),
        "GO:0043165": (
            "Gram-negative outer membrane assembly is appropriate for the LptDE assembly component.",
            "ACCEPT",
            "LptD/LptE assemble LPS at the surface of the outer membrane.",
            None,
            support,
        ),
        "GO:0061024": (
            "Membrane organization is correct but too broad for the LptD LPS assembly role.",
            "MODIFY",
            "Lipopolysaccharide transport and Gram-negative outer membrane assembly better capture the LptD role.",
            [LPS_TRANSPORT, OUTER_MEMBRANE_ASSEMBLY],
            support,
        ),
        "GO:1990351": (
            "Transporter complex membership is appropriate for this Lpt assembly component.",
            "ACCEPT",
            "UniProt describes this protein as a component of the lipopolysaccharide transport and assembly complex.",
            None,
            [support_uniprot(gene, cfg["subunit_text"]), support_uniprot(gene, cfg["domain_text"])],
        ),
    }
    summary, action, reason, proposed, extra = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=extra)


def lptFG_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    mapping = {
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this inner-membrane LptBFG permease.",
            "ACCEPT",
            "UniProt places the protein in the cell inner membrane or cell membrane as a multi-pass membrane protein.",
            None,
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["topology_text"])],
        ),
        "GO:0015920": (
            "Lipopolysaccharide transport is appropriate for this LptBFG permease.",
            "ACCEPT",
            "UniProt describes the LptBFG complex as involved in LPS translocation from the inner membrane to the outer membrane.",
            None,
            lpt_transport_support(gene) + [support_uniprot(gene, cfg["domain_text"]), support_asta(gene, cfg["asta_text"])],
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than plasma membrane for this inner-membrane permease.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also has a plasma-membrane annotation and UniProt places the protein in the cell membrane.",
            None,
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["topology_text"])],
        ),
        "GO:0043190": (
            "ABC transporter complex membership is appropriate for this LptBFG permease.",
            "ACCEPT",
            "UniProt describes LptF/LptG as transmembrane proteins of the LptBFG ABC transporter.",
            None,
            lpt_subunit_support(gene) + lpt_transport_support(gene),
        ),
        "GO:0055085": (
            "Transmembrane transport is correct but too broad for this LptBFG LPS permease.",
            "MODIFY",
            "The supported process is lipopolysaccharide transport.",
            [LPS_TRANSPORT],
            lpt_transport_support(gene),
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def msbA_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    lipid_support = [
        support_uniprot(gene, cfg["product_text"]),
        support_uniprot(gene, cfg["translocates_text"]),
        support_uniprot(gene, cfg["leaflet_text"]),
        support_uniprot(gene, cfg["reaction_text"]),
        support_uniprot(gene, cfg["domain_text"]),
        support_asta(gene, cfg["asta_text"]),
    ]
    mapping = {
        "GO:0005524": (
            "ATP binding is appropriate for MsbA.",
            "ACCEPT",
            "MsbA is an ATP-dependent lipid A-core flippase with ABC transporter domains.",
            None,
            [support_uniprot(gene, cfg["product_text"]), support_uniprot(gene, cfg["domain_text"])],
        ),
        "GO:0005886": (
            "Plasma membrane localization is appropriate for the inner-membrane MsbA flippase.",
            "ACCEPT",
            "UniProt places MsbA in the cell inner membrane as a multi-pass membrane protein.",
            None,
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["topology_text"])],
        ),
        "GO:0015421": (
            "ABC-type oligopeptide transporter activity is an over-propagated PANTHER assignment for MsbA.",
            "REMOVE",
            "The reviewed UniProt/HAMAP record identifies MsbA as a lipid A-core flippase, not an oligopeptide transporter.",
            None,
            lipid_support,
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than plasma membrane for MsbA.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also has a plasma-membrane annotation and UniProt places MsbA in the cell inner membrane.",
            None,
            [support_uniprot(gene, cfg["location_text"]), support_uniprot(gene, cfg["topology_text"])],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is appropriate for MsbA.",
            "ACCEPT",
            "MsbA uses ATP hydrolysis to translocate lipid A-core oligosaccharide.",
            None,
            lipid_support,
        ),
        "GO:0034040": (
            "ATPase-coupled lipid transmembrane transporter activity is the best supported molecular function for MsbA.",
            "ACCEPT",
            "MsbA translocates lipid A-core oligosaccharide across the inner membrane in an ATP-dependent reaction.",
            None,
            lipid_support,
        ),
        "GO:0035672": (
            "Oligopeptide transmembrane transport is an over-propagated inference from the wrong ABC transporter family context.",
            "REMOVE",
            "The target protein is a lipid A-core flippase, and the supported transported substrate is lipid A-core oligosaccharide.",
            None,
            lipid_support,
        ),
        "GO:0055085": (
            "Transmembrane transport is correct but too broad for MsbA.",
            "MODIFY",
            "The supported process is lipid A-core/LPS transport rather than generic transmembrane transport.",
            [LPS_TRANSPORT],
            lipid_support,
        ),
        "GO:0140359": (
            "ABC-type transporter activity is true but less informative than ATPase-coupled lipid transmembrane transporter activity for MsbA.",
            "MODIFY",
            "MsbA is specifically an ATP-dependent lipid A-core flippase.",
            [ATPASE_COUPLED_LIPID_TRANSPORTER],
            lipid_support,
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def add_new_annotations(doc: dict, gene: str, cfg: dict) -> None:
    term_ids = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}
    if gene == "lptB" and LPS_TRANSPORT["id"] not in term_ids:
        doc.setdefault("existing_annotations", []).append(
            new_annotation(
                LPS_TRANSPORT,
                "involved_in",
                gene,
                "Lipopolysaccharide transport is a useful missing process annotation for LptB.",
                "UniProt describes LptBFG as involved in translocation of LPS from the inner membrane to the outer membrane.",
                lpt_transport_support(gene),
            )
        )
    if gene == "lptA" and LPS_TRANSFER["id"] not in term_ids:
        doc.setdefault("existing_annotations", []).append(
            new_annotation(
                LPS_TRANSFER,
                "enables",
                gene,
                "Lipopolysaccharide transfer activity is a useful missing molecular-function annotation for LptA.",
                "UniProt describes LptA as facilitating LPS transfer across the periplasm.",
                [support_uniprot(gene, cfg["transfer_text"]), support_uniprot(gene, cfg["domain_text"])],
            )
        )
    if gene == "msbA" and LPS_TRANSPORT["id"] not in term_ids:
        doc.setdefault("existing_annotations", []).append(
            new_annotation(
                LPS_TRANSPORT,
                "involved_in",
                gene,
                "Lipopolysaccharide transport is a useful missing process annotation for MsbA.",
                "MsbA translocates lipid A-core oligosaccharide across the inner membrane, upstream of Lpt-mediated LPS export.",
                [
                    support_uniprot(gene, cfg["translocates_text"]),
                    support_uniprot(gene, cfg["leaflet_text"]),
                    support_uniprot(gene, cfg["reaction_text"]),
                ],
            )
        )


def set_core_functions(doc: dict, gene: str, cfg: dict) -> None:
    if cfg["kind"] == "lptB":
        core = {
            "description": "ATP-hydrolyzing energy-coupling subunit of the LptBFG LPS transporter.",
            "molecular_function": deepcopy(ATP_HYDROLYSIS),
            "directly_involved_in": [deepcopy(LPS_TRANSPORT)],
            "locations": [deepcopy(PLASMA_MEMBRANE)],
            "in_complex": deepcopy(ABC_COMPLEX),
            "supported_by": [
                support_goa(gene, ATP_HYDROLYSIS["id"], ATP_HYDROLYSIS["label"]),
                support_uniprot(gene, cfg["energy_text"]),
                support_uniprot(gene, LPT_BFG["translocation"]),
                support_uniprot(gene, LPT_BFG["subunit_a"]),
                support_uniprot(gene, LPT_BFG["subunit_b"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    elif cfg["kind"] == "lptA":
        core = {
            "description": "Periplasmic Lpt bridge protein that transfers LPS across the periplasm.",
            "molecular_function": deepcopy(LPS_TRANSFER),
            "directly_involved_in": [deepcopy(LPS_TRANSPORT), deepcopy(OUTER_MEMBRANE_ASSEMBLY)],
            "locations": [deepcopy(PERIPLASM)],
            "supported_by": [
                support_goa(gene, LPS_TRANSPORT["id"], LPS_TRANSPORT["label"]),
                support_uniprot(gene, cfg["bridge_text"]),
                support_uniprot(gene, cfg["transfer_text"]),
                support_uniprot(gene, cfg["location_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    elif cfg["kind"] == "lptC":
        core = {
            "description": "Inner-membrane Lpt component that transfers LPS to periplasmic LptA.",
            "molecular_function": deepcopy(LPS_TRANSFER),
            "directly_involved_in": [deepcopy(LPS_TRANSPORT), deepcopy(OUTER_MEMBRANE_ASSEMBLY)],
            "locations": [deepcopy(PLASMA_MEMBRANE)],
            "supported_by": [
                support_goa(gene, LPS_TRANSFER["id"], LPS_TRANSFER["label"]),
                support_goa(gene, LPS_TRANSPORT["id"], LPS_TRANSPORT["label"]),
                support_uniprot(gene, cfg["transfer_text"]),
                support_uniprot(gene, cfg["lpta_text"]),
                support_uniprot(gene, cfg["location_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    elif cfg["kind"] in {"lptD", "lptE"}:
        core = {
            "description": "Outer-membrane LptDE assembly-site component for LPS insertion at the cell surface.",
            "directly_involved_in": [deepcopy(LPS_TRANSPORT), deepcopy(OUTER_MEMBRANE_ASSEMBLY)],
            "locations": [deepcopy(OUTER_MEMBRANE)],
            "in_complex": deepcopy(TRANSPORTER_COMPLEX),
            "supported_by": [
                support_goa(gene, LPS_TRANSPORT["id"], LPS_TRANSPORT["label"]),
                support_goa(gene, OUTER_MEMBRANE_ASSEMBLY["id"], OUTER_MEMBRANE_ASSEMBLY["label"]),
                support_uniprot(gene, cfg["function_text"]),
                support_uniprot(gene, cfg["surface_text"]),
                support_uniprot(gene, cfg["location_text"]),
                support_uniprot(gene, cfg["subunit_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
        if cfg["kind"] == "lptE":
            core["molecular_function"] = deepcopy(LPS_BINDING)
            core["supported_by"].append(support_goa(gene, LPS_BINDING["id"], LPS_BINDING["label"]))
    elif cfg["kind"] in {"lptF", "lptG"}:
        core = {
            "description": "Multi-pass inner-membrane permease subunit of the LptBFG LPS transporter.",
            "directly_involved_in": [deepcopy(LPS_TRANSPORT)],
            "locations": [deepcopy(PLASMA_MEMBRANE)],
            "in_complex": deepcopy(ABC_COMPLEX),
            "supported_by": [
                support_goa(gene, LPS_TRANSPORT["id"], LPS_TRANSPORT["label"]),
                support_goa(gene, ABC_COMPLEX["id"], ABC_COMPLEX["label"]),
                support_uniprot(gene, LPT_BFG["translocation"]),
                support_uniprot(gene, LPT_BFG["subunit_a"]),
                support_uniprot(gene, LPT_BFG["subunit_b"]),
                support_uniprot(gene, cfg["location_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    else:
        core = {
            "description": "ATP-dependent lipid A-core flippase that moves lipid A-core oligosaccharide across the inner membrane.",
            "molecular_function": deepcopy(ATPASE_COUPLED_LIPID_TRANSPORTER),
            "directly_involved_in": [deepcopy(LPS_TRANSPORT)],
            "locations": [deepcopy(PLASMA_MEMBRANE)],
            "supported_by": [
                support_goa(gene, ATPASE_COUPLED_LIPID_TRANSPORTER["id"], ATPASE_COUPLED_LIPID_TRANSPORTER["label"]),
                support_uniprot(gene, cfg["translocates_text"]),
                support_uniprot(gene, cfg["leaflet_text"]),
                support_uniprot(gene, cfg["reaction_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }

    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "How are the PP_0953-PP_0983 LptBFGAC genes, the distant lptD/lptE "
                "outer-membrane assembly site, and MsbA coordinated in P. putida KT2440 "
                "during LPS export and envelope stress?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Measure LPS surface display, outer-membrane permeability, lipid A-core "
                "accumulation, and growth phenotypes after depletion or perturbation of "
                "LptB, LptF, LptG, LptA, LptC, LptD, LptE, and MsbA."
            ),
            "experiment_type": "targeted Lpt/MsbA LPS transport and envelope-integrity assay",
        }
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
    ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['accession']})", cfg["product_text"])
    ensure_reference(doc, asta_ref(gene), f"Asta retrieval report for {gene} ({cfg['accession']})", cfg["asta_text"])

    for ann in doc.get("existing_annotations", []):
        term_id = ann["term"]["id"]
        label = ann["term"]["label"]
        if cfg["kind"] == "lptB":
            ann["review"] = lptB_review(gene, cfg, term_id, label)
        elif cfg["kind"] == "lptA":
            ann["review"] = lptA_review(gene, cfg, term_id, label)
        elif cfg["kind"] == "lptC":
            ann["review"] = lptC_review(gene, cfg, term_id, label)
        elif cfg["kind"] in {"lptD", "lptE"}:
            ann["review"] = lptDE_review(gene, cfg, term_id, label)
        elif cfg["kind"] in {"lptF", "lptG"}:
            ann["review"] = lptFG_review(gene, cfg, term_id, label)
        else:
            ann["review"] = msbA_review(gene, cfg, term_id, label)

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
        "id": f"{gene}_lpt_lps_transport",
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
        "id": "MODULE:lpt_lps_transport_boundary",
        "title": "Lpt/MsbA lipopolysaccharide transport and outer-membrane assembly boundary",
        "description": (
            "Boundary module for the Pseudomonas putida KT2440 LPS transport system "
            "spanning the ppu02010 ABC-transporter genes lptB, PP_0982/LptF, "
            "PP_0983/LptG, and msbA plus the non-ABC LptA, LptC, LptD, and LptE "
            "bridge/assembly components needed to represent the biological pathway. "
            "The module separates MsbA lipid A-core flipping at the inner membrane "
            "from LptBFGC/A/DE transport of LPS to the outer membrane."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02010",
                "title": "ABC transporters - Pseudomonas putida KT2440",
                "statement": (
                    "KEGG ppu02010 contributes lptB, PP_0982/LptF, PP_0983/LptG, "
                    "and msbA as lipid/LPS ABC-transporter members."
                ),
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.tsv",
                "title": "PSEPK ppu02010 ABC-transporter partition batch",
                "statement": (
                    "The ppu02010 partition batch records LptB, LptF, LptG, and MsbA "
                    "as missing lipid/LPS ABC-transporter sub-batch members before this curation pass."
                ),
            },
            {
                "source_id": "UniProtKB:Q88P99",
                "title": "LptB lipopolysaccharide export ATP-binding protein",
                "statement": "UniProt describes LptB as the LptBFG ATP-binding protein responsible for energy coupling during LPS translocation.",
            },
            {
                "source_id": "UniProtKB:Q88P98",
                "title": "LptA lipopolysaccharide export bridge protein",
                "statement": "UniProt describes LptA as a periplasmic bridge component that facilitates LPS transfer across the periplasm.",
            },
            {
                "source_id": "UniProtKB:Q88P97",
                "title": "LptC lipopolysaccharide export inner-membrane component",
                "statement": "UniProt describes LptC as an inner-membrane Lpt component that transfers LPS to LptA and interacts with LptBFG.",
            },
            {
                "source_id": "UniProtKB:A0A140FVZ0",
                "title": "LptD LPS assembly protein",
                "statement": "UniProt describes LptD as an outer-membrane LptDE component involved in LPS assembly at the cell surface.",
            },
            {
                "source_id": "UniProtKB:Q88DN0",
                "title": "LptE LPS assembly lipoprotein",
                "statement": "UniProt describes LptE as an outer-membrane lipoprotein partner of LptD that binds LPS and supports LptD assembly.",
            },
            {
                "source_id": "UniProtKB:Q88D92",
                "title": "MsbA ATP-dependent lipid A-core flippase",
                "statement": "Reviewed UniProt/HAMAP annotation describes MsbA as an ATP-dependent lipid A-core flippase that moves lipid A-core across the inner membrane.",
            },
        ],
        "module": {
            "id": "lpt_lps_transport_boundary",
            "label": "Lpt/MsbA LPS transport and outer-membrane assembly boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                concept(LPS_TRANSPORT, "Transport of lipopolysaccharide from the inner membrane to the outer membrane."),
                concept(LPS_TRANSFER, "LPS handoff/transfer activity represented by LptA and LptC."),
                concept(ATPASE_COUPLED_LIPID_TRANSPORTER, "ATP-dependent lipid A-core flippase activity of MsbA."),
                concept(OUTER_MEMBRANE_ASSEMBLY, "Outer-membrane assembly context for the Lpt pathway."),
                concept(ABC_COMPLEX, "LptBFG ABC transporter complex at the inner membrane."),
                concept(TRANSPORTER_COMPLEX, "Lpt transport and assembly complex represented by LptD/E."),
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": "bacterial plasma membrane",
                        "term": deepcopy(PLASMA_MEMBRANE),
                        "description": "MsbA and LptBFGC act at the inner membrane.",
                    },
                    {
                        "preferred_term": "outer membrane-bounded periplasmic space",
                        "term": deepcopy(PERIPLASM),
                        "description": "LptA bridges LPS transport across the periplasm.",
                    },
                    {
                        "preferred_term": "cell outer membrane",
                        "term": deepcopy(OUTER_MEMBRANE),
                        "description": "LptD/LptE form the outer-membrane LPS assembly site.",
                    },
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "MsbA lipid A-core flipping at the inner membrane",
                    "node": {
                        "id": "msbA_lipid_a_core_flipping",
                        "label": "MsbA lipid A-core flippase",
                        "module_type": "TRANSPORT_STEP",
                        "description": "MsbA translocates lipid A-core oligosaccharide from the inner to outer leaflet of the inner membrane.",
                        "annotons": [
                            annoton(
                                "msbA",
                                "msbA: ATP-dependent lipid A-core flippase",
                                "Homodimeric ATP-dependent lipid A-core flippase upstream of Lpt-mediated LPS transport.",
                                function=ATPASE_COUPLED_LIPID_TRANSPORTER,
                                processes=[LPS_TRANSPORT],
                                locations=[PLASMA_MEMBRANE],
                            )
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "LptBFGC inner-membrane LPS extraction and handoff",
                    "node": {
                        "id": "lptBFGC_inner_membrane_lps_export",
                        "label": "LptBFGC inner-membrane LPS export",
                        "module_type": "TRANSPORT_STEP",
                        "description": "LptBFG provides ATP-dependent inner-membrane LPS translocation, while LptC links the transporter to periplasmic LptA.",
                        "annotons": [
                            annoton(
                                "lptB",
                                "lptB: LptBFG ATP-binding energy-coupling subunit",
                                "ATP-hydrolyzing subunit of the LptBFG ABC transporter.",
                                function=ATP_HYDROLYSIS,
                                processes=[LPS_TRANSPORT],
                                locations=[PLASMA_MEMBRANE],
                            ),
                            annoton(
                                "PP_0982",
                                "PP_0982/LptF: LptBFG permease",
                                "Multi-pass inner-membrane permease subunit of the LptBFG ABC transporter.",
                                processes=[LPS_TRANSPORT],
                                locations=[PLASMA_MEMBRANE],
                            ),
                            annoton(
                                "PP_0983",
                                "PP_0983/LptG: LptBFG permease",
                                "Multi-pass inner-membrane permease subunit of the LptBFG ABC transporter.",
                                processes=[LPS_TRANSPORT],
                                locations=[PLASMA_MEMBRANE],
                            ),
                            annoton(
                                "lptC",
                                "lptC: LptC LPS handoff component",
                                "Inner-membrane LptC component that transfers LPS to periplasmic LptA.",
                                function=LPS_TRANSFER,
                                processes=[LPS_TRANSPORT, OUTER_MEMBRANE_ASSEMBLY],
                                locations=[PLASMA_MEMBRANE],
                            ),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "Periplasmic bridge and outer-membrane assembly site",
                    "node": {
                        "id": "lptA_lptDE_periplasmic_bridge_outer_membrane_assembly",
                        "label": "LptA bridge and LptDE outer-membrane assembly site",
                        "module_type": "TRANSPORT_STEP",
                        "description": "LptA bridges LPS through the periplasm to the LptD/LptE outer-membrane assembly site.",
                        "annotons": [
                            annoton(
                                "lptA",
                                "lptA: periplasmic LPS transfer bridge",
                                "Periplasmic bridge protein facilitating LPS transfer from the inner membrane toward LptD.",
                                function=LPS_TRANSFER,
                                processes=[LPS_TRANSPORT, OUTER_MEMBRANE_ASSEMBLY],
                                locations=[PERIPLASM],
                            ),
                            annoton(
                                "lptD",
                                "lptD: outer-membrane LPS assembly barrel",
                                "Outer-membrane LptD component of the LptDE LPS assembly site.",
                                processes=[LPS_TRANSPORT, OUTER_MEMBRANE_ASSEMBLY],
                                locations=[OUTER_MEMBRANE],
                            ),
                            annoton(
                                "lptE",
                                "lptE: outer-membrane LPS-binding lipoprotein",
                                "Outer-membrane lipoprotein partner that binds LPS and supports LptD assembly.",
                                function=LPS_BINDING,
                                processes=[LPS_TRANSPORT, OUTER_MEMBRANE_ASSEMBLY],
                                locations=[OUTER_MEMBRANE],
                            ),
                        ],
                    },
                },
            ],
        },
        "notes": (
            "This boundary module complements, rather than replaces, the "
            "lipopolysaccharide_biosynthesis module. It captures envelope transport "
            "and assembly after lipid A/core synthesis, and it keeps the Lpt pathway "
            "separate from the Mla phospholipid retrograde transport module."
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
