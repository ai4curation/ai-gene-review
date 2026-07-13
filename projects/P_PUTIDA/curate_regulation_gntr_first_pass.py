#!/usr/bin/env python3
"""First-pass curation for GntR-family transcriptional regulators."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_DIR = ROOT / "projects" / "P_PUTIDA" / "batches"
BATCH_TSV = BATCH_DIR / "module_regulation_signal_transduction_gntr_transcriptional_regulators.tsv"
MODULE_PATH = ROOT / "modules" / "gntr_transcriptional_regulator_boundary.yaml"
TODAY = "2026-07-10"


UTRA_REGULATORS = {"PP_0204", "PP_1697", "PP_1727", "PP_2066"}
AMINOTRANSFERASE_DOMAIN_REGULATORS = {
    "PP_0486",
    "PP_1109",
    "PP_2542",
    "PP_2642",
    "PP_2829",
    "PP_2948",
    "PP_3544",
    "PP_3750",
    "PP_4197",
    "PP_4429",
    "PP_5342",
}
FADR_GNTR_REGULATORS = {
    "PP_0163",
    "PP_0620",
    "PP_0969",
    "PP_2253",
    "PP_2254",
    "PP_2333",
    "csiR",
    "PP_3603",
    "PP_3649",
    "PP_3738",
    "PP_4277",
    "PP_4283",
    "PP_4345",
    "PP_4759",
}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


TERM: dict[str, dict[str, str]] = {
    "GO:0003677": term("GO:0003677", "DNA binding"),
    "GO:0003700": term("GO:0003700", "DNA-binding transcription factor activity"),
    "GO:0005829": term("GO:0005829", "cytosol"),
    "GO:0006351": term("GO:0006351", "DNA-templated transcription"),
    "GO:0006355": term("GO:0006355", "regulation of DNA-templated transcription"),
    "GO:0030170": term("GO:0030170", "pyridoxal phosphate binding"),
    "GO:0045892": term("GO:0045892", "negative regulation of DNA-templated transcription"),
}


def read_batch_rows() -> dict[str, dict[str, str]]:
    with BATCH_TSV.open(encoding="utf-8") as handle:
        return {row["gene"]: row for row in csv.DictReader(handle, delimiter="\t")}


BATCH_ROWS = read_batch_rows()
GENES = list(BATCH_ROWS)


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return path.read_text(encoding="utf-8").splitlines()


def first_line(path: Path, *needles: str) -> str | None:
    for line in lines(path):
        if all(needle in line for needle in needles):
            return line.strip()
    return None


def support(ref_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": ref_id, "supporting_text": text}


def add_support(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item["supporting_text"] and item not in items:
        items.append(item)


def goa_lines(gene: str) -> list[str]:
    path = gene_file(gene, "goa.tsv")
    return lines(path)[1:] if path.exists() else []


def goa_ids(gene: str) -> set[str]:
    path = gene_file(gene, "goa.tsv")
    if not path.exists() or path.stat().st_size == 0:
        return set()
    with path.open(encoding="utf-8") as handle:
        return {row["GO TERM"] for row in csv.DictReader(handle, delimiter="\t") if row.get("GO TERM")}


def goa_line(gene: str, go_id: str, evidence_type: str | None = None, reference_id: str | None = None) -> str | None:
    for line in goa_lines(gene):
        if f"\t{go_id}\t" not in line:
            continue
        if evidence_type and f"\t{evidence_type}\t" not in line:
            continue
        if reference_id and f"\t{reference_id}\t" not in line:
            continue
        return line
    return None


def goa_support(gene: str, go_id: str, evidence_type: str | None = None, reference_id: str | None = None) -> dict[str, str] | None:
    return support(file_id(gene, "goa.tsv"), goa_line(gene, go_id, evidence_type=evidence_type, reference_id=reference_id))


def uniprot_support_lines(gene: str) -> list[dict[str, str]]:
    path = gene_file(gene, "uniprot.txt")
    items: list[dict[str, str]] = []
    for needle in ("DE   RecName:", "DE   SubName:", "GN   Name=", "GN   OrderedLocusNames="):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "uniprot.txt"), line))
            if needle.startswith("DE"):
                break
    for needle in (
        "DR   InterPro; IPR000524; Tscrpt_reg_HTH_GntR.",
        "DR   InterPro; IPR003992; GntR_C.",
        "DR   InterPro; IPR011711; GntR_C.",
        "DR   InterPro; IPR008920; TF_FadR/GntR_C.",
        "DR   InterPro; IPR011663; UTRA.",
        "DR   InterPro; IPR028978; Chorismate_lyase_/UTRA_dom_sf.",
        "DR   InterPro; IPR050679; Bact_HTH_transcr_reg.",
        "DR   InterPro; IPR004839; Aminotransferase_I/II_large.",
        "DR   InterPro; IPR051446; HTH_trans_reg/aminotransferase.",
        "DR   InterPro; IPR015424; PyrdxlP-dep_Trfase.",
        "DR   InterPro; IPR015421; PyrdxlP-dep_Trfase_major.",
        "DR   InterPro; IPR015422; PyrdxlP-dep_Trfase_small.",
        "DR   InterPro; IPR036388; WH-like_DNA-bd_sf.",
        "DR   InterPro; IPR036390; WH_DNA-bd_sf.",
        "DR   Pfam; PF00392; GntR; 1.",
        "DR   Pfam; PF07729; FCD; 1.",
        "DR   Pfam; PF07702; UTRA; 1.",
        "DR   Pfam; PF00155; Aminotran_1_2; 1.",
        "KW   Aminotransferase",
        "KW   DNA-binding",
        "KW   Pyridoxal phosphate",
        "KW   Transcription",
        "KW   Transcription regulation",
        "KW   Transferase",
    ):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "uniprot.txt"), line))
    return items


def asta_support_lines(gene: str) -> list[dict[str, str]]:
    path = gene_file(gene, "deep-research-asta.md")
    items: list[dict[str, str]] = []
    for needle in ("protein_description:", "**Protein Description:**", "- **Protein Description:**"):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "deep-research-asta.md"), line))
            break
    for needle in ("protein_family:", "- **Protein Family:**", "protein_domains:", "- **Key Domains:**"):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "deep-research-asta.md"), line))
    return items


def evidence_for(
    gene: str,
    go_id: str | None = None,
    evidence_type: str | None = None,
    reference_id: str | None = None,
) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if go_id:
        add_support(items, goa_support(gene, go_id, evidence_type=evidence_type, reference_id=reference_id))
    for item in uniprot_support_lines(gene):
        add_support(items, item)
    for item in asta_support_lines(gene):
        add_support(items, item)
    return items


def role_for(gene: str) -> str:
    if gene == "csiR":
        return "CsiR-named GntR/FadR-family DNA-binding transcription repressor candidate with unresolved direct regulon"
    if gene == "PP_3738":
        return "VanR-named GntR/FadR-family DNA-binding transcription regulator candidate with unresolved aromatic-acid regulon"
    if gene in UTRA_REGULATORS:
        return "UTRA-domain GntR/HutC-family DNA-binding transcription regulator candidate with unresolved effector and regulon"
    if gene in AMINOTRANSFERASE_DOMAIN_REGULATORS:
        return "GntR-family HTH regulator with PLP-dependent aminotransferase-like domain and unresolved substrate or regulon"
    return "FadR/GntR-family DNA-binding transcription regulator candidate with unresolved effector and regulon"


def description_for(gene: str) -> str:
    product = BATCH_ROWS[gene]["protein_name"]
    if gene == "csiR":
        return (
            "csiR encodes a named DNA-binding transcriptional repressor in Pseudomonas putida KT2440. Its GntR/FadR-family "
            "HTH and C-terminal domains support a cytosolic transcription-regulator role; the direct operator, ligand, "
            "and target regulon remain unresolved."
        )
    if gene == "PP_3738":
        return (
            "PP_3738 encodes a VanR-named GntR/FadR-family transcription regulator in Pseudomonas putida KT2440. The protein "
            "has HTH and FadR/GntR-family domain features consistent with DNA-binding transcription regulation, but the "
            "specific aromatic-acid or vanillate regulon is unresolved."
        )
    if gene in UTRA_REGULATORS:
        return (
            f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. Its HTH and UTRA-domain architecture "
            "supports a HutC/GntR-like DNA-binding transcription-regulator role; the effector ligand, target operator, "
            "and regulated pathway are unresolved."
        )
    if gene in AMINOTRANSFERASE_DOMAIN_REGULATORS:
        return (
            f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. The protein combines a GntR-family HTH "
            "region with a PLP-dependent aminotransferase-like domain, supporting transcription-regulator context plus "
            "cofactor-binding architecture; the direct regulon and any catalytic substrate remain unresolved."
        )
    return (
        f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. HTH and FadR/GntR-family C-terminal domain "
        "features support a DNA-binding transcription-regulator role, while the effector ligand, regulatory direction, "
        "and target regulon remain unresolved."
    )


def replacement(go_id: str) -> list[dict[str, str]]:
    return [TERM[go_id]]


def review_for(gene: str, annotation: dict[str, object]) -> dict[str, object]:
    term_obj = annotation.get("term", {})
    go_id = str(term_obj.get("id", "")) if isinstance(term_obj, dict) else ""
    label = str(term_obj.get("label", "")) if isinstance(term_obj, dict) else go_id
    evidence_type = str(annotation.get("evidence_type", ""))
    reference_id = str(annotation.get("original_reference_id", ""))
    evidence = evidence_for(gene, go_id, evidence_type=evidence_type, reference_id=reference_id)

    if go_id == "GO:0003700":
        return {
            "summary": "DNA-binding transcription factor activity is the appropriate shared first-pass molecular function.",
            "action": "ACCEPT",
            "reason": (
                "The product name, HTH-domain context, and GntR/FadR or UTRA/aminotransferase-domain family evidence support "
                f"a DNA-binding transcription-regulator role. The direct regulon is not resolved: {role_for(gene)}."
            ),
            "supported_by": evidence,
        }

    if go_id == "GO:0003677":
        return {
            "summary": "Generic DNA binding is true but less informative than transcription-regulator activity.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": (
                "The supported role is not generic DNA binding; these records are GntR-family HTH transcription regulators. "
                "GO:0003700 is the more informative molecular-function term."
            ),
            "proposed_replacement_terms": replacement("GO:0003700"),
            "supported_by": evidence,
        }

    if go_id == "GO:0006351":
        return {
            "summary": "DNA-templated transcription is a broad parent process for a transcription regulator.",
            "action": "MODIFY",
            "reason": (
                "The gene product regulates transcription rather than forming the basal transcription machinery. Regulation "
                "of DNA-templated transcription is the appropriate process-level term."
            ),
            "proposed_replacement_terms": replacement("GO:0006355"),
            "supported_by": evidence,
        }

    if go_id == "GO:0006355":
        return {
            "summary": "Regulation of DNA-templated transcription is appropriate broad process context.",
            "action": "ACCEPT",
            "reason": (
                "The GntR-family HTH context supports transcription regulation while the direct operator, effector, and "
                "regulated genes remain unresolved."
            ),
            "supported_by": evidence,
        }

    if go_id == "GO:0045892":
        return {
            "summary": "Negative regulation of transcription is plausible but kept non-core pending gene-specific regulon evidence.",
            "action": "KEEP_AS_NON_CORE",
            "reason": (
                "Many GntR-family proteins are repressors, but this first-pass evidence does not identify the direct target "
                "operator or confirm the regulatory direction for this KT2440 paralog."
            ),
            "supported_by": evidence,
        }

    if go_id == "GO:0030170":
        return {
            "summary": "Pyridoxal phosphate binding is retained as non-core domain/cofactor context.",
            "action": "KEEP_AS_NON_CORE",
            "reason": (
                "The PLP-dependent aminotransferase-like domain is real family context, but the primary curated role for this "
                "module is DNA-binding transcription regulation. Substrate chemistry remains unresolved."
            ),
            "supported_by": evidence,
        }

    return {
        "summary": f"{label} is retained as compatible non-core context.",
        "action": "KEEP_AS_NON_CORE",
        "reason": f"The supported first-pass role is {role_for(gene)}.",
        "supported_by": evidence,
    }


def references_for(gene: str, data: dict[str, object]) -> list[dict[str, object]]:
    refs: list[dict[str, object]] = []
    seen: set[str] = set()
    for ref in data.get("references", []):
        if isinstance(ref, dict) and ref.get("id"):
            refs.append(ref)
            seen.add(str(ref["id"]))
    additions: list[dict[str, object]] = [
        {
            "id": file_id(gene, "goa.tsv"),
            "title": f"QuickGO GOA annotations for {gene} ({BATCH_ROWS[gene]['uniprot_accession']})",
            "findings": [{"supporting_text": line} for line in goa_lines(gene)],
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
            seen.add(str(ref["id"]))
    return refs


def core_functions_for(gene: str) -> list[dict[str, object]]:
    core: dict[str, object] = {
        "description": role_for(gene),
        "molecular_function": TERM["GO:0003700"],
        "supported_by": evidence_for(gene, "GO:0003700"),
    }
    add_support(core["supported_by"], goa_support(gene, "GO:0003677"))  # type: ignore[arg-type]
    if "GO:0006355" in goa_ids(gene):
        core["directly_involved_in"] = [TERM["GO:0006355"]]
        add_support(core["supported_by"], goa_support(gene, "GO:0006355"))  # type: ignore[arg-type]
    return [core]


def suggested_questions(gene: str) -> list[dict[str, object]]:
    if gene in AMINOTRANSFERASE_DOMAIN_REGULATORS:
        question = (
            f"Does the PLP-dependent aminotransferase-like domain in {gene} retain catalytic activity, bind an effector, "
            "or function mainly as a regulatory sensory domain?"
        )
    elif gene == "PP_3738":
        question = "Does PP_3738 directly regulate vanillate/aromatic-acid catabolism genes in KT2440?"
    else:
        question = f"What direct operator, effector ligand, and target regulon define {gene} in KT2440?"
    return [{"question": question, "experts": []}]


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    if gene in AMINOTRANSFERASE_DOMAIN_REGULATORS:
        description = (
            f"Map {gene}-dependent transcription changes and promoter binding, then test purified protein for PLP binding "
            "and candidate aminotransferase substrates."
        )
    else:
        description = (
            f"Map {gene}-dependent transcription changes and promoter binding under candidate carbon, amino-acid, or "
            "aromatic-acid effector conditions."
        )
    return [{"experiment_type": "regulatory network mapping", "description": description}]


def write_notes(gene: str) -> None:
    path = gene_file(gene, "notes.md")
    heading = f"## {TODAY} GntR-family regulator first pass"
    evidence = evidence_for(gene, "GO:0003700")
    lines_out = [
        heading,
        "",
        f"- Batch: `{BATCH_TSV.relative_to(ROOT)}`.",
        f"- Main conclusion: {role_for(gene)}.",
        "- Decision: keep DNA-binding transcription factor activity as the core molecular function; regulon, effector, and direction remain unresolved unless already represented by broad GOA context.",
    ]
    if gene in AMINOTRANSFERASE_DOMAIN_REGULATORS:
        lines_out.append("- PLP binding and aminotransferase-like architecture are retained as non-core context pending substrate evidence.")
    if gene == "PP_3738":
        lines_out.append("- VanR product name is retained as a naming clue, not as proof of a specific vanillate/aromatic-acid regulon.")
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


def curate_gene(gene: str) -> None:
    path = gene_file(gene, "ai-review.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    data["status"] = "DRAFT"
    data["description"] = description_for(gene)
    data["references"] = references_for(gene, data)
    for annotation in data.get("existing_annotations", []):
        if isinstance(annotation, dict):
            annotation["review"] = review_for(gene, annotation)
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


def clean_id(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_]+", "_", value.lower())
    return re.sub(r"_+", "_", cleaned).strip("_")


def module_term(go_id: str, description: str | None = None) -> dict[str, object]:
    out: dict[str, object] = {"preferred_term": TERM[go_id]["label"], "term": TERM[go_id]}
    if description:
        out["description"] = description
    return out


def annoton(gene: str) -> dict[str, object]:
    role = role_for(gene)
    out: dict[str, object] = {
        "id": f"{clean_id(gene)}_{clean_id(role)}",
        "label": f"{gene}: {role}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": role,
        "function": {"preferred_term": TERM["GO:0003700"]["label"], "term": TERM["GO:0003700"]},
        "notes": "Target regulon, effector ligand, and regulatory direction remain unresolved in this first-pass boundary module.",
    }
    if "GO:0006355" in goa_ids(gene) or "GO:0045892" in goa_ids(gene):
        out["processes"] = [{"preferred_term": TERM["GO:0006355"]["label"], "term": TERM["GO:0006355"]}]
    if gene in AMINOTRANSFERASE_DOMAIN_REGULATORS:
        out["notes"] = (
            "PLP-dependent aminotransferase-like domain retained as non-core context; substrate chemistry and regulon remain unresolved."
        )
    if gene == "PP_3738":
        out["notes"] = "VanR product name retained as context; aromatic-acid or vanillate regulon remains unresolved."
    return out


def part(part_id: str, label: str, genes: list[str], description: str) -> dict[str, object]:
    return {
        "order": len(PARTS) + 1,
        "role": label,
        "node": {
            "id": part_id,
            "label": label,
            "module_type": "BIOLOGICAL_PROCESS",
            "description": description,
            "annotons": [annoton(gene) for gene in genes],
        },
    }


PARTS: list[dict[str, object]] = []


def build_module() -> None:
    PARTS.clear()
    PARTS.append(
        part(
            "fadR_gntr_family_regulators",
            "FadR/GntR-family regulator candidates",
            [gene for gene in GENES if gene in FADR_GNTR_REGULATORS],
            "GntR-family HTH regulators with FadR/GntR C-terminal domains, including named CsiR and VanR candidates.",
        )
    )
    PARTS.append(
        part(
            "utra_hutc_gntr_family_regulators",
            "UTRA/HutC-like GntR regulator candidates",
            [gene for gene in GENES if gene in UTRA_REGULATORS],
            "GntR-family HTH regulators with UTRA-like effector-binding domains and unresolved ligands/regulons.",
        )
    )
    PARTS.append(
        part(
            "plp_aminotransferase_domain_gntr_regulators",
            "PLP/aminotransferase-domain GntR regulator candidates",
            [gene for gene in GENES if gene in AMINOTRANSFERASE_DOMAIN_REGULATORS],
            "GntR-family HTH regulators fused to PLP-dependent aminotransferase-like domains; substrate chemistry is unresolved.",
        )
    )
    data: dict[str, object] = {
        "id": "MODULE:gntr_transcriptional_regulator_boundary",
        "title": "GntR-family transcriptional regulator boundary",
        "description": (
            "Boundary module for PSEPK GntR-family transcriptional regulators from the broad regulation/signal-transduction "
            "functional bucket. It separates FadR/GntR C-terminal, UTRA/HutC-like, and PLP/aminotransferase-domain GntR "
            "regulators while leaving target regulons and effector ligands unresolved."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_TSV.relative_to(ROOT)}",
                "title": "PSEPK regulation/signal-transduction GntR-family split",
                "statement": "The batch table records 29 GntR-family transcriptional regulators curated in this first pass.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_regulation_signal_transduction_partition.tsv",
                "title": "PSEPK regulation/signal-transduction partition table",
                "statement": "The regulation umbrella was partitioned into family-scale transcription-regulator and signaling splits.",
            },
        ]
        + [
            {
                "source_id": file_id(gene, "ai-review.yaml"),
                "title": f"Curated {gene} review",
                "statement": role_for(gene),
            }
            for gene in GENES
        ],
        "module": {
            "id": "gntr_transcriptional_regulator_boundary",
            "label": "GntR-family transcriptional regulator boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                module_term("GO:0003700", "Shared molecular function for GntR-family HTH transcription-regulator candidates."),
                module_term("GO:0006355", "Broad process context for regulator candidates with unresolved direct regulons."),
                module_term("GO:0045892", "Direction-specific repressor context kept non-core where only family-level evidence supports it."),
                module_term("GO:0030170", "PLP cofactor-binding context for aminotransferase-domain GntR regulators."),
            ],
            "context": {
                "cellular_components": [
                    module_term("GO:0005829", "Expected soluble bacterial regulator localization when cytosol is asserted.")
                ]
            },
            "parts": PARTS,
        },
    }
    MODULE_PATH.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120, allow_unicode=False),
        encoding="utf-8",
    )
    print(f"Wrote {MODULE_PATH.relative_to(ROOT)}")


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
    build_module()


if __name__ == "__main__":
    main()
