#!/usr/bin/env python3
"""First-pass curation for the final ppu02010 gap genes."""

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


def ensure_reference(
    doc: dict, ref_id: str, title: str, statement: str | None = None, supporting_text: str | None = None
) -> None:
    refs = doc.setdefault("references", [])
    for ref in refs:
        if ref.get("id") == ref_id:
            if supporting_text:
                findings = ref.setdefault("findings", [])
                if not any(f.get("supporting_text") == supporting_text for f in findings):
                    finding = {"supporting_text": supporting_text}
                    if statement:
                        finding["statement"] = statement
                    findings.append(finding)
            return
    ref = {"id": ref_id, "title": title, "findings": []}
    if supporting_text:
        finding = {"supporting_text": supporting_text}
        if statement:
            finding["statement"] = statement
        ref["findings"].append(finding)
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
    data = {"summary": summary, "action": action, "reason": reason, "supported_by": supported_by}
    if proposed:
        data["proposed_replacement_terms"] = deepcopy(proposed)
    return data


NUCLEOTIDE_BINDING = {"id": "GO:0000166", "label": "nucleotide binding"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
IRON_TRANSPORT = {"id": "GO:0006826", "label": "iron ion transport"}
FERRIC_IRON_TRANSPORTER = {"id": "GO:0015408", "label": "ABC-type ferric iron transporter activity"}
QUATERNARY_AMMONIUM_TRANSPORT = {"id": "GO:0015697", "label": "quaternary ammonium group transport"}
MEMBRANE = {"id": "GO:0016020", "label": "membrane"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
TRANSMEMBRANE_TRANSPORTER = {"id": "GO:0022857", "label": "transmembrane transporter activity"}
CELL_ENVELOPE = {"id": "GO:0030313", "label": "cell envelope"}
LIPID_TRANSPORTER = {"id": "GO:0034040", "label": "ATPase-coupled lipid transmembrane transporter activity"}
IRON_TRANSMEMBRANE_TRANSPORT = {"id": "GO:0034755", "label": "iron ion transmembrane transport"}
OLIGOPEPTIDE_TRANSPORT = {"id": "GO:0035672", "label": "oligopeptide transmembrane transport"}
COBALAMIN_BINDING = {"id": "GO:0031419", "label": "cobalamin binding"}
PHOSPHATE_TRANSPORT = {"id": "GO:0035435", "label": "phosphate ion transmembrane transport"}
ATPASE_COUPLED_TRANSPORTER = {
    "id": "GO:0042626",
    "label": "ATPase-coupled transmembrane transporter activity",
}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PHOSPHATE_BINDING = {"id": "GO:0042301", "label": "phosphate ion binding"}
PERIPLASM = {"id": "GO:0042597", "label": "periplasmic space"}
TRANSMEMBRANE_TRANSPORT = {"id": "GO:0055085", "label": "transmembrane transport"}
MONOATOMIC_CATION_TRANSPORT = {"id": "GO:0098655", "label": "monoatomic cation transmembrane transport"}
ABC_TYPE_TRANSPORTER = {"id": "GO:0140359", "label": "ABC-type transporter activity"}


GENES: dict[str, dict] = {
    "PP_0524": {
        "accession": "Q88QG9",
        "status": "COMPLETE",
        "description": (
            "PP_0524 encodes a predicted signal-peptide-bearing periplasmic cobalamin-binding protein in the "
            "PP_0524-PP_0525 vitamin B12 uptake neighborhood. UniProt names the protein HutB and records an "
            "ABC-transporter solute-binding fold with a vitamin B12-binding signature. The lone GOA iron-response "
            "annotation is treated as a family-transfer spillover rather than the gene's core role."
        ),
        "product": "Full=Periplasmic cobalamin-binding protein HutB",
        "domain": "InterPro; IPR054828; Vit_B12_bind_prot.",
        "fold": "InterPro; IPR002491; ABC_transptr_periplasmic_BD.",
        "pfam": "DR   Pfam; PF01497; Peripla_BP_2; 1.",
        "asta_product": "Full=Periplasmic cobalamin-binding protein HutB",
        "rules": {
            "GO:0071281": (
                "cellular response to iron ion",
                "REMOVE",
                "Cellular response to iron ion is not supported for this cobalamin-binding protein.",
                (
                    "The product name and vitamin B12-binding domain support cobalamin-binding/transport context, "
                    "not an iron-response role; this looks like over-propagated TreeGrafter/PANTHER context."
                ),
                [],
            )
        },
        "core_functions": [
            {
                "description": "Periplasmic cobalamin-binding protein, likely acting in vitamin B12 uptake context.",
                "molecular_function": COBALAMIN_BINDING,
                "directly_involved_in": [{"id": "GO:0015889", "label": "cobalamin transport"}],
                "locations": [PERIPLASM],
                "supported_by": [
                    support_uniprot("PP_0524", "Full=Periplasmic cobalamin-binding protein HutB"),
                    support_uniprot("PP_0524", "InterPro; IPR054828; Vit_B12_bind_prot."),
                    support_uniprot("PP_0524", "InterPro; IPR002491; ABC_transptr_periplasmic_BD."),
                    support_asta("PP_0524", "Full=Periplasmic cobalamin-binding protein HutB"),
                ],
            }
        ],
        "questions": [
            "Does PP_0524 pair functionally with the adjacent PP_0525 TonB-dependent B12-family receptor in KT2440 cobalamin uptake?",
            "What is the exact corrinoid substrate range for PP_0524?",
        ],
        "experiment": (
            "Test PP_0524 and PP_0525 mutants for vitamin B12/cobalamin uptake and growth rescue under cobalamin-dependent "
            "conditions, with purified PP_0524 ligand-binding assays for cobalamin and related corrinoids."
        ),
    },
    "PP_1078": {
        "accession": "Q88NX5",
        "status": "DRAFT",
        "description": (
            "PP_1078 encodes an unresolved ABC transporter ATP-binding protein with ABC ATPase, TOBE/OB-fold, and "
            "small-molecule-importer family signatures. Existing iron, ferric-iron, quaternary-ammonium, and generic "
            "transmembrane-transporter annotations are not supported by local transporter context; the defensible "
            "first-pass role is an ATP-hydrolyzing ABC energy-coupling component of unknown substrate specificity."
        ),
        "product": "Full=ABC transporter, ATP-binding protein",
        "abc": "InterPro; IPR003439; ABC_transporter-like_ATP-bd.",
        "tobe": "InterPro; IPR013611; Transp-assoc_OB_typ2.",
        "asta_product": "Full=ABC transporter, ATP-binding protein",
        "rules": {},
        "core_functions": [
            {
                "description": "Unresolved ABC transporter ATP-binding energy-coupling component.",
                "molecular_function": ATP_HYDROLYSIS,
                "in_complex": ABC_COMPLEX,
                "supported_by": [
                    support_goa("PP_1078", "GO:0016887", "ATP hydrolysis activity"),
                    support_uniprot("PP_1078", "Full=ABC transporter, ATP-binding protein"),
                    support_uniprot("PP_1078", "InterPro; IPR003439; ABC_transporter-like_ATP-bd."),
                    support_asta("PP_1078", "Full=ABC transporter, ATP-binding protein"),
                ],
            }
        ],
        "questions": [
            "What permease and substrate-binding components, if any, partner with PP_1078?",
            "Are the ferric-iron and quaternary-ammonium annotations family-transfer artifacts or clues to a missing transporter context?",
        ],
        "experiment": "Map PP_1078 interaction partners and test uptake phenotypes across iron, polyamine, and quaternary-amine substrates.",
    },
    "PP_2595": {
        "accession": "Q88JQ4",
        "status": "DRAFT",
        "description": (
            "PP_2595 encodes a fused cell-membrane ABCB/type-1-exporter-like permease/ATPase. It sits immediately "
            "downstream of a ferric-siderophore ABC uptake locus, but its own substrate is unresolved. ATP binding, "
            "ATP hydrolysis, plasma-membrane localization, and generic ABC-type transmembrane transporter activity are "
            "supportable; the lipid-transporter call is treated as automated family spillover."
        ),
        "product": "Full=ABC transporter, permease/ATP-binding protein",
        "type1": "InterPro; IPR039421; Type_1_exporter.",
        "abc_tm": "InterPro; IPR011527; ABC1_TM_dom.",
        "abc": "InterPro; IPR003439; ABC_transporter-like_ATP-bd.",
        "location": "Cell membrane",
        "asta_product": "Full=ABC transporter, permease/ATP-binding protein",
        "rules": {},
        "core_functions": [],
        "questions": [
            "Do PP_2595 and PP_2596 form a redundant pair, a heteromeric exporter, or two independent ABCB-like exporters?",
            "Is either transporter linked to the adjacent ferric-siderophore uptake locus or to an unrelated envelope substrate?",
        ],
        "experiment": "Construct PP_2595/PP_2596 single and double mutants and assay siderophore sensitivity, envelope stress, and export phenotypes.",
    },
    "PP_2596": {
        "accession": "Q88JQ3",
        "status": "DRAFT",
        "description": (
            "PP_2596 encodes a fused cell-membrane ABCB/type-1-exporter-like permease/ATPase adjacent to PP_2595. "
            "The protein has ABC1 transmembrane, ABC ATP-binding, and Type_1_exporter signatures, but current evidence "
            "does not identify its substrate. The first-pass core role is generic ABC-type ATP-dependent transmembrane "
            "transport."
        ),
        "product": "Full=ABC transporter, permease/ATP-binding protein",
        "type1": "InterPro; IPR039421; Type_1_exporter.",
        "abc_tm": "InterPro; IPR011527; ABC1_TM_dom.",
        "abc": "InterPro; IPR003439; ABC_transporter-like_ATP-bd.",
        "location": "Cell membrane",
        "asta_product": "Full=ABC transporter, permease/ATP-binding protein",
        "rules": {},
        "core_functions": [],
        "questions": [
            "Do PP_2595 and PP_2596 form a redundant pair, a heteromeric exporter, or two independent ABCB-like exporters?",
            "Does PP_2596 export an envelope lipid, peptide, siderophore-related compound, or another substrate?",
        ],
        "experiment": "Construct PP_2595/PP_2596 single and double mutants and assay substrate-export and envelope-stress phenotypes.",
    },
    "PP_2628": {
        "accession": "Q88JM1",
        "status": "DRAFT",
        "description": (
            "PP_2628 encodes an unresolved fused cell-membrane ABCB/type-1-exporter-like transporter adjacent to a "
            "type VI secretion/cell-envelope locus and upstream of cellulose-biosynthesis genes. UniProt and InterPro "
            "support an ABC1 transmembrane plus ABC ATP-binding architecture, but the oligopeptide transporter annotation "
            "is not supported by direct substrate evidence."
        ),
        "product": "Full=Uncharacterized ABC transporter ATP-binding protein HI_1051",
        "type1": "InterPro; IPR039421; Type_1_exporter.",
        "abc_tm": "InterPro; IPR011527; ABC1_TM_dom.",
        "abc": "InterPro; IPR003439; ABC_transporter-like_ATP-bd.",
        "location": "Cell membrane",
        "asta_product": "Full=Uncharacterized ABC transporter ATP-binding protein HI_1051",
        "rules": {},
        "core_functions": [],
        "questions": [
            "Is PP_2628 functionally linked to the neighboring type VI secretion or cellulose/envelope loci?",
            "What substrate, if any, is transported by the PP_2628 ABCB-like protein?",
        ],
        "experiment": "Test PP_2628 mutants for type VI secretion, biofilm/cellulose, envelope-stress, and generic export phenotypes.",
    },
    "PP_3818": {
        "accession": "Q88GA6",
        "status": "COMPLETE",
        "description": (
            "PP_3818 encodes a predicted signal-peptide-bearing PstS-family phosphate-binding protein. The protein has "
            "PBP/phosphate-ABC-transporter signatures and is near a separate polyamine ABC importer, but current evidence "
            "does not identify cognate phosphate permease or ATPase partners. It is best treated as a phosphate-binding "
            "singleton related to the phosphate-import boundary."
        ),
        "product": "Full=Periplamic phosphate-binding protein",
        "phosphate_domain": "InterPro; IPR050811; Phosphate_ABC_transporter.",
        "pather": "PANTHER; PTHR30570; PERIPLASMIC PHOSPHATE BINDING COMPONENT OF PHOSPHATE ABC TRANSPORTER; 1.",
        "signal": "Signal",
        "asta_product": "Full=Periplamic phosphate-binding protein",
        "rules": {
            "GO:0016020": (
                "membrane",
                "KEEP_AS_NON_CORE",
                "Membrane localization is broad context for this signal-peptide/OmpA-like phosphate-binding protein.",
                (
                    "The product and phosphate-ABC-transporter family support a periplasmic or envelope-associated "
                    "solute-binding role rather than a membrane transport channel."
                ),
                [],
            )
        },
        "core_functions": [
            {
                "description": "PstS-family phosphate-binding solute-binding protein with unresolved transporter partners.",
                "molecular_function": PHOSPHATE_BINDING,
                "directly_involved_in": [PHOSPHATE_TRANSPORT],
                "locations": [PERIPLASM],
                "supported_by": [
                    support_uniprot("PP_3818", "Full=Periplamic phosphate-binding protein"),
                    support_uniprot("PP_3818", "InterPro; IPR050811; Phosphate_ABC_transporter."),
                    support_uniprot(
                        "PP_3818",
                        "PANTHER; PTHR30570; PERIPLASMIC PHOSPHATE BINDING COMPONENT OF PHOSPHATE ABC TRANSPORTER",
                    ),
                    support_asta("PP_3818", "Full=Periplamic phosphate-binding protein"),
                ],
            }
        ],
        "questions": [
            "Which transporter partners, if any, pair with the PP_3818 phosphate-binding protein?",
            "Is PP_3818 a functional phosphate-binding component or a paralog retained for another envelope ligand?",
        ],
        "experiment": "Test PP_3818 ligand binding to phosphate and monitor phosphate-limitation phenotypes in PP_3818 and pst-system mutants.",
    },
    "PP_4542": {
        "accession": "Q88EC4",
        "status": "DRAFT",
        "description": (
            "PP_4542 encodes an unresolved fused cell-membrane ABCB/type-1-exporter-like permease/ATPase. The protein "
            "has ABC1 transmembrane, ABC ATP-binding, and Type_1_exporter signatures, but no local or literature evidence "
            "identifies an oligopeptide substrate. The first-pass core role is generic ABC-type ATP-dependent "
            "transmembrane transport."
        ),
        "product": "Full=ABC transporter, ATP-binding protein/permease protein",
        "type1": "InterPro; IPR039421; Type_1_exporter.",
        "abc_tm": "InterPro; IPR011527; ABC1_TM_dom.",
        "abc": "InterPro; IPR003439; ABC_transporter-like_ATP-bd.",
        "location": "Cell membrane",
        "asta_product": "Full=ABC transporter, ATP-binding protein/permease protein",
        "rules": {},
        "core_functions": [],
        "questions": [
            "What substrate is exported or transported by PP_4542?",
            "Are the oligopeptide transport annotations over-propagated from MDL-family ABCB proteins?",
        ],
        "experiment": "Screen PP_4542 mutants for peptide, envelope-stress, and xenobiotic/export phenotypes.",
    },
    "PP_5157": {
        "accession": "Q88CM3",
        "status": "DRAFT",
        "description": (
            "PP_5157 encodes a short signal-peptide-bearing bacterial solute-binding protein family 3 member located in "
            "the cell envelope. It is mapped to the broad ppu02010/ppu02040 region, but current evidence does not support "
            "a specific substrate or a direct flagellar-assembly role."
        ),
        "product": "Full=Solute-binding protein family 3/N-terminal domain-containing protein",
        "family": "Belongs to the bacterial solute-binding protein 3 family.",
        "signal": "FT   SIGNAL          1..19",
        "location": "Cell envelope",
        "asta_product": "Full=Solute-binding protein family 3/N-terminal domain-containing protein",
        "rules": {
            "GO:0030313": (
                "cell envelope",
                "ACCEPT",
                "Cell envelope localization is appropriate for this signal-peptide-bearing solute-binding family protein.",
                "UniProt places PP_5157 in the cell envelope and predicts an N-terminal signal peptide.",
                [],
            )
        },
        "core_functions": [],
        "questions": [
            "What ligand, if any, is bound by PP_5157?",
            "Is the ppu02040 flagellar-map membership functional or only a broad neighborhood/annotation artifact?",
        ],
        "experiment": "Purify PP_5157 for ligand-screening assays and test deletion phenotypes in motility, envelope stress, and nutrient uptake panels.",
    },
}


def abcb_rules(gene: str, cfg: dict, *, has_lipid: bool = False, has_oligo: bool = False, has_atpase_coupled: bool = False) -> dict:
    supports = [
        support_uniprot(gene, cfg["product"]),
        support_uniprot(gene, cfg["type1"]),
        support_uniprot(gene, cfg["abc_tm"]),
        support_uniprot(gene, cfg["abc"]),
        support_uniprot(gene, cfg["location"]),
        support_asta(gene, cfg["asta_product"]),
    ]
    rules = {
        "GO:0000166": (
            "nucleotide binding",
            "MODIFY",
            "Nucleotide binding is true but less specific than ATP binding for this ABC transporter.",
            "The protein has an ABC ATP-binding domain, so ATP binding is the more informative nucleotide-binding term.",
            [ATP_BINDING],
        ),
        "GO:0005524": (
            "ATP binding",
            "ACCEPT",
            "ATP binding is appropriate for this fused ABC transporter.",
            "The product name and ABC ATP-binding domain support ATP binding.",
            [],
        ),
        "GO:0005886": (
            "plasma membrane",
            "ACCEPT",
            "Plasma membrane localization is appropriate for this bacterial membrane ABC transporter.",
            "UniProt places the protein in the cell membrane and predicts multiple transmembrane helices.",
            [],
        ),
        "GO:0016020": (
            "membrane",
            "MARK_AS_OVER_ANNOTATED",
            "Membrane localization is correct but less specific than plasma membrane.",
            "The record already has a more specific plasma membrane annotation.",
            [],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity",
            "ACCEPT",
            "ATP hydrolysis activity is appropriate for the ABC ATPase domain.",
            "The ABC ATP-binding domain and conserved ABC transporter signatures support ATP hydrolysis.",
            [],
        ),
        "GO:0043190": (
            "ATP-binding cassette (ABC) transporter complex",
            "KEEP_AS_NON_CORE",
            "ABC transporter complex membership is broad context for this fused transporter.",
            "The protein is an ABC membrane/ATPase transporter, but substrate and partner context remain unresolved.",
            [],
        ),
        "GO:0055085": (
            "transmembrane transport",
            "ACCEPT",
            "Transmembrane transport is broad but defensible for this membrane ABC transporter.",
            "The protein has fused transmembrane and ABC ATP-binding transporter domains, although its substrate is unknown.",
            [],
        ),
        "GO:0140359": (
            "ABC-type transporter activity",
            "ACCEPT",
            "ABC-type transporter activity is the best-supported molecular-function annotation.",
            "UniProt and InterPro support a fused ABC transmembrane and ATP-binding transporter architecture.",
            [],
        ),
    }
    if has_lipid:
        rules["GO:0034040"] = (
            "ATPase-coupled lipid transmembrane transporter activity",
            "MARK_AS_OVER_ANNOTATED",
            "Lipid-transporter activity is more specific than the available evidence supports.",
            (
                "The Type_1_exporter/ABCB architecture supports generic ABC-type transport, but there is no direct "
                "lipid-substrate evidence for this protein."
            ),
            [ABC_TYPE_TRANSPORTER],
        )
    if has_oligo:
        rules["GO:0015421"] = (
            "ABC-type oligopeptide transporter activity",
            "REMOVE",
            "Oligopeptide transporter activity is not supported for this unresolved ABCB-like transporter.",
            "The protein has generic ABCB/type-1-exporter domains, but no oligopeptide substrate or peptide-import locus evidence.",
            [ABC_TYPE_TRANSPORTER],
        )
        rules["GO:0035672"] = (
            "oligopeptide transmembrane transport",
            "REMOVE",
            "Oligopeptide transport is not supported by current evidence.",
            "The local and domain evidence supports an unresolved ABCB-like transporter, not a defined oligopeptide transporter.",
            [TRANSMEMBRANE_TRANSPORT],
        )
    if has_atpase_coupled:
        rules["GO:0042626"] = (
            "ATPase-coupled transmembrane transporter activity",
            "ACCEPT",
            "ATPase-coupled transmembrane transporter activity is appropriate for this fused ABC transporter.",
            "The protein combines ABC ATPase and transmembrane transporter domains.",
            [],
        )
    core = {
        "description": "Unresolved fused ABCB/type-1-exporter-like membrane transporter with unknown substrate.",
        "molecular_function": ABC_TYPE_TRANSPORTER,
        "directly_involved_in": [TRANSMEMBRANE_TRANSPORT],
        "locations": [PLASMA_MEMBRANE],
        "supported_by": [
            support_goa(gene, "GO:0140359", "ABC-type transporter activity"),
            support_uniprot(gene, cfg["product"]),
            support_uniprot(gene, cfg["type1"]),
            support_uniprot(gene, cfg["abc_tm"]),
            support_uniprot(gene, cfg["abc"]),
            support_asta(gene, cfg["asta_product"]),
        ],
    }
    cfg["rules"] = rules
    cfg["core_functions"] = [core]
    cfg["shared_supports"] = supports
    return cfg


GENES["PP_2595"] = abcb_rules("PP_2595", GENES["PP_2595"], has_lipid=True, has_atpase_coupled=True)
GENES["PP_2596"] = abcb_rules("PP_2596", GENES["PP_2596"], has_atpase_coupled=True)
GENES["PP_2628"] = abcb_rules("PP_2628", GENES["PP_2628"], has_oligo=True)
GENES["PP_4542"] = abcb_rules("PP_4542", GENES["PP_4542"], has_oligo=True)


def pp1078_rules() -> dict:
    supports = [
        support_uniprot("PP_1078", "Full=ABC transporter, ATP-binding protein"),
        support_uniprot("PP_1078", "InterPro; IPR003439; ABC_transporter-like_ATP-bd."),
        support_uniprot("PP_1078", "InterPro; IPR013611; Transp-assoc_OB_typ2."),
        support_asta("PP_1078", "Full=ABC transporter, ATP-binding protein"),
    ]
    rules = {
        "GO:0000166": (
            "nucleotide binding",
            "MODIFY",
            "Nucleotide binding is true but less specific than ATP binding for this ABC ATPase.",
            "The protein has an ABC transporter ATP-binding domain.",
            [ATP_BINDING],
        ),
        "GO:0005524": (
            "ATP binding",
            "ACCEPT",
            "ATP binding is appropriate for this ABC ATP-binding protein.",
            "The product name and ABC transporter ATP-binding domain support ATP binding.",
            [],
        ),
        "GO:0006826": (
            "iron ion transport",
            "REMOVE",
            "Iron ion transport is not supported for this isolated ABC ATP-binding protein.",
            "The record lacks a coherent local ferric-iron transporter locus, and other family transfers conflict with the iron call.",
            [],
        ),
        "GO:0015408": (
            "ABC-type ferric iron transporter activity",
            "REMOVE",
            "Ferric-iron transporter activity is more specific than current evidence supports.",
            "PP_1078 has generic ABC ATPase/FbpC-like domain evidence but no confirmed ferric-iron permease or substrate-binding partners.",
            [ATP_HYDROLYSIS],
        ),
        "GO:0015697": (
            "quaternary ammonium group transport",
            "REMOVE",
            "Quaternary-ammonium transport is not supported by the local or domain evidence.",
            "This looks like ARBA/PANTHER family spillover from PotA-like ATPases rather than a substrate-specific call.",
            [],
        ),
        "GO:0016020": (
            "membrane",
            "KEEP_AS_NON_CORE",
            "Membrane association is retained only as broad context.",
            "PP_1078 is an ABC ATP-binding component without clear transmembrane helices in the UniProt feature table.",
            [],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity",
            "ACCEPT",
            "ATP hydrolysis activity is appropriate for this ABC ATPase component.",
            "The ABC transporter ATP-binding domain supports ATP hydrolysis.",
            [],
        ),
        "GO:0022857": (
            "transmembrane transporter activity",
            "MARK_AS_OVER_ANNOTATED",
            "Generic transmembrane transporter activity is too broad for an isolated ABC ATP-binding component.",
            "The direct activity is ATP binding/hydrolysis; substrate transport remains unresolved without partner context.",
            [],
        ),
        "GO:0034755": (
            "iron ion transmembrane transport",
            "REMOVE",
            "Iron ion transmembrane transport is not supported for this isolated ABC ATP-binding protein.",
            "The specific iron-substrate call is not backed by a coherent ferric-iron transporter locus for PP_1078.",
            [],
        ),
        "GO:0043190": (
            "ATP-binding cassette (ABC) transporter complex",
            "KEEP_AS_NON_CORE",
            "ABC transporter complex context is plausible but substrate and partners are unresolved.",
            "The protein is an ABC ATP-binding component, but a complete transporter assignment is not yet established.",
            [],
        ),
        "GO:0055085": (
            "transmembrane transport",
            "KEEP_AS_NON_CORE",
            "Transmembrane transport is retained as broad ABC-transporter context.",
            "The protein likely energizes an ABC transporter, but the substrate and cognate partners are unknown.",
            [],
        ),
        "GO:0098655": (
            "monoatomic cation transmembrane transport",
            "REMOVE",
            "Monoatomic-cation transport is not supported by current evidence.",
            "This appears to follow from the over-specific iron/cation transporter inference rather than direct PP_1078 evidence.",
            [],
        ),
    }
    GENES["PP_1078"]["rules"] = rules
    GENES["PP_1078"]["shared_supports"] = supports
    return GENES["PP_1078"]


GENES["PP_1078"] = pp1078_rules()


def curate_gene(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["product_type"] = "PROTEIN"
    doc["status"] = cfg["status"]
    doc["description"] = cfg["description"]

    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(
        doc,
        uniprot_ref(gene),
        f"UniProtKB entry for {gene} ({cfg['accession']})",
        "UniProt product/domain evidence used for first-pass curation.",
        cfg["product"],
    )
    ensure_reference(
        doc,
        asta_ref(gene),
        f"Asta retrieval report for {gene} ({cfg['accession']})",
        "Asta retrieval confirmed the target product string but did not add strong gene-specific literature.",
        cfg["asta_product"],
    )

    for text in [
        cfg.get("domain"),
        cfg.get("fold"),
        cfg.get("pfam"),
        cfg.get("abc"),
        cfg.get("abc_tm"),
        cfg.get("type1"),
        cfg.get("tobe"),
        cfg.get("phosphate_domain"),
        cfg.get("pather"),
        cfg.get("family"),
        cfg.get("signal"),
        cfg.get("location"),
    ]:
        if text:
            ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['accession']})", supporting_text=text)

    rules = cfg["rules"]
    for ann in doc.get("existing_annotations", []):
        term = ann["term"]
        term_id = term["id"]
        label, action, summary, reason, proposed = rules[term_id]
        extra_support = []
        if gene in {"PP_2595", "PP_2596", "PP_2628", "PP_4542", "PP_1078"}:
            extra_support = cfg.get("shared_supports", [])
        elif gene == "PP_5157":
            extra_support = [
                support_uniprot(gene, cfg["product"]),
                support_uniprot(gene, cfg["family"]),
                support_uniprot(gene, cfg["location"]),
                support_uniprot(gene, cfg["signal"]),
                support_asta(gene, cfg["asta_product"]),
            ]
        elif gene == "PP_3818":
            extra_support = [
                support_uniprot(gene, cfg["product"]),
                support_uniprot(gene, cfg["phosphate_domain"]),
                support_uniprot(gene, cfg["pather"]),
                support_asta(gene, cfg["asta_product"]),
            ]
        elif gene == "PP_0524":
            extra_support = [
                support_uniprot(gene, cfg["product"]),
                support_uniprot(gene, cfg["domain"]),
                support_uniprot(gene, cfg["fold"]),
                support_asta(gene, cfg["asta_product"]),
            ]
        ann["review"] = review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=extra_support)

    doc["core_functions"] = deepcopy(cfg["core_functions"])
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [{"question": q} for q in cfg["questions"]]
    doc["suggested_experiments"] = [{"description": cfg["experiment"], "experiment_type": "targeted transporter phenotype and substrate assay"}]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
