#!/usr/bin/env python3
"""First-pass curation for KEGG ppu03410 base-excision repair stubs."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path("genes") / SPECIES
OVERLAP_GENES = ["polA", "recJ", "ligA", "ligB"]


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000003": "Gene Ontology annotation based on Enzyme Commission mapping",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on on inter-ontology links",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


GENES: dict[str, dict] = {
    "tag": {
        "symbol": "tag",
        "description": (
            "tag (PP_0062) encodes DNA-3-methyladenine glycosylase I, a small "
            "DNA glycosylase that initiates base-excision repair by hydrolyzing "
            "the N-glycosidic bond at 3-methyladenine and related alkylated bases."
        ),
        "core": {
            "description": "DNA-3-methyladenine glycosylase initiating alkyl-base removal in base-excision repair.",
            "molecular_function": {
                "id": "GO:0008725",
                "label": "DNA-3-methyladenine glycosylase activity",
            },
            "directly_involved_in": [{"id": "GO:0006284", "label": "base-excision repair"}],
        },
        "decisions": {
            "GO:0003824": ("MARK_AS_OVER_ANNOTATED", "generic catalytic activity is uninformative for a specific DNA glycosylase"),
            "GO:0006281": ("ACCEPT", "DNA repair is correct for a DNA alkylation-damage glycosylase"),
            "GO:0006284": ("ACCEPT", "base-excision repair is the pathway-defining process for Tag glycosylase"),
            "GO:0008725": ("ACCEPT", "DNA-3-methyladenine glycosylase activity is the specific Tag molecular function"),
        },
    },
    "mutY": {
        "symbol": "mutY",
        "description": (
            "mutY (PP_0286) encodes adenine DNA glycosylase, a MutY-family "
            "base-excision repair enzyme that recognizes adenine mispaired with "
            "oxidized guanine lesions and removes the adenine base to prevent "
            "G:C to T:A transversion mutations."
        ),
        "core": {
            "description": "MutY adenine DNA glycosylase acting on adenine/guanine and oxidized-purine mispairs in BER.",
            "molecular_function": {
                "id": "GO:0000701",
                "label": "purine-specific mismatch base pair DNA N-glycosylase activity",
            },
            "directly_involved_in": [{"id": "GO:0006284", "label": "base-excision repair"}],
        },
        "decisions": {
            "GO:0000701": ("ACCEPT", "purine-specific mismatch base-pair DNA N-glycosylase activity is the specific MutY catalytic function"),
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is necessary context but less specific than mismatch-base glycosylase activity"),
            "GO:0003824": ("MARK_AS_OVER_ANNOTATED", "generic catalytic activity is uninformative for MutY"),
            "GO:0006281": ("ACCEPT", "DNA repair is correct for MutY"),
            "GO:0006284": ("ACCEPT", "MutY is a base-excision repair glycosylase"),
            "GO:0006298": ("KEEP_AS_NON_CORE", "MutY works on mispaired bases but the more precise pathway here is base-excision repair"),
            "GO:0006950": ("MARK_AS_OVER_ANNOTATED", "response to stress is too broad for this DNA glycosylase"),
            "GO:0016798": ("KEEP_AS_NON_CORE", "hydrolase activity on glycosyl bonds is a broad parent of DNA N-glycosylase activity"),
            "GO:0019104": ("KEEP_AS_NON_CORE", "DNA N-glycosylase activity is correct but less specific than the MutY mismatch-base term"),
            "GO:0032357": ("ACCEPT", "oxidized purine DNA binding fits MutY recognition of adenine opposite oxidized guanine lesions"),
            "GO:0034039": (
                "MODIFY",
                "this term implies excision of 8-oxo-7,8-dihydroguanine itself; MutY primarily removes adenine from oxidized-purine mispairs",
                [{"id": "GO:0000701", "label": "purine-specific mismatch base pair DNA N-glycosylase activity"}],
            ),
            "GO:0035485": ("ACCEPT", "adenine/guanine mispair binding is the MutY substrate-recognition context"),
            "GO:0046872": (
                "MODIFY",
                "generic metal ion binding should be replaced by the more specific iron-sulfur cluster term already present in GOA",
                [{"id": "GO:0051539", "label": "4 iron, 4 sulfur cluster binding"}],
            ),
            "GO:0051539": ("ACCEPT", "4 iron, 4 sulfur cluster binding is expected for MutY-family glycosylases"),
        },
    },
    "PP_0705": {
        "symbol": "PP_0705",
        "description": (
            "PP_0705 encodes DNA-3-methyladenine glycosylase II, an AlkA-family "
            "alkylbase DNA N-glycosylase that removes alkylated bases to create "
            "AP sites for downstream base-excision repair."
        ),
        "core": {
            "description": "AlkA-family alkylbase DNA N-glycosylase initiating AP-site formation during alkylation-damage BER.",
            "molecular_function": {
                "id": "GO:0003905",
                "label": "alkylbase DNA N-glycosylase activity",
            },
            "directly_involved_in": [
                {"id": "GO:0006285", "label": "base-excision repair, AP site formation"},
                {"id": "GO:0006307", "label": "DNA alkylation repair"},
            ],
        },
        "decisions": {
            "GO:0003824": ("MARK_AS_OVER_ANNOTATED", "generic catalytic activity is uninformative for an alkylbase DNA glycosylase"),
            "GO:0003905": ("ACCEPT", "alkylbase DNA N-glycosylase activity is the core AlkA-family molecular function"),
            "GO:0006281": ("ACCEPT", "DNA repair is correct for PP_0705"),
            "GO:0006284": ("ACCEPT", "base-excision repair is correct for an alkylbase glycosylase"),
            "GO:0006285": ("ACCEPT", "AP-site formation is the immediate BER consequence of glycosylase base removal"),
            "GO:0006307": ("ACCEPT", "DNA alkylation repair fits the DNA-3-methyladenine glycosylase II assignment"),
            "GO:0008725": ("ACCEPT", "DNA-3-methyladenine glycosylase activity is supported for this AlkA-family enzyme"),
            "GO:0032131": ("ACCEPT", "alkylated DNA binding is the expected substrate-recognition context"),
            "GO:0032993": ("KEEP_AS_NON_CORE", "protein-DNA complex is plausible substrate-bound context but not a stable pathway component"),
            "GO:0043916": ("ACCEPT", "DNA-7-methylguanine glycosylase activity is compatible with AlkA-family alkylbase specificity"),
        },
    },
    "nth": {
        "symbol": "nth",
        "description": (
            "nth (PP_1092) encodes endonuclease III, an Nth/MutY-family DNA "
            "glycosylase/AP lyase that removes oxidized pyrimidine lesions and "
            "processes the resulting abasic sites during base-excision repair."
        ),
        "core": {
            "description": "Endonuclease III DNA glycosylase/AP-lyase for oxidized-base removal and AP-site processing in BER.",
            "molecular_function": {
                "id": "GO:0140078",
                "label": "class I DNA-(apurinic or apyrimidinic site) endonuclease activity",
            },
            "directly_involved_in": [{"id": "GO:0006285", "label": "base-excision repair, AP site formation"}],
        },
        "decisions": {
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected for Nth but less specific than its glycosylase/AP-lyase activities"),
            "GO:0003824": ("MARK_AS_OVER_ANNOTATED", "generic catalytic activity is uninformative for endonuclease III"),
            "GO:0003906": ("ACCEPT", "AP-site endonuclease/lyase activity is supported for Nth-family endonuclease III"),
            "GO:0006281": ("ACCEPT", "DNA repair is correct for Nth"),
            "GO:0006284": ("ACCEPT", "base-excision repair is the pathway-defining Nth process"),
            "GO:0006285": ("ACCEPT", "Nth glycosylase activity creates AP-site repair intermediates"),
            "GO:0019104": ("ACCEPT", "DNA N-glycosylase activity is part of the bifunctional Nth enzyme function"),
            "GO:0051539": ("ACCEPT", "4 iron, 4 sulfur cluster binding fits endonuclease III family metadata"),
            "GO:0140078": ("ACCEPT", "class I AP-site endonuclease activity is the most specific current Nth AP-site processing term"),
        },
    },
    "ung": {
        "symbol": "ung",
        "description": (
            "ung (PP_1413) encodes uracil-DNA glycosylase, a cytoplasmic BER "
            "enzyme that excises uracil from DNA after cytosine deamination or "
            "dUMP misincorporation, generating AP sites for repair."
        ),
        "core": {
            "description": "Cytoplasmic uracil-DNA glycosylase initiating BER of deaminated or misincorporated uracil bases.",
            "molecular_function": {"id": "GO:0004844", "label": "uracil DNA N-glycosylase activity"},
            "directly_involved_in": [
                {
                    "id": "GO:0097510",
                    "label": "base-excision repair, AP site formation via deaminated base removal",
                }
            ],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
        },
        "decisions": {
            "GO:0004844": ("ACCEPT", "uracil DNA N-glycosylase activity is the core Ung molecular function"),
            "GO:0005737": ("ACCEPT", "cytoplasm is the expected location for a bacterial DNA repair enzyme"),
            "GO:0006281": ("ACCEPT", "DNA repair is correct for Ung"),
            "GO:0006284": ("ACCEPT", "base-excision repair is correct for uracil-DNA glycosylase"),
            "GO:0016799": ("KEEP_AS_NON_CORE", "hydrolyzing N-glycosyl compounds is a broad parent of uracil DNA N-glycosylase activity"),
            "GO:0097510": ("ACCEPT", "deaminated-base AP-site formation is the precise BER process for Ung"),
        },
    },
    "PP_2707": {
        "symbol": "PP_2707",
        "description": (
            "PP_2707 encodes an ExoIII-like AP/ExoA-family nuclease with "
            "endonuclease/exonuclease-phosphatase domains. The current "
            "annotations support a cytoplasmic magnesium-dependent DNA repair "
            "nuclease likely acting on BER-associated AP-site or DNA-end substrates."
        ),
        "core": {
            "description": "ExoIII-like AP/ExoA-family DNA repair nuclease of unresolved BER-paralog specificity.",
            "molecular_function": {
                "id": "GO:0008311",
                "label": "double-stranded DNA 3'-5' DNA exonuclease activity",
            },
            "directly_involved_in": [{"id": "GO:0006281", "label": "DNA repair"}],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
        },
        "decisions": {
            "GO:0000287": ("KEEP_AS_NON_CORE", "magnesium ion binding is plausible cofactor context for this nuclease"),
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected but less informative than nuclease activity"),
            "GO:0003824": ("MARK_AS_OVER_ANNOTATED", "generic catalytic activity is uninformative for an AP/ExoA-family nuclease"),
            "GO:0004518": ("KEEP_AS_NON_CORE", "nuclease activity is correct but less specific than the DNA exonuclease term"),
            "GO:0004519": ("ACCEPT", "endonuclease activity is supported by the AP/ExoA-family annotation"),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for a bacterial DNA repair nuclease"),
            "GO:0006281": ("ACCEPT", "DNA repair is supported for the ExoIII-like AP/ExoA-family protein"),
            "GO:0008311": ("ACCEPT", "double-stranded DNA 3'-5' exonuclease activity is the most specific current GOA molecular function"),
        },
        "questions": [
            "Does PP_2707 provide in vivo AP endonuclease activity in base-excision repair, or is its physiological substrate distinct from xthA and PP_5292?"
        ],
    },
    "xthA": {
        "symbol": "xthA",
        "description": (
            "xthA (PP_2890) encodes an Exodeoxyribonuclease III/AP endonuclease "
            "VI-family DNA repair nuclease with AP endonuclease and 3'-5' "
            "double-stranded DNA exonuclease annotations. It is a plausible BER "
            "AP-site processing enzyme in KT2440."
        ),
        "core": {
            "description": "XthA ExoIII/AP-endonuclease-family nuclease for DNA repair and likely AP-site processing.",
            "molecular_function": {
                "id": "GO:0008311",
                "label": "double-stranded DNA 3'-5' DNA exonuclease activity",
            },
            "directly_involved_in": [{"id": "GO:0006281", "label": "DNA repair"}],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
        },
        "decisions": {
            "GO:0000287": ("KEEP_AS_NON_CORE", "magnesium ion binding is plausible cofactor context for ExoIII/AP endonuclease activity"),
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected but less informative than nuclease activity"),
            "GO:0003824": ("MARK_AS_OVER_ANNOTATED", "generic catalytic activity is uninformative for XthA"),
            "GO:0004518": ("KEEP_AS_NON_CORE", "nuclease activity is correct but less specific than the DNA exonuclease/endonuclease terms"),
            "GO:0004519": ("ACCEPT", "endonuclease activity is supported for XthA/AP endonuclease VI"),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for a bacterial DNA repair nuclease"),
            "GO:0006281": ("ACCEPT", "DNA repair is correct for XthA"),
            "GO:0008311": ("ACCEPT", "double-stranded DNA 3'-5' exonuclease activity is supported for XthA"),
        },
        "questions": [
            "Which of the KT2440 ExoIII-like paralogs, including xthA, is the dominant AP endonuclease during alkylation- or oxidation-induced base-excision repair?"
        ],
    },
    "PP_4812": {
        "symbol": "PP_4812",
        "description": (
            "PP_4812 encodes a putative 3-methyladenine DNA glycosylase of the "
            "MPG family. Its current annotations support alkylbase DNA "
            "N-glycosylase activity and base-excision repair, but the exact "
            "alkylated-base substrate range remains unresolved in KT2440."
        ),
        "core": {
            "description": "MPG-family putative alkylbase DNA N-glycosylase acting in base-excision repair.",
            "molecular_function": {
                "id": "GO:0003905",
                "label": "alkylbase DNA N-glycosylase activity",
            },
            "directly_involved_in": [{"id": "GO:0006284", "label": "base-excision repair"}],
        },
        "decisions": {
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected but less specific than glycosylase activity"),
            "GO:0003824": ("MARK_AS_OVER_ANNOTATED", "generic catalytic activity is uninformative for a putative DNA glycosylase"),
            "GO:0003905": ("ACCEPT", "alkylbase DNA N-glycosylase activity is the most specific current molecular function"),
            "GO:0006281": ("ACCEPT", "DNA repair is correct for this putative alkylbase glycosylase"),
            "GO:0006284": ("ACCEPT", "base-excision repair is supported for the MPG-family glycosylase"),
            "GO:0019104": ("KEEP_AS_NON_CORE", "DNA N-glycosylase activity is correct but broader than alkylbase DNA N-glycosylase activity"),
        },
        "questions": [
            "What alkylated bases are removed by PP_4812, and how does its substrate range differ from Tag and PP_0705?"
        ],
    },
    "mutM": {
        "symbol": "mutM",
        "description": (
            "mutM (PP_5125, fpg) encodes formamidopyrimidine-DNA glycosylase, a "
            "bifunctional BER enzyme that recognizes oxidized purine lesions, "
            "excises damaged bases such as 8-oxo-7,8-dihydroguanine or Fapy "
            "lesions, and performs AP-lyase cleavage during repair."
        ),
        "core": {
            "description": "Fpg/MutM oxidized-purine DNA glycosylase/AP-lyase for oxidative-damage base-excision repair.",
            "molecular_function": {
                "id": "GO:0008534",
                "label": "oxidized purine nucleobase lesion DNA N-glycosylase activity",
            },
            "directly_involved_in": [{"id": "GO:0006284", "label": "base-excision repair"}],
        },
        "decisions": {
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for MutM"),
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected but less specific than damaged-DNA binding and glycosylase activity"),
            "GO:0003684": ("ACCEPT", "damaged DNA binding fits MutM recognition of oxidized bases"),
            "GO:0003906": ("ACCEPT", "AP-site endonuclease/lyase activity is part of the bifunctional MutM repair mechanism"),
            "GO:0006281": ("ACCEPT", "DNA repair is correct for MutM"),
            "GO:0006284": ("ACCEPT", "base-excision repair is the pathway-defining MutM process"),
            "GO:0008270": ("ACCEPT", "zinc ion binding is supported by the Fpg zinc-finger family context"),
            "GO:0008534": ("ACCEPT", "oxidized purine lesion DNA N-glycosylase activity is the core MutM activity"),
            "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "generic hydrolase activity is uninformative for a bifunctional DNA glycosylase/AP lyase"),
            "GO:0016799": ("KEEP_AS_NON_CORE", "N-glycosyl hydrolase activity is a broad parent of the specific MutM glycosylase activity"),
            "GO:0019104": ("KEEP_AS_NON_CORE", "DNA N-glycosylase activity is correct but less specific than oxidized-purine lesion activity"),
            "GO:0034039": ("ACCEPT", "8-oxo-7,8-dihydroguanine DNA N-glycosylase activity is compatible with MutM/Fpg substrate specificity"),
            "GO:0140078": ("ACCEPT", "class I AP-site endonuclease activity is supported by the MutM AP-lyase annotation"),
        },
    },
    "PP_5292": {
        "symbol": "PP_5292",
        "description": (
            "PP_5292 encodes an ExoIII-like AP/ExoA-family nuclease despite a "
            "generic submitted name. Domain, family, and GOA evidence support a "
            "cytoplasmic magnesium-dependent DNA repair nuclease with "
            "double-stranded DNA 3'-5' exonuclease activity."
        ),
        "core": {
            "description": "ExoIII-like AP/ExoA-family DNA repair nuclease; submitted product name is non-specific.",
            "molecular_function": {
                "id": "GO:0008311",
                "label": "double-stranded DNA 3'-5' DNA exonuclease activity",
            },
            "directly_involved_in": [{"id": "GO:0006281", "label": "DNA repair"}],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
        },
        "decisions": {
            "GO:0000287": ("KEEP_AS_NON_CORE", "magnesium ion binding is plausible cofactor context for this nuclease"),
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected but less informative than nuclease activity"),
            "GO:0003824": ("MARK_AS_OVER_ANNOTATED", "generic catalytic activity is uninformative for an ExoIII-like nuclease"),
            "GO:0004518": ("KEEP_AS_NON_CORE", "nuclease activity is correct but less specific than the DNA exonuclease term"),
            "GO:0004519": ("ACCEPT", "endonuclease activity is supported by the AP/ExoA-family annotation"),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for a bacterial DNA repair nuclease"),
            "GO:0006281": ("ACCEPT", "DNA repair is supported by ExoIII-like family and GOA evidence"),
            "GO:0008311": ("ACCEPT", "double-stranded DNA 3'-5' exonuclease activity is the most specific current GOA molecular function"),
        },
        "questions": [
            "Is PP_5292 a functional AP endonuclease/exonuclease in BER despite the generic catabolite-repression product name?"
        ],
    },
}


def support_for(term_id: str, label: str, gene: str) -> dict:
    return {
        "reference_id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
        "supporting_text": f"{term_id}\t{label}",
    }


def asta_support(gene: str) -> dict:
    path = ROOT / gene / f"{gene}-deep-research-asta.md"
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("- **Protein Description:** "):
            return {
                "reference_id": f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md",
                "supporting_text": line,
            }
    raise ValueError(f"No Asta protein-description line found for {gene}")


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
                    "statement": "Asta retrieval used as fast gene-level context; no unsupported hypotheses were imported."
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
        summary = f"{label} is supported for {gene} in the ppu03410 first-pass curation."
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
        "supported_by": [support_for(term_id, label, gene), asta_support(gene)],
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
        decision = decisions.get(term["id"], ("KEEP_AS_NON_CORE", "not part of the primary ppu03410 first-pass interpretation"))
        ann["review"] = curated_review(gene, term["id"], term["label"], decision)

    core = dict(spec["core"])
    core["supported_by"] = core_supported_by(core, data.get("existing_annotations", []), gene)
    data["core_functions"] = [core]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {"question": question}
        for question in spec.get(
            "questions",
            [
                (
                    f"What is the precise substrate specificity and physiological contribution of "
                    f"{spec['symbol']} within P. putida KT2440 base-excision repair?"
                )
            ],
        )
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Measure survival, lesion repair, and mutation spectra after methylating-agent and oxidative-DNA-damage "
                f"challenge in a targeted {spec['symbol']} perturbation."
            ),
            "experiment_type": "gene perturbation and DNA repair phenotype assay",
        }
    ]
    data["references"] = unique_references(data.get("references", []), gene)

    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def add_asta_support_to_existing_gene(gene: str) -> None:
    path = ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    support = asta_support(gene)
    for ann in data.get("existing_annotations", []):
        review = ann.get("review") or {}
        supported_by = review.setdefault("supported_by", [])
        if not any(item.get("reference_id") == support["reference_id"] for item in supported_by):
            supported_by.append(support)
        if gene == "ligA" and ann.get("term", {}).get("id") == "GO:0005829":
            review["summary"] = "cytosol is supported for ligA in the ppu03410 first-pass overlap cleanup."
            review["action"] = "ACCEPT"
            review["reason"] = "cytosol is appropriate cellular context for a bacterial DNA ligase and is used in the core function"
        ann["review"] = review
    data["references"] = unique_references(data.get("references", []), gene)
    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    for gene, spec in GENES.items():
        curate_gene(gene, spec)
    for gene in OVERLAP_GENES:
        add_asta_support_to_existing_gene(gene)


if __name__ == "__main__":
    main()
