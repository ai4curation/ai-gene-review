#!/usr/bin/env python3
"""First-pass curation for compact metabolic transcriptional regulators."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_DIR = ROOT / "projects" / "P_PUTIDA" / "batches"
BATCH_TSV = BATCH_DIR / "module_regulation_signal_transduction_small_family_metabolic_transcriptional_regulators.tsv"
PARTITION_TSV = BATCH_DIR / "module_regulation_signal_transduction_partition.tsv"
MODULE_PATH = ROOT / "modules" / "metabolic_transcriptional_regulator_boundary.yaml"
TAXON_LABEL = "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)"
TODAY = "2026-07-10"
PRESERVE_EXISTING_REVIEWS = {"ptxS"}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


STATIC_TERMS = {
    "GO:0000976": term("GO:0000976", "transcription cis-regulatory region binding"),
    "GO:0001217": term("GO:0001217", "DNA-binding transcription repressor activity"),
    "GO:0003677": term("GO:0003677", "DNA binding"),
    "GO:0003700": term("GO:0003700", "DNA-binding transcription factor activity"),
    "GO:0005829": term("GO:0005829", "cytosol"),
    "GO:0005975": term("GO:0005975", "carbohydrate metabolic process"),
    "GO:0006351": term("GO:0006351", "DNA-templated transcription"),
    "GO:0006355": term("GO:0006355", "regulation of DNA-templated transcription"),
    "GO:0030246": term("GO:0030246", "carbohydrate binding"),
    "GO:0032993": term("GO:0032993", "protein-DNA complex"),
    "GO:0042802": term("GO:0042802", "identical protein binding"),
    "GO:0043200": term("GO:0043200", "response to amino acid"),
    "GO:0043565": term("GO:0043565", "sequence-specific DNA binding"),
    "GO:0045892": term("GO:0045892", "negative regulation of DNA-templated transcription"),
    "GO:0045893": term("GO:0045893", "positive regulation of DNA-templated transcription"),
    "GO:0046278": term("GO:0046278", "3,4-dihydroxybenzoate metabolic process"),
    "GO:0097367": term("GO:0097367", "carbohydrate derivative binding"),
    "GO:1901135": term("GO:1901135", "carbohydrate derivative metabolic process"),
}


GENE_INFO = {
    "PP_0384": {
        "accession": "Q88QV0",
        "family": "AsnC/Lrp-family",
        "description": (
            "PP_0384 encodes a predicted AsnC/Lrp-family helix-turn-helix transcriptional regulator in "
            "Pseudomonas putida KT2440. Current evidence supports sequence-specific DNA binding, transcription "
            "regulation, and cytosolic localization, but does not resolve the regulated operon or amino-acid effector."
        ),
        "core_mf": "GO:0043565",
        "core_processes": ["GO:0006355"],
        "locations": ["GO:0005829"],
        "role": "AsnC/Lrp-family transcriptional regulator with unresolved target regulon",
        "part": "asnc_lrp_amino_acid_regulators",
    },
    "PP_0663": {
        "accession": "Q88Q35",
        "family": "AsnC/Lrp-family",
        "description": (
            "PP_0663 encodes a predicted AsnC/Lrp-family helix-turn-helix transcriptional regulator. "
            "The fetched GOA/UniProt evidence supports sequence-specific DNA binding and transcription-regulation "
            "context, while the target regulon and amino-acid response remain unresolved."
        ),
        "core_mf": "GO:0043565",
        "core_processes": ["GO:0006355"],
        "locations": ["GO:0005829"],
        "role": "AsnC/Lrp-family transcriptional regulator with unresolved target regulon",
        "part": "asnc_lrp_amino_acid_regulators",
    },
    "glpR": {
        "accession": "Q88NX9",
        "family": "DeoR/GlpR-family",
        "description": (
            "glpR encodes a predicted DeoR/GlpR-family DNA-binding transcriptional repressor associated with "
            "glycerol-3-phosphate/carbohydrate metabolism context. This first pass supports a generic DNA-binding "
            "transcription-regulator role and does not assign a KT2440-specific regulon beyond the product-family signal."
        ),
        "core_mf": "GO:0003700",
        "core_processes": ["GO:0006355"],
        "locations": [],
        "role": "DeoR/GlpR-family metabolic transcriptional regulator",
        "part": "deor_laci_carbohydrate_regulators",
    },
    "PP_1307": {
        "accession": "Q88NA5",
        "family": "AsnC/Lrp-family",
        "description": (
            "PP_1307 encodes a predicted AsnC/Lrp-family transcriptional regulator. The current annotations support "
            "sequence-specific DNA binding, regulation of transcription, and cytosolic localization, but not a specific "
            "amino-acid response or regulated operon."
        ),
        "core_mf": "GO:0043565",
        "core_processes": ["GO:0006355"],
        "locations": ["GO:0005829"],
        "role": "AsnC/Lrp-family transcriptional regulator with unresolved target regulon",
        "part": "asnc_lrp_amino_acid_regulators",
    },
    "rbsR": {
        "accession": "Q88K35",
        "family": "LacI/RbsR-family",
        "description": (
            "rbsR encodes a predicted LacI-family DNA-binding transcription regulator/repressor in KT2440. GOA supports "
            "cis-regulatory-region binding and DNA-binding transcription-factor activity, while this first pass avoids "
            "asserting the precise ribose-operon regulatory target without direct organism-specific evidence."
        ),
        "core_mf": "GO:0003700",
        "core_processes": ["GO:0006355"],
        "locations": [],
        "role": "LacI-family metabolic transcriptional regulator",
        "part": "deor_laci_carbohydrate_regulators",
    },
    "PP_2601": {
        "accession": "Q88JP8",
        "family": "IclR-family",
        "description": (
            "PP_2601 encodes a predicted IclR-family metabolic transcriptional regulator. The supported first-pass "
            "function is DNA-binding transcription-factor activity in transcription regulation; directional repression "
            "or pathway assignment remains family-level context rather than a resolved KT2440 regulon."
        ),
        "core_mf": "GO:0003700",
        "core_processes": ["GO:0006355"],
        "locations": [],
        "role": "IclR-family metabolic transcriptional regulator",
        "part": "iclr_rpir_catabolic_regulators",
    },
    "PP_2609": {
        "accession": "Q88JP0",
        "family": "IclR/PcaR-family",
        "description": (
            "PP_2609 encodes a predicted IclR/PcaR-family transcriptional regulator. GOA supports DNA-binding "
            "transcription-factor activity and broad transcription-regulation context; the positive/negative regulation "
            "and 3,4-dihydroxybenzoate-process rows are treated as non-core family-context until the target regulon is verified."
        ),
        "core_mf": "GO:0003700",
        "core_processes": ["GO:0006355"],
        "locations": [],
        "role": "IclR/PcaR-family catabolic transcriptional regulator candidate",
        "part": "iclr_rpir_catabolic_regulators",
    },
    "fnrB": {
        "accession": "Q88HX0",
        "family": "Crp/Fnr-family",
        "description": (
            "fnrB encodes a predicted Crp/Fnr-family transcriptional regulator with 4Fe-4S-cluster family context. "
            "This first pass supports DNA-binding transcription-factor activity, transcription regulation, and cytosolic "
            "localization, while leaving the oxygen/redox regulon unresolved."
        ),
        "core_mf": "GO:0003700",
        "core_processes": ["GO:0006355"],
        "locations": ["GO:0005829"],
        "role": "Crp/Fnr-family redox-responsive transcriptional regulator candidate",
        "part": "crp_fnr_redox_regulators",
    },
    "fnrC": {
        "accession": "Q88HR6",
        "family": "Crp/Fnr-family",
        "description": (
            "fnrC encodes a predicted Crp/Fnr-family transcriptional regulator with 4Fe-4S-cluster family context. "
            "The supported first-pass role is a cytosolic DNA-binding transcription regulator, not a resolved redox-response "
            "module or specific regulon."
        ),
        "core_mf": "GO:0003700",
        "core_processes": ["GO:0006355"],
        "locations": ["GO:0005829"],
        "role": "Crp/Fnr-family redox-responsive transcriptional regulator candidate",
        "part": "crp_fnr_redox_regulators",
    },
    "PP_3362": {
        "accession": "Q88HJ4",
        "family": "AsnC/Lrp-family",
        "description": (
            "PP_3362 encodes a predicted AsnC/Lrp-family transcriptional regulator. Current evidence supports "
            "sequence-specific DNA binding and transcription-regulation context, but not a specific amino-acid response "
            "or target regulon."
        ),
        "core_mf": "GO:0043565",
        "core_processes": ["GO:0006355"],
        "locations": ["GO:0005829"],
        "role": "AsnC/Lrp-family transcriptional regulator with unresolved target regulon",
        "part": "asnc_lrp_amino_acid_regulators",
    },
    "ptxS": {
        "accession": "Q88HH7",
        "family": "LacI/PtxS-family",
        "description": "Existing curated PtxS review preserved; see genes/PSEPK/ptxS/ptxS-ai-review.yaml.",
        "core_mf": "GO:0001217",
        "core_processes": ["GO:0045892"],
        "locations": [],
        "role": "experimentally supported PtxS 2-ketogluconate-responsive transcriptional repressor",
        "part": "deor_laci_carbohydrate_regulators",
    },
    "PP_3415": {
        "accession": "Q88HE5",
        "family": "LacI/GalR-family",
        "description": (
            "PP_3415 encodes a predicted LacI/GalR-family transcriptional regulator. The fetched annotations support "
            "cis-regulatory-region binding and DNA-binding transcription-factor activity, but not the exact effector or "
            "regulated carbohydrate operon."
        ),
        "core_mf": "GO:0003700",
        "core_processes": ["GO:0006355"],
        "locations": [],
        "role": "LacI/GalR-family metabolic transcriptional regulator candidate",
        "part": "deor_laci_carbohydrate_regulators",
    },
    "PP_3532": {
        "accession": "Q88H33",
        "family": "AsnC/Lrp-family",
        "description": (
            "PP_3532 encodes a predicted AsnC/Lrp-family transcriptional regulator. The current evidence supports "
            "sequence-specific DNA binding, regulation of transcription, and cytosolic localization; amino-acid response "
            "is retained only as family-level context."
        ),
        "core_mf": "GO:0043565",
        "core_processes": ["GO:0006355"],
        "locations": ["GO:0005829"],
        "role": "AsnC/Lrp-family transcriptional regulator with unresolved target regulon",
        "part": "asnc_lrp_amino_acid_regulators",
    },
    "PP_3592": {
        "accession": "Q88GX5",
        "family": "RpiR-family",
        "description": (
            "PP_3592 encodes a predicted RpiR-family transcriptional regulator with HTH and SIS-domain carbohydrate-effector "
            "context. GOA supports DNA-binding transcription-factor activity and broad carbohydrate-derivative context, but "
            "the exact effector and regulated pathway are unresolved."
        ),
        "core_mf": "GO:0003700",
        "core_processes": ["GO:0006355"],
        "locations": [],
        "role": "RpiR-family carbohydrate/catabolic transcriptional regulator candidate",
        "part": "iclr_rpir_catabolic_regulators",
    },
    "PP_4308": {
        "accession": "Q88EZ2",
        "family": "AsnC/Lrp-family",
        "description": (
            "PP_4308 encodes a predicted AsnC/Lrp-family transcriptional regulator. Sequence-specific DNA binding, "
            "transcription-regulation context, and cytosolic localization are supported, but a specific regulated pathway "
            "is not resolved in this first pass."
        ),
        "core_mf": "GO:0043565",
        "core_processes": ["GO:0006355"],
        "locations": ["GO:0005829"],
        "role": "AsnC/Lrp-family transcriptional regulator with unresolved target regulon",
        "part": "asnc_lrp_amino_acid_regulators",
    },
    "bkdR": {
        "accession": "Q88EQ3",
        "family": "AsnC/Lrp-family",
        "description": (
            "bkdR encodes a predicted AsnC/Lrp-family transcriptional regulator annotated as a Bkd operon regulator. "
            "This pass supports sequence-specific DNA-binding transcription regulation and cytosolic localization, while "
            "leaving the exact branched-chain keto-acid regulon and effector as curation questions."
        ),
        "core_mf": "GO:0043565",
        "core_processes": ["GO:0006355"],
        "locations": ["GO:0005829"],
        "role": "BkdR/AsnC-family metabolic transcriptional regulator candidate",
        "part": "asnc_lrp_amino_acid_regulators",
    },
    "ybaO": {
        "accession": "Q88E71",
        "family": "AsnC/Lrp-family",
        "description": (
            "ybaO encodes a predicted Lrp-like AsnC-family transcriptional regulator. Available evidence supports "
            "sequence-specific DNA binding, transcription regulation, and cytosolic localization, but does not resolve "
            "the target regulon."
        ),
        "core_mf": "GO:0043565",
        "core_processes": ["GO:0006355"],
        "locations": ["GO:0005829"],
        "role": "Lrp-like transcriptional regulator with unresolved target regulon",
        "part": "asnc_lrp_amino_acid_regulators",
    },
    "PP_4776": {
        "accession": "Q88DP7",
        "family": "AsnC/Lrp-family",
        "description": (
            "PP_4776 encodes a predicted AsnC/Lrp-family transcriptional regulator. The first-pass evidence supports "
            "sequence-specific DNA binding, regulation of transcription, and cytosolic localization, but not a specific "
            "amino-acid response or regulon."
        ),
        "core_mf": "GO:0043565",
        "core_processes": ["GO:0006355"],
        "locations": ["GO:0005829"],
        "role": "AsnC/Lrp-family transcriptional regulator with unresolved target regulon",
        "part": "asnc_lrp_amino_acid_regulators",
    },
    "PP_5188": {
        "accession": "Q88CJ3",
        "family": "AsnC/Lrp-family",
        "description": (
            "PP_5188 encodes a predicted AsnC/Lrp-family transcriptional regulator. Current annotations support "
            "sequence-specific DNA binding and transcription regulation in the cytosol; the target regulon is unresolved."
        ),
        "core_mf": "GO:0043565",
        "core_processes": ["GO:0006355"],
        "locations": ["GO:0005829"],
        "role": "AsnC/Lrp-family transcriptional regulator with unresolved target regulon",
        "part": "asnc_lrp_amino_acid_regulators",
    },
    "PP_5350": {
        "accession": "Q88C33",
        "family": "RpiR-family",
        "description": (
            "PP_5350 encodes a predicted RpiR-family transcriptional regulator with carbohydrate/SIS-domain family context. "
            "GOA supports DNA-binding transcription-factor activity, transcription regulation, and broad carbohydrate "
            "binding/metabolism context; the exact effector and regulon are unresolved."
        ),
        "core_mf": "GO:0003700",
        "core_processes": ["GO:0006355"],
        "locations": [],
        "role": "RpiR-family carbohydrate/catabolic transcriptional regulator candidate",
        "part": "iclr_rpir_catabolic_regulators",
    },
    "PP_5410": {
        "accession": "Q88BX7",
        "family": "DeoR-family",
        "description": (
            "PP_5410 encodes a predicted DeoR-family carbohydrate-metabolism transcriptional regulator. The current "
            "first-pass call is generic DNA-binding transcription-factor activity in transcription regulation, with "
            "the precise carbohydrate pathway and effector unresolved."
        ),
        "core_mf": "GO:0003700",
        "core_processes": ["GO:0006355"],
        "locations": [],
        "role": "DeoR-family metabolic transcriptional regulator candidate",
        "part": "deor_laci_carbohydrate_regulators",
    },
}


PARTS = [
    (
        "asnc_lrp_amino_acid_regulators",
        "AsnC/Lrp-family amino-acid/metabolic regulators",
        "AsnC/Lrp-family HTH regulators with amino-acid-response or BkdR/Lrp-like family context but unresolved target regulons.",
        ["PP_0384", "PP_0663", "PP_1307", "PP_3362", "PP_3532", "PP_4308", "bkdR", "ybaO", "PP_4776", "PP_5188"],
    ),
    (
        "deor_laci_carbohydrate_regulators",
        "DeoR/LacI carbohydrate-family regulators",
        "DeoR, LacI/GalR, RbsR, and PtxS-family carbohydrate or organic-acid transcription regulators.",
        ["glpR", "rbsR", "ptxS", "PP_3415", "PP_5410"],
    ),
    (
        "iclr_rpir_catabolic_regulators",
        "IclR/RpiR catabolic regulators",
        "IclR/PcaR and RpiR-family transcription regulators with catabolic or carbohydrate-effector context.",
        ["PP_2601", "PP_2609", "PP_3592", "PP_5350"],
    ),
    (
        "crp_fnr_redox_regulators",
        "Crp/Fnr redox-responsive regulators",
        "Crp/Fnr-family transcription regulators with 4Fe-4S/redox family context and unresolved KT2440 regulons.",
        ["fnrB", "fnrC"],
    ),
]


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def load_review(gene: str) -> dict:
    return yaml.safe_load(gene_file(gene, "ai-review.yaml").read_text(encoding="utf-8")) or {}


def build_term_map() -> dict[str, dict[str, str]]:
    terms = dict(STATIC_TERMS)
    for gene in GENE_INFO:
        path = gene_file(gene, "ai-review.yaml")
        if not path.exists():
            continue
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for ann in data.get("existing_annotations", []):
            item = ann.get("term") or {}
            if item.get("id") and item.get("label"):
                terms[item["id"]] = term(item["id"], item["label"])
    return terms


TERM = build_term_map()


def t(go_id: str) -> dict[str, str]:
    if go_id not in TERM:
        raise KeyError(f"Missing GO term label for {go_id}")
    return TERM[go_id]


def lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return path.read_text(encoding="utf-8").splitlines()


def first_line(path: Path, *needles: str) -> str | None:
    for line in lines(path):
        if all(needle in line for needle in needles):
            return line
    return None


def support(reference_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": reference_id, "supporting_text": text}


def add_support(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item not in items:
        items.append(item)


def goa_line(gene: str, term_id: str) -> str | None:
    return first_line(gene_file(gene, "goa.tsv"), term_id)


def evidence_for(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if term_id:
        add_support(items, support(file_id(gene, "goa.tsv"), goa_line(gene, term_id)))
    uniprot = gene_file(gene, "uniprot.txt")
    for marker in ("DE   ", "GN   ", "CC   -!- FUNCTION:", "CC   -!- SIMILARITY:"):
        add_support(items, support(file_id(gene, "uniprot.txt"), first_line(uniprot, marker)))
    if term_id:
        add_support(items, support(file_id(gene, "uniprot.txt"), first_line(uniprot, f"DR   GO; {term_id};")))
    for marker in ("DR   InterPro;", "DR   Pfam;", "DR   PANTHER;"):
        add_support(items, support(file_id(gene, "uniprot.txt"), first_line(uniprot, marker)))
    keyword = first_line(uniprot, "KW   ")
    if keyword and "Reference proteome" not in keyword:
        add_support(items, support(file_id(gene, "uniprot.txt"), keyword))
    return items


def references_for(gene: str, data: dict) -> list[dict]:
    seen = set()
    refs: list[dict] = []
    for ref in data.get("references", []):
        ref_id = ref.get("id")
        if ref_id and ref_id not in seen:
            refs.append(ref)
            seen.add(ref_id)
    titles = {
        file_id(gene, "uniprot.txt"): f"UniProtKB flat-file entry for {gene} ({GENE_INFO[gene]['accession']})",
        file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({GENE_INFO[gene]['accession']})",
        file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({GENE_INFO[gene]['accession']})",
    }
    for ref_id, title in titles.items():
        if ref_id in seen:
            continue
        ref = {"id": ref_id, "title": title, "findings": []}
        if ref_id.endswith("deep-research-asta.md") and gene_file(gene, "deep-research-asta.md").exists():
            accession_line = first_line(gene_file(gene, "deep-research-asta.md"), "uniprot_accession:")
            if accession_line:
                ref["findings"].append(
                    {
                        "statement": "Asta retrieval was generated for this first-pass review and retained as lightweight gene-level context.",
                        "supporting_text": accession_line.strip(),
                    }
                )
        refs.append(ref)
        seen.add(ref_id)
    return refs


def review_for(gene: str, term_id: str) -> dict:
    info = GENE_INFO[gene]
    label = TERM.get(term_id, {"label": term_id})["label"]
    core_mf = info["core_mf"]
    core_processes = set(info["core_processes"])
    locations = set(info["locations"])

    if term_id in {core_mf, "GO:0000976"}:
        return {
            "summary": f"{label} is supported for this {info['family']} regulator.",
            "action": "ACCEPT",
            "reason": (
                "The annotation matches the protein-family/domain evidence for a DNA-binding transcriptional regulator. "
                f"The target regulon remains unresolved, so the first pass keeps the molecular-function call at this level: {info['role']}."
            ),
            "supported_by": evidence_for(gene, term_id),
        }

    if term_id in core_processes:
        return {
            "summary": f"{label} is appropriate transcription-regulation process context.",
            "action": "ACCEPT",
            "reason": (
                "The gene product is a predicted DNA-binding transcriptional regulator; this process captures the supported "
                "regulatory role without asserting a specific regulon."
            ),
            "supported_by": evidence_for(gene, term_id),
        }

    if term_id in locations:
        return {
            "summary": f"{label} is appropriate location context for this soluble bacterial regulator.",
            "action": "ACCEPT",
            "reason": "The location row is compatible with a cytosolic transcription factor.",
            "supported_by": evidence_for(gene, term_id),
        }

    if term_id == "GO:0003677":
        replacement = [t(core_mf)] if core_mf != "GO:0003677" else []
        out = {
            "summary": "Generic DNA binding is true but less informative than the transcription-regulator-specific term.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": (
                "The protein is not merely a generic DNA-binding protein; the family and GOA context support a "
                "DNA-binding transcription regulator."
            ),
            "supported_by": evidence_for(gene, term_id),
        }
        if replacement:
            out["proposed_replacement_terms"] = replacement
        return out

    if term_id == "GO:0006351":
        return {
            "summary": "DNA-templated transcription is a broad parent process for a transcription regulator.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": (
                "This regulator participates in transcriptional control, but the gene product is not core RNA polymerase "
                "or the transcription process itself. Regulation of DNA-templated transcription is the better process level."
            ),
            "proposed_replacement_terms": [t("GO:0006355")],
            "supported_by": evidence_for(gene, term_id),
        }

    if term_id == "GO:0043200":
        return {
            "summary": "Response to amino acid is retained as AsnC/Lrp-family context, not a resolved core process.",
            "action": "KEEP_AS_NON_CORE",
            "reason": (
                "AsnC/Lrp-family regulators often respond to amino acids, but the current evidence does not establish a "
                "specific amino-acid cue or response pathway for this KT2440 paralog."
            ),
            "supported_by": evidence_for(gene, term_id),
        }

    if term_id in {"GO:0045892", "GO:0045893"}:
        return {
            "summary": f"{label} is plausible directional transcription-regulation context but not resolved as the core call.",
            "action": "KEEP_AS_NON_CORE",
            "reason": (
                "The directional regulation row is derived from family/electronic evidence. Without a verified target regulon, "
                "the core function is kept as DNA-binding transcription-factor activity plus generic transcription regulation."
            ),
            "supported_by": evidence_for(gene, term_id),
        }

    if term_id in {"GO:0030246", "GO:0097367"}:
        return {
            "summary": f"{label} is compatible effector-binding context for an RpiR/DeoR-like regulator.",
            "action": "KEEP_AS_NON_CORE",
            "reason": (
                "The carbohydrate/SIS-domain family context is plausible, but the exact effector ligand for this KT2440 "
                "regulator has not been established in this pass."
            ),
            "supported_by": evidence_for(gene, term_id),
        }

    if term_id in {"GO:0005975", "GO:0046278", "GO:1901135"}:
        return {
            "summary": f"{label} is retained as family/regulon context rather than a direct core function.",
            "action": "KEEP_AS_NON_CORE",
            "reason": (
                "The gene product is a transcriptional regulator, not a metabolic enzyme. The pathway/process annotation "
                "may describe a regulated pathway, but that target relationship needs gene-specific support."
            ),
            "supported_by": evidence_for(gene, term_id),
        }

    return {
        "summary": f"{label} is compatible with the regulator-family assignment but not central to the first-pass function.",
        "action": "KEEP_AS_NON_CORE",
        "reason": f"The supported core role is {info['role']}.",
        "supported_by": evidence_for(gene, term_id),
    }


def core_function(gene: str) -> dict:
    info = GENE_INFO[gene]
    core = {
        "description": info["role"],
        "molecular_function": t(info["core_mf"]),
        "directly_involved_in": [t(go_id) for go_id in info["core_processes"]],
        "supported_by": evidence_for(gene, info["core_mf"]),
    }
    if info["locations"]:
        core["locations"] = [t(go_id) for go_id in info["locations"]]
        for go_id in info["locations"]:
            add_support(core["supported_by"], support(file_id(gene, "goa.tsv"), goa_line(gene, go_id)))
    for go_id in info["core_processes"]:
        add_support(core["supported_by"], support(file_id(gene, "goa.tsv"), goa_line(gene, go_id)))
    return core


def suggested_questions(gene: str) -> list[dict[str, object]]:
    info = GENE_INFO[gene]
    return [
        {
            "question": f"What is the direct target regulon and small-molecule effector for {gene}, the {info['role']}?",
            "experts": [],
        }
    ]


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    return [
        {
            "experiment_type": "regulon and effector mapping",
            "description": (
                f"Map {gene}-dependent transcription changes by RNA-seq, test promoter binding by EMSA/DNase footprinting, "
                "and screen candidate metabolites for altered DNA binding."
            ),
        }
    ]


def write_notes(gene: str) -> None:
    path = gene_file(gene, "notes.md")
    info = GENE_INFO[gene]
    heading = f"## {TODAY} metabolic transcriptional regulator first pass"
    provenance = []
    for item in evidence_for(gene, info["core_mf"]):
        if item["supporting_text"] and len(provenance) < 6:
            provenance.append(f"- [{item['reference_id']} \"{item['supporting_text']}\"]")
    asta_line = first_line(gene_file(gene, "deep-research-asta.md"), "uniprot_accession:")
    if asta_line:
        provenance.append(f"- [{file_id(gene, 'deep-research-asta.md')} \"{asta_line.strip()}\"]")
    block = "\n".join(
        [
            heading,
            "",
            f"- Batch: `{BATCH_TSV.relative_to(ROOT)}`.",
            f"- Main conclusion: {info['role']}.",
            "- Regulated operon, effector ligand, and activation/repression direction remain unresolved unless captured in existing curated evidence.",
            "",
            "Primary provenance:",
            *provenance,
            "",
        ]
    )
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if heading not in existing:
            path.write_text(existing.rstrip() + "\n\n" + block, encoding="utf-8")
    else:
        path.write_text(f"# {gene} notes\n\n{block}", encoding="utf-8")


def curate_gene(gene: str) -> None:
    data = load_review(gene)
    data["references"] = references_for(gene, data)
    if gene not in PRESERVE_EXISTING_REVIEWS:
        data["status"] = "DRAFT"
        data["description"] = GENE_INFO[gene]["description"]
        for ann in data.get("existing_annotations", []):
            ann["review"] = review_for(gene, ann["term"]["id"])
        data["core_functions"] = [core_function(gene)]
        data["proposed_new_terms"] = []
        data["suggested_questions"] = suggested_questions(gene)
        data["suggested_experiments"] = suggested_experiments(gene)
    gene_file(gene, "ai-review.yaml").write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120, allow_unicode=True),
        encoding="utf-8",
    )
    write_notes(gene)


def clean_id(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_]+", "_", value.lower())
    return re.sub(r"_+", "_", cleaned).strip("_")


def annoton(gene: str) -> dict:
    info = GENE_INFO[gene]
    out = {
        "id": f"{clean_id(gene)}_{clean_id(info['family'])}_regulator",
        "label": f"{gene}: {info['role']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": info["role"],
        "function": {"preferred_term": TERM[info["core_mf"]]["label"], "term": t(info["core_mf"])},
        "processes": [{"preferred_term": TERM[x]["label"], "term": t(x)} for x in info["core_processes"]],
    }
    if info["locations"]:
        out["locations"] = [{"preferred_term": TERM[x]["label"], "term": t(x)} for x in info["locations"]]
    return out


def write_module() -> None:
    evidence = [
        {
            "source_id": f"file:{BATCH_TSV.relative_to(ROOT)}",
            "title": "PSEPK regulation/signal-transduction small-family metabolic-regulator split",
            "statement": "The batch table records 21 compact metabolic transcriptional regulators curated in this first pass.",
        },
        {
            "source_id": f"file:{PARTITION_TSV.relative_to(ROOT)}",
            "title": "PSEPK regulation/signal-transduction partition table",
            "statement": "The regulation umbrella was partitioned into family-scale transcription-regulator and two-component/sigma/phage splits.",
        },
    ]
    for gene in GENE_INFO:
        evidence.append(
            {
                "source_id": file_id(gene, "ai-review.yaml"),
                "title": f"Curated {gene} review",
                "statement": GENE_INFO[gene]["role"],
            }
        )

    module = {
        "id": "MODULE:metabolic_transcriptional_regulator_boundary",
        "title": "Metabolic transcriptional regulator boundary",
        "description": (
            "Boundary module for compact PSEPK metabolic transcriptional regulators from the broad regulation/signal-transduction "
            "functional bucket. It groups AsnC/Lrp, DeoR/LacI, IclR/RpiR, and Crp/Fnr-family regulators while keeping target "
            "regulons and effector ligands unresolved unless separately curated."
        ),
        "status": "DRAFT",
        "evidence": evidence,
        "module": {
            "id": "metabolic_transcriptional_regulator_boundary",
            "label": "Metabolic transcriptional regulator boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {
                    "preferred_term": "DNA-binding transcription factor activity",
                    "term": t("GO:0003700"),
                    "description": "Generic DNA-binding transcription-regulator function used for LacI, DeoR, IclR, RpiR, and Crp/Fnr-family candidates.",
                },
                {
                    "preferred_term": "sequence-specific DNA binding",
                    "term": t("GO:0043565"),
                    "description": "Sequence-specific DNA-binding function used for AsnC/Lrp-family entries where GOA does not expose GO:0003700.",
                },
                {
                    "preferred_term": "transcription cis-regulatory region binding",
                    "term": t("GO:0000976"),
                    "description": "Cis-regulatory-region binding for LacI-family regulators with promoter/operator binding annotations.",
                },
                {
                    "preferred_term": "regulation of DNA-templated transcription",
                    "term": t("GO:0006355"),
                    "description": "Shared process context for this transcription-regulator boundary.",
                },
                {
                    "preferred_term": "carbohydrate derivative binding",
                    "term": t("GO:0097367"),
                    "description": "Non-core effector-binding context for RpiR/DeoR-like carbohydrate regulators where exact ligand is unresolved.",
                },
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": "cytosol",
                        "term": t("GO:0005829"),
                        "description": "Soluble cytosolic localization used when supported by TreeGrafter/GOA rows.",
                    }
                ]
            },
            "parts": [],
        },
        "notes": (
            "This is a boundary and triage module, not a single satisfiable metabolic pathway. Generic regulator paralogs "
            "should not be assigned pathway targets, activation/repression direction, or effector specificity without direct "
            "gene-level evidence."
        ),
    }

    for order, (part_id, label, description, genes) in enumerate(PARTS, start=1):
        module["module"]["parts"].append(
            {
                "order": order,
                "role": label,
                "node": {
                    "id": part_id,
                    "label": label,
                    "module_type": "BIOLOGICAL_PROCESS",
                    "description": description,
                    "annotons": [annoton(gene) for gene in genes],
                },
            }
        )
    MODULE_PATH.write_text(
        yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, width=120, allow_unicode=True),
        encoding="utf-8",
    )


def update_partition() -> None:
    rows = list(csv.DictReader(PARTITION_TSV.open(encoding="utf-8"), delimiter="\t"))
    for row in rows:
        if row["partition_bucket"] != "small_family_metabolic_transcriptional_regulators":
            continue
        gene = row["gene"]
        row["proposed_module"] = "metabolic_transcriptional_regulator_boundary"
        row["recommended_action"] = "COMPLETED_SUBMODULE"
        row["bucket_status"] = "CURATED"
        row["review_status"] = "PRESENT" if gene_file(gene, "ai-review.yaml").exists() else "MISSING"
        text = gene_file(gene, "ai-review.yaml").read_text(encoding="utf-8") if gene_file(gene, "ai-review.yaml").exists() else ""
        row["curation_status"] = "PENDING" if "action: PENDING" in text or "TODO: Review" in text else "CURATED"
        row["asta_research_status"] = "PRESENT" if gene_file(gene, "deep-research-asta.md").exists() else "MISSING"
    with PARTITION_TSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    for gene in GENE_INFO:
        curate_gene(gene)
    write_module()
    update_partition()


if __name__ == "__main__":
    main()
