#!/usr/bin/env python3
"""First-pass curation for the PSEPK peptide-processing/aminopeptidase split."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_DIR = ROOT / "genes" / "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


TERM = {
    "GO:0004177": {"id": "GO:0004177", "label": "aminopeptidase activity"},
    "GO:0004222": {"id": "GO:0004222", "label": "metalloendopeptidase activity"},
    "GO:0004239": {"id": "GO:0004239", "label": "initiator methionyl aminopeptidase activity"},
    "GO:0005506": {"id": "GO:0005506", "label": "iron ion binding"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0005829": {"id": "GO:0005829", "label": "cytosol"},
    "GO:0006508": {"id": "GO:0006508", "label": "proteolysis"},
    "GO:0006518": {"id": "GO:0006518", "label": "peptide metabolic process"},
    "GO:0006526": {"id": "GO:0006526", "label": "L-arginine biosynthetic process"},
    "GO:0008233": {"id": "GO:0008233", "label": "peptidase activity"},
    "GO:0008237": {"id": "GO:0008237", "label": "metallopeptidase activity"},
    "GO:0008270": {"id": "GO:0008270", "label": "zinc ion binding"},
    "GO:0008777": {"id": "GO:0008777", "label": "acetylornithine deacetylase activity"},
    "GO:0016787": {"id": "GO:0016787", "label": "hydrolase activity"},
    "GO:0016805": {"id": "GO:0016805", "label": "dipeptidase activity"},
    "GO:0030145": {"id": "GO:0030145", "label": "manganese ion binding"},
    "GO:0046872": {"id": "GO:0046872", "label": "metal ion binding"},
    "GO:0050118": {"id": "GO:0050118", "label": "N-acetyldiaminopimelate deacetylase activity"},
    "GO:0070006": {"id": "GO:0070006", "label": "metalloaminopeptidase activity"},
}


DESCRIPTIONS = {
    "prlC": "prlC encodes a cytosolic M3-family oligopeptidase A metallopeptidase involved in peptide turnover.",
    "PP_0203": "PP_0203 encodes a predicted M20A-family metal-dependent dipeptidase/acylase with acetylornithine deacetylase family-transfer evidence.",
    "mtfA": "mtfA encodes an MtfA/M90-family cytosolic metallopeptidase with aminopeptidase activity annotations.",
    "map": "map encodes methionine aminopeptidase, which removes initiator methionine from nascent proteins.",
    "apeB": "apeB encodes a cytoplasmic M18-family metal-dependent aminopeptidase.",
    "PP_1748": "PP_1748 encodes a predicted M42-family metal-dependent aminopeptidase associated with osmoprotectant NAGGN system context.",
    "yegQ": "yegQ encodes a cytosolic U32-family peptidase candidate with limited substrate evidence.",
    "PP_2704": "PP_2704 encodes an M20/M25/M40-family metal-dependent deacetylase candidate annotated as N-acetyldiaminopimelate deacetylase.",
    "ydcP": "ydcP encodes a U32-family peptidase-domain protein with only generic hydrolase/peptidase evidence.",
    "PP_4752": "PP_4752 encodes an M24B-family Xaa-Pro aminopeptidase candidate.",
    "PP_4949": "PP_4949 encodes a cytosolic TldD/PmbA/U62-family metallopeptidase candidate.",
    "pepP": "pepP encodes a cytosolic M24B-family Xaa-Pro aminopeptidase/aminopeptidase P.",
    "PP_5629": "PP_5629 encodes a DJ-1/PfpI-domain intracellular protease/amidase candidate with generic peptidase evidence.",
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
    refs = []
    if path.exists():
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
    refs = []
    if path.exists():
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
        "CC   -!- CATALYTIC ACTIVITY:",
        "CC   -!- COFACTOR:",
        "CC   -!- SUBCELLULAR LOCATION:",
        "CC   -!- SIMILARITY:",
        "DR   PANTHER;",
        "DR   Pfam;",
        "DR   InterPro;",
        "FT   ACT_SITE",
        "FT   BINDING",
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
    (GENE_DIR / gene / f"{gene}-ai-review.yaml").write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120)
    )


def ensure_references(data: dict, gene: str) -> None:
    refs = data.setdefault("references", [])
    existing = {r["id"] for r in refs}
    for entry in [
        {"id": file_id(gene, "goa.tsv"), "title": f"QuickGO GOA annotations for {gene} ({accession(gene)})", "findings": []},
        {"id": file_id(gene, "uniprot.txt"), "title": f"UniProtKB entry for {gene} ({accession(gene)})", "findings": []},
        {"id": file_id(gene, "deep-research-asta.md"), "title": f"Asta retrieval report for {gene} ({accession(gene)})", "findings": []},
    ]:
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
            ann["review"] = {"summary": summary, "action": action, "supported_by": standard_support(gene, term_id)}
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


def has_term(data: dict, term_id: str) -> bool:
    return any(ann.get("term", {}).get("id") == term_id for ann in data.get("existing_annotations") or [])


def remove_term(data: dict, term_id: str) -> None:
    data["existing_annotations"] = [
        ann for ann in data.get("existing_annotations", []) if ann.get("term", {}).get("id") != term_id
    ]


def core(description: str, mf: str, processes: list[str] | None = None, locations: list[str] | None = None, supported_by: list[dict[str, str]] | None = None) -> dict:
    item = {"description": description, "molecular_function": TERM[mf], "supported_by": supported_by or []}
    if processes:
        item["directly_involved_in"] = [TERM[p] for p in processes]
    if locations:
        item["locations"] = [TERM[l] for l in locations]
    return item


def curate_prlC() -> None:
    gene = "prlC"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0004222", "ACCEPT", "Oligopeptidase A EC 3.4.24.70 and M3-family evidence support metalloendopeptidase activity.")
    set_review(data, gene, "GO:0005829", "ACCEPT", "Cytosol is consistent with soluble peptide-turnover context.")
    set_review(data, gene, "GO:0006508", "ACCEPT", "Proteolysis is appropriate process context for oligopeptidase activity.")
    set_review(data, gene, "GO:0006518", "ACCEPT", "Peptide metabolic process is appropriate for oligopeptidase A peptide turnover.")
    set_review(data, gene, "GO:0008233", "MARK_AS_OVER_ANNOTATED", "Generic peptidase activity is less informative than metalloendopeptidase activity.")
    set_review(data, gene, "GO:0008237", "MARK_AS_OVER_ANNOTATED", "Generic metallopeptidase activity is less informative than metalloendopeptidase activity.")
    set_review(data, gene, "GO:0046872", "KEEP_AS_NON_CORE", "Metal ion binding is cofactor context for M3 metalloendopeptidase activity.")
    data["core_functions"] = [
        core("Cytosolic M3-family oligopeptidase/metalloendopeptidase activity.", "GO:0004222", ["GO:0006508", "GO:0006518"], ["GO:0005829"], standard_support(gene, "GO:0004222")),
    ]
    write(gene, data)


def curate_pp0203() -> None:
    gene = "PP_0203"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0006526", "ACCEPT", "L-arginine biosynthetic process is supported by the acetylornithine deacetylase family-transfer annotation.")
    set_review(data, gene, "GO:0008270", "KEEP_AS_NON_CORE", "Zinc binding is cofactor context for the M20A metal-dependent hydrolase.")
    set_review(data, gene, "GO:0008777", "ACCEPT", "Acetylornithine deacetylase activity is the specific TreeGrafter-transferred M20A-family call.")
    set_review(data, gene, "GO:0016787", "MARK_AS_OVER_ANNOTATED", "Generic hydrolase activity is less informative than dipeptidase/deacetylase activity.")
    set_review(data, gene, "GO:0016805", "ACCEPT", "Dipeptidase activity is consistent with the product name and M20A peptidase family.")
    data["core_functions"] = [
        core("M20A-family acetylornithine deacetylase/acylase activity.", "GO:0008777", ["GO:0006526"], None, standard_support(gene, "GO:0008777")),
        core("Metal-dependent dipeptidase activity.", "GO:0016805", None, None, standard_support(gene, "GO:0016805")),
    ]
    write(gene, data)


def curate_simple_aminopeptidase(gene: str, location: str | None = None) -> None:
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0004177", "ACCEPT", "Aminopeptidase activity is supported by peptidase-family/domain evidence.")
    if has_term(data, "GO:0008237"):
        set_review(data, gene, "GO:0008237", "KEEP_AS_NON_CORE", "Metallopeptidase activity is correct class context but less specific than aminopeptidase activity.")
    if has_term(data, "GO:0046872"):
        set_review(data, gene, "GO:0046872", "KEEP_AS_NON_CORE", "Metal ion binding is cofactor context for aminopeptidase activity.")
    if location:
        set_review(data, gene, location, "ACCEPT", "Soluble bacterial localization is consistent with the peptide-processing enzyme context.")
    locations = [location] if location else None
    data["core_functions"] = [
        core("Metal-dependent aminopeptidase activity in peptide turnover context.", "GO:0004177", None, locations, standard_support(gene, "GO:0004177")),
    ]
    write(gene, data)


def curate_map() -> None:
    gene = "map"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0004239", "ACCEPT", "Methionine aminopeptidase removes N-terminal methionine from nascent proteins.")
    set_review(data, gene, "GO:0005506", "KEEP_AS_NON_CORE", "Iron binding is possible cofactor context, but the key role is MetAP activity.")
    set_review(data, gene, "GO:0005829", "ACCEPT", "Cytosolic localization is appropriate for nascent-protein processing.")
    set_review(data, gene, "GO:0006508", "ACCEPT", "Proteolysis is appropriate process context for initiator-methionine removal.")
    set_review(data, gene, "GO:0046872", "KEEP_AS_NON_CORE", "Metal ion binding is cofactor context for the metalloaminopeptidase.")
    set_review(data, gene, "GO:0070006", "MARK_AS_OVER_ANNOTATED", "Metalloaminopeptidase activity is correct but broader than initiator methionyl aminopeptidase activity.")
    data["core_functions"] = [
        core("Cytosolic initiator methionyl aminopeptidase activity for nascent-protein N-terminal processing.", "GO:0004239", ["GO:0006508"], ["GO:0005829"], standard_support(gene, "GO:0004239")),
    ]
    write(gene, data)


def curate_apeB() -> None:
    gene = "apeB"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0004177", "ACCEPT", "M18-family/HAMAP evidence supports aminopeptidase activity.")
    set_review(data, gene, "GO:0005737", "ACCEPT", "Cytoplasm is appropriate for this soluble aminopeptidase.")
    set_review(data, gene, "GO:0006508", "ACCEPT", "Proteolysis is appropriate process context.")
    set_review(data, gene, "GO:0008237", "KEEP_AS_NON_CORE", "Metallopeptidase activity is correct class context but less specific than aminopeptidase activity.")
    set_review(data, gene, "GO:0008270", "KEEP_AS_NON_CORE", "Zinc binding is cofactor context.")
    data["core_functions"] = [
        core("Cytoplasmic M18-family aminopeptidase activity.", "GO:0004177", ["GO:0006508"], ["GO:0005737"], standard_support(gene, "GO:0004177")),
    ]
    write(gene, data)


def curate_yegQ() -> None:
    gene = "yegQ"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0005829", "ACCEPT", "Cytosolic localization is consistent with the soluble U32-family protein.")
    ensure_new_annotation(data, gene, "GO:0008233", "enables", "U32-family and UniProt keyword evidence support generic peptidase activity, but no substrate specificity is available.", "GOA only returned cytosolic localization despite UniProt carrying peptidase/proteolysis evidence.")
    ensure_new_annotation(data, gene, "GO:0006508", "involved_in", "Proteolysis is conservative process context for the U32-family peptidase candidate.", "GOA only returned localization despite UniProt carrying proteolysis evidence.")
    data["core_functions"] = [
        core("Cytosolic U32-family generic peptidase activity.", "GO:0008233", ["GO:0006508"], ["GO:0005829"], standard_support(gene, "GO:0008233")),
    ]
    data["suggested_questions"] = [{"question": "What peptide or RNA-associated substrate is processed by yegQ in KT2440?"}]
    write(gene, data)


def curate_pp2704() -> None:
    gene = "PP_2704"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0016787", "MARK_AS_OVER_ANNOTATED", "Generic hydrolase activity is less informative than N-acetyldiaminopimelate deacetylase activity.")
    set_review(data, gene, "GO:0050118", "ACCEPT", "N-acetyldiaminopimelate deacetylase activity is the specific ARBA-transferred M20-family call.")
    remove_term(data, "GO:0019877")
    data["core_functions"] = [
        core("M20-family N-acetyldiaminopimelate deacetylase activity.", "GO:0050118", None, None, standard_support(gene, "GO:0050118")),
    ]
    write(gene, data)


def curate_ydcP() -> None:
    gene = "ydcP"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    ensure_new_annotation(data, gene, "GO:0008233", "enables", "U32-family peptidase domains and EC 3.4.-.- support generic peptidase activity, but no substrate-specific term.", "QuickGO returned no GOA rows for ydcP.")
    if has_term(data, "GO:0016787"):
        set_review(data, gene, "GO:0016787", "MARK_AS_OVER_ANNOTATED", "Generic hydrolase activity is less informative than peptidase-domain evidence.")
    data["core_functions"] = [
        core("U32-family generic peptidase activity with unresolved substrate specificity.", "GO:0008233", None, None, standard_support(gene, "GO:0008233")),
    ]
    data["suggested_questions"] = [{"question": "Does ydcP have peptidase activity in KT2440, and what is its physiological substrate?"}]
    write(gene, data)


def curate_pp4752() -> None:
    gene = "PP_4752"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    ensure_new_annotation(data, gene, "GO:0004177", "enables", "Xaa-Pro aminopeptidase product name and M24B-family evidence support aminopeptidase activity.", "QuickGO returned no GOA rows despite UniProt aminopeptidase evidence.")
    data["core_functions"] = [
        core("M24B-family Xaa-Pro aminopeptidase activity.", "GO:0004177", None, None, standard_support(gene, "GO:0004177")),
    ]
    data["suggested_questions"] = [{"question": "Is PP_4752 functionally redundant with PepP or does it prefer a different proline-containing peptide substrate?"}]
    write(gene, data)


def curate_pp4949() -> None:
    gene = "PP_4949"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0005829", "ACCEPT", "Cytosolic localization is appropriate for the soluble TldD/PmbA-family candidate.")
    set_review(data, gene, "GO:0006508", "ACCEPT", "Proteolysis is conservative process context for the U62/TldD/PmbA peptidase candidate.")
    set_review(data, gene, "GO:0008237", "ACCEPT", "Metallopeptidase activity is supported by U62/TldD/PmbA metalloprotease domains.")
    data["core_functions"] = [
        core("Cytosolic TldD/PmbA-family metallopeptidase activity.", "GO:0008237", ["GO:0006508"], ["GO:0005829"], standard_support(gene, "GO:0008237")),
    ]
    data["suggested_questions"] = [{"question": "What peptide or cellular substrate is processed by PP_4949/TldD-PmbA family protein in KT2440?"}]
    write(gene, data)


def curate_pepP() -> None:
    gene = "pepP"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0004177", "ACCEPT", "Xaa-Pro aminopeptidase/aminopeptidase P evidence supports aminopeptidase activity.")
    set_review(data, gene, "GO:0005737", "ACCEPT", "Cytoplasm is appropriate for this soluble peptide-processing enzyme.")
    set_review(data, gene, "GO:0005829", "ACCEPT", "Cytosol is appropriate for this soluble peptide-processing enzyme.")
    set_review(data, gene, "GO:0006508", "ACCEPT", "Proteolysis is appropriate process context.")
    set_review(data, gene, "GO:0008233", "MARK_AS_OVER_ANNOTATED", "Generic peptidase activity is less informative than aminopeptidase/metalloaminopeptidase activity.")
    set_review(data, gene, "GO:0030145", "KEEP_AS_NON_CORE", "Manganese binding is cofactor context for M24B metalloaminopeptidase activity.")
    set_review(data, gene, "GO:0070006", "ACCEPT", "Metalloaminopeptidase activity is supported by M24B and InterPro evidence.")
    data["core_functions"] = [
        core("Cytosolic M24B-family Xaa-Pro aminopeptidase/metalloaminopeptidase activity.", "GO:0070006", ["GO:0006508"], ["GO:0005829"], standard_support(gene, "GO:0070006")),
    ]
    write(gene, data)


def curate_pp5629() -> None:
    gene = "PP_5629"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    ensure_new_annotation(data, gene, "GO:0008233", "enables", "UniProt keyword and DJ-1/PfpI protease/amidase domain evidence support generic peptidase activity.", "QuickGO returned no GOA rows for PP_5629.")
    ensure_new_annotation(data, gene, "GO:0006508", "involved_in", "Proteolysis is conservative process context for the protease/amidase candidate.", "QuickGO returned no GOA rows for PP_5629.")
    data["core_functions"] = [
        core("Generic DJ-1/PfpI-domain peptidase or protease/amidase activity with unresolved specificity.", "GO:0008233", ["GO:0006508"], None, standard_support(gene, "GO:0008233")),
    ]
    data["suggested_questions"] = [{"question": "Does PP_5629 act as a peptidase, amidase, or regulatory protein in KT2440?"}]
    write(gene, data)


def main() -> None:
    curate_prlC()
    curate_pp0203()
    curate_simple_aminopeptidase("mtfA", "GO:0005829")
    curate_map()
    curate_apeB()
    curate_simple_aminopeptidase("PP_1748")
    curate_yegQ()
    curate_pp2704()
    curate_ydcP()
    curate_pp4752()
    curate_pp4949()
    curate_pepP()
    curate_pp5629()
    print("Curated peptide-processing aminopeptidase split")


if __name__ == "__main__":
    main()
