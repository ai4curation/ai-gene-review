#!/usr/bin/env python3
"""First-pass curation for the PSEPK DNA-topology/topoisomerase split."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "dna_topology_topoisomerase_boundary.yaml"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0003677": {"id": "GO:0003677", "label": "DNA binding"},
    "GO:0003916": {"id": "GO:0003916", "label": "DNA topoisomerase activity"},
    "GO:0003917": {
        "id": "GO:0003917",
        "label": "DNA topoisomerase type I (single strand cut, ATP-independent) activity",
    },
    "GO:0003918": {
        "id": "GO:0003918",
        "label": "DNA topoisomerase type II (double strand cut, ATP-hydrolyzing) activity",
    },
    "GO:0005524": {"id": "GO:0005524", "label": "ATP binding"},
    "GO:0005694": {"id": "GO:0005694", "label": "chromosome"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0005886": {"id": "GO:0005886", "label": "plasma membrane"},
    "GO:0006259": {"id": "GO:0006259", "label": "DNA metabolic process"},
    "GO:0006265": {"id": "GO:0006265", "label": "DNA topological change"},
    "GO:0006281": {"id": "GO:0006281", "label": "DNA repair"},
    "GO:0006310": {"id": "GO:0006310", "label": "DNA recombination"},
    "GO:0006355": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "GO:0007059": {"id": "GO:0007059", "label": "chromosome segregation"},
    "GO:0008270": {"id": "GO:0008270", "label": "zinc ion binding"},
    "GO:0008657": {
        "id": "GO:0008657",
        "label": "DNA topoisomerase type II (double strand cut, ATP-hydrolyzing) inhibitor activity",
    },
    "GO:0009330": {
        "id": "GO:0009330",
        "label": "DNA topoisomerase type II (double strand cut, ATP-hydrolyzing) complex",
    },
    "GO:0019897": {"id": "GO:0019897", "label": "extrinsic component of plasma membrane"},
    "GO:0034335": {"id": "GO:0034335", "label": "DNA negative supercoiling activity"},
    "GO:0043597": {"id": "GO:0043597", "label": "cytoplasmic replication fork"},
    "GO:0051276": {"id": "GO:0051276", "label": "chromosome organization"},
}


GENE_INFO = {
    "yacG": {
        "accession": "Q88Q66",
        "description": (
            "yacG (PP_0630) encodes DNA gyrase inhibitor YacG, a small zinc-binding "
            "protein in Pseudomonas putida KT2440. UniProt/HAMAP metadata supports a "
            "YacG-family protein that binds the GyrB C-terminal domain and inhibits DNA "
            "gyrase by preventing productive DNA interaction. In this first pass it is "
            "curated as a DNA-topology regulatory side node, not as a general "
            "transcription regulator."
        ),
        "core": [
            {
                "description": "Zinc-binding YacG-family inhibitor of the DNA gyrase/type II topoisomerase reaction.",
                "molecular_function": TERM["GO:0008657"],
                "support_term": "GO:0008657",
            }
        ],
        "questions": [
            "Does KT2440 YacG measurably tune gyrase activity or antibiotic sensitivity under specific growth or stress conditions?"
        ],
        "experiments": [
            {
                "experiment_type": "gyrase inhibition assay",
                "description": "Purify YacG with GyrA/GyrB and test inhibition of DNA supercoiling/relaxation and GyrB binding in vitro.",
            }
        ],
    },
    "topA": {
        "accession": "Q88KZ9",
        "description": (
            "topA (PP_2139) encodes DNA topoisomerase I, a type IA topoisomerase in "
            "Pseudomonas putida KT2440. The protein is a monomeric, ATP-independent "
            "single-strand breakage/rejoining enzyme that releases supercoiling and "
            "torsional tension generated during DNA replication and transcription. "
            "Its primary role is DNA topological change on chromosomal DNA rather than "
            "a generic DNA-binding activity."
        ),
        "core": [
            {
                "description": "Type IA DNA topoisomerase I that relaxes DNA supercoiling through ATP-independent single-strand passage.",
                "molecular_function": TERM["GO:0003917"],
                "directly_involved_in": [TERM["GO:0006265"]],
                "locations": [TERM["GO:0005694"]],
                "support_term": "GO:0003917",
            }
        ],
        "questions": ["Which DNA-topology phenotypes distinguish TopA from TopB and PP_3831 in KT2440?"],
        "experiments": [
            {
                "experiment_type": "DNA supercoiling assay",
                "description": "Compare plasmid supercoiling and transcriptome effects in topA deletion/depletion strains with complementation.",
            }
        ],
    },
    "PP_3831": {
        "accession": "Q88G94",
        "description": (
            "PP_3831 encodes a predicted DNA topoisomerase in Pseudomonas putida KT2440. "
            "The current UniProt, InterPro, Pfam, and GOA metadata support a type IB "
            "topoisomerase-like protein with ATP-independent type I topoisomerase activity "
            "and DNA topological-change context, but the physiological substrate and "
            "relationship to the canonical TopA/TopB enzymes remain unresolved."
        ),
        "core": [
            {
                "description": "Predicted type IB DNA topoisomerase acting in DNA topological change.",
                "molecular_function": TERM["GO:0003917"],
                "directly_involved_in": [TERM["GO:0006265"]],
                "support_term": "GO:0003917",
            }
        ],
        "questions": ["What is the in vivo role of the predicted type IB topoisomerase PP_3831 in KT2440?"],
        "experiments": [
            {
                "experiment_type": "topoisomerase substrate assay",
                "description": "Purify PP_3831 and test ATP-independent relaxation or cleavage/rejoining activity on supercoiled DNA substrates.",
            }
        ],
    },
    "topB": {
        "accession": "Q88FR4",
        "description": (
            "topB (PP_4019) encodes a TopB/topoisomerase III-like type IA DNA "
            "topoisomerase in Pseudomonas putida KT2440. UniProt and domain evidence "
            "support ATP-independent type I topoisomerase activity and DNA topological "
            "change. TreeGrafter also propagates repair, recombination, and replication-fork "
            "context; those are treated here as non-core or over-specific side context "
            "pending KT2440-specific evidence."
        ),
        "core": [
            {
                "description": "Topoisomerase III-like type IA enzyme for ATP-independent DNA topological change.",
                "molecular_function": TERM["GO:0003917"],
                "directly_involved_in": [TERM["GO:0006265"]],
                "support_term": "GO:0003917",
            }
        ],
        "questions": ["Does TopB act with RecQ-like helicases in KT2440 recombination or repair, or mainly as a standalone topology enzyme?"],
        "experiments": [
            {
                "experiment_type": "genetic interaction assay",
                "description": "Test topB interactions with RecQ/repair mutants and assay recombination or DNA-damage phenotypes.",
            }
        ],
    },
    "PP_4476": {
        "accession": "Q88EI6",
        "description": (
            "PP_4476 is an uncharacterized Pseudomonas putida KT2440 protein whose "
            "current UniProt record carries only a ProtNLM-derived RecName of "
            "Topoisomerase II. The fetched record has no GOA rows and no UniProt family, "
            "InterPro, or Pfam domain support for a topoisomerase assignment. This first "
            "pass therefore records PP_4476 as an unresolved DNA-topology candidate and "
            "does not propose GO terms from the protein name alone."
        ),
        "core": [],
        "questions": ["Is PP_4476 a true type II topoisomerase-related protein, or is the ProtNLM name unsupported for this sequence?"],
        "experiments": [
            {
                "experiment_type": "domain and activity validation",
                "description": "Reannotate PP_4476 with profile HMMs and test purified protein for ATP-dependent topoisomerase activity only if conserved catalytic domains are found.",
            }
        ],
    },
    "parC": {
        "accession": "Q88DB5",
        "description": (
            "parC (PP_4912) encodes DNA topoisomerase IV subunit A in Pseudomonas putida "
            "KT2440. Together with ParE it forms a type II topoisomerase heterotetramer "
            "that relaxes supercoiled DNA and performs the decatenation events required "
            "for segregation of circular chromosomes. ParC provides the GyrA/ParC-family "
            "DNA cleavage/rejoining subunit of the Topo IV complex; ATP binding is "
            "retained only as complex-level context because ParE is the ATPase subunit."
        ),
        "core": [
            {
                "description": "Topo IV subunit A contributing type II topoisomerase activity for chromosome decatenation and segregation.",
                "molecular_function": TERM["GO:0003918"],
                "directly_involved_in": [TERM["GO:0006265"], TERM["GO:0007059"]],
                "locations": [TERM["GO:0005694"], TERM["GO:0005737"], TERM["GO:0005886"]],
                "in_complex": TERM["GO:0009330"],
                "support_term": "GO:0003918",
            }
        ],
        "questions": ["How much of KT2440 Topo IV localization is chromosome-associated versus peripheral membrane-associated during the cell cycle?"],
        "experiments": [
            {
                "experiment_type": "cell biology and decatenation assay",
                "description": "Localize tagged ParC and assay chromosome decatenation/segregation phenotypes under parC depletion or inhibition.",
            }
        ],
    },
    "parE": {
        "accession": "Q88DB2",
        "description": (
            "parE (PP_4915) encodes DNA topoisomerase IV subunit B in Pseudomonas putida "
            "KT2440. Together with ParC it forms the type II Topo IV heterotetramer that "
            "uses ATP-dependent double-strand passage to relax supercoiled DNA and "
            "decatenate replicated circular chromosomes for segregation. ParE supplies "
            "the topoisomerase B-family ATPase/TOPRIM subunit of this complex."
        ),
        "core": [
            {
                "description": "Topo IV ATPase/TOPRIM subunit contributing type II topoisomerase activity during chromosome decatenation and segregation.",
                "molecular_function": TERM["GO:0003918"],
                "directly_involved_in": [TERM["GO:0006265"], TERM["GO:0007059"]],
                "locations": [TERM["GO:0005694"]],
                "in_complex": TERM["GO:0009330"],
                "support_term": "GO:0003918",
            }
        ],
        "questions": ["What ParE residues or domains control ATP turnover and metal coordination in KT2440 Topo IV?"],
        "experiments": [
            {
                "experiment_type": "ATPase and decatenation assay",
                "description": "Measure ParE-dependent ATP hydrolysis and Topo IV decatenation using purified ParC/ParE complexes.",
            }
        ],
    },
}


REVIEWS = {
    "yacG": {
        "GO:0006355": (
            "MARK_AS_OVER_ANNOTATED",
            "Regulation of DNA-templated transcription is an indirect InterPro propagation for YacG.",
            "YacG is curated here as a gyrase inhibitor. Changes in transcription can follow altered DNA topology, but the fetched evidence does not support YacG as a direct transcription regulator.",
        ),
        "GO:0008270": (
            "KEEP_AS_NON_CORE",
            "Zinc ion binding is supported by the YacG cofactor annotation.",
            "The zinc-binding annotation is correct and supports the YacG fold, but the core activity is inhibition of DNA gyrase/type II topoisomerase.",
        ),
        "GO:0008657": (
            "ACCEPT",
            "DNA topoisomerase type II inhibitor activity is the defining YacG function.",
            "UniProt/HAMAP states that YacG inhibits DNA gyrase by preventing DNA interaction through GyrB binding, matching this specific molecular function.",
        ),
    },
    "topA": {
        "GO:0003677": (
            "KEEP_AS_NON_CORE",
            "DNA binding is expected for TopA but less specific than topoisomerase activity.",
            "TopA must bind DNA to cleave and rejoin a strand, but GO:0003917 and GO:0006265 capture the core function more precisely.",
        ),
        "GO:0003916": (
            "KEEP_AS_NON_CORE",
            "General topoisomerase activity is correct but broader than the type I activity.",
            "The type IA topoisomerase identity is already represented by GO:0003917, so the broad parent is retained as non-core.",
        ),
        "GO:0003917": (
            "ACCEPT",
            "Type I DNA topoisomerase activity is the core TopA molecular function.",
            "The UniProt/HAMAP function and catalytic activity describe ATP-independent single-strand breakage and rejoining by topoisomerase I.",
        ),
        "GO:0005694": (
            "ACCEPT",
            "Chromosome is an appropriate substrate/location context for bacterial TopA.",
            "TopA acts on chromosomal DNA topology; the InterPro-supported chromosome row is consistent with the bacterial DNA substrate.",
        ),
        "GO:0006265": (
            "ACCEPT",
            "DNA topological change is the core process for TopA.",
            "The enzyme releases supercoiling and torsional tension by transient single-strand cleavage/rejoining, directly matching DNA topological change.",
        ),
    },
    "PP_3831": {
        "GO:0003677": (
            "KEEP_AS_NON_CORE",
            "DNA binding is plausible for the predicted type IB topoisomerase but less specific than topoisomerase activity.",
            "The protein carries topoisomerase/domain evidence; DNA binding is supporting context rather than the specific core activity.",
        ),
        "GO:0003917": (
            "ACCEPT",
            "Type I topoisomerase activity is supported by EC/domain evidence for PP_3831.",
            "UniProt/ARBA, Pfam, and InterPro metadata support a type IB/topoisomerase I-like protein, so the type I activity is accepted in first pass.",
        ),
        "GO:0006265": (
            "ACCEPT",
            "DNA topological change is the best current process context for PP_3831.",
            "The current evidence supports a DNA topoisomerase-like protein but does not resolve a narrower pathway role.",
        ),
    },
    "topB": {
        "GO:0003677": (
            "KEEP_AS_NON_CORE",
            "DNA binding is expected for TopB but less specific than type I topoisomerase activity.",
            "TopB has type IA/TOPRIM domain evidence; DNA binding is substrate context rather than the primary function.",
        ),
        "GO:0003916": (
            "KEEP_AS_NON_CORE",
            "General topoisomerase activity is correct but broader than type I activity.",
            "GO:0003917 gives the more precise current molecular function for this TopB/topoisomerase III-like protein.",
        ),
        "GO:0003917": (
            "ACCEPT",
            "Type I topoisomerase activity is the core TopB molecular function.",
            "UniProt EC and domain metadata support ATP-independent type I topoisomerase activity for this type IA family member.",
        ),
        "GO:0006265": (
            "ACCEPT",
            "DNA topological change is the core process for TopB.",
            "The type IA topoisomerase domain architecture supports a role in changing DNA topology.",
        ),
        "GO:0006281": (
            "KEEP_AS_NON_CORE",
            "DNA repair is plausible side context from TreeGrafter but is not the resolved core function.",
            "Topoisomerase III-like enzymes can participate in repair-associated DNA transactions, but the direct first-pass function remains DNA topological change.",
        ),
        "GO:0006310": (
            "KEEP_AS_NON_CORE",
            "DNA recombination is plausible side context from TreeGrafter but is not the resolved core function.",
            "The current fetched evidence does not establish a specific KT2440 recombination role, so this is retained as non-core context.",
        ),
        "GO:0043597": (
            "MARK_AS_OVER_ANNOTATED",
            "Cytoplasmic replication fork is an over-specific TreeGrafter localization for this first pass.",
            "The evidence supports a soluble type IA topoisomerase, but not enough KT2440-specific information to localize TopB specifically to cytoplasmic replication forks.",
        ),
    },
    "parC": {
        "GO:0003677": (
            "KEEP_AS_NON_CORE",
            "DNA binding is expected for ParC but less specific than Topo IV activity.",
            "ParC is the DNA-cleavage/rejoining subunit of Topo IV, but type II topoisomerase activity and chromosome segregation capture the core role.",
        ),
        "GO:0003916": (
            "KEEP_AS_NON_CORE",
            "General topoisomerase activity is correct but broader than type II Topo IV activity.",
            "GO:0003918 is already present and captures the specific ATP-hydrolyzing double-strand-passage activity.",
        ),
        "GO:0003918": (
            "ACCEPT",
            "Type II topoisomerase activity is the core ParC/Topo IV molecular function.",
            "UniProt/HAMAP describes ATP-dependent breakage, passage, and rejoining of double-stranded DNA by Topo IV.",
        ),
        "GO:0005524": (
            "KEEP_AS_NON_CORE",
            "ATP binding is complex-level context for Topo IV rather than ParC-specific core chemistry.",
            "The Topo IV reaction is ATP-dependent, but ParE is the ATPase subunit; ParC is retained with this term only as non-core complex context.",
        ),
        "GO:0005694": (
            "ACCEPT",
            "Chromosome is an appropriate component/substrate context for Topo IV.",
            "Topo IV decatenates replicated circular chromosomes and is essential for chromosome segregation.",
        ),
        "GO:0005737": (
            "ACCEPT",
            "Cytoplasm is compatible with bacterial Topo IV activity.",
            "Topo IV is a bacterial chromosomal enzyme acting in the cytoplasmic/nucleoid compartment.",
        ),
        "GO:0005886": (
            "ACCEPT",
            "Plasma membrane localization is supported by UniProt/HAMAP subcellular-location metadata.",
            "The UniProt record explicitly annotates ParC as cell membrane/peripheral membrane protein; this is accepted while keeping the core function as Topo IV activity.",
        ),
        "GO:0006259": (
            "MARK_AS_OVER_ANNOTATED",
            "DNA metabolic process is a broad parent for the more precise Topo IV process terms.",
            "GO:0006265 and GO:0007059 capture the specific DNA-topology and chromosome-segregation roles better than this broad process parent.",
        ),
        "GO:0006265": (
            "ACCEPT",
            "DNA topological change is a core Topo IV process.",
            "Topo IV relaxes supercoiled DNA and performs decatenation events required after circular-chromosome replication.",
        ),
        "GO:0007059": (
            "ACCEPT",
            "Chromosome segregation is a core Topo IV biological role.",
            "The UniProt/HAMAP function states that Topo IV is essential for chromosome segregation and decatenation.",
        ),
        "GO:0009330": (
            "ACCEPT",
            "ParC is part of the type II topoisomerase complex.",
            "UniProt/HAMAP describes Topo IV as a heterotetramer composed of ParC and ParE.",
        ),
        "GO:0019897": (
            "ACCEPT",
            "Extrinsic component of plasma membrane is supported by the UniProt/HAMAP peripheral membrane annotation.",
            "This is accepted as location context, while the core biological story remains chromosome decatenation by Topo IV.",
        ),
    },
    "parE": {
        "GO:0003677": (
            "KEEP_AS_NON_CORE",
            "DNA binding is expected for the Topo IV complex but less specific than type II topoisomerase activity.",
            "ParE contributes to the ParC/ParE topoisomerase complex; the core activity is represented by GO:0003918.",
        ),
        "GO:0003918": (
            "ACCEPT",
            "Type II topoisomerase activity is the core ParE/Topo IV molecular function.",
            "UniProt/HAMAP describes ATP-dependent breakage, passage, and rejoining of double-stranded DNA by Topo IV.",
        ),
        "GO:0005524": (
            "KEEP_AS_NON_CORE",
            "ATP binding is a genuine ParE subunit activity but broad compared with the topoisomerase reaction.",
            "ParE is the topoisomerase B-family ATPase/TOPRIM subunit, so ATP binding is retained as supporting molecular context.",
        ),
        "GO:0005694": (
            "ACCEPT",
            "Chromosome is an appropriate component/substrate context for Topo IV.",
            "Topo IV acts on replicated circular chromosomes during decatenation and segregation.",
        ),
        "GO:0006265": (
            "ACCEPT",
            "DNA topological change is a core Topo IV process.",
            "The Topo IV heterotetramer relaxes supercoiled DNA and decatenates replicated chromosomes.",
        ),
        "GO:0007059": (
            "ACCEPT",
            "Chromosome segregation is a core Topo IV biological role.",
            "UniProt/HAMAP states Topo IV is essential for chromosome segregation.",
        ),
        "GO:0051276": (
            "KEEP_AS_NON_CORE",
            "Chromosome organization is correct broad context but less precise than chromosome segregation and DNA topological change.",
            "Topo IV contributes to chromosome organization through decatenation, but the more specific process terms are preferred as core.",
        ),
        "GO:0009330": (
            "NEW",
            "Topo IV complex membership should be recorded for ParE.",
            "The fetched GOA block lacks a ParE complex row, but UniProt/HAMAP states that Topo IV is a heterotetramer composed of ParC and ParE.",
        ),
    },
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_lines(path: Path) -> list[str]:
    return read_text(path).splitlines()


def first_line(path: Path, *needles: str) -> str:
    for line in read_lines(path):
        if all(needle in line for needle in needles):
            return line
    raise ValueError(f"No line in {path} contains all needles: {needles}")


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
    line = optional_first_line(GENE_ROOT / gene / f"{gene}-goa.tsv", term_id)
    return support(file_id(gene, "goa.tsv"), line)


def uniprot_evidence(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    items: list[dict[str, str]] = []
    add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, "DE   RecName")))
    if term_id:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, f"DR   GO; {term_id};")))
    for marker in (
        "CC   -!- FUNCTION:",
        "CC   -!- CATALYTIC ACTIVITY:",
        "CC   -!- COFACTOR:",
        "CC   -!- SUBUNIT:",
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
    return items


def reference_list(existing_refs: list[dict] | None, gene: str, accession: str) -> list[dict]:
    refs: list[dict] = []
    seen = set()
    for ref in existing_refs or []:
        ref_id = ref["id"]
        seen.add(ref_id)
        refs.append(ref)
    for ref_id, title in {
        file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({accession})",
        file_id(gene, "uniprot.txt"): f"UniProtKB entry for {gene} ({accession})",
        file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({accession})",
    }.items():
        if ref_id not in seen and (ROOT / "genes" / "PSEPK" / gene / ref_id.split("/")[-1]).exists():
            refs.append({"id": ref_id, "title": title, "findings": []})
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
    if gene == "parE" and term_id == "GO:0009330":
        return {
            "term": TERM[term_id],
            "evidence_type": "IEA",
            "original_reference_id": file_id(gene, "uniprot.txt"),
            "qualifier": "part_of",
            "review": review_for_annotation(gene, term_id),
        }
    raise ValueError(f"No NEW annotation rule for {gene} {term_id}")


def core_functions(gene: str) -> list[dict]:
    cores = []
    for item in GENE_INFO[gene]["core"]:
        support_term = item.get("support_term")
        core = {
            "description": item["description"],
            "supported_by": standard_support(gene, support_term),
        }
        for key in ("molecular_function", "directly_involved_in", "locations", "in_complex"):
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
        term_id = annotation["term"]["id"]
        annotation["review"] = review_for_annotation(gene, term_id)
    if gene == "parE" and not any(annotation["term"]["id"] == "GO:0009330" for annotation in existing):
        existing.append(new_annotation(gene, "GO:0009330"))
    data["existing_annotations"] = existing
    data["core_functions"] = core_functions(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": question, "experts": []} for question in info["questions"]]
    data["suggested_experiments"] = info["experiments"]
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str) -> None:
    info = GENE_INFO[gene]
    path = GENE_ROOT / gene / f"{gene}-notes.md"
    evidence = standard_support(gene, info["core"][0]["support_term"] if info["core"] else None)
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass DNA topology/topoisomerase sub-batch curation.",
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
    if gene == "PP_4476":
        lines.append("- Decision: leave without proposed GO terms because the only topoisomerase signal is a ProtNLM RecName.")
    else:
        lines.append("- Decision: curate as part of the DNA-topology/topoisomerase boundary module.")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def descriptor(term_id: str, description: str) -> dict:
    return {
        "preferred_term": TERM[term_id]["label"],
        "term": TERM[term_id],
        "description": description,
    }


def gene_annoton(annoton_id: str, gene: str, term_id: str, role: str, processes: list[str] | None = None) -> dict:
    annoton = {
        "id": annoton_id,
        "label": f"{gene}: {TERM[term_id]['label']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]},
        "role_description": role,
    }
    if processes:
        annoton["processes"] = [{"preferred_term": TERM[p]["label"], "term": TERM[p]} for p in processes]
    return annoton


def write_module() -> None:
    data = {
        "id": "MODULE:dna_topology_topoisomerase_boundary",
        "title": "DNA topology and topoisomerase boundary",
        "description": (
            "Boundary module for Pseudomonas putida KT2440 DNA-topology proteins in the broad "
            "DNA replication/repair/recombination bucket. It includes DNA gyrase GyrA/GyrB, "
            "the YacG gyrase inhibitor, type I topoisomerases TopA/TopB/PP_3831, and Topo IV "
            "ParC/ParE. PP_4476 is retained only as an unresolved low-evidence candidate."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_dna_topology_topoisomerase.tsv",
                "title": "PSEPK DNA-topology/topoisomerase partition table",
                "statement": "The sub-batch table lists the nine genes assigned to the DNA-topology/topoisomerase split.",
            },
            {
                "source_id": "file:PSEPK/gyrA/gyrA-ai-review.yaml",
                "title": "Curated gyrA review",
                "statement": "The existing gyrA review accepts type II topoisomerase and negative-supercoiling activity.",
            },
            {
                "source_id": "file:PSEPK/gyrB/gyrB-ai-review.yaml",
                "title": "Curated gyrB review",
                "statement": "The existing gyrB review accepts type II topoisomerase activity in DNA topological change.",
            },
        ],
        "notes": (
            "First-pass boundary: the satisfiable module is DNA topology, not generic DNA repair. "
            "TopB repair/recombination annotations are kept as side context, and PP_4476 remains a knowledge gap."
        ),
        "module": {
            "id": "dna_topology_topoisomerase_boundary",
            "label": "DNA topology and topoisomerase boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                descriptor("GO:0006265", "Direct alteration of DNA topology by gyrase and topoisomerases."),
                descriptor("GO:0003918", "Type II topoisomerase activity used by DNA gyrase and Topo IV."),
                descriptor("GO:0003917", "Type I topoisomerase activity used by TopA, TopB, and PP_3831."),
                descriptor("GO:0034335", "Gyrase-specific negative-supercoiling activity."),
                descriptor("GO:0007059", "Topo IV decatenation role in chromosome segregation."),
                descriptor("GO:0008657", "YacG inhibition of DNA gyrase/type II topoisomerase activity."),
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": "bacterial chromosome",
                        "term": TERM["GO:0005694"],
                        "description": "Chromosomal DNA substrate context for topology enzymes.",
                    },
                    {
                        "preferred_term": "bacterial cytoplasm",
                        "term": TERM["GO:0005737"],
                        "description": "Soluble bacterial topology enzymes act around the cytoplasmic nucleoid.",
                    },
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "DNA gyrase negative supercoiling",
                    "node": {
                        "id": "dna_gyrase_negative_supercoiling",
                        "label": "DNA gyrase negative supercoiling",
                        "module_type": "MOLECULAR_FUNCTION",
                        "description": "GyrA/GyrB type II topoisomerase activity introduces ATP-dependent negative supercoils.",
                        "annotons": [
                            gene_annoton("gyra_type_ii_topoisomerase", "gyrA", "GO:0003918", "Gyrase A DNA cleavage/rejoining subunit.", ["GO:0006265"]),
                            gene_annoton("gyrb_type_ii_topoisomerase", "gyrB", "GO:0003918", "Gyrase B ATPase/TOPRIM subunit.", ["GO:0006265"]),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "YacG gyrase inhibition",
                    "node": {
                        "id": "yacg_gyrase_inhibition",
                        "label": "YacG gyrase inhibition",
                        "module_type": "MOLECULAR_FUNCTION",
                        "description": "YacG binds GyrB and inhibits gyrase catalytic activity.",
                        "annotons": [
                            gene_annoton("yacg_gyrase_inhibitor", "yacG", "GO:0008657", "Small zinc-binding inhibitor of DNA gyrase.")
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "Type I topoisomerase relaxation",
                    "node": {
                        "id": "type_i_topoisomerase_relaxation",
                        "label": "Type I topoisomerase relaxation",
                        "module_type": "MOLECULAR_FUNCTION",
                        "description": "TopA, TopB, and PP_3831 provide ATP-independent type I topoisomerase activities.",
                        "annotons": [
                            gene_annoton("topa_type_i_topoisomerase", "topA", "GO:0003917", "Canonical TopA/topoisomerase I.", ["GO:0006265"]),
                            gene_annoton("topb_type_i_topoisomerase", "topB", "GO:0003917", "TopB/topoisomerase III-like enzyme.", ["GO:0006265"]),
                            gene_annoton("pp3831_type_i_topoisomerase", "PP_3831", "GO:0003917", "Predicted type IB topoisomerase candidate.", ["GO:0006265"]),
                        ],
                    },
                },
                {
                    "order": 4,
                    "role": "Topo IV decatenation and segregation",
                    "node": {
                        "id": "topo_iv_chromosome_decatenation",
                        "label": "Topo IV chromosome decatenation",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "ParC/ParE Topo IV relaxes supercoils and decatenates replicated circular chromosomes.",
                        "annotons": [
                            gene_annoton("parc_topo_iv_subunit_a", "parC", "GO:0003918", "Topo IV subunit A in chromosome decatenation.", ["GO:0006265", "GO:0007059"]),
                            gene_annoton("pare_topo_iv_subunit_b", "parE", "GO:0003918", "Topo IV subunit B in chromosome decatenation.", ["GO:0006265", "GO:0007059"]),
                        ],
                    },
                },
                {
                    "order": 5,
                    "role": "Unresolved topoisomerase-name candidate",
                    "optional": True,
                    "node": {
                        "id": "pp4476_unresolved_candidate",
                        "label": "PP_4476 unresolved topoisomerase-name candidate",
                        "module_type": "MOLECULAR_FUNCTION",
                        "description": (
                            "PP_4476 has a ProtNLM-derived Topoisomerase II RecName but no GOA, InterPro, "
                            "Pfam, or family support in the fetched metadata; no module annoton is asserted."
                        ),
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
