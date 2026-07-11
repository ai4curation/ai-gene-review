#!/usr/bin/env python3
"""First-pass curation for MerR/ArsR/MarR metal, redox, and stress regulators."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_DIR = ROOT / "projects" / "P_PUTIDA" / "batches"
BATCH_TSV = BATCH_DIR / "module_regulation_signal_transduction_merr_arsr_marr_metal_redox_regulators.tsv"
PARTITION_TSV = BATCH_DIR / "module_regulation_signal_transduction_partition.tsv"
MODULE_PATH = ROOT / "modules" / "metal_redox_stress_transcription_regulator_boundary.yaml"
TODAY = "2026-07-10"


NAMED_ARSR = {"arsR1", "arsR2"}
SOXR = {"soxR"}
MERR_GENES = {
    "PP_0585",
    "PP_0740",
    "PP_2472",
    "PP_2740",
    "PP_2788",
    "PP_2990",
    "PP_3841",
    "PP_4273",
    "PP_4630",
    "PP_5140",
}
ARSR_GENERIC = {"PP_0590", "PP_0921", "PP_1253", "PP_2484"}
MARR_GENES = {"PP_1683", "PP_3550", "PP_4515"}
UNRESOLVED_NO_CORE = {"PP_1578", "PP_2296", "PP_3866", "PP_4102", "PP_5592"}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


TERM: dict[str, dict[str, str]] = {
    "GO:0003677": term("GO:0003677", "DNA binding"),
    "GO:0003700": term("GO:0003700", "DNA-binding transcription factor activity"),
    "GO:0005507": term("GO:0005507", "copper ion binding"),
    "GO:0005737": term("GO:0005737", "cytoplasm"),
    "GO:0006351": term("GO:0006351", "DNA-templated transcription"),
    "GO:0006355": term("GO:0006355", "regulation of DNA-templated transcription"),
    "GO:0006950": term("GO:0006950", "response to stress"),
    "GO:0006979": term("GO:0006979", "response to oxidative stress"),
    "GO:0010288": term("GO:0010288", "response to lead ion"),
    "GO:0010468": term("GO:0010468", "regulation of gene expression"),
    "GO:0032791": term("GO:0032791", "lead ion binding"),
    "GO:0045893": term("GO:0045893", "positive regulation of DNA-templated transcription"),
    "GO:0046686": term("GO:0046686", "response to cadmium ion"),
    "GO:0046872": term("GO:0046872", "metal ion binding"),
    "GO:0051537": term("GO:0051537", "2 iron, 2 sulfur cluster binding"),
    "GO:0097063": term("GO:0097063", "cadmium ion sensor activity"),
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


def publication_support_lines() -> list[dict[str, str]]:
    path = ROOT / "publications" / "PMID_27208139.md"
    items: list[dict[str, str]] = []
    if not path.exists():
        return items
    text = path.read_text(encoding="utf-8")
    for snippet in (
        "transcriptional regulators ArsR1 and ArsR2 that control operon expression",
        "show here that purified ArsR1 and ArsR2 bind the trivalent salt of arsenic",
    ):
        if snippet in text:
            add_support(items, support("PMID:27208139", snippet))
    return items


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
        "CC   -!- SUBCELLULAR LOCATION:",
        "DR   InterPro; IPR011789; CueR.",
        "DR   InterPro; IPR011791; CadR-PbrR.",
        "DR   InterPro; IPR009061; DNA-bd_dom_put_sf.",
        "DR   InterPro; IPR000551; MerR-type_HTH_dom.",
        "DR   InterPro; IPR047057; MerR_fam.",
        "DR   InterPro; IPR015358; Tscrpt_reg_MerR_DNA-bd.",
        "DR   InterPro; IPR010211; Redox-sen_tscrpt-act_SoxR.",
        "DR   InterPro; IPR011991; ArsR-like_HTH.",
        "DR   InterPro; IPR001845; HTH_ArsR_DNA-bd_dom.",
        "DR   InterPro; IPR051081; HTH_MetalResp_TranReg.",
        "DR   InterPro; IPR052543; HTH_Metal-responsive_Reg.",
        "DR   InterPro; IPR000835; HTH_MarR-typ.",
        "DR   InterPro; IPR039422; MarR/SlyA-like.",
        "DR   InterPro; IPR023187; Tscrpt_reg_MarR-type_CS.",
        "DR   InterPro; IPR036388; WH-like_DNA-bd_sf.",
        "DR   InterPro; IPR036390; WH_DNA-bd_sf.",
        "DR   InterPro; IPR014974; DUF1833.",
        "DR   InterPro; IPR019289; Phage_tail_E/E.",
        "DR   InterPro; IPR052552; YeaO-like.",
        "DR   Pfam; PF00376; MerR; 1.",
        "DR   Pfam; PF01022; HTH_5; 1.",
        "DR   Pfam; PF01047; MarR; 1.",
        "DR   Pfam; PF12802; MarR_2; 1.",
        "FT   DNA_BIND",
        "/ligand=\"arsenite\"",
        "/ligand=\"[2Fe-2S] cluster\"",
        "KW   Arsenical resistance",
        "KW   2Fe-2S",
        "KW   DNA-binding",
        "KW   Metal-binding",
        "KW   Transcription",
        "KW   Transcription regulation",
        "KW   Cytoplasm",
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
    for needle in ("protein_domains:", "**Key Domains:**"):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "deep-research-asta.md"), line))
            break
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
    if gene in NAMED_ARSR:
        for item in publication_support_lines():
            add_support(items, item)
    return items


def has_hth_transcription_support(gene: str) -> bool:
    return gene not in UNRESOLVED_NO_CORE


def role_for(gene: str) -> str:
    if gene in NAMED_ARSR:
        return f"{gene} arsenite-responsive ArsR regulator controlling arsenic efflux operon expression"
    if gene == "soxR":
        return "SoxR-like redox-sensitive MerR-family DNA-binding transcription regulator candidate"
    if gene == "PP_0585":
        return "CueR-like MerR-family metal-responsive DNA-binding transcription regulator candidate"
    if gene == "PP_5140":
        return "CadR/PbrR-like MerR-family metal-responsive DNA-binding transcription regulator candidate"
    if gene in MERR_GENES:
        return "MerR-family DNA-binding transcription regulator candidate with unresolved direct regulon"
    if gene == "PP_0590":
        return "ArsR-family metal-responsive DNA-binding transcription regulator candidate with Pb/Cd family-level context"
    if gene in ARSR_GENERIC:
        return "ArsR-family metal-responsive DNA-binding transcription regulator candidate with unresolved ligand and regulon"
    if gene == "PP_3550":
        return "EmrR/MarR-family DNA-binding transcription regulator candidate with unresolved efflux regulon"
    if gene in MARR_GENES:
        return "MarR-family DNA-binding transcription regulator candidate with unresolved stress or efflux regulon"
    if gene == "PP_2296":
        return "product-name-only MarR regulator candidate with weak winged-helix support but no GOA rows"
    return "product-name-only metal or stress regulator candidate with unresolved transcription-regulator evidence"


def description_for(gene: str) -> str:
    product = BATCH_ROWS[gene]["protein_name"]
    if gene in NAMED_ARSR:
        return (
            f"{gene} encodes a named arsenic resistance transcriptional regulator in Pseudomonas putida KT2440. UniProt "
            "and the ArsR1/ArsR2 study support an ArsR-family DNA-binding regulator that binds arsenite and controls "
            "arsenic efflux operon expression. This first pass keeps the core GO function at DNA-binding transcription "
            "factor activity and treats cytoplasmic localization as supporting context."
        )
    if gene == "soxR":
        return (
            "soxR encodes a predicted redox-sensitive SoxR/MerR-family transcription regulator in Pseudomonas putida "
            "KT2440. UniProt, GOA, and Asta retrieval support a MerR-type HTH regulator with SoxR-family and iron-sulfur "
            "cluster features; this first pass does not infer a specific oxidative-stress regulon beyond the generic "
            "transcription-regulator role."
        )
    if gene in UNRESOLVED_NO_CORE:
        return (
            f"{gene} is named as a {product} in Pseudomonas putida KT2440, but the fetched record has no GOA rows and "
            "does not carry coherent MerR/ArsR/MarR HTH-domain evidence. This first pass leaves the molecular function "
            "unresolved rather than asserting DNA-binding transcription factor activity from the product name alone."
        )
    return (
        f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. The current GOA rows plus UniProt/Asta "
        "domain context support a DNA-binding transcription-regulator role in the MerR, ArsR, or MarR family, but do "
        "not identify the direct regulon, effector ligand, metal specificity, or regulatory direction for this paralog."
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
            "summary": "DNA-binding transcription factor activity is the appropriate first-pass molecular function.",
            "action": "ACCEPT",
            "reason": (
                "The product name, HTH-domain context, and GOA family evidence support a DNA-binding transcription-regulator "
                f"role. The direct regulon and effector remain unresolved for this pass: {role_for(gene)}."
            ),
            "supported_by": evidence,
        }

    if go_id == "GO:0003677":
        return {
            "summary": "Generic DNA binding is true but less informative than transcription-regulator activity.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": (
                "The supported role is not generic DNA binding; these records are HTH-family transcription regulators. "
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

    if go_id == "GO:0010468":
        return {
            "summary": "Regulation of gene expression is compatible but less precise than transcription regulation.",
            "action": "MODIFY",
            "reason": (
                "The supported role is an HTH DNA-binding transcription regulator. GO:0006355 captures that process more "
                "directly than the broader gene-expression term."
            ),
            "proposed_replacement_terms": replacement("GO:0006355"),
            "supported_by": evidence,
        }

    if go_id == "GO:0006355":
        return {
            "summary": "Regulation of DNA-templated transcription is appropriate broad process context.",
            "action": "ACCEPT",
            "reason": (
                "The gene product is a predicted DNA-binding transcription regulator; this process term is broad but suitable "
                "while the target regulon and direction remain unresolved."
            ),
            "supported_by": evidence,
        }

    if go_id == "GO:0005737":
        action = "KEEP_AS_NON_CORE"
        return {
            "summary": f"{label} is retained as localization context for this soluble bacterial regulator.",
            "action": action,
            "reason": (
                "Cytoplasmic localization is compatible with a bacterial transcription factor. It is useful context but is not "
                "the core molecular function for this boundary module."
            ),
            "supported_by": evidence,
        }

    if go_id in {"GO:0005507", "GO:0032791", "GO:0046872", "GO:0051537", "GO:0097063"}:
        return {
            "summary": f"{label} is retained as family-level ligand, metal-sensing, or cofactor context.",
            "action": "KEEP_AS_NON_CORE",
            "reason": (
                "The metal/cofactor row is plausible from family-level electronic evidence, but this first pass does not promote "
                "it above the DNA-binding transcription-regulator function without gene-specific ligand or regulon evidence."
            ),
            "supported_by": evidence,
        }

    if go_id in {"GO:0006950", "GO:0006979", "GO:0010288", "GO:0046686", "GO:0045893"}:
        return {
            "summary": f"{label} is retained as non-core stress, metal-response, or directional-regulation context.",
            "action": "KEEP_AS_NON_CORE",
            "reason": (
                "The annotation is biologically plausible for this regulator family, but direct target genes, effector ligand, "
                "and regulatory direction are not established for this specific KT2440 paralog in the first-pass evidence."
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


def prune_synthetic_annotations(data: dict[str, object], gene: str) -> None:
    allowed_ids = goa_ids(gene)
    annotations = data.get("existing_annotations", [])
    if not isinstance(annotations, list):
        return
    data["existing_annotations"] = [
        ann
        for ann in annotations
        if not (
            isinstance(ann, dict)
            and isinstance(ann.get("term"), dict)
            and ann["term"].get("id") not in allowed_ids
            and str(ann.get("original_reference_id", "")).startswith(f"file:PSEPK/{gene}/")
        )
    ]


def reference_with_findings(ref: dict[str, object], findings: list[dict[str, str]]) -> dict[str, object]:
    out = dict(ref)
    existing = list(out.get("findings", [])) if isinstance(out.get("findings", []), list) else []
    seen = {(item.get("supporting_text"), item.get("statement")) for item in existing if isinstance(item, dict)}
    for item in findings:
        key = (item.get("supporting_text"), item.get("statement"))
        if key not in seen:
            existing.append(item)
            seen.add(key)
    out["findings"] = existing
    return out


def references_for(gene: str, data: dict[str, object]) -> list[dict[str, object]]:
    refs: list[dict[str, object]] = []
    seen: set[str] = set()
    for ref in data.get("references", []):
        if not isinstance(ref, dict) or not ref.get("id"):
            continue
        if ref["id"] == "PMID:27208139":
            ref = reference_with_findings(ref, [{"supporting_text": item["supporting_text"]} for item in publication_support_lines()])
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
    if not has_hth_transcription_support(gene):
        return []
    core: dict[str, object] = {
        "description": role_for(gene),
        "molecular_function": TERM["GO:0003700"],
        "supported_by": evidence_for(gene, "GO:0003700"),
    }
    if "GO:0006355" in goa_ids(gene):
        core["directly_involved_in"] = [TERM["GO:0006355"]]
        add_support(core["supported_by"], goa_support(gene, "GO:0006355"))  # type: ignore[arg-type]
    if gene in NAMED_ARSR:
        add_support(core["supported_by"], goa_support(gene, "GO:0005737", reference_id="PMID:27208139"))  # type: ignore[arg-type]
    return [core]


def suggested_questions(gene: str) -> list[dict[str, object]]:
    if gene in NAMED_ARSR:
        question = f"Which promoters and efflux genes are directly regulated by {gene} in KT2440 under arsenite exposure?"
    elif gene == "soxR":
        question = "Which oxidative-stress promoters are directly regulated by P. putida SoxR, and under which redox-active compounds?"
    elif gene in UNRESOLVED_NO_CORE:
        question = f"Does {gene} encode a functional DNA-binding transcription regulator, or is the product name unsupported by the current domains?"
    else:
        question = f"What direct target regulon, effector ligand, and regulatory direction define the {gene} regulator?"
    return [{"question": question, "experts": []}]


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    if gene in NAMED_ARSR:
        description = f"Map {gene}-dependent promoter binding and transcript changes under arsenite, arsenate, antimony, and control conditions."
    elif gene == "soxR":
        description = "Map the SoxR regulon using perturbation RNA-seq and promoter binding assays under redox-cycling and oxidative-stress conditions."
    elif gene in UNRESOLVED_NO_CORE:
        description = f"Re-evaluate {gene} with comparative sequence analysis and DNA-binding assays before assigning transcription-regulator GO terms."
    else:
        description = f"Map {gene}-dependent transcription changes and test binding to candidate promoters with EMSA or reporter assays under candidate ligand conditions."
    return [{"experiment_type": "regulatory network mapping", "description": description}]


def write_notes(gene: str) -> None:
    path = gene_file(gene, "notes.md")
    heading = f"## {TODAY} MerR/ArsR/MarR metal-redox regulator first pass"
    evidence = evidence_for(gene, "GO:0003700" if gene not in UNRESOLVED_NO_CORE else None)
    lines_out = [
        heading,
        "",
        f"- Batch: `{BATCH_TSV.relative_to(ROOT)}`.",
        f"- Main conclusion: {role_for(gene)}.",
    ]
    if gene in UNRESOLVED_NO_CORE:
        lines_out.append("- Decision: no core GO function assigned; the current record has no GOA rows and weak or inconsistent regulator-domain support.")
    else:
        lines_out.append("- Decision: curate the core function as DNA-binding transcription factor activity; keep ligand, metal, stress, localization, and direction terms as context unless directly supported.")
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
    prune_synthetic_annotations(data, gene)
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
    if gene in UNRESOLVED_NO_CORE:
        out["notes"] = "No core GO function asserted; current evidence lacks coherent regulator-domain and GOA support."
    else:
        out["function"] = {"preferred_term": TERM["GO:0003700"]["label"], "term": TERM["GO:0003700"]}
        if "GO:0006355" in goa_ids(gene):
            out["processes"] = [{"preferred_term": TERM["GO:0006355"]["label"], "term": TERM["GO:0006355"]}]
        if gene in NAMED_ARSR:
            out["notes"] = "Named ArsR regulator with UniProt/literature support for arsenite binding and arsenic efflux operon regulation."
        elif gene == "soxR":
            out["notes"] = "SoxR-like MerR-family regulator with redox-sensitive and 2Fe-2S context; direct KT2440 regulon unresolved."
        else:
            out["notes"] = "Family-level DNA-binding transcription regulator candidate; ligand, regulon, and regulatory direction are unresolved."
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
            "title": "PSEPK regulation/signal-transduction MerR/ArsR/MarR split",
            "statement": "The batch table records 25 MerR/ArsR/MarR metal, redox, and stress regulator candidates handled in this first pass.",
        },
        {
            "source_id": f"file:{PARTITION_TSV.relative_to(ROOT)}",
            "title": "PSEPK regulation/signal-transduction partition table",
            "statement": "The regulation umbrella partition routes these genes into the MerR/ArsR/MarR metal-redox-stress regulator split.",
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
        "id": "MODULE:metal_redox_stress_transcription_regulator_boundary",
        "title": "MerR/ArsR/MarR metal, redox, and stress transcription regulator boundary",
        "description": (
            "Boundary module for MerR-, ArsR-, and MarR-family regulator candidates from the broad PSEPK "
            "regulation/signal-transduction bucket. It separates named arsenic/redox regulators from generic "
            "family-level transcription regulators and product-name-only records with weak regulator evidence."
        ),
        "status": "DRAFT",
        "evidence": evidence,
        "notes": (
            "This is a regulator-family boundary rather than one satisfiable pathway. The first pass accepts "
            "DNA-binding transcription regulator activity where GOA and HTH/domain context agree, keeps metal, "
            "cofactor, stress, localization, and direction annotations as non-core context, and does not infer "
            "specific ligands or regulons for generic paralogs."
        ),
        "module": {
            "id": "metal_redox_stress_transcription_regulator_boundary",
            "label": "MerR/ArsR/MarR metal, redox, and stress transcription regulator boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                module_term("GO:0003700", "Core molecular-function call for supported HTH transcription-regulator candidates."),
                module_term("GO:0006355", "Broad process context for transcription-regulation annotations."),
                module_term("GO:0003677", "Generic DNA-binding rows marked less informative than transcription-factor activity."),
                module_term("GO:0005507", "Copper-binding context for CueR-like MerR-family annotations."),
                module_term("GO:0032791", "Lead-binding context for Pb/Cd-responsive ArsR-family annotations."),
                module_term("GO:0097063", "Cadmium-sensor context kept non-core pending gene-specific evidence."),
                module_term("GO:0051537", "Iron-sulfur cluster cofactor context for SoxR-like annotations."),
                module_term("GO:0006979", "Oxidative-stress response context for SoxR-like annotations."),
                module_term("GO:0045893", "Directional positive-regulation context retained as non-core unless directly resolved."),
            ],
            "parts": [
                part(
                    1,
                    "named_arsenic_and_redox_regulators",
                    "Named arsenic and redox regulators",
                    "arsR1, arsR2, and soxR have stronger named regulator context than the generic paralogs.",
                    ["arsR1", "arsR2", "soxR"],
                ),
                part(
                    2,
                    "merr_family_metal_responsive_regulator_candidates",
                    "MerR-family metal-responsive regulator candidates",
                    "MerR-family proteins with GOA/domain support for DNA-binding transcription-regulator activity.",
                    sorted(MERR_GENES),
                ),
                part(
                    3,
                    "arsr_family_metal_responsive_regulator_candidates",
                    "ArsR-family metal-responsive regulator candidates",
                    "ArsR-family proteins with generic metal-responsive HTH regulator evidence but unresolved ligands and regulons.",
                    sorted(ARSR_GENERIC),
                ),
                part(
                    4,
                    "marr_emrr_family_stress_regulator_candidates",
                    "MarR/EmrR-family stress regulator candidates",
                    "MarR/EmrR-family proteins with HTH regulator support but unresolved efflux or stress-response targets.",
                    sorted(MARR_GENES),
                ),
                part(
                    5,
                    "weak_or_product_name_only_regulator_candidates",
                    "Weak or product-name-only regulator candidates",
                    "No-GOA records where the current domain evidence does not support a confident core transcription-regulator annotation.",
                    sorted(UNRESOLVED_NO_CORE),
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
