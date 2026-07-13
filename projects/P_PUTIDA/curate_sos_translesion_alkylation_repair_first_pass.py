#!/usr/bin/env python3
"""First-pass curation for the PSEPK SOS/translesion/alkylation-repair split."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "dna_damage_response_translesion_repair_boundary.yaml"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0000166": {"id": "GO:0000166", "label": "nucleotide binding"},
    "GO:0003676": {"id": "GO:0003676", "label": "nucleic acid binding"},
    "GO:0003677": {"id": "GO:0003677", "label": "DNA binding"},
    "GO:0003684": {"id": "GO:0003684", "label": "damaged DNA binding"},
    "GO:0003824": {"id": "GO:0003824", "label": "catalytic activity"},
    "GO:0003887": {"id": "GO:0003887", "label": "DNA-directed DNA polymerase activity"},
    "GO:0003908": {"id": "GO:0003908", "label": "methylated-DNA-[protein]-cysteine S-methyltransferase activity"},
    "GO:0004252": {"id": "GO:0004252", "label": "serine-type endopeptidase activity"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0006260": {"id": "GO:0006260", "label": "DNA replication"},
    "GO:0006281": {"id": "GO:0006281", "label": "DNA repair"},
    "GO:0006307": {"id": "GO:0006307", "label": "DNA alkylation repair"},
    "GO:0006355": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "GO:0006508": {"id": "GO:0006508", "label": "proteolysis"},
    "GO:0006974": {"id": "GO:0006974", "label": "DNA damage response"},
    "GO:0008296": {"id": "GO:0008296", "label": "3'-5'-DNA exonuclease activity"},
    "GO:0008408": {"id": "GO:0008408", "label": "3'-5' exonuclease activity"},
    "GO:0008413": {"id": "GO:0008413", "label": "8-oxo-7,8-dihydroguanosine triphosphate pyrophosphatase activity"},
    "GO:0009432": {"id": "GO:0009432", "label": "SOS response"},
    "GO:0001217": {"id": "GO:0001217", "label": "DNA-binding transcription repressor activity"},
    "GO:0016787": {"id": "GO:0016787", "label": "hydrolase activity"},
    "GO:0034061": {"id": "GO:0034061", "label": "DNA polymerase activity"},
    "GO:0035539": {"id": "GO:0035539", "label": "8-oxo-7,8-dihydrodeoxyguanosine triphosphate pyrophosphatase activity"},
    "GO:0042276": {"id": "GO:0042276", "label": "error-prone translesion synthesis"},
    "GO:0044715": {"id": "GO:0044715", "label": "8-oxo-dGDP phosphatase activity"},
    "GO:0044716": {"id": "GO:0044716", "label": "8-oxo-GDP phosphatase activity"},
    "GO:0045004": {"id": "GO:0045004", "label": "DNA replication proofreading"},
    "GO:0045892": {"id": "GO:0045892", "label": "negative regulation of DNA-templated transcription"},
    "GO:0046872": {"id": "GO:0046872", "label": "metal ion binding"},
    "GO:0071897": {"id": "GO:0071897", "label": "DNA biosynthetic process"},
}


PUBS = {
    "PMID:17933893": "Cohabitation of two different lexA regulons in Pseudomonas putida.",
    "PMID:15458417": "Widespread distribution of a lexA-regulated DNA damage-inducible multiple gene cassette in the Proteobacteria phylum.",
}


GENE_INFO = {
    "PP_1348": {
        "accession": "Q88N67",
        "description": (
            "PP_1348 encodes a MutT-like Nudix hydrolase in Pseudomonas putida KT2440. "
            "UniProt, EC, InterPro, Pfam, and PANTHER metadata support 8-oxo-dGTP/"
            "8-oxo-GTP phosphohydrolase activity that sanitizes oxidized guanine "
            "nucleotide pools and thereby reduces mutagenic incorporation during DNA "
            "replication and repair contexts."
        ),
        "core": [
            {
                "description": "MutT-like oxidized guanine nucleotide triphosphatase sanitizing 8-oxo-dGTP pools.",
                "molecular_function": TERM["GO:0035539"],
                "directly_involved_in": [TERM["GO:0006281"]],
                "support_term": "GO:0035539",
            }
        ],
    },
    "lexA1": {
        "accession": "P0A153",
        "description": (
            "lexA1 encodes the conventional LexA repressor in Pseudomonas putida KT2440. "
            "It is a LexA-family DNA-binding transcriptional repressor and RecA-stimulated "
            "autocleaving serine peptidase that controls the main E. coli-like SOS regulon "
            "in KT2440, in contrast to the narrower lexA2-imuA-imuB-dnaE2 cassette regulator."
        ),
        "core": [
            {
                "description": "DNA-binding transcriptional repressor controlling the conventional SOS regulon.",
                "molecular_function": TERM["GO:0001217"],
                "directly_involved_in": [TERM["GO:0045892"], TERM["GO:0009432"]],
                "support_term": "GO:0045892",
            },
            {
                "description": "LexA-family autocleavage activity enabling RecA-stimulated SOS derepression.",
                "molecular_function": TERM["GO:0004252"],
                "support_term": "GO:0004252",
            },
        ],
        "new_terms": ["GO:0001217"],
        "pubs": ["PMID:17933893"],
    },
    "polB": {
        "accession": "Q88K98",
        "description": (
            "polB encodes a type-B/DNA polymerase II-like DNA polymerase in Pseudomonas "
            "putida KT2440. The protein has DNA polymerase B catalytic and exonuclease "
            "domains, supporting DNA-directed DNA polymerase activity plus 3'-5' "
            "exonuclease/proofreading context. TreeGrafter SOS-response placement is "
            "retained as damage-response context rather than a direct regulatory role."
        ),
        "core": [
            {
                "description": "Type-B DNA polymerase catalytic activity for DNA synthesis in repair/replication-associated contexts.",
                "molecular_function": TERM["GO:0003887"],
                "support_term": "GO:0003887",
            },
            {
                "description": "Associated 3'-5' exonuclease/proofreading activity from the PolB exonuclease domain.",
                "molecular_function": TERM["GO:0008296"],
                "directly_involved_in": [TERM["GO:0045004"]],
                "support_term": "GO:0008296",
            },
        ],
    },
    "ogt": {
        "accession": "Q88II2",
        "description": (
            "ogt encodes O6-alkylguanine-DNA alkyltransferase/MGMT in Pseudomonas putida "
            "KT2440. It repairs O6-methylguanine and O4-methylthymine lesions by "
            "stoichiometric transfer of the alkyl group from damaged DNA to an active-site "
            "cysteine, a suicide methyltransferase reaction in the cytoplasm."
        ),
        "core": [
            {
                "description": "MGMT/Ogt suicide methyltransferase repairing alkylated DNA bases.",
                "molecular_function": TERM["GO:0003908"],
                "directly_involved_in": [TERM["GO:0006307"]],
                "locations": [TERM["GO:0005737"]],
                "support_term": "GO:0003908",
            }
        ],
    },
    "imuB": {
        "accession": "Q88I83",
        "description": (
            "imuB encodes a conserved ImuB/UmuC-like DNA-damage-tolerance accessory protein "
            "in the lexA2-imuA-imuB-dnaE2 cassette of Pseudomonas putida KT2440. Current "
            "metadata support DNA repair context and UmuC/IMS-family domains, but no precise "
            "standalone molecular function is resolved in this first pass."
        ),
        "core": [
            {
                "description": "ImuB-family accessory protein in the LexA2-regulated mutagenic DNA damage tolerance cassette.",
                "directly_involved_in": [TERM["GO:0006281"]],
                "support_term": "GO:0006281",
            }
        ],
        "pubs": ["PMID:17933893", "PMID:15458417"],
    },
    "dnaE2": {
        "accession": "Q88I82",
        "description": (
            "dnaE2 encodes an error-prone DnaE2-family DNA polymerase in Pseudomonas putida "
            "KT2440. UniProt/HAMAP describes a cytoplasmic DNA polymerase involved in "
            "damage-induced mutagenesis and translesion synthesis, not the major replicative "
            "DNA polymerase. It is part of the lexA2-imuA-imuB-dnaE2 damage-inducible cassette."
        ),
        "core": [
            {
                "description": "Error-prone DnaE2 DNA polymerase acting in damage-induced mutagenesis/translesion synthesis.",
                "molecular_function": TERM["GO:0003887"],
                "directly_involved_in": [TERM["GO:0042276"], TERM["GO:0006281"]],
                "locations": [TERM["GO:0005737"]],
                "support_term": "GO:0003887",
            }
        ],
        "new_terms": ["GO:0042276"],
        "pubs": ["PMID:17933893", "PMID:15458417"],
    },
    "PP_5679": {
        "accession": "A0A140FWN1",
        "description": (
            "PP_5679 encodes a small protein containing a DNA polymerase Y-family little-finger/"
            "IMS_C domain. The current metadata support damaged-DNA binding and DNA repair context "
            "but do not show a catalytic polymerase domain, so this first pass treats PP_5679 as "
            "a low-information Y-family accessory/domain protein rather than as an active polymerase."
        ),
        "core": [
            {
                "description": "Y-family little-finger domain protein with damaged-DNA-binding context but unresolved catalytic role.",
                "molecular_function": TERM["GO:0003684"],
                "support_term": "GO:0003684",
            }
        ],
    },
}


REVIEWS = {
    "PP_1348": {
        "GO:0006281": ("ACCEPT", "DNA repair is accepted as oxidized nucleotide-pool sanitation context.", "MutT-like hydrolysis of 8-oxo-dGTP prevents mutagenic oxidized nucleotide incorporation and is commonly treated as DNA-repair/genome-maintenance context."),
        "GO:0008413": ("ACCEPT", "8-oxo-GTP pyrophosphatase activity is supported by UniProt catalytic-activity metadata.", "The protein is a MutT-like Nudix hydrolase with an explicit 8-oxo-GTP reaction in UniProt."),
        "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "Generic hydrolase activity is much broader than the oxidized guanine nucleotide hydrolase terms.", "The specific 8-oxo-dGTP and 8-oxo-GTP pyrophosphatase terms are already present."),
        "GO:0035539": ("ACCEPT", "8-oxo-dGTP pyrophosphatase activity is the core PP_1348 molecular function.", "UniProt EC 3.6.1.55 and MutT/Nudix family metadata support this activity."),
        "GO:0044715": ("KEEP_AS_NON_CORE", "8-oxo-dGDP phosphatase activity is plausible substrate-range context from TreeGrafter.", "The strongest first-pass evidence is for triphosphate substrates; diphosphate activity is retained as non-core substrate-range context."),
        "GO:0044716": ("KEEP_AS_NON_CORE", "8-oxo-GDP phosphatase activity is plausible substrate-range context from TreeGrafter.", "The strongest first-pass evidence is for triphosphate substrates; diphosphate activity is retained as non-core substrate-range context."),
        "GO:0046872": ("KEEP_AS_NON_CORE", "Metal ion binding is cofactor context for a Nudix hydrolase.", "This supports the enzyme mechanism but is less informative than the oxidized nucleotide hydrolase activity."),
    },
    "lexA1": {
        "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is correct but less specific than DNA-binding transcription repressor activity.", "LexA1 binds operator DNA as a transcriptional repressor; a specific NEW repressor activity is added."),
        "GO:0004252": ("ACCEPT", "LexA-family serine endopeptidase/autocleavage activity is supported.", "UniProt/HAMAP records hydrolysis of the Ala-Gly bond in LexA and RecA-stimulated autocleavage."),
        "GO:0006260": ("MARK_AS_OVER_ANNOTATED", "DNA replication is downstream SOS-regulon context, not a direct LexA1 function.", "LexA1 represses DNA-damage response genes; it is not a replication enzyme."),
        "GO:0006281": ("KEEP_AS_NON_CORE", "DNA repair is downstream regulon context for LexA1.", "LexA1 controls the conventional SOS response, which includes repair genes, but its direct function is transcriptional repression and autocleavage."),
        "GO:0006355": ("MARK_AS_OVER_ANNOTATED", "Generic transcription regulation is true but less specific than negative regulation by a DNA-binding repressor.", "GO:0045892 and the NEW GO:0001217 row capture the direct function better."),
        "GO:0006508": ("KEEP_AS_NON_CORE", "Proteolysis is broad context for LexA autocleavage.", "The specific serine-type endopeptidase activity is retained as the direct molecular function."),
        "GO:0006974": ("KEEP_AS_NON_CORE", "DNA damage response is correct context for the SOS repressor.", "LexA1 is a regulator of the response rather than a repair enzyme."),
        "GO:0009432": ("ACCEPT", "LexA1 is the main conventional SOS-response regulator in KT2440.", "The KT2440 LexA regulon study states that LexA1 controls the conventional E. coli-like SOS response."),
        "GO:0045892": ("ACCEPT", "Negative regulation of DNA-templated transcription is the core LexA1 biological process.", "LexA1 represses SOS regulon transcription until RecA-stimulated autocleavage causes derepression."),
        "GO:0001217": ("NEW", "Specific DNA-binding transcription repressor activity should be recorded for LexA1.", "LexA1 is a LexA-family DNA-binding transcriptional repressor controlling the conventional SOS regulon."),
    },
    "polB": {
        "GO:0000166": ("KEEP_AS_NON_CORE", "Nucleotide binding is broad substrate context for a polymerase.", "The DNA-directed DNA polymerase term captures the direct activity more specifically."),
        "GO:0003676": ("MARK_AS_OVER_ANNOTATED", "Nucleic acid binding is broader than DNA binding and polymerase activity.", "The protein is a DNA polymerase; generic nucleic-acid binding adds little."),
        "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected for PolB but less specific than polymerase and exonuclease activities.", "DNA binding is substrate context for the type-B polymerase."),
        "GO:0003887": ("ACCEPT", "DNA-directed DNA polymerase activity is the core PolB molecular function.", "UniProt/RuleBase and EC metadata support a type-B DNA polymerase."),
        "GO:0008296": ("ACCEPT", "3'-5'-DNA exonuclease activity is supported by PolB exonuclease-domain evidence.", "TreeGrafter and domain metadata support the proofreading/exonuclease component."),
        "GO:0009432": ("KEEP_AS_NON_CORE", "SOS response is plausible damage-response context but not PolB's direct activity.", "PolB is a polymerase/exonuclease; SOS assignment is retained as non-core context."),
        "GO:0034061": ("MARK_AS_OVER_ANNOTATED", "DNA polymerase activity is a parent of the more specific DNA-directed DNA polymerase term.", "GO:0003887 should carry the core activity."),
        "GO:0045004": ("ACCEPT", "DNA replication proofreading is compatible with the PolB 3'-5' exonuclease domain.", "This is retained as the process context for the exonuclease/proofreading function."),
        "GO:0071897": ("KEEP_AS_NON_CORE", "DNA biosynthetic process is correct but broad polymerase context.", "The molecular function is more informative than this broad process term."),
    },
    "ogt": {
        "GO:0003824": ("MARK_AS_OVER_ANNOTATED", "Generic catalytic activity is uninformative for Ogt.", "The specific methylated-DNA cysteine S-methyltransferase term is present."),
        "GO:0003908": ("ACCEPT", "Methylated-DNA-[protein]-cysteine S-methyltransferase activity is the core Ogt function.", "UniProt/HAMAP describes stoichiometric transfer of alkyl groups from damaged DNA to an active-site cysteine."),
        "GO:0005737": ("ACCEPT", "Cytoplasm is the supported bacterial Ogt location.", "UniProt/HAMAP records cytoplasmic localization."),
        "GO:0006281": ("ACCEPT", "DNA repair is correct for Ogt.", "Ogt directly repairs alkylated DNA bases."),
        "GO:0006307": ("ACCEPT", "DNA alkylation repair is the core Ogt process.", "The protein specifically repairs O6-methylguanine and O4-methylthymine lesions."),
    },
    "imuB": {
        "GO:0006281": ("ACCEPT", "DNA repair is the best current GOA process context for ImuB.", "The protein is part of the LexA2-regulated damage-inducible cassette and carries UmuC/IMS domain evidence, but no standalone MF is resolved."),
    },
    "dnaE2": {
        "GO:0003676": ("KEEP_AS_NON_CORE", "Nucleic acid binding is broad substrate context for DnaE2.", "The DNA-directed DNA polymerase activity captures the molecular function better."),
        "GO:0003824": ("MARK_AS_OVER_ANNOTATED", "Generic catalytic activity is uninformative for DnaE2.", "The specific DNA-directed DNA polymerase activity is present."),
        "GO:0003887": ("ACCEPT", "DNA-directed DNA polymerase activity is the core DnaE2 molecular function.", "UniProt/HAMAP describes DnaE2 as an error-prone DNA polymerase."),
        "GO:0005737": ("ACCEPT", "Cytoplasm is the supported DnaE2 location.", "UniProt/HAMAP records cytoplasmic localization."),
        "GO:0006260": ("KEEP_AS_NON_CORE", "DNA replication is broad context; DnaE2 is not the major replicative polymerase.", "UniProt explicitly says DnaE2 is not the major replicative DNA polymerase."),
        "GO:0006281": ("ACCEPT", "DNA repair is accepted as damage-tolerance context for DnaE2.", "DnaE2 is involved in damage-induced mutagenesis and translesion synthesis."),
        "GO:0006974": ("ACCEPT", "DNA damage response is correct DnaE2 process context.", "DnaE2 acts in a damage-inducible mutagenesis cassette."),
        "GO:0008408": ("KEEP_AS_NON_CORE", "3'-5' exonuclease activity is retained as domain-derived context, not the defining DnaE2 function.", "The first-pass core function is error-prone polymerase/TLS activity."),
        "GO:0034061": ("MARK_AS_OVER_ANNOTATED", "DNA polymerase activity is a parent of DNA-directed DNA polymerase activity.", "GO:0003887 is more specific."),
        "GO:0071897": ("KEEP_AS_NON_CORE", "DNA biosynthetic process is broad polymerase context.", "The direct process is better represented by DNA repair/TLS context."),
        "GO:0042276": ("NEW", "Error-prone translesion synthesis should be added for DnaE2.", "UniProt/HAMAP explicitly describes DnaE2 as involved in damage-induced mutagenesis and translesion synthesis."),
    },
    "PP_5679": {
        "GO:0003684": ("ACCEPT", "Damaged DNA binding is the best supported PP_5679 function.", "The protein contains only a Y-family little-finger/IMS_C domain in current metadata."),
        "GO:0006281": ("KEEP_AS_NON_CORE", "DNA repair is retained as context for a damaged-DNA-binding Y-family domain protein.", "No catalytic polymerase domain or specific repair step is resolved."),
    },
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_lines(path: Path) -> list[str]:
    return read_text(path).splitlines()


def optional_first_line(path: Path, *needles: str) -> str | None:
    for line in read_lines(path):
        if all(needle in line for needle in needles):
            return line
    return None


def prefixed_lines(path: Path, prefix: str, limit: int = 5) -> list[str]:
    return [line for line in read_lines(path) if line.startswith(prefix)][:limit]


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": reference_id, "supporting_text": text}


def add_unique(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if not item:
        return
    key = (item["reference_id"], item["supporting_text"])
    if key not in {(existing["reference_id"], existing["supporting_text"]) for existing in items}:
        items.append(item)


def goa_support(gene: str, term_id: str | None) -> dict[str, str] | None:
    if not term_id:
        return None
    return support(file_id(gene, "goa.tsv"), optional_first_line(GENE_ROOT / gene / f"{gene}-goa.tsv", term_id))


def pub_support(pmid: str, *needles: str) -> dict[str, str] | None:
    path = ROOT / "publications" / f"{pmid.replace(':', '_')}.md"
    return support(pmid, optional_first_line(path, *needles))


def uniprot_evidence(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    items: list[dict[str, str]] = []
    add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, "DE   RecName")))
    add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, "DE   SubName")))
    if term_id:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, f"DR   GO; {term_id};")))
    for marker in (
        "CC   -!- FUNCTION:",
        "CC   -!- CATALYTIC ACTIVITY:",
        "CC   -!- COFACTOR:",
        "CC   -!- SUBCELLULAR LOCATION:",
        "CC   -!- SIMILARITY:",
        "DR   PANTHER;",
        "DR   Pfam;",
        "KW   ",
        "FT   DOMAIN",
    ):
        line = optional_first_line(path, marker)
        if line and "Reference proteome" not in line:
            add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    for line in prefixed_lines(path, "DR   InterPro;", 5):
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


def standard_support(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    add_unique(items, goa_support(gene, term_id))
    for item in uniprot_evidence(gene, term_id):
        add_unique(items, item)
    for item in asta_evidence(gene):
        add_unique(items, item)
    if gene in {"lexA1", "imuB", "dnaE2"}:
        add_unique(items, pub_support("PMID:17933893", "LexA1", "conventional"))
        add_unique(items, pub_support("PMID:17933893", "imuA", "imuB", "dnaE2"))
    if gene in {"imuB", "dnaE2"}:
        add_unique(items, pub_support("PMID:15458417", "DNA damage-inducible operon"))
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
    for pub_id in GENE_INFO[gene].get("pubs", []):
        if pub_id not in seen:
            refs.append({"id": pub_id, "title": PUBS[pub_id], "findings": []})
    return refs


def review_for_annotation(gene: str, term_id: str) -> dict:
    action, summary, reason = REVIEWS[gene][term_id]
    return {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": standard_support(gene, term_id),
    }


def new_annotation(gene: str, term_id: str) -> dict:
    qualifier = "enables" if term_id in {"GO:0001217"} else "involved_in"
    return {
        "term": TERM[term_id],
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": qualifier,
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
    data["suggested_questions"] = suggested_questions(gene)
    data["suggested_experiments"] = suggested_experiments(gene)
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def suggested_questions(gene: str) -> list[dict[str, object]]:
    text = {
        "PP_1348": "Which oxidized guanine nucleotide substrates does PP_1348 sanitize most efficiently in KT2440?",
        "lexA1": "Which KT2440 promoters belong to the LexA1 regulon versus the LexA2 cassette regulon under each DNA-damaging stress?",
        "polB": "Does KT2440 PolB primarily support accurate repair synthesis, SOS-induced synthesis, or replication-restart proofreading?",
        "ogt": "Which alkylating agents induce or require KT2440 Ogt in vivo?",
        "imuB": "What molecular role does ImuB play in recruiting or modulating DnaE2 during damage-induced mutagenesis?",
        "dnaE2": "What mutation spectrum is generated by KT2440 DnaE2-dependent translesion synthesis?",
        "PP_5679": "Does PP_5679 interact with DinB, ImuB/DnaE2, or damaged DNA as a standalone Y-family little-finger accessory protein?",
    }[gene]
    return [{"question": text, "experts": []}]


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    return [
        {
            "experiment_type": "genetic and biochemical validation",
            "description": f"Construct a {gene} deletion or depletion strain and pair damage-sensitivity/mutagenesis assays with purified-protein substrate assays where an activity is predicted.",
        }
    ]


def write_notes(gene: str) -> None:
    info = GENE_INFO[gene]
    path = GENE_ROOT / gene / f"{gene}-notes.md"
    evidence = standard_support(gene, info["core"][0].get("support_term") if info["core"] else None)
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass SOS/translesion/alkylation-repair split curation.",
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
    lines.extend(["", "Decision: curate conservatively inside the SOS/translesion/alkylation-repair boundary split.", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def annoton(annoton_id: str, gene: str, term_id: str, role: str, processes: list[str] | None = None) -> dict:
    data = {
        "id": annoton_id,
        "label": f"{gene}: {TERM[term_id]['label']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]},
        "role_description": role,
    }
    if processes:
        data["processes"] = [{"preferred_term": TERM[p]["label"], "term": TERM[p]} for p in processes]
    return data


def write_module() -> None:
    data = {
        "id": "MODULE:dna_damage_response_translesion_repair_boundary",
        "title": "SOS, translesion synthesis, alkylation repair, and oxidized nucleotide sanitation",
        "description": (
            "Boundary module for the PSEPK SOS/translesion/alkylation-repair split. "
            "It groups LexA regulation, DinB/PolB/DnaE2 polymerase context, ImuB and PP_5679 accessory candidates, "
            "Ogt alkylated-base repair, and PP_1348 MutT-like oxidized nucleotide sanitation."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_sos_translesion_alkylation_repair.tsv",
                "title": "PSEPK SOS/translesion/alkylation-repair split table",
                "statement": "The split table lists the nine genes assigned to this DNA-damage-response boundary.",
            },
            {
                "source_id": "PMID:17933893",
                "title": PUBS["PMID:17933893"],
                "statement": "LexA1 controls the conventional KT2440 SOS regulon while LexA2 controls the imuA-imuB-dnaE2 cassette.",
            },
        ],
        "notes": "First-pass boundary; do not collapse LexA regulation, polymerase lesion bypass, Ogt alkylation repair, and MutT-like nucleotide sanitation into a single enzyme pathway.",
        "module": {
            "id": "dna_damage_response_translesion_repair_boundary",
            "label": "SOS/translesion/alkylation repair boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {"preferred_term": TERM["GO:0009432"]["label"], "term": TERM["GO:0009432"], "description": "LexA-regulated bacterial SOS response."},
                {"preferred_term": TERM["GO:0042276"]["label"], "term": TERM["GO:0042276"], "description": "Error-prone lesion-bypass DNA synthesis."},
                {"preferred_term": TERM["GO:0006307"]["label"], "term": TERM["GO:0006307"], "description": "Direct repair of alkylated DNA bases."},
                {"preferred_term": TERM["GO:0035539"]["label"], "term": TERM["GO:0035539"], "description": "MutT-like oxidized dGTP sanitation."},
            ],
            "parts": [
                {
                    "order": 1,
                    "role": "LexA regulon control",
                    "node": {
                        "id": "lexa_regulon_control",
                        "label": "LexA regulon control",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "annotons": [
                            annoton("lexa1_sos_repressor", "lexA1", "GO:0001217", "Main conventional SOS regulon repressor.", ["GO:0045892", "GO:0009432"]),
                            annoton("lexa2_cassette_repressor", "lexA2", "GO:0001217", "Narrow lexA2-imuA-imuB-dnaE2 cassette repressor.", ["GO:0045892"]),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "Error-prone and repair-associated DNA polymerases",
                    "node": {
                        "id": "damage_tolerance_polymerases",
                        "label": "Damage-tolerance polymerases",
                        "module_type": "MOLECULAR_FUNCTION",
                        "annotons": [
                            annoton("dinb_pol_iv_tls", "dinB", "GO:0003887", "Y-family Pol IV translesion polymerase.", ["GO:0042276", "GO:0006281"]),
                            annoton("polb_type_b_polymerase", "polB", "GO:0003887", "Type-B PolB repair/proofreading polymerase context.", ["GO:0071897"]),
                            annoton("dnae2_error_prone_tls", "dnaE2", "GO:0003887", "DnaE2 error-prone damage-induced polymerase.", ["GO:0042276", "GO:0006281"]),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "Accessory damaged-DNA or Imu proteins",
                    "node": {
                        "id": "imu_y_family_accessory_context",
                        "label": "Imu/Y-family accessory context",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "annotons": [
                            annoton("imuB_damage_tolerance_accessory", "imuB", "GO:0006281", "ImuB cassette member with unresolved standalone molecular function."),
                            annoton("pp5679_damaged_dna_binding", "PP_5679", "GO:0003684", "Y-family little-finger damaged-DNA-binding candidate.", ["GO:0006281"]),
                        ],
                    },
                },
                {
                    "order": 4,
                    "role": "Alkylated-base repair and oxidized nucleotide sanitation",
                    "node": {
                        "id": "alkylation_and_oxidized_nucleotide_sanitation",
                        "label": "Alkylation repair and oxidized nucleotide sanitation",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "annotons": [
                            annoton("ogt_mgmt_alkylation_repair", "ogt", "GO:0003908", "Ogt/MGMT suicide methyltransferase repairing alkylated DNA.", ["GO:0006307"]),
                            annoton("pp1348_mutT_sanitation", "PP_1348", "GO:0035539", "MutT-like 8-oxo-dGTP hydrolase sanitizing oxidized nucleotide pools.", ["GO:0006281"]),
                        ],
                    },
                },
            ],
        },
    }
    MODULE_PATH.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    for gene in GENE_INFO:
        apply_review(gene)
        write_notes(gene)
    write_module()


if __name__ == "__main__":
    main()
