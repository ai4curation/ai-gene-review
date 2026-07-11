#!/usr/bin/env python3
"""First-pass curation for AraC/XylS-family transcriptional regulators."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_DIR = ROOT / "projects" / "P_PUTIDA" / "batches"
BATCH_TSV = BATCH_DIR / "module_regulation_signal_transduction_arac_xyls_transcriptional_regulators.tsv"
MODULE_PATH = ROOT / "modules" / "arac_xyls_transcriptional_regulator_boundary.yaml"
TODAY = "2026-07-10"


EXISTING_CURATED = {"ada", "benR"}
PREFIX = {"benR": "BenR"}

NAMED_REGULATORS = {"ada", "benR", "gbdR", "cdhR", "pobR", "oruR"}
DJ1_INH_QAR_REGULATORS = {"PP_1313", "PP_2234", "PP_3526", "PP_3564", "PP_3665", "PP_5245"}
RMLC_CUPIN_REGULATORS = {
    "PP_0583",
    "PP_2070",
    "PP_2072",
    "PP_2365",
    "PP_2383",
    "PP_2430",
    "PP_2960",
    "PP_3022",
    "PP_3439",
    "PP_3640",
    "PP_4511",
    "PP_4852",
}
ARABINOSE_BINDING_DOMAIN_REGULATORS = {"PP_2004", "PP_2211", "PP_3659", "PP_3753", "PP_4508"}
OTHER_SENSOR_DOMAIN_REGULATORS = {"PP_0876", "PP_1395", "PP_1711", "PP_2173", "PP_2425", "PP_3149", "PP_3516", "PP_4482", "PP_4602", "PP_4605", "PP_5244"}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


TERM: dict[str, dict[str, str]] = {
    "GO:0000976": term("GO:0000976", "transcription cis-regulatory region binding"),
    "GO:0003677": term("GO:0003677", "DNA binding"),
    "GO:0003700": term("GO:0003700", "DNA-binding transcription factor activity"),
    "GO:0005737": term("GO:0005737", "cytoplasm"),
    "GO:0005829": term("GO:0005829", "cytosol"),
    "GO:0006351": term("GO:0006351", "DNA-templated transcription"),
    "GO:0006355": term("GO:0006355", "regulation of DNA-templated transcription"),
    "GO:0009893": term("GO:0009893", "positive regulation of metabolic process"),
    "GO:0016301": term("GO:0016301", "kinase activity"),
    "GO:0043565": term("GO:0043565", "sequence-specific DNA binding"),
    "GO:0045893": term("GO:0045893", "positive regulation of DNA-templated transcription"),
    "GO:0046872": term("GO:0046872", "metal ion binding"),
}


def read_batch_rows() -> dict[str, dict[str, str]]:
    with BATCH_TSV.open(encoding="utf-8") as handle:
        return {row["gene"]: row for row in csv.DictReader(handle, delimiter="\t")}


BATCH_ROWS = read_batch_rows()
GENES = list(BATCH_ROWS)


def prefix(gene: str) -> str:
    return PREFIX.get(gene, gene)


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{prefix(gene)}-{suffix}"


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{prefix(gene)}-{suffix}"


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
        "CC   -!- FUNCTION:",
        "DR   InterPro; IPR018060; HTH_AraC.",
        "DR   InterPro; IPR018062; HTH_AraC-typ_CS.",
        "DR   InterPro; IPR020449; Tscrpt_reg_AraC-type_HTH.",
        "DR   InterPro; IPR050204; AraC_XylS_family_regulators.",
        "DR   InterPro; IPR009057; Homeodomain-like_sf.",
        "DR   InterPro; IPR037923; HTH-like.",
        "DR   InterPro; IPR003313; AraC-bd.",
        "DR   InterPro; IPR035418; AraC-bd_2.",
        "DR   InterPro; IPR032687; AraC-type_N.",
        "DR   InterPro; IPR032783; AraC_lig.",
        "DR   InterPro; IPR009594; Tscrpt_reg_HTH_AraC_N.",
        "DR   InterPro; IPR014710; RmlC-like_jellyroll.",
        "DR   InterPro; IPR011051; RmlC_Cupin_sf.",
        "DR   InterPro; IPR047264; Cupin_HpaA-like_N.",
        "DR   InterPro; IPR029062; Class_I_gatase-like.",
        "DR   InterPro; IPR002818; DJ-1/PfpI.",
        "DR   InterPro; IPR052158; INH-QAR.",
        "DR   InterPro; IPR010499; AraC_E-bd.",
        "DR   InterPro; IPR029442; GyrI-like.",
        "DR   InterPro; IPR032710; NTF2-like_dom_sf.",
        "DR   InterPro; IPR037401; SnoaL-like.",
        "DR   InterPro; IPR035965; PAS-like_dom_sf.",
        "DR   InterPro; IPR013656; PAS_4.",
        "DR   InterPro; IPR035451; Ada-like_dom_sf.",
        "DR   InterPro; IPR004026; Ada_DNA_repair_Zn-bd.",
        "DR   InterPro; IPR016221; Bifunct_regulatory_prot_Ada.",
        "DR   InterPro; IPR001497; O6MeG_DNA_MeTrfase.",
        "DR   Pfam; PF12833; HTH_18; 1.",
        "DR   Pfam; PF01965; DJ-1_PfpI; 1.",
        "DR   Pfam; PF02311; AraC_binding; 1.",
        "DR   Pfam; PF12625; Arabinose_bd; 1.",
        "DR   Pfam; PF12852; Cupin_6; 1.",
        "DR   Pfam; PF06719; AraC_N; 1.",
        "DR   Pfam; PF14525; AraC_binding_2; 1.",
        "DR   Pfam; PF12680; SnoaL_4; 1.",
        "DR   Pfam; PF06445; A_cyano_beta_N; 1.",
        "DR   Pfam; PF08448; PAS_4; 1.",
        "DR   Pfam; PF02805; Ada_Zn_binding; 1.",
        "DR   Pfam; PF01035; DNA_binding_1; 1.",
        "KW   Activator",
        "KW   DNA-binding",
        "KW   Repressor",
        "KW   Transcription",
        "KW   Transcription regulation",
        "KW   Metal-binding",
        "KW   Kinase",
        "KW   DNA damage",
        "KW   DNA repair",
        "KW   Methyltransferase",
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
    if gene == "ada":
        return "bifunctional Ada DNA alkylation-repair enzyme and methylation-responsive AraC-domain transcription activator"
    if gene == "benR":
        return "BenR benzoate-responsive AraC/XylS-family transcription activator for benzoate catabolism"
    if gene == "gbdR":
        return "GbdR-named AraC-family transcription regulator candidate with unresolved quaternary-amine regulon in KT2440"
    if gene == "cdhR":
        return "CdhR-named AraC-family transcription regulator candidate with unresolved catabolic regulon"
    if gene == "pobR":
        return "PobR-named AraC-family transcription regulator candidate with unresolved 4-hydroxybenzoate regulon"
    if gene == "oruR":
        return "OruR-named AraC-family transcription regulator candidate for ornithine-utilization context"
    if gene in DJ1_INH_QAR_REGULATORS:
        return "DJ-1/PfpI or INH-QAR-associated AraC-family DNA-binding transcription regulator candidate with unresolved regulon"
    if gene in RMLC_CUPIN_REGULATORS:
        return "RmlC/cupin-associated AraC-family DNA-binding transcription regulator candidate with unresolved effector and regulon"
    if gene in ARABINOSE_BINDING_DOMAIN_REGULATORS:
        return "arabinose-binding-domain AraC-family DNA-binding transcription regulator candidate with unresolved effector and regulon"
    if gene == "PP_4602":
        return "PAS-domain AraC-family DNA-binding transcription regulator candidate with unsupported kinase-family side call"
    if gene == "PP_0876":
        return "NTF2/SnoaL-associated AraC-family DNA-binding transcription regulator candidate with unresolved effector"
    if gene == "PP_2173":
        return "GyrI/AraC-E-domain AraC-family DNA-binding transcription regulator candidate with unresolved effector"
    return "AraC/XylS-family DNA-binding transcription regulator candidate with unresolved effector and regulon"


def description_for(gene: str) -> str:
    product = BATCH_ROWS[gene]["protein_name"]
    if gene in {"gbdR", "cdhR", "pobR", "oruR"}:
        return (
            f"{gene} encodes a named {product} in Pseudomonas putida KT2440. UniProt, GOA, and Asta retrieval support an "
            "AraC/XylS-family DNA-binding transcription-regulator role. The direct operator, effector ligand, and full "
            "target regulon remain unresolved beyond the name-derived context."
        )
    if gene in DJ1_INH_QAR_REGULATORS:
        return (
            f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. The protein combines AraC-family HTH "
            "transcription-regulator features with a DJ-1/PfpI or INH-QAR-like domain, supporting a regulatory role while "
            "leaving the effector ligand and regulon unresolved."
        )
    if gene in RMLC_CUPIN_REGULATORS:
        return (
            f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. AraC-family DNA-binding features plus "
            "RmlC/cupin-like domain context support a transcription-regulator candidate, but substrate, effector, and "
            "pathway assignments remain unresolved."
        )
    if gene in ARABINOSE_BINDING_DOMAIN_REGULATORS:
        return (
            f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. Its AraC-type N-terminal/arabinose-binding "
            "domain and C-terminal HTH region support an effector-responsive transcription-regulator role; the actual "
            "effector and regulon are unresolved."
        )
    if gene == "PP_4602":
        return (
            "PP_4602 encodes a predicted AraC-family transcription regulator in Pseudomonas putida KT2440 with PAS-like "
            "domain context. Domain and GOA evidence support DNA-binding transcription factor activity; no resolved "
            "catalytic kinase domain is evident from the fetched domain architecture."
        )
    return (
        f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. The fetched GOA, UniProt, and Asta context "
        "support an AraC/XylS-family DNA-binding transcription-regulator role, but direct target genes, effector ligand, "
        "regulated pathway, and regulatory direction remain unresolved."
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
            "summary": "DNA-binding transcription factor activity is the appropriate shared molecular function.",
            "action": "ACCEPT",
            "reason": (
                "The product name, AraC/XylS HTH-domain context, and GOA/UniProt family evidence support a DNA-binding "
                f"transcription-regulator role. The direct regulon is not resolved: {role_for(gene)}."
            ),
            "supported_by": evidence,
        }

    if go_id == "GO:0043565":
        return {
            "summary": "Sequence-specific DNA binding is appropriate for this AraC/XylS-family transcription regulator.",
            "action": "ACCEPT",
            "reason": (
                "AraC/XylS-family transcription factors bind promoter/operator sequences through the HTH domain. The exact "
                "operator sequence is unresolved for this paralog, but the sequence-specific DNA-binding function is suitable."
            ),
            "supported_by": evidence,
        }

    if go_id == "GO:0000976":
        return {
            "summary": "Transcription cis-regulatory region binding is appropriate promoter/operator-binding context.",
            "action": "ACCEPT",
            "reason": (
                "This is a useful molecular-function term for AraC-family regulators with cis-regulatory-region binding rows; "
                "the specific operator and regulon remain unresolved."
            ),
            "supported_by": evidence,
        }

    if go_id == "GO:0003677":
        return {
            "summary": "Generic DNA binding is true but less informative than transcription-regulator activity.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": (
                "The supported role is not generic DNA binding; these proteins are AraC/XylS-family transcription regulators. "
                "GO:0003700 and GO:0043565 are more informative molecular-function terms."
            ),
            "proposed_replacement_terms": [TERM["GO:0003700"], TERM["GO:0043565"]],
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
                "The AraC/XylS-family HTH context supports transcription regulation while the direct operator, effector, "
                "and regulated genes remain unresolved."
            ),
            "supported_by": evidence,
        }

    if go_id == "GO:0009893":
        return {
            "summary": "Positive regulation of metabolic process is retained as non-core family or name-derived context.",
            "action": "KEEP_AS_NON_CORE",
            "reason": (
                "Many AraC/XylS-family regulators control catabolic or metabolic operons, but the direct metabolic pathway "
                "for this KT2440 paralog is not resolved unless already curated separately."
            ),
            "supported_by": evidence,
        }

    if go_id in {"GO:0005737", "GO:0005829"}:
        return {
            "summary": f"{label} is retained as localization context for a soluble bacterial transcription regulator.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "Cytoplasmic/cytosolic localization is compatible with the transcription-regulator role but is not the core molecular function.",
            "supported_by": evidence,
        }

    if go_id == "GO:0046872":
        return {
            "summary": "Metal ion binding is retained as non-core structural or family context.",
            "action": "KEEP_AS_NON_CORE",
            "reason": (
                "The record has metal-binding context, but the primary function for this boundary module is AraC-family "
                "DNA-binding transcription regulation; the bound metal and regulatory relevance are unresolved."
            ),
            "supported_by": evidence,
        }

    if go_id == "GO:0016301":
        return {
            "summary": "Kinase activity is likely an over-propagated keyword/domain-side annotation for this AraC-family regulator.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": (
                "The fetched UniProt domain context supports a PAS-like AraC-family transcription regulator but does not show "
                "a resolved protein-kinase or small-molecule kinase catalytic domain. This term is not promoted as core."
            ),
            "supported_by": evidence,
        }

    return {
        "summary": f"{label} is retained as compatible non-core context.",
        "action": "KEEP_AS_NON_CORE",
        "reason": f"The supported role is {role_for(gene)}.",
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
    add_support(core["supported_by"], goa_support(gene, "GO:0043565"))  # type: ignore[arg-type]
    if "GO:0006355" in goa_ids(gene):
        core["directly_involved_in"] = [TERM["GO:0006355"]]
        add_support(core["supported_by"], goa_support(gene, "GO:0006355"))  # type: ignore[arg-type]
    return [core]


def suggested_questions(gene: str) -> list[dict[str, object]]:
    if gene == "pobR":
        question = "Does P. putida KT2440 PobR directly regulate pobA or other 4-hydroxybenzoate catabolism genes?"
    elif gene == "oruR":
        question = "Which ornithine-utilization genes are directly controlled by OruR in KT2440?"
    elif gene in {"gbdR", "cdhR"}:
        question = f"What effector ligand and catabolic regulon define the named {gene} regulator in KT2440?"
    elif gene == "PP_4602":
        question = "Does PP_4602 have any catalytic kinase activity, or is the kinase call an over-propagated PAS-domain artifact?"
    else:
        question = f"What direct operator, effector ligand, regulatory direction, and target regulon define {gene}?"
    return [{"question": question, "experts": []}]


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    if gene == "PP_4602":
        description = "Map PP_4602-dependent transcription and test whether purified protein has kinase activity before retaining kinase-related annotations."
    else:
        description = f"Map {gene}-dependent transcription changes and promoter binding under candidate carbon, nitrogen, aromatic-acid, or stress effector conditions."
    return [{"experiment_type": "regulatory network mapping", "description": description}]


def write_notes(gene: str) -> None:
    path = gene_file(gene, "notes.md")
    heading = f"## {TODAY} AraC/XylS-family regulator first pass"
    evidence = evidence_for(gene, "GO:0003700")
    lines_out = [
        heading,
        "",
        f"- Batch: `{BATCH_TSV.relative_to(ROOT)}`.",
        f"- Main conclusion: {role_for(gene)}.",
        "- Decision: keep DNA-binding transcription factor activity as the shared core molecular function; leave direct regulon, effector, and regulatory direction unresolved unless separately curated.",
    ]
    if gene == "PP_4602":
        lines_out.append("- Kinase activity is treated as likely over-propagated side context and not a core function.")
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
        "notes": "Direct regulon, effector ligand, and regulatory direction remain unresolved in this boundary module.",
    }
    process_ids = goa_ids(gene)
    if "GO:0006355" in process_ids:
        out["processes"] = [{"preferred_term": TERM["GO:0006355"]["label"], "term": TERM["GO:0006355"]}]
    if gene == "ada":
        out["notes"] = "Existing curated Ada review captures DNA alkylation repair and methylation-responsive transcription activation; included here only as AraC-domain regulator context."
    elif gene == "benR":
        out["notes"] = "Existing curated BenR review captures benzoate-responsive activation of benABCD; included here as named AraC/XylS anchor context."
    elif gene == "PP_4602":
        out["notes"] = "PAS-domain AraC regulator candidate; kinase activity is not treated as core in this first pass."
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
            "named_arac_xyls_regulators",
            "Named AraC/XylS regulators",
            [gene for gene in GENES if gene in NAMED_REGULATORS],
            "Named AraC/XylS regulators, including already curated Ada and BenR anchor cases plus named candidate regulators.",
        )
    )
    PARTS.append(
        part(
            "dj1_inh_qar_arac_regulators",
            "DJ-1/PfpI or INH-QAR-associated AraC regulators",
            [gene for gene in GENES if gene in DJ1_INH_QAR_REGULATORS],
            "AraC-family HTH regulators with DJ-1/PfpI or INH-QAR-like sensory domains and unresolved regulons.",
        )
    )
    PARTS.append(
        part(
            "rmlc_cupin_arac_regulators",
            "RmlC/cupin-associated AraC regulators",
            [gene for gene in GENES if gene in RMLC_CUPIN_REGULATORS],
            "AraC-family HTH regulators with RmlC/cupin-like domains, generally treated as unresolved effector-binding context.",
        )
    )
    PARTS.append(
        part(
            "arabinose_binding_domain_arac_regulators",
            "Arabinose-binding-domain AraC regulators",
            [gene for gene in GENES if gene in ARABINOSE_BINDING_DOMAIN_REGULATORS],
            "AraC-family regulators with AraC-type N-terminal or arabinose-binding-domain architecture and unresolved ligands.",
        )
    )
    PARTS.append(
        part(
            "other_arac_sensor_domain_regulators",
            "Other AraC/XylS sensor-domain regulators",
            [gene for gene in GENES if gene in OTHER_SENSOR_DOMAIN_REGULATORS],
            "AraC/XylS-family transcription regulators with NTF2/SnoaL, AraC-N, GyrI-like, PAS, or minimal HTH domain context.",
        )
    )
    assigned = {ann["participant"]["gene"]["preferred_term"] for p in PARTS for ann in p["node"]["annotons"]}  # type: ignore[index]
    missing = set(GENES) - assigned
    if missing:
        raise ValueError(f"Genes missing from module parts: {sorted(missing)}")
    data: dict[str, object] = {
        "id": "MODULE:arac_xyls_transcriptional_regulator_boundary",
        "title": "AraC/XylS-family transcriptional regulator boundary",
        "description": (
            "Boundary module for PSEPK AraC/XylS-family transcription regulators from the broad regulation/signal-transduction "
            "functional bucket. It groups named catabolic or DNA-damage regulators, DJ-1/PfpI or INH-QAR-associated regulators, "
            "RmlC/cupin-associated regulators, arabinose-binding-domain regulators, and other AraC/XylS sensor-domain candidates "
            "while leaving most direct regulons and effector ligands unresolved."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_TSV.relative_to(ROOT)}",
                "title": "PSEPK regulation/signal-transduction AraC/XylS-family split",
                "statement": "The batch table records 40 AraC/XylS-family transcriptional regulators curated or represented in this first pass.",
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
            "id": "arac_xyls_transcriptional_regulator_boundary",
            "label": "AraC/XylS-family transcriptional regulator boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                module_term("GO:0003700", "Shared molecular function for AraC/XylS-family HTH transcription-regulator candidates."),
                module_term("GO:0043565", "Sequence-specific DNA binding supported by AraC/XylS HTH-domain family evidence."),
                module_term("GO:0000976", "Cis-regulatory-region binding for AraC-family regulators with promoter/operator binding rows."),
                module_term("GO:0006355", "Broad process context for regulator candidates with unresolved direct regulons."),
                module_term("GO:0009893", "Non-core metabolic-output context for catabolic-regulator candidates where the specific pathway is unresolved."),
            ],
            "context": {
                "cellular_components": [
                    module_term("GO:0005829", "Cytosolic localization used where asserted by imported GOA."),
                    module_term("GO:0005737", "Cytoplasmic localization used where asserted by imported GOA."),
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
        if gene in EXISTING_CURATED:
            print(f"Preserved existing curated review for {gene}")
            continue
        curate_gene(gene)
    build_module()


if __name__ == "__main__":
    main()
