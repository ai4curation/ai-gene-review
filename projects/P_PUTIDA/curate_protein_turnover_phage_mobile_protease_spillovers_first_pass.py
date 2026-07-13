#!/usr/bin/env python3
"""First-pass curation for protein-turnover phage/mobile protease spillovers."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "phage_structural_packaging_boundary.yaml"
BATCH_TSV = "projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_phage_mobile_protease_spillovers.tsv"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0006508": {"id": "GO:0006508", "label": "proteolysis"},
    "GO:0008233": {"id": "GO:0008233", "label": "peptidase activity"},
    "GO:0008236": {"id": "GO:0008236", "label": "serine-type peptidase activity"},
    "GO:0019068": {"id": "GO:0019068", "label": "virion assembly"},
}


GENE_INFO = {
    "PP_1566": {
        "accession": "Q88MK5",
        "description": "PP_1566 encodes a prophage U35/S78 prohead protease candidate. The supported role is phage-associated peptidase activity and proteolysis, most plausibly in prophage head or capsid maturation rather than host protein turnover.",
        "core_function": "GO:0008233",
    },
    "PP_3878": {
        "accession": "Q88G48",
        "description": "PP_3878 encodes a phage minor capsid protein C with a peptidase S49 domain. The supported role is serine-type peptidase activity/proteolysis in prophage structural maturation context rather than general host protein turnover.",
        "core_function": "GO:0008236",
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


def prefixed_lines(path: Path, prefix: str, limit: int = 8) -> list[str]:
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


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def product_line(gene: str) -> str | None:
    path = gene_file(gene, "uniprot.txt")
    return optional_first_line(path, "DE   RecName") or optional_first_line(path, "DE   SubName")


def evidence_for(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    path = gene_file(gene, "uniprot.txt")
    items: list[dict[str, str]] = []
    if term_id:
        add_unique(items, support(file_id(gene, "goa.tsv"), optional_first_line(gene_file(gene, "goa.tsv"), term_id)))
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, f"DR   GO; {term_id};")))
    add_unique(items, support(file_id(gene, "uniprot.txt"), product_line(gene)))
    for marker in (
        "CC   -!- SIMILARITY:",
        "Peptidase_S78_dom",
        "Prohead_protease",
        "Peptidase_S49",
        "Protein_C",
        "DR   PANTHER;",
        "DR   Pfam;",
        "KW   Viral release",
        "KW   Serine protease",
        "FT   DOMAIN",
    ):
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, marker)))
    for line in prefixed_lines(path, "DR   InterPro;", 8):
        add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    asta = gene_file(gene, "deep-research-asta.md")
    for marker in ("uniprot_accession:", "protein_description:", "protein_family:", "protein_domains:"):
        add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, marker)))
    return items


def ensure_references(data: dict, gene: str) -> None:
    refs = data.setdefault("references", [])
    seen = {ref.get("id") for ref in refs}
    for ref_id, title in [
        (file_id(gene, "goa.tsv"), f"QuickGO GOA annotations for {gene} ({GENE_INFO[gene]['accession']})"),
        (file_id(gene, "uniprot.txt"), f"UniProtKB entry for {gene} ({GENE_INFO[gene]['accession']})"),
        (file_id(gene, "deep-research-asta.md"), f"Asta retrieval report for {gene} ({GENE_INFO[gene]['accession']})"),
    ]:
        if ref_id not in seen and (GENE_ROOT / gene / ref_id.split("/")[-1]).exists():
            refs.append({"id": ref_id, "title": title, "findings": []})
            seen.add(ref_id)


def review_for(gene: str, term_id: str) -> dict:
    if gene == "PP_1566" and term_id == "GO:0008233":
        return {
            "summary": "Peptidase activity is added for the U35/S78 prohead protease candidate.",
            "action": "NEW",
            "reason": "UniProt keyword/domain evidence supports a prophage prohead peptidase. The role is treated as phage maturation context, not host protein-turnover biology.",
            "supported_by": evidence_for(gene, term_id),
        }
    if gene == "PP_1566" and term_id == "GO:0006508":
        return {
            "summary": "Proteolysis is added from UniProt keyword/domain evidence.",
            "action": "NEW",
            "reason": "The prohead protease domain and UniProt proteolysis row support a proteolytic role, but the likely context is prophage maturation rather than general cellular protein turnover.",
            "supported_by": evidence_for(gene, term_id),
        }
    if gene == "PP_3878" and term_id == "GO:0006508":
        return {
            "summary": "Proteolysis is retained for the phage minor capsid/S49 peptidase protein.",
            "action": "ACCEPT",
            "reason": "The InterPro Peptidase S49 GOA row and UniProt serine-protease support indicate a phage-associated proteolysis role.",
            "supported_by": evidence_for(gene, term_id),
        }
    if gene == "PP_3878" and term_id == "GO:0008233":
        return {
            "summary": "Generic peptidase activity is too broad for the S49-family assignment.",
            "action": "MODIFY",
            "reason": "The local UniProt record supports the more specific serine-type peptidase activity term for this Peptidase S49 family protein.",
            "proposed_replacement_terms": [TERM["GO:0008236"]],
            "supported_by": evidence_for(gene, "GO:0008236") or evidence_for(gene, term_id),
        }
    if gene == "PP_3878" and term_id == "GO:0008236":
        return {
            "summary": "Serine-type peptidase activity is supported by the S49-family UniProt row.",
            "action": "NEW",
            "reason": "UniProt carries serine-type peptidase activity for this Peptidase S49/minor capsid protein, providing the more specific replacement for the generic GOA peptidase row.",
            "supported_by": evidence_for(gene, term_id),
        }
    if term_id == "GO:0019068":
        return {
            "summary": "Virion assembly is added as phage structural maturation context.",
            "action": "NEW",
            "reason": "The prohead protease/minor capsid domain context supports prophage structural maturation or assembly context; it is not a host protein-turnover pathway annotation.",
            "supported_by": evidence_for(gene, None),
        }
    raise ValueError(f"No review rule for {gene} {term_id}")


def add_new_annotation(rows: list[dict], gene: str, term_id: str, qualifier: str) -> None:
    if any(row.get("term", {}).get("id") == term_id for row in rows):
        return
    rows.append(
        {
            "term": TERM[term_id],
            "evidence_type": "IEA",
            "original_reference_id": file_id(gene, "uniprot.txt"),
            "qualifier": qualifier,
            "review": review_for(gene, term_id),
        }
    )


def core_functions_for(gene: str) -> list[dict]:
    mf = GENE_INFO[gene]["core_function"]
    return [
        {
            "description": f"Phage-associated {TERM[mf]['label']} in prophage structural maturation context.",
            "supported_by": evidence_for(gene, mf),
            "molecular_function": TERM[mf],
            "directly_involved_in": [TERM["GO:0019068"]],
        }
    ]


def suggested_question(gene: str) -> str:
    if gene == "PP_1566":
        return "Does PP_1566 function as an active U35/S78 prophage prohead protease during capsid maturation?"
    return "Does PP_3878 act as an active S49 serine protease in prophage minor capsid maturation?"


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    return [
        {
            "experiment_type": "comparative sequence analysis",
            "description": f"Compare {gene} against curated phage prohead/minor-capsid proteases to verify domain completeness and catalytic motif conservation.",
            "hypothesis": f"{gene} retains the catalytic features expected for an active phage-associated protease.",
        },
        {
            "experiment_type": "prophage locus inspection",
            "description": f"Inspect genes neighboring {gene} for coherent prophage head, tail, packaging, and lysis modules.",
            "hypothesis": f"{gene} belongs to a prophage structural maturation locus rather than a host protein-turnover pathway.",
        },
    ]


def curate_gene(gene: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(read_text(path))
    data["status"] = "DRAFT"
    data["description"] = GENE_INFO[gene]["description"]
    ensure_references(data, gene)
    rows = data.setdefault("existing_annotations", [])
    for row in rows:
        row["review"] = review_for(gene, row["term"]["id"])
    if gene == "PP_1566":
        add_new_annotation(rows, gene, "GO:0008233", "enables")
        add_new_annotation(rows, gene, "GO:0006508", "involved_in")
    if gene == "PP_3878":
        add_new_annotation(rows, gene, "GO:0008236", "enables")
    add_new_annotation(rows, gene, "GO:0019068", "involved_in")
    data["core_functions"] = core_functions_for(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": suggested_question(gene), "experts": []}]
    data["suggested_experiments"] = suggested_experiments(gene)
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def descriptor(term_id: str, description: str | None = None) -> dict:
    obj = {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]}
    if description:
        obj["description"] = description
    return obj


def annoton(gene: str) -> dict:
    mf = GENE_INFO[gene]["core_function"]
    role = f"phage-associated {TERM[mf]['label']} in structural maturation context"
    return {
        "id": f"{gene.lower()}_phage_protease_maturation",
        "label": f"{gene}: {role}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": role,
        "function": descriptor(mf),
        "processes": [descriptor("GO:0019068")],
    }


def extend_module() -> None:
    data = yaml.safe_load(read_text(MODULE_PATH))
    source_id = f"file:{BATCH_TSV}"
    if not any(item.get("source_id") == source_id for item in data.get("evidence", [])):
        data.setdefault("evidence", []).append(
            {
                "source_id": source_id,
                "title": "PSEPK protein-turnover phage/mobile protease spillover split table",
                "statement": "The split table routes two phage-associated protease candidates out of host protein-turnover context and into prophage structural maturation context.",
            }
        )
    note = (
        " The protein_folding_targeting_turnover phage/mobile protease split contributes PP_1566 and PP_3878 as "
        "phage-associated prohead/minor-capsid protease candidates, represented as proteolytic maturation context "
        "rather than host protein turnover."
    )
    if note.strip() not in data.get("notes", ""):
        data["notes"] = (data.get("notes", "") + note).strip()
    concepts = data["module"].setdefault("concepts", [])
    existing_terms = {item.get("term", {}).get("id") for item in concepts}
    for term_id, description in [
        ("GO:0008233", "Generic peptidase activity for U35/S78 phage prohead protease context."),
        ("GO:0008236", "Serine-type peptidase activity for S49 phage minor capsid protease context."),
        ("GO:0006508", "Proteolysis in prophage structural maturation context."),
    ]:
        if term_id not in existing_terms:
            concepts.append(descriptor(term_id, description))
            existing_terms.add(term_id)
    parts = data["module"].setdefault("parts", [])
    parts = [part for part in parts if part.get("node", {}).get("id") != "phage_protease_maturation_spillovers"]
    parts.append(
        {
            "order": 3,
            "role": "Phage-associated protease maturation spillovers",
            "node": {
                "id": "phage_protease_maturation_spillovers",
                "label": "Phage protease maturation spillovers",
                "module_type": "MOLECULAR_FUNCTION",
                "description": "Protease-keyword genes routed to prophage structural maturation context rather than host protein turnover.",
                "annotons": [annoton(gene) for gene in sorted(GENE_INFO)],
            },
        }
    )
    data["module"]["parts"] = parts
    MODULE_PATH.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str) -> None:
    evidence = evidence_for(gene, GENE_INFO[gene]["core_function"])
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass curation for the protein-turnover phage/mobile protease spillover bucket.",
        GENE_INFO[gene]["description"],
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
    lines.extend(
        [
            "",
            "Decision: route to prophage structural/maturation context and do not treat as a host protein-turnover enzyme.",
            "",
        ]
    )
    gene_file(gene, "notes.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    for gene in GENE_INFO:
        curate_gene(gene)
        write_notes(gene)
    extend_module()
    print("Curated protein-turnover phage/mobile protease spillovers")


if __name__ == "__main__":
    main()
