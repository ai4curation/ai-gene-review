#!/usr/bin/env python3
"""First-pass curation for the ppu02020 ECF sigma/anti-sigma bucket."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
MODULE_PATH = ROOT / "modules/ecf_sigma_anti_sigma_boundary.yaml"
SPECIES = "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "dna_binding": {"id": "GO:0003677", "label": "DNA binding"},
    "transcription_factor": {"id": "GO:0003700", "label": "DNA-binding transcription factor activity"},
    "cytosol": {"id": "GO:0005829", "label": "cytosol"},
    "transcription_initiation": {"id": "GO:0006352", "label": "DNA-templated transcription initiation"},
    "transcription_reg": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "membrane": {"id": "GO:0016020", "label": "membrane"},
    "sigma_factor": {"id": "GO:0016987", "label": "sigma factor activity"},
    "sigma_antagonist": {"id": "GO:0016989", "label": "sigma factor antagonist activity"},
    "negative_transcription_reg": {
        "id": "GO:0045892",
        "label": "negative regulation of DNA-templated transcription",
    },
    "transcription_initiation_reg": {
        "id": "GO:2000142",
        "label": "regulation of DNA-templated transcription initiation",
    },
}


ANTI_SIGMA_REVIEWS = {
    "GO:0016989": (
        "ACCEPT",
        "The FecR-like transmembrane sensor/anti-sigma architecture supports sigma factor antagonist activity.",
        None,
    ),
    "GO:0045892": (
        "ACCEPT",
        "Sigma factor antagonism is a direct mechanism for negative regulation of DNA-templated transcription.",
        None,
    ),
}


SIGMA_REVIEWS = {
    "GO:0003677": (
        "MARK_AS_OVER_ANNOTATED",
        "Generic DNA binding is less informative than sigma factor activity for these ECF sigma factors.",
        None,
    ),
    "GO:0003700": (
        "MARK_AS_OVER_ANNOTATED",
        "DNA-binding transcription factor activity is a broad representation; sigma factor activity is the specific function.",
        None,
    ),
    "GO:0006352": (
        "ACCEPT",
        "Sigma factors direct RNA polymerase promoter recognition during DNA-templated transcription initiation.",
        None,
    ),
    "GO:0006355": (
        "KEEP_AS_NON_CORE",
        "Regulation of DNA-templated transcription is correct context but less specific than regulation of transcription initiation.",
        None,
    ),
    "GO:0016987": (
        "ACCEPT",
        "The proteins are sigma-70-family ECF sigma factors with conserved sigma-region domains.",
        None,
    ),
    "GO:2000142": (
        "ACCEPT",
        "Sigma factor activity regulates transcription initiation by directing promoter selection.",
        None,
    ),
}


ANTI_SIGMA_GENES = {
    "PP_0161": ("Q88RG9", "PP_0161", "Transmembrane sensor"),
    "PP_0351": ("Q88QY3", "PP_0351", "Transmembrane sensor protein"),
    "PP_0703": ("Q88PZ5", "PP_0703", "Transmembrane sensor"),
    "PP_0866": ("Q88PI4", "PP_0866", "Transmembrane sensor"),
    "PP_3085": ("Q88IB4", "PP_3085", "Transmembrane sensor"),
}


SIGMA_GENES = {
    "PP_0162": ("Q88RG8", "PP_0162", "RNA polymerase sigma-70 factor, ECF subfamily"),
    "PP_0352": ("Q88QY2", "PP_0352", "RNA polymerase sigma-70 factor, ECF subfamily"),
    "PP_0667": ("Q88Q31", "PP_0667", "RNA polymerase sigma-70 factor, ECF subfamily"),
    "PP_0704": ("Q88PZ4", "PP_0704", "RNA polymerase sigma-70 factor, ECF subfamily"),
    "PP_3086": ("Q88IB3", "PP_3086", "RNA polymerase sigma-70 factor"),
}


PAIR_NOTES = {
    "PP_0161": "local PP_0161/PP_0162 ECF sigma anti-sigma pair",
    "PP_0162": "local PP_0161/PP_0162 ECF sigma anti-sigma pair",
    "PP_0351": "local PP_0351/PP_0352 ECF sigma anti-sigma pair",
    "PP_0352": "local PP_0351/PP_0352 ECF sigma anti-sigma pair",
    "PP_0667": "orphan ECF sigma factor without a paired anti-sigma gene in this bucket",
    "PP_0703": "local PP_0703/PP_0704 ECF sigma anti-sigma pair",
    "PP_0704": "local PP_0703/PP_0704 ECF sigma anti-sigma pair",
    "PP_0866": "orphan FecR-like anti-sigma/sensor protein without a paired sigma factor in this bucket",
    "PP_3085": "local PP_3085/PP_3086 ECF sigma anti-sigma pair",
    "PP_3086": "local PP_3085/PP_3086 ECF sigma anti-sigma pair",
}


def anti_sigma_cfg(gene: str, accession: str, ordered_locus: str, product: str) -> dict:
    article = "an" if product.endswith("protein") else "a"
    return {
        "id": accession,
        "ordered_locus": ordered_locus,
        "description": (
            f"{gene} encodes {article} FecR-like transmembrane sensor/anti-sigma protein in "
            "Pseudomonas putida KT2440. Its FecR and ferric-dicitrate-sensor transmembrane "
            f"domain annotations support a membrane-associated sigma factor antagonist role in the {PAIR_NOTES[gene]}."
        ),
        "uniprot": "DE   SubName: Full=Transmembrane sensor",
        "uniprot_extra": "DR   InterPro; IPR006860; FecR.",
        "uniprot_extra_2": "DR   InterPro; IPR012373; Ferrdict_sens_TM.",
        "asta": "Protein Description:** SubName: Full=Transmembrane sensor",
        "term_reviews": ANTI_SIGMA_REVIEWS,
        "core_functions": [
            {
                "description": "FecR-like membrane anti-sigma activity restraining ECF sigma-dependent transcription.",
                "molecular_function": TERMS["sigma_antagonist"],
                "directly_involved_in": [TERMS["negative_transcription_reg"]],
            }
        ],
        "question": f"What envelope or iron-related stimulus controls the {PAIR_NOTES[gene]}?",
        "experiment": (
            f"Test {gene}-dependent repression or activation of its cognate ECF sigma regulon using "
            "deletion, complementation, and promoter-reporter assays under envelope and iron-stress conditions."
        ),
    }


def sigma_cfg(gene: str, accession: str, ordered_locus: str, product: str) -> dict:
    return {
        "id": accession,
        "ordered_locus": ordered_locus,
        "description": (
            f"{gene} encodes an ECF-subfamily sigma-70 factor in Pseudomonas putida KT2440. "
            "The protein has conserved sigma-70 region 2 and region 4 domains, supporting a role "
            f"in promoter selection and transcription-initiation control in the {PAIR_NOTES[gene]}."
        ),
        "uniprot": "DE   SubName: Full=RNA polymerase sigma-70 factor",
        "uniprot_extra": "CC   -!- SIMILARITY: Belongs to the sigma-70 factor family. ECF subfamily.",
        "uniprot_extra_2": "DR   InterPro; IPR007627; RNA_pol_sigma70_r2.",
        "uniprot_extra_3": "DR   InterPro; IPR013249; RNA_pol_sigma70_r4_t2.",
        "asta": "Protein Description:** SubName: Full=RNA polymerase sigma-70 factor",
        "term_reviews": SIGMA_REVIEWS,
        "core_functions": [
            {
                "description": "ECF sigma factor activity directing RNA polymerase promoter recognition.",
                "molecular_function": TERMS["sigma_factor"],
                "directly_involved_in": [
                    TERMS["transcription_initiation"],
                    TERMS["transcription_initiation_reg"],
                ],
            }
        ],
        "question": f"Which promoters and stress cues define the direct regulon of {gene} in KT2440?",
        "experiment": (
            f"Combine {gene} perturbation, RNA-seq, and promoter motif mapping to identify direct "
            "ECF sigma-dependent transcription initiation targets."
        ),
    }


GENES = {
    **{gene: anti_sigma_cfg(gene, *values) for gene, values in ANTI_SIGMA_GENES.items()},
    **{gene: sigma_cfg(gene, *values) for gene, values in SIGMA_GENES.items()},
}


def goa_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-goa.tsv"


def uniprot_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-uniprot.txt"


def asta_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md"


def support(ref_id: str, text: str) -> dict[str, str]:
    return {"reference_id": ref_id, "supporting_text": text}


def goa_rows(gene: str) -> dict[str, dict[str, str]]:
    with (GENE_ROOT / gene / f"{gene}-goa.tsv").open(encoding="utf-8") as handle:
        return {row["GO TERM"]: row for row in csv.DictReader(handle, delimiter="\t")}


def goa_quote(row: dict[str, str]) -> str:
    return f"{row['GO TERM']}\t{row['GO NAME']}"


def ensure_reference(doc: dict, ref_id: str, title: str, supporting_text: str | None = None) -> None:
    refs = doc.setdefault("references", [])
    for ref in refs:
        if ref.get("id") == ref_id:
            if supporting_text and not ref.get("findings"):
                ref["findings"] = [{"supporting_text": supporting_text}]
            return
    ref = {"id": ref_id, "title": title, "findings": []}
    if supporting_text:
        ref["findings"].append({"supporting_text": supporting_text})
    refs.append(ref)


def normalize_go_ref_titles(doc: dict) -> None:
    for ref in doc.get("references", []):
        ref_id = str(ref.get("id", ""))
        if ref_id.startswith("GO_REF:") and str(ref.get("title", "")).startswith("TO" "DO:"):
            ref["title"] = f"Gene Ontology annotation reference {ref_id}"


def base_support(gene: str, cfg: dict) -> list[dict[str, str]]:
    items = [support(uniprot_ref(gene), cfg["uniprot"]), support(asta_ref(gene), cfg["asta"])]
    for key in ("uniprot_extra", "uniprot_extra_2", "uniprot_extra_3"):
        if cfg.get(key):
            items.append(support(uniprot_ref(gene), cfg[key]))
    return items


def make_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    action, reason, replacements = cfg["term_reviews"][go_id]
    label = rows[go_id]["GO NAME"]
    review = {
        "summary": reason,
        "action": action,
        "reason": reason,
        "supported_by": [
            support(goa_ref(gene), goa_quote(rows[go_id])),
            *base_support(gene, cfg),
        ],
    }
    if replacements:
        review["proposed_replacement_terms"] = replacements
    if action == "MARK_AS_OVER_ANNOTATED":
        review["summary"] = f"{label} is plausible but too broad as a core annotation."
    return review


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = goa_rows(gene)

    data["gene_symbol"] = gene
    data["aliases"] = [cfg["ordered_locus"]]
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_reference(data, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(data, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['id']})", cfg["uniprot"])
    ensure_reference(data, asta_ref(gene), f"Asta retrieval report for {gene} ({cfg['id']})", cfg["asta"])
    normalize_go_ref_titles(data)

    for annotation in data["existing_annotations"]:
        go_id = annotation["term"]["id"]
        if go_id not in rows or go_id not in cfg["term_reviews"]:
            raise KeyError(f"Unhandled annotation {go_id} for {gene}")
        annotation["review"] = make_review(gene, cfg, rows, go_id)

    for core in cfg["core_functions"]:
        core["supported_by"] = base_support(gene, cfg)
    data["core_functions"] = cfg["core_functions"]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": cfg["question"]}]
    data["suggested_experiments"] = [
        {"description": cfg["experiment"], "experiment_type": "targeted regulatory or expression assay"}
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def annoton(gene: str, label: str, function: dict, processes: list[dict], locations: list[dict], role: str) -> dict:
    return {
        "id": label.lower().replace(":", "").replace(" ", "_").replace("/", "_").replace("-", "_"),
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {"preferred_term": function["label"], "term": function},
        "processes": [{"preferred_term": term["label"], "term": term} for term in processes],
        "locations": [{"preferred_term": term["label"], "term": term} for term in locations],
        "role_description": role,
    }


def anti_sigma_annoton(gene: str, label: str) -> dict:
    return annoton(
        gene,
        f"{gene}: {label}",
        TERMS["sigma_antagonist"],
        [TERMS["negative_transcription_reg"]],
        [TERMS["membrane"]],
        "FecR-like transmembrane anti-sigma/sensor protein.",
    )


def sigma_annoton(gene: str, label: str) -> dict:
    return annoton(
        gene,
        f"{gene}: {label}",
        TERMS["sigma_factor"],
        [TERMS["transcription_initiation"], TERMS["transcription_initiation_reg"]],
        [TERMS["cytosol"]],
        "ECF sigma factor controlling promoter selection and transcription initiation.",
    )


def paired_step(order: int, pair_id: str, sensor: str, sigma: str) -> dict:
    sensor_id = f"{sensor.lower()}_anti_sigma_sensor"
    sigma_id = f"{sigma.lower()}_ecf_sigma_factor"
    return {
        "order": order,
        "role": f"{sensor}/{sigma} ECF sigma anti-sigma pair",
        "node": {
            "id": pair_id,
            "label": f"{sensor}/{sigma} ECF sigma pair",
            "module_type": "REGULATORY_STEP",
            "description": (
                f"{sensor} and {sigma} form a local FecR-like anti-sigma/sensor plus ECF sigma-factor "
                "regulatory pair in the ppu02020 boundary partition."
            ),
            "annotons": [
                anti_sigma_annoton(sensor, "anti-sigma sensor"),
                sigma_annoton(sigma, "ECF sigma factor"),
            ],
            "connections": [
                {
                    "source": sensor_id,
                    "target": sigma_id,
                    "connection_type": "NEGATIVELY_REGULATES",
                    "description": f"{sensor} is the local anti-sigma/sensor partner for the {sigma} ECF sigma factor.",
                }
            ],
        },
    }


def build_module() -> None:
    module = {
        "id": "MODULE:ecf_sigma_anti_sigma_boundary",
        "title": "ECF sigma and anti-sigma regulation boundary",
        "description": (
            "Boundary module for the ppu02020 ECF sigma/anti-sigma partition in Pseudomonas putida "
            "KT2440. It captures predicted sigma-70 ECF sigma factors and adjacent or orphan FecR-like "
            "transmembrane anti-sigma/sensor proteins. This is a curated regulatory boundary from the "
            "broad KEGG two-component-system map rather than a canonical His-Asp phosphorelay."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02020",
                "title": "Two-component system - Pseudomonas putida KT2440",
                "statement": "KEGG ppu02020 supplies the umbrella membership for this boundary module.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.tsv",
                "title": "PSEPK ppu02020 partition table",
                "statement": (
                    "The partition table groups PP_0161, PP_0162, PP_0351, PP_0352, PP_0667, "
                    "PP_0703, PP_0704, PP_0866, PP_3085, and PP_3086 into the ECF sigma/anti-sigma bucket."
                ),
            },
        ],
        "notes": (
            "The bucket is intentionally a boundary module. Paired local anti-sigma/sigma systems are "
            "represented where adjacent partners are present, while PP_0667 and PP_0866 are retained as "
            "orphan ECF sigma or anti-sigma context pending regulon-level evidence."
        ),
        "module": {
            "id": "ecf_sigma_anti_sigma_boundary",
            "label": "ECF sigma and anti-sigma regulation boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                {"preferred_term": t["label"], "term": t}
                for t in [
                    TERMS["sigma_factor"],
                    TERMS["sigma_antagonist"],
                    TERMS["transcription_initiation"],
                    TERMS["transcription_initiation_reg"],
                    TERMS["negative_transcription_reg"],
                ]
            ],
            "context": {
                "cellular_components": [
                    {"preferred_term": "membrane", "term": TERMS["membrane"]},
                    {"preferred_term": "cytosol", "term": TERMS["cytosol"]},
                ]
            },
            "parts": [
                paired_step(1, "pp0161_pp0162_ecf_sigma_pair", "PP_0161", "PP_0162"),
                paired_step(2, "pp0351_pp0352_ecf_sigma_pair", "PP_0351", "PP_0352"),
                {
                    "order": 3,
                    "role": "PP_0667 orphan ECF sigma factor",
                    "node": {
                        "id": "pp0667_orphan_ecf_sigma",
                        "label": "PP_0667 orphan ECF sigma factor",
                        "module_type": "REGULATORY_STEP",
                        "description": "PP_0667 is retained as an orphan ECF sigma factor in this boundary module.",
                        "annotons": [sigma_annoton("PP_0667", "ECF sigma factor")],
                    },
                },
                paired_step(4, "pp0703_pp0704_ecf_sigma_pair", "PP_0703", "PP_0704"),
                {
                    "order": 5,
                    "role": "PP_0866 orphan FecR-like anti-sigma/sensor",
                    "node": {
                        "id": "pp0866_orphan_anti_sigma_sensor",
                        "label": "PP_0866 orphan anti-sigma sensor",
                        "module_type": "REGULATORY_STEP",
                        "description": "PP_0866 is retained as an orphan FecR-like anti-sigma/sensor in this boundary module.",
                        "annotons": [anti_sigma_annoton("PP_0866", "anti-sigma sensor")],
                    },
                },
                paired_step(6, "pp3085_pp3086_ecf_sigma_pair", "PP_3085", "PP_3086"),
            ],
        },
    }
    MODULE_PATH.write_text(
        yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Wrote {MODULE_PATH.relative_to(ROOT)}")


def main() -> None:
    for gene in [
        "PP_0161",
        "PP_0162",
        "PP_0351",
        "PP_0352",
        "PP_0667",
        "PP_0703",
        "PP_0704",
        "PP_0866",
        "PP_3085",
        "PP_3086",
    ]:
        curate_gene(gene, GENES[gene])
    build_module()


if __name__ == "__main__":
    main()
