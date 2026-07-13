#!/usr/bin/env python3
"""First-pass curation for low-information peptidase-family spillovers."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "protein_turnover_peptidase_spillover_boundary.yaml"
BATCH_TSV = "projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_low_information_peptidase_spillovers.tsv"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


TERM = {
    "GO:0004190": {"id": "GO:0004190", "label": "aspartic-type endopeptidase activity"},
    "GO:0004252": {"id": "GO:0004252", "label": "serine-type endopeptidase activity"},
    "GO:0005524": {"id": "GO:0005524", "label": "ATP binding"},
    "GO:0006508": {"id": "GO:0006508", "label": "proteolysis"},
    "GO:0008233": {"id": "GO:0008233", "label": "peptidase activity"},
    "GO:0008236": {"id": "GO:0008236", "label": "serine-type peptidase activity"},
    "GO:0016020": {"id": "GO:0016020", "label": "membrane"},
    "GO:0016787": {"id": "GO:0016787", "label": "hydrolase activity"},
}


GENE_INFO = {
    "PP_0831": {
        "accession": "Q88PL9",
        "description": (
            "PP_0831 encodes a predicted trypsin-like S1/PA clan serine protease in "
            "Pseudomonas putida KT2440. Domain evidence supports a conservative "
            "serine-type endopeptidase activity and proteolysis call, but the "
            "substrate and physiological pathway remain unresolved."
        ),
        "core": [
            {
                "description": "Trypsin-like S1/PA serine endopeptidase candidate with unresolved substrate.",
                "molecular_function": "GO:0004252",
                "directly_involved_in": ["GO:0006508"],
            }
        ],
        "new_terms": ["GO:0004252", "GO:0006508"],
        "question": "What substrate or cellular context, if any, does the PP_0831 S1/PA serine protease act on in KT2440?",
    },
    "PP_2447": {
        "accession": "Q88K45",
        "description": (
            "PP_2447 encodes a low-information Peptidase C39 single-domain family "
            "protein in Pseudomonas putida KT2440. The current record has no fetched "
            "GOA rows and no substrate, process, localization, or accessory-system "
            "evidence, so this first pass leaves the gene without an assigned core GO "
            "function."
        ),
        "core": [],
        "new_terms": [],
        "question": "Is PP_2447 an active C39-family processing peptidase, and what substrate or partner system defines its physiological role?",
    },
    "PP_2685": {
        "accession": "Q88JG4",
        "description": (
            "PP_2685 encodes a predicted N-terminal nucleophile hydrolase/protease "
            "family protein in Pseudomonas putida KT2440. The fetched record has no "
            "GOA rows and no specific substrate or pathway evidence; this first pass "
            "therefore records it as an unresolved peptidase-family candidate rather "
            "than adding a generic GO function."
        ),
        "core": [],
        "new_terms": [],
        "question": "Does PP_2685 retain catalytic N-terminal nucleophile protease activity, and what substrate class does it act on?",
    },
    "pfpI": {
        "accession": "Q88JC4",
        "description": (
            "pfpI encodes a DJ-1/PfpI-domain, peptidase C56-family protein in "
            "Pseudomonas putida KT2440. UniRule/UniProt evidence supports generic "
            "peptidase activity and proteolysis, but not a substrate-specific "
            "peptidase or detoxification process in this first pass."
        ),
        "core": [
            {
                "description": "PfpI/C56-family peptidase candidate with unresolved substrate specificity.",
                "molecular_function": "GO:0008233",
                "directly_involved_in": ["GO:0006508"],
            }
        ],
        "new_terms": ["GO:0006508"],
        "question": "Does pfpI act as a protease in KT2440, and can its substrate specificity be distinguished from HSP31-like DJ-1/PfpI detoxification proteins?",
    },
    "PP_2855": {
        "accession": "Q88IZ4",
        "description": (
            "PP_2855 encodes a signal-peptide-bearing Peptidase C39 domain-containing "
            "protein in Pseudomonas putida KT2440. InterPro/PROSITE evidence supports "
            "membrane-associated generic peptidase activity and proteolysis, while "
            "ATP binding is retained only as non-core imported context because the "
            "local record does not establish an ATPase/transporter role."
        ),
        "core": [
            {
                "description": "Membrane-associated Peptidase C39-family peptidase candidate with unresolved substrate.",
                "molecular_function": "GO:0008233",
                "directly_involved_in": ["GO:0006508"],
                "locations": ["GO:0016020"],
            }
        ],
        "new_terms": [],
        "question": "What exported or membrane-associated substrate is processed by PP_2855, and is it coupled to a partner transporter?",
    },
    "PP_4583": {
        "accession": "Q88E83",
        "description": (
            "PP_4583 encodes a peptidase S9A/prolyl-oligopeptidase-family protein in "
            "Pseudomonas putida KT2440. InterPro and UniProt keyword evidence support "
            "serine-type endopeptidase activity and proteolysis, with broader generic "
            "peptidase rows treated as over-annotated context."
        ),
        "core": [
            {
                "description": "Peptidase S9A serine-type endopeptidase candidate.",
                "molecular_function": "GO:0004252",
                "directly_involved_in": ["GO:0006508"],
            }
        ],
        "new_terms": [],
        "question": "What peptide or protein substrates define the physiological role of the PP_4583 S9A serine endopeptidase?",
    },
    "PP_4913": {
        "accession": "Q88DB4",
        "description": (
            "PP_4913 encodes a TIGR02281/clan AA retropepsin-like aspartic protease "
            "candidate in Pseudomonas putida KT2440. InterPro evidence supports "
            "aspartic-type endopeptidase activity and proteolysis, but the substrate "
            "and pathway context are unresolved."
        ),
        "core": [
            {
                "description": "Clan AA retropepsin-like aspartic-type endopeptidase candidate.",
                "molecular_function": "GO:0004190",
                "directly_involved_in": ["GO:0006508"],
            }
        ],
        "new_terms": [],
        "question": "What substrate or mobile-element/envelope context, if any, explains the PP_4913 clan AA aspartic protease candidate?",
    },
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def lines(path: Path) -> list[str]:
    return read_text(path).splitlines()


def optional_first_line(path: Path, *needles: str) -> str | None:
    if not path.exists():
        return None
    for line in lines(path):
        if all(needle in line for needle in needles):
            return line
    return None


def prefixed_lines(path: Path, prefix: str, limit: int = 8) -> list[str]:
    if not path.exists():
        return []
    return [line for line in lines(path) if line.startswith(prefix)][:limit]


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def support(reference_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": reference_id, "supporting_text": text}


def add_unique(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item not in items:
        items.append(item)


def product_line(gene: str) -> str | None:
    uniprot = gene_file(gene, "uniprot.txt")
    return optional_first_line(uniprot, "DE   RecName:") or optional_first_line(uniprot, "DE   SubName:")


def evidence_for(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    uniprot = gene_file(gene, "uniprot.txt")
    items: list[dict[str, str]] = []
    if term_id:
        for line in lines(gene_file(gene, "goa.tsv")) if gene_file(gene, "goa.tsv").exists() else []:
            if term_id in line:
                add_unique(items, support(file_id(gene, "goa.tsv"), line))
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(uniprot, f"DR   GO; {term_id};")))
    add_unique(items, support(file_id(gene, "uniprot.txt"), product_line(gene)))
    for marker in (
        "CC   -!- SIMILARITY:",
        "Gene3D;",
        "CDD;",
        "PIRSF;",
        "DR   PANTHER;",
        "DR   Pfam;",
        "DR   PROSITE;",
        "KW   Hydrolase",
        "KW   Protease",
        "KW   Serine protease",
        "KW   Signal",
        "FT   SIGNAL",
        "FT   DOMAIN",
    ):
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(uniprot, marker)))
    for line in prefixed_lines(uniprot, "DR   InterPro;", 8):
        add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    asta = gene_file(gene, "deep-research-asta.md")
    for marker in ("  uniprot_accession:", "  protein_description:", "  protein_family:", "  protein_domains:"):
        add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, marker)))
    return items


def accession(gene: str) -> str:
    return GENE_INFO[gene]["accession"]


def ensure_references(data: dict, gene: str) -> None:
    refs = data.setdefault("references", [])
    seen = {ref.get("id") for ref in refs}
    for ref_id, title in [
        (file_id(gene, "goa.tsv"), f"QuickGO GOA annotations for {gene} ({accession(gene)})"),
        (file_id(gene, "uniprot.txt"), f"UniProtKB entry for {gene} ({accession(gene)})"),
        (file_id(gene, "deep-research-asta.md"), f"Asta retrieval report for {gene} ({accession(gene)})"),
    ]:
        if ref_id not in seen and (GENE_ROOT / gene / ref_id.split("/")[-1]).exists():
            refs.append({"id": ref_id, "title": title, "findings": []})
            seen.add(ref_id)


def has(data: dict, term_id: str) -> bool:
    return any(row.get("term", {}).get("id") == term_id for row in data.get("existing_annotations", []))


def review_for(gene: str, term_id: str) -> dict:
    if gene == "PP_0831" and term_id == "GO:0004252":
        return {
            "summary": "Serine-type endopeptidase activity is added from S1/PA trypsin-like domain evidence.",
            "action": "NEW",
            "reason": "The UniProt record has no GOA rows but carries a serine-protease name plus Peptidase_S1_PA/chymotrypsin and Trypsin_2 domain evidence.",
            "supported_by": evidence_for(gene, term_id),
        }
    if gene == "PP_0831" and term_id == "GO:0006508":
        return {
            "summary": "Proteolysis is added as conservative process context for the S1/PA serine protease candidate.",
            "action": "NEW",
            "reason": "The process is supported only as generic catalytic context; no substrate or pathway is asserted.",
            "supported_by": evidence_for(gene, "GO:0004252"),
        }
    if gene == "pfpI" and term_id == "GO:0008233":
        return {
            "summary": "Generic peptidase activity is retained for the PfpI/C56-family protein.",
            "action": "ACCEPT",
            "reason": "UniRule/UniProt, C56_PfpI-like, DJ-1/PfpI, and PANTHER proteinase-family evidence support peptidase activity, but not a more specific substrate class.",
            "supported_by": evidence_for(gene, term_id),
        }
    if gene == "pfpI" and term_id == "GO:0016787":
        return {
            "summary": "Hydrolase activity is true but too broad relative to peptidase activity.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": "The same UniRule transfer supports the more informative peptidase activity row; hydrolase activity adds little biological specificity.",
            "supported_by": evidence_for(gene, term_id) or evidence_for(gene, "GO:0008233"),
        }
    if gene == "pfpI" and term_id == "GO:0006508":
        return {
            "summary": "Proteolysis is added from the UniProt proteolysis cross-reference.",
            "action": "NEW",
            "reason": "UniProt carries a proteolysis row and protease keyword for this C56-family protein, while substrate specificity remains unresolved.",
            "supported_by": evidence_for(gene, term_id),
        }
    if gene == "PP_2855" and term_id == "GO:0005524":
        return {
            "summary": "ATP binding is retained as non-core imported InterPro context.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The local protein is a 226 aa signal-peptide-bearing C39-domain protein; the fetched record does not establish a standalone ATPase or transporter energy-coupling role.",
            "supported_by": evidence_for(gene, term_id),
        }
    if gene == "PP_2855" and term_id == "GO:0006508":
        return {
            "summary": "Proteolysis is accepted for the Peptidase C39 domain-containing protein.",
            "action": "ACCEPT",
            "reason": "InterPro/PROSITE Peptidase C39 evidence supports generic proteolysis context, while substrate specificity remains unresolved.",
            "supported_by": evidence_for(gene, term_id),
        }
    if gene == "PP_2855" and term_id == "GO:0008233":
        return {
            "summary": "Generic peptidase activity is accepted for the C39-domain protein.",
            "action": "ACCEPT",
            "reason": "The C39 domain and InterPro GOA transfer support peptidase activity, but the evidence does not justify a more specific substrate or process term.",
            "supported_by": evidence_for(gene, term_id),
        }
    if gene == "PP_2855" and term_id == "GO:0016020":
        return {
            "summary": "Membrane localization is accepted as context for the signal-peptide-bearing C39 protein.",
            "action": "ACCEPT",
            "reason": "The InterPro membrane row and SignalP feature support membrane/export context for this C39-domain protein.",
            "supported_by": evidence_for(gene, term_id),
        }
    if gene == "PP_4583" and term_id == "GO:0004252":
        return {
            "summary": "Serine-type endopeptidase activity is accepted for the S9A-family protein.",
            "action": "ACCEPT",
            "reason": "InterPro Peptidase S9A catalytic/N-terminal domains, UniProt S9A-family similarity, and serine-protease keyword support the specific endopeptidase term.",
            "supported_by": evidence_for(gene, term_id),
        }
    if gene == "PP_4583" and term_id == "GO:0006508":
        return {
            "summary": "Proteolysis is accepted as process context for the S9A-family serine endopeptidase.",
            "action": "ACCEPT",
            "reason": "UniProt carries proteolysis and protease keyword evidence for the S9A-family protein.",
            "supported_by": evidence_for(gene, term_id),
        }
    if gene == "PP_4583" and term_id == "GO:0008233":
        return {
            "summary": "Generic peptidase activity is over-annotated relative to the specific S9A serine endopeptidase term.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": "The review already accepts GO:0004252, which captures the activity more informatively than generic peptidase activity.",
            "supported_by": evidence_for(gene, "GO:0004252"),
        }
    if gene == "PP_4583" and term_id == "GO:0008236":
        return {
            "summary": "Serine-type peptidase activity is correct but less specific than serine-type endopeptidase activity.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": "The same InterPro evidence supports the more specific GO:0004252 row already present in GOA.",
            "supported_by": evidence_for(gene, term_id) or evidence_for(gene, "GO:0004252"),
        }
    if gene == "PP_4913" and term_id == "GO:0004190":
        return {
            "summary": "Aspartic-type endopeptidase activity is accepted for the clan AA retropepsin-like protein.",
            "action": "ACCEPT",
            "reason": "InterPro/Pfam/PROSITE aspartic-peptidase signatures and the GOA row support this molecular function.",
            "supported_by": evidence_for(gene, term_id),
        }
    if gene == "PP_4913" and term_id == "GO:0006508":
        return {
            "summary": "Proteolysis is accepted as process context for the clan AA aspartic protease candidate.",
            "action": "ACCEPT",
            "reason": "InterPro GOA and the local aspartic-protease domain evidence support proteolysis, while substrate specificity remains unresolved.",
            "supported_by": evidence_for(gene, term_id),
        }
    raise ValueError(f"No review rule for {gene} {term_id}")


def ensure_new(data: dict, gene: str, term_id: str, qualifier: str) -> None:
    if has(data, term_id):
        return
    data.setdefault("existing_annotations", []).append(
        {
            "term": TERM[term_id],
            "evidence_type": "IEA",
            "original_reference_id": file_id(gene, "uniprot.txt"),
            "qualifier": qualifier,
            "review": review_for(gene, term_id),
        }
    )


def core_functions_for(gene: str) -> list[dict]:
    core_items = []
    for item in GENE_INFO[gene]["core"]:
        term_id = item["molecular_function"]
        core = {
            "description": item["description"],
            "molecular_function": TERM[term_id],
            "supported_by": evidence_for(gene, term_id),
        }
        if item.get("directly_involved_in"):
            core["directly_involved_in"] = [TERM[t] for t in item["directly_involved_in"]]
        if item.get("locations"):
            core["locations"] = [TERM[t] for t in item["locations"]]
        core_items.append(core)
    return core_items


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    if GENE_INFO[gene]["core"]:
        return [
            {
                "experiment_type": "comparative sequence analysis",
                "description": f"Check catalytic motif conservation and domain completeness for {gene} against experimentally characterized family members.",
                "hypothesis": f"{gene} retains the active-site features expected for the predicted peptidase family.",
            },
            {
                "experiment_type": "substrate profiling",
                "description": f"Assay recombinant or tagged {gene} against peptide/protein substrate panels matched to its predicted peptidase family.",
                "hypothesis": f"{gene} has measurable peptidase activity but an unresolved physiological substrate.",
            },
        ]
    return [
        {
            "experiment_type": "comparative sequence analysis",
            "description": f"Compare {gene} with curated active and inactive members of the same peptidase-family domain.",
            "hypothesis": f"{gene} may be a non-catalytic or substrate-unresolved family member rather than a confident peptidase.",
        }
    ]


def curate_gene(gene: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(read_text(path))
    data["status"] = "DRAFT"
    data["description"] = GENE_INFO[gene]["description"]
    ensure_references(data, gene)
    for row in data.setdefault("existing_annotations", []):
        row["review"] = review_for(gene, row["term"]["id"])
    for term_id in GENE_INFO[gene]["new_terms"]:
        qualifier = "involved_in" if term_id == "GO:0006508" else "enables"
        ensure_new(data, gene, term_id, qualifier)
    data["core_functions"] = core_functions_for(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": GENE_INFO[gene]["question"], "experts": []}]
    data["suggested_experiments"] = suggested_experiments(gene)
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def descriptor(term_id: str, description: str | None = None) -> dict:
    obj = {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]}
    if description:
        obj["description"] = description
    return obj


def participant(gene: str) -> dict:
    return {"selector_type": "GENE", "gene": {"preferred_term": gene}}


def annoton(gene: str) -> dict:
    core = GENE_INFO[gene]["core"]
    if not core:
        return {
            "id": f"{gene.lower()}_unresolved_peptidase_family_candidate",
            "label": f"{gene}: unresolved peptidase-family candidate",
            "participant": participant(gene),
            "role_description": "Low-information peptidase-family candidate retained without a core GO function in this pass.",
        }
    first = core[0]
    mf = first["molecular_function"]
    item = {
        "id": f"{gene.lower()}_{mf.replace(':', '').lower()}",
        "label": f"{gene}: {TERM[mf]['label']}",
        "participant": participant(gene),
        "role_description": first["description"],
        "function": descriptor(mf),
    }
    if first.get("directly_involved_in"):
        item["processes"] = [descriptor(term_id) for term_id in first["directly_involved_in"]]
    if first.get("locations"):
        item["locations"] = [descriptor(term_id) for term_id in first["locations"]]
    return item


def write_module() -> None:
    data = {
        "id": "MODULE:protein_turnover_peptidase_spillover_boundary",
        "title": "Protein turnover peptidase spillover boundary",
        "description": (
            "Boundary module for low-information Pseudomonas putida KT2440 peptidase-family genes from the "
            "protein folding/targeting/turnover umbrella bucket. The module records only domain/GOA-supported "
            "generic or class-specific peptidase activities and keeps product-name-only or weak domain records unresolved."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_TSV}",
                "title": "PSEPK low-information peptidase-family spillover split",
                "statement": (
                    "The batch table assigns PP_0831, PP_2447, PP_2685, pfpI, PP_2855, PP_4583, and PP_4913 "
                    "to the low-information peptidase-family spillover split."
                ),
            },
            {
                "source_id": "file:PSEPK/PP_0831/PP_0831-ai-review.yaml",
                "title": "Curated PP_0831 review",
                "statement": "The PP_0831 review adds only conservative S1/PA serine endopeptidase and proteolysis rows.",
            },
            {
                "source_id": "file:PSEPK/pfpI/pfpI-ai-review.yaml",
                "title": "Curated pfpI review",
                "statement": "The pfpI review retains generic PfpI/C56-family peptidase activity and marks broad hydrolase as over-annotated.",
            },
            {
                "source_id": "file:PSEPK/PP_4583/PP_4583-ai-review.yaml",
                "title": "Curated PP_4583 review",
                "statement": "The PP_4583 review accepts S9A-family serine-type endopeptidase activity and treats generic peptidase rows as over-annotated.",
            },
        ],
        "notes": (
            "First-pass interpretation: this is not a single pathway. PP_0831, PP_4583, and PP_4913 have enough domain/GOA "
            "support for class-specific endopeptidase calls; pfpI and PP_2855 are retained at generic peptidase level; "
            "PP_2447 and PP_2685 remain no-core unresolved because the current records lack GOA rows and substrate/pathway evidence."
        ),
        "module": {
            "id": "protein_turnover_peptidase_spillover_boundary",
            "label": "Protein turnover peptidase spillover boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                descriptor("GO:0004252", "Class-specific serine endopeptidase call for PP_0831 and PP_4583."),
                descriptor("GO:0004190", "Class-specific aspartic endopeptidase call for PP_4913."),
                descriptor("GO:0008233", "Conservative peptidase activity for pfpI and PP_2855 where substrate specificity is unresolved."),
                descriptor("GO:0006508", "Generic proteolysis process context for domain-supported peptidase candidates."),
                descriptor("GO:0016020", "Membrane context for the signal-peptide-bearing PP_2855 C39-domain protein."),
                descriptor("GO:0005524", "Non-core ATP-binding context imported for PP_2855, not used as a core role."),
                {
                    "preferred_term": "unresolved peptidase-family candidate",
                    "description": "Product/domain-only peptidase-family records kept without a core GO function in this pass.",
                },
            ],
            "parts": [
                {
                    "order": 1,
                    "role": "class-specific endopeptidase candidates",
                    "node": {
                        "id": "class_specific_endopeptidase_candidates",
                        "label": "Class-specific endopeptidase candidates",
                        "module_type": "MOLECULAR_FUNCTION",
                        "description": "S1/S9A serine and clan AA aspartic endopeptidase candidates with class-level domain support.",
                        "annotons": [annoton(gene) for gene in ["PP_0831", "PP_4583", "PP_4913"]],
                    },
                },
                {
                    "order": 2,
                    "role": "generic peptidase candidates",
                    "node": {
                        "id": "generic_peptidase_candidates",
                        "label": "Generic peptidase candidates",
                        "module_type": "MOLECULAR_FUNCTION",
                        "description": "Peptidase-family proteins kept at generic peptidase level because substrate specificity is unresolved.",
                        "annotons": [annoton(gene) for gene in ["pfpI", "PP_2855"]],
                    },
                },
                {
                    "order": 3,
                    "role": "unresolved low-information peptidase-family records",
                    "node": {
                        "id": "unresolved_peptidase_family_records",
                        "label": "Unresolved peptidase-family records",
                        "module_type": "MODULE",
                        "description": "Low-information peptidase-family records left no-core pending stronger catalytic or pathway evidence.",
                        "annotons": [annoton(gene) for gene in ["PP_2447", "PP_2685"]],
                    },
                },
            ],
        },
    }
    MODULE_PATH.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str) -> None:
    evidence = evidence_for(gene, GENE_INFO[gene]["core"][0]["molecular_function"] if GENE_INFO[gene]["core"] else None)
    note_lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass curation for the protein-turnover low-information peptidase-family spillover bucket.",
        GENE_INFO[gene]["description"],
        "",
        "Primary provenance:",
    ]
    seen: set[tuple[str, str]] = set()
    for item in evidence:
        key = (item["reference_id"], item["supporting_text"])
        if key in seen:
            continue
        seen.add(key)
        note_lines.append(f"- [{item['reference_id']} \"{item['supporting_text']}\"]")
        if len(seen) >= 10:
            break
    decision = (
        "Decision: retain a conservative peptidase core function only where domain or GOA evidence supports it."
        if GENE_INFO[gene]["core"]
        else "Decision: no core GO function assigned in this pass; the current record is product/domain-only and substrate/pathway unresolved."
    )
    note_lines.extend(["", decision, ""])
    gene_file(gene, "notes.md").write_text("\n".join(note_lines), encoding="utf-8")


def main() -> None:
    for gene in GENE_INFO:
        curate_gene(gene)
        write_notes(gene)
    write_module()
    print("Curated low-information peptidase-family spillovers")


if __name__ == "__main__":
    main()
