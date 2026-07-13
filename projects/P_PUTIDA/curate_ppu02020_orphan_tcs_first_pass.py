#!/usr/bin/env python3
"""First-pass curation for the ppu02020 orphan/generic TCS bucket."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
MODULE_PATH = ROOT / "modules/orphan_two_component_regulators_boundary.yaml"
SPECIES = "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "sensor_kinase": {"id": "GO:0000155", "label": "phosphorelay sensor kinase activity"},
    "response_regulator": {"id": "GO:0000156", "label": "phosphorelay response regulator activity"},
    "phosphorelay": {"id": "GO:0000160", "label": "phosphorelay signal transduction system"},
    "transcription_region_binding": {"id": "GO:0000976", "label": "transcription cis-regulatory region binding"},
    "dna_binding": {"id": "GO:0003677", "label": "DNA binding"},
    "protein_his_kinase": {"id": "GO:0004673", "label": "protein histidine kinase activity"},
    "cytoplasm": {"id": "GO:0005737", "label": "cytoplasm"},
    "cytosol": {"id": "GO:0005829", "label": "cytosol"},
    "plasma_membrane": {"id": "GO:0005886", "label": "plasma membrane"},
    "transcription": {"id": "GO:0006351", "label": "DNA-templated transcription"},
    "transcription_reg": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "signal_transduction": {"id": "GO:0007165", "label": "signal transduction"},
    "histidine_phosphotransfer": {"id": "GO:0009927", "label": "histidine phosphotransfer kinase activity"},
    "membrane": {"id": "GO:0016020", "label": "membrane"},
    "kinase": {"id": "GO:0016301", "label": "kinase activity"},
    "transferase": {"id": "GO:0016740", "label": "transferase activity"},
    "phosphorus_transferase": {"id": "GO:0016772", "label": "transferase activity, transferring phosphorus-containing groups"},
    "sigma_antagonist": {"id": "GO:0016989", "label": "sigma factor antagonist activity"},
    "protein_dna_complex": {"id": "GO:0032993", "label": "protein-DNA complex"},
    "sequence_specific_dna_binding": {"id": "GO:0043565", "label": "sequence-specific DNA binding"},
    "negative_transcription_reg": {"id": "GO:0045892", "label": "negative regulation of DNA-templated transcription"},
    "protein_dimerization": {"id": "GO:0046983", "label": "protein dimerization activity"},
}


RESPONSE_REVIEWS = {
    "GO:0000156": ("ACCEPT", "Phosphorelay response-regulator activity is appropriate for the receiver-domain regulator.", None),
    "GO:0000160": ("ACCEPT", "Phosphorelay signal transduction matches the CheY-like receiver-domain architecture.", None),
    "GO:0000976": ("ACCEPT", "Transcription cis-regulatory region binding fits the LuxR/GerE or OmpR/PhoB-type DNA-binding output domain.", None),
    "GO:0003677": ("MARK_AS_OVER_ANNOTATED", "Generic DNA binding is less informative than transcriptional regulatory-region or sequence-specific DNA binding.", None),
    "GO:0005737": ("ACCEPT", "Cytoplasm localization is compatible with a soluble bacterial response regulator.", None),
    "GO:0005829": ("ACCEPT", "Cytosol localization is compatible with a soluble bacterial response regulator.", None),
    "GO:0006351": ("MARK_AS_OVER_ANNOTATED", "DNA-templated transcription is broad process context; regulation of transcription is the more accurate role.", None),
    "GO:0006355": ("ACCEPT", "The response regulator has a DNA-binding output domain consistent with transcriptional regulation.", None),
    "GO:0032993": ("KEEP_AS_NON_CORE", "Protein-DNA complex membership is plausible for a DNA-bound regulator but is not the core molecular role.", None),
    "GO:0043565": ("ACCEPT", "Sequence-specific DNA binding fits the HTH/Fis or LuxR/GerE-family regulatory output domain.", None),
}

SENSOR_REVIEWS = {
    "GO:0000155": ("ACCEPT", "The protein has conserved HisKA/HATPase sensor histidine kinase architecture.", None),
    "GO:0000160": ("ACCEPT", "Phosphorelay signal transduction matches the sensor kinase role.", None),
    "GO:0004673": ("ACCEPT", "Protein histidine kinase activity is the specific catalytic activity.", None),
    "GO:0005886": ("ACCEPT", "The protein is annotated as a plasma-membrane or inner-membrane sensor kinase.", None),
    "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than phosphorelay sensor kinase signaling.", None),
    "GO:0009927": ("ACCEPT", "The hybrid BvgS-like architecture includes an Hpt domain, supporting histidine phosphotransfer activity.", None),
    "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane localization is correct but less informative than the bacterial inner/plasma-membrane sensor role.", None),
    "GO:0016301": ("MARK_AS_OVER_ANNOTATED", "Generic kinase activity is less informative than protein histidine kinase activity.", None),
    "GO:0016740": ("MARK_AS_OVER_ANNOTATED", "Generic transferase activity is less informative than protein histidine kinase activity.", None),
    "GO:0016772": ("MARK_AS_OVER_ANNOTATED", "This parent transferase term is less informative than protein histidine kinase activity.", None),
    "GO:0046983": ("KEEP_AS_NON_CORE", "Dimerization is plausible for histidine-kinase signaling but is secondary to the sensor kinase activity.", None),
}

PP2671_SENSOR_REVIEWS = {
    **SENSOR_REVIEWS,
    "GO:0016020": ("ACCEPT", "Membrane localization is supported for this orphan sensor histidine kinase.", None),
}

ANTI_SIGMA_REVIEWS = {
    "GO:0016989": ("ACCEPT", "The FecR-like transmembrane sensor/anti-sigma architecture supports sigma factor antagonist activity.", None),
    "GO:0045892": ("ACCEPT", "Sigma factor antagonism is a direct mechanism for negative regulation of DNA-templated transcription.", None),
}

NEW_TERM_TEMPLATES = {
    "response_regulator": {
        "qualifier": "enables",
        "summary": "Receiver-domain response regulator activity should be recorded for this DNA-binding response regulator.",
        "reason": "The UniProt product/domain evidence and Asta retrieval identify a CheY-like receiver-domain DNA-binding response regulator.",
    },
    "transcription_reg": {
        "qualifier": "involved_in",
        "summary": "Response-regulator DNA binding should be represented as regulation of DNA-templated transcription.",
        "reason": "The HTH/Fis receiver-domain architecture supports phosphorelay-dependent transcriptional regulation.",
    },
    "membrane": {
        "qualifier": "located_in",
        "summary": "The transmembrane/FecR-like sensor should be represented as membrane localized.",
        "reason": "The UniProt product and Ferrdict_sens_TM/FecR domain annotations support a membrane-associated anti-sigma sensor role.",
    },
}


GENES = {
    "PP_0574": {
        "id": "Q88QC0",
        "ordered_locus": "PP_0574",
        "class": "response_luxr",
        "description": (
            "PP_0574 encodes a predicted LuxR/GerE-family DNA-binding response regulator in "
            "Pseudomonas putida KT2440. Its CheY-like receiver and LuxR-type winged-helix output "
            "domains support a phosphorelay-dependent transcriptional regulatory role, but the "
            "input signal and target regulon remain unresolved."
        ),
        "uniprot": "DE   SubName: Full=DNA-binding response regulator, LuxR family",
        "asta": "Protein Description:** SubName: Full=DNA-binding response regulator, LuxR family",
        "extra": ["DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.", "DR   InterPro; IPR000792; Tscrpt_reg_LuxR_C."],
        "reviews": RESPONSE_REVIEWS,
        "new_terms": ["response_regulator"],
    },
    "PP_0887": {
        "id": "Q88PG3",
        "ordered_locus": "PP_0887",
        "class": "sensor",
        "description": (
            "PP_0887 encodes a predicted membrane sensor histidine kinase in Pseudomonas putida "
            "KT2440. Multiple transmembrane segments plus HisKA/HATPase domains support a "
            "two-component phosphorelay sensor role, most likely paired with the adjacent regA "
            "response regulator, but the sensed cue is unresolved."
        ),
        "uniprot": "DE   RecName: Full=histidine kinase",
        "asta": "Protein Description:** RecName: Full=histidine kinase",
        "extra": ["CC   -!- SUBCELLULAR LOCATION: Membrane", "DR   InterPro; IPR005467; His_kinase_dom.", "FT   TRANSMEM        51..70"],
        "reviews": SENSOR_REVIEWS,
        "location": "plasma_membrane",
    },
    "regA": {
        "id": "Q88PG2",
        "ordered_locus": "PP_0888",
        "class": "response_fis",
        "description": (
            "regA encodes a predicted HTH/Fis-family DNA-binding response regulator in "
            "Pseudomonas putida KT2440. The product name derives from RegA-like regulators, "
            "but in this non-photosynthetic bacterium the supported first-pass assignment is "
            "generic phosphorelay-dependent transcription regulation by a receiver-domain regulator."
        ),
        "uniprot": "DE   SubName: Full=Photosynthetic apparatus regulatory protein RegA",
        "asta": "Protein Description:** SubName: Full=Photosynthetic apparatus regulatory protein RegA",
        "extra": ["DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.", "DR   InterPro; IPR002197; HTH_Fis."],
        "reviews": RESPONSE_REVIEWS,
        "new_terms": ["response_regulator", "transcription_reg"],
        "dna_term": "sequence_specific_dna_binding",
    },
    "PP_1007": {
        "id": "Q88P46",
        "ordered_locus": "PP_1007",
        "class": "anti_sigma",
        "description": (
            "PP_1007 encodes a predicted FecR-like transmembrane sensor/anti-sigma protein in "
            "Pseudomonas putida KT2440. FecR, FecR_N/FecR_C, and ferric-dicitrate-sensor "
            "transmembrane domain annotations support a membrane-associated sigma factor antagonist "
            "role rather than a canonical His-Asp sensor kinase assignment."
        ),
        "uniprot": "DE   SubName: Full=Transmembrane sensor",
        "asta": "Protein Description:** SubName: Full=Transmembrane sensor",
        "extra": ["DR   InterPro; IPR006860; FecR.", "DR   InterPro; IPR012373; Ferrdict_sens_TM."],
        "reviews": ANTI_SIGMA_REVIEWS,
        "new_terms": ["membrane"],
    },
    "bvgA": {
        "id": "Q88NW4",
        "ordered_locus": "PP_1090",
        "class": "response_luxr",
        "description": (
            "bvgA encodes a predicted LuxR/GerE-family DNA-binding response regulator in "
            "Pseudomonas putida KT2440. Its CheY-like receiver and LuxR-type output domains "
            "support phosphorelay-dependent transcriptional regulation, while the specific "
            "virulence-like or envelope signal implied by the name remains unresolved for KT2440."
        ),
        "uniprot": "DE   SubName: Full=Virulence factors positive transcription regulator BvgA",
        "asta": "Protein Description:** SubName: Full=Virulence factors positive transcription regulator BvgA",
        "extra": ["DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.", "DR   InterPro; IPR000792; Tscrpt_reg_LuxR_C."],
        "reviews": RESPONSE_REVIEWS,
        "new_terms": ["response_regulator"],
    },
    "PP_1181": {
        "id": "Q88NM6",
        "ordered_locus": "PP_1181",
        "class": "response_ompr",
        "description": (
            "PP_1181 encodes a predicted OmpR/PhoB-family DNA-binding response regulator in "
            "Pseudomonas putida KT2440. Its CheY-like receiver and OmpR/PhoB-type DNA-binding "
            "domains support a cytosolic phosphorelay-dependent transcriptional regulatory role, "
            "likely paired with the adjacent PP_1182 sensor kinase."
        ),
        "uniprot": "DE   SubName: Full=DNA-binding response regulator",
        "asta": "Protein Description:** SubName: Full=DNA-binding response regulator",
        "extra": ["DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.", "DR   InterPro; IPR001867; OmpR/PhoB-type_DNA-bd."],
        "reviews": RESPONSE_REVIEWS,
        "location": "cytosol",
    },
    "PP_1182": {
        "id": "Q88NM5",
        "ordered_locus": "PP_1182",
        "class": "sensor",
        "description": (
            "PP_1182 encodes a predicted membrane sensor histidine kinase in Pseudomonas putida "
            "KT2440. HAMP, HisKA, and HATPase domains support a two-component phosphorelay sensor "
            "role, likely paired with the adjacent PP_1181 response regulator."
        ),
        "uniprot": "DE   RecName: Full=histidine kinase",
        "asta": "Protein Description:** RecName: Full=histidine kinase",
        "extra": ["CC   -!- SUBCELLULAR LOCATION: Cell membrane", "DR   InterPro; IPR005467; His_kinase_dom.", "DR   InterPro; IPR003660; HAMP_dom."],
        "reviews": SENSOR_REVIEWS,
        "location": "plasma_membrane",
    },
    "PP_2671": {
        "id": "Q88JH8",
        "ordered_locus": "PP_2671",
        "class": "sensor",
        "description": (
            "PP_2671 encodes a predicted membrane-associated sensor histidine kinase in "
            "Pseudomonas putida KT2440. HAMP, HisKA_3, and HATPase domains support a "
            "two-component phosphorelay sensor role, but no cognate response regulator or "
            "specific input signal is assigned in this first pass."
        ),
        "uniprot": "DE   RecName: Full=histidine kinase",
        "asta": "Protein Description:** RecName: Full=histidine kinase",
        "extra": ["CC   -!- SUBCELLULAR LOCATION: Membrane", "DR   InterPro; IPR005467; His_kinase_dom.", "DR   InterPro; IPR050482; Sensor_HK_TwoCompSys."],
        "reviews": PP2671_SENSOR_REVIEWS,
        "location": "membrane",
    },
    "PP_3412": {
        "id": "Q88HE8",
        "ordered_locus": "PP_3412",
        "class": "response_luxr",
        "description": (
            "PP_3412 encodes a predicted LuxR/GerE-family DNA-binding response regulator in "
            "Pseudomonas putida KT2440. Receiver and LuxR-type output domains support a "
            "phosphorelay-dependent transcriptional regulatory role, likely in the same branch as "
            "the adjacent BvgS-like PP_3413 hybrid sensor kinase."
        ),
        "uniprot": "DE   SubName: Full=DNA-binding response regulator, LuxR family",
        "asta": "Protein Description:** SubName: Full=DNA-binding response regulator, LuxR family",
        "extra": ["DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.", "DR   InterPro; IPR000792; Tscrpt_reg_LuxR_C."],
        "reviews": RESPONSE_REVIEWS,
        "new_terms": ["response_regulator"],
    },
    "PP_3413": {
        "id": "Q88HE7",
        "ordered_locus": "PP_3413",
        "class": "hybrid_sensor",
        "description": (
            "PP_3413 encodes a predicted BvgS-like hybrid sensor histidine kinase in Pseudomonas "
            "putida KT2440. Periplasmic input domains, HisKA/HATPase catalytic domains, receiver "
            "and Hpt domains support a membrane two-component phosphorelay sensor/phosphotransfer "
            "role, likely connected to the adjacent PP_3412 response regulator."
        ),
        "uniprot": "DE   RecName: Full=histidine kinase",
        "asta": "Protein Description:** RecName: Full=histidine kinase",
        "extra": ["CC   -!- SUBCELLULAR LOCATION: Cell inner membrane", "DR   InterPro; IPR008207; Sig_transdc_His_kin_Hpt_dom.", "DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver."],
        "reviews": SENSOR_REVIEWS,
        "location": "plasma_membrane",
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
    for text in cfg.get("extra", []):
        items.append(support(uniprot_ref(gene), text))
    return items


def make_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    action, reason, replacements = cfg["reviews"][go_id]
    review = {
        "summary": reason,
        "action": action,
        "reason": reason,
        "supported_by": [support(goa_ref(gene), goa_quote(rows[go_id])), *base_support(gene, cfg)],
    }
    if replacements:
        review["proposed_replacement_terms"] = replacements
    return review


def new_annotation(gene: str, cfg: dict, term: dict, qualifier: str, summary: str, reason: str) -> dict:
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": uniprot_ref(gene),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
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


def response_core_functions(gene: str, cfg: dict) -> list[dict]:
    location = TERMS[cfg["location"]] if cfg.get("location") else None
    dna_term = TERMS[cfg.get("dna_term", "transcription_region_binding")]
    cores = [
        {
            "description": "Response regulator receiver activity in a two-component phosphorelay branch.",
            "molecular_function": TERMS["response_regulator"],
            "directly_involved_in": [TERMS["phosphorelay"]],
            "supported_by": base_support(gene, cfg),
        },
        {
            "description": "DNA-binding transcriptional regulation by a response-regulator output domain.",
            "molecular_function": dna_term,
            "directly_involved_in": [TERMS["transcription_reg"]],
            "supported_by": base_support(gene, cfg),
        },
    ]
    if location:
        for core in cores:
            core["locations"] = [location]
    return cores


def sensor_core_functions(gene: str, cfg: dict) -> list[dict]:
    location = TERMS[cfg.get("location", "membrane")]
    return [
        {
            "description": "Sensor histidine kinase activity in a two-component phosphorelay branch.",
            "molecular_function": TERMS["sensor_kinase"],
            "directly_involved_in": [TERMS["phosphorelay"]],
            "locations": [location],
            "supported_by": base_support(gene, cfg),
        }
    ]


def anti_sigma_core_functions(gene: str, cfg: dict) -> list[dict]:
    return [
        {
            "description": "FecR-like membrane anti-sigma activity restraining sigma factor-dependent transcription.",
            "molecular_function": TERMS["sigma_antagonist"],
            "directly_involved_in": [TERMS["negative_transcription_reg"]],
            "locations": [TERMS["membrane"]],
            "supported_by": base_support(gene, cfg),
        }
    ]


def core_functions(gene: str, cfg: dict) -> list[dict]:
    if cfg["class"].startswith("response"):
        return response_core_functions(gene, cfg)
    if cfg["class"] in {"sensor", "hybrid_sensor"}:
        return sensor_core_functions(gene, cfg)
    if cfg["class"] == "anti_sigma":
        return anti_sigma_core_functions(gene, cfg)
    raise ValueError(cfg["class"])


def suggested_question(gene: str, cfg: dict) -> str:
    if gene == "PP_1007":
        return "Which ECF sigma factor and envelope or iron-related stimulus are controlled by PP_1007 in KT2440?"
    if cfg["class"] in {"sensor", "hybrid_sensor"}:
        return f"What input signal and response-regulator partner define the {gene} phosphorelay branch in KT2440?"
    return f"What upstream sensor and target regulon define the {gene} response-regulator branch in KT2440?"


def suggested_experiment(gene: str, cfg: dict) -> str:
    if gene == "PP_1007":
        return "Delete PP_1007 and assay candidate ECF sigma-factor activity with promoter reporters under iron and envelope-stress conditions."
    if cfg["class"] in {"sensor", "hybrid_sensor"}:
        return f"Construct a {gene} deletion and phospho-site mutant, then profile transcriptional changes and test phosphotransfer to adjacent or candidate response regulators."
    return f"Construct a {gene} deletion and phospho-acceptor mutant, profile transcript changes under candidate stresses, and test DNA binding to candidate promoters."


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
        template = NEW_TERM_TEMPLATES[term_key]
        data.setdefault("existing_annotations", []).append(
            new_annotation(
                gene,
                cfg,
                TERMS[term_key],
                template["qualifier"],
                template["summary"],
                template["reason"],
            )
        )
        existing_ids.add(TERMS[term_key]["id"])

    data["core_functions"] = core_functions(gene, cfg)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": suggested_question(gene, cfg)}]
    data["suggested_experiments"] = [
        {"description": suggested_experiment(gene, cfg), "experiment_type": "targeted two-component or regulatory assay"}
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def annoton(gene: str, label: str, function: dict | None, processes: list[dict], locations: list[dict], role: str) -> dict:
    item = {
        "id": slug(label),
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "processes": [{"preferred_term": term["label"], "term": term} for term in processes],
        "locations": [{"preferred_term": term["label"], "term": term} for term in locations],
        "role_description": role,
    }
    if function:
        item["function"] = {"preferred_term": function["label"], "term": function}
    return item


def tcs_pair_part(order: int, role: str, sensor_gene: str, response_gene: str, node_id: str, label: str, description: str) -> dict:
    return {
        "order": order,
        "role": role,
        "node": {
            "id": node_id,
            "label": label,
            "module_type": "SIGNALING_PATHWAY",
            "description": description,
            "annotons": [
                annoton(
                    sensor_gene,
                    f"{sensor_gene}: sensor histidine kinase",
                    TERMS["sensor_kinase"],
                    [TERMS["phosphorelay"]],
                    [TERMS["plasma_membrane"]],
                    "Membrane sensor histidine kinase with unresolved input signal.",
                ),
                annoton(
                    response_gene,
                    f"{response_gene}: DNA-binding response regulator",
                    TERMS["response_regulator"],
                    [TERMS["phosphorelay"], TERMS["transcription_reg"]],
                    [TERMS["cytosol"]] if response_gene == "PP_1181" else [],
                    "DNA-binding response regulator with unresolved target regulon.",
                ),
            ],
            "connections": [
                {
                    "source": slug(f"{sensor_gene}: sensor histidine kinase"),
                    "target": slug(f"{response_gene}: DNA-binding response regulator"),
                    "connection_type": "PROVIDES_INPUT_FOR",
                    "description": f"{sensor_gene} is the plausible upstream phosphodonor for the adjacent {response_gene} response regulator.",
                }
            ],
        },
    }


def singleton_part(order: int, gene: str, cfg: dict) -> dict:
    if cfg["class"].startswith("response"):
        annotons = [
            annoton(
                gene,
                f"{gene}: orphan DNA-binding response regulator",
                TERMS["response_regulator"],
                [TERMS["phosphorelay"], TERMS["transcription_reg"]],
                [],
                "Orphan response regulator with unresolved sensor partner and target regulon.",
            )
        ]
        label = f"{gene} orphan response regulator"
    elif cfg["class"] == "anti_sigma":
        annotons = [
            annoton(
                gene,
                f"{gene}: FecR-like anti-sigma sensor",
                TERMS["sigma_antagonist"],
                [TERMS["negative_transcription_reg"]],
                [TERMS["membrane"]],
                "FecR-like transmembrane anti-sigma/sensor side context from the KEGG TCS map.",
            )
        ]
        label = f"{gene} FecR-like anti-sigma sensor"
    else:
        annotons = [
            annoton(
                gene,
                f"{gene}: orphan sensor histidine kinase",
                TERMS["sensor_kinase"],
                [TERMS["phosphorelay"]],
                [TERMS[cfg.get("location", "membrane")]],
                "Orphan sensor histidine kinase with unresolved response-regulator partner and input signal.",
            )
        ]
        label = f"{gene} orphan sensor kinase"
    return {
        "order": order,
        "role": label,
        "node": {
            "id": f"{slug(label)}_branch",
            "label": label,
            "module_type": "REGULATORY_STEP",
            "description": "Singleton side branch retained from the ppu02020 orphan/generic TCS partition.",
            "annotons": annotons,
        },
    }


def build_module() -> None:
    module = {
        "id": "MODULE:orphan_two_component_regulators_boundary",
        "title": "Orphan and generic two-component regulators boundary",
        "description": (
            "Boundary module for the ppu02020 orphan/generic two-component-system partition in "
            "Pseudomonas putida KT2440. It captures three adjacent sensor/regulator branches "
            "(PP_0887/regA, PP_1182/PP_1181, and PP_3413/PP_3412), orphan response regulators "
            "PP_0574 and bvgA, orphan sensor kinase PP_2671, and the FecR-like PP_1007 "
            "anti-sigma sensor side context."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02020",
                "title": "Two-component system - Pseudomonas putida KT2440",
                "statement": "KEGG ppu02020 supplies the umbrella membership for this orphan/generic regulatory boundary module.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.tsv",
                "title": "PSEPK ppu02020 partition table",
                "statement": (
                    "The partition table groups PP_0574, PP_0887, regA, PP_1007, bvgA, "
                    "PP_1181, PP_1182, PP_2671, PP_3412, and PP_3413 into the orphan/generic TCS bucket."
                ),
            },
        ],
        "notes": (
            "The module is intentionally conservative: it records generic two-component or anti-sigma "
            "regulatory functions, but does not assign target regulons, input signals, photosynthesis, "
            "virulence, or other pathway-specific phenotypes from names alone. PP_1007 is FecR-like "
            "anti-sigma context, not a canonical His-Asp sensor kinase."
        ),
        "module": {
            "id": "orphan_two_component_regulators_boundary",
            "label": "Orphan and generic two-component regulators boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                {"preferred_term": term["label"], "term": term}
                for term in [
                    TERMS["sensor_kinase"],
                    TERMS["response_regulator"],
                    TERMS["phosphorelay"],
                    TERMS["transcription_region_binding"],
                    TERMS["transcription_reg"],
                    TERMS["sigma_antagonist"],
                    TERMS["negative_transcription_reg"],
                ]
            ],
            "context": {
                "cellular_components": [
                    {"preferred_term": "plasma membrane", "term": TERMS["plasma_membrane"]},
                    {"preferred_term": "membrane", "term": TERMS["membrane"]},
                    {"preferred_term": "cytosol", "term": TERMS["cytosol"]},
                ]
            },
            "parts": [
                tcs_pair_part(
                    1,
                    "PP_0887-regA predicted two-component branch",
                    "PP_0887",
                    "regA",
                    "pp0887_rega_two_component_branch",
                    "PP_0887-regA two-component branch",
                    "Adjacent predicted membrane sensor kinase and HTH/Fis response regulator with unresolved cue and regulon.",
                ),
                tcs_pair_part(
                    2,
                    "PP_1182-PP_1181 predicted two-component branch",
                    "PP_1182",
                    "PP_1181",
                    "pp1182_pp1181_two_component_branch",
                    "PP_1182-PP_1181 two-component branch",
                    "Adjacent predicted membrane sensor kinase and OmpR/PhoB-family response regulator.",
                ),
                tcs_pair_part(
                    3,
                    "PP_3413-PP_3412 BvgS/BvgA-like branch",
                    "PP_3413",
                    "PP_3412",
                    "pp3413_pp3412_two_component_branch",
                    "PP_3413-PP_3412 two-component branch",
                    "Adjacent BvgS-like hybrid sensor kinase and LuxR/GerE-family response regulator.",
                ),
                singleton_part(4, "PP_0574", GENES["PP_0574"]),
                singleton_part(5, "bvgA", GENES["bvgA"]),
                singleton_part(6, "PP_2671", GENES["PP_2671"]),
                singleton_part(7, "PP_1007", GENES["PP_1007"]),
            ],
        },
    }
    MODULE_PATH.write_text(
        yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Wrote {MODULE_PATH.relative_to(ROOT)}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    build_module()


if __name__ == "__main__":
    main()
