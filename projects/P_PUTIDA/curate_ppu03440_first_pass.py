#!/usr/bin/env python3
"""First-pass curation for KEGG ppu03440 homologous-recombination stubs."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path("genes") / SPECIES
OVERLAP_GENES = ["ruvB", "recA", "recB"]


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
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on on inter-ontology links",
    "GO_REF:0000116": "Automatic Gene Ontology annotation based on Rhea mapping",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


GENES: dict[str, dict] = {
    "recF": {
        "symbol": "recF",
        "description": (
            "recF (PP_0012) encodes a conserved RecF-family DNA replication and repair protein. "
            "It acts with RecO and RecR as a bacterial recombination mediator system that responds "
            "to single-stranded DNA gaps and damaged replication intermediates, helping load or "
            "stabilize RecA filaments during recombinational DNA repair."
        ),
        "core": {
            "description": (
                "RecFOR-pathway recombination mediator that binds DNA/ATP and supports RecA filament "
                "formation on single-stranded DNA repair intermediates."
            ),
            "molecular_function": {"id": "GO:0003697", "label": "single-stranded DNA binding"},
            "directly_involved_in": [
                {"id": "GO:0006281", "label": "DNA repair"},
                {"id": "GO:0006302", "label": "double-strand break repair"},
            ],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
        },
        "decisions": {
            "GO:0000731": (
                "KEEP_AS_NON_CORE",
                "RecF supports recombinational repair intermediates, but it is not a DNA-synthesis enzyme.",
            ),
            "GO:0003697": ("ACCEPT", "single-stranded DNA binding fits the RecFOR mediator role on ssDNA repair gaps"),
            "GO:0005524": ("ACCEPT", "ATP binding is supported by the conserved RecF/SMC-like P-loop NTPase domain"),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for this bacterial DNA repair protein"),
            "GO:0006260": (
                "KEEP_AS_NON_CORE",
                "RecF is connected to replication-associated repair but is not a replisome core factor",
            ),
            "GO:0006281": ("ACCEPT", "DNA repair is the broad biological role of RecF"),
            "GO:0006302": ("ACCEPT", "double-strand break repair is compatible with RecFOR-mediated recombinational repair"),
            "GO:0006974": (
                "KEEP_AS_NON_CORE",
                "DNA damage response is true pathway context but less specific than DNA repair and DSB repair",
            ),
            "GO:0009432": (
                "KEEP_AS_NON_CORE",
                "SOS response is downstream DNA-damage-response context rather than RecF's direct activity",
            ),
        },
    },
    "ruvC": {
        "symbol": "ruvC",
        "description": (
            "ruvC (PP_1215) encodes the bacterial Holliday junction resolvase, a magnesium-dependent "
            "crossover-junction endodeoxyribonuclease. RuvC acts with RuvA and RuvB in homologous "
            "recombination and recombinational repair by cleaving migrated Holliday junctions to "
            "resolve DNA crossover intermediates."
        ),
        "core": {
            "description": "Magnesium-dependent Holliday junction resolvase that cleaves four-way DNA junctions.",
            "molecular_function": {"id": "GO:0008821", "label": "crossover junction DNA endonuclease activity"},
            "directly_involved_in": [
                {"id": "GO:0006310", "label": "DNA recombination"},
                {"id": "GO:0006281", "label": "DNA repair"},
            ],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
            "in_complex": {"id": "GO:0048476", "label": "Holliday junction resolvase complex"},
        },
        "decisions": {
            "GO:0000287": ("ACCEPT", "magnesium ion binding is expected for the RuvC nuclease active site"),
            "GO:0003676": (
                "KEEP_AS_NON_CORE",
                "nucleic acid binding is correct but less informative than crossover-junction endonuclease activity",
            ),
            "GO:0004520": (
                "MODIFY",
                "generic DNA endonuclease activity should be narrowed to the RuvC crossover-junction nuclease term",
                [{"id": "GO:0008821", "label": "crossover junction DNA endonuclease activity"}],
            ),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for a bacterial recombination nuclease"),
            "GO:0006281": ("ACCEPT", "RuvC resolves recombination intermediates during DNA repair"),
            "GO:0006310": ("ACCEPT", "Holliday junction resolution is part of DNA recombination"),
            "GO:0006974": (
                "KEEP_AS_NON_CORE",
                "DNA damage response is pathway context but less specific than recombination and repair",
            ),
            "GO:0008821": ("ACCEPT", "crossover junction DNA endonuclease activity is the core RuvC function"),
            "GO:0048476": ("ACCEPT", "RuvC is the catalytic resolvase in the Holliday junction resolvase complex"),
        },
    },
    "ruvA": {
        "symbol": "ruvA",
        "description": (
            "ruvA (PP_1216) encodes the DNA-binding recognition subunit of the bacterial RuvAB Holliday "
            "junction branch-migration machinery. RuvA binds four-way DNA junctions, holds the junction "
            "open, and recruits or organizes RuvB motor subunits for ATP-dependent branch migration before "
            "RuvC-mediated resolution."
        ),
        "core": {
            "description": (
                "Holliday junction DNA-binding scaffold of the RuvAB branch-migration complex, organizing "
                "RuvB motor action on four-way DNA junctions."
            ),
            "molecular_function": {"id": "GO:0000400", "label": "four-way junction DNA binding"},
            "directly_involved_in": [
                {"id": "GO:0006310", "label": "DNA recombination"},
                {"id": "GO:0006281", "label": "DNA repair"},
            ],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
            "in_complex": {"id": "GO:0009379", "label": "Holliday junction helicase complex"},
        },
        "decisions": {
            "GO:0000400": ("ACCEPT", "four-way junction DNA binding is the defining RuvA molecular function"),
            "GO:0003677": (
                "MARK_AS_OVER_ANNOTATED",
                "generic DNA binding is redundant with the specific four-way junction DNA-binding term",
            ),
            "GO:0003678": (
                "MODIFY",
                "RuvA is the junction-binding scaffold rather than the ATPase motor; use four-way junction DNA binding",
                [{"id": "GO:0000400", "label": "four-way junction DNA binding"}],
            ),
            "GO:0005524": (
                "MARK_AS_OVER_ANNOTATED",
                "ATP binding belongs to the RuvB motor; RuvA's core function is junction DNA binding",
            ),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for a bacterial DNA recombination factor"),
            "GO:0006281": ("ACCEPT", "RuvA acts in Holliday junction processing during DNA repair"),
            "GO:0006310": ("ACCEPT", "RuvA is part of the Holliday junction branch-migration machinery"),
            "GO:0006974": (
                "KEEP_AS_NON_CORE",
                "DNA damage response is broad context for RuvABC repair activity",
            ),
            "GO:0009378": (
                "MODIFY",
                "four-way junction helicase activity is a RuvAB complex activity powered by RuvB; RuvA contributes as the junction-binding subunit",
                [{"id": "GO:0000400", "label": "four-way junction DNA binding"}],
            ),
            "GO:0009379": ("ACCEPT", "RuvA is a component of the Holliday junction helicase complex"),
            "GO:0048476": ("ACCEPT", "RuvA participates in the larger RuvABC Holliday junction resolvase machinery"),
        },
    },
    "recO": {
        "symbol": "recO",
        "description": (
            "recO (PP_1435) encodes DNA repair protein RecO, a RecFOR-pathway recombination mediator. "
            "RecO acts with RecF and RecR during homologous recombination and recombinational repair, "
            "promoting RecA loading or stabilization on single-stranded DNA regions generated by DNA damage "
            "or stalled replication."
        ),
        "core": {
            "description": "RecFOR recombination mediator for RecA filament assembly on repair-associated ssDNA gaps.",
            "directly_involved_in": [
                {"id": "GO:0006310", "label": "DNA recombination"},
                {"id": "GO:0006302", "label": "double-strand break repair"},
            ],
            "locations": [{"id": "GO:0043590", "label": "bacterial nucleoid"}],
        },
        "decisions": {
            "GO:0006281": ("ACCEPT", "RecO is a conserved DNA repair and recombination mediator"),
            "GO:0006302": ("ACCEPT", "double-strand break repair fits the RecFOR recombinational-repair role"),
            "GO:0006310": ("ACCEPT", "DNA recombination is the core process for RecO"),
            "GO:0043590": ("ACCEPT", "bacterial nucleoid is plausible for a DNA repair/recombination mediator"),
        },
    },
    "recR": {
        "symbol": "recR",
        "description": (
            "recR (PP_4267) encodes recombination protein RecR, a RecFOR pathway factor with conserved "
            "DNA-binding and zinc-associated domains. RecR acts with RecF and RecO to support RecA-mediated "
            "homologous recombination and DNA repair at single-stranded DNA gaps or damaged replication "
            "intermediates."
        ),
        "core": {
            "description": "RecFOR recombination mediator subunit supporting RecA-dependent DNA repair and recombination.",
            "molecular_function": {"id": "GO:0003677", "label": "DNA binding"},
            "directly_involved_in": [
                {"id": "GO:0006310", "label": "DNA recombination"},
                {"id": "GO:0006281", "label": "DNA repair"},
            ],
        },
        "decisions": {
            "GO:0003677": ("ACCEPT", "DNA binding is supported by RecR DNA-binding and Toprim-related domains"),
            "GO:0006281": ("ACCEPT", "RecR is a conserved DNA repair factor"),
            "GO:0006310": ("ACCEPT", "RecR participates in RecFOR-dependent DNA recombination"),
            "GO:0046872": (
                "MODIFY",
                "generic metal ion binding should be narrowed to zinc ion binding for the RecR zinc-associated domain",
                [{"id": "GO:0008270", "label": "zinc ion binding"}],
            ),
        },
    },
    "recD": {
        "symbol": "recD",
        "description": (
            "recD (PP_4672) encodes the RecD subunit of the RecBCD exonuclease V complex. RecD is the "
            "5'-to-3' DNA helicase/translocase motor in the complex, contributing to double-strand DNA-end "
            "processing, ATP hydrolysis, and homologous recombination-mediated double-strand break repair."
        ),
        "core": {
            "description": "RecBCD subunit providing 5'-3' DNA helicase activity during double-strand-end processing.",
            "molecular_function": {"id": "GO:0043139", "label": "5'-3' DNA helicase activity"},
            "contributes_to_molecular_function": {"id": "GO:0008854", "label": "exodeoxyribonuclease V activity"},
            "directly_involved_in": [{"id": "GO:0000724", "label": "double-strand break repair via homologous recombination"}],
            "in_complex": {"id": "GO:0009338", "label": "exodeoxyribonuclease V complex"},
        },
        "decisions": {
            "GO:0000724": ("ACCEPT", "RecD acts in RecBCD-mediated DSB repair by homologous recombination"),
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected for a DNA helicase complex subunit"),
            "GO:0003678": ("KEEP_AS_NON_CORE", "DNA helicase activity is correct but less specific than 5'-3' DNA helicase activity"),
            "GO:0004386": ("MARK_AS_OVER_ANNOTATED", "generic helicase activity is less informative than DNA helicase directionality"),
            "GO:0005524": ("ACCEPT", "ATP binding is required for RecD helicase motor activity"),
            "GO:0006302": ("ACCEPT", "double-strand break repair is the broad RecBCD repair process"),
            "GO:0006310": ("ACCEPT", "RecD contributes to homologous recombination through RecBCD DNA-end processing"),
            "GO:0008854": (
                "KEEP_AS_NON_CORE",
                "exodeoxyribonuclease V is the RecBCD complex activity; RecD contributes as a helicase subunit",
            ),
            "GO:0009338": ("ACCEPT", "RecD is an obligate subunit of the exodeoxyribonuclease V complex"),
            "GO:0016887": ("ACCEPT", "ATP hydrolysis powers RecD translocation"),
            "GO:0017116": ("KEEP_AS_NON_CORE", "single-stranded DNA helicase activity is plausible but less specific than 5'-3' DNA helicase activity"),
            "GO:0043139": ("ACCEPT", "5'-3' DNA helicase activity is the defining RecD motor function"),
        },
    },
    "recC": {
        "symbol": "recC",
        "description": (
            "recC (PP_4674) encodes the RecC subunit of the RecBCD exonuclease V complex. RecC is the "
            "DNA-recognition and scaffold subunit that helps organize RecB and RecD for double-strand "
            "DNA-end processing and homologous recombination-mediated repair."
        ),
        "core": {
            "description": "DNA-recognition/scaffold subunit of the RecBCD exonuclease V complex for DSB-end processing.",
            "contributes_to_molecular_function": {"id": "GO:0008854", "label": "exodeoxyribonuclease V activity"},
            "directly_involved_in": [{"id": "GO:0000724", "label": "double-strand break repair via homologous recombination"}],
            "in_complex": {"id": "GO:0009338", "label": "exodeoxyribonuclease V complex"},
        },
        "decisions": {
            "GO:0000724": ("ACCEPT", "RecC acts in RecBCD-mediated DSB repair by homologous recombination"),
            "GO:0003677": ("ACCEPT", "DNA binding fits the RecC DNA-recognition/scaffold role in RecBCD"),
            "GO:0003678": (
                "MODIFY",
                "RecC is not the primary RecBCD motor subunit; record its complex-level contribution instead",
                [{"id": "GO:0009338", "label": "exodeoxyribonuclease V complex"}],
            ),
            "GO:0005524": (
                "MARK_AS_OVER_ANNOTATED",
                "ATP binding is not the defining RecC activity; RecB and RecD provide the helicase motors",
            ),
            "GO:0006310": ("ACCEPT", "RecC contributes to homologous recombination through RecBCD DNA-end processing"),
            "GO:0008854": (
                "KEEP_AS_NON_CORE",
                "exodeoxyribonuclease V is the RecBCD complex activity; RecC contributes as a noncatalytic subunit",
            ),
            "GO:0009338": ("ACCEPT", "RecC is an obligate subunit of the exodeoxyribonuclease V complex"),
            "GO:0140097": (
                "MARK_AS_OVER_ANNOTATED",
                "generic catalytic activity acting on DNA is too broad for the RecC scaffold/recognition subunit",
            ),
        },
    },
    "priA": {
        "symbol": "priA",
        "description": (
            "priA (PP_5088) encodes replication restart protein PriA, an ATP-dependent 3'-to-5' DNA "
            "helicase that recognizes stalled or repaired replication fork structures and helps reload "
            "the primosome/replisome. In homologous-recombination maps it marks the replication-restart "
            "output of recombinational repair rather than the RecA strand-exchange core."
        ),
        "core": {
            "description": "ATP-dependent 3'-5' DNA helicase that initiates replication restart at repaired or stalled forks.",
            "molecular_function": {"id": "GO:0043138", "label": "3'-5' DNA helicase activity"},
            "directly_involved_in": [
                {"id": "GO:0006270", "label": "DNA replication initiation"},
                {"id": "GO:0006310", "label": "DNA recombination"},
            ],
            "in_complex": {"id": "GO:1990077", "label": "primosome complex"},
        },
        "decisions": {
            "GO:0000166": (
                "MARK_AS_OVER_ANNOTATED",
                "nucleotide binding is a generic parent of the ATP-binding/helicase activity terms",
            ),
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for PriA"),
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected but less specific than helicase/restart function"),
            "GO:0003678": ("KEEP_AS_NON_CORE", "DNA helicase activity is correct but less specific than 3'-5' DNA helicase activity"),
            "GO:0005524": ("ACCEPT", "ATP binding is required for PriA helicase activity"),
            "GO:0006260": ("ACCEPT", "PriA functions in replication restart"),
            "GO:0006270": ("ACCEPT", "PriA initiates replication restart/primosome assembly at fork structures"),
            "GO:0006302": ("KEEP_AS_NON_CORE", "PriA acts downstream of repair to restart replication but is not a DSB-end-processing enzyme"),
            "GO:0006310": ("ACCEPT", "PriA is linked to recombination-dependent replication restart"),
            "GO:0008270": ("ACCEPT", "zinc ion binding is supported by the PriA zinc-binding region"),
            "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "generic hydrolase activity is uninformative for PriA"),
            "GO:0016887": ("ACCEPT", "ATP hydrolysis powers PriA helicase activity"),
            "GO:0043138": ("ACCEPT", "3'-5' DNA helicase activity is the specific PriA molecular function"),
            "GO:1990077": ("ACCEPT", "PriA is a primosome/replication-restart factor"),
        },
    },
    "recG": {
        "symbol": "recG",
        "description": (
            "recG (PP_5310) encodes ATP-dependent DNA helicase RecG, a RecG-family 3'-to-5' DNA "
            "helicase that remodels branched DNA structures including stalled replication forks and "
            "recombination intermediates. It contributes to DNA repair and homologous recombination "
            "by branch migration/fork regression outside the RuvAB motor system."
        ),
        "core": {
            "description": "ATP-dependent 3'-5' DNA helicase for branch migration and stalled-fork regression.",
            "molecular_function": {"id": "GO:0043138", "label": "3'-5' DNA helicase activity"},
            "directly_involved_in": [
                {"id": "GO:0006281", "label": "DNA repair"},
                {"id": "GO:0006310", "label": "DNA recombination"},
            ],
        },
        "decisions": {
            "GO:0000166": (
                "MARK_AS_OVER_ANNOTATED",
                "nucleotide binding is a generic parent of the ATP-binding/helicase activity terms",
            ),
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for RecG"),
            "GO:0003678": ("KEEP_AS_NON_CORE", "DNA helicase activity is correct but less specific than 3'-5' DNA helicase activity"),
            "GO:0005524": ("ACCEPT", "ATP binding is required for RecG helicase activity"),
            "GO:0006281": ("ACCEPT", "RecG remodels repair and stalled-fork DNA intermediates"),
            "GO:0006310": ("ACCEPT", "RecG branch-migration activity acts in DNA recombination contexts"),
            "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "generic hydrolase activity is uninformative for RecG"),
            "GO:0016887": ("ACCEPT", "ATP hydrolysis powers RecG helicase activity"),
            "GO:0043138": ("ACCEPT", "3'-5' DNA helicase activity is the specific RecG molecular function"),
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
        if ref["id"] not in seen:
            refs.append(ref)
            seen.add(ref["id"])
    return refs


def curated_review(gene: str, term_id: str, label: str, decision: tuple) -> dict:
    action, reason, *rest = decision
    if action == "ACCEPT":
        summary = f"{label} is supported for {gene} in the ppu03440 first-pass curation."
    elif action == "KEEP_AS_NON_CORE":
        summary = f"{label} is plausible for {gene} but is not the most specific pathway-defining function."
    elif action == "MARK_AS_OVER_ANNOTATED":
        summary = f"{label} is too broad or over-propagated for the main function of {gene}."
    elif action == "MODIFY":
        summary = f"{label} should be replaced by a more specific or subunit-appropriate term for {gene}."
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
            ("KEEP_AS_NON_CORE", "not part of the primary ppu03440 first-pass interpretation"),
        )
        ann["review"] = curated_review(gene, term["id"], term["label"], decision)

    core = dict(spec["core"])
    core["supported_by"] = core_supported_by(core, data.get("existing_annotations", []), gene)
    data["core_functions"] = [core]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": (
                f"What is the precise in vivo contribution of {spec['symbol']} to P. putida KT2440 "
                f"homologous recombination compared with adjacent DNA repair and replication-restart pathways?"
            )
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Measure survival, recombination frequency, and replication-restart phenotypes for a targeted "
                f"{spec['symbol']} perturbation after double-strand-break or replication-stress challenge."
            ),
            "experiment_type": "gene perturbation and recombinational repair phenotype assay",
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
