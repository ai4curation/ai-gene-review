#!/usr/bin/env python3
"""First-pass curation for the PSEPK ppu00946 flavonoid-degradation batch."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


BATCH = Path("projects/P_PUTIDA/batches/ppu00946_flavonoid_degradation_boundary.tsv")


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


CONFIG: dict[str, dict] = {
    "PP_3195": {
        "description": "PP_3195 encodes a predicted S9/prolyl-oligopeptidase-family serine peptidase or alpha/beta-hydrolase fold protein. In the ppu00946 boundary set it is best treated as a generic hydrolase/peptidase-family side node rather than evidence for a defined flavonoid-degradation reaction.",
        "accept": {"GO:0006508", "GO:0008236"},
        "core": [
            {
                "description": "Predicted serine-type peptidase activity from S9 peptidase-domain annotation; physiological substrate remains unresolved.",
                "molecular_function": term("GO:0008236", "serine-type peptidase activity"),
                "directly_involved_in": [term("GO:0006508", "proteolysis")],
            }
        ],
        "questions": [
            "Is PP_3195 an active peptidase/esterase in KT2440, and is it functionally connected to the PP_3197-PP_3206 aromatic-compound cluster?"
        ],
    },
    "PP_3197": {
        "description": "PP_3197 encodes a glyoxalase/VOC-family protein in the ppu00946 boundary cluster, but the fetched GOA table has no annotations and its substrate is unresolved.",
        "core": [
            {
                "description": "Predicted glyoxalase/VOC-family protein with unresolved small-molecule substrate.",
            }
        ],
        "questions": [
            "What substrate does PP_3197 act on, and is it part of aromatic/flavonoid-derived compound degradation?"
        ],
    },
    "PP_3198": {
        "description": "PP_3198 encodes a predicted Rieske 2Fe-2S ferredoxin/electron-transfer protein in the ppu00946 boundary cluster. The current GOA table only supports iron-sulfur cluster binding, so its redox partner and pathway role remain unresolved.",
        "non_core": {"GO:0051537"},
        "core": [
            {
                "description": "Predicted Rieske 2Fe-2S electron-transfer component with unresolved partner enzyme and substrate context.",
            }
        ],
        "questions": [
            "Which oxygenase or redox enzyme partners with PP_3198 in the PP_3195-PP_3206 cluster?"
        ],
    },
    "PP_3204": {
        "description": "PP_3204 encodes a cupin type-2 domain protein in the ppu00946 boundary cluster, but the fetched GOA table has no annotations and the exact catalytic role is unresolved.",
        "core": [
            {
                "description": "Predicted cupin-domain protein with unresolved aromatic-compound or small-molecule substrate.",
            }
        ],
        "questions": [
            "Does PP_3204 catalyze a cupin-family ring-cleavage, isomerization, or dioxygenase reaction in this cluster?"
        ],
    },
    "PP_3205": {
        "description": "PP_3205 encodes a fumarylacetoacetate hydrolase-family protein in the ppu00946 boundary cluster. Current GOA support is only generic catalytic activity, so the specific hydrolase substrate remains unresolved.",
        "over": {"GO:0003824"},
        "core": [
            {
                "description": "Predicted fumarylacetoacetase-like hydrolase with unresolved substrate in an aromatic/flavonoid-degradation boundary cluster.",
            }
        ],
        "questions": [
            "What hydrolase substrate is used by PP_3205, and does it process a flavonoid- or aromatic-ring-cleavage product?"
        ],
    },
    "PP_3206": {
        "description": "PP_3206 encodes a predicted NAD-dependent epimerase/dehydratase-domain protein in the ppu00946 boundary cluster, but the fetched GOA table has no annotations and the substrate is unresolved.",
        "core": [
            {
                "description": "Predicted NAD-dependent epimerase/dehydratase-family enzyme with unresolved small-molecule substrate.",
            }
        ],
        "questions": [
            "What substrate and reaction are catalyzed by PP_3206 in KT2440?"
        ],
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def uniprot_snippet(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if "Full=" in line:
            return line.strip()
    match = re.search(r"AC\s+([A-Z0-9]+);", text)
    if match:
        return f"AC   {match.group(1)};"
    return text.splitlines()[0]


def goa_snippet(annotation: dict[str, str]) -> str:
    return f"{annotation['GO TERM']}\t{annotation['GO NAME']}"


def ensure_file_references(data: dict, gene: str, accession: str, gene_dir: Path) -> None:
    references = list(data.get("references") or [])
    by_id = {ref.get("id"): ref for ref in references}
    additions: list[dict] = []
    uniprot = gene_dir / f"{gene}-uniprot.txt"
    if uniprot.exists():
        ref_id = f"file:PSEPK/{gene}/{gene}-uniprot.txt"
        if ref_id not in by_id:
            additions.append(
                {
                    "id": ref_id,
                    "title": f"UniProt entry for {gene}",
                    "findings": [
                        {
                            "statement": "UniProt provides the protein identity and first-pass functional context used for this review.",
                            "supporting_text": uniprot_snippet(uniprot),
                        }
                    ],
                }
            )
    goa = gene_dir / f"{gene}-goa.tsv"
    if goa.exists():
        ref_id = f"file:PSEPK/{gene}/{gene}-goa.tsv"
        if ref_id not in by_id:
            additions.append(
                {
                    "id": ref_id,
                    "title": f"QuickGO GOA annotations for {gene}",
                    "findings": [
                        {
                            "statement": "The fetched GOA table contains the annotations reviewed for this gene.",
                        }
                    ],
                }
            )
    asta = gene_dir / f"{gene}-deep-research-asta.md"
    if asta.exists():
        ref_id = f"file:PSEPK/{gene}/{gene}-deep-research-asta.md"
        if ref_id not in by_id:
            additions.append(
                {
                    "id": ref_id,
                    "title": f"Asta retrieval report for {gene}",
                    "findings": [
                        {
                            "statement": "Asta retrieval was generated for this first-pass review and used as lightweight identity/literature context.",
                            "supporting_text": f"uniprot_accession: {accession}",
                        }
                    ],
                }
            )
    data["references"] = references + additions


def action_label(action: str) -> str:
    return {
        "ACCEPT": "Accepted",
        "KEEP_AS_NON_CORE": "Retained as non-core",
        "MARK_AS_OVER_ANNOTATED": "Marked as over-annotated",
    }[action]


def classify(annotation: dict[str, str], cfg: dict) -> str:
    go_id = annotation["GO TERM"]
    if go_id in cfg.get("accept", set()):
        return "ACCEPT"
    if go_id in cfg.get("non_core", set()):
        return "KEEP_AS_NON_CORE"
    if go_id in cfg.get("over", set()):
        return "MARK_AS_OVER_ANNOTATED"
    if annotation["GO ASPECT"] == "cellular_component" or "binding" in annotation["GO NAME"]:
        return "KEEP_AS_NON_CORE"
    if annotation["GO NAME"] in {"catalytic activity", "hydrolase activity"}:
        return "MARK_AS_OVER_ANNOTATED"
    return "KEEP_AS_NON_CORE"


def reason_for(action: str, annotation: dict[str, str]) -> str:
    label = annotation["GO NAME"]
    if action == "ACCEPT":
        return (
            f"{label} matches the fetched GOA/UniProt identity for this ppu00946 first-pass review, "
            "but the pathway placement remains a boundary assignment rather than proof of flavonoid degradation."
        )
    if action == "KEEP_AS_NON_CORE":
        return (
            f"{label} is plausible context for this protein, but it is a cofactor, location, binding, "
            "or broad family feature rather than a resolved core reaction."
        )
    if action == "MARK_AS_OVER_ANNOTATED":
        return (
            f"{label} is not necessarily false, but it is broader than the specific molecular activity needed "
            "to support a flavonoid-degradation route."
        )
    raise AssertionError(action)


def review_annotation(
    gene: str,
    annotation: dict,
    goa_by_id_label: dict[tuple[str, str], dict[str, str]],
    cfg: dict,
) -> None:
    term_data = annotation["term"]
    go_id = term_data["id"]
    label = term_data["label"]
    goa_row = goa_by_id_label.get((go_id, label))
    if goa_row is None:
        goa_row = next((row for (gid, _), row in goa_by_id_label.items() if gid == go_id), None)
    action = classify(goa_row or {"GO TERM": go_id, "GO NAME": label, "GO ASPECT": ""}, cfg)
    review = {
        "summary": f"{action_label(action)}: {label} for {gene} in the ppu00946 flavonoid-degradation first-pass review.",
        "action": action,
        "reason": reason_for(action, goa_row or {"GO NAME": label}),
    }
    if goa_row is not None:
        review["supported_by"] = [
            {
                "reference_id": f"file:PSEPK/{gene}/{gene}-goa.tsv",
                "supporting_text": goa_snippet(goa_row),
            }
        ]
    annotation["review"] = review


def support_for_core(gene: str, core: dict, goa_rows: list[dict[str, str]], uniprot: Path) -> list[dict[str, str]]:
    support: list[dict[str, str]] = []
    term_ids: set[str] = set()
    if "molecular_function" in core:
        term_ids.add(core["molecular_function"]["id"])
    for item in core.get("directly_involved_in", []) or []:
        term_ids.add(item["id"])
    for row in goa_rows:
        if row["GO TERM"] in term_ids:
            support.append(
                {
                    "reference_id": f"file:PSEPK/{gene}/{gene}-goa.tsv",
                    "supporting_text": goa_snippet(row),
                }
            )
    if uniprot.exists():
        support.append(
            {
                "reference_id": f"file:PSEPK/{gene}/{gene}-uniprot.txt",
                "supporting_text": uniprot_snippet(uniprot),
            }
        )
    return support


def curate(row: dict[str, str]) -> None:
    gene = row["suggested_review_name"]
    if gene not in CONFIG:
        return
    cfg = CONFIG[gene]
    review_path = Path(row["review_file"])
    gene_dir = review_path.parent
    goa_path = gene_dir / f"{gene}-goa.tsv"
    uniprot_path = gene_dir / f"{gene}-uniprot.txt"
    data = yaml.safe_load(review_path.read_text(encoding="utf-8")) or {}
    goa_rows = read_tsv(goa_path) if goa_path.exists() else []
    goa_by_id_label = {(row["GO TERM"], row["GO NAME"]): row for row in goa_rows}

    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_file_references(data, gene, row["uniprot_accession"], gene_dir)
    for annotation in data.get("existing_annotations") or []:
        review_annotation(gene, annotation, goa_by_id_label, cfg)
    core_functions: list[dict] = []
    for core in cfg.get("core", []):
        core_entry = dict(core)
        core_entry["supported_by"] = support_for_core(gene, core_entry, goa_rows, uniprot_path)
        core_functions.append(core_entry)
    data["core_functions"] = core_functions
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": q} for q in cfg.get("questions", [])]
    data["suggested_experiments"] = []
    review_path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False), encoding="utf-8")


def main() -> None:
    for row in read_tsv(BATCH):
        curate(row)


if __name__ == "__main__":
    main()
