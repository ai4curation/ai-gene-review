#!/usr/bin/env python3
"""First-pass curate the PSEPK cofactor/metal maturation chaperone split."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0000166": {"id": "GO:0000166", "label": "nucleotide binding"},
    "GO:0003924": {"id": "GO:0003924", "label": "GTPase activity"},
    "GO:0004109": {"id": "GO:0004109", "label": "coproporphyrinogen oxidase activity"},
    "GO:0005525": {"id": "GO:0005525", "label": "GTP binding"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0006105": {"id": "GO:0006105", "label": "succinate metabolic process"},
    "GO:0006457": {"id": "GO:0006457", "label": "protein folding"},
    "GO:0006779": {"id": "GO:0006779", "label": "porphyrin-containing compound biosynthetic process"},
    "GO:0009236": {"id": "GO:0009236", "label": "cobalamin biosynthetic process"},
    "GO:0016151": {"id": "GO:0016151", "label": "nickel cation binding"},
    "GO:0016531": {"id": "GO:0016531", "label": "copper chaperone activity"},
    "GO:0016787": {"id": "GO:0016787", "label": "hydrolase activity"},
    "GO:0019627": {"id": "GO:0019627", "label": "urea metabolic process"},
    "GO:0020037": {"id": "GO:0020037", "label": "heme binding"},
    "GO:0043419": {"id": "GO:0043419", "label": "urea catabolic process"},
    "GO:0046872": {"id": "GO:0046872", "label": "metal ion binding"},
    "GO:0050660": {"id": "GO:0050660", "label": "flavin adenine dinucleotide binding"},
    "GO:0051082": {"id": "GO:0051082", "label": "unfolded protein binding"},
    "GO:0051536": {"id": "GO:0051536", "label": "iron-sulfur cluster binding"},
    "GO:0051539": {"id": "GO:0051539", "label": "4 iron, 4 sulfur cluster binding"},
    "GO:0065003": {"id": "GO:0065003", "label": "protein-containing complex assembly"},
    "GO:0140827": {"id": "GO:0140827", "label": "zinc chaperone activity"},
}


DESCRIPTIONS = {
    "PP_0588": "PP_0588 is a small HMA-domain copper/metal-binding chaperone candidate. The first-pass evidence supports metal binding and HMA-domain copper-chaperone context, but not a resolved target pathway.",
    "sdhE": "SdhE is a cytoplasmic FAD assembly factor required for covalent flavinylation and assembly of the succinate dehydrogenase flavoprotein subunit SdhA and related flavinylated proteins.",
    "ureD": "UreD is a cytoplasmic urease accessory protein required for nickel metallocenter incorporation during urease maturation. Together with UreF and UreG, it forms a GTP-hydrolysis-dependent chaperone complex that activates urease apoprotein.",
    "ureE": "UreE is a cytoplasmic urease accessory metallochaperone that binds nickel and probably donates nickel during urease metallocenter assembly.",
    "ureF": "UreF is a cytoplasmic urease accessory protein required for functional incorporation of the nickel metallocenter into urease, acting with UreD and UreG in the urease activation complex.",
    "ureG": "UreG is a cytoplasmic SIMIBI/G3E-family GTPase required for GTP-dependent incorporation of nickel into the urease metallocenter during urease maturation.",
    "cobW": "CobW is a SIMIBI/G3E-family zinc chaperone candidate with GTPase-domain signatures. Current UniProt evidence supports zinc-cofactor transfer requiring GTP hydrolysis rather than a specific cobalamin-biosynthesis role.",
    "zinU": "ZinU is a predicted P-loop GTPase-dependent zinc chaperone. UniProt evidence supports GTP-dependent zinc cofactor transfer to target proteins, but the specific target in KT2440 is unresolved.",
    "PP_4836": "PP_4836 is a signal-peptide-containing PCu(A)C/LpqE-like copper chaperone candidate. Domain and product-name evidence support copper-chaperone context, but no GOA rows are currently available.",
    "yggW": "YggW/HemW is a cytoplasmic radical-SAM-family heme chaperone candidate that binds heme and a [4Fe-4S] cluster and probably transfers heme to an unknown acceptor.",
    "PP_5361": "PP_5361 is a ZNG1/ZigA-like SIMIBI/G3E-family zinc chaperone candidate with GTPase-domain signatures. Current evidence supports GTP-dependent zinc-cofactor transfer but not a specific target protein.",
    "PP_5393": "PP_5393 is a small HMA-domain metal-binding chaperone candidate. Local evidence supports only a conservative metal-binding/HMA-domain context.",
}


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def optional_first_line(path: Path, *needles: str) -> str | None:
    for line in read_lines(path):
        if all(needle in line for needle in needles):
            return line
    return None


def first_line(path: Path, *needles: str) -> str:
    line = optional_first_line(path, *needles)
    if line is None:
        raise ValueError(f"No line in {path} contains {needles}")
    return line


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def add_unique(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if not item:
        return
    key = (item["reference_id"], item["supporting_text"])
    if key not in {(existing["reference_id"], existing["supporting_text"]) for existing in items}:
        items.append(item)


def goa_support(gene: str, term_id: str) -> dict[str, str] | None:
    line = optional_first_line(GENE_ROOT / gene / f"{gene}-goa.tsv", term_id)
    if not line:
        return None
    return support(file_id(gene, "goa.tsv"), line)


def uniprot_support(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    items: list[dict[str, str]] = []
    add_unique(items, support(file_id(gene, "uniprot.txt"), first_line(path, "DE   ")))
    if term_id:
        line = optional_first_line(path, f"DR   GO; {term_id};")
        if line:
            add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    for needles in (
        ("CC   -!- FUNCTION:",),
        ("CC   -!- CATALYTIC ACTIVITY:",),
        ("CC   -!- SUBUNIT:",),
        ("CC   -!- SUBCELLULAR LOCATION:",),
        ("CC   -!- COFACTOR:",),
        ("CC   -!- SIMILARITY:",),
        ("DR   PANTHER;",),
        ("DR   Pfam;",),
        ("FT   DOMAIN",),
        ("FT   SIGNAL",),
    ):
        line = optional_first_line(path, *needles)
        if line:
            add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    for line in [line for line in read_lines(path) if line.startswith("DR   InterPro;")][:5]:
        add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    return items


def asta_support(gene: str) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    items: list[dict[str, str]] = []
    for marker in ("  uniprot_accession:", "  protein_description:", "  protein_family:", "  protein_domains:"):
        line = optional_first_line(path, marker)
        if line:
            add_unique(items, support(file_id(gene, "deep-research-asta.md"), line))
    return items


def standard_support(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if term_id:
        add_unique(items, goa_support(gene, term_id))
    for item in uniprot_support(gene, term_id):
        add_unique(items, item)
    for item in asta_support(gene):
        add_unique(items, item)
    return items


def load(gene: str) -> dict:
    return yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text(encoding="utf-8"))


def write(gene: str, data: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=120), encoding="utf-8")


def accession(data: dict) -> str:
    return data.get("id", "")


def ensure_references(data: dict, gene: str) -> None:
    refs = data.setdefault("references", [])
    seen = {ref["id"] for ref in refs}
    acc = accession(data)
    for ref_id, title in {
        file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({acc})",
        file_id(gene, "uniprot.txt"): f"UniProtKB entry for {gene} ({acc})",
        file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({acc})",
    }.items():
        if ref_id not in seen:
            refs.append({"id": ref_id, "title": title, "findings": []})
            seen.add(ref_id)


def finish_common(data: dict, gene: str) -> None:
    data["status"] = "DRAFT"
    data["description"] = DESCRIPTIONS[gene]
    data["proposed_new_terms"] = data.get("proposed_new_terms") or []
    data["suggested_questions"] = data.get("suggested_questions") or []
    data["suggested_experiments"] = data.get("suggested_experiments") or []


def set_review(data: dict, gene: str, term_id: str, action: str, summary: str, reason: str | None = None) -> None:
    for ann in data.get("existing_annotations") or []:
        if ann.get("term", {}).get("id") == term_id:
            review = {"summary": summary, "action": action, "supported_by": standard_support(gene, term_id)}
            if reason:
                review["reason"] = reason
            ann["review"] = review
            return
    raise ValueError(f"{gene} has no annotation {term_id}")


def ensure_new_annotation(data: dict, gene: str, term_id: str, qualifier: str, summary: str, reason: str) -> None:
    annotations = data.setdefault("existing_annotations", [])
    if any(ann.get("term", {}).get("id") == term_id for ann in annotations):
        return
    annotations.append(
        {
            "term": TERM[term_id],
            "evidence_type": "IEA",
            "original_reference_id": file_id(gene, "uniprot.txt"),
            "qualifier": qualifier,
            "review": {
                "summary": summary,
                "action": "NEW",
                "reason": reason,
                "supported_by": standard_support(gene, term_id),
            },
        }
    )


def core(description: str, mf: str, processes: list[str] | None = None, locations: list[str] | None = None, supported_by: list[dict[str, str]] | None = None) -> dict:
    item = {"description": description, "molecular_function": TERM[mf], "supported_by": supported_by or []}
    if processes:
        item["directly_involved_in"] = [TERM[p] for p in processes]
    if locations:
        item["locations"] = [TERM[loc] for loc in locations]
    return item


def curate_hma(gene: str, copper: bool = False) -> None:
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    if any(ann.get("term", {}).get("id") == "GO:0046872" for ann in data.get("existing_annotations") or []):
        set_review(data, gene, "GO:0046872", "ACCEPT", "Conservative metal-binding annotation is supported by HMA-domain evidence.")
    if copper:
        ensure_new_annotation(data, gene, "GO:0016531", "enables", "Copper-chaperone activity is supported by product name and PCu(A)C/HMA-domain context.", "Local UniProt and domain evidence support copper-chaperone context.")
        data["core_functions"] = [core("Conservative copper/metal chaperone activity inferred from HMA/PCu(A)C-family evidence.", "GO:0016531", supported_by=standard_support(gene, "GO:0016531"))]
    else:
        data["core_functions"] = [core("Conservative HMA-domain metal-ion-binding activity.", "GO:0046872", supported_by=standard_support(gene, "GO:0046872"))]
    data["suggested_questions"] = [{"question": f"What metal and target protein does {gene} deliver in KT2440?"}]
    write(gene, data)


def curate_sdhE() -> None:
    gene = "sdhE"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0005737", "ACCEPT", "Correct cytoplasmic localization for SdhE.")
    # Duplicate cytoplasm rows are valid; update both.
    for ann in data.get("existing_annotations") or []:
        if ann.get("term", {}).get("id") == "GO:0005737":
            ann["review"] = {"summary": "Correct cytoplasmic localization for SdhE.", "action": "ACCEPT", "supported_by": standard_support(gene, "GO:0005737")}
    set_review(data, gene, "GO:0006105", "KEEP_AS_NON_CORE", "SdhE supports succinate metabolism indirectly through succinate dehydrogenase flavinylation rather than catalyzing a TCA-cycle reaction.")
    ensure_new_annotation(data, gene, "GO:0050660", "enables", "SdhE is an FAD assembly factor that accelerates covalent attachment of FAD to SdhA and other flavinylated proteins.", "FAD assembly/flavinylation is the supported molecular role; GOA lacks a molecular-function row.")
    data["core_functions"] = [core("FAD assembly/flavinylation factor for succinate dehydrogenase and related flavoproteins.", "GO:0050660", None, ["GO:0005737"], standard_support(gene, "GO:0050660"))]
    write(gene, data)


def curate_ureD_or_F(gene: str) -> None:
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0005737", "ACCEPT", "Correct cytoplasmic localization for urease accessory protein.")
    set_review(data, gene, "GO:0016151", "ACCEPT", "Nickel-binding annotation is consistent with urease metallocenter assembly, although the main role is accessory activation rather than a free metal-storage function.")
    data["core_functions"] = [core("Nickel-associated urease maturation accessory role in metallocenter incorporation.", "GO:0016151", None, ["GO:0005737"], standard_support(gene, "GO:0016151"))]
    write(gene, data)


def curate_ureE() -> None:
    gene = "ureE"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0005737", "ACCEPT", "Correct cytoplasmic localization for UreE.")
    set_review(data, gene, "GO:0006457", "KEEP_AS_NON_CORE", "UreE supports urease maturation/metallocenter assembly; generic protein folding is broader than the nickel donor role.")
    set_review(data, gene, "GO:0016151", "ACCEPT", "Core nickel-binding function for the UreE urease metallochaperone.")
    set_review(data, gene, "GO:0019627", "ACCEPT", "Urea metabolic process is appropriate downstream context because UreE activates urease by nickel delivery.")
    set_review(data, gene, "GO:0065003", "ACCEPT", "Protein-containing complex assembly captures urease metallocenter/complex maturation context.")
    ensure_new_annotation(data, gene, "GO:0051082", "enables", "UniProt carries unfolded-protein-binding evidence for UreE, consistent with its chaperone-like urease assembly role.", "GOA lacks this UniProt-transferred molecular-function row.")
    data["core_functions"] = [
        core("Nickel donor/metallochaperone role during urease metallocenter assembly.", "GO:0016151", ["GO:0065003", "GO:0019627"], ["GO:0005737"], standard_support(gene, "GO:0016151")),
        core("Chaperone-like client binding during urease maturation.", "GO:0051082", ["GO:0065003"], ["GO:0005737"], standard_support(gene, "GO:0051082")),
    ]
    write(gene, data)


def curate_ureG() -> None:
    gene = "ureG"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0003924", "ACCEPT", "Correct GTPase activity for the SIMIBI/G3E UreG maturation factor.")
    set_review(data, gene, "GO:0005737", "ACCEPT", "Correct cytoplasmic localization for UreG.")
    set_review(data, gene, "GO:0016151", "ACCEPT", "Nickel-binding annotation is consistent with UreG-mediated nickel metallocenter incorporation.")
    set_review(data, gene, "GO:0043419", "ACCEPT", "Urea catabolic process is appropriate because UreG activates urease for urea hydrolysis.")
    ensure_new_annotation(data, gene, "GO:0005525", "enables", "GTP binding is supported by UniProt nucleotide-binding features for UreG.", "GTP binding is part of the UreG GTPase mechanism and is missing from the fetched GOA rows.")
    data["core_functions"] = [core("GTP hydrolysis-dependent urease nickel-metallocenter maturation.", "GO:0003924", ["GO:0043419"], ["GO:0005737"], standard_support(gene, "GO:0003924"))]
    write(gene, data)


def curate_zng(gene: str, has_goa: bool = True) -> None:
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    if has_goa:
        if any(ann.get("term", {}).get("id") == "GO:0005737" for ann in data.get("existing_annotations") or []):
            set_review(data, gene, "GO:0005737", "ACCEPT", "Cytoplasmic localization is consistent with soluble ZNG1/CobW-family GTPase chaperone context.")
        if any(ann.get("term", {}).get("id") == "GO:0000166" for ann in data.get("existing_annotations") or []):
            set_review(data, gene, "GO:0000166", "MARK_AS_OVER_ANNOTATED", "Correct but broad; GTPase activity is the more informative molecular-function term.")
        if any(ann.get("term", {}).get("id") == "GO:0016787" for ann in data.get("existing_annotations") or []):
            set_review(data, gene, "GO:0016787", "MARK_AS_OVER_ANNOTATED", "Correct but broad hydrolase parent; GTPase/zinc-chaperone function is more informative.")
    if gene == "cobW":
        set_review(data, gene, "GO:0009236", "REMOVE", "The CobW name/family transfer does not establish a cobalamin-biosynthesis role; UniProt currently describes a ZNG1-like zinc chaperone function.")
    ensure_new_annotation(data, gene, "GO:0003924", "enables", "GTPase activity is supported by the G3E/P-loop NTPase family and UniProt GTP hydrolysis reaction.", "GOA has only broad nucleotide/hydrolase terms or no rows for this zinc chaperone candidate.")
    ensure_new_annotation(data, gene, "GO:0140827", "enables", "Zinc chaperone activity is supported by UniProt function text describing zinc cofactor transfer to target proteins.", "This is the most informative molecular function for the ZNG1/CobW-family candidate.")
    data["core_functions"] = [
        core("GTP-dependent zinc chaperone activity for target-protein metal cofactor delivery.", "GO:0140827", None, ["GO:0005737"] if any(ann.get("term", {}).get("id") == "GO:0005737" for ann in data.get("existing_annotations") or []) else None, standard_support(gene, "GO:0140827")),
        core("GTP hydrolysis supporting zinc cofactor transfer.", "GO:0003924", None, ["GO:0005737"] if any(ann.get("term", {}).get("id") == "GO:0005737" for ann in data.get("existing_annotations") or []) else None, standard_support(gene, "GO:0003924")),
    ]
    data["suggested_questions"] = [{"question": f"What zinc-dependent target protein is activated by {gene} in KT2440?"}]
    write(gene, data)


def curate_yggW() -> None:
    gene = "yggW"
    data = load(gene)
    ensure_references(data, gene)
    finish_common(data, gene)
    set_review(data, gene, "GO:0003824", "MARK_AS_OVER_ANNOTATED", "Generic catalytic activity is uninformative and weaker than the specific heme/Fe-S chaperone evidence.")
    set_review(data, gene, "GO:0004109", "MARK_AS_OVER_ANNOTATED", "The family transfer suggests coproporphyrinogen oxidase ancestry, but UniProt describes HemW as probably a heme chaperone rather than assigning this reaction as the main role.")
    set_review(data, gene, "GO:0005737", "ACCEPT", "Correct cytoplasmic localization.")
    set_review(data, gene, "GO:0006779", "KEEP_AS_NON_CORE", "Porphyrin/heme biosynthetic context is plausible, but the direct role is heme transfer to an unknown acceptor.")
    set_review(data, gene, "GO:0046872", "MARK_AS_OVER_ANNOTATED", "Correct broad parent, but 4 iron, 4 sulfur cluster binding and heme binding are more informative.")
    set_review(data, gene, "GO:0051536", "KEEP_AS_NON_CORE", "Iron-sulfur cluster binding is correct but the 4Fe-4S child term is more precise.")
    set_review(data, gene, "GO:0051539", "ACCEPT", "Correct 4Fe-4S cluster binding for the radical-SAM HemW-like protein.")
    ensure_new_annotation(data, gene, "GO:0020037", "enables", "Heme binding is directly supported by UniProt function text for HemW.", "GOA lacks the heme-binding molecular-function row despite heme-chaperone evidence.")
    data["core_functions"] = [
        core("Heme binding and probable heme-chaperone transfer to an unknown acceptor.", "GO:0020037", None, ["GO:0005737"], standard_support(gene, "GO:0020037")),
        core("4Fe-4S cluster binding by the radical-SAM-family HemW protein.", "GO:0051539", None, ["GO:0005737"], standard_support(gene, "GO:0051539")),
    ]
    data["suggested_questions"] = [{"question": "What is the physiological heme acceptor for HemW/YggW in KT2440?"}]
    write(gene, data)


def main() -> None:
    curate_hma("PP_0588", copper=True)
    curate_sdhE()
    curate_ureD_or_F("ureD")
    curate_ureE()
    curate_ureD_or_F("ureF")
    curate_ureG()
    curate_zng("cobW", has_goa=True)
    curate_zng("zinU", has_goa=True)
    curate_hma("PP_4836", copper=True)
    curate_yggW()
    curate_zng("PP_5361", has_goa=False)
    curate_hma("PP_5393", copper=False)
    print("Curated cofactor/metal maturation chaperone split")


if __name__ == "__main__":
    main()
