#!/usr/bin/env python3
"""First-pass curation for low-information or named transcription regulators."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_DIR = ROOT / "projects" / "P_PUTIDA" / "batches"
BATCH_TSV = BATCH_DIR / "module_regulation_signal_transduction_low_information_or_named_transcriptional_regulators.tsv"
MODULE_PATH = ROOT / "modules" / "transcriptional_regulator_spillover_boundary.yaml"
TODAY = "2026-07-10"

EXISTING_CURATED = {"hexR"}

NEW_REPRESSOR = {"PP_0357", "nrdR", "PP_1236", "PP_3033", "paaX", "hmgR"}
NEW_DNA_BINDING_TF = {
    "PP_0017",
    "PP_0537",
    "PP_1057",
    "PP_1366",
    "PP_2816",
    "PP_2947",
    "PP_3510",
    "PP_3693",
    "PP_4133",
    "PP_4470",
    "PP_5527",
    "PP_5545",
    "PP_5611",
}
NO_CORE = {"PP_1762", "PP_2738", "PP_4528", "PP_5232", "PP_5343"}

HNS_MVAT = {"PP_0017", "PP_1366", "PP_2947", "PP_3693"}
GCVR = {"PP_0357", "PP_1236"}
PHAGE_LIKE = {"PP_0274", "PP_0537", "PP_3033", "PP_4133", "PP_5527", "PP_5545"}
NAMED = {"nrdR", "hexR", "mraZ", "ohrR", "nfxB", "paaX", "hmgR", "sahR"}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


TERM = {
    "GO:0000976": term("GO:0000976", "transcription cis-regulatory region binding"),
    "GO:0001046": term("GO:0001046", "core promoter sequence-specific DNA binding"),
    "GO:0001217": term("GO:0001217", "DNA-binding transcription repressor activity"),
    "GO:0003677": term("GO:0003677", "DNA binding"),
    "GO:0003700": term("GO:0003700", "DNA-binding transcription factor activity"),
    "GO:0003712": term("GO:0003712", "transcription coregulator activity"),
    "GO:0005524": term("GO:0005524", "ATP binding"),
    "GO:0005737": term("GO:0005737", "cytoplasm"),
    "GO:0006351": term("GO:0006351", "DNA-templated transcription"),
    "GO:0006355": term("GO:0006355", "regulation of DNA-templated transcription"),
    "GO:0006950": term("GO:0006950", "response to stress"),
    "GO:0008168": term("GO:0008168", "methyltransferase activity"),
    "GO:0008270": term("GO:0008270", "zinc ion binding"),
    "GO:0008757": term("GO:0008757", "S-adenosylmethionine-dependent methyltransferase activity"),
    "GO:0009295": term("GO:0009295", "nucleoid"),
    "GO:0032993": term("GO:0032993", "protein-DNA complex"),
    "GO:0045892": term("GO:0045892", "negative regulation of DNA-templated transcription"),
    "GO:0097367": term("GO:0097367", "carbohydrate derivative binding"),
    "GO:1901135": term("GO:1901135", "carbohydrate derivative metabolic process"),
    "GO:2000143": term("GO:2000143", "positive regulation of DNA-templated transcription initiation"),
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
    for line in lines(path):
        if (
            line.startswith("DR   InterPro;")
            or line.startswith("DR   Pfam;")
            or line.startswith("DR   NCBIfam;")
            or line.startswith("DR   CDD;")
            or line.startswith("FT   DOMAIN")
            or line.startswith("FT                   /note=")
            or line.startswith("CC   -!- FUNCTION:")
            or line.startswith("KW   DNA-binding")
            or line.startswith("KW   Transcription")
            or line.startswith("KW   Transcription regulation")
            or line.startswith("KW   Repressor")
            or line.startswith("KW   Activator")
        ):
            add_support(items, support(file_id(gene, "uniprot.txt"), line.strip()))
        if len(items) >= 14:
            break
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
    if gene == "hexR":
        return "experimentally supported HexR glucose-catabolism transcriptional repressor"
    if gene in GCVR:
        return "GcvR-like glycine-cleavage transcriptional repressor candidate"
    if gene == "nrdR":
        return "NrdR-family ribonucleotide-reductase transcriptional repressor candidate"
    if gene == "mraZ":
        return "MraZ-family cell-division operon transcriptional regulator candidate"
    if gene == "ohrR":
        return "OhrR/MarR-like organic-hydroperoxide stress transcriptional regulator candidate"
    if gene in {"PP_2816", "nfxB"}:
        return "NfxB/TetR-like transcriptional regulator candidate with unresolved efflux or stress regulon"
    if gene == "paaX":
        return "PaaX phenylacetyl-CoA-responsive transcriptional repressor candidate"
    if gene == "hmgR":
        return "HmgR homogentisate-pathway transcriptional repressor candidate"
    if gene == "sahR":
        return "SahR methionine-metabolism transcriptional regulator candidate with methyltransferase-domain side context"
    if gene in HNS_MVAT:
        return "MvaT/H-NS-like transcriptional regulator candidate with unresolved target loci"
    if gene in PHAGE_LIKE:
        return "phage, antitoxin, or Cro/C1-like DNA-binding transcriptional regulator candidate with unresolved target context"
    if gene == "PP_1057":
        return "PadR-family DNA-binding transcriptional regulator candidate with unresolved ligand and regulon"
    if gene == "PP_3539":
        return "MerR-family DNA-binding transcriptional regulator candidate with unresolved ligand and regulon"
    if gene == "PP_4470":
        return "Arc-domain ribbon-helix-helix DNA-binding transcriptional regulator candidate"
    if gene == "PP_5611":
        return "CapW/WYL-domain transcriptional regulator candidate with unresolved CBASS or defense-associated context"
    if gene in NO_CORE:
        return "low-information transcription-regulator-associated candidate with unresolved molecular function"
    return "DNA-binding transcriptional regulator candidate with unresolved target regulon"


def description_for(gene: str) -> str:
    product = BATCH_ROWS[gene]["protein_name"]
    if gene in NO_CORE:
        return (
            f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. The fetched UniProt and Asta context "
            "does not resolve a specific DNA-binding, catalytic, RNA-polymerase-binding, effector, or pathway role, so the "
            "protein remains a low-information regulator-associated candidate."
        )
    if gene == "sahR":
        return (
            "sahR encodes a predicted transcriptional regulator of methionine metabolism in Pseudomonas putida KT2440. "
            "The protein has an ArsR-like DNA-binding region and SAM-dependent methyltransferase-domain context; the "
            "regulatory target, effector, and catalytic relevance of the methyltransferase-like domain remain unresolved."
        )
    if gene == "hexR":
        return "HexR is a curated glucose-catabolism transcriptional repressor retained as an anchor for this regulator spillover split."
    return (
        f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. UniProt, GOA where present, and Asta retrieval "
        f"support a {role_for(gene)}, while direct operator sites, effector ligands, and complete target regulons remain unresolved."
    )


def core_term_for(gene: str) -> dict[str, str] | None:
    if gene in NO_CORE:
        return None
    if gene in NEW_REPRESSOR:
        return TERM["GO:0001217"]
    if gene == "PP_0274":
        return TERM["GO:0001046"]
    if "GO:0001217" in goa_ids(gene):
        return TERM["GO:0001217"]
    if "GO:0003700" in goa_ids(gene) or gene in NEW_DNA_BINDING_TF:
        return TERM["GO:0003700"]
    if "GO:0000976" in goa_ids(gene):
        return TERM["GO:0000976"]
    if "GO:0001046" in goa_ids(gene):
        return TERM["GO:0001046"]
    return None


def replacement(go_id: str) -> list[dict[str, str]]:
    return [TERM[go_id]]


def review_for(gene: str, annotation: dict[str, object]) -> dict[str, object]:
    term_obj = annotation.get("term", {})
    go_id = str(term_obj.get("id", "")) if isinstance(term_obj, dict) else ""
    label = str(term_obj.get("label", "")) if isinstance(term_obj, dict) else go_id
    evidence_type = str(annotation.get("evidence_type", ""))
    reference_id = str(annotation.get("original_reference_id", ""))
    evidence = evidence_for(gene, go_id, evidence_type=evidence_type, reference_id=reference_id)
    core_term = core_term_for(gene)

    if go_id in {"GO:0003700", "GO:0001217", "GO:0001046", "GO:0000976"}:
        return {
            "summary": f"{label} is supported for this regulator candidate.",
            "action": "ACCEPT",
            "reason": f"The product name, domain architecture, and fetched annotation context support the role: {role_for(gene)}.",
            "supported_by": evidence,
        }

    if go_id == "GO:0003677":
        replacements = [core_term] if core_term else [TERM["GO:0003700"]]
        return {
            "summary": "Generic DNA binding is true but less informative than a transcription-regulator molecular function.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": (
                "The evidence points to regulatory DNA binding rather than generic DNA binding. A transcription-regulator "
                "molecular-function term better captures the supported role."
            ),
            "proposed_replacement_terms": replacements,
            "supported_by": evidence,
        }

    if go_id == "GO:0006351":
        return {
            "summary": "DNA-templated transcription is a broad parent process for a transcription regulator.",
            "action": "MODIFY",
            "reason": (
                "These proteins regulate transcription rather than serving as basal transcription machinery. Regulation of "
                "DNA-templated transcription is the appropriate process-level term where a process term is needed."
            ),
            "proposed_replacement_terms": replacement("GO:0006355"),
            "supported_by": evidence,
        }

    if go_id == "GO:0006355":
        return {
            "summary": "Regulation of DNA-templated transcription is appropriate broad process context.",
            "action": "ACCEPT",
            "reason": "The product and domain evidence support transcriptional regulation while the direct regulon remains unresolved.",
            "supported_by": evidence,
        }

    if go_id == "GO:0045892":
        return {
            "summary": "Negative regulation of DNA-templated transcription is compatible with the repressor-family context.",
            "action": "ACCEPT",
            "reason": "The fetched product or family context supports a transcriptional repressor role; target operons remain unresolved unless curated separately.",
            "supported_by": evidence,
        }

    if go_id in {"GO:0005524", "GO:0008270", "GO:0005737", "GO:0006950", "GO:0008168", "GO:0008757", "GO:0009295", "GO:0032993", "GO:0097367", "GO:2000143"}:
        return {
            "summary": f"{label} is retained as non-core domain, localization, effector, complex, or broad process context.",
            "action": "KEEP_AS_NON_CORE",
            "reason": f"The primary supported role in this split is {role_for(gene)}; this annotation is compatible but not the core function.",
            "supported_by": evidence,
        }

    if go_id == "GO:1901135":
        return {
            "summary": "Carbohydrate derivative metabolic process is likely over-propagated for a regulator.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": "Regulator-domain or effector-binding context should not be interpreted as direct carbohydrate metabolism by the gene product.",
            "supported_by": evidence,
        }

    return {
        "summary": f"{label} is retained as compatible non-core context.",
        "action": "KEEP_AS_NON_CORE",
        "reason": f"The supported role is {role_for(gene)}.",
        "supported_by": evidence,
    }


def new_annotation(gene: str, term_obj: dict[str, str]) -> dict[str, object]:
    if term_obj["id"] == "GO:0001217":
        summary = "DNA-binding transcription repressor activity is a missing precise molecular-function annotation."
        reason = "The product/family context identifies this protein as a DNA-binding transcriptional repressor candidate."
    else:
        summary = "DNA-binding transcription factor activity is a missing molecular-function annotation."
        reason = "The product and DNA-binding regulator domain context support a transcription-regulator molecular function."
    return {
        "term": term_obj,
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": "enables",
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": f"{reason} Direct operator, effector, regulon, and regulatory direction remain unresolved.",
            "supported_by": evidence_for(gene, term_obj["id"]),
        },
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
    core_term = core_term_for(gene)
    if not core_term:
        return []
    core: dict[str, object] = {
        "description": role_for(gene),
        "molecular_function": core_term,
        "supported_by": evidence_for(gene, core_term["id"]),
    }
    if "GO:0045892" in goa_ids(gene):
        core["directly_involved_in"] = [TERM["GO:0045892"]]
        add_support(core["supported_by"], goa_support(gene, "GO:0045892"))  # type: ignore[arg-type]
    elif "GO:0006355" in goa_ids(gene):
        core["directly_involved_in"] = [TERM["GO:0006355"]]
        add_support(core["supported_by"], goa_support(gene, "GO:0006355"))  # type: ignore[arg-type]
    return [core]


def suggested_questions(gene: str) -> list[dict[str, object]]:
    if gene in NO_CORE:
        question = f"What molecular function, if any, is supported for the low-information regulator-associated protein {gene}?"
    elif gene == "sahR":
        question = "Does SahR have catalytic methyltransferase activity, or is the SAM-dependent methyltransferase-like domain regulatory or inactive?"
    elif gene in NAMED:
        question = f"What direct operator, effector, and regulon define {gene} in Pseudomonas putida KT2440?"
    else:
        question = f"What direct target genes, effector ligand, and regulatory direction define {gene}?"
    return [{"question": question, "experts": []}]


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    if gene in NO_CORE:
        description = f"Test {gene} expression and protein-DNA/RNA-polymerase binding under candidate stress, metabolic, or prophage-inducing conditions."
    else:
        description = f"Map {gene}-dependent transcription changes and direct promoter binding under candidate metabolic, stress, or prophage-inducing conditions."
    return [{"experiment_type": "regulatory network mapping", "description": description}]


def write_notes(gene: str) -> None:
    path = gene_file(gene, "notes.md")
    heading = f"## {TODAY} low-information transcription-regulator split"
    evidence = evidence_for(gene, (core_term_for(gene) or {}).get("id"))
    lines_out = [
        heading,
        "",
        f"- Batch: `{BATCH_TSV.relative_to(ROOT)}`.",
        f"- Main conclusion: {role_for(gene)}.",
    ]
    if gene in NO_CORE:
        lines_out.append("- Decision: leave without an assigned core GO function pending stronger DNA-binding, catalytic, or regulatory evidence.")
    else:
        lines_out.append("- Decision: keep or add a conservative transcription-regulator molecular function; avoid inferring a specific target regulon from the product name alone.")
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
    annotations = [ann for ann in data.get("existing_annotations", []) if not (isinstance(ann, dict) and ann.get("review", {}).get("action") == "NEW")]
    for annotation in annotations:
        if isinstance(annotation, dict):
            annotation["review"] = review_for(gene, annotation)
    existing_ids = {ann.get("term", {}).get("id") for ann in annotations if isinstance(ann, dict)}
    core_term = core_term_for(gene)
    if core_term and core_term["id"] not in existing_ids:
        annotations.append(new_annotation(gene, core_term))
    data["existing_annotations"] = annotations
    data["core_functions"] = core_functions_for(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_questions(gene)
    data["suggested_experiments"] = suggested_experiments(gene)
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120, allow_unicode=False), encoding="utf-8")
    write_notes(gene)
    print(f"Curated {path.relative_to(ROOT)}")


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.casefold()).strip("_")


def module_annoton(gene: str) -> dict[str, object]:
    core_term = core_term_for(gene)
    annoton: dict[str, object] = {
        "id": f"{slug(gene)}_{slug(role_for(gene))}",
        "label": f"{gene}: {role_for(gene)}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": role_for(gene),
        "notes": "Direct operator, effector ligand, and full target regulon remain unresolved unless separately curated.",
    }
    if core_term:
        annoton["function"] = {"preferred_term": core_term["label"], "term": core_term}
    if "GO:0045892" in goa_ids(gene):
        annoton["processes"] = [{"preferred_term": TERM["GO:0045892"]["label"], "term": TERM["GO:0045892"]}]
    elif "GO:0006355" in goa_ids(gene):
        annoton["processes"] = [{"preferred_term": TERM["GO:0006355"]["label"], "term": TERM["GO:0006355"]}]
    if gene in NO_CORE:
        annoton["notes"] = "Molecular function and target context remain unresolved; retained as a low-information regulator-associated spillover."
    if gene == "sahR":
        annoton["notes"] = "SAM-dependent methyltransferase-domain context is retained as non-core until catalytic relevance is shown."
    return annoton


def module_part(order: int, role: str, node_id: str, description: str, genes: list[str]) -> dict[str, object]:
    return {
        "order": order,
        "role": role,
        "node": {
            "id": node_id,
            "label": role,
            "module_type": "BIOLOGICAL_PROCESS",
            "description": description,
            "annotons": [module_annoton(gene) for gene in genes],
        },
    }


def write_module() -> None:
    parts = [
        module_part(1, "Curated named metabolic regulator anchor", "curated_named_anchor", "Existing curated HexR review retained as a well-supported anchor.", ["hexR"]),
        module_part(2, "Named metabolic, stress, and cell-cycle regulator candidates", "named_metabolic_stress_regulators", "Named regulators where product/family context suggests a biological regulon but direct KT2440 target evidence remains incomplete.", ["PP_0357", "nrdR", "PP_1236", "mraZ", "ohrR", "nfxB", "paaX", "hmgR", "sahR"]),
        module_part(3, "MvaT/H-NS-like and compact DNA-binding regulator candidates", "compact_dna_binding_regulators", "MvaT/H-NS-like, MarR/PadR/NfxB, Fis, MerR, Arc, and WYL/CapW-associated candidates curated only to conservative regulator functions.", ["PP_0017", "PP_0175", "PP_1057", "PP_1366", "PP_2816", "PP_2947", "PP_3510", "PP_3539", "PP_3693", "PP_4470", "PP_5611"]),
        module_part(4, "Phage, antitoxin, and Cro/C1-like regulator candidates", "phage_antitoxin_cro_like_regulators", "Phage-like and antitoxin-like DNA-binding regulator candidates retained here rather than forced into a specific phage pathway.", ["PP_0274", "PP_0537", "PP_3033", "PP_4133", "PP_5527", "PP_5545"]),
        module_part(5, "Low-information noncanonical regulator-associated candidates", "low_information_noncanonical_candidates", "Product-name-only or noncanonical domain records that do not yet justify a core molecular function.", ["PP_1762", "PP_2738", "PP_4528", "PP_5232", "PP_5343"]),
    ]
    module = {
        "id": "MODULE:transcriptional_regulator_spillover_boundary",
        "title": "Transcriptional regulator spillover boundary",
        "description": (
            "Boundary module for PSEPK low-information or named transcription-regulator-associated proteins from the broad "
            "regulation/signal-transduction functional bucket. It preserves curated HexR context, separates named regulator "
            "candidates and phage-like spillovers, and leaves direct regulons, effector ligands, and weak noncanonical entries unresolved."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_TSV.relative_to(ROOT)}",
                "title": "PSEPK regulation/signal-transduction low-information regulator split",
                "statement": "The batch table records 32 low-information or named transcription-regulator-associated proteins represented in this boundary module.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_regulation_signal_transduction_partition.tsv",
                "title": "PSEPK regulation/signal-transduction partition table",
                "statement": "The regulation umbrella was partitioned into family-scale transcription-regulator and signaling splits.",
            },
        ]
        + [{"source_id": file_id(gene, "ai-review.yaml"), "title": f"Curated {gene} review", "statement": role_for(gene)} for gene in GENES],
        "module": {
            "id": "transcriptional_regulator_spillover_boundary",
            "label": "Transcriptional regulator spillover boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {"preferred_term": TERM["GO:0003700"]["label"], "term": TERM["GO:0003700"], "description": "Generic DNA-binding transcription-regulator function for supported candidates."},
                {"preferred_term": TERM["GO:0001217"]["label"], "term": TERM["GO:0001217"], "description": "Repressor-specific molecular function for named or family-supported repressors."},
                {"preferred_term": TERM["GO:0001046"]["label"], "term": TERM["GO:0001046"], "description": "Core-promoter DNA-binding context for HigA-like candidates where GOA uses this term."},
                {"preferred_term": TERM["GO:0006355"]["label"], "term": TERM["GO:0006355"], "description": "Broad transcription-regulation process context."},
                {"preferred_term": TERM["GO:0045892"]["label"], "term": TERM["GO:0045892"], "description": "Negative transcription-regulation process context for repressor candidates."},
                {"preferred_term": TERM["GO:0008757"]["label"], "term": TERM["GO:0008757"], "description": "Non-core methyltransferase-domain context for SahR."},
            ],
            "parts": parts,
        },
    }
    MODULE_PATH.write_text(yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, width=120, allow_unicode=False), encoding="utf-8")
    print(f"Wrote {MODULE_PATH.relative_to(ROOT)}")


def main() -> None:
    for gene in GENES:
        if gene in EXISTING_CURATED:
            print(f"Preserved existing curated review for {gene}")
            continue
        curate_gene(gene)
    write_module()


if __name__ == "__main__":
    main()
