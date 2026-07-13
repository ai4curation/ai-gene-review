#!/usr/bin/env python3
"""First-pass curation for the ppu02025 orphan regulatory-sensor bucket."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
SPECIES = "PSEPK"
GENE_ROOT = ROOT / "genes" / SPECIES
PARTITION = ROOT / "projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.tsv"
MODULE_PATH = ROOT / "modules/orphan_biofilm_regulatory_sensors_boundary.yaml"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "sensor_kinase": {"id": "GO:0000155", "label": "phosphorelay sensor kinase activity"},
    "phosphorelay": {"id": "GO:0000160", "label": "phosphorelay signal transduction system"},
    "protein_kinase": {"id": "GO:0004672", "label": "protein kinase activity"},
    "protein_his_kinase": {"id": "GO:0004673", "label": "protein histidine kinase activity"},
    "plasma_membrane": {"id": "GO:0005886", "label": "plasma membrane"},
    "signal_transduction": {"id": "GO:0007165", "label": "signal transduction"},
    "histidine_phosphotransfer": {"id": "GO:0009927", "label": "histidine phosphotransfer kinase activity"},
    "membrane": {"id": "GO:0016020", "label": "membrane"},
    "kinase": {"id": "GO:0016301", "label": "kinase activity"},
    "transferase": {"id": "GO:0016740", "label": "transferase activity"},
    "phosphorus_transferase": {
        "id": "GO:0016772",
        "label": "transferase activity, transferring phosphorus-containing groups",
    },
    "phosphatase": {"id": "GO:0016791", "label": "phosphatase activity"},
    "t6ss_process": {"id": "GO:0033103", "label": "protein secretion by the type VI secretion system"},
    "anti_sigma_antagonist": {"id": "GO:0043856", "label": "anti-sigma factor antagonist activity"},
    "positive_transcription": {"id": "GO:0045893", "label": "positive regulation of DNA-templated transcription"},
}

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000003": "Gene Ontology annotation based on Enzyme Commission mapping",
    "GO_REF:0000044": (
        "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, "
        "accompanied by conservative changes to GO terms applied by UniProt"
    ),
    "GO_REF:0000104": (
        "Electronic Gene Ontology annotations created by transferring manual GO annotations between related "
        "proteins based on shared sequence features"
    ),
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on on inter-ontology links.",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

SENSOR_REVIEW_RULES = {
    "GO:0000155": (
        "ACCEPT",
        "The conserved HisKA/HATPase architecture supports phosphorelay sensor kinase activity.",
        None,
    ),
    "GO:0000160": (
        "ACCEPT",
        "The receiver-domain sensor-kinase architecture supports a two-component phosphorelay role.",
        None,
    ),
    "GO:0004673": (
        "ACCEPT",
        "Protein histidine kinase activity is the specific catalytic activity expected for this sensor kinase.",
        None,
    ),
    "GO:0005886": (
        "ACCEPT",
        "Plasma-membrane localization is consistent with a membrane sensor histidine kinase.",
        None,
    ),
    "GO:0007165": (
        "KEEP_AS_NON_CORE",
        "Signal transduction is correct but generic; the phosphorelay-specific term is more informative.",
        None,
    ),
    "GO:0009927": (
        "ACCEPT",
        "The hybrid sensor architecture supports histidine phosphotransfer activity in the phosphorelay.",
        None,
    ),
    "GO:0016020": (
        "KEEP_AS_NON_CORE",
        "Membrane localization is plausible but generic relative to the sensor-kinase activity.",
        None,
    ),
    "GO:0016301": (
        "MARK_AS_OVER_ANNOTATED",
        "Generic kinase activity is less informative than protein histidine kinase or sensor kinase activity.",
        None,
    ),
    "GO:0016740": (
        "MARK_AS_OVER_ANNOTATED",
        "Generic transferase activity is less informative than protein histidine kinase activity.",
        None,
    ),
    "GO:0016772": (
        "MARK_AS_OVER_ANNOTATED",
        "This broad parent transferase term adds little beyond the specific histidine-kinase annotations.",
        None,
    ),
}

SENSOR_MEMBRANE_CORE_REVIEW_RULES = {
    **SENSOR_REVIEW_RULES,
    "GO:0016020": (
        "ACCEPT",
        "Membrane localization is part of the supported sensor-kinase context for this protein.",
        None,
    ),
}

NEW_TERM_TEMPLATES = {
    "membrane": {
        "qualifier": "located_in",
        "evidence_type": "ISS",
        "summary": "Membrane localization should be represented for this transmembrane sensor kinase.",
        "reason": (
            "UniProt records membrane and transmembrane topology for this sensor histidine kinase, supporting "
            "a sequence-based membrane location annotation."
        ),
    },
}

GENES = {
    "PP_1875": {
        "id": "Q88LQ4",
        "ordered_locus": "PP_1875",
        "partition_gene": "PP_1875",
        "class": "sensor",
        "description": (
            "PP_1875 encodes a membrane-associated hybrid sensor histidine kinase in Pseudomonas putida "
            "KT2440. HisKA/HATPase catalytic domains and a CheY-like receiver domain support a "
            "two-component phosphorelay role, while the input cue and downstream response regulator remain "
            "unresolved."
        ),
        "uniprot": "DE   RecName: Full=histidine kinase",
        "asta": "Protein Description:** RecName: Full=histidine kinase",
        "extra": [
            "DR   InterPro; IPR005467; His_kinase_dom.",
            "DR   InterPro; IPR003594; HATPase_dom.",
            "DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.",
            "CC   -!- SUBCELLULAR LOCATION: Membrane",
        ],
        "reviews": SENSOR_MEMBRANE_CORE_REVIEW_RULES,
        "location": "membrane",
    },
    "PP_2664": {
        "id": "Q88JI5",
        "ordered_locus": "PP_2664",
        "partition_gene": "PP_2664",
        "class": "sensor",
        "description": (
            "PP_2664 encodes a PAS/PAC-domain sensor histidine kinase in Pseudomonas putida KT2440. Its "
            "HisKA/HATPase catalytic region and receiver domain support a membrane phosphorelay sensor role, "
            "but the sensed cue and output branch are not yet assigned."
        ),
        "uniprot": "DE   RecName: Full=Sensor histidine kinase PP_2664",
        "asta": "Protein Description:** RecName: Full=Sensor histidine kinase PP_2664",
        "extra": [
            "DR   InterPro; IPR005467; His_kinase_dom.",
            "DR   InterPro; IPR000014; PAS.",
            "DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.",
        ],
        "reviews": SENSOR_REVIEW_RULES,
        "location": "plasma_membrane",
    },
    "PP_4173": {
        "id": "Q88FC5",
        "ordered_locus": "PP_4173",
        "partition_gene": "PP_4173",
        "class": "sensor",
        "description": (
            "PP_4173 encodes an RpfC-like sensory/regulatory protein in Pseudomonas putida KT2440. HAMP, "
            "BarA_N, HisKA/HATPase, and receiver-domain annotations support an inner-membrane hybrid sensor "
            "kinase role; a specific Rpf-like signal or target regulon has not been resolved for KT2440."
        ),
        "uniprot": "DE   RecName: Full=Sensory/regulatory protein RpfC",
        "asta": "Protein Description:** RecName: Full=Sensory/regulatory protein RpfC",
        "extra": [
            "CC   -!- SUBCELLULAR LOCATION: Cell inner membrane",
            "DR   InterPro; IPR005467; His_kinase_dom.",
            "DR   InterPro; IPR003660; HAMP_dom.",
            "DR   InterPro; IPR019247; Histidine_kinase_BarA_N.",
            "DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.",
        ],
        "reviews": SENSOR_REVIEW_RULES,
        "location": "plasma_membrane",
    },
    "PP_4362": {
        "id": "Q88EU1",
        "ordered_locus": "PP_4362",
        "partition_gene": "PP_4362",
        "class": "hpt",
        "description": (
            "PP_4362 encodes an HPt domain-containing phosphorelay protein in Pseudomonas putida KT2440. "
            "The Hpt domain supports a histidine phosphotransfer relay role, but the cognate sensor, response "
            "regulator, and physiological input remain unresolved."
        ),
        "uniprot": "DE   RecName: Full=HPt domain-containing protein",
        "asta": "Protein Description:** RecName: Full=HPt domain-containing protein",
        "extra": [
            "DR   InterPro; IPR008207; Sig_transdc_His_kin_Hpt_dom.",
            "DR   Pfam; PF01627; Hpt; 1.",
        ],
        "reviews": {
            "GO:0000160": (
                "ACCEPT",
                "The Hpt domain is a two-component phosphorelay module, supporting phosphorelay signal transduction.",
                None,
            ),
            "GO:0004672": (
                "MODIFY",
                "The broad protein kinase annotation should be replaced by the more specific histidine phosphotransfer activity expected for an HPt relay protein.",
                [TERMS["histidine_phosphotransfer"]],
            ),
        },
        "core_function": "histidine_phosphotransfer",
    },
    "PP_4363": {
        "id": "Q88EU0",
        "ordered_locus": "PP_4363",
        "partition_gene": "PP_4363",
        "class": "spoIIe_like",
        "description": (
            "PP_4363 encodes a SpoIIE/PPM-type phosphatase-like response regulatory protein in Pseudomonas "
            "putida KT2440. Receiver, HATPase-like, bacterial sigma-regulatory, and PPM-type phosphatase "
            "domain annotations place it in a phosphorelay or anti-sigma regulatory neighborhood, but its "
            "substrate and upstream signal are unresolved."
        ),
        "uniprot": "DE   SubName: Full=Sensor histidine kinase/response regulator",
        "asta": "Protein Description:** SubName: Full=Sensor histidine kinase/response regulator",
        "extra": [
            "DR   InterPro; IPR052016; Bact_Sigma-Reg.",
            "DR   InterPro; IPR001932; PPM-type_phosphatase-like_dom.",
            "DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.",
            "DR   Pfam; PF07228; SpoIIE; 1.",
        ],
        "reviews": {
            "GO:0000160": (
                "ACCEPT",
                "The receiver-domain architecture supports a phosphorelay signal-transduction role.",
                None,
            ),
            "GO:0016791": (
                "ACCEPT",
                "The PPM-type/SpoIIE-like domain supports phosphatase activity, although the substrate is unresolved.",
                None,
            ),
        },
        "core_function": "phosphatase",
    },
    "PP_4364": {
        "id": "Q88ET9",
        "ordered_locus": "PP_4364",
        "partition_gene": "PP_4364",
        "class": "anti_sigma_antagonist",
        "description": (
            "PP_4364 encodes a STAS-domain anti-sigma factor antagonist in Pseudomonas putida KT2440. The "
            "domain profile supports antagonist activity toward a sigma-factor control module, but the "
            "specific sigma factor and regulated gene set remain unresolved."
        ),
        "uniprot": "DE   SubName: Full=Anti-sigma F factor antagonist",
        "asta": "Protein Description:** SubName: Full=Anti-sigma F factor antagonist",
        "extra": [
            "DR   InterPro; IPR002645; STAS_dom.",
            "DR   PANTHER; PTHR33495; ANTI-SIGMA FACTOR ANTAGONIST",
        ],
        "reviews": {
            "GO:0043856": (
                "ACCEPT",
                "The STAS-domain anti-sigma antagonist family assignment supports anti-sigma factor antagonist activity.",
                None,
            ),
            "GO:0045893": (
                "KEEP_AS_NON_CORE",
                "Positive regulation of transcription is a plausible regulatory outcome of anti-sigma antagonism, but the core role is the antagonist molecular function.",
                None,
            ),
        },
        "core_function": "anti_sigma_antagonist",
    },
    "PP_4781": {
        "id": "Q88DP3",
        "ordered_locus": "PP_4781",
        "partition_gene": "PP_4781",
        "class": "sensor",
        "description": (
            "PP_4781 encodes a predicted 7TMR-DISM sensor histidine kinase in Pseudomonas putida KT2440. "
            "Extracytoplasmic sensory, transmembrane, HisKA, and HATPase domains support a membrane "
            "phosphorelay sensor role, but the ligand and response-regulator partner are unresolved."
        ),
        "uniprot": "DE   RecName: Full=histidine kinase",
        "asta": "Protein Description:** RecName: Full=histidine kinase",
        "extra": [
            "DR   InterPro; IPR011623; 7TMR_DISM_rcpt_extracell_dom1.",
            "DR   InterPro; IPR005467; His_kinase_dom.",
            "DR   InterPro; IPR050736; Sensor_HK_Regulatory.",
            "KW   Membrane",
        ],
        "reviews": SENSOR_REVIEW_RULES,
        "location": "membrane",
        "new_terms": ["membrane"],
    },
}


def goa_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-goa.tsv"


def uniprot_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-uniprot.txt"


def asta_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md"


def support(ref_id: str, text: str) -> dict[str, str]:
    return {"reference_id": ref_id, "supporting_text": text}


def first_line(path: Path, token: str) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if token in line:
            return line
    raise ValueError(f"Could not find {token!r} in {path}")


def goa_rows(gene: str) -> dict[str, str]:
    path = GENE_ROOT / gene / f"{gene}-goa.tsv"
    rows: dict[str, str] = {}
    with path.open(encoding="utf-8") as handle:
        header = next(handle)
        if "GO TERM" not in header:
            raise ValueError(f"Unexpected GOA header in {path}: {header}")
        for line in handle:
            if not line.strip():
                continue
            columns = line.rstrip("\n").split("\t")
            rows[columns[4]] = line.rstrip("\n")
    return rows


def line_support(gene: str, filename: str, token: str) -> dict[str, str]:
    path = GENE_ROOT / gene / filename
    return support(f"file:{SPECIES}/{gene}/{filename}", first_line(path, token))


def base_support(gene: str, cfg: dict) -> list[dict[str, str]]:
    items = [
        line_support(gene, f"{gene}-uniprot.txt", cfg["uniprot"]),
        line_support(gene, f"{gene}-deep-research-asta.md", cfg["asta"]),
    ]
    for token in cfg["extra"]:
        items.append(line_support(gene, f"{gene}-uniprot.txt", token))
    return items


def ensure_reference(doc: dict, ref_id: str, title: str, finding_text: str | None = None) -> None:
    refs = doc.setdefault("references", [])
    for ref in refs:
        if ref.get("id") == ref_id:
            ref["title"] = title
            if finding_text and not ref.get("findings"):
                ref["findings"] = [{"supporting_text": finding_text}]
            return
    ref = {"id": ref_id, "title": title, "findings": []}
    if finding_text:
        ref["findings"].append({"supporting_text": finding_text})
    refs.append(ref)


def normalize_references(doc: dict, gene: str, cfg: dict) -> None:
    for ref in doc.get("references", []):
        ref_id = str(ref.get("id", ""))
        if ref_id in GO_REF_TITLES:
            ref["title"] = GO_REF_TITLES[ref_id]
    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(
        doc,
        uniprot_ref(gene),
        f"UniProtKB entry for {gene} ({cfg['id']})",
        line_support(gene, f"{gene}-uniprot.txt", cfg["uniprot"])["supporting_text"],
    )
    ensure_reference(
        doc,
        asta_ref(gene),
        f"Asta retrieval report for {gene} ({cfg['id']})",
        line_support(gene, f"{gene}-deep-research-asta.md", cfg["asta"])["supporting_text"],
    )


def make_review(gene: str, cfg: dict, rows: dict[str, str], go_id: str) -> dict:
    action, reason, replacements = cfg["reviews"][go_id]
    review = {
        "summary": reason,
        "action": action,
        "reason": reason,
        "supported_by": [support(goa_ref(gene), rows[go_id]), *base_support(gene, cfg)],
    }
    if replacements:
        review["proposed_replacement_terms"] = replacements
    return review


def new_annotation(gene: str, cfg: dict, term: dict, template: dict) -> dict:
    return {
        "term": term,
        "evidence_type": template["evidence_type"],
        "original_reference_id": uniprot_ref(gene),
        "qualifier": template["qualifier"],
        "review": {
            "summary": template["summary"],
            "action": "NEW",
            "reason": template["reason"],
            "supported_by": base_support(gene, cfg),
        },
    }


def remove_authored_new_annotations(data: dict, term_ids: set[str]) -> None:
    data["existing_annotations"] = [
        annotation
        for annotation in data.get("existing_annotations", [])
        if not (
            annotation.get("term", {}).get("id") in term_ids
            and annotation.get("review", {}).get("action") == "NEW"
        )
    ]


def sensor_core(gene: str, cfg: dict, rows: dict[str, str]) -> list[dict]:
    location = TERMS[cfg.get("location", "membrane")]
    supports = [support(goa_ref(gene), rows["GO:0000155"]), support(goa_ref(gene), rows["GO:0000160"])]
    if location["id"] in rows:
        supports.append(support(goa_ref(gene), rows[location["id"]]))
    return [
        {
            "description": "Membrane sensor histidine kinase activity in a two-component phosphorelay branch.",
            "molecular_function": TERMS["sensor_kinase"],
            "directly_involved_in": [TERMS["phosphorelay"]],
            "locations": [location],
            "supported_by": [*supports, *base_support(gene, cfg)],
        }
    ]


def hpt_core(gene: str, cfg: dict, rows: dict[str, str]) -> list[dict]:
    return [
        {
            "description": "HPt-domain histidine phosphotransfer relay activity in a two-component phosphorelay branch.",
            "molecular_function": TERMS["histidine_phosphotransfer"],
            "directly_involved_in": [TERMS["phosphorelay"]],
            "supported_by": [support(goa_ref(gene), rows["GO:0000160"]), *base_support(gene, cfg)],
        }
    ]


def spoIIe_core(gene: str, cfg: dict, rows: dict[str, str]) -> list[dict]:
    return [
        {
            "description": "SpoIIE/PPM-type phosphatase-like activity in a phosphorelay regulatory context.",
            "molecular_function": TERMS["phosphatase"],
            "directly_involved_in": [TERMS["phosphorelay"]],
            "supported_by": [
                support(goa_ref(gene), rows["GO:0016791"]),
                support(goa_ref(gene), rows["GO:0000160"]),
                *base_support(gene, cfg),
            ],
        }
    ]


def anti_sigma_core(gene: str, cfg: dict, rows: dict[str, str]) -> list[dict]:
    return [
        {
            "description": "STAS-domain anti-sigma factor antagonist activity with an unresolved cognate sigma-factor branch.",
            "molecular_function": TERMS["anti_sigma_antagonist"],
            "supported_by": [support(goa_ref(gene), rows["GO:0043856"]), *base_support(gene, cfg)],
        }
    ]


def core_functions(gene: str, cfg: dict, rows: dict[str, str]) -> list[dict]:
    if cfg["class"] == "sensor":
        return sensor_core(gene, cfg, rows)
    if cfg["class"] == "hpt":
        return hpt_core(gene, cfg, rows)
    if cfg["class"] == "spoIIe_like":
        return spoIIe_core(gene, cfg, rows)
    if cfg["class"] == "anti_sigma_antagonist":
        return anti_sigma_core(gene, cfg, rows)
    raise ValueError(cfg["class"])


def suggested_question(gene: str, cfg: dict) -> str:
    if cfg["class"] == "anti_sigma_antagonist":
        return f"Which sigma-factor branch and target regulon are controlled by {gene} in KT2440?"
    if cfg["class"] == "hpt":
        return f"Which sensor kinase and response regulator use {gene} as an HPt relay protein in KT2440?"
    if cfg["class"] == "spoIIe_like":
        return f"What is the phosphatase substrate and upstream regulatory input for {gene} in KT2440?"
    return f"What input signal and response-regulator partner define the {gene} phosphorelay branch in KT2440?"


def suggested_experiment(gene: str, cfg: dict) -> str:
    if cfg["class"] == "anti_sigma_antagonist":
        return f"Delete {gene} and assay candidate sigma-factor reporter activity and transcript changes under surface, stress, and stationary-phase conditions."
    if cfg["class"] == "hpt":
        return f"Construct {gene} phospho-site mutants and test phosphotransfer with candidate neighboring sensor and response-regulator proteins."
    if cfg["class"] == "spoIIe_like":
        return f"Construct {gene} catalytic-site and receiver-domain mutants, then profile transcriptional and phosphoprotein changes to identify the regulated substrate branch."
    return f"Construct {gene} deletion and phospho-site mutants, then profile transcript changes and test phosphotransfer to candidate response regulators."


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    rows = goa_rows(gene)

    data["gene_symbol"] = gene
    data["aliases"] = [cfg["ordered_locus"]]
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    normalize_references(data, gene, cfg)

    authored_ids = {TERMS[key]["id"] for key in cfg.get("new_terms", [])}
    if authored_ids:
        remove_authored_new_annotations(data, authored_ids)

    for annotation in data.get("existing_annotations", []):
        go_id = annotation["term"]["id"]
        if go_id not in rows or go_id not in cfg["reviews"]:
            raise KeyError(f"Unhandled annotation {go_id} for {gene}")
        annotation["review"] = make_review(gene, cfg, rows, go_id)

    existing_ids = {annotation["term"]["id"] for annotation in data.get("existing_annotations", [])}
    for term_key in cfg.get("new_terms", []):
        if TERMS[term_key]["id"] in existing_ids:
            continue
        data.setdefault("existing_annotations", []).append(
            new_annotation(gene, cfg, TERMS[term_key], NEW_TERM_TEMPLATES[term_key])
        )
        existing_ids.add(TERMS[term_key]["id"])

    data["core_functions"] = core_functions(gene, cfg, rows)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": suggested_question(gene, cfg)}]
    data["suggested_experiments"] = [
        {
            "description": suggested_experiment(gene, cfg),
            "experiment_type": "targeted phosphorelay or regulatory assay",
        }
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=110),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def append_unique_support(items: list[dict], new_item: dict) -> None:
    for item in items:
        if item.get("reference_id") == new_item["reference_id"] and item.get("supporting_text") == new_item["supporting_text"]:
            return
    items.append(new_item)


def wire_retS_asta() -> None:
    gene = "retS"
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    data["description"] = (
        "retS (PP_4824) encodes a membrane-anchored hybrid sensor histidine kinase of the RetS/Gac "
        "signaling family in Pseudomonas putida KT2440. Domain architecture and orthology support "
        "phosphorelay sensor kinase activity, with an N-terminal 7TMR-DISM sensory region, a C-terminal "
        "histidine kinase module, and two receiver domains. Direct KT2440 evidence supports an upstream "
        "negative regulatory role for RetS in K1 type VI secretion system expression during exponential "
        "growth, while the sensory ligand and broader output regulon remain unresolved."
    )
    asta_line = line_support(gene, f"{gene}-deep-research-asta.md", "Protein Description:** RecName: Full=histidine kinase")
    ensure_reference(
        data,
        asta_ref(gene),
        "Asta retrieval report for retS (PP_4824 / Q88DK1)",
        asta_line["supporting_text"],
    )
    for annotation in data.get("existing_annotations", []):
        if annotation.get("term", {}).get("id") in {"GO:0000155", "GO:0000160", "GO:0004673", "GO:0007165"}:
            append_unique_support(annotation.setdefault("review", {}).setdefault("supported_by", []), asta_line)
    for core in data.get("core_functions", []):
        append_unique_support(core.setdefault("supported_by", []), asta_line)
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=110),
        encoding="utf-8",
    )
    print(f"Wired Asta support into {path.relative_to(ROOT)}")


def slug(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_")


def term_entry(term: dict) -> dict:
    return {"preferred_term": term["label"], "term": term}


def annoton(gene: str, label: str, function: dict, processes: list[dict], locations: list[dict], role: str) -> dict:
    item = {
        "id": slug(label),
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "processes": [term_entry(term) for term in processes],
        "locations": [term_entry(term) for term in locations],
        "role_description": role,
        "function": term_entry(function),
    }
    return item


def sensor_annoton(gene: str, location: str, role: str) -> dict:
    return annoton(
        gene,
        f"{gene}: orphan sensor histidine kinase",
        TERMS["sensor_kinase"],
        [TERMS["phosphorelay"]],
        [TERMS[location]],
        role,
    )


def build_module() -> None:
    module = {
        "id": "MODULE:orphan_biofilm_regulatory_sensors_boundary",
        "title": "Orphan biofilm regulatory sensors boundary",
        "description": (
            "Boundary module for the ppu02025 orphan regulatory-sensor partition in Pseudomonas putida "
            "KT2440. It records RetS/7TMR-DISM and other unresolved sensor histidine kinases plus a "
            "PP_4362-PP_4364 HPt/SpoIIE/STAS regulatory neighborhood."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02025",
                "title": "Biofilm formation - Pseudomonas aeruginosa",
                "statement": (
                    "KEGG ppu02025 supplies umbrella membership, but this bucket is treated as regulatory "
                    "context rather than direct evidence that every gene has a validated biofilm role in KT2440."
                ),
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.tsv",
                "title": "PSEPK ppu02025 partition table",
                "statement": (
                    "The partition table groups PP_1875, PP_2664, PP_4173, PP_4362, PP_4363, PP_4364, "
                    "PP_4781, and PP_4824/retS into the orphan regulatory-sensor bucket."
                ),
            },
        ],
        "notes": (
            "The module is intentionally conservative. Except for retS, the first-pass reviews do not assign "
            "specific biofilm output, ligand identity, response-regulator partner, or regulon. PP_4824 is "
            "represented by the existing retS review folder."
        ),
        "module": {
            "id": "orphan_biofilm_regulatory_sensors_boundary",
            "label": "Orphan biofilm regulatory sensors boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                term_entry(TERMS["sensor_kinase"]),
                term_entry(TERMS["phosphorelay"]),
                term_entry(TERMS["protein_his_kinase"]),
                term_entry(TERMS["histidine_phosphotransfer"]),
                term_entry(TERMS["phosphatase"]),
                term_entry(TERMS["anti_sigma_antagonist"]),
                term_entry(TERMS["positive_transcription"]),
                term_entry(TERMS["t6ss_process"]),
            ],
            "context": {
                "cellular_components": [
                    term_entry(TERMS["plasma_membrane"]),
                    term_entry(TERMS["membrane"]),
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "Orphan membrane sensor histidine kinases",
                    "node": {
                        "id": "orphan_membrane_sensor_histidine_kinases",
                        "label": "Orphan membrane sensor histidine kinases",
                        "module_type": "REGULATORY_STEP",
                        "description": (
                            "Predicted membrane or transmembrane sensor histidine kinases retained from the "
                            "ppu02025 umbrella map with unresolved cues and output branches."
                        ),
                        "annotons": [
                            sensor_annoton("PP_1875", "membrane", "Hybrid sensor kinase with unresolved input signal."),
                            sensor_annoton("PP_2664", "plasma_membrane", "PAS/PAC-domain sensor kinase with unresolved cue."),
                            sensor_annoton("PP_4173", "plasma_membrane", "RpfC-like hybrid sensor kinase with unresolved KT2440 regulon."),
                            sensor_annoton("PP_4781", "membrane", "7TMR-DISM sensor kinase with unresolved ligand and partner."),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "retS regulatory branch",
                    "node": {
                        "id": "rets_regulatory_branch",
                        "label": "retS regulatory branch",
                        "module_type": "REGULATORY_STEP",
                        "description": (
                            "RetS/PP_4824 is the best-supported gene-specific regulatory node in this bucket, "
                            "with KT2440 evidence for upstream negative control of K1-T6SS expression."
                        ),
                        "annotons": [
                            annoton(
                                "retS",
                                "retS: K1-T6SS upstream regulatory sensor kinase",
                                TERMS["sensor_kinase"],
                                [TERMS["phosphorelay"], TERMS["t6ss_process"]],
                                [TERMS["plasma_membrane"]],
                                "Membrane hybrid sensor kinase acting upstream of K1-T6SS expression.",
                            )
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "PP_4362-PP_4364 HPt/SpoIIE/STAS regulatory neighborhood",
                    "node": {
                        "id": "pp4362_pp4364_hpt_spoiie_stas_neighborhood",
                        "label": "PP_4362-PP_4364 HPt/SpoIIE/STAS neighborhood",
                        "module_type": "REGULATORY_STEP",
                        "description": (
                            "Adjacent HPt, SpoIIE/PPM-like, and STAS anti-sigma antagonist proteins retained "
                            "as a candidate phosphorelay or anti-sigma regulatory neighborhood."
                        ),
                        "annotons": [
                            annoton(
                                "PP_4362",
                                "PP_4362: HPt phosphotransfer protein",
                                TERMS["histidine_phosphotransfer"],
                                [TERMS["phosphorelay"]],
                                [],
                                "HPt-domain phosphotransfer protein with unresolved cognate partners.",
                            ),
                            annoton(
                                "PP_4363",
                                "PP_4363: SpoIIE-like phosphatase regulator",
                                TERMS["phosphatase"],
                                [TERMS["phosphorelay"]],
                                [],
                                "PPM/SpoIIE-like regulatory phosphatase with unresolved substrate.",
                            ),
                            annoton(
                                "PP_4364",
                                "PP_4364: anti-sigma factor antagonist",
                                TERMS["anti_sigma_antagonist"],
                                [TERMS["positive_transcription"]],
                                [],
                                "STAS-domain anti-sigma antagonist with unresolved cognate sigma branch.",
                            ),
                        ],
                    },
                },
            ],
        },
    }
    MODULE_PATH.write_text(
        yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=110),
        encoding="utf-8",
    )
    print(f"Wrote {MODULE_PATH.relative_to(ROOT)}")


def verify_partition_rows() -> None:
    rows = list(csv.DictReader(PARTITION.open(encoding="utf-8"), delimiter="\t"))
    bucket = {row["gene"] for row in rows if row["partition_bucket"] == "orphan_biofilm_regulatory_sensors"}
    expected = {cfg["partition_gene"] for cfg in GENES.values()} | {"PP_4824"}
    if bucket != expected:
        raise ValueError(f"Partition bucket mismatch: expected {sorted(expected)}, found {sorted(bucket)}")


def main() -> None:
    verify_partition_rows()
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    wire_retS_asta()
    build_module()


if __name__ == "__main__":
    main()
