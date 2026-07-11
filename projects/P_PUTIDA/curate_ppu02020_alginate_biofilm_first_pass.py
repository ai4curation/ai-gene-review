#!/usr/bin/env python3
"""First-pass curation for the ppu02020 alginate/biofilm regulation bucket."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
MODULE_PATH = ROOT / "modules/alginate_biofilm_regulation_boundary.yaml"
SPECIES = "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "sensor_kinase": {"id": "GO:0000155", "label": "phosphorelay sensor kinase activity"},
    "response_regulator": {"id": "GO:0000156", "label": "phosphorelay response regulator activity"},
    "phosphorelay": {"id": "GO:0000160", "label": "phosphorelay signal transduction system"},
    "cis_binding": {"id": "GO:0000976", "label": "transcription cis-regulatory region binding"},
    "dna_binding": {"id": "GO:0003677", "label": "DNA binding"},
    "sequence_specific_dna_binding": {"id": "GO:0043565", "label": "sequence-specific DNA binding"},
    "histidine_kinase": {"id": "GO:0004673", "label": "protein histidine kinase activity"},
    "atp_binding": {"id": "GO:0005524", "label": "ATP binding"},
    "cytosol": {"id": "GO:0005829", "label": "cytosol"},
    "plasma_membrane": {"id": "GO:0005886", "label": "plasma membrane"},
    "transcription": {"id": "GO:0006351", "label": "DNA-templated transcription"},
    "transcription_reg": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "signal_transduction": {"id": "GO:0007165", "label": "signal transduction"},
    "sam_methyltransferase": {"id": "GO:0008757", "label": "S-adenosylmethionine-dependent methyltransferase activity"},
    "protein_glutamate_methyltransferase": {"id": "GO:0008983", "label": "protein-glutamate O-methyltransferase activity"},
    "membrane": {"id": "GO:0016020", "label": "membrane"},
    "kinase": {"id": "GO:0016301", "label": "kinase activity"},
    "transferase": {"id": "GO:0016740", "label": "transferase activity"},
    "phosphorus_transferase": {"id": "GO:0016772", "label": "transferase activity, transferring phosphorus-containing groups"},
    "protein_dna_complex": {"id": "GO:0032993", "label": "protein-DNA complex"},
    "biofilm_formation": {"id": "GO:0042710", "label": "biofilm formation"},
    "alginic_acid_biosynthesis": {"id": "GO:0042121", "label": "alginic acid biosynthetic process"},
}


SENSOR_REVIEWS = {
    "GO:0000155": ("ACCEPT", "The protein has conserved sensor histidine kinase architecture.", None),
    "GO:0000160": ("ACCEPT", "The protein participates in His-Asp phosphorelay signaling.", None),
    "GO:0004673": ("ACCEPT", "Protein histidine kinase activity is the core catalytic activity of this sensor kinase.", None),
    "GO:0005886": ("ACCEPT", "The KinB protein has predicted transmembrane helices and a UniProt cell-membrane location.", None),
    "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than phosphorelay signal transduction.", None),
    "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than the plasma-membrane location where supported.", None),
    "GO:0016301": ("MARK_AS_OVER_ANNOTATED", "Generic kinase activity is less informative than sensor histidine kinase activity.", None),
    "GO:0016740": ("MARK_AS_OVER_ANNOTATED", "Generic transferase activity is less informative than protein histidine kinase activity.", None),
    "GO:0016772": ("MARK_AS_OVER_ANNOTATED", "This broad phosphorus-transfer term is less informative than protein histidine kinase activity.", None),
}


FLES_REVIEWS = {
    key: value
    for key, value in SENSOR_REVIEWS.items()
    if key not in {"GO:0005886", "GO:0016020"}
}


RESPONSE_REGULATOR_REVIEWS = {
    "GO:0000156": ("ACCEPT", "The receiver-domain protein is a phosphorelay response regulator.", None),
    "GO:0000160": ("ACCEPT", "The protein acts in a two-component phosphorelay system.", None),
    "GO:0000976": ("ACCEPT", "The response regulator has a DNA-binding output domain for cis-regulatory region binding.", None),
    "GO:0003677": ("MARK_AS_OVER_ANNOTATED", "Generic DNA binding is less informative than transcription cis-regulatory region binding.", None),
    "GO:0005829": ("ACCEPT", "Cytosol is compatible with a soluble bacterial response regulator.", None),
    "GO:0006351": ("KEEP_AS_NON_CORE", "DNA-templated transcription is broad context; the regulator controls transcription rather than carrying it out.", None),
    "GO:0006355": ("ACCEPT", "The DNA-binding response regulator controls transcription of target genes.", None),
    "GO:0032993": ("KEEP_AS_NON_CORE", "Protein-DNA complex membership is transient context for a DNA-bound regulator.", None),
}


ALGB_LIKE_REVIEWS = {
    "GO:0000160": ("ACCEPT", "The receiver-domain regulator participates in phosphorelay signal transduction.", None),
    "GO:0000166": ("MARK_AS_OVER_ANNOTATED", "Generic nucleotide binding is less informative than the response-regulator/sigma-54 activator role.", None),
    "GO:0005524": ("KEEP_AS_NON_CORE", "ATP binding is expected for the sigma-54 enhancer-binding AAA+ domain but is not by itself the core regulatory function.", None),
    "GO:0006351": ("KEEP_AS_NON_CORE", "DNA-templated transcription is broad context for a transcription regulator.", None),
    "GO:0006355": ("ACCEPT", "The AlgB-like protein is a transcriptional regulatory protein.", None),
    "GO:0043565": ("ACCEPT", "Sequence-specific DNA binding is supported for AlgB by its HTH/Fis DNA-binding domain.", None),
    "GO:0042121": ("ACCEPT", "AlgB is annotated as a positive regulator of alginate biosynthesis and algD expression.", None),
}


GENES = {
    "kinB": {
        "id": "Q88RJ7",
        "ordered_locus": "PP_0132",
        "description": (
            "kinB encodes a membrane-associated sensor histidine kinase in Pseudomonas putida KT2440. "
            "Its HAMP, PAS/sensor, HisKA, and HATPase domains support a role as a two-component "
            "phosphorelay input protein in the alginate/biofilm regulatory neighborhood."
        ),
        "uniprot": "RecName: Full=histidine kinase",
        "uniprot_extra": "DR   InterPro; IPR005467; His_kinase_dom.",
        "asta": "Protein Description:** RecName: Full=histidine kinase",
        "term_reviews": SENSOR_REVIEWS,
        "core_functions": [
            {
                "description": "Membrane sensor histidine kinase activity feeding a bacterial phosphorelay.",
                "molecular_function": TERMS["sensor_kinase"],
                "directly_involved_in": [TERMS["phosphorelay"]],
                "locations": [TERMS["plasma_membrane"]],
            }
        ],
        "question": "Which environmental or envelope signal is sensed by KinB in KT2440?",
        "experiment": "Measure AlgB phosphorylation and alginate-regulatory promoter output in kinB mutant and complemented strains.",
    },
    "algB": {
        "id": "Q88RJ6",
        "ordered_locus": "PP_0133",
        "description": (
            "algB encodes an AlgB/NtrC-family transcriptional regulatory protein in Pseudomonas putida "
            "KT2440. The protein combines an N-terminal receiver domain, a sigma-54 enhancer-binding "
            "AAA+ ATPase region, and an HTH/Fis DNA-binding domain, consistent with phosphorelay-linked "
            "transcriptional regulation of alginate biosynthesis genes."
        ),
        "uniprot": "RecName: Full=Alginate biosynthesis transcriptional regulatory protein AlgB",
        "uniprot_extra": "CC   -!- FUNCTION: Positive regulator of the alginate biosynthetic gene algD.",
        "asta": "Protein Description:** RecName: Full=Alginate biosynthesis transcriptional regulatory protein AlgB",
        "term_reviews": ALGB_LIKE_REVIEWS,
        "new_annotations": [
            {
                "term": TERMS["response_regulator"],
                "qualifier": "enables",
                "summary": "AlgB should be represented as a phosphorelay response regulator.",
                "reason": "AlgB has a receiver domain and is already annotated to phosphorelay signal transduction.",
            }
        ],
        "core_functions": [
            {
                "description": "AlgB phosphorelay response regulator controlling alginate-associated transcription.",
                "molecular_function": TERMS["response_regulator"],
                "directly_involved_in": [
                    TERMS["phosphorelay"],
                    TERMS["transcription_reg"],
                    TERMS["alginic_acid_biosynthesis"],
                ],
            },
            {
                "description": "Sequence-specific DNA binding by the HTH/Fis output domain of AlgB.",
                "molecular_function": TERMS["sequence_specific_dna_binding"],
                "directly_involved_in": [TERMS["transcription_reg"]],
            },
        ],
        "question": "Which KT2440 promoters are directly bound and activated by AlgB under alginate-inducing conditions?",
        "experiment": "Combine AlgB ChIP-seq or CUT&RUN with algD promoter reporter assays in wild-type and kinB mutant backgrounds.",
    },
    "algR": {
        "id": "Q88RE6",
        "ordered_locus": "PP_0185",
        "description": (
            "algR encodes a predicted AlgR/LytTR-family two-component response regulator in "
            "Pseudomonas putida KT2440. Its receiver and LytTR DNA-binding domains support a soluble "
            "transcription-regulatory role in alginate or surface-behavior control."
        ),
        "uniprot": "SubName: Full=Positive alginate biosynthesis regulatory protein",
        "uniprot_extra": "DR   InterPro; IPR007492; LytTR_DNA-bd_dom.",
        "asta": "Protein Description:** SubName: Full=Positive alginate biosynthesis regulatory protein",
        "term_reviews": RESPONSE_REGULATOR_REVIEWS,
        "core_functions": [
            {
                "description": "AlgR-family phosphorelay response regulator controlling transcription.",
                "molecular_function": TERMS["response_regulator"],
                "directly_involved_in": [TERMS["phosphorelay"], TERMS["transcription_reg"]],
                "locations": [TERMS["cytosol"]],
            },
            {
                "description": "LytTR-domain cis-regulatory DNA binding by AlgR.",
                "molecular_function": TERMS["cis_binding"],
                "directly_involved_in": [TERMS["transcription_reg"]],
                "locations": [TERMS["cytosol"]],
            },
        ],
        "question": "Which alginate or biofilm promoters are direct AlgR targets in KT2440?",
        "experiment": "Map AlgR binding sites and transcriptional changes in algR deletion and complemented strains.",
    },
    "wspC": {
        "id": "Q88MS8",
        "ordered_locus": "PP_1490",
        "description": (
            "wspC encodes CheR1, a Wsp chemosensory-system methyltransferase in Pseudomonas putida "
            "KT2440. UniProt and primary literature support a role in biofilm formation rather than "
            "the CheR2-dependent chemotaxis branch."
        ),
        "uniprot": "RecName: Full=Probable biofilm formation methyltransferase WspC",
        "uniprot_extra": "CC   -!- FUNCTION: Involved in biofilm formation. {ECO:0000269|PubMed:23677992}.",
        "asta": "Protein Description:** RecName: Full=Probable biofilm formation methyltransferase WspC",
        "term_reviews": {
            "GO:0008757": (
                "MODIFY",
                "The broad SAM-dependent methyltransferase annotation is correct but should be specialized to CheR-type protein-glutamate O-methyltransferase activity.",
                [TERMS["protein_glutamate_methyltransferase"]],
            ),
        },
        "new_annotations": [
            {
                "term": TERMS["biofilm_formation"],
                "qualifier": "involved_in",
                "summary": "WspC/CheR1 should be represented as involved in biofilm formation.",
                "reason": "The P. putida CheR paralogue study reports impaired biofilm formation for the CheR1 mutant and assigns CheR1 to a biofilm-control route.",
                "evidence_type": "IMP",
                "original_reference_id": "PMID:23677992",
                "extra_support": [
                    {
                        "reference_id": "PMID:23677992",
                        "supporting_text": "In contrast, biofilm formation of the CheR1 mutant was largely impaired but not affected in the other mutants.",
                    },
                    {
                        "reference_id": "PMID:23677992",
                        "supporting_text": "CheR1 forms part of a chemosensory route that controls biofilm formation.",
                    },
                ],
            }
        ],
        "pmid_refs": [
            {
                "id": "PMID:23677992",
                "title": "High specificity in CheR methyltransferase function: CheR2 of Pseudomonas putida is essential for chemotaxis, whereas CheR1 is involved in biofilm formation.",
                "finding": "CheR1 forms part of a chemosensory route that controls biofilm formation.",
            }
        ],
        "core_functions": [
            {
                "description": "CheR-type methyltransferase activity in the Wsp biofilm-control chemosensory route.",
                "molecular_function": TERMS["protein_glutamate_methyltransferase"],
                "directly_involved_in": [TERMS["biofilm_formation"]],
            }
        ],
        "question": "Which Wsp receptor or output regulator is the cognate substrate/pathway partner for WspC in KT2440?",
        "experiment": "Assay WspC-dependent receptor methylation, c-di-GMP output, and biofilm formation in wspC and Wsp-pathway mutants.",
    },
    "fleS": {
        "id": "Q88ET1",
        "ordered_locus": "PP_4372",
        "description": (
            "fleS encodes a soluble FleS-family sensor histidine kinase in Pseudomonas putida KT2440. "
            "The protein contains PAS, HisKA, and HATPase domains, supporting a two-component "
            "phosphorelay sensor role, most likely in flagellar or surface-behavior regulation."
        ),
        "uniprot": "RecName: Full=histidine kinase",
        "uniprot_extra": "DR   InterPro; IPR005467; His_kinase_dom.",
        "asta": "Protein Description:** RecName: Full=histidine kinase",
        "term_reviews": FLES_REVIEWS,
        "core_functions": [
            {
                "description": "FleS-family sensor histidine kinase activity feeding a bacterial phosphorelay.",
                "molecular_function": TERMS["sensor_kinase"],
                "directly_involved_in": [TERMS["phosphorelay"]],
            }
        ],
        "question": "Does KT2440 FleS regulate flagellar biogenesis, motility, biofilm state transitions, or a different surface behavior?",
        "experiment": "Measure flagellar gene expression, motility, and biofilm phenotypes in fleS and candidate cognate response-regulator mutants.",
    },
    "PP_4696": {
        "id": "Q88DX2",
        "ordered_locus": "PP_4696",
        "description": (
            "PP_4696 encodes an AlgB-like sigma-54 enhancer-binding response regulator in "
            "Pseudomonas putida KT2440. Its receiver and AAA+ sigma-54 activator domains support a "
            "phosphorelay-linked transcription-regulatory role, but the cognate sensor and direct "
            "targets remain unclear in this first pass."
        ),
        "uniprot": "RecName: Full=Alginate biosynthesis transcriptional regulatory protein AlgB",
        "uniprot_extra": "DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.",
        "asta": "Protein Description:** RecName: Full=Alginate biosynthesis transcriptional regulatory protein AlgB",
        "term_reviews": ALGB_LIKE_REVIEWS,
        "new_annotations": [
            {
                "term": TERMS["response_regulator"],
                "qualifier": "enables",
                "summary": "PP_4696 should be represented as a phosphorelay response regulator.",
                "reason": "The protein has a receiver domain and is already annotated to phosphorelay signal transduction.",
            }
        ],
        "core_functions": [
            {
                "description": "AlgB-like phosphorelay response regulator controlling transcription.",
                "molecular_function": TERMS["response_regulator"],
                "directly_involved_in": [TERMS["phosphorelay"], TERMS["transcription_reg"]],
            }
        ],
        "question": "What is the cognate sensor and regulon for the PP_4696 AlgB-like response regulator?",
        "experiment": "Use phosphotransfer assays and transcriptomics to identify the sensor kinase and direct transcriptional targets of PP_4696.",
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
    items = [
        support(uniprot_ref(gene), cfg["uniprot"]),
        support(asta_ref(gene), cfg["asta"]),
    ]
    if cfg.get("uniprot_extra"):
        items.append(support(uniprot_ref(gene), cfg["uniprot_extra"]))
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
        review["summary"] = f"{label} is true or plausible but too broad as a core annotation."
    return review


def make_new_annotation(gene: str, cfg: dict, item: dict) -> dict:
    supported_by = [*base_support(gene, cfg), *item.get("extra_support", [])]
    return {
        "term": item["term"],
        "evidence_type": item.get("evidence_type", "IEA"),
        "original_reference_id": item.get("original_reference_id", uniprot_ref(gene)),
        "qualifier": item["qualifier"],
        "review": {
            "summary": item["summary"],
            "action": "NEW",
            "reason": item["reason"],
            "supported_by": supported_by,
        },
    }


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
    for ref in cfg.get("pmid_refs", []):
        ensure_reference(data, ref["id"], ref["title"], ref.get("finding"))
    normalize_go_ref_titles(data)

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
        core["supported_by"] = base_support(gene, cfg)
        if gene == "wspC":
            core["supported_by"].append(
                support("PMID:23677992", "CheR1 forms part of a chemosensory route that controls biofilm formation.")
            )
    data["core_functions"] = cfg["core_functions"]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": cfg["question"]}]
    data["suggested_experiments"] = [
        {"description": cfg["experiment"], "experiment_type": "targeted regulatory or phenotype assay"}
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
        "id": "MODULE:alginate_biofilm_regulation_boundary",
        "title": "Alginate and biofilm regulation boundary",
        "description": (
            "Boundary module for the ppu02020 alginate/biofilm partition in Pseudomonas putida "
            "KT2440. It captures KinB/AlgB-like phosphorelay regulators, AlgR-family transcription "
            "control, WspC/CheR1 biofilm methyltransferase context, and FleS-family surface-behavior "
            "sensor kinase context. This is a curated partition of the broad KEGG two-component-system "
            "map rather than a single linear pathway."
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
                    "The partition table groups kinB, algB, algR, wspC, fleS, and PP_4696 into the "
                    "alginate/biofilm regulation bucket."
                ),
            },
            {
                "source_id": "PMID:23677992",
                "title": "High specificity in CheR methyltransferase function: CheR2 of Pseudomonas putida is essential for chemotaxis, whereas CheR1 is involved in biofilm formation.",
                "statement": "CheR1/WspC is experimentally connected to biofilm formation in Pseudomonas putida.",
            },
        ],
        "notes": (
            "The bucket is intentionally a boundary module. KinB/AlgB and AlgR are alginate-linked "
            "regulatory proteins, WspC belongs to a Wsp chemosensory biofilm route, and FleS is kept as "
            "surface-behavior phosphorelay context pending a more precise module assignment."
        ),
        "module": {
            "id": "alginate_biofilm_regulation_boundary",
            "label": "Alginate and biofilm regulation boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                {"preferred_term": t["label"], "term": t}
                for t in [
                    TERMS["phosphorelay"],
                    TERMS["transcription_reg"],
                    TERMS["alginic_acid_biosynthesis"],
                    TERMS["biofilm_formation"],
                ]
            ],
            "context": {
                "cellular_components": [
                    {"preferred_term": "plasma membrane", "term": TERMS["plasma_membrane"]},
                    {"preferred_term": "cytosol", "term": TERMS["cytosol"]},
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "KinB/AlgB alginate transcription control",
                    "node": {
                        "id": "kinb_algb_regulation",
                        "label": "KinB/AlgB regulation",
                        "module_type": "REGULATORY_STEP",
                        "description": "KinB and AlgB provide sensor/regulator context for alginate-associated transcription.",
                        "annotons": [
                            annoton("kinB", "kinB: sensor kinase", TERMS["sensor_kinase"], [TERMS["phosphorelay"]], [TERMS["plasma_membrane"]], "Membrane sensor histidine kinase in the alginate regulatory neighborhood."),
                            annoton("algB", "algB: AlgB response regulator", TERMS["response_regulator"], [TERMS["phosphorelay"], TERMS["transcription_reg"], TERMS["alginic_acid_biosynthesis"]], [TERMS["cytosol"]], "AlgB/NtrC-family transcriptional response regulator."),
                        ],
                        "connections": [
                            {"source": "kinb_sensor_kinase", "target": "algb_algb_response_regulator", "connection_type": "PROVIDES_INPUT_FOR", "description": "KinB is adjacent to AlgB and is the likely phosphorelay input in this local regulatory pair."},
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "AlgR-family alginate/surface transcription control",
                    "node": {
                        "id": "algr_transcription_regulation",
                        "label": "AlgR transcription regulation",
                        "module_type": "REGULATORY_STEP",
                        "description": "AlgR is a receiver/LytTR-domain response regulator for alginate or surface-behavior transcriptional control.",
                        "annotons": [
                            annoton("algR", "algR: AlgR response regulator", TERMS["response_regulator"], [TERMS["phosphorelay"], TERMS["transcription_reg"]], [TERMS["cytosol"]], "AlgR/LytTR-family DNA-binding response regulator."),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "WspC/CheR1 biofilm chemosensory methylation",
                    "node": {
                        "id": "wspc_biofilm_route",
                        "label": "WspC biofilm route",
                        "module_type": "REGULATORY_STEP",
                        "description": "WspC/CheR1 is a CheR-type methyltransferase connected to biofilm formation.",
                        "annotons": [
                            annoton("wspC", "wspC: CheR1 methyltransferase", TERMS["protein_glutamate_methyltransferase"], [TERMS["biofilm_formation"]], [TERMS["cytosol"]], "CheR-type methyltransferase in a biofilm-control chemosensory route."),
                        ],
                    },
                },
                {
                    "order": 4,
                    "role": "FleS and PP_4696 surface-behavior regulatory context",
                    "node": {
                        "id": "fles_pp4696_context",
                        "label": "FleS/PP_4696 context",
                        "module_type": "REGULATORY_STEP",
                        "description": "FleS and PP_4696 are phosphorelay regulators retained as surface-behavior context pending precise targets.",
                        "annotons": [
                            annoton("fleS", "fleS: FleS sensor kinase", TERMS["sensor_kinase"], [TERMS["phosphorelay"]], [TERMS["cytosol"]], "FleS-family sensor histidine kinase."),
                            annoton("PP_4696", "PP_4696: AlgB-like regulator", TERMS["response_regulator"], [TERMS["phosphorelay"], TERMS["transcription_reg"]], [TERMS["cytosol"]], "AlgB-like sigma-54 enhancer-binding response regulator."),
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
