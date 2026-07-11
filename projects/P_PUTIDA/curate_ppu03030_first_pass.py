#!/usr/bin/env python3
"""First-pass curation for KEGG ppu03030 DNA-replication stubs."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path("genes") / SPECIES
OVERLAP_GENES = [
    "dnaN",
    "polA",
    "PP_0353",
    "ssb",
    "holC",
    "dnaEA",
    "holB",
    "dnaQ",
    "dnaX",
    "ligA",
    "PP_4768",
    "holA",
    "ligB",
]


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
    "dnaG": {
        "symbol": "dnaG",
        "description": (
            "dnaG (PP_0388) encodes the bacterial DNA primase. DnaG synthesizes short RNA primers on "
            "single-stranded DNA templates during chromosome replication and acts with the DnaB helicase "
            "within the primosome to initiate lagging-strand Okazaki fragment synthesis."
        ),
        "core": {
            "description": "DNA primase that synthesizes RNA primers during bacterial chromosome replication.",
            "molecular_function": {"id": "GO:0003899", "label": "DNA-directed RNA polymerase activity"},
            "directly_involved_in": [
                {"id": "GO:0006260", "label": "DNA replication"},
                {"id": "GO:0006269", "label": "DNA replication, synthesis of primer"},
            ],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
            "in_complex": {"id": "GO:1990077", "label": "primosome complex"},
        },
        "decisions": {
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected for a primase but less specific than primer synthesis"),
            "GO:0003899": (
                "ACCEPT",
                "DNA-directed RNA polymerase activity captures DnaG primase synthesis of RNA primers on a DNA template",
            ),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for a bacterial replisome/primosome enzyme"),
            "GO:0006260": ("ACCEPT", "DNA replication is the core biological process for DnaG"),
            "GO:0006269": ("ACCEPT", "primer synthesis is the defining DNA replication step for DnaG"),
            "GO:0008270": ("ACCEPT", "zinc ion binding is supported by conserved DnaG primase zinc-binding context"),
            "GO:0016779": ("KEEP_AS_NON_CORE", "nucleotidyltransferase activity is a broad parent of primase activity"),
        },
        "new_annotations": [
            {
                "term": {"id": "GO:1990077", "label": "primosome complex"},
                "evidence_type": "IEA",
                "qualifier": "part_of",
                "reason": "UniProt carries primosome-complex membership for DnaG; it is absent from the fetched GOA seed but matches the core primase/primosome interpretation.",
            }
        ],
    },
    "rnhB": {
        "symbol": "rnhB",
        "description": (
            "rnhB (PP_1605) encodes ribonuclease HII, a type 2 RNase H enzyme that cleaves RNA in "
            "RNA-DNA hybrids and contributes to removal of RNA primers or embedded ribonucleotides during "
            "DNA replication-associated repair and genome maintenance."
        ),
        "core": {
            "description": "RNase HII RNA-DNA hybrid nuclease for replication-associated RNA primer/ribonucleotide removal.",
            "molecular_function": {"id": "GO:0004523", "label": "RNA-DNA hybrid ribonuclease activity"},
            "directly_involved_in": [{"id": "GO:0043137", "label": "DNA replication, removal of RNA primer"}],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
        },
        "decisions": {
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for an RNase H enzyme"),
            "GO:0003723": ("KEEP_AS_NON_CORE", "RNA binding is substrate context but less specific than RNA-DNA hybrid ribonuclease activity"),
            "GO:0004523": ("ACCEPT", "RNA-DNA hybrid ribonuclease activity is the core RNase HII molecular function"),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for a bacterial DNA replication/repair nuclease"),
            "GO:0006298": (
                "MARK_AS_OVER_ANNOTATED",
                "mismatch repair is not the direct pathway role of RNase HII; RNA-DNA hybrid cleavage and primer/ribonucleotide removal are more specific",
            ),
            "GO:0006401": ("KEEP_AS_NON_CORE", "RNA catabolism is true but too broad for RNase HII replication-associated function"),
            "GO:0030145": ("ACCEPT", "manganese ion binding is plausible catalytic cofactor context for RNase HII"),
            "GO:0032299": (
                "KEEP_AS_NON_CORE",
                "ribonuclease H2 complex is retained as imported context, but the bacterial core function is the RNase HII nuclease activity",
            ),
            "GO:0043137": ("ACCEPT", "RNA primer removal is the DNA replication step captured by this KEGG bucket"),
        },
    },
    "PP_3893": {
        "symbol": "PP_3893",
        "description": (
            "PP_3893 encodes a DnaB-family predicted DNA 5'-to-3' helicase. It is a second DnaB-like "
            "helicase in the KT2440 DNA-replication KEGG map; current evidence supports ATP-dependent "
            "DNA helicase activity, while its exact physiological division of labor relative to canonical "
            "dnaB remains unresolved."
        ),
        "core": {
            "description": "DnaB-like ATP-dependent 5'-3' DNA helicase candidate in the DNA replication/primosome boundary.",
            "molecular_function": {"id": "GO:0043139", "label": "5'-3' DNA helicase activity"},
            "directly_involved_in": [{"id": "GO:0006260", "label": "DNA replication"}],
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
        },
        "decisions": {
            "GO:0000166": ("MARK_AS_OVER_ANNOTATED", "nucleotide binding is a generic parent of ATP binding and helicase activity"),
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected for a DnaB-like helicase"),
            "GO:0003678": ("KEEP_AS_NON_CORE", "DNA helicase activity is correct but less specific than 5'-3' DNA helicase activity"),
            "GO:0004386": ("MARK_AS_OVER_ANNOTATED", "generic helicase activity is less informative than DNA helicase directionality"),
            "GO:0005524": ("ACCEPT", "ATP binding supports DnaB-family helicase motor activity"),
            "GO:0005829": ("ACCEPT", "cytosol is appropriate for a soluble bacterial DNA replication helicase"),
            "GO:0006260": ("ACCEPT", "DNA replication is supported by DnaB-family helicase assignment and KEGG membership"),
            "GO:0006269": (
                "KEEP_AS_NON_CORE",
                "DnaB-like helicases support primosome function but do not synthesize RNA primers directly",
            ),
            "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "generic hydrolase activity is uninformative for this helicase"),
            "GO:0043139": ("ACCEPT", "5'-3' DNA helicase activity is the most specific current molecular function"),
        },
        "questions": [
            "Is PP_3893 a functional replicative DnaB paralog, a backup helicase, or a more specialized mobile-element/plasmid-like replication helicase?"
        ],
    },
    "rnhA": {
        "symbol": "rnhA",
        "description": (
            "rnhA (PP_4142) encodes ribonuclease HI, an RNase H enzyme that cleaves the RNA strand of "
            "RNA-DNA hybrids. In DNA replication, RnhA contributes to RNA primer removal and suppression "
            "of persistent R-loops or RNA-DNA hybrid intermediates."
        ),
        "core": {
            "description": "RNase HI RNA-DNA hybrid nuclease for RNA primer and R-loop/RNA-DNA hybrid processing.",
            "molecular_function": {"id": "GO:0004523", "label": "RNA-DNA hybrid ribonuclease activity"},
            "directly_involved_in": [{"id": "GO:0043137", "label": "DNA replication, removal of RNA primer"}],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
        },
        "decisions": {
            "GO:0000287": ("ACCEPT", "magnesium ion binding is expected catalytic cofactor context for RNase HI"),
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for an RNase H enzyme"),
            "GO:0004523": ("ACCEPT", "RNA-DNA hybrid ribonuclease activity is the core RNase HI molecular function"),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for a bacterial DNA replication/repair nuclease"),
            "GO:0006401": ("KEEP_AS_NON_CORE", "RNA catabolic process is true but less specific than RNA-DNA hybrid nuclease activity"),
            "GO:0043137": ("ACCEPT", "RNA primer removal is the DNA replication step captured by this KEGG bucket"),
        },
    },
    "dnaB": {
        "symbol": "dnaB",
        "description": (
            "dnaB (PP_4873) encodes the canonical bacterial replicative DNA helicase. DnaB is an "
            "ATP-dependent hexameric 5'-to-3' DNA helicase that unwinds parental duplex DNA at the "
            "replication fork and works with DnaG primase in the primosome during chromosome replication."
        ),
        "core": {
            "description": "Canonical DnaB replicative 5'-3' DNA helicase of the bacterial primosome/replisome.",
            "molecular_function": {"id": "GO:0043139", "label": "5'-3' DNA helicase activity"},
            "directly_involved_in": [
                {"id": "GO:0006260", "label": "DNA replication"},
                {"id": "GO:0006269", "label": "DNA replication, synthesis of primer"},
            ],
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
            "in_complex": {"id": "GO:1990077", "label": "primosome complex"},
        },
        "decisions": {
            "GO:0000166": ("MARK_AS_OVER_ANNOTATED", "nucleotide binding is a generic parent of ATP binding and helicase activity"),
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected but less specific than helicase activity"),
            "GO:0003678": ("KEEP_AS_NON_CORE", "DNA helicase activity is correct but less specific than 5'-3' DNA helicase activity"),
            "GO:0004386": ("MARK_AS_OVER_ANNOTATED", "generic helicase activity is less informative than DNA helicase directionality"),
            "GO:0005524": ("ACCEPT", "ATP binding is required for DnaB helicase motor activity"),
            "GO:0005829": ("ACCEPT", "cytosol is appropriate for a bacterial replisome/primosome helicase"),
            "GO:0006260": ("ACCEPT", "DNA replication is the core biological process for DnaB"),
            "GO:0006269": ("ACCEPT", "DnaB acts in the primosome with DnaG during primer synthesis at replication forks"),
            "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "generic hydrolase activity is uninformative for DnaB"),
            "GO:0016887": ("ACCEPT", "ATP hydrolysis powers DnaB helicase translocation"),
            "GO:0042802": ("KEEP_AS_NON_CORE", "identical protein binding is plausible for DnaB hexamerization but less informative than helicase/primosome function"),
            "GO:0043139": ("ACCEPT", "5'-3' DNA helicase activity is the core DnaB molecular function"),
            "GO:1990077": ("ACCEPT", "DnaB is a primosome component with DnaG primase"),
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


def uniprot_go_support(gene: str, term_id: str) -> dict:
    path = ROOT / gene / f"{gene}-uniprot.txt"
    for line in path.read_text(encoding="utf-8").splitlines():
        if f"GO; {term_id};" in line:
            return {
                "reference_id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
                "supporting_text": line,
            }
    raise ValueError(f"No UniProt GO line found for {gene} {term_id}")


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
        summary = f"{label} is supported for {gene} in the ppu03030 first-pass curation."
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


def curated_new_annotation(gene: str, spec: dict) -> dict:
    term = spec["term"]
    return {
        "term": term,
        "evidence_type": spec["evidence_type"],
        "original_reference_id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
        "qualifier": spec["qualifier"],
        "review": {
            "summary": f"{term['label']} is a newly recommended annotation for {gene} in the ppu03030 first-pass curation.",
            "action": "NEW",
            "reason": spec["reason"],
            "supported_by": [uniprot_go_support(gene, term["id"]), asta_support(gene)],
        },
    }


def core_supported_by(core: dict, annotations: list[dict], gene: str) -> list[dict]:
    support: list[dict] = []
    term_index = {
        ann["term"]["id"]: ann["term"]["label"]
        for ann in annotations
        if ann.get("term", {}).get("id")
    }
    support_index: dict[str, dict] = {}
    for ann in annotations:
        term_id = ann.get("term", {}).get("id")
        if not term_id:
            continue
        supported_by = ann.get("review", {}).get("supported_by") or []
        if supported_by:
            support_index.setdefault(term_id, supported_by[0])

    def add_term_support(term: dict) -> None:
        term_id = term.get("id")
        if term_id in term_index:
            support.append(support_index.get(term_id, support_for(term_id, term_index[term_id], gene)))

    for slot in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
        term = core.get(slot)
        if isinstance(term, dict):
            add_term_support(term)
    for slot in ("directly_involved_in", "locations"):
        for term in core.get(slot, []) or []:
            add_term_support(term)
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
            ("KEEP_AS_NON_CORE", "not part of the primary ppu03030 first-pass interpretation"),
        )
        ann["review"] = curated_review(gene, term["id"], term["label"], decision)
    existing_term_ids = {ann["term"]["id"] for ann in data.get("existing_annotations", [])}
    for new_ann_spec in spec.get("new_annotations", []):
        if new_ann_spec["term"]["id"] not in existing_term_ids:
            data.setdefault("existing_annotations", []).append(curated_new_annotation(gene, new_ann_spec))
            existing_term_ids.add(new_ann_spec["term"]["id"])

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
            [f"What is the precise in vivo contribution of {spec['symbol']} to P. putida KT2440 DNA replication?"],
        )
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Measure growth, chromosome replication dynamics, and DNA-damage sensitivity after targeted "
                f"{spec['symbol']} perturbation or conditional depletion."
            ),
            "experiment_type": "gene perturbation and DNA replication phenotype assay",
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
