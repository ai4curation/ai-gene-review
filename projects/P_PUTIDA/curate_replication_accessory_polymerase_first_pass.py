#!/usr/bin/env python3
"""First-pass curation for the PSEPK replication accessory/polymerase split."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "bacterial_dna_replication.yaml"
BATCH_TSV = "projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_replication_accessory_polymerase.tsv"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0000166": {"id": "GO:0000166", "label": "nucleotide binding"},
    "GO:0000731": {"id": "GO:0000731", "label": "DNA synthesis involved in DNA repair"},
    "GO:0003676": {"id": "GO:0003676", "label": "nucleic acid binding"},
    "GO:0003677": {"id": "GO:0003677", "label": "DNA binding"},
    "GO:0003678": {"id": "GO:0003678", "label": "DNA helicase activity"},
    "GO:0003697": {"id": "GO:0003697", "label": "single-stranded DNA binding"},
    "GO:0003887": {"id": "GO:0003887", "label": "DNA-directed DNA polymerase activity"},
    "GO:0004386": {"id": "GO:0004386", "label": "helicase activity"},
    "GO:0005524": {"id": "GO:0005524", "label": "ATP binding"},
    "GO:0005829": {"id": "GO:0005829", "label": "cytosol"},
    "GO:0006259": {"id": "GO:0006259", "label": "DNA metabolic process"},
    "GO:0006260": {"id": "GO:0006260", "label": "DNA replication"},
    "GO:0006261": {"id": "GO:0006261", "label": "DNA-templated DNA replication"},
    "GO:0006269": {"id": "GO:0006269", "label": "DNA replication, synthesis of primer"},
    "GO:0006270": {"id": "GO:0006270", "label": "DNA replication initiation"},
    "GO:0006302": {"id": "GO:0006302", "label": "double-strand break repair"},
    "GO:0008047": {"id": "GO:0008047", "label": "enzyme activator activity"},
    "GO:0016787": {"id": "GO:0016787", "label": "hydrolase activity"},
    "GO:0016887": {"id": "GO:0016887", "label": "ATP hydrolysis activity"},
    "GO:0017116": {"id": "GO:0017116", "label": "single-stranded DNA helicase activity"},
    "GO:0032297": {"id": "GO:0032297", "label": "negative regulation of DNA-templated DNA replication initiation"},
    "GO:0043138": {"id": "GO:0043138", "label": "3'-5' DNA helicase activity"},
    "GO:0043139": {"id": "GO:0043139", "label": "5'-3' DNA helicase activity"},
    "GO:0071897": {"id": "GO:0071897", "label": "DNA biosynthetic process"},
}


GENE_INFO = {
    "PP_0978": {
        "accession": "Q88P75",
        "description": "PP_0978 is a low-evidence DNA polymerase III chi-like candidate in the replication-accessory bucket. The fetched UniProt record has only a ProtNLM-derived product name and no GOA, InterPro, Pfam, or family support, so no GO function is promoted in this first pass.",
        "core": [],
    },
    "hda": {
        "accession": "Q88MA6",
        "description": "hda encodes a DnaA/Hda-family replication-initiation regulator. Current GOA, InterPro, Pfam, and PANTHER evidence support a role in preventing premature DNA replication reinitiation rather than a standalone replication enzyme activity.",
        "core": [
            {
                "description": "Hda-family negative regulator of DNA replication reinitiation.",
                "directly_involved_in": [TERM["GO:0032297"]],
                "support_term": "GO:0032297",
            }
        ],
    },
    "PP_2270": {
        "accession": "Q88KM0",
        "description": "PP_2270 is a T7-like helicase/primase-domain replication accessory candidate with SF4/DnaB-like helicase, TOPRIM, and twinkle-like family evidence. The supported first-pass role is 5'-3' DNA helicase activity in DNA replication and primer-synthesis context.",
        "core": [
            {
                "description": "T7-like primase/helicase-family 5'-3' DNA helicase candidate in replication/primer-synthesis context.",
                "molecular_function": TERM["GO:0043139"],
                "directly_involved_in": [TERM["GO:0006260"], TERM["GO:0006269"]],
                "support_term": "GO:0043139",
            }
        ],
    },
    "PP_2273": {
        "accession": "Q88KL7",
        "description": "PP_2273 is a type-A DNA-directed DNA polymerase-family protein with EC 2.7.7.7 support. It is retained as a replication/repair boundary polymerase rather than as part of the canonical Pol III core.",
        "core": [
            {
                "description": "Type-A DNA-directed DNA polymerase candidate in DNA-templated DNA replication context.",
                "molecular_function": TERM["GO:0003887"],
                "directly_involved_in": [TERM["GO:0006261"]],
                "support_term": "GO:0003887",
            }
        ],
    },
    "rarA": {
        "accession": "Q88FT0",
        "description": "rarA encodes a RarA/MGS1/WRNIP1-family AAA+ DNA-dependent ATPase associated with stalled DNA replication responses. The ATPase and replication context are retained, while helicase/enzyme-activator specificity from broad phylogenetic transfer is treated cautiously.",
        "core": [
            {
                "description": "RarA/MGS1-family DNA-dependent ATPase associated with stalled replication responses.",
                "molecular_function": TERM["GO:0016887"],
                "directly_involved_in": [TERM["GO:0006260"]],
                "support_term": "GO:0016887",
            }
        ],
    },
    "rep": {
        "accession": "Q88CB7",
        "description": "rep encodes an ATP-dependent Rep/UvrD-subfamily DNA helicase. UniProt/HAMAP and GOA support a single-stranded DNA-dependent 3'-5' helicase acting in DNA replication, with recombinational repair retained as shared repair context.",
        "core": [
            {
                "description": "Rep-family 3'-5' DNA helicase for DNA replication fork/accessory context.",
                "molecular_function": TERM["GO:0043138"],
                "directly_involved_in": [TERM["GO:0006260"]],
                "locations": [TERM["GO:0005829"]],
                "support_term": "GO:0043138",
            }
        ],
    },
}


GENERIC_REVIEWS = {
    "GO:0000166": ("MARK_AS_OVER_ANNOTATED", "Nucleotide binding is too broad.", "A directional helicase, ATPase, or polymerase term is more informative where supported."),
    "GO:0003676": ("MARK_AS_OVER_ANNOTATED", "Nucleic acid binding is too broad.", "The supported catalytic DNA polymerase or helicase term is more informative."),
    "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is retained as substrate context.", "DNA binding supports the replication accessory role but is not the primary activity."),
    "GO:0003678": ("KEEP_AS_NON_CORE", "DNA helicase activity is retained as parent context.", "A directional 5'-3' or 3'-5' DNA helicase term is more specific where supported."),
    "GO:0003697": ("KEEP_AS_NON_CORE", "Single-stranded DNA binding is retained as substrate context.", "The substrate-binding row supports helicase/replisome activity but is less informative than the catalytic role."),
    "GO:0004386": ("KEEP_AS_NON_CORE", "Generic helicase activity is retained as parent context.", "A directional DNA helicase term is more specific where supported."),
    "GO:0005524": ("KEEP_AS_NON_CORE", "ATP binding is retained as cofactor context.", "ATP binding supports ATPase/helicase activity but is not the most specific function."),
    "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "Hydrolase activity is too broad.", "ATPase or directional helicase activity captures the supported function better."),
    "GO:0016887": ("KEEP_AS_NON_CORE", "ATP hydrolysis activity is retained as catalytic support.", "The directional helicase or RarA-specific ATPase context is more informative where available."),
}


GENE_REVIEWS = {
    "hda": {
        "GO:0006260": ("KEEP_AS_NON_CORE", "DNA replication is retained as broad pathway context.", "Hda regulates replication reinitiation rather than acting as a core replication enzyme."),
        "GO:0006270": ("KEEP_AS_NON_CORE", "DNA replication initiation is retained as pathway context.", "The more specific supported role is negative regulation of reinitiation."),
        "GO:0032297": ("ACCEPT", "Negative regulation of DNA replication initiation is supported.", "Hda-family/domain evidence and GOA support prevention of premature replication reinitiation."),
    },
    "PP_2270": {
        "GO:0006260": ("ACCEPT", "DNA replication context is supported.", "The DnaB-like helicase, TOPRIM, and twinkle-like domain evidence supports replication accessory context."),
        "GO:0006269": ("ACCEPT", "Primer-synthesis context is supported.", "The helicase/primase and TOPRIM domain architecture supports primase-associated replication context."),
        "GO:0043139": ("ACCEPT", "5'-3' DNA helicase activity is supported.", "InterPro and GOA support a directional DnaB-like/twinkle-like DNA helicase activity."),
    },
    "PP_2273": {
        "GO:0003887": ("ACCEPT", "DNA-directed DNA polymerase activity is supported.", "UniProt EC, InterPro, PANTHER, and GOA support type-A DNA polymerase activity."),
        "GO:0006259": ("KEEP_AS_NON_CORE", "DNA metabolic process is retained as broad context.", "The specific supported activity is DNA-directed DNA polymerase activity."),
        "GO:0006260": ("KEEP_AS_NON_CORE", "DNA replication is retained as broad replication context.", "The more specific process row is DNA-templated DNA replication."),
        "GO:0006261": ("ACCEPT", "DNA-templated DNA replication is supported.", "Type-A DNA polymerase family evidence supports DNA synthesis on a DNA template."),
        "GO:0006302": ("KEEP_AS_NON_CORE", "Double-strand break repair is retained as possible repair context.", "The TreeGrafter repair row is plausible for a boundary polymerase but not promoted as the core replication-accessory role."),
        "GO:0071897": ("KEEP_AS_NON_CORE", "DNA biosynthetic process is retained as broad synthesis context.", "The catalytic DNA polymerase term is more informative."),
    },
    "rarA": {
        "GO:0000731": ("KEEP_AS_NON_CORE", "DNA repair synthesis is retained as stalled-fork/repair context.", "RarA is linked to stalled replication responses, but this process is less certain than the ATPase and replication context."),
        "GO:0006260": ("ACCEPT", "DNA replication context is supported.", "UniProt function and InterPro evidence place RarA in stalled replication responses."),
        "GO:0006261": ("KEEP_AS_NON_CORE", "DNA-templated DNA replication is retained as broad pathway context.", "The current evidence supports replication response context rather than direct DNA synthesis."),
        "GO:0008047": ("MARK_AS_OVER_ANNOTATED", "Enzyme activator activity is too generic for RarA.", "The local record supports DNA-dependent ATPase/restart context, not a specific activator mechanism."),
        "GO:0016887": ("ACCEPT", "ATP hydrolysis activity is supported.", "AAA+ RarA/MGS1 family and GOA evidence support ATPase activity."),
        "GO:0017116": ("MARK_AS_OVER_ANNOTATED", "Single-stranded DNA helicase activity is not promoted.", "UniProt describes RarA as a DNA-dependent ATPase, not a directional helicase."),
    },
    "rep": {
        "GO:0000725": ("KEEP_AS_NON_CORE", "Recombinational repair is retained as shared repair context.", "Rep-family helicases can participate in repair, but the core supported role here is replication-associated 3'-5' DNA helicase activity."),
        "GO:0005829": ("ACCEPT", "Cytosol localization is retained.", "The localization is compatible with soluble bacterial DNA replication helicase activity."),
        "GO:0006260": ("ACCEPT", "DNA replication is supported.", "UniProt/HAMAP function and GOA place Rep helicase in DNA replication."),
        "GO:0043138": ("ACCEPT", "3'-5' DNA helicase activity is supported.", "HAMAP/UniRule, EC 5.6.2.4, and GOA support directional Rep helicase activity."),
    },
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
    for marker in ("CC   -!- FUNCTION:", "CC   -!- CATALYTIC ACTIVITY:", "DR   PANTHER;", "DR   Pfam;", "KW   ", "FT   DOMAIN"):
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
    return {"summary": summary, "action": action, "reason": reason, "supported_by": standard_support(gene, term_id)}


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
        "PP_0978": "Is PP_0978 a real DNA polymerase III chi-like accessory protein, or a ProtNLM/product-name false positive?",
        "hda": "How does KT2440 Hda interact with DnaA and the beta clamp to prevent over-initiation?",
        "PP_2270": "Is PP_2270 an active T7-like helicase/primase in chromosomal replication, mobile-element replication, or another DNA metabolism context?",
        "PP_2273": "Does PP_2273 act as a replication-associated type-A DNA polymerase or primarily in repair/mobile-element DNA synthesis?",
        "rarA": "Which stalled-fork or replication-restart pathway uses KT2440 RarA?",
        "rep": "What replication-fork or repair substrates are handled by KT2440 Rep helicase?",
    }[gene]


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
    data["existing_annotations"] = existing
    data["core_functions"] = core_functions(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": suggested_question(gene), "experts": []}]
    data["suggested_experiments"] = [
        {
            "experiment_type": "genetic and biochemical replication-accessory validation",
            "description": f"Test {gene} deletion/overexpression phenotypes under replication stress and assay the predicted DNA replication accessory activity with purified protein where feasible.",
        }
    ]
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str) -> None:
    info = GENE_INFO[gene]
    path = GENE_ROOT / gene / f"{gene}-notes.md"
    support_term = info["core"][0].get("support_term") if info["core"] else None
    evidence = standard_support(gene, support_term)
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass replication-accessory/polymerase split curation.",
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
    lines.extend(["", "Decision: route as replication accessory/polymerase boundary context; do not over-promote weak product names.", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def descriptor(term_id: str) -> dict:
    return {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]}


def annoton(annoton_id: str, gene: str, role: str, function: str | None = None, processes: list[str] | None = None, locations: list[str] | None = None) -> dict:
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


def append_unique_evidence(data: dict) -> None:
    existing = {item.get("source_id") for item in data.get("evidence", [])}
    additions = [
        {
            "source_id": f"file:{BATCH_TSV}",
            "title": "PSEPK replication accessory/polymerase split table",
            "statement": "The split table records six replication-accessory candidates from the broad DNA replication/repair/recombination functional bucket.",
        },
        {
            "source_id": "file:PSEPK/PP_0978/PP_0978-ai-review.yaml",
            "title": "Curated PP_0978 review",
            "statement": "PP_0978 is retained as a low-evidence Pol III chi-like candidate and no GO function is promoted from the ProtNLM-only product name.",
        },
    ]
    for item in additions:
        if item["source_id"] not in existing:
            data.setdefault("evidence", []).append(item)


def append_concepts(module: dict) -> None:
    existing = {concept["term"]["id"] for concept in module.get("concepts", []) if "term" in concept}
    for term_id, description in {
        "GO:0032297": "Hda-mediated negative control of replication reinitiation.",
        "GO:0043138": "Rep-family 3'-5' helicase accessory activity.",
        "GO:0016887": "AAA+ ATPase activity for RarA/stalled-fork response context.",
    }.items():
        if term_id not in existing:
            module.setdefault("concepts", []).append({**descriptor(term_id), "description": description})
            existing.add(term_id)


def extend_module() -> None:
    data = yaml.safe_load(read_text(MODULE_PATH))
    append_unique_evidence(data)
    if "replication-accessory/polymerase split" not in data.get("notes", ""):
        data["notes"] = (
            data.get("notes", "")
            + " The replication-accessory/polymerase split adds Hda reinitiation control, PP_2270 helicase/primase context, PP_2273 type-A polymerase boundary context, RarA stalled-replication ATPase context, and Rep helicase. PP_0978 remains an unpromoted low-evidence chi-like candidate."
        ).strip()
    module = data["module"]
    append_concepts(module)
    parts = module.setdefault("parts", [])
    parts = [part for part in parts if part.get("node", {}).get("id") != "replication_accessory_polymerase_restart_boundary"]
    parts.append(
        {
            "order": 5,
            "role": "Replication initiation control, accessory helicases, and boundary polymerases",
            "node": {
                "id": "replication_accessory_polymerase_restart_boundary",
                "label": "Replication accessory, restart, and boundary polymerase candidates",
                "module_type": "BIOLOGICAL_PROCESS",
                "description": "Accessory split from the broad DNA bucket. These genes support replication regulation, fork/restart helicase or ATPase activity, and secondary polymerase context, but are not part of the canonical Pol III core.",
                "annotons": [
                    annoton("hda_reinitiation_control", "hda", "Hda-family negative regulator of DNA replication reinitiation.", processes=["GO:0032297", "GO:0006270"]),
                    annoton("pp2270_t7_like_helicase_primase", "PP_2270", "T7-like primase/helicase-family 5'-3' DNA helicase candidate.", function="GO:0043139", processes=["GO:0006260", "GO:0006269"]),
                    annoton("pp2273_type_a_polymerase_boundary", "PP_2273", "Type-A DNA polymerase replication/repair boundary candidate.", function="GO:0003887", processes=["GO:0006261"]),
                    annoton("rara_stalled_replication_atpase", "rarA", "RarA/MGS1-family ATPase associated with stalled replication responses.", function="GO:0016887", processes=["GO:0006260"]),
                    annoton("rep_3_5_helicase", "rep", "Rep-family 3'-5' DNA helicase for replication accessory context.", function="GO:0043138", processes=["GO:0006260"], locations=["GO:0005829"]),
                ],
            },
        }
    )
    module["parts"] = sorted(parts, key=lambda item: item.get("order", 999))
    MODULE_PATH.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    for gene in GENE_INFO:
        apply_review(gene)
        write_notes(gene)
    extend_module()


if __name__ == "__main__":
    main()
