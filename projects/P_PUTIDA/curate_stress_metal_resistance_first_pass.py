#!/usr/bin/env python3
"""First-pass curate the PSEPK arsenic/copper metal-resistance stress split."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_DIR = ROOT / "projects" / "P_PUTIDA" / "batches"
BATCH_TSV = BATCH_DIR / "module_stress_detoxification_arsenic_copper_metal_resistance.tsv"
PARTITION_TSV = BATCH_DIR / "module_stress_detoxification_partition.tsv"
MODULE_YAML = ROOT / "modules" / "metal_resistance_detoxification_boundary.yaml"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0005507": {"id": "GO:0005507", "label": "copper ion binding"},
    "GO:0006878": {"id": "GO:0006878", "label": "intracellular copper ion homeostasis"},
    "GO:0009279": {"id": "GO:0009279", "label": "cell outer membrane"},
    "GO:0016491": {"id": "GO:0016491", "label": "oxidoreductase activity"},
    "GO:0016655": {
        "id": "GO:0016655",
        "label": "oxidoreductase activity, acting on NAD(P)H, quinone or similar compound as acceptor",
    },
    "GO:0042597": {"id": "GO:0042597", "label": "periplasmic space"},
    "GO:0046685": {"id": "GO:0046685", "label": "response to arsenic-containing substance"},
    "GO:0052873": {"id": "GO:0052873", "label": "FMN reductase (NADPH) activity"},
}


ARSH_GENES = {"PP_1927", "arsH"}
ARSC_GENES = {"PP_1928", "PP_2716"}
COPB_GENES = {"copB-I", "copB-II"}
COPA_GENES = {"copA-I", "copA-II"}


GENE_INFO = {
    "PP_1927": {
        "role": "ArsH-family NADPH-dependent FMN reductase",
        "description": (
            "PP_1927 encodes an ArsH-family NADPH-dependent FMN reductase in Pseudomonas putida KT2440. "
            "The product and domain evidence support FMN reductase chemistry in arsenical-resistance operon "
            "context; this first pass does not assign a narrower organoarsenical substrate or detoxification "
            "reaction beyond the supported FMN reductase activity."
        ),
        "primary_function": TERM["GO:0052873"],
        "new_terms": [],
    },
    "arsH": {
        "role": "ArsH-family NADPH-dependent FMN reductase",
        "description": (
            "arsH encodes an ArsH-family NADPH-dependent FMN reductase in Pseudomonas putida KT2440. "
            "The product and domain evidence support FMN reductase chemistry in arsenical-resistance operon "
            "context; this first pass does not assign a narrower organoarsenical substrate or detoxification "
            "reaction beyond the supported FMN reductase activity."
        ),
        "primary_function": TERM["GO:0052873"],
        "new_terms": [],
    },
    "PP_1928": {
        "role": "low-molecular-weight arsenate reductase candidate",
        "description": (
            "PP_1928 encodes a predicted low-molecular-weight arsenate reductase in Pseudomonas putida KT2440. "
            "UniProt names the product as arsenate reductase and marks arsenical-resistance context, but the fetched "
            "GOA table has no rows. The first-pass GO-level assignment is therefore conservative oxidoreductase "
            "activity plus response to arsenic-containing substance, without asserting a more specific arsenate "
            "reductase GO term."
        ),
        "primary_function": TERM["GO:0016491"],
        "process": TERM["GO:0046685"],
        "new_terms": ["GO:0016491", "GO:0046685"],
    },
    "PP_2716": {
        "role": "low-molecular-weight arsenate reductase candidate",
        "description": (
            "PP_2716 encodes a predicted low-molecular-weight arsenate reductase in Pseudomonas putida KT2440. "
            "UniProt names the product as arsenate reductase and marks arsenical-resistance context, but the fetched "
            "GOA table has no rows. The first-pass GO-level assignment is therefore conservative oxidoreductase "
            "activity plus response to arsenic-containing substance, without asserting a more specific arsenate "
            "reductase GO term."
        ),
        "primary_function": TERM["GO:0016491"],
        "process": TERM["GO:0046685"],
        "new_terms": ["GO:0016491", "GO:0046685"],
    },
    "copB-I": {
        "role": "outer-membrane copper-resistance protein B",
        "description": (
            "copB-I encodes an outer-membrane copper-resistance protein B in Pseudomonas putida KT2440. "
            "GOA and InterPro evidence support copper ion binding, cell outer membrane localization, and "
            "intracellular copper ion homeostasis context."
        ),
        "primary_function": TERM["GO:0005507"],
        "process": TERM["GO:0006878"],
        "locations": [TERM["GO:0009279"]],
        "new_terms": [],
    },
    "copB-II": {
        "role": "outer-membrane copper-resistance protein B",
        "description": (
            "copB-II encodes an outer-membrane copper-resistance protein B in Pseudomonas putida KT2440. "
            "GOA and InterPro evidence support copper ion binding, cell outer membrane localization, and "
            "intracellular copper ion homeostasis context."
        ),
        "primary_function": TERM["GO:0005507"],
        "process": TERM["GO:0006878"],
        "locations": [TERM["GO:0009279"]],
        "new_terms": [],
    },
    "copA-I": {
        "role": "periplasmic multicopper oxidase-family copper-resistance protein A",
        "description": (
            "copA-I encodes a periplasmic copper-resistance protein A in Pseudomonas putida KT2440. "
            "The multicopper oxidase/CopA domain architecture and GOA support copper ion binding, broad "
            "oxidoreductase activity, and periplasmic localization; this first pass does not assign a narrower "
            "physiological copper-oxidation reaction."
        ),
        "primary_function": TERM["GO:0016491"],
        "locations": [TERM["GO:0042597"]],
        "new_terms": [],
    },
    "copA-II": {
        "role": "periplasmic multicopper oxidase-family copper-resistance protein A",
        "description": (
            "copA-II encodes a periplasmic copper-resistance protein A in Pseudomonas putida KT2440. "
            "The multicopper oxidase/CopA domain architecture and GOA support copper ion binding, broad "
            "oxidoreductase activity, and periplasmic localization; this first pass does not assign a narrower "
            "physiological copper-oxidation reaction."
        ),
        "primary_function": TERM["GO:0016491"],
        "locations": [TERM["GO:0042597"]],
        "new_terms": [],
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


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def goa_support(gene: str, term_id: str) -> dict[str, str] | None:
    line = optional_first_line(GENE_ROOT / gene / f"{gene}-goa.tsv", term_id)
    if not line:
        return None
    return support(file_id(gene, "goa.tsv"), line)


def uniprot_evidence(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    data = [support(file_id(gene, "uniprot.txt"), first_line(uniprot, "DE   "))]
    if term_id:
        line = optional_first_line(uniprot, f"DR   GO; {term_id};")
        if line:
            data.append(support(file_id(gene, "uniprot.txt"), line))
    for marker in (
        ("DE   AltName:",),
        ("CC   -!- FUNCTION:",),
        ("CC   -!- SUBUNIT:",),
        ("CC   -!- SUBCELLULAR LOCATION:",),
        ("CC   -!- SIMILARITY:",),
        ("DR   InterPro;",),
        ("DR   Pfam;",),
        ("FT   SIGNAL",),
    ):
        line = optional_first_line(uniprot, *marker)
        if line and line not in {item["supporting_text"] for item in data}:
            data.append(support(file_id(gene, "uniprot.txt"), line))
    return data


def asta_evidence(gene: str) -> list[dict[str, str]]:
    asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    data = [support(file_id(gene, "deep-research-asta.md"), first_line(asta, "  protein_description:"))]
    for marker in ("  protein_family:", "  protein_domains:"):
        line = optional_first_line(asta, marker)
        if line:
            data.append(support(file_id(gene, "deep-research-asta.md"), line))
    return data


def standard_support(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    data: list[dict[str, str]] = []
    if term_id:
        goa = goa_support(gene, term_id)
        if goa:
            data.append(goa)
    data.extend(uniprot_evidence(gene, term_id))
    data.extend(asta_evidence(gene))
    return data


def reference_list(existing_refs: list[dict], gene: str, accession: str) -> list[dict]:
    refs: list[dict] = []
    seen = set()
    for ref in existing_refs:
        ref_id = ref["id"]
        seen.add(ref_id)
        refs.append(ref)
    titles = {
        file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({accession})",
        file_id(gene, "uniprot.txt"): f"UniProtKB entry for {gene} ({accession})",
        file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({accession})",
    }
    for ref_id, title in titles.items():
        if ref_id not in seen:
            refs.append({"id": ref_id, "title": title, "findings": []})
    return refs


def replacement(term_id: str) -> list[dict[str, str]]:
    return [TERM[term_id]]


def accept_review(gene: str, term_id: str, summary: str, reason: str) -> dict:
    return {
        "summary": summary,
        "action": "ACCEPT",
        "reason": reason,
        "supported_by": standard_support(gene, term_id),
    }


def modify_to_fmn_reductase(gene: str, term_id: str) -> dict:
    return {
        "summary": "The broad oxidoreductase annotation is directionally correct but less specific than the supported ArsH FMN reductase term.",
        "action": "MODIFY",
        "reason": (
            "UniProt and GOA already provide FMN reductase (NADPH) activity for this ArsH-family protein. "
            "Use GO:0052873 as the pathway-relevant molecular-function term and keep the broader oxidoreductase "
            "classes as parent context."
        ),
        "proposed_replacement_terms": replacement("GO:0052873"),
        "supported_by": standard_support(gene, term_id),
    }


def review_for_annotation(gene: str, term_id: str) -> dict:
    info = GENE_INFO[gene]
    if gene in ARSH_GENES:
        if term_id == "GO:0052873":
            return accept_review(
                gene,
                term_id,
                "FMN reductase (NADPH) activity is the most specific supported ArsH molecular-function annotation.",
                "The product name, ArsH-family assignment, FMN reductase domain, and GOA all support this activity.",
            )
        if term_id in {"GO:0016491", "GO:0016655"}:
            return modify_to_fmn_reductase(gene, term_id)
    if gene in COPB_GENES:
        if term_id == "GO:0005507":
            return accept_review(
                gene,
                term_id,
                "Copper ion binding is appropriate for this CopB copper-resistance protein.",
                "The InterPro CopB/Cu-R_B precursor domain and GOA support a copper-binding outer-membrane protein.",
            )
        if term_id == "GO:0006878":
            return accept_review(
                gene,
                term_id,
                "Intracellular copper ion homeostasis is appropriate copper-resistance process context.",
                "The copper-resistance product name and InterPro-derived GOA support the copper homeostasis process annotation.",
            )
        if term_id == "GO:0009279":
            return accept_review(
                gene,
                term_id,
                "Cell outer membrane localization is appropriate for CopB.",
                "GOA and the N-terminal signal peptide are consistent with a cell-envelope copper-resistance protein.",
            )
    if gene in COPA_GENES:
        if term_id == "GO:0005507":
            return accept_review(
                gene,
                term_id,
                "Copper ion binding is appropriate for this multicopper oxidase-family CopA protein.",
                "The CopA/multicopper oxidase domain architecture and InterPro-derived GOA support copper binding.",
            )
        if term_id == "GO:0016491":
            return accept_review(
                gene,
                term_id,
                "Broad oxidoreductase activity is the current supported GO molecular-function term for CopA.",
                "The multicopper oxidase-family domains support oxidoreductase-family chemistry, but the first pass does not assert a narrower substrate reaction.",
            )
        if term_id == "GO:0042597":
            return accept_review(
                gene,
                term_id,
                "Periplasmic localization is appropriate for this CopA copper-resistance protein.",
                "The GOA localization and signal/TAT-signal domain context support a periplasmic copper-resistance enzyme.",
            )
    raise ValueError(f"No review rule for {gene} {term_id}")


def new_annotation(gene: str, term_id: str) -> dict:
    term = TERM[term_id]
    qualifier = "involved_in" if term_id == "GO:0046685" else "enables"
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": f"First-pass evidence supports adding conservative {term['label']} for this {GENE_INFO[gene]['role']}.",
            "action": "NEW",
            "reason": (
                "The fetched GOA table has no rows for this gene. The recommendation is deliberately conservative and "
                "uses UniProt product/domain/keyword evidence plus Asta retrieval metadata rather than inventing a more "
                "specific arsenate reductase molecular-function term."
            ),
            "supported_by": standard_support(gene, term_id),
        },
    }


def core_for(gene: str) -> dict:
    info = GENE_INFO[gene]
    core = {
        "description": info["role"],
        "molecular_function": info["primary_function"],
        "supported_by": standard_support(gene, info["primary_function"]["id"]),
    }
    if "process" in info:
        core["directly_involved_in"] = [info["process"]]
    if info.get("locations"):
        core["locations"] = info["locations"]
    return core


def apply_review(gene: str, accession: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(read_text(path))
    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = GENE_INFO[gene]["description"]
    data["references"] = reference_list(data.get("references") or [], gene, accession)
    existing = data.get("existing_annotations") or []
    retained = []
    seen_new = {annotation.get("term", {}).get("id") for annotation in existing if annotation.get("review", {}).get("action") == "NEW"}
    for annotation in existing:
        if annotation.get("review", {}).get("action") == "NEW":
            retained.append(annotation)
            continue
        annotation["review"] = review_for_annotation(gene, annotation["term"]["id"])
        retained.append(annotation)
    for term_id in GENE_INFO[gene]["new_terms"]:
        if term_id not in seen_new:
            retained.append(new_annotation(gene, term_id))
    data["existing_annotations"] = retained
    data["core_functions"] = [core_for(gene)]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": (
                f"What exact substrate, redox partner, and stress phenotype define the physiological function of {gene} "
                "in Pseudomonas putida KT2440 metal resistance?"
            )
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Test purified {gene} where feasible and compare clean deletion/complemented strains under arsenate, arsenite, "
                "organoarsenical, and copper stress as appropriate for the gene family."
            ),
            "experiment_type": "targeted enzyme assay and metal-stress phenotyping",
        }
    ]
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str) -> None:
    info = GENE_INFO[gene]
    evidence = standard_support(gene, info["primary_function"]["id"])
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass arsenic/copper metal-resistance stress-bucket curation.",
        info["description"],
        "",
        "Primary provenance:",
    ]
    for item in evidence[:6]:
        lines.append(f"- [{item['reference_id']} \"{item['supporting_text']}\"]")
    lines.extend(
        [
            "",
            "Decision: keep the assignment conservative. ArsH proteins are curated to FMN reductase activity; "
            "arsenate reductase candidates get broad oxidoreductase plus arsenic-response context because the fetched GOA "
            "has no exact MF rows; CopAB proteins are represented as copper-binding/homeostasis or broad oxidoreductase "
            "cell-envelope copper-resistance proteins.",
        ]
    )
    (GENE_ROOT / gene / f"{gene}-notes.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def descriptor(term_id: str, description: str) -> dict:
    term = TERM[term_id]
    return {"preferred_term": term["label"], "term": term, "description": description}


def gene_ref(gene: str) -> dict:
    return {"selector_type": "GENE", "gene": {"preferred_term": gene}}


def annoton(
    annoton_id: str,
    label: str,
    gene: str,
    function_id: str,
    role_description: str,
    processes: list[str] | None = None,
    locations: list[str] | None = None,
) -> dict:
    item = {
        "id": annoton_id,
        "label": label,
        "participant": gene_ref(gene),
        "function": {"preferred_term": TERM[function_id]["label"], "term": TERM[function_id]},
        "role_description": role_description,
    }
    if processes:
        item["processes"] = [{"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]} for term_id in processes]
    if locations:
        item["locations"] = [{"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]} for term_id in locations]
    return item


def write_module() -> None:
    module = {
        "id": "MODULE:metal_resistance_detoxification_boundary",
        "title": "Metal resistance detoxification boundary",
        "description": (
            "Boundary module for the Pseudomonas putida KT2440 arsenic/copper resistance split from the "
            "stress/detoxification functional bucket. The module groups two ArsH FMN reductases, two low-molecular-weight "
            "arsenate reductase candidates, and two CopA/CopB copper-resistance pairs. It is curated as metal-resistance "
            "and cell-envelope detoxification context, not as a generic oxidative-stress module."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_stress_detoxification_arsenic_copper_metal_resistance.tsv",
                "title": "PSEPK stress/detoxification arsenic-copper metal-resistance split",
                "statement": (
                    "The batch table records eight PSEPK stress/detoxification genes assigned to the arsenic/copper "
                    "metal-resistance split: PP_1927, PP_1928, copB-I, copA-I, arsH, PP_2716, copB-II, and copA-II."
                ),
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_stress_detoxification_partition.tsv",
                "title": "PSEPK stress/detoxification functional-bucket partition",
                "statement": (
                    "The stress/detoxification umbrella was partitioned into peroxide/peroxiredoxin, glutathione/thiol, "
                    "arsenic/copper metal resistance, universal-stress-protein, cold/heat-shock, ThiJ/DJ-1/PfpI, "
                    "and miscellaneous stress-regulatory splits."
                ),
            },
        ],
        "module": {
            "id": "metal_resistance_detoxification_boundary",
            "label": "Metal resistance detoxification boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                descriptor("GO:0046685", "Arsenical stress-response context for low-molecular-weight arsenate reductase candidates."),
                descriptor("GO:0006878", "Copper homeostasis process context for CopB copper-resistance proteins."),
                descriptor("GO:0052873", "ArsH-family NADPH-dependent FMN reductase activity."),
                descriptor("GO:0016491", "Broad oxidoreductase activity for arsenate reductase and CopA-family candidates where exact chemistry is unresolved."),
                descriptor("GO:0005507", "Copper ion binding for CopA/CopB copper-resistance proteins."),
            ],
            "context": {
                "cellular_components": [
                    descriptor("GO:0009279", "CopB proteins are curated as cell outer membrane copper-resistance proteins."),
                    descriptor("GO:0042597", "CopA proteins are curated as periplasmic multicopper oxidase-family proteins."),
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "Arsenical resistance redox enzymes",
                    "node": {
                        "id": "arsenic_resistance_redox_enzymes",
                        "label": "ArsH and low-molecular-weight arsenate reductase candidates",
                        "module_type": "MOLECULAR_FUNCTION",
                        "description": (
                            "Two ArsH-family proteins have supported NADPH-dependent FMN reductase activity. The adjacent "
                            "low-molecular-weight arsenate reductase candidates have no fetched GOA rows, so the first pass "
                            "uses broad oxidoreductase activity and arsenic-response process context."
                        ),
                        "annotons": [
                            annoton(
                                "PP_1927_arsh_fmn_reductase",
                                "PP_1927: ArsH-family NADPH-dependent FMN reductase",
                                "PP_1927",
                                "GO:0052873",
                                "ArsH-family FMN reductase in arsenical-resistance operon context; organoarsenical substrate unresolved.",
                            ),
                            annoton(
                                "PP_1928_arsenate_reductase_candidate",
                                "PP_1928: arsenate reductase candidate",
                                "PP_1928",
                                "GO:0016491",
                                "Low-molecular-weight arsenate reductase candidate; exact GO molecular-function term unresolved.",
                                processes=["GO:0046685"],
                            ),
                            annoton(
                                "arsH_fmn_reductase",
                                "arsH: ArsH-family NADPH-dependent FMN reductase",
                                "arsH",
                                "GO:0052873",
                                "ArsH-family FMN reductase in arsenical-resistance operon context; organoarsenical substrate unresolved.",
                            ),
                            annoton(
                                "PP_2716_arsenate_reductase_candidate",
                                "PP_2716: arsenate reductase candidate",
                                "PP_2716",
                                "GO:0016491",
                                "Low-molecular-weight arsenate reductase candidate; exact GO molecular-function term unresolved.",
                                processes=["GO:0046685"],
                            ),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "Outer-membrane copper-resistance proteins",
                    "node": {
                        "id": "copb_outer_membrane_copper_resistance",
                        "label": "CopB outer-membrane copper-resistance proteins",
                        "module_type": "MOLECULAR_FUNCTION",
                        "description": (
                            "copB-I and copB-II encode CopB-domain copper-resistance proteins with copper-binding, "
                            "outer-membrane localization, and intracellular copper ion homeostasis annotations."
                        ),
                        "annotons": [
                            annoton(
                                "copB_I_copper_resistance",
                                "copB-I: copper resistance protein B",
                                "copB-I",
                                "GO:0005507",
                                "Outer-membrane copper-binding protein associated with copper ion homeostasis.",
                                processes=["GO:0006878"],
                                locations=["GO:0009279"],
                            ),
                            annoton(
                                "copB_II_copper_resistance",
                                "copB-II: copper resistance protein B",
                                "copB-II",
                                "GO:0005507",
                                "Outer-membrane copper-binding protein associated with copper ion homeostasis.",
                                processes=["GO:0006878"],
                                locations=["GO:0009279"],
                            ),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "Periplasmic CopA multicopper oxidase-family proteins",
                    "node": {
                        "id": "copa_periplasmic_copper_resistance",
                        "label": "CopA periplasmic copper-resistance proteins",
                        "module_type": "MOLECULAR_FUNCTION",
                        "description": (
                            "copA-I and copA-II encode periplasmic CopA/multicopper oxidase-family proteins. "
                            "GOA supports copper ion binding, broad oxidoreductase activity, and periplasmic localization, "
                            "but this first pass does not resolve the physiological copper oxidation reaction."
                        ),
                        "annotons": [
                            annoton(
                                "copA_I_multicopper_oxidoreductase",
                                "copA-I: copper resistance protein A",
                                "copA-I",
                                "GO:0016491",
                                "Periplasmic multicopper oxidase-family copper-resistance protein with unresolved exact substrate reaction.",
                                locations=["GO:0042597"],
                            ),
                            annoton(
                                "copA_II_multicopper_oxidoreductase",
                                "copA-II: copper resistance protein A",
                                "copA-II",
                                "GO:0016491",
                                "Periplasmic multicopper oxidase-family copper-resistance protein with unresolved exact substrate reaction.",
                                locations=["GO:0042597"],
                            ),
                        ],
                    },
                },
            ],
        },
        "notes": (
            "Curation recommendations: use FMN reductase (NADPH) activity as the core MF for PP_1927 and arsH, "
            "and treat arsenical-resistance specificity as context until substrate evidence is stronger. Add conservative "
            "oxidoreductase activity and arsenic-response process context for PP_1928 and PP_2716; do not invent a specific "
            "arsenate reductase GO term in this first pass. Keep copB-I, copB-II, copA-I, and copA-II as cell-envelope "
            "copper-resistance proteins; CopA is not a P-type copper ATPase in this locus context. Open questions: which "
            "arsenic and copper species are the physiological substrates for each duplicated ArsH/ArsC-like and CopAB pair, "
            "and are the two arsenical-resistance loci and two copAB loci differentially induced by arsenate, arsenite, "
            "organoarsenicals, or copper?"
        ),
    }
    MODULE_YAML.write_text(yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def update_batch_status(path: Path, genes: set[str]) -> None:
    rows = list(csv.DictReader(path.open(encoding="utf-8"), delimiter="\t"))
    if not rows:
        return
    for row in rows:
        if row["gene"] in genes:
            row["recommended_action"] = "COMPLETED_SUBMODULE"
            row["bucket_status"] = "CURATED"
            row["review_status"] = "PRESENT"
            row["curation_status"] = "CURATED"
            row["asta_research_status"] = "PRESENT"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = list(csv.DictReader(BATCH_TSV.open(encoding="utf-8"), delimiter="\t"))
    genes = {row["gene"] for row in rows}
    for row in rows:
        gene = row["gene"]
        apply_review(gene, row["uniprot_accession"])
        write_notes(gene)
        print(f"Curated {gene}")
    write_module()
    update_batch_status(BATCH_TSV, genes)
    update_batch_status(PARTITION_TSV, genes)
    print(f"Wrote {MODULE_YAML.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
