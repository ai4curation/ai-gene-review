#!/usr/bin/env python3
"""First-pass curation for the PSEPK envelope peptidase/inhibitor split."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_DIR = ROOT / "genes" / "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


TERM = {
    "GO:0004175": {"id": "GO:0004175", "label": "endopeptidase activity"},
    "GO:0004180": {"id": "GO:0004180", "label": "carboxypeptidase activity"},
    "GO:0004181": {"id": "GO:0004181", "label": "metallocarboxypeptidase activity"},
    "GO:0004222": {"id": "GO:0004222", "label": "metalloendopeptidase activity"},
    "GO:0004252": {"id": "GO:0004252", "label": "serine-type endopeptidase activity"},
    "GO:0004866": {"id": "GO:0004866", "label": "endopeptidase inhibitor activity"},
    "GO:0004867": {"id": "GO:0004867", "label": "serine-type endopeptidase inhibitor activity"},
    "GO:0004869": {"id": "GO:0004869", "label": "cysteine-type endopeptidase inhibitor activity"},
    "GO:0005576": {"id": "GO:0005576", "label": "extracellular region"},
    "GO:0006508": {"id": "GO:0006508", "label": "proteolysis"},
    "GO:0007165": {"id": "GO:0007165", "label": "signal transduction"},
    "GO:0008234": {"id": "GO:0008234", "label": "cysteine-type peptidase activity"},
    "GO:0008236": {"id": "GO:0008236", "label": "serine-type peptidase activity"},
    "GO:0008270": {"id": "GO:0008270", "label": "zinc ion binding"},
    "GO:0009254": {"id": "GO:0009254", "label": "peptidoglycan turnover"},
    "GO:0030288": {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"},
    "GO:0030313": {"id": "GO:0030313", "label": "cell envelope"},
    "GO:0042597": {"id": "GO:0042597", "label": "periplasmic space"},
    "GO:0042834": {"id": "GO:0042834", "label": "peptidoglycan binding"},
}


DESCRIPTIONS = {
    "PP_0435": "PP_0435 is a cell-envelope M23/M37-family metalloendopeptidase candidate with LysM/peptidoglycan-binding context, consistent with peptidoglycan turnover.",
    "yfhM": "yfhM encodes a secreted bacterial alpha-2-macroglobulin-family endopeptidase inhibitor predicted to protect the cell from external peptidases.",
    "PP_1026": "PP_1026 is a signal-peptide-bearing M23/M37-family metalloendopeptidase candidate.",
    "PP_1442": "PP_1442 is a predicted exported chagasin/I42-family cysteine endopeptidase inhibitor.",
    "PP_1669": "PP_1669 is a signal-peptide-bearing NlpC/P60-family cysteine-type peptidase candidate.",
    "PP_1670": "PP_1670 is a predicted lipoprotein NlpC/P60-family cysteine-type peptidase candidate.",
    "prc": "prc encodes a periplasmic tail-specific S41A-family serine peptidase involved in envelope proteolysis.",
    "PP_2108": "PP_2108 is a low-information Peptidase M15A C-terminal domain-containing protein; current evidence does not establish an autonomous peptidase function.",
    "PP_2364": "PP_2364 is an M14-family metallocarboxypeptidase candidate with zinc-binding and proteolysis annotations.",
    "eco": "eco encodes ecotin, a periplasmic homodimeric inhibitor of family S1 serine proteases.",
    "PP_4799": "PP_4799 is a predicted exported muramoyltetrapeptide carboxypeptidase/peptidase S66-family protein.",
    "PP_5057": "PP_5057 is a signal-peptide-bearing M23/M37-family metalloendopeptidase candidate with EnvC-like murein-hydrolase-activator family context.",
    "ctpA": "ctpA encodes a periplasmic C-terminal-processing S41A-family serine endopeptidase.",
    "PP_5092": "PP_5092 is a predicted exported NlpC/P60-family cysteine-type peptidase candidate.",
    "PP_5323": "PP_5323 is a signal-peptide-bearing M23/M37-family metalloendopeptidase candidate with DUF4124 context.",
    "PP_5729": "PP_5729 is a low-information Peptidase inhibitor I78-family protein; current evidence is insufficient to assign a precise GO molecular function.",
}


def read_lines(path: Path) -> list[str]:
    return path.read_text().splitlines()


def optional_first_line(path: Path, contains: str) -> str | None:
    for line in read_lines(path):
        if contains in line:
            return line.rstrip()
    return None


def first_line(path: Path, contains: str) -> str:
    line = optional_first_line(path, contains)
    if line is None:
        raise ValueError(f"Could not find {contains!r} in {path}")
    return line


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, supporting_text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": supporting_text}


def add_unique(items: list[dict], item: dict) -> None:
    if item not in items:
        items.append(item)


def accession(gene: str) -> str:
    return first_line(GENE_DIR / gene / f"{gene}-uniprot.txt", "AC   ").split()[1].rstrip(";")


def goa_support(gene: str, term_id: str) -> list[dict[str, str]]:
    path = GENE_DIR / gene / f"{gene}-goa.tsv"
    if not path.exists():
        return []
    refs = []
    for line in read_lines(path):
        if term_id in line:
            refs.append(support(file_id(gene, "goa.tsv"), line.rstrip()))
    return refs


def uniprot_support(gene: str, *patterns: str) -> list[dict[str, str]]:
    path = GENE_DIR / gene / f"{gene}-uniprot.txt"
    refs = []
    for pattern in patterns:
        line = optional_first_line(path, pattern)
        if line:
            refs.append(support(file_id(gene, "uniprot.txt"), line))
    return refs


def asta_support(gene: str, *patterns: str) -> list[dict[str, str]]:
    path = GENE_DIR / gene / f"{gene}-deep-research-asta.md"
    if not path.exists():
        return []
    refs = []
    for pattern in patterns:
        line = optional_first_line(path, pattern)
        if line:
            refs.append(support(file_id(gene, "deep-research-asta.md"), line))
    return refs


def standard_support(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    refs: list[dict[str, str]] = []
    if term_id:
        refs.extend(goa_support(gene, term_id))
        refs.extend(uniprot_support(gene, f"DR   GO; {term_id};"))
    refs.extend(uniprot_support(
        gene,
        "DE   RecName:",
        "DE   SubName:",
        "CC   -!- FUNCTION:",
        "CC   -!- SUBCELLULAR LOCATION:",
        "CC   -!- SIMILARITY:",
        "DR   PANTHER;",
        "DR   Pfam;",
        "DR   InterPro;",
        "FT   SIGNAL",
        "FT   LIPID",
    ))
    refs.extend(asta_support(
        gene,
        "  uniprot_accession:",
        "  protein_description:",
        "  protein_family:",
        "  protein_domains:",
    ))
    out: list[dict[str, str]] = []
    for ref in refs:
        add_unique(out, ref)
    return out


def load(gene: str) -> dict:
    return yaml.safe_load((GENE_DIR / gene / f"{gene}-ai-review.yaml").read_text())


def write(gene: str, data: dict) -> None:
    path = GENE_DIR / gene / f"{gene}-ai-review.yaml"
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120))


def ensure_references(data: dict, gene: str) -> None:
    refs = data.setdefault("references", [])
    existing = {r["id"] for r in refs}
    entries = [
        {
            "id": file_id(gene, "goa.tsv"),
            "title": f"QuickGO GOA annotations for {gene} ({accession(gene)})",
            "findings": [],
        },
        {
            "id": file_id(gene, "uniprot.txt"),
            "title": f"UniProtKB entry for {gene} ({accession(gene)})",
            "findings": [],
        },
        {
            "id": file_id(gene, "deep-research-asta.md"),
            "title": f"Asta retrieval report for {gene} ({accession(gene)})",
            "findings": [],
        },
    ]
    for entry in entries:
        if entry["id"] not in existing and (GENE_DIR / gene / entry["id"].split("/")[-1]).exists():
            refs.append(entry)
            existing.add(entry["id"])


def finish_common(data: dict, gene: str) -> None:
    data["status"] = "DRAFT"
    data["description"] = DESCRIPTIONS[gene]
    data.setdefault("proposed_new_terms", [])
    data.setdefault("suggested_questions", [])
    data.setdefault("suggested_experiments", [])


def set_review(data: dict, gene: str, term_id: str, action: str, summary: str) -> None:
    matched = False
    for ann in data.get("existing_annotations") or []:
        if ann.get("term", {}).get("id") == term_id:
            ann["review"] = {
                "summary": summary,
                "action": action,
                "supported_by": standard_support(gene, term_id),
            }
            matched = True
    if not matched:
        raise ValueError(f"{gene} lacks expected existing annotation {term_id}")


def ensure_new_annotation(data: dict, gene: str, term_id: str, qualifier: str, summary: str, reason: str) -> None:
    annotations = data.setdefault("existing_annotations", [])
    if any(ann.get("term", {}).get("id") == term_id for ann in annotations):
        return
    annotations.append({
        "term": TERM[term_id],
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": standard_support(gene, term_id),
        },
        "qualifier": qualifier,
    })


def core(
    description: str,
    mf: str,
    processes: list[str] | None = None,
    locations: list[str] | None = None,
    supported_by: list[dict[str, str]] | None = None,
) -> dict:
    item = {
        "description": description,
        "molecular_function": TERM[mf],
        "supported_by": supported_by or [],
    }
    if processes:
        item["directly_involved_in"] = [TERM[p] for p in processes]
    if locations:
        item["locations"] = [TERM[l] for l in locations]
    return item


def curate_m23(gene: str) -> None:
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    if any(ann.get("term", {}).get("id") == "GO:0004175" for ann in data.get("existing_annotations") or []):
        set_review(data, gene, "GO:0004175", "MARK_AS_OVER_ANNOTATED", "Broad endopeptidase activity is less informative than the metalloendopeptidase/M23-family assignment.")
    set_review(data, gene, "GO:0004222", "ACCEPT", "Metalloendopeptidase activity is supported by M23/M37 family, M23 domain, and TreeGrafter evidence.")
    if any(ann.get("term", {}).get("id") == "GO:0009254" for ann in data.get("existing_annotations") or []):
        set_review(data, gene, "GO:0009254", "ACCEPT", "Peptidoglycan turnover is appropriate for the cell-wall M23/LysM-domain peptidase context.")
    if any(ann.get("term", {}).get("id") == "GO:0030313" for ann in data.get("existing_annotations") or []):
        set_review(data, gene, "GO:0030313", "ACCEPT", "Cell-envelope localization is consistent with UniProt localization and cell-wall domains.")
    if any(ann.get("term", {}).get("id") == "GO:0042834" for ann in data.get("existing_annotations") or []):
        set_review(data, gene, "GO:0042834", "ACCEPT", "Peptidoglycan binding is supported by LysM/peptidoglycan-binding domain evidence.")
    processes = ["GO:0009254"] if any(ann.get("term", {}).get("id") == "GO:0009254" for ann in data.get("existing_annotations") or []) else None
    locations = ["GO:0030313"] if any(ann.get("term", {}).get("id") == "GO:0030313" for ann in data.get("existing_annotations") or []) else None
    data["core_functions"] = [
        core("M23/M37-family metalloendopeptidase activity in envelope or cell-wall context.", "GO:0004222", processes, locations, standard_support(gene, "GO:0004222")),
    ]
    if any(ann.get("term", {}).get("id") == "GO:0042834" for ann in data.get("existing_annotations") or []):
        data["core_functions"].append(core("Peptidoglycan binding by LysM/cell-wall-associated domains.", "GO:0042834", None, locations, standard_support(gene, "GO:0042834")))
    data["suggested_questions"] = [{"question": f"What peptidoglycan substrate and partner pathway does {gene} act on in KT2440?"}]
    write(gene, data)


def curate_nlpc(gene: str) -> None:
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0008234", "ACCEPT", "NlpC/P60-domain and Peptidase C40-family evidence support cysteine-type peptidase activity.")
    data["core_functions"] = [
        core("NlpC/P60-family cysteine-type peptidase activity in exported/envelope context.", "GO:0008234", None, None, standard_support(gene, "GO:0008234")),
    ]
    data["suggested_questions"] = [{"question": f"Does {gene} cleave peptidoglycan or another envelope substrate in KT2440?"}]
    write(gene, data)


def curate_tail_specific(gene: str) -> None:
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    if any(ann.get("term", {}).get("id") == "GO:0004175" for ann in data.get("existing_annotations") or []):
        set_review(data, gene, "GO:0004175", "MARK_AS_OVER_ANNOTATED", "Broad endopeptidase activity is less informative than the S41A serine peptidase assignment.")
    if any(ann.get("term", {}).get("id") == "GO:0004252" for ann in data.get("existing_annotations") or []):
        set_review(data, gene, "GO:0004252", "ACCEPT", "Serine-type endopeptidase activity is supported by C-terminal-processing protease EC/domain evidence.")
        mf = "GO:0004252"
    else:
        set_review(data, gene, "GO:0008236", "ACCEPT", "Serine-type peptidase activity is supported by S41A tail-specific protease family evidence.")
        mf = "GO:0008236"
    if any(ann.get("term", {}).get("id") == "GO:0008236" for ann in data.get("existing_annotations") or []) and mf != "GO:0008236":
        set_review(data, gene, "GO:0008236", "MARK_AS_OVER_ANNOTATED", "Correct broad class but less informative than serine-type endopeptidase activity.")
    set_review(data, gene, "GO:0006508", "ACCEPT", "Proteolysis is appropriate process context for this tail-specific/C-terminal-processing peptidase.")
    set_review(data, gene, "GO:0007165", "MARK_AS_OVER_ANNOTATED", "Signal transduction is a broad family-transfer process and is not the core molecular role.")
    set_review(data, gene, "GO:0030288", "ACCEPT", "Outer membrane-bounded periplasmic-space localization is consistent with the signal peptide and TreeGrafter localization.")
    data["core_functions"] = [
        core("Periplasmic S41A-family serine peptidase activity.", mf, ["GO:0006508"], ["GO:0030288"], standard_support(gene, mf)),
    ]
    data["suggested_questions"] = [{"question": f"What physiological C-terminal peptide substrate is processed by {gene} in KT2440?"}]
    write(gene, data)


def curate_yfhM() -> None:
    gene = "yfhM"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0004866", "ACCEPT", "Alpha-2-macroglobulin-family proteins are endopeptidase inhibitors and UniProt states a protective anti-peptidase role.")
    set_review(data, gene, "GO:0005576", "ACCEPT", "Extracellular-region localization is consistent with signal peptide/exported bacterial alpha-2-macroglobulin context.")
    data["core_functions"] = [
        core("Secreted alpha-2-macroglobulin-family endopeptidase inhibitor activity.", "GO:0004866", None, ["GO:0005576"], standard_support(gene, "GO:0004866")),
    ]
    data["suggested_questions"] = [{"question": "Which external or host/environmental peptidases are trapped by KT2440 YfhM?"}]
    write(gene, data)


def curate_chagasin() -> None:
    gene = "PP_1442"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    ensure_new_annotation(data, gene, "GO:0004869", "enables", "Chagasin/I42-family domain evidence supports cysteine-type endopeptidase inhibitor activity.", "QuickGO returned no GOA rows, but UniProt carries a GO cysteine-type endopeptidase inhibitor annotation.")
    data["core_functions"] = [
        core("Chagasin/I42-family cysteine endopeptidase inhibitor activity.", "GO:0004869", None, None, standard_support(gene, "GO:0004869")),
    ]
    data["suggested_questions"] = [{"question": "Which cysteine peptidase target is inhibited by PP_1442 in KT2440?"}]
    write(gene, data)


def curate_m14() -> None:
    gene = "PP_2364"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0004181", "ACCEPT", "M14-family and cytosolic-carboxypeptidase domain evidence support metallocarboxypeptidase activity.")
    set_review(data, gene, "GO:0006508", "ACCEPT", "Proteolysis is appropriate process context for the metallocarboxypeptidase activity.")
    set_review(data, gene, "GO:0008270", "ACCEPT", "Zinc ion binding is consistent with the M14 metallocarboxypeptidase active-site class.")
    data["core_functions"] = [
        core("M14-family metallocarboxypeptidase activity.", "GO:0004181", ["GO:0006508"], None, standard_support(gene, "GO:0004181")),
    ]
    data["suggested_questions"] = [{"question": "What peptide or cell-envelope substrate is processed by PP_2364 in KT2440?"}]
    write(gene, data)


def curate_pp4799() -> None:
    gene = "PP_4799"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    ensure_new_annotation(data, gene, "GO:0004180", "enables", "Muramoyltetrapeptide carboxypeptidase product name and Peptidase S66-family evidence support carboxypeptidase activity.", "QuickGO returned no GOA rows, but UniProt carries carboxypeptidase and Peptidase S66 evidence.")
    ensure_new_annotation(data, gene, "GO:0008236", "enables", "Peptidase S66-family evidence supports serine-type peptidase activity.", "QuickGO returned no GOA rows, but UniProt carries a serine-type peptidase annotation.")
    ensure_new_annotation(data, gene, "GO:0006508", "involved_in", "Proteolysis is the conservative process context for the muramoyltetrapeptide carboxypeptidase.", "QuickGO returned no GOA rows, but UniProt carries a proteolysis process annotation.")
    data["core_functions"] = [
        core("Muramoyltetrapeptide carboxypeptidase activity.", "GO:0004180", ["GO:0006508"], None, standard_support(gene, "GO:0004180")),
    ]
    data["suggested_questions"] = [{"question": "Does PP_4799 act in peptidoglycan recycling/remodeling and what muropeptide substrate does it prefer?"}]
    write(gene, data)


def curate_low_info(gene: str, question: str) -> None:
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    data["core_functions"] = []
    data["suggested_questions"] = [{"question": question}]
    write(gene, data)


def update_eco() -> None:
    gene = "eco"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    # Preserve prior Falcon-backed review decisions; add Asta provenance to this split.
    for ann in data.get("existing_annotations") or []:
        if ann.get("term", {}).get("id") == "GO:0004867":
            ann.setdefault("review", {}).setdefault("supported_by", [])
            for ref in asta_support(gene, "  protein_description:", "  protein_family:", "  protein_domains:"):
                add_unique(ann["review"]["supported_by"], ref)
        if ann.get("term", {}).get("id") == "GO:0042597":
            ann.setdefault("review", {}).setdefault("supported_by", [])
            for ref in asta_support(gene, "  protein_description:", "  protein_domains:"):
                add_unique(ann["review"]["supported_by"], ref)
    for cf in data.get("core_functions") or []:
        cf.setdefault("supported_by", [])
        for ref in asta_support(gene, "  protein_description:", "  protein_family:", "  protein_domains:"):
            add_unique(cf["supported_by"], ref)
    write(gene, data)


def main() -> None:
    curate_m23("PP_0435")
    curate_yfhM()
    curate_m23("PP_1026")
    curate_chagasin()
    curate_nlpc("PP_1669")
    curate_nlpc("PP_1670")
    curate_tail_specific("prc")
    curate_low_info("PP_2108", "Does PP_2108 encode an active M15-family peptidase or only a non-catalytic M15A C-terminal-domain protein?")
    curate_m14()
    update_eco()
    curate_pp4799()
    curate_m23("PP_5057")
    curate_tail_specific("ctpA")
    curate_nlpc("PP_5092")
    curate_m23("PP_5323")
    curate_low_info("PP_5729", "Does PP_5729 have experimentally detectable peptidase-inhibitor activity, and what peptidase family does it inhibit?")
    print("Curated cell-wall/envelope peptidase inhibitor split")


if __name__ == "__main__":
    main()
