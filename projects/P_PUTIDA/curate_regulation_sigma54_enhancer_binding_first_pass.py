#!/usr/bin/env python3
"""First-pass curation for sigma-54 enhancer-binding and LuxR-like regulators."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_DIR = ROOT / "projects" / "P_PUTIDA" / "batches"
BATCH_TSV = BATCH_DIR / "module_regulation_signal_transduction_sigma54_enhancer_binding_regulators.tsv"
PARTITION_TSV = BATCH_DIR / "module_regulation_signal_transduction_partition.tsv"
MODULE_PATH = ROOT / "modules" / "sigma54_enhancer_binding_regulator_boundary.yaml"
TODAY = "2026-07-10"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


TERM = {
    "GO:0000166": term("GO:0000166", "nucleotide binding"),
    "GO:0001216": term("GO:0001216", "DNA-binding transcription activator activity"),
    "GO:0003677": term("GO:0003677", "DNA binding"),
    "GO:0003700": term("GO:0003700", "DNA-binding transcription factor activity"),
    "GO:0005524": term("GO:0005524", "ATP binding"),
    "GO:0006351": term("GO:0006351", "DNA-templated transcription"),
    "GO:0006355": term("GO:0006355", "regulation of DNA-templated transcription"),
    "GO:0043565": term("GO:0043565", "sequence-specific DNA binding"),
}


SIGMA54_GENES = {"PP_0051", "PP_0546", "PP_2259", "PP_2771", "PP_3075", "PP_3467", "PP_3503", "PP_5166"}
LUXR_GENES = {"PP_0767", "PP_2587", "PP_3717", "PP_3847", "PP_3905", "PP_4136", "PP_4647"}
UNRESOLVED_GENES = {"PP_5473"}


def read_batch_rows() -> dict[str, dict[str, str]]:
    with BATCH_TSV.open(encoding="utf-8") as handle:
        return {row["gene"]: row for row in csv.DictReader(handle, delimiter="\t")}


BATCH_ROWS = read_batch_rows()


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def first_line(path: Path, needle: str) -> str | None:
    if not path.exists():
        return None
    for line in lines(path):
        if needle in line:
            return line.strip()
    return None


def add_support(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item["supporting_text"] and item not in items:
        items.append(item)


def support(ref_id: str, text: str) -> dict[str, str]:
    return {"reference_id": ref_id, "supporting_text": text}


def goa_rows(gene: str) -> dict[str, dict[str, str]]:
    path = gene_file(gene, "goa.tsv")
    if not path.exists() or path.stat().st_size == 0:
        return {}
    with path.open(encoding="utf-8") as handle:
        return {row["GO TERM"]: row for row in csv.DictReader(handle, delimiter="\t")}


def goa_line(gene: str, go_id: str) -> str | None:
    path = gene_file(gene, "goa.tsv")
    if not path.exists():
        return None
    for line in lines(path)[1:]:
        if f"\t{go_id}\t" in line:
            return line
    return None


def goa_support(gene: str, go_id: str) -> dict[str, str] | None:
    line = goa_line(gene, go_id)
    if not line:
        return None
    return support(file_id(gene, "goa.tsv"), line)


def product_line(gene: str) -> str | None:
    path = gene_file(gene, "uniprot.txt")
    return first_line(path, "DE   RecName:") or first_line(path, "DE   SubName:")


def uniprot_support_lines(gene: str) -> list[dict[str, str]]:
    path = gene_file(gene, "uniprot.txt")
    items: list[dict[str, str]] = []
    for needle in ("DE   RecName:", "DE   SubName:", "GN   OrderedLocusNames="):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "uniprot.txt"), line))
            if needle.startswith("DE"):
                break
    if gene in SIGMA54_GENES:
        for needle in (
            "DR   InterPro; IPR003593; AAA+_ATPase.",
            "DR   InterPro; IPR002078; Sigma_54_int.",
            "DR   InterPro; IPR025662; Sigma_54_int_dom_ATP-bd_1.",
            "DR   Pfam; PF00158; Sigma54_activat; 1.",
            "DR   InterPro; IPR002197; HTH_Fis.",
            "KW   ATP-binding",
            "KW   Transcription regulation",
        ):
            line = first_line(path, needle)
            if line:
                add_support(items, support(file_id(gene, "uniprot.txt"), line))
    elif gene in LUXR_GENES:
        for needle in (
            "DR   InterPro; IPR016032; Sig_transdc_resp-reg_C-effctor.",
            "DR   InterPro; IPR000792; Tscrpt_reg_LuxR_C.",
            "DR   Pfam; PF00196; GerE; 1.",
            "DR   InterPro; IPR005143; TF_LuxR_autoind-bd_dom.",
            "KW   DNA-binding",
            "KW   Transcription regulation",
        ):
            line = first_line(path, needle)
            if line:
                add_support(items, support(file_id(gene, "uniprot.txt"), line))
    else:
        for needle in ("KW   Membrane", "KW   Transmembrane", "KW   Transmembrane helix"):
            line = first_line(path, needle)
            if line:
                add_support(items, support(file_id(gene, "uniprot.txt"), line))
    return items


def asta_support_lines(gene: str) -> list[dict[str, str]]:
    path = gene_file(gene, "deep-research-asta.md")
    items: list[dict[str, str]] = []
    for needle in ("**Protein Description:**", "protein_description:"):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "deep-research-asta.md"), line))
            break
    line = first_line(path, "**Key Domains:**")
    if line:
        add_support(items, support(file_id(gene, "deep-research-asta.md"), line))
    return items


def evidence_for(gene: str, go_id: str | None = None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if go_id:
        add_support(items, goa_support(gene, go_id))
    for item in uniprot_support_lines(gene):
        add_support(items, item)
    for item in asta_support_lines(gene):
        add_support(items, item)
    return items


def role_for(gene: str) -> str:
    if gene in SIGMA54_GENES:
        return "sigma-54 enhancer-binding transcription activator candidate with unresolved direct regulon"
    if gene == "PP_0767":
        return "MalT-like LuxR-family DNA-binding transcription regulator candidate"
    if gene == "PP_4647":
        return "LuxR autoinducer-binding-family DNA-binding transcription regulator candidate"
    if gene in LUXR_GENES:
        return "LuxR/GerE-family DNA-binding transcription regulator candidate"
    return "product-name-only LuxR-family membrane protein with unresolved transcription-regulator evidence"


def description_for(gene: str) -> str:
    product = BATCH_ROWS[gene]["protein_name"]
    if gene in SIGMA54_GENES:
        return (
            f"{gene} encodes a predicted sigma-54-dependent transcriptional regulator in Pseudomonas putida KT2440. "
            "The local UniProt and Asta retrieval records support AAA+/P-loop and sigma-54 interaction domains, with "
            "HTH or DNA-binding context where present. This first pass curates the protein as a sigma-54 enhancer-binding "
            "transcription activator candidate while leaving its direct regulon and inducing signal unresolved."
        )
    if gene in LUXR_GENES:
        return (
            f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. LuxR/GerE-family DNA-binding domain "
            "evidence supports a DNA-binding transcription-regulator role, but current first-pass evidence does not identify "
            "the regulated operon, ligand, or whether regulation is activating or repressing."
        )
    return (
        f"{gene} is named as a {product} in Pseudomonas putida KT2440, but the fetched record has no GOA rows and no "
        "LuxR/GerE or sigma-54 activator domain support. This first pass leaves the molecular function unresolved; the "
        "record is retained only as product-name and membrane-prediction context."
    )


def replacement(go_id: str) -> list[dict[str, str]]:
    return [TERM[go_id]]


def review_decision(gene: str, go_id: str) -> tuple[str, str, list[dict[str, str]] | None]:
    if gene in SIGMA54_GENES:
        if go_id == "GO:0000166":
            return (
                "MARK_AS_OVER_ANNOTATED",
                "Generic nucleotide binding is true for the AAA+/P-loop sigma-54 activator architecture, but ATP binding and transcription-activator context are more informative.",
                replacement("GO:0005524"),
            )
        if go_id == "GO:0005524":
            return (
                "KEEP_AS_NON_CORE",
                "ATP binding is expected for the AAA+ sigma-54 enhancer-binding domain, but it is cofactor context rather than the most informative regulatory function.",
                None,
            )
        if go_id == "GO:0006351":
            return (
                "MODIFY",
                "The protein regulates transcription rather than being part of the basal transcription machinery; regulation of DNA-templated transcription is the appropriate process-level term.",
                replacement("GO:0006355"),
            )
        if go_id == "GO:0006355":
            return (
                "ACCEPT",
                "Sigma-54 enhancer-binding regulators control transcription by activating sigma-54-dependent promoter output.",
                None,
            )
        if go_id in {"GO:0003677", "GO:0043565", "GO:0003700"}:
            return (
                "MODIFY",
                "The DNA-binding component is sound, but the sigma-54 activator architecture supports the more informative DNA-binding transcription activator activity term.",
                replacement("GO:0001216"),
            )
    if gene in LUXR_GENES:
        if go_id == "GO:0003677":
            return (
                "MODIFY",
                "Generic DNA binding is too broad for a LuxR/GerE-family transcription regulator; DNA-binding transcription factor activity captures the supported role more clearly.",
                replacement("GO:0003700"),
            )
        if go_id == "GO:0006351":
            return (
                "MODIFY",
                "This regulator is not part of the basal transcription process; the supported process is regulation of DNA-templated transcription.",
                replacement("GO:0006355"),
            )
        if go_id == "GO:0006355":
            return (
                "ACCEPT",
                "LuxR/GerE-family DNA-binding domain evidence supports a transcription-regulatory role, while target regulon and direction remain unresolved.",
                None,
            )
    raise KeyError(f"Unhandled annotation {gene} {go_id}")


def review_for(gene: str, go_id: str) -> dict[str, object]:
    if gene in SIGMA54_GENES and go_id == "GO:0001216":
        reason = (
            "The sigma-54 interaction/activator domain architecture supports DNA-binding transcription activator activity "
            "as the clearest core molecular function, even though the fetched GOA rows only expose ATP binding and broad "
            "DNA-binding or transcription-regulation parents."
        )
        return {
            "summary": "DNA-binding transcription activator activity is added as the core sigma-54 enhancer-binding regulator function.",
            "action": "NEW",
            "reason": reason,
            "supported_by": evidence_for(gene, None),
        }
    action, reason, replacements = review_decision(gene, go_id)
    out: dict[str, object] = {
        "summary": reason,
        "action": action,
        "reason": reason,
        "supported_by": evidence_for(gene, go_id),
    }
    if replacements:
        out["proposed_replacement_terms"] = replacements
    return out


def ensure_new_annotations(data: dict[str, object], gene: str) -> None:
    if gene not in SIGMA54_GENES:
        return
    annotations = data.setdefault("existing_annotations", [])
    existing_ids = {ann.get("term", {}).get("id") for ann in annotations if isinstance(ann, dict)}
    if "GO:0001216" in existing_ids:
        return
    if {"GO:0043565", "GO:0003700"} & existing_ids:
        return
    annotations.append(
        {
            "term": TERM["GO:0001216"],
            "evidence_type": "IEA",
            "original_reference_id": file_id(gene, "uniprot.txt"),
            "qualifier": "enables",
            "review": review_for(gene, "GO:0001216"),
        }
    )


def normalize_go_ref_titles(data: dict[str, object]) -> None:
    for ref in data.get("references", []):
        if isinstance(ref, dict) and str(ref.get("id", "")).startswith("GO_REF:") and str(ref.get("title", "")).startswith("TODO:"):
            ref["title"] = f"Gene Ontology annotation reference {ref['id']}"


def references_for(gene: str, data: dict[str, object]) -> list[dict[str, object]]:
    refs = list(data.get("references", []))
    seen = {ref.get("id") for ref in refs if isinstance(ref, dict)}
    goa_findings = [{"supporting_text": line} for line in lines(gene_file(gene, "goa.tsv"))[1:]]
    additions: list[dict[str, object]] = [
        {
            "id": file_id(gene, "goa.tsv"),
            "title": f"QuickGO GOA annotations for {gene} ({BATCH_ROWS[gene]['uniprot_accession']})",
            "findings": goa_findings,
        },
        {
            "id": file_id(gene, "uniprot.txt"),
            "title": f"UniProtKB entry for {gene} ({BATCH_ROWS[gene]['uniprot_accession']})",
            "findings": [{"supporting_text": item["supporting_text"]} for item in uniprot_support_lines(gene)],
        },
        {
            "id": file_id(gene, "deep-research-asta.md"),
            "title": f"Asta retrieval report for {gene} ({BATCH_ROWS[gene]['uniprot_accession']})",
            "findings": [{"supporting_text": item["supporting_text"]} for item in asta_support_lines(gene)],
        },
    ]
    for ref in additions:
        if ref["id"] not in seen:
            refs.append(ref)
            seen.add(ref["id"])
    return refs


def core_functions_for(gene: str) -> list[dict[str, object]]:
    if gene in UNRESOLVED_GENES:
        return []
    if gene in SIGMA54_GENES:
        core = {
            "description": role_for(gene),
            "molecular_function": TERM["GO:0001216"],
            "directly_involved_in": [TERM["GO:0006355"]],
            "supported_by": evidence_for(gene, "GO:0006355"),
        }
        add_support(core["supported_by"], goa_support(gene, "GO:0005524"))  # type: ignore[arg-type]
        if goa_line(gene, "GO:0043565"):
            add_support(core["supported_by"], goa_support(gene, "GO:0043565"))  # type: ignore[arg-type]
        return [core]
    core = {
        "description": role_for(gene),
        "molecular_function": TERM["GO:0003700"],
        "directly_involved_in": [TERM["GO:0006355"]],
        "supported_by": evidence_for(gene, "GO:0006355"),
    }
    add_support(core["supported_by"], goa_support(gene, "GO:0003677"))  # type: ignore[arg-type]
    return [core]


def suggested_questions(gene: str) -> list[dict[str, object]]:
    if gene in SIGMA54_GENES:
        question = f"What signal, partner sigma-54 promoter set, and target regulon are controlled by {gene}?"
    elif gene in LUXR_GENES:
        question = f"What ligand or signal and direct promoter set define the {gene} LuxR-family regulon?"
    else:
        question = f"Is {gene} a functional LuxR-family transcription regulator, or a product-name-only membrane protein?"
    return [{"question": question, "experts": []}]


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    if gene in SIGMA54_GENES:
        description = (
            f"Map {gene}-dependent transcription changes and test ATP-dependent activation of candidate sigma-54 promoters using reporter assays."
        )
    elif gene in LUXR_GENES:
        description = (
            f"Identify {gene}-bound promoters by EMSA or ChIP-seq and test candidate ligand effects on transcriptional regulation."
        )
    else:
        description = (
            f"Re-evaluate {gene} with comparative sequence/domain analysis and membrane-topology prediction before assigning a GO function."
        )
    return [{"experiment_type": "regulatory network mapping", "description": description}]


def curate_gene(gene: str) -> None:
    path = gene_file(gene, "ai-review.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["status"] = "DRAFT"
    data["description"] = description_for(gene)
    data["references"] = references_for(gene, data)
    normalize_go_ref_titles(data)
    for annotation in data.get("existing_annotations", []):
        annotation["review"] = review_for(gene, annotation["term"]["id"])
    ensure_new_annotations(data, gene)
    data["core_functions"] = core_functions_for(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_questions(gene)
    data["suggested_experiments"] = suggested_experiments(gene)
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120, allow_unicode=False),
        encoding="utf-8",
    )
    write_notes(gene)
    print(f"Curated {path.relative_to(ROOT)}")


def write_notes(gene: str) -> None:
    path = gene_file(gene, "notes.md")
    heading = f"## {TODAY} sigma-54/LuxR regulator first pass"
    evidence = evidence_for(gene, "GO:0006355" if gene not in UNRESOLVED_GENES else None)
    lines_out = [
        heading,
        "",
        f"- Batch: `{BATCH_TSV.relative_to(ROOT)}`.",
        f"- Main conclusion: {role_for(gene)}.",
    ]
    if gene in UNRESOLVED_GENES:
        lines_out.append("- Decision: no core GO function assigned; the current record lacks GOA rows and conserved LuxR/sigma-54 domain support.")
    elif gene in SIGMA54_GENES:
        lines_out.append("- Decision: curate as a sigma-54 enhancer-binding transcription activator candidate; ATP binding is retained as non-core cofactor context.")
    else:
        lines_out.append("- Decision: curate as a LuxR/GerE-family DNA-binding transcription regulator candidate; regulon, ligand, and direction remain unresolved.")
    lines_out.extend(["", "Primary provenance:"])
    seen: set[tuple[str, str]] = set()
    for item in evidence:
        key = (item["reference_id"], item["supporting_text"])
        if key in seen:
            continue
        seen.add(key)
        lines_out.append(f"- [{item['reference_id']} \"{item['supporting_text']}\"]")
        if len(seen) >= 8:
            break
    lines_out.append("")
    block = "\n".join(lines_out)
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if heading not in existing:
            path.write_text(existing.rstrip() + "\n\n" + block, encoding="utf-8")
    else:
        path.write_text(f"# {gene} notes\n\n{block}", encoding="utf-8")


def clean_id(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_]+", "_", value.lower())
    return re.sub(r"_+", "_", cleaned).strip("_")


def module_term(go_id: str, description: str | None = None) -> dict[str, object]:
    out: dict[str, object] = {"preferred_term": TERM[go_id]["label"], "term": TERM[go_id]}
    if description:
        out["description"] = description
    return out


def annoton(gene: str) -> dict[str, object]:
    out: dict[str, object] = {
        "id": f"{clean_id(gene)}_{clean_id(role_for(gene))}",
        "label": f"{gene}: {role_for(gene)}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": role_for(gene),
    }
    if gene in SIGMA54_GENES:
        out["function"] = {"preferred_term": TERM["GO:0001216"]["label"], "term": TERM["GO:0001216"]}
        out["processes"] = [{"preferred_term": TERM["GO:0006355"]["label"], "term": TERM["GO:0006355"]}]
        out["notes"] = "ATP binding and sigma-54 interaction domains support enhancer-binding activator context; exact regulon is unresolved."
    elif gene in LUXR_GENES:
        out["function"] = {"preferred_term": TERM["GO:0003700"]["label"], "term": TERM["GO:0003700"]}
        out["processes"] = [{"preferred_term": TERM["GO:0006355"]["label"], "term": TERM["GO:0006355"]}]
        out["notes"] = "LuxR/GerE-family DNA-binding regulator candidate; target regulon and regulatory direction are unresolved."
    else:
        out["notes"] = "Product-name-only LuxR-family record with no GOA rows or conserved LuxR/sigma-54 domain support; no core GO function asserted."
    return out


def part(order: int, part_id: str, label: str, description: str, genes: list[str]) -> dict[str, object]:
    return {
        "order": order,
        "role": label,
        "node": {
            "id": part_id,
            "label": label,
            "module_type": "REGULATORY_STEP",
            "description": description,
            "annotons": [annoton(gene) for gene in genes],
        },
    }


def write_module() -> None:
    evidence: list[dict[str, str]] = [
        {
            "source_id": f"file:{BATCH_TSV.relative_to(ROOT)}",
            "title": "PSEPK regulation/signal-transduction sigma-54/LuxR split",
            "statement": "The batch table records 16 sigma-54 enhancer-binding and LuxR-like regulator candidates handled in this first pass.",
        },
        {
            "source_id": f"file:{PARTITION_TSV.relative_to(ROOT)}",
            "title": "PSEPK regulation/signal-transduction partition table",
            "statement": "The regulation umbrella partition routes these genes into the sigma-54 enhancer-binding regulator split.",
        },
    ]
    for gene in BATCH_ROWS:
        evidence.append({"source_id": file_id(gene, "ai-review.yaml"), "title": f"Curated {gene} review", "statement": role_for(gene)})

    module = {
        "id": "MODULE:sigma54_enhancer_binding_regulator_boundary",
        "title": "Sigma-54 enhancer-binding and LuxR-like regulator boundary",
        "description": (
            "Boundary module for sigma-54 enhancer-binding and LuxR-like regulators from the broad PSEPK regulation/signal-transduction "
            "bucket. It separates AAA+/sigma-54 activator candidates from LuxR/GerE-family DNA-binding regulators and retains "
            "product-name-only records as unresolved context."
        ),
        "status": "DRAFT",
        "evidence": evidence,
        "notes": (
            "This is a regulator-family boundary, not a single pathway. The first pass does not infer target regulons, ligands, "
            "or environmental signals from family/domain names alone."
        ),
        "module": {
            "id": "sigma54_enhancer_binding_regulator_boundary",
            "label": "Sigma-54 enhancer-binding and LuxR-like regulator boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                module_term("GO:0001216", "Specific activator activity used for AAA+/sigma-54 enhancer-binding candidates."),
                module_term("GO:0003700", "Generic transcription-factor function for LuxR/GerE-family regulator candidates."),
                module_term("GO:0005524", "Non-core ATP-binding cofactor context for sigma-54 activator AAA+ domains."),
                module_term("GO:0043565", "DNA-binding component supplied by HTH/Fis or related regulatory domains."),
                module_term("GO:0006355", "Shared process context for transcription regulation."),
            ],
            "parts": [
                part(
                    1,
                    "sigma54_enhancer_binding_activators",
                    "AAA+/sigma-54 enhancer-binding activator candidates",
                    "Sigma-54 interaction and AAA+/P-loop-domain regulators with unresolved target regulons.",
                    ["PP_0051", "PP_0546", "PP_2259", "PP_2771", "PP_3075", "PP_3467", "PP_3503", "PP_5166"],
                ),
                part(
                    2,
                    "luxr_gere_family_transcription_regulators",
                    "LuxR/GerE-family transcription regulator candidates",
                    "LuxR/GerE-family DNA-binding regulators without enough evidence to assign target regulons or direction.",
                    ["PP_0767", "PP_2587", "PP_3717", "PP_3847", "PP_3905", "PP_4136", "PP_4647"],
                ),
                part(
                    3,
                    "unresolved_product_name_only_luxr_record",
                    "Unresolved product-name-only LuxR-family record",
                    "PP_5473 is retained in the batch ledger but no core GO function is asserted in this pass.",
                    ["PP_5473"],
                ),
            ],
        },
    }
    MODULE_PATH.write_text(
        yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, width=120, allow_unicode=False),
        encoding="utf-8",
    )
    print(f"Wrote {MODULE_PATH.relative_to(ROOT)}")


def main() -> None:
    for gene in BATCH_ROWS:
        curate_gene(gene)
    write_module()


if __name__ == "__main__":
    main()
