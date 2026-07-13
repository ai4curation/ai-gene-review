#!/usr/bin/env python3
"""First-pass curation for the ppu02010 choline/betaine/carnitine ABC transporter block."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"


def goa_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-goa.tsv"


def uniprot_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-uniprot.txt"


def asta_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md"


def goa_text(term_id: str, label: str) -> str:
    return f"{term_id}\t{label}"


def support_goa(gene: str, term_id: str, label: str) -> dict:
    return {"reference_id": goa_ref(gene), "supporting_text": goa_text(term_id, label)}


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
    asta_text: str | None = None,
    proposed: list[dict] | None = None,
    extra_support: list[dict] | None = None,
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if asta_text:
        supported_by.append(support_asta(gene, asta_text))
    if extra_support:
        supported_by.extend(extra_support)
    result = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if proposed:
        result["proposed_replacement_terms"] = proposed
    return result


def new_annotation(
    term: dict,
    qualifier: str,
    original_reference_id: str,
    summary: str,
    reason: str,
    supported_by: list[dict],
) -> dict:
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": original_reference_id,
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": supported_by,
        },
    }


CHOLINE_TRANSPORTER = {"id": "GO:0015220", "label": "choline transmembrane transporter activity"}
CARNITINE_TRANSPORTER = {
    "id": "GO:0015226",
    "label": "carnitine transmembrane transporter activity",
}
CHOLINE_TRANSPORT = {"id": "GO:0015871", "label": "choline transport"}
CARNITINE_TRANSPORT = {"id": "GO:1902603", "label": "carnitine transmembrane transport"}
GLYCINE_BETAINE_TRANSPORT = {"id": "GO:0031460", "label": "glycine betaine transport"}
CHOLINE_BINDING = {"id": "GO:0033265", "label": "choline binding"}
QUATERNARY_AMMONIUM_TRANSPORTER = {
    "id": "GO:0015418",
    "label": "ABC-type quaternary ammonium compound transporting activity",
}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
ABC_COMPLEX_SBP = {
    "id": "GO:0055052",
    "label": "ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing",
}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
MEMBRANE = {"id": "GO:0016020", "label": "membrane"}
PERIPLASM = {"id": "GO:0042597", "label": "periplasmic space"}
POLYAMINE_TRANSPORT = {"id": "GO:0015846", "label": "polyamine transport"}
POLYAMINE_BINDING = {"id": "GO:0019808", "label": "polyamine binding"}


CONFIG = {
    "cbcV": {
        "symbol": "cbcV",
        "description": (
            "cbcV (PP_0294) encodes the ATP-binding energy-coupling component of a predicted "
            "choline/betaine/carnitine-family ABC uptake system. Its ABC transporter ATP-binding "
            "domain and conserved choline/osmolyte-uptake ATPase signatures support a role in "
            "ATP-driven import of compatible solutes rather than a standalone metabolic activity."
        ),
        "asta_text": "Protein Description:** SubName: Full=Choline / betaine / carnitine ABC transporter-ATP binding subunit",
        "uniprot_text": "Full=Choline / betaine / carnitine ABC transporter-ATP binding subunit",
        "reviews": {
            "GO:0000166": (
                "Nucleotide binding is true but less informative than ATP binding for this ABC transporter ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The protein has a canonical ABC transporter ATP-binding domain, and the specific ATP-binding and ATP-hydrolysis annotations are more useful than generic nucleotide binding.",
            ),
            "GO:0005524": (
                "ATP binding is correct for the nucleotide-binding subunit of the transporter.",
                "ACCEPT",
                "CbcV is annotated as the ATP-binding subunit of a choline/betaine/carnitine ABC transporter and carries ABC transporter ATP-binding domain signatures.",
            ),
            "GO:0006970": (
                "Response to osmotic stress is plausible compatible-solute context but should be kept as non-core for this transporter ATPase.",
                "KEEP_AS_NON_CORE",
                "Choline and glycine betaine import can support osmoadaptation, but this broad stress-response term is less direct than transporter activity and choline/osmolyte transport.",
            ),
            "GO:0015220": (
                "Choline transmembrane transporter activity is a reasonable substrate-specific complex-level assignment for CbcV.",
                "ACCEPT",
                "The choline transporter ATP-binding-domain signature and local cbcV-cbcW-cbcX locus support the ATPase subunit contributing to choline-family ABC uptake.",
            ),
            "GO:0015871": (
                "Choline transport is an appropriate process annotation for this ABC transporter ATPase component.",
                "ACCEPT",
                "The protein name and InterPro choline transporter ATP-binding-domain mapping support choline-family compatible-solute uptake.",
            ),
            "GO:0016887": (
                "ATP hydrolysis is correct mechanistic context for the energy-coupling ABC ATPase.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers the transporter, while the more informative biological role is choline/osmolyte uptake.",
            ),
            "GO:0055052": (
                "ABC transporter complex membership is appropriate for this ATPase in a substrate-binding-protein-dependent uptake system.",
                "ACCEPT",
                "The CbcV ATPase is part of a predicted ABC importer locus with CbcW permease and CbcX/CaiX-like periplasmic substrate-binding components.",
            ),
        },
        "core": {
            "description": "ATP-binding energy-coupling subunit contributing to a choline/betaine/carnitine-family ABC uptake system.",
            "contributes_to_molecular_function": CHOLINE_TRANSPORTER,
            "directly_involved_in": [CHOLINE_TRANSPORT],
            "in_complex": ABC_COMPLEX_SBP,
            "support": ("GO:0015220", "choline transmembrane transporter activity"),
        },
    },
    "cbcW": {
        "symbol": "cbcW",
        "description": (
            "cbcW (PP_0295) encodes the predicted multi-pass inner-membrane permease component "
            "of a choline/betaine/carnitine-family ABC importer. GOA and domain annotations support "
            "a substrate range spanning choline, glycine betaine, and carnitine compatible-solute "
            "transport, with CbcV providing ATPase activity and CbcX/CaiX-like proteins providing "
            "periplasmic substrate binding."
        ),
        "asta_text": "Protein Description:** SubName: Full=Choline / betaine / carnitine ABC transporter-membrane subunit",
        "uniprot_text": "Full=Choline / betaine / carnitine ABC transporter-membrane subunit",
        "reviews": {
            "GO:0005275": (
                "Amine transmembrane transporter activity is directionally correct but too broad for this Cbc permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The same GOA set provides more informative choline, glycine betaine, and carnitine transporter/process terms for this compatible-solute ABC permease.",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass bacterial inner-membrane permease.",
                "ACCEPT",
                "UniProt predicts CbcW as a cell-membrane multi-pass membrane protein.",
            ),
            "GO:0015226": (
                "Carnitine transmembrane transporter activity is a supported substrate-specific assignment for this CbcW permease.",
                "ACCEPT",
                "TreeGrafter and the choline/betaine/carnitine product name support CbcW as the membrane-channel component of a compatible-solute ABC importer.",
            ),
            "GO:0015837": (
                "Amine transport is true but less informative than the available substrate-specific choline, glycine betaine, and carnitine transport terms.",
                "MARK_AS_OVER_ANNOTATED",
                "The broader amine-transport annotation adds little once substrate-specific compatible-solute transport annotations are retained.",
            ),
            "GO:0015871": (
                "Choline transport is appropriate for this compatible-solute ABC permease.",
                "ACCEPT",
                "CbcW carries the choline permease-family domain and is annotated in a choline/betaine/carnitine ABC transporter locus.",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
            ),
            "GO:0031460": (
                "Glycine betaine transport is appropriate compatible-solute context for this permease.",
                "ACCEPT",
                "PANTHER and ARBA support a glycine-betaine/proline-betaine transporter-family assignment, consistent with a Cbc compatible-solute importer.",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this permease subunit.",
                "ACCEPT",
                "CbcW is the binding-protein-dependent transport-system permease in the local cbcV-cbcW-cbcX ABC transporter locus.",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to the specific compatible-solute transport annotations.",
                "MARK_AS_OVER_ANNOTATED",
                "Choline, glycine betaine, and carnitine transport terms better describe the biological role of this permease.",
            ),
            "GO:1902603": (
                "Carnitine transmembrane transport is appropriate for this compatible-solute permease.",
                "ACCEPT",
                "TreeGrafter and the product name support a carnitine-transport role as part of the choline/betaine/carnitine ABC uptake system.",
            ),
        },
        "core": {
            "description": "Multi-pass permease component of a choline/betaine/carnitine-family ABC importer.",
            "molecular_function": CARNITINE_TRANSPORTER,
            "directly_involved_in": [CHOLINE_TRANSPORT, GLYCINE_BETAINE_TRANSPORT, CARNITINE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0015226", "carnitine transmembrane transporter activity"),
        },
    },
    "cbcX": {
        "symbol": "cbcX",
        "description": (
            "cbcX (PP_0296) encodes a signal-peptide-bearing periplasmic substrate-binding "
            "component of the predicted Cbc choline/betaine/carnitine ABC uptake system. Its "
            "OpuAC/ABC glycine-betaine substrate-binding domain and choline-binding GOA support "
            "a substrate-recognition role feeding the CbcV/CbcW transport machinery."
        ),
        "asta_text": "Protein Description:** SubName: Full=Choline / betaine / carnitine ABC transporter-substrate binding protein",
        "uniprot_text": "Full=Choline / betaine / carnitine ABC transporter-substrate binding protein",
        "reviews": {
            "GO:0015871": (
                "Choline transport is appropriate process context for this periplasmic substrate-binding component.",
                "ACCEPT",
                "CbcX is named as the substrate-binding protein of a choline/betaine/carnitine ABC transporter and carries ABC choline/glycine-betaine substrate-binding domains.",
            ),
            "GO:0022857": (
                "Generic transmembrane transporter activity is too broad and potentially misleading for a soluble periplasmic binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "CbcX likely contributes substrate recognition to an ABC importer rather than forming the membrane translocation pathway itself; choline binding and choline transport capture the role more accurately.",
            ),
            "GO:0033265": (
                "Choline binding is the most direct molecular-function annotation for this substrate-binding component.",
                "ACCEPT",
                "The InterPro choline substrate-binding domain and product name support choline-family substrate binding.",
            ),
            "GO:0042597": (
                "Periplasmic localization is appropriate for this signal-peptide-bearing substrate-binding protein.",
                "ACCEPT",
                "UniProt predicts an N-terminal signal peptide and mature chain for this periplasmic binding protein.",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this substrate-binding component.",
                "ACCEPT",
                "CbcX is the periplasmic substrate-binding protein in the local Cbc ABC transporter locus.",
            ),
            "GO:0055085": (
                "Transmembrane transport is correct only as pathway context and is less precise than choline transport for this binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "The protein is predicted to bind substrate in the periplasm, while CbcW forms the membrane permease; the substrate-specific process term is more informative.",
            ),
        },
        "core": {
            "description": "Periplasmic choline-family substrate-binding component of a predicted Cbc compatible-solute ABC importer.",
            "molecular_function": CHOLINE_BINDING,
            "directly_involved_in": [CHOLINE_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0033265", "choline binding"),
        },
    },
    "caiX": {
        "symbol": "caiX",
        "description": (
            "caiX (PP_0304) encodes a signal-peptide-bearing periplasmic substrate-binding "
            "component of the same choline/glycine-betaine substrate-binding protein family as "
            "CbcX, with a product name pointing to carnitine uptake. In this first pass it is "
            "best treated as a related periplasmic compatible-solute binding component, with "
            "the exact choline versus carnitine substrate preference left for experimental follow-up."
        ),
        "asta_text": "Protein Description:** SubName: Full=Carnitine uptake ABC transporter, periplasmic component",
        "uniprot_text": "Full=Carnitine uptake ABC transporter, periplasmic component",
        "reviews": {
            "GO:0015871": (
                "Choline transport is plausible for this choline/glycine-betaine substrate-binding family member, but CaiX is likely broader or carnitine-biased.",
                "KEEP_AS_NON_CORE",
                "InterPro maps the substrate-binding domain to choline transport, while the product name specifically points to a carnitine-uptake periplasmic component; the exact substrate preference remains unresolved.",
            ),
            "GO:0022857": (
                "Generic transmembrane transporter activity is too broad and potentially misleading for a soluble periplasmic binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "CaiX is predicted as a periplasmic substrate-binding component rather than the membrane translocation subunit.",
            ),
            "GO:0033265": (
                "Choline binding is supported by the substrate-binding domain mapping but may not capture the full substrate range.",
                "ACCEPT",
                "The protein carries the ABC choline/glycine-betaine substrate-binding domain and InterPro2GO choline-binding annotation.",
            ),
            "GO:0042597": (
                "Periplasmic localization is appropriate for this signal-peptide-bearing binding protein.",
                "ACCEPT",
                "UniProt predicts an N-terminal signal peptide and mature chain for CaiX.",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this predicted periplasmic binding component.",
                "ACCEPT",
                "CaiX is named as a carnitine uptake ABC transporter periplasmic component and carries the same ABC-compatible-solute binding-domain family as CbcX.",
            ),
            "GO:0055085": (
                "Transmembrane transport is correct as transporter-system context but too broad for this binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "The protein is a periplasmic substrate-binding component; substrate binding and compatible-solute uptake context are more informative.",
            ),
        },
        "new_annotations": [
            {
                "term": CARNITINE_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "Carnitine transmembrane transport is a useful first-pass process annotation for CaiX.",
                "reason": "The UniProt product name identifies CaiX as a carnitine uptake ABC transporter periplasmic component, while its signal peptide and substrate-binding domains support an import-system role.",
                "supporting_text": "Full=Carnitine uptake ABC transporter, periplasmic component",
            },
            {
                "term": CARNITINE_TRANSPORTER,
                "qualifier": "contributes_to",
                "summary": "CaiX should be recorded as contributing to carnitine transmembrane transporter activity.",
                "reason": "As a periplasmic substrate-binding component, CaiX likely supplies substrate recognition for an ABC importer rather than transporting carnitine by itself.",
                "supporting_text": "Full=Carnitine uptake ABC transporter, periplasmic component",
            },
        ],
        "core": {
            "description": "Periplasmic compatible-solute binding component, probably biased toward carnitine uptake but still in the choline/glycine-betaine binding-protein family.",
            "contributes_to_molecular_function": CARNITINE_TRANSPORTER,
            "directly_involved_in": [CARNITINE_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:1902603", "carnitine transmembrane transport"),
            "support_in_goa": False,
        },
    },
    "yehX": {
        "symbol": "yehX",
        "description": (
            "yehX (PP_0868) encodes the ATP-binding energy-coupling component of a "
            "predicted quaternary-amine compatible-solute ABC importer in the PP_0868-PP_0871 "
            "locus. UniProt/RuleBase records quaternary ammonium import chemistry and an ABC "
            "transporter complex architecture, consistent with glycine-betaine/osmoprotectant "
            "uptake rather than a generic amino-acid transport role."
        ),
        "asta_text": "Protein Description:** RecName: Full=Quaternary amine transport ATP-binding protein",
        "uniprot_text": "Full=Quaternary amine transport ATP-binding protein",
        "reviews": {
            "GO:0000166": (
                "Nucleotide binding is true but less informative than ATP binding for this ABC transporter ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The protein has canonical ABC transporter ATP-binding domains, and the specific ATP-binding and ATP-hydrolysis annotations are more useful than generic nucleotide binding.",
            ),
            "GO:0005524": (
                "ATP binding is correct for the nucleotide-binding subunit of the transporter.",
                "ACCEPT",
                "YehX is annotated as a quaternary-amine transport ATP-binding protein and carries ABC transporter ATP-binding domain signatures.",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for the membrane-associated ATPase component of the importer.",
                "ACCEPT",
                "UniProt places YehX at the cell inner membrane as a peripheral membrane protein.",
                None,
                [support_uniprot("yehX", "Cell inner membrane")],
            ),
            "GO:0006865": (
                "Amino acid transport is too broad and potentially misleading for a quaternary-amine compatible-solute importer.",
                "MARK_AS_OVER_ANNOTATED",
                "The reviewed activity and product name support quaternary ammonium compound import, with glycine betaine transport as the substrate-specific GOA process.",
                None,
                [support_uniprot("yehX", "quaternary ammonium(out)")],
            ),
            "GO:0006970": (
                "Response to osmotic stress is plausible compatible-solute context but should be kept as non-core for this transporter ATPase.",
                "KEEP_AS_NON_CORE",
                "Compatible-solute uptake can support osmoadaptation, but this broad stress-response term is less direct than transporter activity and glycine betaine transport.",
            ),
            "GO:0015418": (
                "ABC-type quaternary ammonium compound transporting activity is the best existing molecular-function annotation for YehX.",
                "ACCEPT",
                "UniProt records quaternary ammonium import chemistry for this ATP-binding ABC transporter component.",
                None,
                [support_uniprot("yehX", "Reaction=a quaternary ammonium(out) + ATP + H2O = a quaternary")],
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane/cell-inner-membrane context for this ABC ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
            ),
            "GO:0016887": (
                "ATP hydrolysis is correct mechanistic context for the energy-coupling ABC ATPase.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers the transporter, while the more informative biological role is quaternary-amine/glycine-betaine uptake.",
            ),
            "GO:0031460": (
                "Glycine betaine transport is appropriate compatible-solute process context for YehX.",
                "ACCEPT",
                "The product, EC mapping, and InterPro support a quaternary-amine/osmoprotectant ABC importer role.",
                None,
                [support_uniprot("yehX", "Glycine betaine/choline ABC transporter ATP-binding protein")],
            ),
        },
        "new_annotations": [
            {
                "term": ABC_COMPLEX,
                "qualifier": "part_of",
                "summary": "YehX should be represented as an ATP-binding subunit of a quaternary-amine ABC transporter complex.",
                "reason": "UniProt describes the likely ABC transporter architecture with two ATP-binding proteins, two transmembrane proteins, and a solute-binding protein.",
                "supporting_text": "The complex is probably composed of two ATP-binding proteins",
            },
        ],
        "core": {
            "description": "ATP-binding energy-coupling subunit of a predicted quaternary-amine compatible-solute ABC importer.",
            "molecular_function": QUATERNARY_AMMONIUM_TRANSPORTER,
            "directly_involved_in": [GLYCINE_BETAINE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0015418", "ABC-type quaternary ammonium compound transporting activity"),
        },
        "question": "What quaternary amines are transported by the PP_0868-PP_0871 Yeh-like importer in KT2440?",
        "experiment": "Measure uptake and growth phenotypes for PP_0868-PP_0871 deletion mutants under osmotic stress with glycine betaine, choline, proline betaine, and carnitine supplied individually.",
    },
    "yehW": {
        "symbol": "yehW",
        "description": (
            "yehW (PP_0869) encodes a predicted multi-pass inner-membrane permease component "
            "of the PP_0868-PP_0871 quaternary-amine/osmoprotectant ABC importer. Its "
            "osmoprotectant permease product name, MetI-like permease domains, and local "
            "YehX/PP_0870/PP_0871 partners support glycine-betaine-compatible-solute transport."
        ),
        "asta_text": "Protein Description:** SubName: Full=Osmoprotectant ABC transporter permease subunit",
        "uniprot_text": "Full=Osmoprotectant ABC transporter permease subunit",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass inner-membrane permease.",
                "ACCEPT",
                "UniProt predicts YehW as a cell-membrane multi-pass membrane protein.",
                None,
                [support_uniprot("yehW", "Cell membrane")],
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
            ),
            "GO:0031460": (
                "Glycine betaine transport is appropriate compatible-solute context for this permease.",
                "ACCEPT",
                "The product name and PANTHER/FunFam assignments support an osmoprotectant/glycine-betaine ABC permease role.",
                None,
                [support_uniprot("yehW", "Full=Osmoprotectant ABC transporter permease subunit")],
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this permease subunit.",
                "ACCEPT",
                "YehW is the binding-protein-dependent transport-system permease in the local PP_0868-PP_0871 ABC importer locus.",
                None,
                [support_uniprot("yehW", "Belongs to the binding-protein-dependent transport system")],
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to glycine betaine compatible-solute transport.",
                "MARK_AS_OVER_ANNOTATED",
                "Glycine betaine transport and ABC complex membership better describe the role of this permease.",
            ),
        },
        "new_annotations": [
            {
                "term": QUATERNARY_AMMONIUM_TRANSPORTER,
                "qualifier": "contributes_to",
                "summary": "YehW should be recorded as contributing to ABC-type quaternary ammonium compound transporting activity.",
                "reason": "As a membrane permease in the PP_0868-PP_0871 osmoprotectant ABC locus, YehW contributes the translocation channel for the quaternary-amine importer.",
                "supporting_text": "Full=Osmoprotectant ABC transporter permease subunit",
            },
        ],
        "core": {
            "description": "Multi-pass permease component of a predicted quaternary-amine compatible-solute ABC importer.",
            "contributes_to_molecular_function": QUATERNARY_AMMONIUM_TRANSPORTER,
            "directly_involved_in": [GLYCINE_BETAINE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0031460", "glycine betaine transport"),
        },
        "question": "Does YehW pair with both PP_0871 and PP_0870 in a single quaternary-amine ABC importer, and what substrates are transported?",
        "experiment": "Assay PP_0868-PP_0871 mutant uptake and osmotic-stress growth with glycine betaine, choline, proline betaine, and carnitine supplied individually.",
    },
    "PP_0870": {
        "symbol": "PP_0870",
        "description": (
            "PP_0870 encodes a predicted periplasmic substrate-binding component of the "
            "PP_0868-PP_0871 glycine betaine/carnitine/choline ABC importer. Its product "
            "name and OpuAC/ABC glycine-betaine substrate-binding domain support a "
            "compatible-solute recognition role feeding the YehX/YehW/PP_0871 transport machinery."
        ),
        "asta_text": "Protein Description:** SubName: Full=Glycine betaine/carnitine/choline ABC transporter, periplasmic binding protein",
        "uniprot_text": "Full=Glycine betaine/carnitine/choline ABC transporter, periplasmic binding protein",
        "reviews": {
            "GO:0022857": (
                "Generic transmembrane transporter activity is too broad and potentially misleading for a periplasmic substrate-binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "PP_0870 likely contributes substrate recognition to an ABC importer rather than forming the membrane translocation pathway itself.",
                None,
                [support_uniprot("PP_0870", "Full=Glycine betaine/carnitine/choline ABC transporter, periplasmic binding protein")],
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this substrate-binding component.",
                "ACCEPT",
                "PP_0870 is the periplasmic binding protein in the local PP_0868-PP_0871 compatible-solute ABC transporter locus.",
                None,
                [support_uniprot("PP_0870", "Full=Glycine betaine/carnitine/choline ABC transporter, periplasmic binding protein")],
            ),
            "GO:0055085": (
                "Transmembrane transport is correct only as transporter-system context and is less precise than glycine betaine compatible-solute transport for this binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "The protein is predicted to bind substrate in the periplasm, while the permease components form the membrane translocation pathway.",
            ),
        },
        "new_annotations": [
            {
                "term": GLYCINE_BETAINE_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "PP_0870 should be represented as contributing to glycine betaine compatible-solute transport.",
                "reason": "The product name and OpuAC/ABC glycine-betaine substrate-binding domain support a glycine-betaine-family substrate-recognition role.",
                "supporting_text": "Full=Glycine betaine/carnitine/choline ABC transporter, periplasmic binding protein",
            },
            {
                "term": QUATERNARY_AMMONIUM_TRANSPORTER,
                "qualifier": "contributes_to",
                "summary": "PP_0870 should be recorded as contributing to ABC-type quaternary ammonium compound transporting activity.",
                "reason": "As the periplasmic binding protein in a quaternary-amine compatible-solute ABC locus, PP_0870 supplies substrate recognition for the importer.",
                "supporting_text": "Full=Glycine betaine/carnitine/choline ABC transporter, periplasmic binding protein",
            },
            {
                "term": PERIPLASM,
                "qualifier": "located_in",
                "summary": "PP_0870 should be represented as a periplasmic substrate-binding component.",
                "reason": "The UniProt product name identifies PP_0870 as a periplasmic binding protein.",
                "supporting_text": "periplasmic binding protein",
            },
        ],
        "core": {
            "description": "Periplasmic substrate-binding component of a predicted quaternary-amine compatible-solute ABC importer.",
            "contributes_to_molecular_function": QUATERNARY_AMMONIUM_TRANSPORTER,
            "directly_involved_in": [GLYCINE_BETAINE_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0031460", "glycine betaine transport"),
            "support_in_goa": False,
        },
        "question": "Which quaternary amine does PP_0870 preferentially bind, and does it act with the PP_0868-PP_0871 importer in vivo?",
        "experiment": "Measure ligand binding by purified PP_0870 and uptake phenotypes of PP_0870 and PP_0868-PP_0871 mutants for glycine betaine, choline, proline betaine, and carnitine.",
    },
    "PP_0871": {
        "symbol": "PP_0871",
        "description": (
            "PP_0871 encodes a predicted multi-pass inner-membrane permease component of the "
            "PP_0868-PP_0871 glycine betaine/carnitine/choline ABC importer. Its product name, "
            "glycine-betaine permease-family assignments, and local YehX/YehW/PP_0870 partners "
            "support compatible-solute import."
        ),
        "asta_text": "Protein Description:** SubName: Full=Glycine betaine/carnitine/choline ABC transporter, permease protein",
        "uniprot_text": "Full=Glycine betaine/carnitine/choline ABC transporter, permease protein",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass inner-membrane permease.",
                "ACCEPT",
                "UniProt predicts PP_0871 as a cell-membrane multi-pass membrane protein.",
                None,
                [support_uniprot("PP_0871", "Cell membrane")],
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
            ),
            "GO:0031460": (
                "Glycine betaine transport is appropriate compatible-solute context for this permease.",
                "ACCEPT",
                "The product name and PANTHER/FunFam assignments support a glycine-betaine/choline compatible-solute ABC permease role.",
                None,
                [support_uniprot("PP_0871", "Full=Glycine betaine/carnitine/choline ABC transporter, permease protein")],
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this permease subunit.",
                "ACCEPT",
                "PP_0871 is a binding-protein-dependent transport-system permease in the local PP_0868-PP_0871 ABC importer locus.",
                None,
                [support_uniprot("PP_0871", "Belongs to the binding-protein-dependent transport system")],
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to glycine betaine compatible-solute transport.",
                "MARK_AS_OVER_ANNOTATED",
                "Glycine betaine transport and ABC complex membership better describe the role of this permease.",
            ),
        },
        "new_annotations": [
            {
                "term": QUATERNARY_AMMONIUM_TRANSPORTER,
                "qualifier": "contributes_to",
                "summary": "PP_0871 should be recorded as contributing to ABC-type quaternary ammonium compound transporting activity.",
                "reason": "As a membrane permease in the PP_0868-PP_0871 compatible-solute ABC locus, PP_0871 contributes the translocation channel for the quaternary-amine importer.",
                "supporting_text": "Full=Glycine betaine/carnitine/choline ABC transporter, permease protein",
            },
        ],
        "core": {
            "description": "Multi-pass permease component of a predicted quaternary-amine compatible-solute ABC importer.",
            "contributes_to_molecular_function": QUATERNARY_AMMONIUM_TRANSPORTER,
            "directly_involved_in": [GLYCINE_BETAINE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0031460", "glycine betaine transport"),
        },
        "question": "Does PP_0871 pair with YehW as the second permease of the PP_0868-PP_0871 quaternary-amine importer, and what substrates are transported?",
        "experiment": "Assay PP_0868-PP_0871 mutant uptake and osmotic-stress growth with glycine betaine, choline, proline betaine, and carnitine supplied individually.",
    },
    "potF-I": {
        "symbol": "potF-I",
        "description": (
            "potF-I (PP_0873) encodes a predicted periplasmic putrescine/polyamine substrate-binding "
            "protein adjacent to, but functionally distinct from, the PP_0868-PP_0871 "
            "compatible-solute ABC importer. UniProt and InterPro support polyamine binding and "
            "polyamine transport context, while the cognate permease/ATPase partners for this "
            "specific PotF-I copy remain unresolved."
        ),
        "asta_text": "Protein Description:** SubName: Full=Putrescine-binding periplasmic protein",
        "uniprot_text": "Full=Putrescine-binding periplasmic protein",
        "reviews": {
            "GO:0015846": (
                "Polyamine transport is appropriate process context for this putrescine-binding periplasmic component.",
                "ACCEPT",
                "UniProt names PotF-I as a putrescine-binding periplasmic protein and InterPro maps the family to polyamine transport.",
                None,
                [support_uniprot("potF-I", "Full=Putrescine-binding periplasmic protein")],
            ),
            "GO:0019808": (
                "Polyamine binding is appropriate molecular-function context for this putrescine-binding protein.",
                "ACCEPT",
                "The product name and spermidine/putrescine-binding periplasmic-protein family support polyamine substrate binding.",
                None,
                [support_uniprot("potF-I", "SPERMIDINE/PUTRESCINE-BINDING PERIPLASMIC PROTEIN")],
            ),
            "GO:0042597": (
                "Periplasmic localization is appropriate for this substrate-binding protein.",
                "ACCEPT",
                "UniProt places PotF-I in the periplasm.",
                None,
                [support_uniprot("potF-I", "Periplasm")],
            ),
        },
        "core": {
            "description": "Periplasmic putrescine/polyamine substrate-binding protein with unresolved transporter partners.",
            "molecular_function": POLYAMINE_BINDING,
            "directly_involved_in": [POLYAMINE_TRANSPORT],
            "locations": [PERIPLASM],
            "support": ("GO:0019808", "polyamine binding"),
        },
        "question": "Which permease and ATPase partners pair with PotF-I in KT2440 polyamine uptake?",
        "experiment": "Map potF-I genetic context and test PotF-I ligand binding and mutant uptake phenotypes for putrescine, spermidine, and related polyamines.",
    },
}


def curate_gene(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["gene_symbol"] = cfg["symbol"]
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]

    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({doc['id']})", cfg["uniprot_text"])
    ensure_reference(doc, asta_ref(gene), f"Asta retrieval report for {gene} ({doc['id']})", cfg["asta_text"])

    doc["existing_annotations"] = [
        ann
        for ann in doc.get("existing_annotations", [])
        if ann.get("review", {}).get("action") != "NEW"
    ]

    for ann in doc.get("existing_annotations", []):
        term = ann["term"]
        term_id = term["id"]
        label = term["label"]
        entry = cfg["reviews"][term_id]
        proposed = entry[3] if len(entry) > 3 else None
        extra_support = entry[4] if len(entry) > 4 else None
        asta_text = cfg["asta_text"] if term_id == cfg["core"]["support"][0] else None
        ann["review"] = review(
            gene,
            term_id,
            label,
            entry[0],
            entry[1],
            entry[2],
            asta_text=asta_text,
            proposed=proposed,
            extra_support=extra_support,
        )

    existing_term_ids = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}
    for extra in cfg.get("new_annotations", []):
        term = extra["term"]
        if term["id"] in existing_term_ids:
            continue
        doc.setdefault("existing_annotations", []).append(
            new_annotation(
                term,
                extra["qualifier"],
                uniprot_ref(gene),
                extra["summary"],
                extra["reason"],
                [
                    support_uniprot(gene, extra["supporting_text"]),
                    support_asta(gene, cfg["asta_text"]),
                ],
            )
        )

    core = dict(cfg["core"])
    support_term = core.pop("support")
    support_in_goa = core.pop("support_in_goa", True)
    core["supported_by"] = []
    if support_in_goa:
        core["supported_by"].append(support_goa(gene, support_term[0], support_term[1]))
    core["supported_by"].extend(
        [
            support_uniprot(gene, cfg["uniprot_text"]),
            support_asta(gene, cfg["asta_text"]),
        ]
    )
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": cfg.get(
                "question",
                "What are the substrate preferences of the PP_0294-PP_0296 and PP_0304 compatible-solute binding components across choline, glycine betaine, proline betaine, and carnitine?",
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": cfg.get(
                "experiment",
                "Measure uptake and growth phenotypes for cbcV/cbcW/cbcX/caiX mutants under osmotic stress with choline, glycine betaine, proline betaine, and carnitine supplied individually.",
            ),
            "experiment_type": "targeted transporter mutant substrate-uptake and osmotic-stress growth assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in CONFIG.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
