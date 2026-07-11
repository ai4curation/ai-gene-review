#!/usr/bin/env python3
"""First-pass curation for KEGG ppu01503 CAMP-resistance boundary stubs."""

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


def product_support(text: str) -> str:
    return text


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


def support_goa(gene: str, term_id: str, label: str) -> dict:
    return {
        "reference_id": goa_ref(gene),
        "supporting_text": goa_text(term_id, label),
    }


def support_asta(gene: str, text: str) -> dict:
    return {
        "reference_id": asta_ref(gene),
        "supporting_text": text,
    }


def support_uniprot(gene: str, text: str) -> dict:
    return {
        "reference_id": uniprot_ref(gene),
        "supporting_text": text,
    }


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
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if asta_text:
        supported_by.append(support_asta(gene, asta_text))
    result = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if proposed:
        result["proposed_replacement_terms"] = proposed
    return result


CONFIG = {
    "dsbA": {
        "symbol": "dsbA",
        "description": "dsbA encodes a predicted periplasmic thiol:disulfide interchange protein of the DsbA/thioredoxin family. It likely catalyzes disulfide oxidoreductase reactions during extracytoplasmic protein folding and contributes to periplasmic redox homeostasis.",
        "asta_text": "Protein Description:** RecName: Full=Thiol:disulfide interchange protein",
        "uniprot_text": "RecName: Full=Thiol:disulfide interchange protein",
        "reviews": {
            "GO:0015036": ("Disulfide oxidoreductase activity is the specific core DsbA-family molecular function.", "ACCEPT", "DsbA is annotated as a thiol:disulfide interchange protein with DsbA/thioredoxin domains, making the disulfide oxidoreductase term appropriate."),
            "GO:0016491": ("Generic oxidoreductase activity is true but less informative than disulfide oxidoreductase activity.", "MARK_AS_OVER_ANNOTATED", "The specific GO:0015036 disulfide oxidoreductase activity is already present and captures the DsbA-family chemistry more precisely."),
            "GO:0042597": ("Periplasmic space is the expected compartment for bacterial DsbA-family oxidative folding proteins.", "ACCEPT", "The GOA localization and UniProt subcellular mapping support periplasmic localization."),
            "GO:0045454": ("Cell redox homeostasis is compatible with DsbA disulfide exchange and periplasmic oxidative folding.", "ACCEPT", "DsbA-family disulfide oxidoreductases directly support extracytoplasmic redox homeostasis."),
        },
        "core": {
            "description": "Periplasmic DsbA-family disulfide oxidoreductase that supports extracytoplasmic protein folding and redox homeostasis.",
            "molecular_function": {"id": "GO:0015036", "label": "disulfide oxidoreductase activity"},
            "directly_involved_in": [{"id": "GO:0045454", "label": "cell redox homeostasis"}],
            "locations": [{"id": "GO:0042597", "label": "periplasmic space"}],
            "support_term": ("GO:0015036", "disulfide oxidoreductase activity"),
        },
    },
    "phoP": {
        "symbol": "phoP",
        "description": "PhoP is a predicted OmpR/PhoB-family response regulator with a CheY-like receiver domain and a winged-helix DNA-binding effector domain. It is the cytosolic transcriptional-regulatory partner of the PhoPQ two-component system and is represented in the CAMP-resistance map as envelope-stress regulatory context.",
        "asta_text": "Protein Description:** SubName: Full=Two component system DNA-binding transcriptional dual regulator",
        "uniprot_text": "SubName: Full=Two component system DNA-binding transcriptional dual regulator",
        "reviews": {
            "GO:0000156": ("PhoP has the receiver-domain architecture expected for a phosphorelay response regulator.", "ACCEPT", "The CheY-like receiver and OmpR/PhoB DNA-binding domains support response-regulator activity."),
            "GO:0000160": ("PhoP participates in two-component phosphorelay signaling as the response regulator component.", "ACCEPT", "The domain architecture and PhoP gene name support phosphorelay signal-transduction context."),
            "GO:0000976": ("Transcription cis-regulatory region binding captures the DNA-binding effector function of PhoP-like regulators.", "ACCEPT", "The OmpR/PhoB-type DNA-binding domain supports regulatory DNA binding."),
            "GO:0003677": ("DNA binding is correct but less informative than transcription cis-regulatory region binding.", "MARK_AS_OVER_ANNOTATED", "GO:0000976 provides the more specific DNA-binding function."),
            "GO:0005829": ("Cytosol is plausible for a soluble bacterial response regulator.", "KEEP_AS_NON_CORE", "Localization is useful context, while the core function is phosphorelay response regulation and transcriptional control."),
            "GO:0006355": ("Regulation of DNA-templated transcription is the expected output of an OmpR/PhoB-family response regulator.", "ACCEPT", "PhoP carries a DNA-binding effector domain and GOA supports transcriptional regulation."),
            "GO:0032993": ("Protein-DNA complex is plausible for DNA-bound response regulator but is not the core function.", "KEEP_AS_NON_CORE", "Retain as complex context while using response-regulator and transcription-regulatory terms as the main functional assertions."),
        },
        "core": {
            "description": "Cytosolic OmpR/PhoB-family response regulator that links phosphorelay signaling to transcriptional regulation.",
            "molecular_function": {"id": "GO:0000156", "label": "phosphorelay response regulator activity"},
            "directly_involved_in": [{"id": "GO:0006355", "label": "regulation of DNA-templated transcription"}],
            "support_term": ("GO:0000156", "phosphorelay response regulator activity"),
        },
    },
    "phoQ": {
        "symbol": "phoQ",
        "description": "PhoQ is a predicted plasma-membrane sensor histidine kinase with HAMP, dimerization/phosphoacceptor, and HATPase domains. It is represented in the CAMP-resistance map as the membrane sensor kinase partner of the PhoPQ envelope-stress regulatory system.",
        "asta_text": "Protein Description:** RecName: Full=histidine kinase",
        "uniprot_text": "RecName: Full=histidine kinase",
        "reviews": {
            "GO:0000155": ("Phosphorelay sensor kinase activity is the core molecular function of PhoQ.", "ACCEPT", "PhoQ has histidine kinase domains and EC 2.7.13.3 support."),
            "GO:0000160": ("PhoQ is a two-component sensor kinase, so phosphorelay signal transduction is appropriate.", "ACCEPT", "The HAMP and histidine-kinase domain architecture supports phosphorelay signaling."),
            "GO:0004673": ("Protein histidine kinase activity is correct enzyme-class context for PhoQ.", "KEEP_AS_NON_CORE", "The more system-specific GO:0000155 phosphorelay sensor kinase activity captures the core function."),
            "GO:0005886": ("Plasma membrane localization is appropriate for a bacterial sensor histidine kinase.", "ACCEPT", "GOA and transmembrane sensor-kinase architecture support membrane localization."),
            "GO:0007165": ("Signal transduction is correct but broad relative to phosphorelay signal transduction.", "KEEP_AS_NON_CORE", "Retain as general signaling context while using GO:0000160 for the specific process."),
            "GO:0016020": ("Membrane is correct but less specific than plasma membrane.", "MARK_AS_OVER_ANNOTATED", "GO:0005886 is the more specific membrane localization already present."),
            "GO:0016301": ("Generic kinase activity is a broad parent of the histidine/sensor kinase function.", "MARK_AS_OVER_ANNOTATED", "GO:0000155 and GO:0004673 describe the PhoQ activity more specifically."),
            "GO:0016740": ("Generic transferase activity is too broad for a histidine kinase.", "MARK_AS_OVER_ANNOTATED", "Specific kinase terms are already present."),
            "GO:0016772": ("Generic phosphorus-transferase activity is too broad for a histidine kinase.", "MARK_AS_OVER_ANNOTATED", "Specific phosphorelay sensor kinase and protein histidine kinase terms are already present."),
        },
        "core": {
            "description": "Plasma-membrane phosphorelay sensor histidine kinase that supports two-component signal transduction.",
            "molecular_function": {"id": "GO:0000155", "label": "phosphorelay sensor kinase activity"},
            "directly_involved_in": [{"id": "GO:0000160", "label": "phosphorelay signal transduction system"}],
            "locations": [{"id": "GO:0005886", "label": "plasma membrane"}],
            "support_term": ("GO:0000155", "phosphorelay sensor kinase activity"),
        },
    },
    "PP_1202": {
        "symbol": "PP_1202",
        "description": "PP_1202 encodes a predicted membrane phosphatidylglycerol lysyltransferase, also known as lysylphosphatidylglycerol synthase. This MprF/LPG-synthase-family enzyme modifies phosphatidylglycerol with lysine, a membrane lipid modification that can reduce anionic surface charge and is therefore relevant to cationic antimicrobial peptide resistance.",
        "asta_text": "Protein Description:** RecName: Full=Phosphatidylglycerol lysyltransferase",
        "uniprot_text": "RecName: Full=Phosphatidylglycerol lysyltransferase",
        "reviews": {
            "GO:0005886": ("Plasma membrane localization is expected for phosphatidylglycerol lysyltransferase.", "ACCEPT", "The enzyme modifies membrane phospholipid and GOA supports plasma membrane localization."),
            "GO:0016755": ("Aminoacyltransferase activity is a broad parent of the specific lysylphosphatidylglycerol synthase activity.", "MARK_AS_OVER_ANNOTATED", "GO:0050071 is the informative molecular function for this protein."),
            "GO:0047637": ("Phosphatidylglycerol alanyltransferase activity is likely the wrong aminoacyl specificity for this lysyltransferase.", "MODIFY", "UniProt and EC mapping support phosphatidylglycerol lysyltransferase activity rather than alanyltransferase activity.", [{"id": "GO:0050071", "label": "phosphatidylglycerol lysyltransferase activity"}]),
            "GO:0050071": ("Phosphatidylglycerol lysyltransferase activity is the core molecular function.", "ACCEPT", "The UniProt name, EC mapping, and LPG synthase/PANTHER family support this assignment."),
            "GO:0055091": ("Phospholipid homeostasis is plausible process context for membrane phosphatidylglycerol aminoacylation.", "ACCEPT", "Phosphatidylglycerol lysylation directly changes membrane phospholipid composition."),
        },
        "core": {
            "description": "Membrane phosphatidylglycerol lysyltransferase that aminoacylates phosphatidylglycerol and contributes to phospholipid homeostasis.",
            "molecular_function": {"id": "GO:0050071", "label": "phosphatidylglycerol lysyltransferase activity"},
            "directly_involved_in": [{"id": "GO:0055091", "label": "phospholipid homeostasis"}],
            "locations": [{"id": "GO:0005886", "label": "plasma membrane"}],
            "support_term": ("GO:0050071", "phosphatidylglycerol lysyltransferase activity"),
        },
    },
    "PP_1430": {
        "symbol": "PP_1430",
        "description": "PP_1430 encodes a predicted periplasmic DegP/HtrA-family serine endoprotease with PDZ domains. It likely functions in envelope protein quality control through periplasmic proteolysis and is included in the CAMP-resistance map as envelope-stress support context.",
        "asta_text": "Protein Description:** RecName: Full=Probable periplasmic serine endoprotease DegP-like",
        "uniprot_text": "RecName: Full=Probable periplasmic serine endoprotease DegP-like",
        "reviews": {
            "GO:0004252": ("Serine-type endopeptidase activity is the core predicted activity of this DegP/HtrA-family protein.", "ACCEPT", "The peptidase S1C/DegP domain architecture and EC mapping support this activity."),
            "GO:0006508": ("Proteolysis is the direct biological process for a DegP-like endoprotease.", "ACCEPT", "GOA and InterPro support proteolysis for this serine endoprotease."),
            "GO:0042597": ("Periplasmic space localization is appropriate for a DegP-like envelope protease.", "ACCEPT", "UniProt/GOA support a periplasmic location."),
        },
        "core": {
            "description": "Periplasmic DegP/HtrA-family serine endoprotease involved in envelope protein proteolysis.",
            "molecular_function": {"id": "GO:0004252", "label": "serine-type endopeptidase activity"},
            "directly_involved_in": [{"id": "GO:0006508", "label": "proteolysis"}],
            "locations": [{"id": "GO:0042597", "label": "periplasmic space"}],
            "support_term": ("GO:0004252", "serine-type endopeptidase activity"),
        },
    },
    "PP_2320": {
        "symbol": "PP_2320",
        "description": "PP_2320 encodes a predicted extracytoplasmic YkuD/L,D-transpeptidase-family protein with LysM cell-wall-binding context. It likely participates in peptidoglycan cross-linking or remodeling and is included in the CAMP-resistance map as cell-envelope remodeling context.",
        "asta_text": "Protein Description:** RecName: Full=L,D-TPase catalytic domain-containing protein",
        "uniprot_text": "RecName: Full=L,D-TPase catalytic domain-containing protein",
        "reviews": {
            "GO:0000270": ("Peptidoglycan metabolic process is broad but compatible with a YkuD/L,D-transpeptidase-family cell-wall enzyme.", "KEEP_AS_NON_CORE", "Retain as broad process context while using L,D-transpeptidase activity and cross-linking as the specific assertions."),
            "GO:0004180": ("Carboxypeptidase activity is less informative than the predicted peptidoglycan L,D-transpeptidase activity.", "MODIFY", "The YkuD/L,D-transpeptidase domain and specific GOA term support GO:0071972 as the better molecular function.", [{"id": "GO:0071972", "label": "peptidoglycan L,D-transpeptidase activity"}]),
            "GO:0005576": ("Extracellular region is broad but plausible for an extracytoplasmic cell-wall-associated protein.", "KEEP_AS_NON_CORE", "Retain as localization context pending a more specific periplasm/cell-envelope term."),
            "GO:0008360": ("Regulation of cell shape is plausible downstream context for peptidoglycan cross-linking.", "KEEP_AS_NON_CORE", "This is not the core activity but is consistent with cell-wall remodeling."),
            "GO:0016740": ("Generic transferase activity is too broad for an L,D-transpeptidase-domain protein.", "MODIFY", "Use the specific peptidoglycan L,D-transpeptidase activity term.", [{"id": "GO:0071972", "label": "peptidoglycan L,D-transpeptidase activity"}]),
            "GO:0018104": ("Peptidoglycan-protein cross-linking is supported by the L,D-transpeptidase/YkuD family assignment.", "ACCEPT", "TreeGrafter and domain architecture support a peptidoglycan cross-linking role."),
            "GO:0071555": ("Cell wall organization is correct envelope-remodeling context.", "KEEP_AS_NON_CORE", "Retain as broad process context while the core function is L,D-transpeptidase activity."),
            "GO:0071972": ("Peptidoglycan L,D-transpeptidase activity is the most specific predicted molecular function.", "ACCEPT", "The YkuD/L,D-transpeptidase domain and GOA term directly support this function."),
            "GO:0009252": ("Peptidoglycan biosynthetic process is acceptable broad pathway context for a peptidoglycan cross-linking enzyme.", "KEEP_AS_NON_CORE", "The more specific process in this review is peptidoglycan-protein cross-linking."),
        },
        "core": {
            "description": "Predicted cell-envelope L,D-transpeptidase-family enzyme involved in peptidoglycan cross-linking/remodeling.",
            "molecular_function": {"id": "GO:0071972", "label": "peptidoglycan L,D-transpeptidase activity"},
            "directly_involved_in": [{"id": "GO:0018104", "label": "peptidoglycan-protein cross-linking"}],
            "support_term": ("GO:0071972", "peptidoglycan L,D-transpeptidase activity"),
        },
    },
    "cpxR": {
        "symbol": "cpxR",
        "description": "CpxR is a predicted OmpR/PhoB-family two-component response regulator with receiver and DNA-binding effector domains. It is the transcriptional regulatory component of Cpx-type envelope-stress signaling and appears in the CAMP-resistance map as regulatory boundary context.",
        "asta_text": "Protein Description:** SubName: Full=CpxR-Pasp DNA-binding transcriptional two-component system regulator",
        "uniprot_text": "SubName: Full=CpxR-Pasp DNA-binding transcriptional two-component system regulator",
        "reviews": {},
        "core": {
            "description": "Cytoplasmic OmpR/PhoB-family response regulator that couples phosphorelay signaling to transcriptional regulation.",
            "molecular_function": {"id": "GO:0000156", "label": "phosphorelay response regulator activity"},
            "directly_involved_in": [{"id": "GO:0006355", "label": "regulation of DNA-templated transcription"}],
            "support_term": ("GO:0000156", "phosphorelay response regulator activity"),
        },
    },
    "PP_4503": {
        "symbol": "PP_4503",
        "description": "PP_4503 encodes a predicted OmpR/PhoB-family DNA-binding response regulator with receiver and transcriptional effector domains. Its specific upstream sensor and regulon are not resolved in this first pass, so it is treated as a generic two-component transcriptional regulator in the CAMP-resistance boundary map.",
        "asta_text": "Protein Description:** SubName: Full=DNA-binding response regulator",
        "uniprot_text": "SubName: Full=DNA-binding response regulator",
        "reviews": {},
        "core": {
            "description": "Predicted cytoplasmic response regulator that links phosphorelay signaling to transcriptional regulation.",
            "molecular_function": {"id": "GO:0000156", "label": "phosphorelay response regulator activity"},
            "directly_involved_in": [{"id": "GO:0006355", "label": "regulation of DNA-templated transcription"}],
            "support_term": ("GO:0000156", "phosphorelay response regulator activity"),
        },
    },
    "ppiA": {
        "symbol": "ppiA",
        "description": "ppiA encodes a predicted cyclophilin-family peptidyl-prolyl cis-trans isomerase. The enzyme catalyzes proline peptide-bond isomerization during protein folding and is included in the CAMP-resistance map as envelope/protein-folding stress context rather than a direct antimicrobial peptide resistance enzyme.",
        "asta_text": "Protein Description:** RecName: Full=Peptidyl-prolyl cis-trans isomerase",
        "uniprot_text": "RecName: Full=Peptidyl-prolyl cis-trans isomerase",
        "reviews": {
            "GO:0003755": ("Peptidyl-prolyl cis-trans isomerase activity is the core molecular function.", "ACCEPT", "The cyclophilin/PPIase domain architecture and EC/Rhea support this activity."),
            "GO:0006457": ("Protein folding is the direct process context for a PPIase.", "ACCEPT", "Peptidyl-prolyl isomerization supports protein folding."),
            "GO:0016853": ("Generic isomerase activity is true but less informative than PPIase activity.", "MARK_AS_OVER_ANNOTATED", "GO:0003755 is the specific isomerase function."),
        },
        "core": {
            "description": "Cyclophilin-family peptidyl-prolyl cis-trans isomerase involved in protein folding.",
            "molecular_function": {"id": "GO:0003755", "label": "peptidyl-prolyl cis-trans isomerase activity"},
            "directly_involved_in": [{"id": "GO:0006457", "label": "protein folding"}],
            "support_term": ("GO:0003755", "peptidyl-prolyl cis-trans isomerase activity"),
        },
    },
    "amiC": {
        "symbol": "amiC",
        "description": "amiC encodes a predicted periplasmic N-acetylmuramoyl-L-alanine amidase with MurNAc-LAA and LysM/AMIN cell-wall-associated domains. It hydrolyzes peptidoglycan amide bonds during cell-wall turnover or cell separation and is included in the CAMP-resistance map as envelope remodeling context.",
        "asta_text": "Protein Description:** RecName: Full=N-acetylmuramoyl-L-alanine amidase AmiC",
        "uniprot_text": "RecName: Full=N-acetylmuramoyl-L-alanine amidase AmiC",
        "reviews": {
            "GO:0008745": ("N-acetylmuramoyl-L-alanine amidase activity is the core molecular function.", "ACCEPT", "The UniProt name, EC assignment, and MurNAc-LAA domain support this activity."),
            "GO:0009253": ("Peptidoglycan catabolic process is the direct process context for AmiC amidase activity.", "ACCEPT", "AmiC hydrolyzes peptidoglycan amide bonds during cell-wall turnover/remodeling."),
            "GO:0030288": ("Outer membrane-bounded periplasmic space is the most specific available localization.", "ACCEPT", "The cell-wall-associated amidase is predicted to act in the Gram-negative periplasm."),
            "GO:0042597": ("Periplasmic space is correct but less specific than outer membrane-bounded periplasmic space.", "KEEP_AS_NON_CORE", "Retain as broad periplasmic context while using GO:0030288 as the more specific location."),
        },
        "core": {
            "description": "Periplasmic N-acetylmuramoyl-L-alanine amidase involved in peptidoglycan catabolism/remodeling.",
            "molecular_function": {"id": "GO:0008745", "label": "N-acetylmuramoyl-L-alanine amidase activity"},
            "directly_involved_in": [{"id": "GO:0009253", "label": "peptidoglycan catabolic process"}],
            "locations": [{"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}],
            "support_term": ("GO:0008745", "N-acetylmuramoyl-L-alanine amidase activity"),
        },
    },
}


REGULATOR_REVIEWS = {
    "GO:0000156": ("Response regulator activity is the core molecular function.", "ACCEPT", "The receiver and OmpR/PhoB-type DNA-binding domains support phosphorelay response-regulator activity."),
    "GO:0000160": ("Phosphorelay signal transduction is the appropriate two-component signaling process.", "ACCEPT", "The receiver-domain architecture supports involvement in bacterial phosphorelay signaling."),
    "GO:0000976": ("Transcription cis-regulatory region binding captures the DNA-binding effector function.", "ACCEPT", "The OmpR/PhoB-type DNA-binding domain supports regulatory DNA binding."),
    "GO:0003677": ("DNA binding is correct but less informative than transcription cis-regulatory region binding.", "MARK_AS_OVER_ANNOTATED", "GO:0000976 is the more specific DNA-binding term."),
    "GO:0005737": ("Cytoplasm is plausible for a soluble response regulator.", "KEEP_AS_NON_CORE", "Localization is context; response-regulator and transcription-regulatory functions are the core assertions."),
    "GO:0005829": ("Cytosol is plausible for a soluble response regulator.", "KEEP_AS_NON_CORE", "Localization is context; response-regulator and transcription-regulatory functions are the core assertions."),
    "GO:0006355": ("Regulation of DNA-templated transcription is the expected output of this response regulator family.", "ACCEPT", "The DNA-binding effector domain supports transcriptional regulation."),
    "GO:0032993": ("Protein-DNA complex is plausible when the regulator binds DNA but is not the core function.", "KEEP_AS_NON_CORE", "Retain as complex context while using response-regulator and transcription-regulatory terms as the main functional assertions."),
}

CONFIG["cpxR"]["reviews"] = REGULATOR_REVIEWS
CONFIG["PP_4503"]["reviews"] = REGULATOR_REVIEWS


def curate_gene(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["gene_symbol"] = cfg["symbol"]
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]

    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({doc['id']})", cfg["uniprot_text"])
    ensure_reference(doc, asta_ref(gene), f"Asta retrieval report for {gene} ({doc['id']})", cfg["asta_text"])

    review_cfg = cfg["reviews"]
    for ann in doc.get("existing_annotations", []):
        term = ann["term"]
        term_id = term["id"]
        label = term["label"]
        entry = review_cfg[term_id]
        proposed = entry[3] if len(entry) > 3 else None
        asta_text = cfg["asta_text"] if term_id == cfg["core"]["support_term"][0] else None
        ann["review"] = review(
            gene,
            term_id,
            label,
            entry[0],
            entry[1],
            entry[2],
            asta_text=asta_text,
            proposed=proposed,
        )

    core = dict(cfg["core"])
    support_term = core.pop("support_term")
    core["supported_by"] = [
        support_goa(gene, support_term[0], support_term[1]),
        support_uniprot(gene, cfg["uniprot_text"]),
        support_asta(gene, cfg["asta_text"]),
    ]
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "Is this CAMP-resistance map member directly required for cationic antimicrobial peptide tolerance in P. putida KT2440, or is it present as broader envelope stress/remodeling context?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Compare deletion or depletion phenotypes under polymyxin/colistin or other cationic antimicrobial peptide challenge, alongside envelope integrity and relevant pathway readouts.",
            "experiment_type": "targeted mutant stress-sensitivity assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in CONFIG.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
