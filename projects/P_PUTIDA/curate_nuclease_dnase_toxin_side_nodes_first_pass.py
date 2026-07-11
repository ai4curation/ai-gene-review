#!/usr/bin/env python3
"""First-pass curation for the PSEPK nuclease/DNase/toxin side-node split."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "nuclease_dnase_boundary.yaml"
BATCH_TSV = "projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_nuclease_dnase_toxin_side_nodes.tsv"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0000175": {"id": "GO:0000175", "label": "3'-5'-RNA exonuclease activity"},
    "GO:0003676": {"id": "GO:0003676", "label": "nucleic acid binding"},
    "GO:0003677": {"id": "GO:0003677", "label": "DNA binding"},
    "GO:0004518": {"id": "GO:0004518", "label": "nuclease activity"},
    "GO:0004519": {"id": "GO:0004519", "label": "endonuclease activity"},
    "GO:0004521": {"id": "GO:0004521", "label": "RNA endonuclease activity"},
    "GO:0004527": {"id": "GO:0004527", "label": "exonuclease activity"},
    "GO:0004528": {"id": "GO:0004528", "label": "phosphodiesterase I activity"},
    "GO:0004530": {"id": "GO:0004530", "label": "deoxyribonuclease I activity"},
    "GO:0005829": {"id": "GO:0005829", "label": "cytosol"},
    "GO:0006401": {"id": "GO:0006401", "label": "RNA catabolic process"},
    "GO:0008270": {"id": "GO:0008270", "label": "zinc ion binding"},
    "GO:0008409": {"id": "GO:0008409", "label": "5'-3' exonuclease activity"},
    "GO:0016787": {"id": "GO:0016787", "label": "hydrolase activity"},
    "GO:0016788": {"id": "GO:0016788", "label": "hydrolase activity, acting on ester bonds"},
    "GO:0017108": {"id": "GO:0017108", "label": "5'-flap endonuclease activity"},
    "GO:0033567": {"id": "GO:0033567", "label": "DNA replication, Okazaki fragment processing"},
    "GO:0036297": {"id": "GO:0036297", "label": "interstrand cross-link repair"},
    "GO:0045892": {"id": "GO:0045892", "label": "negative regulation of DNA-templated transcription"},
    "GO:0046872": {"id": "GO:0046872", "label": "metal ion binding"},
    "GO:1990599": {"id": "GO:1990599", "label": "3' overhang single-stranded DNA endonuclease activity"},
}


GENE_INFO = {
    "PP_1306": {
        "accession": "Q88NA6",
        "description": "PP_1306 is a pyocin/colicin S-type killer-domain protein with HNH nuclease-family domains. This first pass treats it as bacteriocin/toxin nuclease side context rather than as chromosomal DNA repair.",
        "core": [{"description": "Pyocin/colicin-family HNH endonuclease toxin candidate.", "molecular_function": TERM["GO:0004519"], "support_term": "GO:0004519"}],
    },
    "PP_1554": {
        "accession": "Q88ML7",
        "description": "PP_1554 is a VRR-NUC-domain nuclease-family protein. Current evidence supports broad nuclease-family activity but does not resolve DNA versus RNA substrate or pathway context.",
        "core": [{"description": "VRR-NUC-domain nuclease candidate with unresolved substrate.", "molecular_function": TERM["GO:0004518"], "support_term": "GO:0004518"}],
        "new_terms": ["GO:0004518"],
    },
    "PP_2276": {
        "accession": "Q88KL4",
        "description": "PP_2276 is a FEN/5'-3' exonuclease-family protein annotated as a phage exonuclease. It is retained as nuclease/mobile-element boundary context with 5'-3' exonuclease and 5'-flap endonuclease activities.",
        "core": [
            {"description": "FEN-like 5'-to-3' exonuclease activity.", "molecular_function": TERM["GO:0008409"], "support_term": "GO:0008409"},
            {"description": "FEN-family 5'-flap endonuclease activity.", "molecular_function": TERM["GO:0017108"], "support_term": "GO:0017108"},
        ],
    },
    "tatD": {
        "accession": "Q88KH9",
        "description": "tatD encodes a TatD-family metal-dependent hydrolase annotated as a cytoplasmic DNase/RNase. UniProt family and domain evidence support a TatD nuclease/exonuclease candidate, but the fetched GOA block contains only a broad ester-hydrolase row.",
        "core": [{"description": "TatD-family metal-dependent nuclease/exonuclease candidate.", "molecular_function": TERM["GO:0004527"], "support_term": "GO:0004527"}],
        "new_terms": ["GO:0004527"],
    },
    "endX": {
        "accession": "Q88K41",
        "description": "endX encodes an EndA/NucM-family extracellular DNA endonuclease candidate in Pseudomonas putida KT2440. GOA/UniProt EC evidence supports deoxyribonuclease I activity.",
        "core": [{"description": "Extracellular EndA/NucM-family deoxyribonuclease I activity.", "molecular_function": TERM["GO:0004530"], "support_term": "GO:0004530"}],
    },
    "PP_2838": {
        "accession": "Q88J11",
        "description": "PP_2838 is a FAN1/VRR-NUC-family phosphodiesterase I candidate. UniProt and GOA support phosphodiesterase I activity and a possible interstrand cross-link repair context, but substrate specificity remains broad.",
        "core": [{"description": "FAN1-like phosphodiesterase I/nuclease candidate.", "molecular_function": TERM["GO:0004528"], "support_term": "GO:0004528"}],
    },
    "yoeB": {
        "accession": "Q88IR0",
        "description": "yoeB encodes a YoeB/RelE-ParE-toxin-family mRNA interferase candidate. It is curated as RNA-toxin/ribonuclease context rather than DNA repair, and the transcription-regulation row is treated as over-propagated toxin-family context.",
        "core": [{"description": "YoeB-family mRNA-interferase endonuclease involved in RNA catabolism.", "molecular_function": TERM["GO:0004519"], "directly_involved_in": [TERM["GO:0006401"]], "support_term": "GO:0004519"}],
    },
    "endA": {
        "accession": "Q88HI2",
        "description": "endA encodes an EndA/NucM-family endonuclease I candidate with signal-peptide context. The fetched GOA block contains only broad nuclease activity, so a UniProt-backed endonuclease row is added.",
        "core": [{"description": "EndA/NucM-family endonuclease I activity.", "molecular_function": TERM["GO:0004519"], "support_term": "GO:0004519"}],
        "new_terms": ["GO:0004519"],
    },
    "PP_3883": {
        "accession": "Q88G43",
        "description": "PP_3883 is a YajD-like HNH nuclease-family protein. Current evidence supports endonuclease activity, zinc-binding/domain context, and cytosolic localization but not a specific DNA repair pathway role.",
        "core": [{"description": "HNH-family endonuclease candidate.", "molecular_function": TERM["GO:0004519"], "locations": [TERM["GO:0005829"]], "support_term": "GO:0004519"}],
    },
    "PP_3890": {
        "accession": "Q88G36",
        "description": "PP_3890 is a second VRR-NUC-domain nuclease-family protein. Like PP_1554, it is retained as a broad nuclease candidate without assigning a specific DNA repair process.",
        "core": [{"description": "VRR-NUC-domain nuclease candidate with unresolved substrate.", "molecular_function": TERM["GO:0004518"], "support_term": "GO:0004518"}],
        "new_terms": ["GO:0004518"],
    },
    "PP_4247": {
        "accession": "Q88F52",
        "description": "PP_4247 is an ERI-1/RNase-H-like 3'-5' exonuclease-family protein. GOA/InterPro support 3'-5'-RNA exonuclease activity, making this an RNA-processing nuclease side node rather than DNA repair core.",
        "core": [{"description": "ERI-1-like 3'-5'-RNA exonuclease activity.", "molecular_function": TERM["GO:0000175"], "support_term": "GO:0000175"}],
    },
    "yajD": {
        "accession": "Q88E82",
        "description": "yajD encodes a YajD-like HNH nuclease-family protein. Current metadata support endonuclease activity, HNH/zinc context, and cytosolic localization, without a resolved pathway substrate.",
        "core": [{"description": "YajD/HNH-family endonuclease candidate.", "molecular_function": TERM["GO:0004519"], "locations": [TERM["GO:0005829"]], "support_term": "GO:0004519"}],
    },
    "PP_5086": {
        "accession": "Q88CU4",
        "description": "PP_5086 is an SNase-domain nuclease candidate. Existing GOA includes a specific 3' overhang single-stranded DNA endonuclease row, and UniProt supports a broad endonuclease/nuclease context.",
        "core": [{"description": "SNase-domain endonuclease candidate.", "molecular_function": TERM["GO:0004519"], "support_term": "GO:0004519"}],
        "new_terms": ["GO:0004519"],
    },
    "PP_5295": {
        "accession": "Q88C88",
        "description": "PP_5295 is a YicC/YloC-family protein with RNA endonuclease-family annotation and divalent-metal cofactor context. It is retained as an RNA endonuclease side node rather than DNA repair.",
        "core": [{"description": "YicC-family RNA endonuclease candidate.", "molecular_function": TERM["GO:0004521"], "support_term": "GO:0004521"}],
    },
}


GENERIC_REVIEWS = {
    "GO:0003676": ("MARK_AS_OVER_ANNOTATED", "Nucleic acid binding is too broad.", "A nuclease or exonuclease term better captures the supported activity where available."),
    "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is retained as substrate context.", "DNA binding is expected for DNA nuclease/exonuclease proteins but is less informative than the catalytic term."),
    "GO:0004518": ("KEEP_AS_NON_CORE", "Broad nuclease activity is retained as non-core parent context.", "A more specific endonuclease, exonuclease, DNase, RNase, or phosphodiesterase term is preferred where supported."),
    "GO:0004519": ("ACCEPT", "Endonuclease activity is supported.", "The local family/domain evidence supports endonuclease-family activity."),
    "GO:0004521": ("ACCEPT", "RNA endonuclease activity is supported.", "The local family/domain evidence supports an RNA endonuclease side-node function."),
    "GO:0004527": ("KEEP_AS_NON_CORE", "Generic exonuclease activity is retained as parent context.", "A directional DNA or RNA exonuclease term is preferred where available."),
    "GO:0005829": ("ACCEPT", "Cytosol localization is retained.", "The annotation is compatible with soluble bacterial nuclease/toxin proteins."),
    "GO:0008270": ("KEEP_AS_NON_CORE", "Zinc ion binding is retained as HNH/cofactor context.", "Zinc binding supports nuclease-family structure but is not the primary function."),
    "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "Hydrolase activity is too broad.", "Specific nuclease or phosphodiesterase terms are more informative."),
    "GO:0016788": ("MARK_AS_OVER_ANNOTATED", "Ester-hydrolase activity is too broad.", "Specific nuclease or phosphodiesterase terms are more informative."),
    "GO:0046872": ("KEEP_AS_NON_CORE", "Metal ion binding is retained as cofactor context.", "Metal binding supports nuclease catalysis but is not the primary function."),
}


GENE_REVIEWS = {
    "PP_1554": {"GO:0004518": ("NEW", "Nuclease activity is added from UniProt metadata.", "The VRR-NUC domain and UniProt flat file support broad nuclease activity, while the fetched GOA block lacks this catalytic row.")},
    "PP_2276": {
        "GO:0008409": ("ACCEPT", "5'-3' exonuclease activity is supported.", "FEN/5'-3' exonuclease family evidence supports this activity."),
        "GO:0017108": ("ACCEPT", "5'-flap endonuclease activity is supported.", "FEN-family InterPro evidence supports flap endonuclease activity."),
        "GO:0033567": ("KEEP_AS_NON_CORE", "Okazaki-fragment processing is retained as FEN-family context.", "The product is annotated as phage exonuclease, so a chromosomal Okazaki-fragment process is not promoted as core."),
    },
    "tatD": {"GO:0004527": ("NEW", "Exonuclease activity is added from UniProt metadata.", "TatD-family DNase/RNase and UniProt GO evidence support nuclease/exonuclease context, while fetched GOA has only broad hydrolase activity.")},
    "endX": {"GO:0004530": ("ACCEPT", "Deoxyribonuclease I activity is supported.", "EndA/NucM family, EC, and GOA evidence support DNase I activity.")},
    "PP_2838": {
        "GO:0004528": ("ACCEPT", "Phosphodiesterase I activity is supported.", "UniProt EC and GOA evidence support phosphodiesterase I activity."),
        "GO:0036297": ("KEEP_AS_NON_CORE", "Interstrand cross-link repair is retained as FAN1-family context.", "The family context suggests DNA-repair relevance, but substrate/process specificity is not resolved for KT2440."),
    },
    "yoeB": {
        "GO:0006401": ("ACCEPT", "RNA catabolic process is supported.", "YoeB/RelE-family toxin context supports mRNA cleavage/RNA catabolism."),
        "GO:0045892": ("MARK_AS_OVER_ANNOTATED", "Transcriptional regulation is likely over-propagated.", "YoeB-family mRNA interferases act through RNA cleavage/translation inhibition rather than direct transcription-factor function."),
    },
    "endA": {"GO:0004519": ("NEW", "Endonuclease activity is added from UniProt metadata.", "EndA/NucM family and UniProt GO evidence support endonuclease activity, while fetched GOA has only broad nuclease activity.")},
    "PP_3883": {},
    "PP_3890": {"GO:0004518": ("NEW", "Nuclease activity is added from UniProt metadata.", "The VRR-NUC domain and UniProt flat file support broad nuclease activity, while the fetched GOA block lacks this catalytic row.")},
    "PP_4247": {"GO:0000175": ("ACCEPT", "3'-5'-RNA exonuclease activity is supported.", "ERI-1/RNase-H-like family evidence supports RNA exonuclease activity.")},
    "PP_5086": {
        "GO:0004519": ("NEW", "Endonuclease activity is added from UniProt metadata.", "SNase-domain and UniProt GO evidence support endonuclease activity, while fetched GOA lacks that parent catalytic row."),
        "GO:1990599": ("ACCEPT", "3' overhang single-stranded DNA endonuclease activity is retained.", "GOA supports a specific SNase-domain DNA endonuclease activity, although substrate scope needs validation."),
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
    for marker in ("CC   -!- FUNCTION:", "CC   -!- CATALYTIC ACTIVITY:", "CC   -!- COFACTOR:", "DR   PANTHER;", "DR   Pfam;", "KW   ", "FT   DOMAIN"):
        line = optional_first_line(path, marker)
        if line and "Reference proteome" not in line:
            add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    for line in prefixed_lines(path, "DR   InterPro;", 6):
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


def new_annotation(gene: str, term_id: str) -> dict:
    return {
        "term": TERM[term_id],
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": "enables",
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
    data["suggested_questions"] = [{"question": suggested_question(gene), "experts": []}]
    data["suggested_experiments"] = [
        {
            "experiment_type": "substrate and phenotype validation",
            "description": f"Assay purified {gene} against DNA and RNA nuclease substrates and test deletion/overexpression phenotypes only in the relevant toxin, bacteriocin, or DNA-repair context.",
        }
    ]
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def suggested_question(gene: str) -> str:
    return {
        "PP_1306": "Is PP_1306 an active pyocin/colicin-like DNase toxin and what is its immunity or export context?",
        "PP_1554": "What nucleic-acid substrate is cleaved by the PP_1554 VRR-NUC domain?",
        "PP_2276": "Is PP_2276 a mobile-element/phage nuclease or does it contribute to host DNA processing?",
        "tatD": "Does KT2440 TatD act primarily as DNase, RNase, or broad metal-dependent nuclease?",
        "endX": "Is EndX secreted and active as an extracellular DNase in biofilm or eDNA turnover?",
        "PP_2838": "Does PP_2838 have FAN1-like DNA cross-link repair activity in KT2440?",
        "yoeB": "What antitoxin and mRNA targets define the KT2440 YoeB toxin module?",
        "endA": "Is EndA secreted/periplasmic and what DNA substrates does it cleave?",
        "PP_3883": "Is PP_3883 a functional HNH nuclease or a mobile-element remnant?",
        "PP_3890": "What nucleic-acid substrate is cleaved by the PP_3890 VRR-NUC domain?",
        "PP_4247": "Does PP_4247 act on RNA substrates as predicted by ERI-1/RNase-H-like family evidence?",
        "yajD": "Is YajD a functional HNH nuclease and does it have a toxin/mobile-element role?",
        "PP_5086": "Which DNA substrate is cleaved by the SNase-domain PP_5086 protein?",
        "PP_5295": "Is PP_5295 a YicC-family RNA endonuclease and what process uses it in KT2440?",
    }[gene]


def write_notes(gene: str) -> None:
    info = GENE_INFO[gene]
    path = GENE_ROOT / gene / f"{gene}-notes.md"
    evidence = standard_support(gene, info["core"][0].get("support_term") if info["core"] else None)
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass nuclease/DNase/toxin side-node split curation.",
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
    lines.extend(["", "Decision: route as nuclease/toxin/RNA side-node context rather than as a single DNA repair pathway.", ""])
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
        "id": "MODULE:nuclease_dnase_boundary",
        "title": "Nuclease, DNase, RNA-toxin, and phosphodiesterase side-node boundary",
        "description": "Boundary module for PSEPK DNA-bucket nuclease side nodes. The set mixes DNA nucleases, RNA/toxin nucleases, pyocin/mobile-element nucleases, and broad phosphodiesterase candidates; it should not be treated as one coherent DNA repair pathway.",
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_TSV}",
                "title": "PSEPK nuclease/DNase/toxin side-node split table",
                "statement": "The split table records the 14 nuclease-side candidates pulled from the broad DNA replication/repair/recombination functional bucket.",
            }
        ],
        "notes": "First-pass boundary. DNA nuclease, RNA nuclease/toxin, pyocin/mobile-element nuclease, and broad phosphodiesterase roles remain separated.",
        "module": {
            "id": "nuclease_dnase_boundary",
            "label": "Nuclease/DNase/toxin side-node boundary",
            "module_type": "MOLECULAR_FUNCTION",
            "concepts": [
                {"preferred_term": TERM["GO:0004518"]["label"], "term": TERM["GO:0004518"], "description": "Broad nuclease activity."},
                {"preferred_term": TERM["GO:0004519"]["label"], "term": TERM["GO:0004519"], "description": "Endonuclease/toxin nuclease activity."},
                {"preferred_term": TERM["GO:0004521"]["label"], "term": TERM["GO:0004521"], "description": "RNA endonuclease side-node activity."},
                {"preferred_term": TERM["GO:0004527"]["label"], "term": TERM["GO:0004527"], "description": "Exonuclease side-node activity."},
            ],
            "parts": [
                {
                    "order": 1,
                    "role": "DNA nuclease and exonuclease candidates",
                    "node": {
                        "id": "dna_nuclease_candidates",
                        "label": "DNA nuclease and exonuclease candidates",
                        "module_type": "MOLECULAR_FUNCTION",
                        "annotons": [
                            annoton("endx_dnase_i", "endX", "GO:0004530", "EndA/NucM-family extracellular DNase candidate."),
                            annoton("enda_endonuclease_i", "endA", "GO:0004519", "EndA/NucM-family endonuclease candidate."),
                            annoton("tatd_exonuclease", "tatD", "GO:0004527", "TatD-family metal-dependent nuclease/exonuclease candidate."),
                            annoton("pp2276_fen_exonuclease", "PP_2276", "GO:0008409", "FEN-like phage exonuclease boundary member.", ["GO:0033567"]),
                            annoton("pp5086_snase_endonuclease", "PP_5086", "GO:0004519", "SNase-domain endonuclease candidate."),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "HNH, VRR-NUC, and pyocin/toxin nuclease candidates",
                    "node": {
                        "id": "hnh_vrr_pyocin_nuclease_candidates",
                        "label": "HNH/VRR-NUC/pyocin nuclease candidates",
                        "module_type": "MOLECULAR_FUNCTION",
                        "annotons": [
                            annoton("pp1306_pyocin_hnh", "PP_1306", "GO:0004519", "Pyocin/colicin HNH nuclease-toxin candidate."),
                            annoton("pp3883_hnh_yajd_like", "PP_3883", "GO:0004519", "HNH nuclease YajD-like candidate."),
                            annoton("yajd_hnh", "yajD", "GO:0004519", "YajD HNH nuclease candidate."),
                            annoton("pp1554_vrr_nuc", "PP_1554", "GO:0004518", "VRR-NUC broad nuclease candidate."),
                            annoton("pp3890_vrr_nuc", "PP_3890", "GO:0004518", "Second VRR-NUC broad nuclease candidate."),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "RNA/toxin and phosphodiesterase side nodes",
                    "node": {
                        "id": "rna_toxin_phosphodiesterase_side_nodes",
                        "label": "RNA/toxin and phosphodiesterase side nodes",
                        "module_type": "MOLECULAR_FUNCTION",
                        "annotons": [
                            annoton("yoeb_mrna_interferase", "yoeB", "GO:0004519", "YoeB mRNA-interferase toxin candidate.", ["GO:0006401"]),
                            annoton("pp4247_rna_exonuclease", "PP_4247", "GO:0000175", "ERI-1-like 3'-5' RNA exonuclease candidate."),
                            annoton("pp5295_yicc_rna_endonuclease", "PP_5295", "GO:0004521", "YicC-family RNA endonuclease candidate."),
                            annoton("pp2838_fan1_phosphodiesterase", "PP_2838", "GO:0004528", "FAN1/VRR-NUC phosphodiesterase I candidate.", ["GO:0036297"]),
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
