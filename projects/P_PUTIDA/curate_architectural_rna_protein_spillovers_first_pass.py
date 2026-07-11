#!/usr/bin/env python3
"""First-pass curation for PSEPK DNA-bucket architectural/RNA/protein spillovers."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "dna_bucket_architectural_rna_protein_spillover_boundary.yaml"
DNA_SPILLOVER_TSV = "projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_architectural_rna_protein_spillovers.tsv"
PROTEIN_TURNOVER_DNA_SPILLOVER_TSV = "projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_dna_damage_or_repair_spillover_proteases.tsv"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0000166": {"id": "GO:0000166", "label": "nucleotide binding"},
    "GO:0000976": {"id": "GO:0000976", "label": "transcription cis-regulatory region binding"},
    "GO:0001216": {"id": "GO:0001216", "label": "DNA-binding transcription activator activity"},
    "GO:0001217": {"id": "GO:0001217", "label": "DNA-binding transcription repressor activity"},
    "GO:0001671": {"id": "GO:0001671", "label": "ATPase activator activity"},
    "GO:0003676": {"id": "GO:0003676", "label": "nucleic acid binding"},
    "GO:0003677": {"id": "GO:0003677", "label": "DNA binding"},
    "GO:0003697": {"id": "GO:0003697", "label": "single-stranded DNA binding"},
    "GO:0003723": {"id": "GO:0003723", "label": "RNA binding"},
    "GO:0003724": {"id": "GO:0003724", "label": "RNA helicase activity"},
    "GO:0004386": {"id": "GO:0004386", "label": "helicase activity"},
    "GO:0005524": {"id": "GO:0005524", "label": "ATP binding"},
    "GO:0005694": {"id": "GO:0005694", "label": "chromosome"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0005829": {"id": "GO:0005829", "label": "cytosol"},
    "GO:0006310": {"id": "GO:0006310", "label": "DNA recombination"},
    "GO:0006355": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "GO:0006417": {"id": "GO:0006417", "label": "regulation of translation"},
    "GO:0006457": {"id": "GO:0006457", "label": "protein folding"},
    "GO:0006508": {"id": "GO:0006508", "label": "proteolysis"},
    "GO:0006974": {"id": "GO:0006974", "label": "DNA damage response"},
    "GO:0008156": {"id": "GO:0008156", "label": "negative regulation of DNA replication"},
    "GO:0008237": {"id": "GO:0008237", "label": "metallopeptidase activity"},
    "GO:0016787": {"id": "GO:0016787", "label": "hydrolase activity"},
    "GO:0030527": {"id": "GO:0030527", "label": "structural constituent of chromatin"},
    "GO:0032993": {"id": "GO:0032993", "label": "protein-DNA complex"},
    "GO:0042026": {"id": "GO:0042026", "label": "protein refolding"},
    "GO:0045892": {"id": "GO:0045892", "label": "negative regulation of DNA-templated transcription"},
    "GO:0045893": {"id": "GO:0045893", "label": "positive regulation of DNA-templated transcription"},
    "GO:0051087": {"id": "GO:0051087", "label": "protein-folding chaperone binding"},
    "GO:0106300": {"id": "GO:0106300", "label": "protein-DNA covalent cross-linking repair"},
}


GENE_INFO = {
    "tldD": {
        "accession": "Q88PB0",
        "description": "tldD encodes a TldD/PmbA-family U62 metalloprotease associated with proteolysis. In the KT2440 record, its supported functions are cytosolic metallopeptidase activity and proteolysis, with product-name context linking the family to microcin B17 maturation and sensitivity to the gyrase inhibitor LetD.",
        "core": [
            {
                "description": "TldD/PmbA-family cytosolic metallopeptidase activity in proteolysis.",
                "molecular_function": TERM["GO:0008237"],
                "directly_involved_in": [TERM["GO:0006508"]],
                "locations": [TERM["GO:0005829"]],
                "support_term": "GO:0008237",
            }
        ],
    },
    "ihfB": {
        "accession": "P0A128",
        "description": "ihfB encodes the beta subunit of integration host factor, a bacterial histone-like DNA-binding protein. IHF acts as an architectural chromosome-associated factor and participates in promoter regulation, recombination context, and translational control together with the IHF alpha subunit.",
        "core": [
            {
                "description": "Integration host factor beta subunit architectural DNA-binding/chromatin-structural role.",
                "molecular_function": TERM["GO:0030527"],
                "directly_involved_in": [TERM["GO:0006355"]],
                "locations": [TERM["GO:0005694"], TERM["GO:0005829"]],
                "support_term": "GO:0030527",
            }
        ],
    },
    "ihfA": {
        "accession": "P0A126",
        "description": "ihfA encodes the alpha subunit of integration host factor, a bacterial histone-like DNA-binding protein. In Pseudomonas putida it contributes to IHF-DNA complexes at regulatory sites and can support promoter-specific activation or repression through architectural DNA binding.",
        "core": [
            {
                "description": "Integration host factor alpha subunit in promoter-proximal IHF-DNA complexes.",
                "molecular_function": TERM["GO:0000976"],
                "directly_involved_in": [TERM["GO:0045892"], TERM["GO:0045893"]],
                "locations": [TERM["GO:0005829"]],
                "support_term": "GO:0000976",
            },
            {
                "description": "Bacterial histone-like structural constituent of chromatin.",
                "molecular_function": TERM["GO:0030527"],
                "locations": [TERM["GO:0005829"]],
                "support_term": "GO:0030527",
            },
        ],
    },
    "cspD": {
        "accession": "Q88FS3",
        "description": "cspD encodes a cold-shock-domain/OB-fold nucleic-acid-binding protein. The local UniProt record supports DNA-binding and negative regulation of DNA replication, with additional broad regulation-of-transcription context from cold-shock-domain family annotation.",
        "core": [
            {
                "description": "CspD cold-shock-domain DNA-binding role linked to inhibition of DNA replication.",
                "molecular_function": TERM["GO:0003677"],
                "directly_involved_in": [TERM["GO:0008156"]],
                "locations": [TERM["GO:0005737"], TERM["GO:0005829"]],
                "support_term": "GO:0003677",
            }
        ],
        "new_terms": ["GO:0003677", "GO:0008156"],
    },
    "hrpA": {
        "accession": "Q88EC0",
        "description": "hrpA encodes a large DEAD/DEAH-family ATP-dependent RNA helicase with RNA-binding, helicase, ATP-binding, and hydrolase annotations. Its supported catalytic role is RNA helicase activity rather than DNA-repair helicase activity.",
        "core": [
            {
                "description": "DEAD/DEAH-family ATP-dependent RNA helicase activity.",
                "molecular_function": TERM["GO:0003724"],
                "support_term": "GO:0003724",
            }
        ],
    },
    "hrpB": {
        "accession": "Q88DQ1",
        "description": "hrpB encodes an ATP-dependent HrpB helicase with DEAD/DEAH helicase domains and HrpB-specific RNA-helicase-family support. Current evidence supports an RNA-helicase-family nucleic-acid helicase role, while the fetched GOA block remains generic.",
        "core": [
            {
                "description": "HrpB-family ATP-dependent RNA helicase candidate.",
                "molecular_function": TERM["GO:0003724"],
                "support_term": "GO:0003724",
            }
        ],
        "new_terms": ["GO:0003724"],
    },
    "PP_0758": {
        "accession": "Q88PU0",
        "description": "PP_0758 encodes an SRAP/HMCES-like abasic-site processing protein. The supported PSEPK annotation is single-stranded DNA binding in protein-DNA covalent cross-link repair, while the protease-like signal comes from broad family/keyword transfer rather than a general protein-turnover role.",
        "core": [
            {
                "description": "SRAP/HMCES-like single-stranded-DNA binding function in protein-DNA covalent cross-link repair.",
                "molecular_function": TERM["GO:0003697"],
                "directly_involved_in": [TERM["GO:0106300"]],
                "support_term": "GO:0106300",
            }
        ],
    },
    "PP_2493": {
        "accession": "Q88K00",
        "description": "PP_2493 encodes a RadC/UPF0758-family MPN/JAB-domain metalloprotease-like protein. Current local evidence supports a predicted metallopeptidase/proteolysis function, with DNA-repair context limited to family naming rather than direct organism-specific pathway evidence.",
        "core": [
            {
                "description": "RadC/UPF0758-family MPN/JAB-domain metallopeptidase-like activity.",
                "molecular_function": TERM["GO:0008237"],
                "directly_involved_in": [TERM["GO:0006508"]],
                "support_term": "GO:0008237",
            }
        ],
        "new_terms": ["GO:0008237", "GO:0006508"],
    },
    "PP_2941": {
        "accession": "Q88IQ8",
        "description": "PP_2941 encodes an SRAP/HMCES-like abasic-site processing protein. The supported PSEPK annotation is single-stranded DNA binding in protein-DNA covalent cross-link repair, while the protease-like signal comes from broad family/keyword transfer rather than a general protein-turnover role.",
        "core": [
            {
                "description": "SRAP/HMCES-like single-stranded-DNA binding function in protein-DNA covalent cross-link repair.",
                "molecular_function": TERM["GO:0003697"],
                "directly_involved_in": [TERM["GO:0106300"]],
                "support_term": "GO:0106300",
            }
        ],
    },
}


GENERIC_REVIEWS = {
    "GO:0000166": ("MARK_AS_OVER_ANNOTATED", "Nucleotide binding is too broad.", "A more specific ATP-dependent helicase or RNA helicase term is available where supported."),
    "GO:0003676": ("MARK_AS_OVER_ANNOTATED", "Nucleic acid binding is too broad.", "A DNA-binding or RNA-helicase term better captures the supported role where available."),
    "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is retained as architectural or substrate-binding context.", "DNA binding is real for IHF/CspD-family proteins, but a more specific architectural or regulatory role captures the core function where available."),
    "GO:0003723": ("KEEP_AS_NON_CORE", "RNA binding is retained as substrate context.", "RNA binding supports the RNA-helicase role but is less informative than the catalytic helicase activity."),
    "GO:0003724": ("ACCEPT", "RNA helicase activity is supported.", "UniProt EC/domain evidence and local family assignments support RNA helicase activity."),
    "GO:0004386": ("KEEP_AS_NON_CORE", "Generic helicase activity is retained as parent context.", "The RNA-helicase-family assignment is more specific where supported."),
    "GO:0005524": ("KEEP_AS_NON_CORE", "ATP binding is retained as cofactor context.", "ATP binding supports helicase activity but is not the most informative function."),
    "GO:0005694": ("ACCEPT", "Chromosome localization/context is retained.", "IHF is a chromosome-associated bacterial architectural DNA-binding factor."),
    "GO:0005737": ("ACCEPT", "Cytoplasm localization is retained.", "The localization is compatible with a soluble bacterial cold-shock-domain protein."),
    "GO:0005829": ("ACCEPT", "Cytosol localization is retained.", "The localization is compatible with soluble bacterial proteins in this bucket."),
    "GO:0006310": ("KEEP_AS_NON_CORE", "DNA recombination is retained as IHF context.", "IHF participates in recombination-related DNA architecture, but this bucket is not treated as DNA-repair core."),
    "GO:0006355": ("ACCEPT", "Regulation of DNA-templated transcription is supported.", "IHF/CspD family annotation and Pseudomonas promoter studies support regulatory DNA-binding context."),
    "GO:0006417": ("KEEP_AS_NON_CORE", "Regulation of translation is retained as family context.", "The broad UniRule row is compatible with IHF biology but is not the main routing decision here."),
    "GO:0006508": ("ACCEPT", "Proteolysis is supported.", "TldD/PmbA-family and metalloprotease evidence support proteolysis."),
    "GO:0006974": ("KEEP_AS_NON_CORE", "DNA damage response is retained as broad context.", "The more specific protein-DNA covalent cross-link repair term captures the supported SRAP/HMCES-like role."),
    "GO:0008237": ("ACCEPT", "Metallopeptidase activity is supported.", "TldD/PmbA U62 metalloprotease evidence supports this catalytic activity."),
    "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "Hydrolase activity is too broad.", "RNA helicase or ATP-dependent helicase activity is more informative."),
    "GO:0030527": ("ACCEPT", "Structural constituent of chromatin is supported.", "IHF alpha/beta are bacterial histone-like architectural DNA-binding proteins."),
    "GO:0032993": ("ACCEPT", "Protein-DNA complex membership is supported.", "IHF forms protein-DNA complexes at regulatory sites in Pseudomonas promoter studies."),
    "GO:0045892": ("ACCEPT", "Negative regulation of DNA-templated transcription is supported.", "Pseudomonas IHF promoter evidence supports promoter-specific repression/inhibition."),
    "GO:0045893": ("ACCEPT", "Positive regulation of DNA-templated transcription is supported.", "Pseudomonas IHF promoter evidence and CollecTF-derived activity rows support promoter-specific activation context."),
    "GO:0003697": ("ACCEPT", "Single-stranded DNA binding is supported.", "The InterPro SRAP/HMCES-family row directly supports single-stranded DNA binding in these abasic-site processing proteins."),
    "GO:0106300": ("ACCEPT", "Protein-DNA covalent cross-linking repair is supported.", "The InterPro SRAP/HMCES-family row directly supports protein-DNA covalent cross-link repair for these abasic-site processing proteins."),
}


GENE_REVIEWS = {
    "ihfA": {
        "GO:0000976": ("ACCEPT", "Transcription cis-regulatory region binding is supported.", "The CollecTF/PMID-backed Pseudomonas promoter rows and UniProt IHF function support IHF binding at promoter regulatory sites."),
        "GO:0001216": ("ACCEPT", "DNA-binding transcription activator activity is retained.", "The experimental CollecTF row and Pu-promoter study support promoter-specific IHF regulatory activation context."),
        "GO:0001217": ("ACCEPT", "DNA-binding transcription repressor activity is retained.", "The PhhR/phhAB promoter study reports IHF binding overlapping the PhhR site and inhibition of PhhR-dependent expression."),
    },
    "cspD": {
        "GO:0003676": ("MODIFY", "Nucleic acid binding is real but too broad for CspD.", "UniProt supports the more specific DNA binding term for this cold-shock-domain DNA-binding protein."),
        "GO:0003677": ("NEW", "DNA binding is added from UniProt metadata.", "The local UniProt record has a DNA-binding GO cross-reference and cold-shock-domain DNA-binding evidence."),
        "GO:0008156": ("NEW", "Negative regulation of DNA replication is added from UniProt metadata.", "The local UniProt record carries DNA replication inhibitor keyword and GO support for negative regulation of DNA replication."),
    },
    "hrpB": {
        "GO:0003724": ("NEW", "RNA helicase activity is added from HrpB-family evidence.", "The local UniProt record has HrpB RNA-helicase-family InterPro and PANTHER support even though fetched GOA contains only a generic helicase row."),
    },
    "PP_2493": {
        "GO:0008237": ("NEW", "Metallopeptidase activity is added from UniProt keyword/domain evidence.", "The local UniProt record carries metallopeptidase, MPN, RadC_JAB, UPF0758, and RadC-family support; direct DNA-repair process evidence is not added in this first pass."),
        "GO:0006508": ("NEW", "Proteolysis is added from UniProt keyword evidence.", "The local UniProt record has a proteolysis GO cross-reference, but the physiological substrate and DNA-repair relationship remain unresolved."),
    },
}


PROPOSED_REPLACEMENTS = {
    ("cspD", "GO:0003676"): [TERM["GO:0003677"]],
}


NEW_QUALIFIERS = {
    "GO:0003677": "enables",
    "GO:0003724": "enables",
    "GO:0008237": "enables",
    "GO:0006508": "involved_in",
    "GO:0008156": "involved_in",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def optional_first_line(path: Path, *needles: str) -> str | None:
    if not path.exists():
        return None
    for line in read_text(path).splitlines():
        if all(needle in line for needle in needles):
            return line
    return None


def prefixed_lines(path: Path, prefix: str, limit: int = 5) -> list[str]:
    if not path.exists():
        return []
    return [line for line in read_text(path).splitlines() if line.startswith(prefix)][:limit]


def support(reference_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": reference_id, "supporting_text": text}


def add_unique(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item not in items:
        items.append(item)


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def goa_support(gene: str, term_id: str | None) -> dict[str, str] | None:
    if not term_id:
        return None
    return support(file_id(gene, "goa.tsv"), optional_first_line(GENE_ROOT / gene / f"{gene}-goa.tsv", term_id))


def uniprot_evidence(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    items: list[dict[str, str]] = []
    add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, "DE   RecName")))
    add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, "DE   SubName")))
    if term_id:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, f"DR   GO; {term_id};")))
    for marker in (
        "CC   -!- FUNCTION:",
        "specific DNA-binding protein",
        "CC   -!- CATALYTIC ACTIVITY:",
        "DR   PANTHER;",
        "DR   Pfam;",
        "KW   ",
        "FT   DOMAIN",
    ):
        line = optional_first_line(path, marker)
        if line and "Reference proteome" not in line:
            add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    for line in prefixed_lines(path, "DR   InterPro;", 8):
        add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    return items


def asta_evidence(gene: str) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    items: list[dict[str, str]] = []
    if not path.exists():
        return items
    for marker in ("  uniprot_accession:", "  protein_description:", "  protein_family:", "  protein_domains:"):
        line = optional_first_line(path, marker)
        if line and "Not specified in UniProt" not in line:
            add_unique(items, support(file_id(gene, "deep-research-asta.md"), line))
    return items


def publication_evidence(gene: str, term_id: str | None) -> list[dict[str, str]]:
    if gene != "ihfA":
        return []
    items: list[dict[str, str]] = []
    if term_id in {"GO:0000976", "GO:0001217", "GO:0032993", "GO:0045892"}:
        path = ROOT / "publications" / "PMID_17217960.md"
        add_unique(items, support("PMID:17217960", optional_first_line(path, "An IHF binding site overlaps")))
        add_unique(items, support("PMID:17217960", optional_first_line(path, "indeed inhibits PhhR-dependent")))
    if term_id in {"GO:0000976", "GO:0001216", "GO:0032993", "GO:0045893"}:
        path = ROOT / "publications" / "PMID_21958188.md"
        add_unique(items, support("PMID:21958188", optional_first_line(path, "connects cell growth to")))
        add_unique(items, support("PMID:21958188", optional_first_line(path, "IHF-DNA interaction")))
    return items


def standard_support(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    add_unique(items, goa_support(gene, term_id))
    for item in uniprot_evidence(gene, term_id):
        add_unique(items, item)
    for item in asta_evidence(gene):
        add_unique(items, item)
    for item in publication_evidence(gene, term_id):
        add_unique(items, item)
    return items


def reference_list(existing_refs: list[dict] | None, gene: str, accession: str) -> list[dict]:
    refs: list[dict] = []
    seen = set()
    for ref in existing_refs or []:
        seen.add(ref["id"])
        refs.append(ref)
    for ref_id, title in {
        file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({accession})",
        file_id(gene, "uniprot.txt"): f"UniProtKB entry for {gene} ({accession})",
        file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({accession})",
    }.items():
        if ref_id not in seen and (GENE_ROOT / gene / ref_id.split("/")[-1]).exists():
            refs.append({"id": ref_id, "title": title, "findings": []})
            seen.add(ref_id)
    return refs


def review_for_annotation(gene: str, term_id: str) -> dict:
    action, summary, reason = GENE_REVIEWS.get(gene, {}).get(term_id) or GENERIC_REVIEWS[term_id]
    review = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": standard_support(gene, term_id),
    }
    replacements = PROPOSED_REPLACEMENTS.get((gene, term_id))
    if replacements:
        review["proposed_replacement_terms"] = replacements
    return review


def new_annotation(gene: str, term_id: str) -> dict:
    return {
        "term": TERM[term_id],
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": NEW_QUALIFIERS[term_id],
        "review": review_for_annotation(gene, term_id),
    }


def core_functions(gene: str) -> list[dict]:
    cores = []
    for item in GENE_INFO[gene]["core"]:
        core = {"description": item["description"], "supported_by": standard_support(gene, item.get("support_term"))}
        for key in ("molecular_function", "directly_involved_in", "locations"):
            if key in item:
                core[key] = item[key]
        cores.append(core)
    return cores


def suggested_question(gene: str) -> str:
    return {
        "tldD": "What physiological substrate and partner context define KT2440 TldD protease activity?",
        "ihfB": "Which KT2440 promoters or recombination substrates require the IHF beta-containing heterodimer?",
        "ihfA": "Which Pseudomonas putida promoters are directly activated or repressed by IHF alpha-containing complexes?",
        "cspD": "Does KT2440 CspD inhibit DNA replication under stationary-phase, cold-shock, or stress-specific conditions?",
        "hrpA": "Which RNA substrates or RNA-processing pathway use KT2440 HrpA helicase activity?",
        "hrpB": "Does KT2440 HrpB act as an RNA helicase in RNA processing, transcription coupling, or another nucleic-acid pathway?",
        "PP_0758": "Does PP_0758 form SRAP/HMCES-like DNA-protein cross-link intermediates at abasic sites in KT2440?",
        "PP_2493": "Is PP_2493 an active RadC/UPF0758-family metallopeptidase, and does it participate directly in DNA repair?",
        "PP_2941": "Does PP_2941 form SRAP/HMCES-like DNA-protein cross-link intermediates at abasic sites in KT2440?",
    }[gene]


def suggested_experiment(gene: str) -> dict:
    specific = {
        "PP_0758": "Assay purified PP_0758 with abasic-site-containing single-stranded DNA and test for SRAP/HMCES-like covalent DNA-protein cross-link formation and resolution.",
        "PP_2493": "Test PP_2493 for zinc/metal-dependent peptidase activity against candidate protein substrates and compare DNA-damage sensitivity of a deletion strain.",
        "PP_2941": "Assay purified PP_2941 with abasic-site-containing single-stranded DNA and test for SRAP/HMCES-like covalent DNA-protein cross-link formation and resolution.",
    }
    return {
        "experiment_type": "targeted activity and pathway validation",
        "description": specific.get(
            gene,
            f"Test {gene} with the substrate class implied by its curated role and compare deletion or depletion phenotypes under the relevant protease, transcription-regulatory, replication-inhibition, RNA-processing, or chaperone context.",
        ),
    }


def apply_review(gene: str) -> None:
    info = GENE_INFO[gene]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(read_text(path))
    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = info["description"]
    data["references"] = reference_list(data.get("references"), gene, info["accession"])
    existing = data.get("existing_annotations") or []
    for annotation in existing:
        annotation["review"] = review_for_annotation(gene, annotation["term"]["id"])
    for term_id in info.get("new_terms", []):
        if term_id not in {annotation["term"]["id"] for annotation in existing}:
            existing.append(new_annotation(gene, term_id))
    data["existing_annotations"] = existing
    data["core_functions"] = core_functions(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": suggested_question(gene), "experts": []}]
    data["suggested_experiments"] = [suggested_experiment(gene)]
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str) -> None:
    info = GENE_INFO[gene]
    path = GENE_ROOT / gene / f"{gene}-notes.md"
    support_term = info["core"][0].get("support_term") if info["core"] else None
    evidence = standard_support(gene, support_term)
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass curation for the architectural/RNA-helicase/chaperone/protease spillover bucket.",
        info["description"],
        "",
        "Primary provenance:",
    ]
    seen = set()
    for item in evidence:
        key = (item["reference_id"], item["supporting_text"])
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"- [{item['reference_id']} \"{item['supporting_text']}\"]")
        if len(seen) >= 10:
            break
    if gene in {"PP_0758", "PP_2941"}:
        decision = "Decision: treat as SRAP/HMCES-like protein-DNA covalent cross-link repair boundary genes, not as general protein-turnover proteases."
    elif gene == "PP_2493":
        decision = "Decision: curate predicted metallopeptidase/proteolysis from the RadC/JAB/MPN evidence, but do not add a DNA-repair process without direct support."
    else:
        decision = "Decision: route outside DNA repair/replication core unless future organism-specific evidence shows a direct DNA-maintenance role."
    lines.extend(["", decision, ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def descriptor(term_id: str) -> dict:
    return {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]}


def annoton(
    annoton_id: str,
    gene: str,
    role: str,
    function: str | None = None,
    processes: list[str] | None = None,
    locations: list[str] | None = None,
) -> dict:
    data = {
        "id": annoton_id,
        "label": f"{gene}: {role}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": role,
    }
    if function:
        data["function"] = descriptor(function)
    if processes:
        data["processes"] = [descriptor(term_id) for term_id in processes]
    if locations:
        data["locations"] = [descriptor(term_id) for term_id in locations]
    return data


def module_gene_statement(gene: str) -> str:
    if gene in {"PP_0758", "PP_2941"}:
        return f"The {gene} review records SRAP/HMCES-like protein-DNA covalent cross-link repair, while avoiding generic protein-turnover protease over-curation."
    if gene == "PP_2493":
        return "The PP_2493 review records conservative RadC/JAB/MPN metalloprotease-like curation without asserting a direct DNA-repair process."
    return f"The {gene} review records the non-DNA-repair routing decision for this spillover member."


def module_review() -> dict:
    return {
        "id": "MODULE:dna_bucket_architectural_rna_protein_spillover_boundary",
        "title": "DNA-bucket architectural, RNA-helicase, chaperone, and protease spillover boundary",
        "description": "Boundary module for PSEPK genes that entered the DNA replication/repair/recombination umbrella through broad DNA, helicase, inhibitor, or stress keywords but resolve to architectural DNA-binding, RNA helicase, protein-folding, or protease contexts.",
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{DNA_SPILLOVER_TSV}",
                "title": "PSEPK architectural/RNA/protein spillover split table",
                "statement": "The split table records seven genes pulled from the broad DNA replication/repair/recombination functional bucket and routed to non-DNA-repair contexts.",
            },
            {
                "source_id": f"file:{PROTEIN_TURNOVER_DNA_SPILLOVER_TSV}",
                "title": "PSEPK protein-turnover DNA-damage spillover split table",
                "statement": "The split table records three protein-folding/turnover genes whose protease-like keywords overlap DNA-damage or RadC/SRAP-family repair context.",
            },
            {
                "source_id": "file:PSEPK/dnaJ/dnaJ-ai-review.yaml",
                "title": "Curated dnaJ review",
                "statement": "The dnaJ review supports DnaJ as a DnaK/Hsp70 co-chaperone with protein-folding, protein-refolding, ATPase-activator, and chaperone-binding roles.",
            },
        ]
        + [
            {
                "source_id": f"file:PSEPK/{gene}/{gene}-ai-review.yaml",
                "title": f"Curated {gene} review",
                "statement": module_gene_statement(gene),
            }
            for gene in GENE_INFO
        ],
        "notes": "First-pass boundary. TldD is retained as metalloprotease/proteolysis; IHF alpha/beta as architectural and regulatory DNA-binding; CspD as cold-shock-domain DNA-binding replication inhibitor context; HrpA/HrpB as RNA-helicase-family proteins; DnaJ as DnaK-system chaperone context. PP_0758 and PP_2941 are SRAP/HMCES-like protein-DNA cross-link repair proteins, while PP_2493 is retained conservatively as a RadC/JAB/MPN metalloprotease-like spillover pending direct DNA-repair evidence.",
        "module": {
            "id": "dna_bucket_architectural_rna_protein_spillover_boundary",
            "label": "DNA-bucket architectural/RNA/protein spillover boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {**descriptor("GO:0008237"), "description": "TldD/PmbA metallopeptidase activity."},
                {**descriptor("GO:0006508"), "description": "Proteolysis context for TldD."},
                {**descriptor("GO:0030527"), "description": "IHF bacterial histone-like architectural DNA-binding role."},
                {**descriptor("GO:0000976"), "description": "IHF binding at transcriptional regulatory DNA regions."},
                {**descriptor("GO:0008156"), "description": "CspD negative regulation of DNA replication context."},
                {**descriptor("GO:0003724"), "description": "HrpA/HrpB RNA helicase activity."},
                {**descriptor("GO:0001671"), "description": "DnaJ activation of partner DnaK ATPase activity."},
                {**descriptor("GO:0006457"), "description": "DnaJ protein-folding pathway context."},
                {**descriptor("GO:0003697"), "description": "SRAP/HMCES-like single-stranded-DNA binding."},
                {**descriptor("GO:0106300"), "description": "Protein-DNA covalent cross-link repair context."},
            ],
            "context": {
                "cellular_components": [
                    {**descriptor("GO:0005737"), "description": "Bacterial cytoplasm context."},
                    {**descriptor("GO:0005829"), "description": "Bacterial cytosol context."},
                    {**descriptor("GO:0005694"), "description": "Chromosome-associated architectural context."},
                    {**descriptor("GO:0032993"), "description": "IHF protein-DNA complex context."},
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "Protease spillover",
                    "node": {
                        "id": "tldd_metalloprotease_context",
                        "label": "TldD metalloprotease context",
                        "module_type": "MOLECULAR_FUNCTION",
                        "annotons": [
                            annoton("tldd_metallopeptidase", "tldD", "TldD/PmbA-family metallopeptidase.", function="GO:0008237", processes=["GO:0006508"], locations=["GO:0005829"]),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "Architectural and regulatory DNA-binding spillovers",
                    "node": {
                        "id": "ihf_architectural_regulatory_context",
                        "label": "IHF architectural/regulatory context",
                        "module_type": "MOLECULAR_FUNCTION",
                        "description": "IHF alpha/beta are retained as bacterial architectural/regulatory DNA-binding proteins, not DNA-repair enzymes.",
                        "annotons": [
                            annoton("ihfb_structural_constituent", "ihfB", "IHF beta architectural DNA-binding subunit.", function="GO:0030527", processes=["GO:0006355"], locations=["GO:0005694", "GO:0005829"]),
                            annoton("ihfa_promoter_binding", "ihfA", "IHF alpha regulatory-site DNA-binding subunit.", function="GO:0000976", processes=["GO:0045892", "GO:0045893"], locations=["GO:0032993", "GO:0005829"]),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "Cold-shock DNA-binding replication-inhibitor context",
                    "node": {
                        "id": "cspd_cold_shock_replication_inhibitor_context",
                        "label": "CspD cold-shock DNA-binding context",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "annotons": [
                            annoton("cspd_dna_binding_replication_inhibitor", "cspD", "Cold-shock-domain DNA-binding replication inhibitor context.", function="GO:0003677", processes=["GO:0008156"], locations=["GO:0005737", "GO:0005829"]),
                        ],
                    },
                },
                {
                    "order": 4,
                    "role": "RNA helicase spillovers",
                    "node": {
                        "id": "hrpa_hrpb_rna_helicase_context",
                        "label": "HrpA/HrpB RNA helicase context",
                        "module_type": "MOLECULAR_FUNCTION",
                        "annotons": [
                            annoton("hrpa_rna_helicase", "hrpA", "DEAD/DEAH-family ATP-dependent RNA helicase.", function="GO:0003724"),
                            annoton("hrpb_rna_helicase", "hrpB", "HrpB-family ATP-dependent RNA helicase candidate.", function="GO:0003724"),
                        ],
                    },
                },
                {
                    "order": 5,
                    "role": "Protein-folding chaperone spillover",
                    "node": {
                        "id": "dnaj_chaperone_context",
                        "label": "DnaJ chaperone context",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "DnaJ is already curated as a DnaK-system co-chaperone and is included here only to close the DNA-bucket spillover route.",
                        "annotons": [
                            annoton("dnaj_atpase_activator_chaperone", "dnaJ", "DnaK-system ATPase-activating co-chaperone.", function="GO:0001671", processes=["GO:0006457", "GO:0042026"], locations=["GO:0005737"]),
                        ],
                    },
                },
                {
                    "order": 6,
                    "role": "SRAP/HMCES protein-DNA cross-link repair boundary",
                    "node": {
                        "id": "srap_hmces_crosslink_repair_context",
                        "label": "SRAP/HMCES protein-DNA cross-link repair context",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "SRAP/HMCES-like proteins entered the protein-turnover bucket through protease-like keywords but are curated here as DNA-damage repair boundary proteins.",
                        "annotons": [
                            annoton("pp0758_srap_crosslink_repair", "PP_0758", "SRAP/HMCES-like abasic-site processing protein.", function="GO:0003697", processes=["GO:0106300"]),
                            annoton("pp2941_srap_crosslink_repair", "PP_2941", "SRAP/HMCES-like abasic-site processing protein.", function="GO:0003697", processes=["GO:0106300"]),
                        ],
                    },
                },
                {
                    "order": 7,
                    "role": "RadC/JAB metalloprotease-like spillover",
                    "node": {
                        "id": "radc_jab_metalloprotease_like_context",
                        "label": "RadC/JAB metalloprotease-like context",
                        "module_type": "MOLECULAR_FUNCTION",
                        "description": "PP_2493 has RadC/UPF0758/JAB/MPN support for a metalloprotease-like role, but direct DNA-repair process evidence is not asserted.",
                        "annotons": [
                            annoton("pp2493_radc_jab_metallopeptidase", "PP_2493", "RadC/UPF0758-family MPN/JAB-domain metallopeptidase-like protein.", function="GO:0008237", processes=["GO:0006508"]),
                        ],
                    },
                },
            ],
        },
    }


def main() -> None:
    for gene in GENE_INFO:
        apply_review(gene)
        write_notes(gene)
    MODULE_PATH.write_text(yaml.dump(module_review(), Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


if __name__ == "__main__":
    main()
