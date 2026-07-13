#!/usr/bin/env python3
"""First-pass curation for the ppu02020 osmotic/envelope/efflux bucket."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
MODULE_PATH = ROOT / "modules/osmotic_envelope_efflux_regulation_boundary.yaml"
SPECIES = "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "response_regulator": {"id": "GO:0000156", "label": "phosphorelay response regulator activity"},
    "sensor_kinase": {"id": "GO:0000155", "label": "phosphorelay sensor kinase activity"},
    "phosphorelay": {"id": "GO:0000160", "label": "phosphorelay signal transduction system"},
    "histidine_kinase": {"id": "GO:0004673", "label": "protein histidine kinase activity"},
    "histidine_phosphotransfer": {"id": "GO:0009927", "label": "histidine phosphotransfer kinase activity"},
    "cis_binding": {"id": "GO:0000976", "label": "transcription cis-regulatory region binding"},
    "dna_binding": {"id": "GO:0003677", "label": "DNA binding"},
    "cytoplasm": {"id": "GO:0005737", "label": "cytoplasm"},
    "cytosol": {"id": "GO:0005829", "label": "cytosol"},
    "plasma_membrane": {"id": "GO:0005886", "label": "plasma membrane"},
    "membrane": {"id": "GO:0016020", "label": "membrane"},
    "transcription": {"id": "GO:0006351", "label": "DNA-templated transcription"},
    "transcription_reg": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "positive_transcription_reg": {"id": "GO:0045893", "label": "positive regulation of DNA-templated transcription"},
    "protein_dna_complex": {"id": "GO:0032993", "label": "protein-DNA complex"},
    "signal_transduction": {"id": "GO:0007165", "label": "signal transduction"},
    "kinase": {"id": "GO:0016301", "label": "kinase activity"},
    "transferase": {"id": "GO:0016740", "label": "transferase activity"},
    "phosphorus_transferase": {"id": "GO:0016772", "label": "transferase activity, transferring phosphorus-containing groups"},
    "transmembrane_transporter": {"id": "GO:0022857", "label": "transmembrane transporter activity"},
    "xenobiotic_transport": {"id": "GO:0042908", "label": "xenobiotic transport"},
    "xenobiotic_transporter": {"id": "GO:0042910", "label": "xenobiotic transmembrane transporter activity"},
    "transmembrane_transport": {"id": "GO:0055085", "label": "transmembrane transport"},
    "efflux_transporter": {"id": "GO:0015562", "label": "efflux transmembrane transporter activity"},
    "efflux_pump_complex": {"id": "GO:1990281", "label": "efflux pump complex"},
}


SENSOR_REVIEWS = {
    "GO:0000155": ("ACCEPT", "The protein has conserved sensor histidine kinase architecture.", None),
    "GO:0000160": ("ACCEPT", "The protein participates in His-Asp phosphorelay signaling.", None),
    "GO:0004673": ("ACCEPT", "Protein histidine kinase activity is the core catalytic activity.", None),
    "GO:0005886": ("ACCEPT", "The protein is a predicted bacterial inner/plasma-membrane sensor kinase.", None),
    "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than phosphorelay signal transduction.", None),
    "GO:0009927": ("ACCEPT", "The hybrid sensor contains histidine phosphotransfer/Hpt architecture consistent with phosphorelay output.", None),
    "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than plasma membrane.", None),
    "GO:0016301": ("MARK_AS_OVER_ANNOTATED", "Generic kinase activity is less informative than sensor histidine kinase activity.", None),
    "GO:0016740": ("MARK_AS_OVER_ANNOTATED", "Generic transferase activity is less informative than histidine kinase activity.", None),
    "GO:0016772": ("MARK_AS_OVER_ANNOTATED", "This broad phosphorus-transfer term is less informative than protein histidine kinase activity.", None),
}


RESPONSE_REGULATOR_REVIEWS = {
    "GO:0000156": ("ACCEPT", "The receiver-domain protein is a phosphorelay response regulator.", None),
    "GO:0000160": ("ACCEPT", "The protein acts in a two-component phosphorelay system.", None),
    "GO:0000976": ("ACCEPT", "The response regulator has a DNA-binding output domain for cis-regulatory region binding.", None),
    "GO:0003677": ("MARK_AS_OVER_ANNOTATED", "Generic DNA binding is less informative than transcription cis-regulatory region binding.", None),
    "GO:0005737": ("ACCEPT", "A cytoplasmic location is appropriate for a soluble bacterial response regulator.", None),
    "GO:0005829": ("KEEP_AS_NON_CORE", "Cytosol is compatible with cytoplasmic response-regulator function but is not the preferred core location.", None),
    "GO:0006351": ("KEEP_AS_NON_CORE", "DNA-templated transcription is broad context; the regulator controls transcription rather than carrying out transcription itself.", None),
    "GO:0006355": ("ACCEPT", "The DNA-binding response regulator controls transcription of target genes.", None),
    "GO:0032993": ("KEEP_AS_NON_CORE", "Protein-DNA complex membership is transient context for a DNA-bound regulator.", None),
    "GO:0045893": ("KEEP_AS_NON_CORE", "Positive transcriptional regulation is plausible for some OmpR-family targets but broader regulation is the safer core process.", None),
}


RND_TRANSPORTER_REVIEWS = {
    "GO:0005886": ("ACCEPT", "Plasma membrane localization is appropriate for an inner-membrane RND transporter component.", None),
    "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than plasma membrane.", None),
    "GO:0022857": ("KEEP_AS_NON_CORE", "Generic transmembrane transporter activity is correct but less informative than xenobiotic transporter activity.", None),
    "GO:0042908": ("ACCEPT", "Xenobiotic transport captures the predicted multidrug/RND efflux process.", None),
    "GO:0042910": ("ACCEPT", "Xenobiotic transmembrane transporter activity is the best available molecular function for the RND transporter subunit.", None),
    "GO:0055085": ("KEEP_AS_NON_CORE", "Generic transmembrane transport is less specific than xenobiotic transport.", None),
}


GENES = {
    "ompR": {
        "description": (
            "ompR encodes an OmpR-family two-component response regulator in Pseudomonas putida KT2440. "
            "The protein has a receiver domain and an OmpR/PhoB-type DNA-binding output domain, supporting "
            "a cytoplasmic transcription-regulatory role paired with the adjacent EnvZ sensor kinase."
        ),
        "uniprot": "RecName: Full=DNA-binding dual transcriptional regulator OmpR",
        "uniprot_extra": "DR   InterPro; IPR001867; OmpR/PhoB-type_DNA-bd.",
        "asta": "Protein Description:** RecName: Full=DNA-binding dual transcriptional regulator OmpR",
        "term_reviews": RESPONSE_REGULATOR_REVIEWS,
        "core_functions": [
            {
                "description": "OmpR-family phosphorelay response regulator for EnvZ/OmpR transcriptional control.",
                "molecular_function": TERMS["response_regulator"],
                "directly_involved_in": [TERMS["phosphorelay"], TERMS["transcription_reg"]],
                "locations": [TERMS["cytoplasm"]],
            },
            {
                "description": "Cis-regulatory DNA binding by an OmpR/PhoB-family transcription regulator.",
                "molecular_function": TERMS["cis_binding"],
                "directly_involved_in": [TERMS["transcription_reg"]],
                "locations": [TERMS["cytoplasm"]],
            },
        ],
        "question": "Which envelope or osmotic-stress promoters are directly regulated by KT2440 OmpR?",
        "experiment": "Measure EnvZ/OmpR-dependent promoter activity and OmpR binding under osmotic and envelope-stress conditions.",
    },
    "envZ": {
        "description": (
            "envZ encodes the membrane sensor histidine kinase paired with OmpR in Pseudomonas putida "
            "KT2440. Its HAMP, HisKA, and HATPase domains support a bacterial inner-membrane sensor role "
            "that feeds phosphorelay control of OmpR-dependent transcription."
        ),
        "uniprot": "RecName: Full=histidine kinase",
        "uniprot_extra": "DR   InterPro; IPR005467; His_kinase_dom.",
        "asta": "Protein Description:** RecName: Full=histidine kinase",
        "term_reviews": SENSOR_REVIEWS,
        "core_functions": [
            {
                "description": "EnvZ membrane sensor kinase control of the OmpR response regulator.",
                "molecular_function": TERMS["sensor_kinase"],
                "directly_involved_in": [TERMS["phosphorelay"]],
                "locations": [TERMS["plasma_membrane"]],
            }
        ],
        "question": "Does KT2440 EnvZ primarily respond to osmolarity, envelope stress, or another input?",
        "experiment": "Assay OmpR phosphorylation and OmpR-regulated promoters across osmotic and envelope-stress gradients.",
    },
    "PP_2100": {
        "description": (
            "PP_2100 encodes a large predicted EvgS/BvgS-like hybrid sensor histidine kinase in "
            "Pseudomonas putida KT2440. It contains periplasmic sensory domains, HisKA/HATPase, Hpt, and "
            "receiver-domain architecture, consistent with a membrane phosphorelay sensor paired with EvgA."
        ),
        "uniprot": "RecName: Full=histidine kinase",
        "uniprot_extra": "DR   InterPro; IPR008207; Sig_transdc_His_kin_Hpt_dom.",
        "asta": "Protein Description:** RecName: Full=histidine kinase",
        "term_reviews": SENSOR_REVIEWS,
        "core_functions": [
            {
                "description": "Hybrid membrane sensor kinase/phosphotransfer protein for EvgA-like transcriptional regulation.",
                "molecular_function": TERMS["sensor_kinase"],
                "directly_involved_in": [TERMS["phosphorelay"]],
                "locations": [TERMS["plasma_membrane"]],
            },
            {
                "description": "Histidine phosphotransfer activity within a multi-step phosphorelay sensor.",
                "molecular_function": TERMS["histidine_phosphotransfer"],
                "directly_involved_in": [TERMS["phosphorelay"]],
                "locations": [TERMS["plasma_membrane"]],
            },
        ],
        "question": "What envelope or stress signal is sensed by the PP_2100/EvgA pair?",
        "experiment": "Measure EvgA-dependent transcription in PP_2100 mutant and complemented strains during acid, osmotic, and envelope-stress challenges.",
    },
    "evgA": {
        "description": (
            "evgA encodes a predicted EvgA-family DNA-binding response regulator in Pseudomonas putida "
            "KT2440. Domain architecture and product naming support a transcription-regulatory output role "
            "paired with the adjacent PP_2100 EvgS/BvgS-like sensor kinase."
        ),
        "uniprot": "SubName: Full=DNA-binding response regulator in two-component regulatory system with EvgS",
        "uniprot_extra": "DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.",
        "asta": "Protein Description:** SubName: Full=DNA-binding response regulator in two-component regulatory system with EvgS",
        "term_reviews": RESPONSE_REGULATOR_REVIEWS,
        "new_annotations": [
            {
                "term": TERMS["response_regulator"],
                "qualifier": "enables",
                "summary": "EvgA should be represented as a phosphorelay response regulator.",
                "reason": "The product name and receiver-domain architecture identify EvgA as a two-component response regulator.",
            }
        ],
        "core_functions": [
            {
                "description": "EvgA-family phosphorelay response regulator controlling transcription.",
                "molecular_function": TERMS["response_regulator"],
                "directly_involved_in": [TERMS["phosphorelay"], TERMS["transcription_reg"]],
            },
            {
                "description": "DNA-binding transcription-regulator output for the PP_2100/EvgA system.",
                "molecular_function": TERMS["cis_binding"],
                "directly_involved_in": [TERMS["transcription_reg"]],
            },
        ],
        "question": "Which envelope-stress or efflux genes are controlled by EvgA in KT2440?",
        "experiment": "Compare transcriptomes of wild-type, evgA deletion, and complemented strains during envelope stress and xenobiotic exposure.",
    },
    "mdtC": {
        "description": (
            "mdtC encodes a predicted inner-membrane AcrB/RND-family multidrug efflux transporter subunit "
            "in Pseudomonas putida KT2440. It is likely part of the MdtABC tripartite efflux system with "
            "the adjacent MdtB transporter and MdtA membrane-fusion/adaptor protein."
        ),
        "uniprot": "SubName: Full=Multidrug efflux transport system-membrane subunit",
        "uniprot_extra": "DR   InterPro; IPR001036; Acrflvin-R.",
        "asta": "Protein Description:** SubName: Full=Multidrug efflux transport system-membrane subunit",
        "term_reviews": RND_TRANSPORTER_REVIEWS,
        "new_annotations": [
            {
                "term": TERMS["efflux_pump_complex"],
                "qualifier": "part_of",
                "summary": "MdtC should be represented as part of an efflux pump complex.",
                "reason": "The AcrB/RND-family transporter identity and local mdtABC context support complex membership.",
            }
        ],
        "core_functions": [
            {
                "description": "Inner-membrane RND multidrug/xenobiotic efflux transporter component.",
                "molecular_function": TERMS["xenobiotic_transporter"],
                "directly_involved_in": [TERMS["xenobiotic_transport"]],
                "locations": [TERMS["plasma_membrane"]],
                "in_complex": TERMS["efflux_pump_complex"],
            }
        ],
        "question": "Which xenobiotic or antibiotic substrates require MdtC in KT2440?",
        "experiment": "Construct mdtC, mdtB, and mdtABC mutants and test susceptibility and efflux of representative xenobiotics and antibiotics.",
    },
    "mdtB": {
        "description": (
            "mdtB encodes a predicted inner-membrane AcrB/RND-family multidrug efflux transporter subunit "
            "in Pseudomonas putida KT2440. Together with MdtC and MdtA, it likely contributes to a "
            "tripartite efflux pump for xenobiotic export."
        ),
        "uniprot": "SubName: Full=Multidrug efflux transport system-membrane subunit",
        "uniprot_extra": "DR   InterPro; IPR001036; Acrflvin-R.",
        "asta": "Protein Description:** SubName: Full=Multidrug efflux transport system-membrane subunit",
        "term_reviews": RND_TRANSPORTER_REVIEWS,
        "new_annotations": [
            {
                "term": TERMS["efflux_pump_complex"],
                "qualifier": "part_of",
                "summary": "MdtB should be represented as part of an efflux pump complex.",
                "reason": "The AcrB/RND-family transporter identity and local mdtABC context support complex membership.",
            }
        ],
        "core_functions": [
            {
                "description": "Inner-membrane RND multidrug/xenobiotic efflux transporter component.",
                "molecular_function": TERMS["xenobiotic_transporter"],
                "directly_involved_in": [TERMS["xenobiotic_transport"]],
                "locations": [TERMS["plasma_membrane"]],
                "in_complex": TERMS["efflux_pump_complex"],
            }
        ],
        "question": "Does MdtB form a heteromeric RND transporter with MdtC in KT2440?",
        "experiment": "Test MdtB/MdtC codependence by comparing single and double mutants for drug susceptibility, efflux, and pump stability.",
    },
    "mdtA": {
        "description": (
            "mdtA encodes a predicted membrane-fusion/adaptor component of the MdtABC multidrug efflux "
            "system in Pseudomonas putida KT2440. Its RND-pump MFP domains support a periplasmic adaptor "
            "role in the efflux pump complex rather than independent transporter activity."
        ),
        "uniprot": "SubName: Full=Multidrug efflux transport system-putative membrane fusion protein",
        "uniprot_extra": "DR   InterPro; IPR006143; RND_pump_MFP.",
        "asta": "Protein Description:** SubName: Full=Multidrug efflux transport system-putative membrane fusion protein",
        "term_reviews": {
            "GO:0005886": ("ACCEPT", "Plasma membrane localization is appropriate for a membrane-associated RND pump adaptor.", None),
            "GO:0015562": ("MARK_AS_OVER_ANNOTATED", "The MFP adaptor contributes to efflux transporter activity but should not be treated as an independently enabling transporter.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than plasma membrane.", None),
            "GO:0022857": ("MARK_AS_OVER_ANNOTATED", "Generic transporter activity overstates the role of a membrane-fusion/adaptor subunit.", None),
            "GO:0055085": ("KEEP_AS_NON_CORE", "Transmembrane transport is correct as complex context but broad for this adaptor subunit.", None),
            "GO:1990281": ("ACCEPT", "Efflux pump complex membership captures the component role of MdtA.", None),
        },
        "core_functions": [
            {
                "description": "Membrane-fusion/adaptor subunit contributing to MdtABC efflux pump activity.",
                "contributes_to_molecular_function": TERMS["efflux_transporter"],
                "in_complex": TERMS["efflux_pump_complex"],
                "locations": [TERMS["plasma_membrane"]],
            }
        ],
        "question": "Which outer-membrane factor pairs with MdtABC in KT2440?",
        "experiment": "Identify MdtABC-associated outer-membrane channel partners by affinity purification or genetic epistasis with candidate OMF deletions.",
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


def make_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    action, reason, replacements = cfg["term_reviews"][go_id]
    label = rows[go_id]["GO NAME"]
    review = {
        "summary": reason,
        "action": action,
        "reason": reason,
        "supported_by": [
            support(goa_ref(gene), goa_quote(rows[go_id])),
            support(uniprot_ref(gene), cfg["uniprot"]),
            support(asta_ref(gene), cfg["asta"]),
        ],
    }
    if cfg.get("uniprot_extra"):
        review["supported_by"].append(support(uniprot_ref(gene), cfg["uniprot_extra"]))
    if replacements:
        review["proposed_replacement_terms"] = replacements
    if action == "MARK_AS_OVER_ANNOTATED":
        review["summary"] = f"{label} is true or plausible but too broad or misleading as a core annotation."
    return review


def make_new_annotation(gene: str, cfg: dict, item: dict) -> dict:
    term = item["term"]
    supported_by = [
        support(uniprot_ref(gene), cfg["uniprot"]),
        support(asta_ref(gene), cfg["asta"]),
    ]
    if cfg.get("uniprot_extra"):
        supported_by.append(support(uniprot_ref(gene), cfg["uniprot_extra"]))
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": uniprot_ref(gene),
        "qualifier": item["qualifier"],
        "review": {
            "summary": item["summary"],
            "action": "NEW",
            "reason": item["reason"],
            "supported_by": supported_by,
        },
    }


def supported_by_for_core(gene: str, cfg: dict) -> list[dict[str, str]]:
    items = [
        support(uniprot_ref(gene), cfg["uniprot"]),
        support(asta_ref(gene), cfg["asta"]),
    ]
    if cfg.get("uniprot_extra"):
        items.append(support(uniprot_ref(gene), cfg["uniprot_extra"]))
    return items


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = goa_rows(gene)

    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_reference(data, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(data, uniprot_ref(gene), f"UniProtKB entry for {gene}", cfg["uniprot"])
    ensure_reference(data, asta_ref(gene), f"Asta retrieval report for {gene}", cfg["asta"])

    new_items = {item["term"]["id"]: item for item in cfg.get("new_annotations", [])}
    for annotation in data["existing_annotations"]:
        go_id = annotation["term"]["id"]
        if go_id in rows and go_id in cfg["term_reviews"]:
            annotation["review"] = make_review(gene, cfg, rows, go_id)
        elif go_id in new_items:
            annotation.update(make_new_annotation(gene, cfg, new_items[go_id]))
        else:
            raise KeyError(f"Unhandled annotation {go_id} for {gene}")

    existing_ids = {annotation["term"]["id"] for annotation in data["existing_annotations"]}
    for item in cfg.get("new_annotations", []):
        if item["term"]["id"] not in existing_ids:
            data["existing_annotations"].append(make_new_annotation(gene, cfg, item))
            existing_ids.add(item["term"]["id"])

    for core in cfg["core_functions"]:
        core["supported_by"] = supported_by_for_core(gene, cfg)
    data["core_functions"] = cfg["core_functions"]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": cfg["question"]}]
    data["suggested_experiments"] = [
        {
            "description": cfg["experiment"],
            "experiment_type": "targeted envelope regulation or efflux assay",
        }
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


def build_module() -> None:
    module = {
        "id": "MODULE:osmotic_envelope_efflux_regulation_boundary",
        "title": "Osmotic envelope and efflux regulation boundary",
        "description": (
            "Boundary module for the ppu02020 osmotic/envelope/efflux partition in Pseudomonas putida "
            "KT2440. It captures EnvZ/OmpR and EvgS/EvgA-like phosphorelay regulators plus the adjacent "
            "MdtABC RND multidrug efflux pump context. This is a partition of the broad KEGG "
            "two-component-system map, not a single linear pathway."
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
                    "The partition table groups ompR, envZ, PP_2100, evgA, mdtC, mdtB, and mdtA into "
                    "the osmotic/envelope/efflux regulation bucket."
                ),
            },
        ],
        "notes": (
            "The MdtABC efflux pump is transport context for the regulatory bucket, not a His-Asp "
            "phosphorelay component. Its subunits are kept in the same boundary module because the KEGG "
            "ppu02020 umbrella groups local regulatory and efflux context together."
        ),
        "module": {
            "id": "osmotic_envelope_efflux_regulation_boundary",
            "label": "Osmotic envelope and efflux regulation boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                {"preferred_term": t["label"], "term": t}
                for t in [
                    TERMS["phosphorelay"],
                    TERMS["transcription_reg"],
                    TERMS["xenobiotic_transport"],
                    TERMS["efflux_transporter"],
                    TERMS["efflux_pump_complex"],
                ]
            ],
            "context": {
                "cellular_components": [
                    {"preferred_term": "cytoplasm", "term": TERMS["cytoplasm"]},
                    {"preferred_term": "plasma membrane", "term": TERMS["plasma_membrane"]},
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "EnvZ/OmpR envelope transcription control",
                    "node": {
                        "id": "envz_ompr_regulation",
                        "label": "EnvZ/OmpR regulation",
                        "module_type": "REGULATORY_STEP",
                        "description": "EnvZ and OmpR form a canonical two-component sensor/regulator pair.",
                        "annotons": [
                            annoton("envZ", "envZ: OmpR sensor kinase", TERMS["sensor_kinase"], [TERMS["phosphorelay"]], [TERMS["plasma_membrane"]], "Membrane sensor kinase paired with OmpR."),
                            annoton("ompR", "ompR: response regulator", TERMS["response_regulator"], [TERMS["phosphorelay"], TERMS["transcription_reg"]], [TERMS["cytoplasm"]], "OmpR-family DNA-binding response regulator."),
                        ],
                        "connections": [
                            {"source": "envz_ompr_sensor_kinase", "target": "ompr_response_regulator", "connection_type": "PROVIDES_INPUT_FOR", "description": "EnvZ is the cognate sensor kinase for OmpR."},
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "PP_2100/EvgA-like envelope-stress regulation",
                    "node": {
                        "id": "evgs_evga_like_regulation",
                        "label": "PP_2100/EvgA-like regulation",
                        "module_type": "REGULATORY_STEP",
                        "description": "PP_2100 and EvgA form an EvgS/EvgA-like regulatory pair with hybrid phosphorelay architecture.",
                        "annotons": [
                            annoton("PP_2100", "PP_2100: EvgS-like hybrid sensor", TERMS["sensor_kinase"], [TERMS["phosphorelay"]], [TERMS["plasma_membrane"]], "Hybrid sensor kinase/phosphotransfer protein."),
                            annoton("evgA", "evgA: EvgA response regulator", TERMS["response_regulator"], [TERMS["phosphorelay"], TERMS["transcription_reg"]], [TERMS["cytoplasm"]], "EvgA-family DNA-binding response regulator."),
                        ],
                        "connections": [
                            {"source": "pp_2100_evgs_like_hybrid_sensor", "target": "evga_evga_response_regulator", "connection_type": "PROVIDES_INPUT_FOR", "description": "PP_2100 is the adjacent EvgS/BvgS-like sensor for EvgA."},
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "MdtABC RND multidrug efflux context",
                    "node": {
                        "id": "mdtabc_efflux_pump",
                        "label": "MdtABC efflux pump",
                        "module_type": "TRANSPORT_STEP",
                        "description": "MdtB and MdtC are RND-family transporter subunits, while MdtA is the membrane-fusion/adaptor subunit.",
                        "annotons": [
                            annoton("mdtC", "mdtC: RND efflux transporter subunit", TERMS["xenobiotic_transporter"], [TERMS["xenobiotic_transport"]], [TERMS["plasma_membrane"]], "RND inner-membrane transporter component of the efflux pump complex."),
                            annoton("mdtB", "mdtB: RND efflux transporter subunit", TERMS["xenobiotic_transporter"], [TERMS["xenobiotic_transport"]], [TERMS["plasma_membrane"]], "RND inner-membrane transporter component of the efflux pump complex."),
                            annoton("mdtA", "mdtA: membrane-fusion efflux adaptor", TERMS["efflux_transporter"], [TERMS["transmembrane_transport"]], [TERMS["plasma_membrane"]], "MFP adaptor contributing to MdtABC efflux pump activity."),
                        ],
                        "connections": [
                            {"source": "mdta_membrane_fusion_efflux_adaptor", "target": "mdtb_rnd_efflux_transporter_subunit", "connection_type": "PROVIDES_INPUT_FOR", "description": "MdtA is the membrane-fusion/adaptor component of the local efflux pump."},
                            {"source": "mdta_membrane_fusion_efflux_adaptor", "target": "mdtc_rnd_efflux_transporter_subunit", "connection_type": "PROVIDES_INPUT_FOR", "description": "MdtA is the membrane-fusion/adaptor component of the local efflux pump."},
                        ],
                    },
                },
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
