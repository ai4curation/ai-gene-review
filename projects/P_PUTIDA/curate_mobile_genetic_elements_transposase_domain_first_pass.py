#!/usr/bin/env python3
"""First-pass curation for PSEPK domain-only or fragmentary transposase candidates."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "mobile_genetic_elements_boundary.yaml"
BATCH_ID = "module_mobile_genetic_elements_transposase_domain_or_fragment"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0003676": {"id": "GO:0003676", "label": "nucleic acid binding"},
    "GO:0004803": {"id": "GO:0004803", "label": "transposase activity"},
    "GO:0006313": {"id": "GO:0006313", "label": "DNA transposition"},
}

GENES = [
    "PP_0015",
    "PP_0016",
    "PP_0637",
    "PP_0638",
    "PP_0650",
    "PP_3113",
    "PP_3114",
    "PP_3115",
    "PP_3500",
    "PP_3501",
    "PP_3964",
    "PP_3984",
    "PP_3986",
    "PP_4024",
    "PP_4091",
    "PP_4092",
    "PP_4442",
    "PP_4443",
    "PP_4459",
    "PP_5405",
    "PP_5406",
    "PP_5408",
]

FULL_IS66 = {"PP_0637", "PP_3114", "PP_3501", "PP_3964", "PP_4091", "PP_4443"}
IS66_ORF2 = {"PP_0638", "PP_3113", "PP_3500", "PP_3986", "PP_4024", "PP_4092", "PP_4442"}
DUF_ONLY = {"PP_3115", "PP_3984"}
TNI_ACCESSORY = {"PP_0015", "PP_0016", "PP_5408"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def optional_first_line(path: Path, *needles: str) -> str | None:
    if not path.exists():
        return None
    for line in read_text(path).splitlines():
        if all(needle in line for needle in needles):
            return line
    return None


def support(reference_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": reference_id, "supporting_text": text}


def add_unique(items: list[dict], item: dict | None) -> None:
    if item and item not in items:
        items.append(item)


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def product_line(gene: str) -> str | None:
    path = gene_file(gene, "uniprot.txt")
    return optional_first_line(path, "DE   RecName") or optional_first_line(path, "DE   SubName")


def product_text(gene: str) -> str:
    return (product_line(gene) or "DE   SubName: Full=mobile-element protein").removeprefix("DE   ").rstrip(".")


def goa_line(gene: str, term_id: str) -> str | None:
    return optional_first_line(gene_file(gene, "goa.tsv"), term_id)


def evidence_for(gene: str, term_id: str | None = None, domain_needles: tuple[str, ...] = ()) -> list[dict[str, str]]:
    path = gene_file(gene, "uniprot.txt")
    items: list[dict[str, str]] = []
    if term_id:
        add_unique(items, support(file_id(gene, "goa.tsv"), goa_line(gene, term_id)))
    add_unique(items, support(file_id(gene, "uniprot.txt"), product_line(gene)))
    if term_id:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, f"DR   GO; {term_id};")))
    for needle in domain_needles:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, needle)))
    for marker in ("DR   PANTHER;", "DR   Pfam;", "KW   DNA-binding"):
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, marker)))
    asta = gene_file(gene, "deep-research-asta.md")
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "uniprot_accession:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "protein_description:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "protein_domains:")))
    return items


def description_for(gene: str) -> str:
    product = product_text(gene)
    if gene in FULL_IS66:
        return (
            f"{gene} encodes an IS66-family transposase-domain protein ({product}) with central DDE transposase, "
            "IS66 C-terminal, homeodomain-like, and zinc-finger domain support. The sequence context is consistent "
            "with an insertion-sequence transposition protein."
        )
    if gene in IS66_ORF2:
        return (
            f"{gene} encodes an IS66 Orf2/TnpB-like transposase-related protein ({product}). It is associated with "
            "mobile-element context, but the local evidence resolves only an isolated Orf2/TnpB domain rather than a "
            "complete transposase activity."
        )
    if gene == "PP_0650":
        return (
            f"{gene} encodes an IS66 C-terminal domain-containing transposase-related protein ({product}). The local "
            "record supports a fragmentary mobile-element domain context rather than a resolved catalytic function."
        )
    if gene in DUF_ONLY:
        return (
            f"{gene} encodes a DUF6429-containing transposase-named protein ({product}). The current sequence record "
            "supports mobile-element association but does not resolve a molecular function."
        )
    if gene == "PP_0015":
        return (
            f"{gene} encodes a TniB/AAA+ P-loop NTPase-like transposon protein ({product}) associated with transposon "
            "systems. The available evidence supports transposition-accessory context but not a specific GO molecular "
            "function in this first pass."
        )
    if gene in {"PP_0016", "PP_5408"}:
        return (
            f"{gene} encodes a TniQ-family transposition-associated protein ({product}). The available record supports "
            "TniQ/mobile-element context but does not resolve a specific GO molecular function."
        )
    if gene == "PP_4459":
        return (
            f"{gene} encodes a transposase-named protein ({product}) with DDE/RNaseH-like domain evidence and an "
            "MscS-like PANTHER family assignment. The mixed domain evidence supports mobile-element context but not a "
            "single resolved core function."
        )
    if gene == "PP_5406":
        return (
            f"{gene} encodes a transposase-named protein ({product}) with restriction-endonuclease-like and "
            "tRNA-endonuclease-like superfamily evidence. The record supports broad nucleic-acid-binding context but "
            "does not resolve a specific nuclease or transposase function."
        )
    return (
        f"{gene} encodes a transposase-named protein ({product}) without conserved domain or GOA support sufficient to "
        "resolve a molecular function."
    )


def ensure_references(data: dict, gene: str) -> None:
    refs = data.setdefault("references", [])
    by_id = {ref.get("id"): ref for ref in refs}
    local_refs = [
        (file_id(gene, "uniprot.txt"), f"UniProtKB entry for {gene}", product_line(gene)),
        (file_id(gene, "goa.tsv"), f"QuickGO GOA annotations for {gene}", None),
        (
            file_id(gene, "deep-research-asta.md"),
            f"Asta retrieval report for {gene}",
            optional_first_line(gene_file(gene, "deep-research-asta.md"), "uniprot_accession:"),
        ),
    ]
    for ref_id, title, quote in local_refs:
        if ref_id in by_id:
            continue
        finding = {"statement": "Local first-pass source used for domain/fragmentary transposase review."}
        if quote:
            finding["supporting_text"] = quote
        refs.append({"id": ref_id, "title": title, "findings": [finding]})


def review_for(gene: str, term_id: str) -> dict:
    if gene in FULL_IS66 and term_id == "GO:0004803":
        return {
            "summary": "Domain-supported IS66 transposase activity is added as the conservative core molecular function.",
            "action": "NEW",
            "reason": "The combined IS66 central DDE transposase, IS66 C-terminal, homeodomain-like, and zinc-finger domains support a complete IS66-family transposase rather than an isolated fragment.",
            "supported_by": evidence_for(
                gene,
                None,
                ("IS66_C", "Transposase-related", "Transposase_IS66_central", "Transposase_TnpC_homeodom", "Znf_dom_IS66"),
            ),
        }
    if gene in FULL_IS66 and term_id == "GO:0006313":
        return {
            "summary": "DNA transposition is added as the process context for the IS66-family transposase.",
            "action": "NEW",
            "reason": "The full IS66 transposase-domain architecture supports an insertion-sequence DNA transposition role.",
            "supported_by": evidence_for(
                gene,
                None,
                ("IS66_C", "Transposase-related", "Transposase_IS66_central", "Transposase_TnpC_homeodom", "Znf_dom_IS66"),
            ),
        }
    if term_id == "GO:0003676" and gene == "PP_4459":
        return {
            "summary": "The broad nucleic-acid-binding row is retained as non-core.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The DDE/RNaseH-like domain evidence is compatible with nucleic-acid interaction, but the mixed MscS-like family assignment and lack of a specific GOA function do not support a core transposase or nuclease call.",
            "supported_by": evidence_for(
                gene,
                term_id,
                ("Homeodomain-like_sf", "MscS-like_channel", "RNaseH-like_sf", "RNaseH_sf", "Tc1-like_DDE_dom"),
            ),
        }
    if term_id == "GO:0003676" and gene == "PP_5406":
        return {
            "summary": "The broad nucleic-acid-binding row is retained as non-core.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "Restriction-endonuclease-like and tRNA-endonuclease-like superfamily evidence supports broad nucleic-acid interaction, but does not resolve a specific nuclease or transposase molecular function.",
            "supported_by": evidence_for(gene, term_id, ("Restrct_endonuc-II-like", "tRNA_endonuc-like_dom_sf")),
        }
    raise ValueError(f"No review rule for {gene} {term_id}")


def ensure_new_rows(data: dict, gene: str) -> None:
    if gene not in FULL_IS66:
        return
    rows = data.setdefault("existing_annotations", [])
    if not any(row.get("term", {}).get("id") == "GO:0004803" for row in rows):
        rows.append(
            {
                "term": TERM["GO:0004803"],
                "evidence_type": "IEA",
                "original_reference_id": file_id(gene, "uniprot.txt"),
                "qualifier": "enables",
                "review": review_for(gene, "GO:0004803"),
            }
        )
    if not any(row.get("term", {}).get("id") == "GO:0006313" for row in rows):
        rows.append(
            {
                "term": TERM["GO:0006313"],
                "evidence_type": "IEA",
                "original_reference_id": file_id(gene, "uniprot.txt"),
                "qualifier": "involved_in",
                "review": review_for(gene, "GO:0006313"),
            }
        )


def core_functions_for(gene: str) -> list[dict]:
    if gene not in FULL_IS66:
        return []
    return [
        {
            "description": "IS66-family transposase activity in DNA transposition.",
            "supported_by": evidence_for(
                gene,
                None,
                ("IS66_C", "Transposase-related", "Transposase_IS66_central", "Transposase_TnpC_homeodom", "Znf_dom_IS66"),
            ),
            "molecular_function": TERM["GO:0004803"],
            "directly_involved_in": [TERM["GO:0006313"]],
        }
    ]


def questions_for(gene: str) -> list[dict[str, str]]:
    if gene in FULL_IS66:
        text = f"Is {gene} part of an active IS66 insertion sequence in KT2440 or a decaying mobile-element copy?"
    elif gene in IS66_ORF2:
        text = f"Does {gene} encode an active IS66 Orf2/TnpB-like component, or is it an isolated nonfunctional transposase fragment?"
    elif gene == "PP_0015":
        text = f"Does {gene} encode an ATP-binding TniB accessory factor in an intact transposition system?"
    elif gene in {"PP_0016", "PP_5408"}:
        text = f"Does {gene} encode a functional TniQ targeting/accessory factor for a local transposition system?"
    else:
        text = f"Is {gene} an active mobile-element protein or a product-name/domain-only fragment?"
    return [{"question": text}]


def experiments_for(gene: str) -> list[dict[str, str]]:
    return [
        {
            "experiment_type": "genomic neighborhood inspection",
            "description": f"Inspect the local genomic neighborhood of {gene} for terminal inverted repeats, paired transposase ORFs, or disrupted coding sequence.",
            "hypothesis": f"{gene} belongs to an intact local mobile element rather than a decaying fragment.",
        },
        {
            "experiment_type": "comparative sequence analysis",
            "description": f"Compare {gene} against curated IS66/Tni-family proteins to test whether catalytic and accessory residues are intact.",
            "hypothesis": f"{gene} retains the sequence features expected for its assigned transposase-related class.",
        },
    ]


def curate_gene(gene: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(read_text(path))
    data["status"] = "DRAFT"
    data["description"] = description_for(gene)
    ensure_references(data, gene)
    for row in data.get("existing_annotations") or []:
        term_id = row.get("term", {}).get("id")
        row["review"] = review_for(gene, term_id)
    ensure_new_rows(data, gene)
    data["core_functions"] = core_functions_for(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = questions_for(gene)
    data["suggested_experiments"] = experiments_for(gene)
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def descriptor(term_id: str, description: str | None = None) -> dict:
    obj = {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]}
    if description:
        obj["description"] = description
    return obj


def is66_annoton(gene: str) -> dict:
    return {
        "id": f"{gene.lower()}_domain_supported_is66_transposase",
        "label": f"{gene}: domain-supported IS66 transposase activity in DNA transposition",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": "domain-supported IS66 transposase activity in DNA transposition",
        "function": descriptor("GO:0004803"),
        "processes": [descriptor("GO:0006313")],
    }


def extend_module() -> None:
    data = yaml.safe_load(read_text(MODULE_PATH))
    source_id = f"file:projects/P_PUTIDA/batches/{BATCH_ID}.tsv"
    if not any(e.get("source_id") == source_id for e in data.get("evidence", [])):
        data.setdefault("evidence", []).append(
            {
                "source_id": source_id,
                "title": "PSEPK mobile-genetic-elements domain-only/fragmentary transposase split table",
                "statement": "The split table routes 22 broad mobile-genetic-elements genes to full IS66, isolated Orf2/TnpB, TniB/TniQ, DUF, product-only, or mixed-domain transposase-related evidence classes.",
            }
        )
    note = (
        " The transposase_domain_or_fragment sub-batch adds six full IS66 multi-domain proteins as domain-supported "
        "transposase/DNA-transposition annotons; isolated IS66 Orf2/TnpB, IS66-C-only, DUF6429, TniB/TniQ, mixed-domain, "
        "and product-only records remain curated as unresolved mobile-element context without core GO functions."
    )
    if note.strip() not in data.get("notes", ""):
        data["notes"] = (data.get("notes", "") + note).strip()
    parts = data["module"].setdefault("parts", [])
    parts = [
        part
        for part in parts
        if part.get("node", {}).get("id") != "mobile_bucket_domain_supported_is66_transposases"
    ]
    parts.append(
        {
            "order": 8,
            "role": "Domain-supported IS66 transposase candidates from broad mobile-genetic-elements bucket",
            "node": {
                "id": "mobile_bucket_domain_supported_is66_transposases",
                "label": "Broad-bucket domain-supported IS66 transposases",
                "module_type": "BIOLOGICAL_PROCESS",
                "annotons": [is66_annoton(gene) for gene in sorted(FULL_IS66)],
            },
        }
    )
    data["module"]["parts"] = parts
    MODULE_PATH.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
    extend_module()
    print(f"Curated {len(GENES)} gene reviews")
    print(f"Extended {MODULE_PATH}")


if __name__ == "__main__":
    main()
