#!/usr/bin/env python3
"""First-pass curation for XRE/Cro phage and toxin-antitoxin regulators."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_DIR = ROOT / "projects" / "P_PUTIDA" / "batches"
BATCH_TSV = BATCH_DIR / "module_regulation_signal_transduction_xre_cro_phage_toxin_antitoxin_regulators.tsv"
PARTITION_TSV = BATCH_DIR / "module_regulation_signal_transduction_partition.tsv"
MODULE_PATH = ROOT / "modules" / "phage_regulation_toxin_antitoxin_boundary.yaml"
TODAY = "2026-07-10"


MOBILE_EXISTING = ["PP_2500", "PP_5558", "PP_5626"]
HIGA_MQSA = {"PP_0276", "PP_1198", "mqsA"}
MQSR = {"mqsR"}
LEXA_LIKE = {"PP_1549", "PP_3896", "PP_4068"}
CUPIN_CRO = {"PP_2177", "PP_2181", "PP_2232", "PP_2245", "PP_2256", "PP_2868", "PP_2884", "PP_3125", "puuR"}
SIMPLE_CRO = {"PP_0497", "PP_1550", "PP_1716", "PP_1935", "PP_2653", "PP_4100", "PP_5618"}
SPILLOVERS = {"PP_0852", "PP_2815", "PP_3177", "PP_4468"}
UNRESOLVED_NO_CORE = {"PP_5680"}


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
    "GO:0009372": term("GO:0009372", "quorum sensing"),
    "GO:0017148": term("GO:0017148", "negative regulation of translation"),
    "GO:0044010": term("GO:0044010", "single-species biofilm formation"),
    "GO:0090729": term("GO:0090729", "toxin activity"),
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
        "CC   -!- SIMILARITY:",
        "DR   InterPro; IPR001387; Cro/C1-type_HTH.",
        "DR   InterPro; IPR039554; HigA2-like_HTH.",
        "DR   InterPro; IPR052359; HTH-type_reg/antitoxin.",
        "DR   InterPro; IPR010982; Lambda_DNA-bd_dom_sf.",
        "DR   InterPro; IPR039418; LexA-like.",
        "DR   InterPro; IPR036286; LexA/Signal_pep-like_sf.",
        "DR   InterPro; IPR015927; Peptidase_S24_S26A/B/C.",
        "DR   InterPro; IPR013096; Cupin_2.",
        "DR   InterPro; IPR014710; RmlC-like_jellyroll.",
        "DR   InterPro; IPR011051; RmlC_Cupin_sf.",
        "DR   InterPro; IPR050807; TransReg_Diox_bact_type.",
        "DR   InterPro; IPR041413; MLTR_LBD.",
        "DR   InterPro; IPR050400; Bact_Cytoskel_RodZ.",
        "DR   InterPro; IPR025194; RodZ-like_C.",
        "DR   InterPro; IPR051448; CdaR-like_regulators.",
        "DR   InterPro; IPR041522; CdaR_GGDEF.",
        "DR   InterPro; IPR008599; Diacid_rec.",
        "DR   InterPro; IPR025736; PucR_C-HTH_dom.",
        "DR   InterPro; IPR042070; PucR_C-HTH_sf.",
        "DR   InterPro; IPR022452; MqsA.",
        "DR   InterPro; IPR032758; MqsA/HigA-2.",
        "DR   InterPro; IPR022453; Znf_MqsA-type.",
        "DR   InterPro; IPR038493; MqsR_sf.",
        "DR   InterPro; IPR031451; MqsR_toxin.",
        "DR   InterPro; IPR016032; Sig_transdc_resp-reg_C-effctor.",
        "DR   InterPro; IPR000792; Tscrpt_reg_LuxR_C.",
        "DR   Pfam; PF01381; HTH_3; 1.",
        "DR   Pfam; PF00717; Peptidase_S24; 1.",
        "DR   Pfam; PF07883; Cupin_2; 1.",
        "DR   Pfam; PF15731; MqsA_antitoxin; 1.",
        "DR   Pfam; PF15723; MqsR_toxin; 1.",
        "FT   DOMAIN",
        "KW   DNA-binding",
        "KW   Hydrolase",
        "KW   Transcription",
        "KW   Transcription regulation",
        "KW   Membrane",
        "KW   Transmembrane",
    ):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "uniprot.txt"), line))
    return items


def asta_support_lines(gene: str) -> list[dict[str, str]]:
    path = gene_file(gene, "deep-research-asta.md")
    items: list[dict[str, str]] = []
    for needle in ("protein_description:", "**Protein Description:**"):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "deep-research-asta.md"), line))
            break
    for needle in ("protein_family:", "**Protein Family:**", "protein_domains:", "**Key Domains:**"):
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
    if gene in MQSR:
        return "MqsR-family type II toxin candidate with mRNA-interferase and translation-inhibition context"
    if gene == "mqsA":
        return "MqsA-family type II antitoxin and DNA-binding transcription repressor candidate"
    if gene == "PP_1198":
        return "HigA-like Cro/C1-family antitoxin transcription regulator candidate"
    if gene == "PP_0276":
        return "HigA2-like Cro/C1-family DNA-binding transcription regulator candidate"
    if gene in LEXA_LIKE:
        return "LexA-like Cro/C1-family DNA-binding transcription regulator candidate"
    if gene in CUPIN_CRO:
        if gene == "puuR":
            return "PuuR putrescine-associated Cro/C1-cupin transcription repressor candidate"
        return "Cro/C1-cupin DNA-binding transcription regulator candidate with unresolved metabolic or mobile-element context"
    if gene in SIMPLE_CRO:
        return "Cro/C1-family DNA-binding transcription regulator candidate with unresolved mobile-element context"
    if gene == "PP_0852":
        return "RodZ-like membrane-associated Cro/C1 HTH regulator candidate outside phage-specific biology"
    if gene in {"PP_2815", "PP_3177"}:
        return "CdaR/PucR-family DNA-binding transcription regulator candidate outside phage-specific biology"
    if gene == "PP_4468":
        return "LuxR/GerE-like DNA-binding transcription regulator candidate outside phage-specific biology"
    return "product-name-only Cro/CI transcription regulator candidate with unresolved domain support"


def description_for(gene: str) -> str:
    product = BATCH_ROWS[gene]["protein_name"]
    if gene in MQSR:
        return (
            f"{gene} encodes a predicted MqsR-family type II toxin in Pseudomonas putida KT2440. UniProt and Asta context "
            "support an MqsR toxin-family protein with mRNA-interferase wording, while current GOA rows focus on downstream "
            "translation, biofilm, and quorum-sensing process context. This first pass records toxin activity as the core "
            "molecular-function-level call and avoids asserting a specific KT2440 physiological phenotype."
        )
    if gene in HIGA_MQSA:
        return (
            f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. The local UniProt and Asta records support "
            "a Cro/C1-type HTH regulator with antitoxin-family context where present. This first pass curates a generic "
            "DNA-binding transcription-regulator role while leaving the paired toxin, target operator, and stress signal unresolved."
        )
    if gene in UNRESOLVED_NO_CORE:
        return (
            f"{gene} is named as a {product} in Pseudomonas putida KT2440, but the fetched record has no GOA rows and no "
            "resolved Cro/C1, XRE, or antitoxin domain support. This first pass leaves the molecular function unresolved."
        )
    if gene in SPILLOVERS:
        return (
            f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. The protein is in the XRE/Cro batch because "
            "of HTH or product-name signals, but its domain context points to RodZ-like, CdaR/PucR, or LuxR/GerE-like regulator "
            "biology rather than phage-specific regulation. This first pass keeps the transcription-regulator assignment "
            "conservative and leaves pathway placement unresolved."
        )
    return (
        f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. UniProt, GOA, and Asta retrieval support a "
        "Cro/C1 or XRE-like helix-turn-helix DNA-binding transcription regulator assignment, but current first-pass evidence "
        "does not identify a direct regulon, mobile-element target, paired toxin, or regulatory direction."
    )


def replacement(go_id: str) -> list[dict[str, str]]:
    return [TERM[go_id]]


def core_mf_for(gene: str) -> str | None:
    if gene in UNRESOLVED_NO_CORE:
        return None
    if gene in MQSR:
        return "GO:0090729"
    return "GO:0003700"


def review_for(gene: str, annotation: dict[str, object]) -> dict[str, object]:
    term_obj = annotation.get("term", {})
    go_id = str(term_obj.get("id", "")) if isinstance(term_obj, dict) else ""
    label = str(term_obj.get("label", "")) if isinstance(term_obj, dict) else go_id
    evidence_type = str(annotation.get("evidence_type", ""))
    reference_id = str(annotation.get("original_reference_id", ""))
    evidence = evidence_for(gene, go_id, evidence_type=evidence_type, reference_id=reference_id)

    if go_id == "GO:0003700":
        return {
            "summary": "DNA-binding transcription factor activity is the appropriate first-pass molecular function.",
            "action": "ACCEPT",
            "reason": (
                "The HTH-domain and product context support a DNA-binding transcription-regulator role. The direct regulon "
                f"and pathway placement remain unresolved: {role_for(gene)}."
            ),
            "supported_by": evidence,
        }

    if go_id == "GO:0003677":
        core_mf = core_mf_for(gene)
        if core_mf == "GO:0003700":
            return {
                "summary": "Generic DNA binding is true but less informative than transcription-regulator activity.",
                "action": "MARK_AS_OVER_ANNOTATED",
                "reason": (
                    "The protein is not merely a generic DNA-binding protein; the HTH-family and product context support "
                    "a DNA-binding transcription-regulator call."
                ),
                "proposed_replacement_terms": replacement("GO:0003700"),
                "supported_by": evidence,
            }
        return {
            "summary": "DNA binding is retained as non-core context for this toxin-antitoxin-family protein.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The strongest core call is toxin activity, while DNA binding remains product-name context.",
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
                "The HTH-family product context supports a transcription-regulator role without resolving the direct operator, "
                "regulated genes, or regulatory direction."
            ),
            "supported_by": evidence,
        }

    if go_id == "GO:0005829":
        return {
            "summary": "Cytosol is retained as localization context.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The row is compatible with a soluble bacterial regulator but is not the core molecular function.",
            "supported_by": evidence,
        }

    if gene in MQSR and go_id == "GO:0017148":
        return {
            "summary": "Negative regulation of translation is retained as direct process context for the MqsR toxin candidate.",
            "action": "ACCEPT",
            "reason": (
                "The MqsR toxin-family and mRNA-interferase product context support translation-inhibition process context, "
                "although the precise RNA cleavage activity is not represented in the current GOA rows."
            ),
            "supported_by": evidence,
        }

    if gene in MQSR and go_id in {"GO:0009372", "GO:0044010"}:
        return {
            "summary": f"{label} is likely downstream or over-propagated from MqsR-family biology.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": (
                "The local evidence supports an MqsR-family toxin candidate, but does not establish quorum-sensing or biofilm "
                "phenotypes for this KT2440 gene. These process annotations are kept out of the core function."
            ),
            "supported_by": evidence,
        }

    return {
        "summary": f"{label} is retained as compatible non-core context.",
        "action": "KEEP_AS_NON_CORE",
        "reason": f"The supported first-pass role is {role_for(gene)}.",
        "supported_by": evidence,
    }


def normalize_go_ref_titles(data: dict[str, object]) -> None:
    for ref in data.get("references", []):
        if isinstance(ref, dict) and str(ref.get("id", "")).startswith("GO_REF:") and str(ref.get("title", "")).startswith("TODO:"):
            ref["title"] = f"Gene Ontology annotation reference {ref['id']}"


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
    core_mf = core_mf_for(gene)
    if not core_mf:
        return []
    core: dict[str, object] = {
        "description": role_for(gene),
        "molecular_function": TERM[core_mf],
        "supported_by": evidence_for(gene, core_mf if core_mf in goa_ids(gene) else None),
    }
    if core_mf == "GO:0003700":
        add_support(core["supported_by"], goa_support(gene, "GO:0003700"))  # type: ignore[arg-type]
        add_support(core["supported_by"], goa_support(gene, "GO:0003677"))  # type: ignore[arg-type]
        if "GO:0006355" in goa_ids(gene):
            core["directly_involved_in"] = [TERM["GO:0006355"]]
            add_support(core["supported_by"], goa_support(gene, "GO:0006355"))  # type: ignore[arg-type]
    if gene in MQSR:
        core["directly_involved_in"] = [TERM["GO:0017148"]]
        add_support(core["supported_by"], goa_support(gene, "GO:0017148"))  # type: ignore[arg-type]
    return [core]


def suggested_questions(gene: str) -> list[dict[str, object]]:
    if gene in MQSR | HIGA_MQSA:
        question = f"What toxin-antitoxin partner, operator target, and stress condition define {gene} in KT2440?"
    elif gene in SPILLOVERS:
        question = f"What non-phage regulon or pathway context explains the {gene} HTH regulator?"
    elif gene in UNRESOLVED_NO_CORE:
        question = f"Does {gene} encode a functional Cro/CI-family DNA-binding regulator, or is the product name unsupported?"
    else:
        question = f"What direct operator/regulon and mobile-element or metabolic context define {gene}?"
    return [{"question": question, "experts": []}]


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    if gene in MQSR | HIGA_MQSA:
        description = f"Test {gene} in toxin-antitoxin interaction, promoter binding, and stress-induced expression assays."
    elif gene in UNRESOLVED_NO_CORE:
        description = f"Re-evaluate {gene} with comparative sequence/domain analysis before assigning DNA-binding regulator GO terms."
    else:
        description = f"Map {gene}-dependent transcription changes and promoter binding, then test whether neighboring mobile-element or metabolic genes are direct targets."
    return [{"experiment_type": "regulatory network mapping", "description": description}]


def write_notes(gene: str) -> None:
    path = gene_file(gene, "notes.md")
    heading = f"## {TODAY} XRE/Cro toxin-antitoxin regulator first pass"
    evidence = evidence_for(gene, "GO:0003700" if "GO:0003700" in goa_ids(gene) else None)
    lines_out = [
        heading,
        "",
        f"- Batch: `{BATCH_TSV.relative_to(ROOT)}`.",
        f"- Main conclusion: {role_for(gene)}.",
    ]
    if gene in UNRESOLVED_NO_CORE:
        lines_out.append("- Decision: no core GO function assigned; the current record has no GOA rows and no resolved Cro/C1/XRE domain support.")
    elif gene in MQSR:
        lines_out.append("- Decision: curate as an MqsR-family toxin candidate; keep quorum-sensing and biofilm rows out of the core function.")
    else:
        lines_out.append("- Decision: curate as a DNA-binding transcription regulator candidate; phage, toxin-antitoxin, metabolic, or other pathway context remains unresolved unless domain context supports it.")
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
    normalize_go_ref_titles(data)
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
    }
    core_mf = core_mf_for(gene)
    if not core_mf:
        out["notes"] = "No core GO function asserted; current evidence lacks resolved Cro/C1/XRE or antitoxin-domain support."
    else:
        out["function"] = {"preferred_term": TERM[core_mf]["label"], "term": TERM[core_mf]}
        if gene in MQSR:
            out["processes"] = [{"preferred_term": TERM["GO:0017148"]["label"], "term": TERM["GO:0017148"]}]
            out["notes"] = "MqsR-family toxin candidate; quorum-sensing and biofilm rows are not treated as core KT2440 phenotypes."
        elif "GO:0006355" in goa_ids(gene):
            out["processes"] = [{"preferred_term": TERM["GO:0006355"]["label"], "term": TERM["GO:0006355"]}]
            out["notes"] = "DNA-binding transcription regulator candidate; target operator and pathway context unresolved."
        else:
            out["notes"] = "DNA-binding transcription regulator candidate from product/domain context; target regulon unresolved."
    return out


def existing_annoton(gene: str, role: str, function_id: str, process_ids: list[str] | None = None) -> dict[str, object]:
    out: dict[str, object] = {
        "id": f"{clean_id(gene)}_{clean_id(role)}",
        "label": f"{gene}: {role}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": role,
        "function": {"preferred_term": TERM[function_id]["label"], "term": TERM[function_id]},
    }
    if process_ids:
        out["processes"] = [{"preferred_term": TERM[go_id]["label"], "term": TERM[go_id]} for go_id in process_ids]
    return out


def part(order: int, part_id: str, label: str, description: str, genes: list[str], existing: bool = False) -> dict[str, object]:
    if existing:
        annotons = [
            existing_annoton("PP_2500", "RelE/ParE-family toxin activity", "GO:0090729"),
            existing_annoton("PP_5558", "XRE-family phage-origin DNA binding", "GO:0003677"),
            existing_annoton("PP_5626", "phage repressor-like DNA binding", "GO:0003677", ["GO:0006355"]),
        ]
    else:
        annotons = [annoton(gene) for gene in genes]
    return {
        "order": order,
        "role": label,
        "node": {
            "id": part_id,
            "label": label,
            "module_type": "BIOLOGICAL_PROCESS",
            "description": description,
            "annotons": annotons,
        },
    }


def write_module() -> None:
    evidence: list[dict[str, str]] = [
        {
            "source_id": "file:projects/P_PUTIDA/batches/module_mobile_genetic_elements_phage_regulatory_toxin_antitoxin.tsv",
            "title": "PSEPK mobile-genetic-elements phage regulatory and toxin-antitoxin split table",
            "statement": "The mobile-genetic-elements split routes three broad genes to phage regulatory or toxin-antitoxin context.",
        },
        {
            "source_id": f"file:{BATCH_TSV.relative_to(ROOT)}",
            "title": "PSEPK regulation/signal-transduction XRE/Cro and toxin-antitoxin split",
            "statement": "The regulation bucket split records 28 XRE/Cro/CdaR/PucR/MqsRA regulator candidates handled in this first pass.",
        },
        {
            "source_id": f"file:{PARTITION_TSV.relative_to(ROOT)}",
            "title": "PSEPK regulation/signal-transduction partition table",
            "statement": "The regulation umbrella partition routes these genes into the XRE/Cro phage and toxin-antitoxin split.",
        },
    ]
    for gene in GENES:
        evidence.append(
            {
                "source_id": f"file:PSEPK/{gene}/{gene}-ai-review.yaml",
                "title": f"Curated {gene} review",
                "statement": role_for(gene),
            }
        )

    module = {
        "id": "MODULE:phage_regulation_toxin_antitoxin_boundary",
        "title": "Phage regulation and toxin-antitoxin boundary",
        "description": (
            "Boundary module for PSEPK phage-origin regulatory DNA-binding proteins, type II toxin-antitoxin candidates, "
            "and XRE/Cro-family regulator spillovers from the broad regulation/signal-transduction bucket."
        ),
        "status": "DRAFT",
        "evidence": evidence,
        "notes": (
            "This boundary now combines the earlier mobile-genetic-elements toxin/phage regulator split with the regulation "
            "bucket XRE/Cro split. Not every batch member is phage-origin: RodZ-like, CdaR/PucR, LuxR/GerE, and PuuR/cupin "
            "records are retained as regulator spillovers with unresolved pathway placement. mqsR is kept as an MqsR-family "
            "toxin candidate; quorum-sensing and biofilm annotations are not promoted to core KT2440 phenotypes."
        ),
        "module": {
            "id": "phage_regulation_toxin_antitoxin_boundary",
            "label": "Phage regulation and toxin-antitoxin boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                module_term("GO:0090729", "Generic toxin activity for RelE/ParE and MqsR-family toxin candidates."),
                module_term("GO:0003700", "Transcription-factor activity for HTH regulator candidates."),
                module_term("GO:0003677", "Generic DNA-binding rows marked less informative where regulator activity is supported."),
                module_term("GO:0006355", "Broad transcription-regulation process context."),
                module_term("GO:0017148", "Translation-inhibition context for MqsR-family toxin candidates."),
            ],
            "parts": [
                part(
                    1,
                    "previous_mobile_element_phage_toxin_antitoxin_context",
                    "Previous mobile-element phage/toxin-antitoxin context",
                    "Existing phage/toxin-antitoxin annotons from the mobile-genetic-elements bucket.",
                    MOBILE_EXISTING,
                    existing=True,
                ),
                part(
                    2,
                    "mqsra_and_higa_like_toxin_antitoxin_regulators",
                    "MqsRA and HigA-like toxin-antitoxin regulators",
                    "MqsRA and HigA-like proteins with antitoxin or toxin-domain context.",
                    ["PP_0276", "PP_1198", "mqsA", "mqsR"],
                ),
                part(
                    3,
                    "lexa_like_cro_c1_regulator_candidates",
                    "LexA-like Cro/C1 regulator candidates",
                    "Cro/C1-family proteins with LexA-like or S24 peptidase-domain context.",
                    sorted(LEXA_LIKE),
                ),
                part(
                    4,
                    "cro_c1_cupin_regulator_candidates",
                    "Cro/C1-cupin regulator candidates",
                    "Cro/C1-family proteins with cupin/RmlC-like domains or named PuuR context.",
                    sorted(CUPIN_CRO),
                ),
                part(
                    5,
                    "simple_cro_c1_regulator_candidates",
                    "Simple Cro/C1 regulator candidates",
                    "Cro/C1-family HTH regulators with unresolved target operator and pathway context.",
                    sorted(SIMPLE_CRO),
                ),
                part(
                    6,
                    "non_phage_regulatory_spillovers",
                    "Non-phage regulatory spillovers",
                    "RodZ-like, CdaR/PucR, and LuxR/GerE-like records retained as spillovers from the XRE/Cro split.",
                    sorted(SPILLOVERS | UNRESOLVED_NO_CORE),
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
    for gene in GENES:
        curate_gene(gene)
    write_module()


if __name__ == "__main__":
    main()
