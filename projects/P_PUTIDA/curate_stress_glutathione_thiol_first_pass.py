#!/usr/bin/env python3
"""First-pass curate the PSEPK glutathione/thiol detoxification stress split."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_TSV = ROOT / "projects/P_PUTIDA/batches/module_stress_detoxification_glutathione_thiol_detoxification.tsv"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0016407": {"id": "GO:0016407", "label": "acetyltransferase activity"},
    "GO:0016491": {"id": "GO:0016491", "label": "oxidoreductase activity"},
    "GO:0016740": {"id": "GO:0016740", "label": "transferase activity"},
    "GO:0016747": {"id": "GO:0016747", "label": "acyltransferase activity, transferring groups other than amino-acyl groups"},
    "GO:0140085": {"id": "GO:0140085", "label": "L-amino-acid N-acetyltransferase activity"},
}


GENE_INFO = {
    "PP_0335": {
        "role": "GST-family transferase candidate",
        "description": (
            "PP_0335 encodes a cytoplasmic GST-family protein in Pseudomonas putida KT2440. "
            "The first-pass evidence supports GST-fold transferase-family context, but not a "
            "specific substrate, conjugation reaction, or pathway process."
        ),
        "primary_function": TERM["GO:0016740"],
        "locations": [TERM["GO:0005737"]],
        "new_terms": ["GO:0016740"],
    },
    "PP_2023": {
        "role": "GST-family transferase candidate",
        "description": (
            "PP_2023 encodes a cytoplasmic GST-family protein in Pseudomonas putida KT2440. "
            "The GST N- and C-terminal domain evidence supports conservative transferase-family "
            "context, but the exact glutathione-conjugation substrate remains unresolved."
        ),
        "primary_function": TERM["GO:0016740"],
        "locations": [TERM["GO:0005737"]],
        "new_terms": ["GO:0016740"],
    },
    "PP_3742": {
        "role": "GST-superfamily transferase candidate",
        "description": (
            "PP_3742 encodes a GST-superfamily protein in Pseudomonas putida KT2440. "
            "The first-pass evidence supports a GST-fold transferase candidate, with no "
            "resolved substrate or detoxification process."
        ),
        "primary_function": TERM["GO:0016740"],
        "locations": [],
        "new_terms": ["GO:0016740"],
    },
    "PP_4104": {
        "role": "GST-superfamily transferase candidate",
        "description": (
            "PP_4104 encodes a GST-superfamily protein in Pseudomonas putida KT2440. "
            "The first-pass evidence supports a GST-fold transferase candidate, with no "
            "resolved substrate or detoxification process."
        ),
        "primary_function": TERM["GO:0016740"],
        "locations": [],
        "new_terms": ["GO:0016740"],
    },
    "yffB": {
        "role": "glutathione-dependent thiol reductase candidate",
        "description": (
            "yffB encodes an ArsC-family glutathione-dependent thiol reductase candidate in "
            "Pseudomonas putida KT2440. The first-pass evidence supports a thioredoxin-like "
            "redox enzyme, but the exact in vivo substrate and whether it functions as an "
            "arsenate reductase remain unresolved."
        ),
        "primary_function": TERM["GO:0016491"],
        "locations": [],
        "new_terms": ["GO:0016491"],
    },
    "PP_1939": {
        "role": "glutathione-independent formaldehyde dehydrogenase candidate",
        "description": (
            "PP_1939 encodes a predicted glutathione-independent formaldehyde dehydrogenase "
            "in Pseudomonas putida KT2440. Available first-pass evidence supports only a "
            "conservative oxidoreductase/formaldehyde-detoxification candidate; no specific "
            "cofactor term or pathway process is assigned."
        ),
        "primary_function": TERM["GO:0016491"],
        "locations": [],
        "new_terms": ["GO:0016491"],
    },
    "mnaT": {
        "role": "methionine-derivative N-acetyltransferase",
        "description": (
            "mnaT encodes a GNAT/acyltransferase-family methionine-derivative detoxifier in "
            "Pseudomonas putida KT2440. Existing GOA supports L-amino-acid N-acetyltransferase "
            "activity, consistent with acetylation of L-methionine sulfoximine or "
            "L-methionine sulfone."
        ),
        "primary_function": TERM["GO:0140085"],
        "locations": [],
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


def uniprot_evidence(gene: str) -> list[dict[str, str]]:
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    data = [support(file_id(gene, "uniprot.txt"), first_line(uniprot, "DE   "))]
    for marker in (
        ("DE   AltName:",),
        ("CC   -!- CATALYTIC ACTIVITY:",),
        ("CC   -!- SIMILARITY:",),
        ("DR   InterPro;",),
        ("DR   Pfam;",),
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
    data.extend(uniprot_evidence(gene))
    data.extend(asta_evidence(gene))
    return data


def reference_list(existing_refs: list[dict], gene: str, accession: str) -> list[dict]:
    refs = list(existing_refs)
    seen = {ref["id"] for ref in refs}
    titles = {
        file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({accession})",
        file_id(gene, "uniprot.txt"): f"UniProtKB entry for {gene} ({accession})",
        file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({accession})",
    }
    for ref_id, title in titles.items():
        if ref_id not in seen:
            refs.append({"id": ref_id, "title": title, "findings": []})
    return refs


def review_for_annotation(gene: str, term_id: str) -> dict:
    primary = GENE_INFO[gene]["primary_function"]
    role = GENE_INFO[gene]["role"]
    if term_id == "GO:0005737":
        return {
            "summary": "Cytoplasmic localization is compatible with the soluble enzyme-family context.",
            "action": "ACCEPT",
            "reason": "The GOA localization is reasonable supporting context, though not the pathway-defining function.",
            "supported_by": standard_support(gene, term_id),
        }
    if term_id == primary["id"]:
        return {
            "summary": f"{primary['label']} is the most informative existing molecular-function term for this {role}.",
            "action": "ACCEPT",
            "reason": "The term matches the product name, domain context, and current GOA evidence.",
            "supported_by": standard_support(gene, term_id),
        }
    if gene == "mnaT" and term_id in {"GO:0016407", "GO:0016740", "GO:0016747"}:
        return {
            "summary": "The broad transferase-family annotation is directionally correct but less specific than the supported L-amino-acid N-acetyltransferase term.",
            "action": "MODIFY",
            "reason": "mnaT is annotated as a methionine-derivative detoxifier; GO:0140085 captures the relevant N-acetyltransferase activity more precisely.",
            "proposed_replacement_terms": [TERM["GO:0140085"]],
            "supported_by": standard_support(gene, term_id),
        }
    raise ValueError(f"No review rule for {gene} {term_id}")


def new_annotation(gene: str, term_id: str) -> dict:
    term = TERM[term_id]
    qualifier = "enables"
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": f"First-pass evidence supports adding conservative {term['label']} for this {GENE_INFO[gene]['role']}.",
            "action": "NEW",
            "reason": (
                "The seeded GOA is empty or lacks a molecular-function row. The recommendation is deliberately broad and "
                "based on UniProt product/domain evidence plus Asta retrieval metadata."
            ),
            "supported_by": standard_support(gene, None),
        },
    }


def core_for(gene: str) -> dict:
    info = GENE_INFO[gene]
    core = {
        "description": info["role"],
        "molecular_function": info["primary_function"],
        "supported_by": standard_support(gene, info["primary_function"]["id"]),
    }
    if info["locations"]:
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
                f"What substrate, reaction partner, and stress condition define the physiological function of {gene} in "
                "Pseudomonas putida KT2440?"
            )
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Purify {gene} or test a clean deletion strain under candidate glutathione, thiol-redox, electrophile, "
                "formaldehyde, methionine-derivative, and metal-stress conditions as appropriate for the family."
            ),
            "experiment_type": "targeted enzyme assay and stress-phenotyping assay",
        }
    ]
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str) -> None:
    evidence = standard_support(gene, GENE_INFO[gene]["primary_function"]["id"])
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass glutathione/thiol detoxification stress-bucket curation.",
        GENE_INFO[gene]["description"],
        "",
        "Primary provenance:",
    ]
    for item in evidence[:5]:
        lines.append(f"- [{item['reference_id']} \"{item['supporting_text']}\"]")
    lines.extend(
        [
            "",
            "Decision: keep the assignment conservative. Use broad transferase or oxidoreductase activity where family evidence "
            "does not resolve substrate chemistry, and avoid asserting a glutathione metabolic process unless gene-specific "
            "evidence supports it.",
        ]
    )
    (GENE_ROOT / gene / f"{gene}-notes.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    with BATCH_TSV.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            gene = row["gene"]
            apply_review(gene, row["uniprot_accession"])
            write_notes(gene)
            print(f"Curated {gene}")


if __name__ == "__main__":
    main()
