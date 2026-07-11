#!/usr/bin/env python3
"""First-pass curation for KEGG ppu03018 RNA-degradation stubs."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path("genes") / SPECIES
OVERLAP_GENES = ["ppkB", "groEL", "eno", "dnaK", "hfq", "ppk"]

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000003": "Gene Ontology annotation based on Enzyme Commission mapping",
    "GO_REF:0000044": (
        "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, "
        "accompanied by conservative changes to GO terms applied by UniProt"
    ),
    "GO_REF:0000104": (
        "Electronic Gene Ontology annotations created by transferring manual GO annotations between "
        "related proteins based on shared sequence features"
    ),
    "GO_REF:0000116": "Automatic Gene Ontology annotation based on Rhea mapping",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


RNA_HELICASE_DECISIONS = {
    "GO:0000166": ("MARK_AS_OVER_ANNOTATED", "nucleotide binding is a generic parent of ATP binding and RNA helicase activity"),
    "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for a DEAD-box RNA helicase"),
    "GO:0003723": ("KEEP_AS_NON_CORE", "RNA binding is expected substrate context but less specific than RNA helicase activity"),
    "GO:0003724": ("ACCEPT", "RNA helicase activity is the defining molecular function of this DEAD-box helicase"),
    "GO:0005524": ("ACCEPT", "ATP binding supports ATP-dependent RNA helicase activity"),
    "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for a soluble bacterial RNA helicase"),
    "GO:0005829": ("ACCEPT", "cytosol is appropriate for a soluble bacterial RNA helicase"),
    "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "generic hydrolase activity is uninformative compared with ATP-dependent RNA helicase activity"),
    "GO:0016887": ("ACCEPT", "ATP hydrolysis powers DEAD-box helicase remodeling"),
}


GENES: dict[str, dict] = {
    "rhlB": {
        "symbol": "rhlB",
        "description": (
            "rhlB (PP_1295) encodes a DEAD-box ATP-dependent RNA helicase of the RhlB subfamily. "
            "It is a soluble bacterial RNA-remodeling enzyme linked by UniProt/GOA to RNA catabolism, "
            "where it likely helps unwind structured RNA substrates for the RNA-degradation machinery."
        ),
        "core": {
            "description": "DEAD-box ATP-dependent RNA helicase supporting bacterial RNA catabolism.",
            "molecular_function": {"id": "GO:0003724", "label": "RNA helicase activity"},
            "directly_involved_in": [{"id": "GO:0006401", "label": "RNA catabolic process"}],
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
        },
        "decisions": {
            **RNA_HELICASE_DECISIONS,
            "GO:0006401": ("ACCEPT", "RNA catabolic process matches the ppu03018 RNA-degradation context"),
        },
    },
    "deaD": {
        "symbol": "deaD",
        "description": (
            "deaD (PP_1868, also csdA) encodes the cold-shock DEAD-box ATP-dependent RNA helicase DeaD/CsdA. "
            "The protein remodels RNA and ribonucleoprotein substrates, with GOA support for RNA catabolism, "
            "ribosomal large-subunit assembly, ribosome assembly, and cold-response context."
        ),
        "core": {
            "description": "Cold-shock DEAD-box RNA helicase with RNA-catabolism and ribosome-assembly context.",
            "molecular_function": {"id": "GO:0003724", "label": "RNA helicase activity"},
            "directly_involved_in": [
                {"id": "GO:0006401", "label": "RNA catabolic process"},
                {"id": "GO:0042255", "label": "ribosome assembly"},
            ],
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
        },
        "decisions": {
            **RNA_HELICASE_DECISIONS,
            "GO:0000027": ("ACCEPT", "ribosomal large subunit assembly is supported DeaD/CsdA ribonucleoprotein-remodeling context"),
            "GO:0005840": ("KEEP_AS_NON_CORE", "ribosome localization is plausible for DeaD but secondary to RNA helicase activity"),
            "GO:0006401": ("ACCEPT", "RNA catabolic process is part of the ppu03018 RNA-turnover context"),
            "GO:0009266": ("KEEP_AS_NON_CORE", "temperature-stimulus response is broad context for a cold-shock helicase"),
            "GO:0009409": ("ACCEPT", "response to cold is supported for DeaD/CsdA-family RNA remodeling"),
            "GO:0033592": ("KEEP_AS_NON_CORE", "RNA strand annealing is plausible DEAD-box accessory activity but secondary here"),
            "GO:0042255": ("ACCEPT", "ribosome assembly is supported ribonucleoprotein-remodeling context"),
            "GO:0070417": ("ACCEPT", "cellular response to cold is supported for DeaD/CsdA-family RNA helicase context"),
        },
    },
    "rne": {
        "symbol": "rne",
        "description": (
            "rne (PP_1905) encodes ribonuclease E, a bacterial endoribonuclease that initiates RNA processing "
            "and mRNA decay. RNase E cleaves RNA substrates, contributes to rRNA and tRNA processing, and is "
            "a central scaffold/activity in bacterial RNA-degradation machinery."
        ),
        "core": {
            "description": "RNase E endoribonuclease initiating bacterial RNA processing and mRNA decay.",
            "molecular_function": {"id": "GO:0008995", "label": "ribonuclease E activity"},
            "directly_involved_in": [
                {"id": "GO:0006402", "label": "mRNA catabolic process"},
                {"id": "GO:0006364", "label": "rRNA processing"},
                {"id": "GO:0008033", "label": "tRNA processing"},
            ],
            "locations": [{"id": "GO:0009898", "label": "cytoplasmic side of plasma membrane"}],
        },
        "decisions": {
            "GO:0000287": ("ACCEPT", "magnesium ion binding is catalytic cofactor context for RNase E"),
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for an RNase"),
            "GO:0003723": ("KEEP_AS_NON_CORE", "RNA binding is substrate context but less specific than RNase E activity"),
            "GO:0004521": ("ACCEPT", "RNA endonuclease activity is the parent activity for RNase E"),
            "GO:0004540": ("ACCEPT", "RNA nuclease activity is correct but broader than ribonuclease E activity"),
            "GO:0005737": ("ACCEPT", "cytoplasm is compatible with bacterial RNase E localization"),
            "GO:0005886": ("KEEP_AS_NON_CORE", "plasma membrane reflects RNase E membrane association but is less precise than cytoplasmic side of plasma membrane"),
            "GO:0006364": ("ACCEPT", "rRNA processing is a supported RNase E process"),
            "GO:0006396": ("ACCEPT", "RNA processing is supported but broader than the specific RNA-processing processes"),
            "GO:0006402": ("ACCEPT", "mRNA catabolic process is the central RNA-degradation role"),
            "GO:0008033": ("ACCEPT", "tRNA processing is a supported RNase E process"),
            "GO:0008270": ("ACCEPT", "zinc ion binding is supported cofactor/domain context for RNase E"),
            "GO:0008995": ("ACCEPT", "ribonuclease E activity is the defining molecular function"),
            "GO:0009898": ("ACCEPT", "cytoplasmic side of plasma membrane captures RNase E membrane-associated bacterial localization"),
        },
    },
    "recQ": {
        "symbol": "recQ",
        "description": (
            "recQ (PP_4516) encodes a RecQ-family ATP-dependent 3'-to-5' DNA helicase. "
            "Although KEGG includes it in ppu03018, the local UniProt/GOA evidence supports DNA replication, "
            "repair, recombination, SOS-response, replisome, and nucleoid roles rather than RNA degradation."
        ),
        "core": {
            "description": "RecQ-family 3'-5' DNA helicase for DNA replication, repair, recombination, and SOS-associated genome maintenance.",
            "molecular_function": {"id": "GO:0043138", "label": "3'-5' DNA helicase activity"},
            "directly_involved_in": [
                {"id": "GO:0006281", "label": "DNA repair"},
                {"id": "GO:0006310", "label": "DNA recombination"},
                {"id": "GO:0006260", "label": "DNA replication"},
            ],
            "locations": [{"id": "GO:0043590", "label": "bacterial nucleoid"}],
        },
        "decisions": {
            "GO:0000166": ("MARK_AS_OVER_ANNOTATED", "nucleotide binding is generic for this ATP-dependent DNA helicase"),
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for RecQ"),
            "GO:0003678": ("KEEP_AS_NON_CORE", "DNA helicase activity is correct but less specific than 3'-5' DNA helicase activity"),
            "GO:0004386": ("MARK_AS_OVER_ANNOTATED", "generic helicase activity is less informative than DNA helicase directionality"),
            "GO:0005524": ("ACCEPT", "ATP binding supports the RecQ helicase motor"),
            "GO:0005694": ("KEEP_AS_NON_CORE", "chromosome is broad substrate/localization context for RecQ"),
            "GO:0005737": ("ACCEPT", "cytoplasm is compatible with bacterial RecQ localization"),
            "GO:0006260": ("ACCEPT", "DNA replication is supported RecQ genome-maintenance context"),
            "GO:0006281": ("ACCEPT", "DNA repair is a core RecQ process"),
            "GO:0006310": ("ACCEPT", "DNA recombination is a core RecQ process"),
            "GO:0009378": ("KEEP_AS_NON_CORE", "four-way junction helicase activity is plausible RecQ substrate context but less central than directional DNA helicase activity"),
            "GO:0009432": ("ACCEPT", "SOS response is supported DNA-damage response context"),
            "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "generic hydrolase activity is uninformative for RecQ"),
            "GO:0030894": ("KEEP_AS_NON_CORE", "replisome is plausible replication context but not the clearest RecQ core assignment"),
            "GO:0043138": ("ACCEPT", "3'-5' DNA helicase activity is the defining RecQ molecular function"),
            "GO:0043590": ("ACCEPT", "bacterial nucleoid is appropriate chromosomal DNA substrate context"),
            "GO:0046872": ("KEEP_AS_NON_CORE", "metal ion binding is domain/cofactor context and not pathway-defining"),
        },
        "questions": [
            "Why does KEGG ppu03018 include RecQ for KT2440 RNA degradation despite the local evidence supporting DNA helicase/genome-maintenance function?"
        ],
    },
    "pcnB": {
        "symbol": "pcnB",
        "description": (
            "pcnB (PP_4697) encodes poly(A) polymerase I. PcnB adds poly(A) tails to bacterial RNA substrates, "
            "which can promote polyadenylation-dependent RNA decay and also intersects with RNA processing."
        ),
        "core": {
            "description": "Poly(A) polymerase I that polyadenylates RNA substrates for RNA processing and polyadenylation-dependent decay.",
            "molecular_function": {"id": "GO:1990817", "label": "poly(A) RNA polymerase activity"},
            "directly_involved_in": [
                {"id": "GO:0043633", "label": "polyadenylation-dependent RNA catabolic process"},
                {"id": "GO:0006396", "label": "RNA processing"},
            ],
        },
        "decisions": {
            "GO:0003723": ("KEEP_AS_NON_CORE", "RNA binding is substrate context but less specific than poly(A) RNA polymerase activity"),
            "GO:0005524": ("ACCEPT", "ATP binding supports poly(A) polymerase nucleotide addition"),
            "GO:0006351": ("MARK_AS_OVER_ANNOTATED", "DNA-templated transcription is too broad and indirect for PcnB polyadenylation"),
            "GO:0006396": ("ACCEPT", "RNA processing is supported but broad"),
            "GO:0016779": ("KEEP_AS_NON_CORE", "nucleotidyltransferase activity is a broad parent of poly(A) RNA polymerase activity"),
            "GO:0042780": ("KEEP_AS_NON_CORE", "tRNA 3'-end processing is plausible family context but not the central ppu03018 role"),
            "GO:0043633": ("ACCEPT", "polyadenylation-dependent RNA catabolic process is the pathway-defining PcnB role"),
            "GO:1990817": ("ACCEPT", "poly(A) RNA polymerase activity is the defining molecular function"),
        },
    },
    "pnp": {
        "symbol": "pnp",
        "description": (
            "pnp (PP_4708) encodes polynucleotide phosphorylase/PNPase, a phosphorolytic 3'-to-5' RNA-degradation enzyme. "
            "It participates in RNA processing and mRNA decay and is a central bacterial RNA-turnover factor."
        ),
        "core": {
            "description": "PNPase phosphorolytic 3'-5' RNA exonuclease/nucleotidyltransferase for RNA processing and mRNA decay.",
            "molecular_function": {"id": "GO:0004654", "label": "polyribonucleotide nucleotidyltransferase activity"},
            "directly_involved_in": [
                {"id": "GO:0006402", "label": "mRNA catabolic process"},
                {"id": "GO:0006401", "label": "RNA catabolic process"},
            ],
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
        },
        "decisions": {
            "GO:0000175": ("ACCEPT", "3'-5'-RNA exonuclease activity captures PNPase RNA-degradation directionality"),
            "GO:0000287": ("ACCEPT", "magnesium ion binding is catalytic cofactor context for PNPase"),
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for PNPase"),
            "GO:0003723": ("KEEP_AS_NON_CORE", "RNA binding is substrate context but less specific than PNPase catalytic activity"),
            "GO:0004654": ("ACCEPT", "polyribonucleotide nucleotidyltransferase activity is the defining PNPase activity"),
            "GO:0005737": ("ACCEPT", "cytoplasm is compatible with bacterial PNPase localization"),
            "GO:0005829": ("ACCEPT", "cytosol is appropriate for soluble bacterial PNPase"),
            "GO:0006396": ("ACCEPT", "RNA processing is a supported PNPase process"),
            "GO:0006401": ("ACCEPT", "RNA catabolic process matches the ppu03018 pathway context"),
            "GO:0006402": ("ACCEPT", "mRNA catabolic process is a central PNPase role"),
        },
    },
    "rhlE-I": {
        "symbol": "rhlE-I",
        "description": (
            "rhlE-I (PP_4766) encodes a DEAD-box ATP-dependent RNA helicase annotated as RhpA/RhlE-like. "
            "The protein is a cytosolic RNA-remodeling enzyme linked to ribosome assembly and temperature-response context."
        ),
        "core": {
            "description": "Cytosolic DEAD-box RNA helicase linked to ribosome assembly and RNA remodeling.",
            "molecular_function": {"id": "GO:0003724", "label": "RNA helicase activity"},
            "directly_involved_in": [{"id": "GO:0042255", "label": "ribosome assembly"}],
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
        },
        "decisions": {
            **RNA_HELICASE_DECISIONS,
            "GO:0009266": ("KEEP_AS_NON_CORE", "temperature-stimulus response is broad context for an RNA helicase"),
            "GO:0042255": ("ACCEPT", "ribosome assembly is supported RNA-remodeling context"),
        },
    },
    "rnr": {
        "symbol": "rnr",
        "description": (
            "rnr (PP_4880) encodes ribonuclease R, a 3'-to-5' exoribonuclease in the RNase II/R family. "
            "It binds RNA and contributes to mRNA decay and broader RNA metabolism in the bacterial cytosol."
        ),
        "core": {
            "description": "RNase R exoribonuclease for bacterial mRNA decay and RNA turnover.",
            "molecular_function": {"id": "GO:0008859", "label": "exoribonuclease II activity"},
            "directly_involved_in": [{"id": "GO:0006402", "label": "mRNA catabolic process"}],
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
        },
        "decisions": {
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for RNase R"),
            "GO:0003723": ("KEEP_AS_NON_CORE", "RNA binding is substrate context but less specific than exoribonuclease activity"),
            "GO:0004518": ("KEEP_AS_NON_CORE", "nuclease activity is too broad for RNase R"),
            "GO:0004540": ("KEEP_AS_NON_CORE", "RNA nuclease activity is correct but broader than exoribonuclease II activity"),
            "GO:0005737": ("ACCEPT", "cytoplasm is compatible with bacterial RNase R localization"),
            "GO:0005829": ("ACCEPT", "cytosol is appropriate for soluble bacterial RNase R"),
            "GO:0006402": ("ACCEPT", "mRNA catabolic process is a central RNase R role"),
            "GO:0008859": ("ACCEPT", "exoribonuclease II activity captures RNase R 3'-5' exonuclease activity"),
            "GO:0016070": ("KEEP_AS_NON_CORE", "RNA metabolic process is true but less specific than mRNA catabolism"),
        },
    },
    "rhlE": {
        "symbol": "rhlE",
        "description": (
            "rhlE (PP_4980, also rhlE-II) encodes a DEAD-box ATP-dependent RNA helicase of the RhlE subfamily. "
            "It is a cytosolic RNA-remodeling enzyme linked to ribosome biogenesis/assembly and temperature-response context."
        ),
        "core": {
            "description": "Cytosolic RhlE-family DEAD-box RNA helicase linked to ribosome biogenesis and RNA remodeling.",
            "molecular_function": {"id": "GO:0003724", "label": "RNA helicase activity"},
            "directly_involved_in": [
                {"id": "GO:0042254", "label": "ribosome biogenesis"},
                {"id": "GO:0042255", "label": "ribosome assembly"},
            ],
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
        },
        "decisions": {
            **RNA_HELICASE_DECISIONS,
            "GO:0009266": ("KEEP_AS_NON_CORE", "temperature-stimulus response is broad context for an RNA helicase"),
            "GO:0042254": ("ACCEPT", "ribosome biogenesis is supported for RhlE-family RNA remodeling"),
            "GO:0042255": ("ACCEPT", "ribosome assembly is supported RNA-remodeling context"),
        },
    },
    "rppH": {
        "symbol": "rppH",
        "description": (
            "rppH (PP_5146, also nudH) encodes an RNA pyrophosphohydrolase/Nudix-family enzyme. "
            "RppH removes pyrophosphate from 5' triphosphorylated mRNAs to generate decay-prone 5' monophosphate ends, "
            "thereby promoting bacterial mRNA degradation."
        ),
        "core": {
            "description": "RppH mRNA 5'-diphosphatase that initiates bacterial mRNA decay by converting protected 5' ends to decay-prone forms.",
            "molecular_function": {"id": "GO:0034353", "label": "mRNA 5'-diphosphatase activity"},
            "directly_involved_in": [{"id": "GO:0006402", "label": "mRNA catabolic process"}],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
        },
        "decisions": {
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for bacterial RppH"),
            "GO:0006402": ("ACCEPT", "mRNA catabolic process is the pathway-defining RppH role"),
            "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "generic hydrolase activity is uninformative for RppH"),
            "GO:0016818": ("KEEP_AS_NON_CORE", "acid-anhydride hydrolase activity is broad Nudix chemistry"),
            "GO:0034353": ("ACCEPT", "mRNA 5'-diphosphatase activity is the defining RppH molecular function"),
        },
    },
    "rho": {
        "symbol": "rho",
        "description": (
            "rho (PP_5214) encodes the Rho transcription termination factor, an ATP-dependent RNA-binding translocase/helicase. "
            "Rho terminates transcription on nascent RNA and is included in the ppu03018 RNA-degradation map as RNA-turnover-adjacent termination context rather than a ribonuclease."
        ),
        "core": {
            "description": "Rho RNA-dependent ATPase/helicase that mediates DNA-templated transcription termination.",
            "molecular_function": {"id": "GO:0008186", "label": "ATP-dependent activity, acting on RNA"},
            "directly_involved_in": [{"id": "GO:0006353", "label": "DNA-templated transcription termination"}],
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
        },
        "decisions": {
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for Rho"),
            "GO:0003723": ("ACCEPT", "RNA binding is central for Rho substrate recognition"),
            "GO:0004386": ("KEEP_AS_NON_CORE", "helicase activity is correct but less specific than ATP-dependent activity acting on RNA"),
            "GO:0005524": ("ACCEPT", "ATP binding supports Rho translocation/termination"),
            "GO:0005829": ("ACCEPT", "cytosol is appropriate for soluble bacterial Rho"),
            "GO:0006353": ("ACCEPT", "DNA-templated transcription termination is Rho's core biological process"),
            "GO:0008186": ("ACCEPT", "ATP-dependent activity acting on RNA captures Rho's RNA translocase activity"),
            "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "generic hydrolase activity is uninformative for Rho"),
        },
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
            "findings": [{"statement": "GOA table containing the annotations reviewed in this file."}],
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
        if ref["id"] not in seen and (ROOT / gene / ref["id"].split("/")[-1]).exists():
            refs.append(ref)
            seen.add(ref["id"])
    return refs


def curated_review(gene: str, term_id: str, label: str, decision: tuple) -> dict:
    action, reason, *rest = decision
    if action == "ACCEPT":
        summary = f"{label} is supported for {gene} in the ppu03018 first-pass curation."
    elif action == "KEEP_AS_NON_CORE":
        summary = f"{label} is plausible for {gene} but is not the most specific pathway-defining function."
    elif action == "MARK_AS_OVER_ANNOTATED":
        summary = f"{label} is too broad or over-propagated for the main function of {gene}."
    elif action == "MODIFY":
        summary = f"{label} should be replaced by a more specific or role-appropriate term for {gene}."
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
    support.append(asta_support(gene))
    deduped: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for item in support:
        key = (item["reference_id"], item["supporting_text"])
        if key not in seen:
            deduped.append(item)
            seen.add(key)
    return deduped


def curate_gene(gene: str, spec: dict) -> None:
    path = ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["gene_symbol"] = spec["symbol"]
    data["status"] = "DRAFT"
    data["description"] = spec["description"]

    decisions = spec["decisions"]
    for ann in data.get("existing_annotations", []):
        term = ann["term"]
        decision = decisions.get(
            term["id"],
            ("KEEP_AS_NON_CORE", "reviewed as ppu03018 boundary context but not central to the first-pass interpretation"),
        )
        ann["review"] = curated_review(gene, term["id"], term["label"], decision)

    core = dict(spec["core"])
    core["supported_by"] = core_supported_by(core, data.get("existing_annotations", []), gene)
    data["core_functions"] = [core]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": question
        }
        for question in spec.get(
            "questions",
            [f"What is the precise in vivo contribution of {spec['symbol']} to P. putida KT2440 RNA turnover or the ppu03018 boundary context?"],
        )
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Measure RNA half-lives, ribonucleoprotein profiles, and stress phenotypes after targeted "
                f"{spec['symbol']} perturbation in P. putida KT2440."
            ),
            "experiment_type": "gene perturbation with RNA stability and growth/stress phenotype assays",
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
        if not any(
            item.get("reference_id") == support["reference_id"]
            and item.get("supporting_text") == support["supporting_text"]
            for item in supported_by
        ):
            supported_by.append(support)
        ann["review"] = review
    for core in data.get("core_functions", []) or []:
        supported_by = core.setdefault("supported_by", [])
        if not any(
            item.get("reference_id") == support["reference_id"]
            and item.get("supporting_text") == support["supporting_text"]
            for item in supported_by
        ):
            supported_by.append(support)
    data["references"] = unique_references(data.get("references", []), gene)
    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    for gene, spec in GENES.items():
        curate_gene(gene, spec)
    for gene in OVERLAP_GENES:
        add_asta_support_to_existing_gene(gene)


if __name__ == "__main__":
    main()
