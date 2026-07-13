#!/usr/bin/env python3
"""First-pass curation for remaining ppu02010 compatible-solute ABC transporter candidates."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"


def ref_path(gene: str, suffix: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{suffix}"


def goa_ref(gene: str) -> str:
    return ref_path(gene, "goa.tsv")


def uniprot_ref(gene: str) -> str:
    return ref_path(gene, "uniprot.txt")


def asta_ref(gene: str) -> str:
    return ref_path(gene, "deep-research-asta.md")


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
    uniprot_text: str | None = None,
    asta_text: str | None = None,
    extra_support: list[dict] | None = None,
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if uniprot_text:
        supported_by.append(support_uniprot(gene, uniprot_text))
    if asta_text:
        supported_by.append(support_asta(gene, asta_text))
    if extra_support:
        supported_by.extend(extra_support)
    return {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }


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


ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
CHOLINE_BINDING = {"id": "GO:0033265", "label": "choline binding"}
CHOLINE_TRANSPORT = {"id": "GO:0015871", "label": "choline transport"}
CARNITINE_TRANSPORT = {"id": "GO:1902603", "label": "carnitine transmembrane transport"}
GLYCINE_BETAINE_TRANSPORT = {"id": "GO:0031460", "label": "glycine betaine transport"}
QUATERNARY_AMMONIUM_TRANSPORTER = {
    "id": "GO:0015418",
    "label": "ABC-type quaternary ammonium compound transporting activity",
}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PERIPLASM = {"id": "GO:0042597", "label": "periplasmic space"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}


CONFIG = {
    "betX": {
        "symbol": "betX",
        "description": (
            "betX (PP_1741) encodes a signal-peptide-bearing substrate-binding component "
            "of the choline/betaine/carnitine ABC transporter family. Its product name, "
            "OpuAC/ABC glycine-betaine substrate-binding domain, and retrieved Cbc-family "
            "evidence support a compatible-solute recognition role, with glycine betaine "
            "as the strongest first-pass core substrate call."
        ),
        "uniprot_text": "Full=Choline / betaine / carnitine ABC transporter-substrate binding protein BetX",
        "asta_text": "Protein Description:** SubName: Full=Choline / betaine / carnitine ABC transporter-substrate binding protein BetX",
        "reviews": {
            "GO:0005275": (
                "Amine transmembrane transporter activity is directionally compatible but too broad for this substrate-binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "BetX is annotated as a substrate-binding protein, so it should be represented as contributing substrate recognition rather than as the membrane translocation activity itself.",
                "Full=Choline / betaine / carnitine ABC transporter-substrate binding protein BetX",
            ),
            "GO:0005886": (
                "Plasma membrane localization is plausible for this signal-peptide-bearing transporter-associated component but is not the most informative localization call.",
                "KEEP_AS_NON_CORE",
                "UniProt maps BetX to the cell membrane, while the product/domain evidence and Cbc-family literature support a periplasmic-side substrate-binding role.",
                "Cell membrane",
            ),
            "GO:0015226": (
                "Carnitine transmembrane transporter activity is too strong as a direct enables annotation for this substrate-binding protein.",
                "MARK_AS_OVER_ANNOTATED",
                "The Cbc-family model assigns carnitine recognition to CaiX and betaine recognition to BetX; BetX should be represented as a binding component contributing to compatible-solute ABC transport.",
                "Full=Choline / betaine / carnitine ABC transporter-substrate binding protein BetX",
            ),
            "GO:0015837": (
                "Amine transport is broad compatible-solute context and is less informative than glycine betaine transport for BetX.",
                "MARK_AS_OVER_ANNOTATED",
                "The product and retrieved Cbc-family evidence support a quaternary-amine compatible-solute substrate-binding role rather than generic amine transport.",
                "Full=Choline / betaine / carnitine ABC transporter-substrate binding protein BetX",
            ),
            "GO:0015871": (
                "Choline transport is plausible compatible-solute context but is not the core BetX substrate call.",
                "KEEP_AS_NON_CORE",
                "TreeGrafter/product evidence links BetX to the choline/betaine/carnitine Cbc family, but the retrieved Cbc model identifies BetX as betaine-specific relative to CbcX choline binding and CaiX carnitine binding.",
                "Full=Choline / betaine / carnitine ABC transporter-substrate binding protein BetX",
            ),
            "GO:0022857": (
                "Generic transmembrane transporter activity is too broad and potentially misleading for a substrate-binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "BetX likely supplies substrate recognition to an ABC importer rather than forming the membrane translocation pathway.",
                "ABC_Gly_betaine_transp_sub-bd",
            ),
            "GO:0031460": (
                "Glycine betaine transport is the best supported process annotation for BetX.",
                "ACCEPT",
                "The product, OpuAC/ABC glycine-betaine substrate-binding domain, and retrieved Cbc-family evidence support BetX as a betaine-family substrate-binding component.",
                "ABC_Gly_betaine_transp_sub-bd",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this substrate-binding component.",
                "ACCEPT",
                "The product name and domain assignment support BetX as a substrate-binding component of a compatible-solute ABC transporter system.",
                "Full=Choline / betaine / carnitine ABC transporter-substrate binding protein BetX",
            ),
            "GO:0055085": (
                "Transmembrane transport is correct only as transporter-system context and is less precise than glycine betaine compatible-solute transport for BetX.",
                "MARK_AS_OVER_ANNOTATED",
                "The protein is a substrate-binding component; cognate permease and ATPase components would mediate membrane translocation.",
                "Full=Choline / betaine / carnitine ABC transporter-substrate binding protein BetX",
            ),
            "GO:1902603": (
                "Carnitine transmembrane transport is plausible Cbc-family context but is not the core BetX substrate call.",
                "KEEP_AS_NON_CORE",
                "The retrieved Cbc-family model identifies CaiX as the carnitine-specific binding protein and BetX as betaine-specific, so carnitine transport should not be treated as the defining BetX process.",
                "Full=Choline / betaine / carnitine ABC transporter-substrate binding protein BetX",
            ),
        },
        "new": [
            new_annotation(
                QUATERNARY_AMMONIUM_TRANSPORTER,
                "contributes_to",
                "betX",
                "BetX should be represented as contributing substrate recognition to ABC-type quaternary ammonium compound transport.",
                "BetX is a substrate-binding component in the choline/betaine/carnitine ABC transporter family, with retrieved Cbc-family evidence supporting betaine-specific binding.",
                [
                    support_uniprot("betX", "Full=Choline / betaine / carnitine ABC transporter-substrate binding protein BetX"),
                    support_uniprot("betX", "ABC_Gly_betaine_transp_sub-bd"),
                    support_asta("betX", "the betaine‐specific SBP BetX"),
                ],
            ),
            new_annotation(
                PERIPLASM,
                "located_in",
                "betX",
                "BetX should be represented as a periplasmic-side substrate-binding component.",
                "The protein has an N-terminal signal peptide and belongs to the periplasmic OpuAC/ABC glycine-betaine substrate-binding family.",
                [
                    support_uniprot("betX", "SIGNAL          1..29"),
                    support_uniprot("betX", "Periplasmic binding protein-like"),
                    support_asta("betX", "multiple periplasmic substrate‐binding proteins"),
                ],
            ),
        ],
        "core": {
            "description": "Periplasmic-side betaine-family substrate-binding component contributing to compatible-solute ABC import.",
            "contributes_to_molecular_function": QUATERNARY_AMMONIUM_TRANSPORTER,
            "directly_involved_in": [GLYCINE_BETAINE_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("betX", "GO:0031460", "glycine betaine transport"),
                support_uniprot("betX", "Full=Choline / betaine / carnitine ABC transporter-substrate binding protein BetX"),
                support_uniprot("betX", "ABC_Gly_betaine_transp_sub-bd"),
                support_asta("betX", "the betaine‐specific SBP BetX"),
            ],
        },
        "question": "Does KT2440 BetX pair with CbcW/CbcV or another transporter core, and is glycine betaine its dominant in vivo ligand?",
        "experiment": "Measure purified BetX ligand binding and test betX/cbcWV mutant uptake phenotypes for glycine betaine, choline, carnitine, and proline betaine.",
    },
    "PP_0076": {
        "symbol": "PP_0076",
        "description": (
            "PP_0076 encodes a signal-peptide-bearing choline betaine-binding protein in the "
            "OpuAC/ABC glycine-betaine substrate-binding family. Its InterPro2GO annotations "
            "support a periplasmic substrate-recognition role in choline-family compatible-solute "
            "ABC uptake, while the cognate membrane and ATPase partners remain unresolved."
        ),
        "uniprot_text": "Full=Choline betaine-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Choline betaine-binding protein",
        "reviews": {
            "GO:0015871": (
                "Choline transport is appropriate process context for this compatible-solute substrate-binding component.",
                "ACCEPT",
                "The InterPro choline-binding substrate-binding domain maps PP_0076 to choline transport.",
                "ABC_choline_sub-bd",
            ),
            "GO:0022857": (
                "Generic transmembrane transporter activity is too broad and potentially misleading for a soluble periplasmic binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "PP_0076 is a signal-peptide-bearing substrate-binding protein; it likely supplies substrate recognition rather than forming the membrane translocation pathway.",
                "Full=Choline betaine-binding protein",
            ),
            "GO:0033265": (
                "Choline binding is the most direct molecular-function annotation for this substrate-binding component.",
                "ACCEPT",
                "The product name and InterPro choline substrate-binding domain support choline-family substrate binding.",
                "Full=Choline betaine-binding protein",
            ),
            "GO:0042597": (
                "Periplasmic localization is appropriate for this signal-peptide-bearing binding protein.",
                "ACCEPT",
                "UniProt predicts an N-terminal signal peptide and mature chain for PP_0076.",
                "SIGNAL          1..20",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this substrate-binding component.",
                "ACCEPT",
                "The ABC glycine-betaine substrate-binding family annotation supports PP_0076 as a binding component of an ABC transporter complex.",
                "ABC_Gly_betaine_transp_sub-bd",
            ),
            "GO:0055085": (
                "Transmembrane transport is correct only as transporter-system context and is less precise than choline transport for this binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "The protein is predicted to bind substrate in the periplasm, while cognate permease components would form the membrane translocation pathway.",
                "Full=Choline betaine-binding protein",
            ),
        },
        "core": {
            "description": "Periplasmic choline-family substrate-binding component with unresolved cognate transporter partners.",
            "molecular_function": CHOLINE_BINDING,
            "directly_involved_in": [CHOLINE_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("PP_0076", "GO:0033265", "choline binding"),
                support_uniprot("PP_0076", "Full=Choline betaine-binding protein"),
                support_uniprot("PP_0076", "ABC_choline_sub-bd"),
                support_asta("PP_0076", "Protein Description:** SubName: Full=Choline betaine-binding protein"),
            ],
        },
        "question": "Which permease and ATPase partners pair with PP_0076, and does it prefer choline, glycine betaine, proline betaine, or another compatible solute?",
        "experiment": "Measure ligand binding by purified PP_0076 and test uptake phenotypes of candidate neighboring transporter mutants with choline, glycine betaine, and proline betaine.",
    },
    "opuA": {
        "symbol": "opuA",
        "description": (
            "opuA (PP_2774) encodes a glycine betaine ABC transporter ATPase/permease fusion "
            "protein. Its N-terminal ABC transporter ATP-binding domain, C-terminal MetI-like "
            "multi-pass permease domain, plasma-membrane localization, and adjacent PP_2775 "
            "substrate-binding component support an ATP-dependent glycine-betaine compatible-solute "
            "import role."
        ),
        "uniprot_text": "Full=Glycine betaine ABC transporter, ATPase/permease fusion protein",
        "asta_text": "Protein Description:** SubName: Full=Glycine betaine ABC transporter, ATPase/permease fusion protein",
        "reviews": {
            "GO:0000166": (
                "Nucleotide binding is true but less informative than ATP binding for this ABC transporter fusion protein.",
                "MARK_AS_OVER_ANNOTATED",
                "The specific ATP-binding annotation captures the relevant nucleotide-binding chemistry for the ABC ATPase domain.",
                "ABC_transporter-like_ATP-bd",
            ),
            "GO:0005524": (
                "ATP binding is correct for the ABC ATPase domain of the fusion protein.",
                "ACCEPT",
                "UniProt records ABC transporter ATP-binding signatures in the N-terminal portion of OpuA.",
                "ABC_transporter-like_ATP-bd",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass membrane transporter component.",
                "ACCEPT",
                "UniProt places OpuA at the cell membrane and predicts multiple transmembrane helices.",
                "Cell membrane",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane transporter.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell membrane",
            ),
            "GO:0016887": (
                "ATP hydrolysis is correct mechanistic chemistry but non-core relative to ABC glycine-betaine transport.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers ABC transport, while the biological role is glycine-betaine compatible-solute uptake.",
                "ABC_transporter-like_ATP-bd",
            ),
            "GO:0031460": (
                "Glycine betaine transport is the best substrate-specific process annotation for OpuA.",
                "ACCEPT",
                "The product name identifies OpuA as a glycine betaine ABC transporter ATPase/permease fusion protein.",
                "Full=Glycine betaine ABC transporter, ATPase/permease fusion protein",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this ATPase/permease fusion component.",
                "ACCEPT",
                "OpuA combines ATP-binding and permease domains and is adjacent to the PP_2775 periplasmic substrate-binding component.",
                "Belongs to the binding-protein-dependent transport system",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to glycine betaine transport for this importer component.",
                "MARK_AS_OVER_ANNOTATED",
                "The glycine betaine transport annotation better captures the substrate-specific biological process.",
                "Full=Glycine betaine ABC transporter, ATPase/permease fusion protein",
            ),
        },
        "new": [
            new_annotation(
                QUATERNARY_AMMONIUM_TRANSPORTER,
                "contributes_to",
                "opuA",
                "OpuA should be represented as contributing ATPase/permease functions to ABC-type quaternary ammonium compound transport.",
                "Glycine betaine is a quaternary-amine compatible solute, and OpuA contains both ABC ATP-binding and MetI-like permease domains.",
                [
                    support_uniprot("opuA", "Full=Glycine betaine ABC transporter, ATPase/permease fusion protein"),
                    support_uniprot("opuA", "ABC_osmolyte_uptake_ATP-bind"),
                    support_asta("opuA", "Protein Description:** SubName: Full=Glycine betaine ABC transporter, ATPase/permease fusion protein"),
                ],
            )
        ],
        "core": {
            "description": "ATPase/permease fusion component of a predicted glycine-betaine compatible-solute ABC importer.",
            "contributes_to_molecular_function": QUATERNARY_AMMONIUM_TRANSPORTER,
            "directly_involved_in": [GLYCINE_BETAINE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("opuA", "GO:0031460", "glycine betaine transport"),
                support_uniprot("opuA", "Full=Glycine betaine ABC transporter, ATPase/permease fusion protein"),
                support_uniprot("opuA", "ABC_osmolyte_uptake_ATP-bind"),
                support_asta("opuA", "Protein Description:** SubName: Full=Glycine betaine ABC transporter, ATPase/permease fusion protein"),
            ],
        },
        "question": "Does the opuA-PP_2775 importer prefer glycine betaine, L-proline, proline betaine, or another compatible solute in KT2440?",
        "experiment": "Assay opuA and PP_2775 mutants for compatible-solute uptake and osmotic-stress growth with glycine betaine, L-proline, proline betaine, and choline supplied individually.",
    },
    "PP_2775": {
        "symbol": "PP_2775",
        "description": (
            "PP_2775 encodes a signal-peptide-bearing glycine betaine/L-proline ABC transporter "
            "periplasmic component. Its OpuAC/ABC glycine-betaine substrate-binding domain and "
            "adjacent opuA ATPase/permease fusion support a substrate-recognition role in a "
            "predicted glycine-betaine compatible-solute ABC importer."
        ),
        "uniprot_text": "Full=Glycine betaine/L-proline ABC transporter, periplasmic component",
        "asta_text": "Protein Description:** SubName: Full=Glycine betaine/L-proline ABC transporter, periplasmic component",
        "reviews": {
            "GO:0022857": (
                "Generic transmembrane transporter activity is too broad and potentially misleading for a periplasmic substrate-binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "PP_2775 likely contributes substrate recognition to the adjacent OpuA ABC importer rather than forming the membrane translocation pathway itself.",
                "Full=Glycine betaine/L-proline ABC transporter, periplasmic component",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this substrate-binding component.",
                "ACCEPT",
                "PP_2775 is the periplasmic binding component adjacent to the opuA ATPase/permease fusion.",
                "ABC_Gly_betaine_transp_sub-bd",
            ),
            "GO:0055085": (
                "Transmembrane transport is correct only as transporter-system context and is less precise than glycine betaine transport for this binding component.",
                "MARK_AS_OVER_ANNOTATED",
                "The protein is predicted to bind substrate in the periplasm, while OpuA provides membrane translocation and ATPase domains.",
                "Full=Glycine betaine/L-proline ABC transporter, periplasmic component",
            ),
        },
        "new": [
            new_annotation(
                GLYCINE_BETAINE_TRANSPORT,
                "involved_in",
                "PP_2775",
                "PP_2775 should be represented with glycine betaine transport as compatible-solute process context.",
                "The product name and OpuAC/ABC glycine-betaine substrate-binding domain support a glycine-betaine-family substrate-recognition role.",
                [
                    support_uniprot("PP_2775", "Full=Glycine betaine/L-proline ABC transporter, periplasmic component"),
                    support_uniprot("PP_2775", "ABC_Gly_betaine_transp_sub-bd"),
                    support_asta("PP_2775", "Protein Description:** SubName: Full=Glycine betaine/L-proline ABC transporter, periplasmic component"),
                ],
            ),
            new_annotation(
                QUATERNARY_AMMONIUM_TRANSPORTER,
                "contributes_to",
                "PP_2775",
                "PP_2775 should be recorded as contributing substrate recognition to ABC-type quaternary ammonium compound transport.",
                "As a periplasmic binding component of the opuA-adjacent glycine-betaine ABC importer, PP_2775 contributes substrate recognition rather than ATP hydrolysis or membrane translocation.",
                [
                    support_uniprot("PP_2775", "Full=Glycine betaine/L-proline ABC transporter, periplasmic component"),
                    support_uniprot("PP_2775", "ABC_Gly_betaine_transp_sub-bd"),
                    support_asta("PP_2775", "Protein Description:** SubName: Full=Glycine betaine/L-proline ABC transporter, periplasmic component"),
                ],
            ),
            new_annotation(
                PERIPLASM,
                "located_in",
                "PP_2775",
                "PP_2775 should be represented as a periplasmic substrate-binding component.",
                "UniProt predicts an N-terminal signal peptide and mature chain for this periplasmic binding component.",
                [
                    support_uniprot("PP_2775", "SIGNAL          1..26"),
                    support_uniprot("PP_2775", "Full=Glycine betaine/L-proline ABC transporter, periplasmic component"),
                    support_asta("PP_2775", "Protein Description:** SubName: Full=Glycine betaine/L-proline ABC transporter, periplasmic component"),
                ],
            ),
        ],
        "core": {
            "description": "Periplasmic substrate-binding component of the predicted opuA-PP_2775 glycine-betaine compatible-solute ABC importer.",
            "contributes_to_molecular_function": QUATERNARY_AMMONIUM_TRANSPORTER,
            "directly_involved_in": [GLYCINE_BETAINE_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("PP_2775", "Full=Glycine betaine/L-proline ABC transporter, periplasmic component"),
                support_uniprot("PP_2775", "ABC_Gly_betaine_transp_sub-bd"),
                support_uniprot("PP_2775", "SIGNAL          1..26"),
                support_asta("PP_2775", "Protein Description:** SubName: Full=Glycine betaine/L-proline ABC transporter, periplasmic component"),
            ],
        },
        "question": "Does PP_2775 bind glycine betaine, L-proline, proline betaine, or another osmoprotectant, and is OpuA its sole membrane partner?",
        "experiment": "Measure PP_2775 ligand binding and opuA/PP_2775 mutant uptake phenotypes for glycine betaine, L-proline, proline betaine, and choline.",
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
        ann for ann in doc.get("existing_annotations", []) if ann.get("review", {}).get("action") != "NEW"
    ]

    for ann in doc.get("existing_annotations", []):
        term_id = ann["term"]["id"]
        if term_id not in cfg["reviews"]:
            raise ValueError(f"No review configured for {gene} {term_id}")
        summary, action, reason, uniprot_text = cfg["reviews"][term_id]
        ann["review"] = review(
            gene,
            term_id,
            ann["term"]["label"],
            summary,
            action,
            reason,
            uniprot_text=uniprot_text,
            asta_text=cfg["asta_text"],
        )

    doc["existing_annotations"].extend(deepcopy(cfg.get("new", [])))

    core = deepcopy(cfg["core"])
    core["supported_by"] = core.pop("support")
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [{"question": cfg["question"]}]
    doc["suggested_experiments"] = [
        {
            "description": cfg["experiment"],
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
