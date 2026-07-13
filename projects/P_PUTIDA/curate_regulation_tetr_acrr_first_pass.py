#!/usr/bin/env python3
"""First-pass curation for TetR/AcrR-family transcription regulators."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_DIR = ROOT / "projects" / "P_PUTIDA" / "batches"
BATCH_TSV = BATCH_DIR / "module_regulation_signal_transduction_tetr_acrr_transcriptional_regulators.tsv"
PARTITION_TSV = BATCH_DIR / "module_regulation_signal_transduction_partition.tsv"
MODULE_PATH = ROOT / "modules" / "tetr_acrr_transcriptional_regulator_boundary.yaml"
TODAY = "2026-07-10"
PRESERVE_REVIEWS = {"ttgR"}
UNRESOLVED_NO_CORE = {"PP_2597"}
PSRA_LIKE = {"PP_2144"}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


TERM: dict[str, dict[str, str]] = {
    "GO:0000976": term("GO:0000976", "transcription cis-regulatory region binding"),
    "GO:0001216": term("GO:0001216", "DNA-binding transcription activator activity"),
    "GO:0001217": term("GO:0001217", "DNA-binding transcription repressor activity"),
    "GO:0003677": term("GO:0003677", "DNA binding"),
    "GO:0003700": term("GO:0003700", "DNA-binding transcription factor activity"),
    "GO:0006355": term("GO:0006355", "regulation of DNA-templated transcription"),
    "GO:0032993": term("GO:0032993", "protein-DNA complex"),
    "GO:0045892": term("GO:0045892", "negative regulation of DNA-templated transcription"),
    "GO:0045893": term("GO:0045893", "positive regulation of DNA-templated transcription"),
}


def read_batch_rows() -> dict[str, dict[str, str]]:
    with BATCH_TSV.open(encoding="utf-8") as handle:
        return {row["gene"]: row for row in csv.DictReader(handle, delimiter="\t")}


BATCH_ROWS = read_batch_rows()


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


def goa_line(gene: str, go_id: str, evidence_type: str | None = None) -> str | None:
    for line in lines(gene_file(gene, "goa.tsv"))[1:]:
        if f"\t{go_id}\t" not in line:
            continue
        if evidence_type and f"\t{evidence_type}\t" not in line:
            continue
        return line
    return None


def goa_ids(gene: str) -> set[str]:
    ids: set[str] = set()
    path = gene_file(gene, "goa.tsv")
    if not path.exists() or path.stat().st_size == 0:
        return ids
    with path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row.get("GO TERM"):
                ids.add(row["GO TERM"])
    return ids


def goa_support(gene: str, go_id: str, evidence_type: str | None = None) -> dict[str, str] | None:
    return support(file_id(gene, "goa.tsv"), goa_line(gene, go_id, evidence_type=evidence_type))


def publication_title_support(pmid: str) -> dict[str, str] | None:
    pub_id = pmid.removeprefix("PMID:")
    path = ROOT / "publications" / f"PMID_{pub_id}.md"
    if not path.exists():
        return None
    for line in lines(path):
        if "TetR family member psrA directly binds" in line:
            return support(pmid, "TetR family member psrA directly binds the Pseudomonas rpoS and psrA promoters.")
    return None


def uniprot_support_lines(gene: str) -> list[dict[str, str]]:
    path = gene_file(gene, "uniprot.txt")
    items: list[dict[str, str]] = []
    for needle in ("DE   RecName:", "DE   SubName:", "DE   AltName:", "GN   Name=", "GN   OrderedLocusNames="):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "uniprot.txt"), line))
            if needle.startswith("DE"):
                break
    for needle in (
        "DR   InterPro; IPR023772; DNA-bd_HTH_TetR-type_CS.",
        "DR   InterPro; IPR050109; HTH-type_TetR-like_transc_reg.",
        "DR   InterPro; IPR001647; HTH_TetR.",
        "DR   InterPro; IPR036271; Tet_transcr_reg_TetR-rel_C_sf.",
        "DR   InterPro; IPR039538; BetI_C.",
        "DR   InterPro; IPR041586; PsrA_TetR_C.",
        "DR   InterPro; IPR041474; NicS_C.",
        "DR   InterPro; IPR049484; Rv0078-like_C.",
        "DR   InterPro; IPR054129; DesT_TetR_C.",
        "DR   InterPro; IPR050692; HTH_transcr_repressor_FabR.",
        "KW   DNA-binding",
        "KW   Transcription regulation",
        "KW   Membrane",
        "FT   TRANSMEM",
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


def evidence_for(gene: str, go_id: str | None = None, evidence_type: str | None = None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if go_id:
        add_support(items, goa_support(gene, go_id, evidence_type=evidence_type))
    for item in uniprot_support_lines(gene):
        add_support(items, item)
    for item in asta_support_lines(gene):
        add_support(items, item)
    return items


def role_for(gene: str) -> str:
    if gene == "ttgR":
        return "experimentally supported TetR-family repressor of the ttgABC efflux locus"
    if gene in PSRA_LIKE:
        return "PsrA-like TetR-family transcription regulator with curated promoter-binding activator and repressor annotations"
    if gene == "PP_2597":
        return "membrane-associated TetR-like protein with unresolved DNA-binding regulator function"
    if gene == "PP_4859":
        return "FabR/DesT-like TetR-family transcription regulator candidate with unresolved direct regulon"
    if gene in {"PP_2824", "PP_3731"}:
        return "BetI-like TetR-family transcription regulator candidate with unresolved direct regulon"
    if gene in {"PP_0594", "rutR", "PP_4295"}:
        return "YcdC-like TetR-family transcription regulator candidate with unresolved direct regulon"
    if gene == "PP_3527":
        return "NicS-like TetR-family transcription regulator candidate with unresolved direct regulon"
    if gene == "PP_3960":
        return "Rv0078-like TetR-family transcription regulator candidate with unresolved direct regulon"
    return "TetR/AcrR-family DNA-binding transcription regulator candidate with unresolved direct regulon"


def description_for(gene: str) -> str:
    product = BATCH_ROWS[gene]["protein_name"]
    if gene in PSRA_LIKE:
        return (
            f"{gene} encodes a predicted PsrA-like TetR-family transcription regulator in Pseudomonas putida KT2440. "
            "GOA includes experimental curator annotations to promoter binding and both DNA-binding transcription activator "
            "and repressor activities from the PsrA literature, while UniProt/Asta domain evidence places the protein in the "
            "TetR/PsrA regulator family. This first pass preserves the experimental directionality but does not infer a broader "
            "regulon beyond the curated promoter-binding context."
        )
    if gene in UNRESOLVED_NO_CORE:
        return (
            f"{gene} is named as a {product} in Pseudomonas putida KT2440, but the fetched record has no GOA rows, lacks the "
            "canonical HTH_TetR InterPro row used by the other batch members, and carries membrane/transmembrane prediction "
            "context. This first pass leaves the molecular function unresolved rather than asserting DNA-binding transcription "
            "regulator activity from the product name alone."
        )
    return (
        f"{gene} encodes a predicted {product} in Pseudomonas putida KT2440. UniProt, GOA, and Asta retrieval support a "
        "TetR/AcrR-family helix-turn-helix DNA-binding transcription regulator assignment, but current first-pass evidence "
        "does not identify the direct regulon, ligand, signal, or regulatory direction."
    )


def replacement(go_id: str) -> list[dict[str, str]]:
    return [TERM[go_id]]


def review_for(gene: str, annotation: dict[str, object]) -> dict[str, object]:
    go_id = annotation["term"]["id"]  # type: ignore[index]
    evidence_type = str(annotation.get("evidence_type", ""))
    reference_id = str(annotation.get("original_reference_id", ""))

    if gene in PSRA_LIKE and reference_id.startswith("PMID:"):
        items = evidence_for(gene, go_id, evidence_type=evidence_type)
        add_support(items, publication_title_support(reference_id))
        if go_id in {"GO:0000976", "GO:0001216", "GO:0001217"}:
            return {
                "summary": "This experimental PsrA-family annotation is retained; the cached reference is metadata-only, so this pass defers to the GO curator's full-text assessment.",
                "action": "ACCEPT",
                "reason": (
                    "The PMID title supports direct promoter binding by PsrA, and the GOA row is an experimental IPI annotation. "
                    "Because the local publication cache lacks full text, the conservative action is to retain the curator-supported "
                    "promoter-binding and activator/repressor molecular-function calls."
                ),
                "supported_by": items,
            }
        if go_id == "GO:0032993":
            return {
                "summary": "Protein-DNA complex participation is compatible with the experimental promoter-binding annotation but is not the most informative core function.",
                "action": "KEEP_AS_NON_CORE",
                "reason": (
                    "The core biological call is DNA-binding transcription regulation. The protein-DNA complex row is retained as "
                    "binding-state context from the experimental annotation."
                ),
                "supported_by": items,
            }

    if gene in PSRA_LIKE and go_id in {"GO:0045892", "GO:0045893"}:
        items = evidence_for(gene, go_id)
        add_support(items, goa_support(gene, "GO:0001216", evidence_type="IPI"))
        add_support(items, goa_support(gene, "GO:0001217", evidence_type="IPI"))
        return {
            "summary": "Directional transcription-regulation context is retained for the PsrA-like regulator because the batch includes curator-supported activator and repressor molecular-function rows.",
            "action": "ACCEPT",
            "reason": (
                "Although these process rows are electronic logical-inference annotations, they match the experimental activator and "
                "repressor molecular-function annotations already present for this PsrA-like TetR regulator."
            ),
            "supported_by": items,
        }

    if go_id == "GO:0000976":
        return {
            "summary": "Cis-regulatory-region binding is a suitable specific molecular-function annotation for this TetR/AcrR-family regulator.",
            "action": "ACCEPT",
            "reason": (
                "The gene product is a predicted HTH TetR/AcrR-family transcription regulator. This term captures promoter/operator "
                "DNA binding without asserting a target regulon or direction of regulation."
            ),
            "supported_by": evidence_for(gene, go_id),
        }

    if go_id == "GO:0003700":
        return {
            "summary": "DNA-binding transcription factor activity is the appropriate first-pass molecular function.",
            "action": "ACCEPT",
            "reason": (
                "The TetR/AcrR-family HTH domain and product context support a DNA-binding transcription-regulator role, while the "
                "specific regulated operon and effector are unresolved."
            ),
            "supported_by": evidence_for(gene, go_id),
        }

    if go_id == "GO:0003677":
        return {
            "summary": "Generic DNA binding is true but less informative than transcription-regulator activity.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": (
                "The protein is not merely a generic DNA-binding protein; the supported family-level role is a DNA-binding "
                "transcription regulator. Use GO:0003700 when the regulator assignment is retained."
            ),
            "proposed_replacement_terms": replacement("GO:0003700"),
            "supported_by": evidence_for(gene, go_id),
        }

    if go_id == "GO:0006355":
        return {
            "summary": "Regulation of DNA-templated transcription is suitable broad process context.",
            "action": "ACCEPT",
            "reason": (
                "The supported first-pass role is a DNA-binding transcription regulator. This process term is broad but appropriate "
                "when the direct regulon and regulatory direction are unresolved."
            ),
            "supported_by": evidence_for(gene, go_id),
        }

    if go_id in {"GO:0045892", "GO:0045893"}:
        return {
            "summary": "Directional transcription regulation is plausible but not resolved as the core call for this generic TetR/AcrR-family paralog.",
            "action": "KEEP_AS_NON_CORE",
            "reason": (
                "The direction is derived from family or electronic evidence. Without a verified target regulon, this pass keeps "
                "the core function at DNA-binding transcription-factor activity plus generic transcription-regulation context."
            ),
            "supported_by": evidence_for(gene, go_id),
        }

    return {
        "summary": "This annotation is retained as compatible context for the TetR/AcrR-family regulator assignment.",
        "action": "KEEP_AS_NON_CORE",
        "reason": f"The supported first-pass role is {role_for(gene)}.",
        "supported_by": evidence_for(gene, go_id),
    }


def new_go3700_review(gene: str) -> dict[str, object]:
    return {
        "summary": "DNA-binding transcription factor activity is added as the specific first-pass molecular-function call.",
        "action": "NEW",
        "reason": (
            "The existing GOA rows do not include GO:0003700, but the UniProt product name, HTH/TetR-family domain context, "
            "and Asta retrieval support a DNA-binding transcription-regulator function. Target regulon and direction remain unresolved."
        ),
        "supported_by": evidence_for(gene),
    }


def ensure_new_annotations(data: dict[str, object], gene: str) -> None:
    # Gene review validation requires existing_annotations to mirror GOA rows.
    # Missing sharper terms are represented through MODIFY/proposed_replacement_terms
    # and core_functions rather than synthetic existing_annotations entries.
    return


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
            and ann.get("term", {}).get("id") not in allowed_ids
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
        if ref["id"] == "PMID:11914368":
            ref = dict(ref)
            ref["findings"] = [
                item
                for item in ref.get("findings", [])
                if not (isinstance(item, dict) and str(item.get("supporting_text", "")).startswith("title: TetR family member"))
            ]
            finding = publication_title_support("PMID:11914368")
            if finding:
                ref = reference_with_findings(ref, [{"supporting_text": finding["supporting_text"]}])
        refs.append(ref)
        seen.add(str(ref["id"]))

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
            seen.add(str(ref["id"]))
    return refs


def core_functions_for(gene: str) -> list[dict[str, object]]:
    if gene in UNRESOLVED_NO_CORE:
        return []
    if gene in PSRA_LIKE:
        activator_support = evidence_for(gene, "GO:0001216", evidence_type="IPI")
        add_support(activator_support, goa_support(gene, "GO:0045893"))
        add_support(activator_support, publication_title_support("PMID:11914368"))
        repressor_support = evidence_for(gene, "GO:0001217", evidence_type="IPI")
        add_support(repressor_support, goa_support(gene, "GO:0045892"))
        add_support(repressor_support, publication_title_support("PMID:11914368"))
        return [
            {
                "description": "PsrA-like DNA-binding transcription activator activity retained from curator-supported promoter-binding evidence.",
                "molecular_function": TERM["GO:0001216"],
                "directly_involved_in": [TERM["GO:0045893"]],
                "supported_by": activator_support,
            },
            {
                "description": "PsrA-like DNA-binding transcription repressor activity retained from curator-supported promoter-binding evidence.",
                "molecular_function": TERM["GO:0001217"],
                "directly_involved_in": [TERM["GO:0045892"]],
                "supported_by": repressor_support,
            },
        ]
    core: dict[str, object] = {
        "description": role_for(gene),
        "molecular_function": TERM["GO:0003700"],
        "supported_by": evidence_for(gene, "GO:0003700"),
    }
    add_support(core["supported_by"], goa_support(gene, "GO:0000976"))  # type: ignore[arg-type]
    add_support(core["supported_by"], goa_support(gene, "GO:0003677"))  # type: ignore[arg-type]
    if "GO:0006355" in goa_ids(gene):
        core["directly_involved_in"] = [TERM["GO:0006355"]]
        add_support(core["supported_by"], goa_support(gene, "GO:0006355"))  # type: ignore[arg-type]
    return [core]


def suggested_questions(gene: str) -> list[dict[str, object]]:
    if gene in UNRESOLVED_NO_CORE:
        question = f"Does {gene} encode a functional DNA-binding TetR-family regulator, or is the membrane-associated product name misleading?"
    elif gene in PSRA_LIKE:
        question = f"What are the direct PP_2144/PsrA target promoters and regulatory outputs in KT2440?"
    else:
        question = f"What direct target regulon, small-molecule effector, and regulatory direction define the {gene} TetR/AcrR-family regulator?"
    return [{"question": question, "experts": []}]


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    if gene in UNRESOLVED_NO_CORE:
        description = f"Re-evaluate {gene} with topology-aware comparative sequence analysis before assigning DNA-binding or transcription-regulator GO terms."
    elif gene in PSRA_LIKE:
        description = "Map PP_2144/PsrA binding sites by ChIP-seq or targeted EMSA and measure promoter output in deletion/complemented strains."
    else:
        description = f"Map {gene}-dependent transcription changes and test binding to candidate promoters with EMSA or reporter assays under candidate ligand conditions."
    return [{"experiment_type": "regulatory network mapping", "description": description}]


def write_notes(gene: str) -> None:
    path = gene_file(gene, "notes.md")
    heading = f"## {TODAY} TetR/AcrR regulator first pass"
    evidence = evidence_for(gene, "GO:0003700" if gene not in UNRESOLVED_NO_CORE else None)
    if gene in PSRA_LIKE:
        add_support(evidence, publication_title_support("PMID:11914368"))
    lines_out = [
        heading,
        "",
        f"- Batch: `{BATCH_TSV.relative_to(ROOT)}`.",
        f"- Main conclusion: {role_for(gene)}.",
    ]
    if gene in UNRESOLVED_NO_CORE:
        lines_out.append(
            "- Decision: no core GO function assigned; this record has no GOA rows and has membrane/transmembrane context without the canonical HTH_TetR row."
        )
    elif gene in PSRA_LIKE:
        lines_out.append(
            "- Decision: preserve curator-supported PsrA-like promoter-binding activator and repressor annotations; do not infer additional targets in this first pass."
        )
    else:
        lines_out.append(
            "- Decision: curate as a TetR/AcrR-family DNA-binding transcription regulator candidate; target regulon, ligand, and direction remain unresolved."
        )
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
    if gene in PRESERVE_REVIEWS:
        print(f"Preserved existing curated review for {gene}")
        return
    path = gene_file(gene, "ai-review.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    data["status"] = "DRAFT"
    data["description"] = description_for(gene)
    prune_synthetic_annotations(data, gene)
    data["references"] = references_for(gene, data)
    normalize_go_ref_titles(data)
    for annotation in data.get("existing_annotations", []):
        annotation["review"] = review_for(gene, annotation)
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
        out["notes"] = "No core GO function asserted; current evidence has membrane/transmembrane context and lacks GOA rows."
    elif gene == "ttgR":
        out["function"] = {"preferred_term": TERM["GO:0001217"]["label"], "term": TERM["GO:0001217"]}
        out["processes"] = [{"preferred_term": TERM["GO:0045892"]["label"], "term": TERM["GO:0045892"]}]
        out["notes"] = "Existing curated review supports TtgR as a local DNA-binding transcription repressor of the ttgABC efflux locus."
    elif gene in PSRA_LIKE:
        out["function"] = {"preferred_term": TERM["GO:0003700"]["label"], "term": TERM["GO:0003700"]}
        out["processes"] = [
            {"preferred_term": TERM["GO:0045892"]["label"], "term": TERM["GO:0045892"]},
            {"preferred_term": TERM["GO:0045893"]["label"], "term": TERM["GO:0045893"]},
        ]
        out["notes"] = "PsrA-like regulator with curator-supported promoter-binding activator and repressor annotations."
    else:
        out["function"] = {"preferred_term": TERM["GO:0003700"]["label"], "term": TERM["GO:0003700"]}
        if "GO:0006355" in goa_ids(gene):
            out["processes"] = [{"preferred_term": TERM["GO:0006355"]["label"], "term": TERM["GO:0006355"]}]
        out["notes"] = "TetR/AcrR-family DNA-binding transcription regulator candidate; target regulon and regulatory direction are unresolved."
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
            "title": "PSEPK regulation/signal-transduction TetR/AcrR split",
            "statement": "The batch table records 25 TetR/AcrR-family regulators handled in this first pass.",
        },
        {
            "source_id": f"file:{PARTITION_TSV.relative_to(ROOT)}",
            "title": "PSEPK regulation/signal-transduction partition table",
            "statement": "The regulation umbrella partition routes these genes into the TetR/AcrR-family transcriptional regulator split.",
        },
    ]
    for gene in BATCH_ROWS:
        evidence.append({"source_id": file_id(gene, "ai-review.yaml"), "title": f"Curated {gene} review", "statement": role_for(gene)})

    module = {
        "id": "MODULE:tetr_acrr_transcriptional_regulator_boundary",
        "title": "TetR/AcrR-family transcriptional regulator boundary",
        "description": (
            "Boundary module for TetR/AcrR-family regulators from the broad PSEPK regulation/signal-transduction bucket. "
            "It separates named or experimentally anchored regulators from generic HTH TetR/AcrR candidates, low-information "
            "DNA-binding-only records, and one membrane-associated no-core record."
        ),
        "status": "DRAFT",
        "evidence": evidence,
        "notes": (
            "This is a regulator-family boundary, not one satisfiable pathway. Except for ttgR and PP_2144/PsrA-like evidence, "
            "the first pass does not infer direct regulons, ligands, substrates, or regulatory direction from TetR/AcrR family names alone."
        ),
        "module": {
            "id": "tetr_acrr_transcriptional_regulator_boundary",
            "label": "TetR/AcrR-family transcriptional regulator boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                module_term("GO:0003700", "Generic transcription-factor activity for TetR/AcrR-family regulator candidates."),
                module_term("GO:0000976", "Specific cis-regulatory-region binding for promoter/operator-binding annotations."),
                module_term("GO:0001216", "Activator activity retained where curator-supported PsrA-like evidence exists."),
                module_term("GO:0001217", "Repressor activity retained for ttgR and curator-supported PsrA-like evidence."),
                module_term("GO:0006355", "Shared broad process context for transcription regulation."),
                module_term("GO:0045892", "Directional negative regulation retained only where supported or as non-core context."),
                module_term("GO:0045893", "Directional positive regulation retained only where supported or as non-core context."),
            ],
            "parts": [
                part(
                    1,
                    "named_or_experimentally_anchored_tetr_regulators",
                    "Named or experimentally anchored TetR-family regulators",
                    "ttgR and PP_2144 have stronger gene-level or curator-supported evidence than the product-name-only batch members.",
                    ["ttgR", "PP_2144"],
                ),
                part(
                    2,
                    "generic_hth_tetr_acrr_regulator_candidates",
                    "Generic HTH TetR/AcrR regulator candidates",
                    "TetR/AcrR-family regulators with HTH/domain evidence and generic transcription-regulator GOA support.",
                    [
                        "PP_0242",
                        "PP_0594",
                        "PP_1497",
                        "PP_1515",
                        "PP_1968",
                        "PP_2806",
                        "PP_2824",
                        "PP_3300",
                        "PP_3527",
                        "PP_3731",
                        "PP_3756",
                        "PP_3960",
                        "PP_4295",
                        "PP_5006",
                        "PP_5119",
                    ],
                ),
                part(
                    3,
                    "low_information_tetr_dna_binding_candidates",
                    "Low-information TetR-family DNA-binding candidates",
                    "TetR-family records with product/domain support but sparse GOA, kept at generic regulator function pending target-regulon evidence.",
                    ["PP_1978", "PP_2475", "PP_2880", "PP_2951", "rutR", "PP_4754", "PP_4859"],
                ),
                part(
                    4,
                    "unresolved_membrane_associated_tetr_like_record",
                    "Unresolved membrane-associated TetR-like record",
                    "PP_2597 has no GOA rows and membrane/transmembrane context, so no core GO function is asserted in this pass.",
                    ["PP_2597"],
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
