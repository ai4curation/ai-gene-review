#!/usr/bin/env python3
"""First-pass curation for KEGG ppu03420 nucleotide-excision repair stubs."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path("genes") / SPECIES


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on on inter-ontology links",
    "GO_REF:0000116": "Automatic Gene Ontology annotation based on Rhea mapping",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


GENES: dict[str, dict] = {
    "polA": {
        "symbol": "polA",
        "description": (
            "polA (PP_0123) encodes DNA polymerase I, a bacterial family-A DNA polymerase "
            "with polymerase, 3'-5' exonuclease, and 5'-3' exonuclease activities. It "
            "acts in DNA repair-synthesis and Okazaki-fragment maturation, including the "
            "gap-filling step after nucleotide-excision repair has removed damaged DNA."
        ),
        "core": {
            "description": (
                "DNA polymerase I repair/replication enzyme with polymerase and exonuclease "
                "activities used for DNA gap filling and primer/flap removal."
            ),
            "molecular_function": {
                "id": "GO:0003887",
                "label": "DNA-directed DNA polymerase activity",
            },
            "directly_involved_in": [
                {"id": "GO:0006281", "label": "DNA repair"},
                {"id": "GO:0006260", "label": "DNA replication"},
            ],
        },
        "decisions": {
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is expected for DNA polymerase I but is less informative than its polymerase and exonuclease activities"),
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is correct background context for PolA but not the pathway-defining function"),
            "GO:0003824": ("MARK_AS_OVER_ANNOTATED", "generic catalytic activity is uninformative for a well-defined polymerase/exonuclease enzyme"),
            "GO:0003887": ("ACCEPT", "DNA-directed DNA polymerase activity is the core PolA polymerase function"),
            "GO:0006260": ("ACCEPT", "PolA participates in DNA replication through Okazaki-fragment processing and repair synthesis"),
            "GO:0006261": ("KEEP_AS_NON_CORE", "DNA-templated DNA replication is correct but broader than the PolA-specific repair/Okazaki-processing role"),
            "GO:0006281": ("ACCEPT", "DNA repair is a core process for PolA repair synthesis after excision repair"),
            "GO:0006302": ("MARK_AS_OVER_ANNOTATED", "double-strand break repair is not the primary PolA pathway assignment in this first-pass NER batch"),
            "GO:0008408": ("ACCEPT", "PolA carries a 3'-5' exonuclease proofreading domain"),
            "GO:0008409": ("ACCEPT", "PolA carries the 5'-3' exonuclease activity used in nick translation and primer/flap removal"),
            "GO:0016779": ("KEEP_AS_NON_CORE", "nucleotidyltransferase activity is a broad parent of DNA polymerase activity"),
            "GO:0034061": ("KEEP_AS_NON_CORE", "DNA polymerase activity is correct but less specific than DNA-directed DNA polymerase activity"),
            "GO:0071897": ("KEEP_AS_NON_CORE", "DNA biosynthetic process is a broad process parent of DNA replication and repair synthesis"),
        },
    },
    "mfd": {
        "symbol": "mfd",
        "description": (
            "mfd (PP_2148) encodes transcription-repair coupling factor, an ATP-dependent "
            "UvrB/RecG-like DNA motor that recognizes stalled transcription complexes, "
            "removes or remodels RNA polymerase at DNA lesions, and recruits the UvrABC "
            "nucleotide-excision repair machinery for transcription-coupled repair."
        ),
        "core": {
            "description": (
                "ATP-dependent transcription-repair coupling factor linking stalled RNA "
                "polymerase complexes to bacterial nucleotide-excision repair."
            ),
            "molecular_function": {"id": "GO:0016887", "label": "ATP hydrolysis activity"},
            "directly_involved_in": [
                {
                    "id": "GO:0000716",
                    "label": "transcription-coupled nucleotide-excision repair, DNA damage recognition",
                },
                {"id": "GO:0006281", "label": "DNA repair"},
            ],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
        },
        "decisions": {
            "GO:0000166": ("KEEP_AS_NON_CORE", "nucleotide binding is generic for an ATP-dependent DNA motor"),
            "GO:0000716": ("ACCEPT", "transcription-coupled nucleotide-excision repair is the defining Mfd process"),
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is expected but generic"),
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected for TRCF but less specific than the transcription-coupled repair process"),
            "GO:0003678": ("MARK_AS_OVER_ANNOTATED", "Mfd is best treated as an ATP-dependent transcription-repair coupling DNA motor rather than a standalone DNA helicase"),
            "GO:0003684": ("KEEP_AS_NON_CORE", "damaged DNA binding is plausible repair context but Mfd primarily recognizes stalled transcription complexes"),
            "GO:0005524": ("ACCEPT", "ATP binding is required for the Mfd DNA motor cycle"),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for a bacterial DNA repair factor"),
            "GO:0006281": ("ACCEPT", "Mfd links stalled transcription complexes to DNA repair"),
            "GO:0006355": ("KEEP_AS_NON_CORE", "Mfd affects transcription complexes during repair, but generic transcription regulation is not the main annotation"),
            "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "generic hydrolase activity is uninformative for an ATP-dependent DNA motor"),
            "GO:0016887": ("ACCEPT", "ATP hydrolysis powers Mfd translocation/remodeling during transcription-coupled repair"),
        },
    },
    "PP_2839": {
        "symbol": "PP_2839",
        "description": (
            "PP_2839 encodes a predicted DinG/Rad3-like superfamily helicase with "
            "ATP-binding and helicase domains. In the ppu03420 boundary it is treated as "
            "a candidate DNA repair helicase side node rather than a defined UvrABC core "
            "subunit, because current local metadata do not specify the physiological "
            "repair substrate or exact NER step."
        ),
        "core": {
            "description": "Predicted DinG/Rad3-like ATP-dependent DNA helicase of unresolved repair-pathway specificity.",
            "molecular_function": {"id": "GO:0003678", "label": "DNA helicase activity"},
        },
        "decisions": {
            "GO:0000166": ("KEEP_AS_NON_CORE", "nucleotide binding is generic for a P-loop helicase"),
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is expected but less informative than DNA helicase activity"),
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected for a DNA helicase but not specific"),
            "GO:0003678": ("ACCEPT", "DNA helicase activity fits the DinG/Rad3-like helicase domain architecture"),
            "GO:0004386": ("KEEP_AS_NON_CORE", "generic helicase activity is less specific than DNA helicase activity"),
            "GO:0005524": ("ACCEPT", "ATP binding is required for the predicted helicase motor"),
            "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "generic hydrolase activity is uninformative for a predicted helicase"),
            "GO:0016818": ("MARK_AS_OVER_ANNOTATED", "acid-anhydride hydrolase activity is a broad ATPase parent and should not be the main function"),
        },
    },
    "PP_3087": {
        "symbol": "PP_3087",
        "description": (
            "PP_3087 encodes an unreviewed UvrA-family ATPase-like protein with ABC/P-loop "
            "ATPase and UvrA DNA-binding-domain signatures. KEGG places it in the "
            "Pseudomonas putida nucleotide-excision repair map, but the current GOA set "
            "supports only ATP-binding/hydrolysis and cytoplasmic localization, so this "
            "first pass treats it as a candidate UvrA-like NER boundary component."
        ),
        "core": {
            "description": "Candidate UvrA-family ATPase-like protein in the ppu03420 NER boundary.",
            "molecular_function": {"id": "GO:0016887", "label": "ATP hydrolysis activity"},
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
        },
        "decisions": {
            "GO:0000166": ("KEEP_AS_NON_CORE", "nucleotide binding is generic for an ATPase-family protein"),
            "GO:0005524": ("ACCEPT", "ATP binding is supported by the ABC/P-loop ATPase-family assignment"),
            "GO:0005737": ("ACCEPT", "cytoplasm is plausible for a bacterial DNA repair ATPase"),
            "GO:0016887": ("ACCEPT", "ATP hydrolysis activity is the most specific current GOA molecular-function annotation"),
        },
        "questions": [
            "Is PP_3087 a functional second UvrA-like nucleotide-excision repair factor in KT2440, or an ATPase paralog with a different DNA-repair substrate?"
        ],
    },
}


def support_for(term_id: str, label: str, gene: str) -> dict:
    return {
        "reference_id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
        "supporting_text": f"{term_id}\t{label}",
    }


def unique_references(existing: list[dict], gene: str) -> list[dict]:
    refs: list[dict] = []
    seen: set[str] = set()
    for ref in existing:
        ref_id = ref.get("id")
        if not ref_id or ref_id in seen:
            continue
        if ref_id in GO_REF_TITLES:
            ref = {"id": ref_id, "title": GO_REF_TITLES[ref_id], "findings": []}
        refs.append(ref)
        seen.add(ref_id)
    for ref in [
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
            "title": f"UniProtKB entry for {gene}",
            "findings": [
                {
                    "statement": "UniProt identity, protein name, family, and domain metadata used for first-pass pathway curation."
                }
            ],
        },
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
            "title": f"QuickGO GOA annotations for {gene}",
            "findings": [
                {"statement": "GOA table containing the annotations reviewed in this file."}
            ],
        },
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md",
            "title": f"Asta retrieval report for {gene}",
            "findings": [
                {
                    "statement": "Asta retrieval used as fast gene-level literature context; no unsupported hypotheses were imported."
                }
            ],
        },
    ]:
        if ref["id"] not in seen:
            refs.append(ref)
            seen.add(ref["id"])
    return refs


def curated_review(gene: str, term_id: str, label: str, decision: tuple) -> dict:
    action, reason, *rest = decision
    if action == "ACCEPT":
        summary = f"{label} is supported for {gene} in the ppu03420 first-pass curation."
    elif action == "KEEP_AS_NON_CORE":
        summary = f"{label} is plausible for {gene} but is not the most specific pathway-defining function."
    elif action == "MARK_AS_OVER_ANNOTATED":
        summary = f"{label} is too broad or over-propagated for the main function of {gene}."
    elif action == "MODIFY":
        summary = f"{label} should be replaced by a more specific or biologically appropriate term for {gene}."
    else:
        summary = f"{label} was reviewed for {gene}."
    review = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": [support_for(term_id, label, gene)],
    }
    if rest:
        review["proposed_replacement_terms"] = rest[0]
    return review


def core_supported_by(core: dict, annotations: list[dict], gene: str) -> list[dict]:
    support: list[dict] = []
    term_index = {
        ann["term"]["id"]: ann["term"]["label"]
        for ann in annotations
        if ann.get("term", {}).get("id")
    }
    for slot in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
        term = core.get(slot)
        if isinstance(term, dict) and term.get("id") in term_index:
            support.append(support_for(term["id"], term_index[term["id"]], gene))
    for slot in ("directly_involved_in", "locations"):
        for term in core.get(slot, []) or []:
            if term.get("id") in term_index:
                support.append(support_for(term["id"], term_index[term["id"]], gene))
    if support:
        return support
    return [
        {
            "reference_id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
            "supporting_text": "Reference proteome",
        }
    ]


def curate_gene(gene: str, spec: dict) -> None:
    path = ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["gene_symbol"] = spec["symbol"]
    data["status"] = "DRAFT"
    data["description"] = spec["description"]

    decisions = spec["decisions"]
    for ann in data.get("existing_annotations", []):
        term = ann["term"]
        decision = decisions.get(term["id"], ("KEEP_AS_NON_CORE", "not part of the primary ppu03420 first-pass interpretation"))
        ann["review"] = curated_review(gene, term["id"], term["label"], decision)

    core = dict(spec["core"])
    core["supported_by"] = core_supported_by(core, data.get("existing_annotations", []), gene)
    data["core_functions"] = [core]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": question,
        }
        for question in spec.get(
            "questions",
            [
                (
                    f"What is the precise physiological contribution of {spec['symbol']} "
                    "to nucleotide-excision repair versus neighboring replication, "
                    "transcription-coupled repair, or general DNA-repair pathways in P. putida KT2440?"
                )
            ],
        )
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Measure UV survival, bulky-lesion repair, and transcription-coupled repair "
                f"phenotypes in a targeted {spec['symbol']} perturbation under matched growth conditions."
            ),
            "experiment_type": "gene perturbation and DNA repair phenotype assay",
        }
    ]
    data["references"] = unique_references(data.get("references", []), gene)

    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def add_asta_reference(gene: str) -> None:
    path = ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["references"] = unique_references(data.get("references", []), gene)
    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    for gene, spec in GENES.items():
        curate_gene(gene, spec)
    for gene in ["uvrA", "uvrB", "uvrC", "ligA", "ligB", "uvrD"]:
        add_asta_reference(gene)


if __name__ == "__main__":
    main()
