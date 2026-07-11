#!/usr/bin/env python3
"""First-pass curation for the ppu02020 iron-uptake regulation bucket."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
MODULE_PATH = ROOT / "modules/iron_uptake_regulation_boundary.yaml"
SPECIES = "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "response_regulator": {"id": "GO:0000156", "label": "phosphorelay response regulator activity"},
    "sensor_kinase": {"id": "GO:0000155", "label": "phosphorelay sensor kinase activity"},
    "phosphorelay": {"id": "GO:0000160", "label": "phosphorelay signal transduction system"},
    "histidine_kinase": {"id": "GO:0004673", "label": "protein histidine kinase activity"},
    "cis_binding": {"id": "GO:0000976", "label": "transcription cis-regulatory region binding"},
    "dna_binding": {"id": "GO:0003677", "label": "DNA binding"},
    "dna_tf": {"id": "GO:0003700", "label": "DNA-binding transcription factor activity"},
    "cytoplasm": {"id": "GO:0005737", "label": "cytoplasm"},
    "cytosol": {"id": "GO:0005829", "label": "cytosol"},
    "plasma_membrane": {"id": "GO:0005886", "label": "plasma membrane"},
    "membrane": {"id": "GO:0016020", "label": "membrane"},
    "outer_membrane": {"id": "GO:0009279", "label": "cell outer membrane"},
    "transcription_initiation": {"id": "GO:0006352", "label": "DNA-templated transcription initiation"},
    "transcription_reg": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "protein_dna_complex": {"id": "GO:0032993", "label": "protein-DNA complex"},
    "signal_transduction": {"id": "GO:0007165", "label": "signal transduction"},
    "kinase": {"id": "GO:0016301", "label": "kinase activity"},
    "transferase": {"id": "GO:0016740", "label": "transferase activity"},
    "phosphorus_transferase": {"id": "GO:0016772", "label": "transferase activity, transferring phosphorus-containing groups"},
    "siderophore_iron_transporter": {"id": "GO:0015343", "label": "siderophore-iron transmembrane transporter activity"},
    "siderophore_uptake_transporter": {"id": "GO:0015344", "label": "siderophore uptake transmembrane transporter activity"},
    "siderophore_transport": {"id": "GO:0015891", "label": "siderophore transport"},
    "siderophore_iron_import": {"id": "GO:0033214", "label": "siderophore-iron import into cell"},
    "signaling_receptor": {"id": "GO:0038023", "label": "signaling receptor activity"},
    "siderophore_transmembrane_transport": {"id": "GO:0044718", "label": "siderophore transmembrane transport"},
    "sigma_antagonist": {"id": "GO:0016989", "label": "sigma factor antagonist activity"},
    "sigma_factor": {"id": "GO:0016987", "label": "sigma factor activity"},
    "negative_transcription_reg": {"id": "GO:0045892", "label": "negative regulation of DNA-templated transcription"},
    "transcription_initiation_reg": {"id": "GO:2000142", "label": "regulation of DNA-templated transcription initiation"},
}


SENSOR_REVIEWS = {
    "GO:0000155": ("ACCEPT", "This protein has the conserved HAMP/HisKA/HATPase architecture of a phosphorelay sensor kinase.", None),
    "GO:0000160": ("ACCEPT", "The sensor kinase participates in His-Asp phosphorelay signaling with a cognate response regulator.", None),
    "GO:0004673": ("ACCEPT", "Protein histidine kinase activity is the catalytic mechanism for response-regulator phosphorylation.", None),
    "GO:0005886": ("ACCEPT", "The protein is a predicted multi-pass bacterial plasma-membrane sensor kinase.", None),
    "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than phosphorelay signal transduction.", None),
    "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than plasma membrane for this sensor kinase.", None),
    "GO:0016301": ("MARK_AS_OVER_ANNOTATED", "Generic kinase activity is less informative than phosphorelay sensor kinase and protein histidine kinase activity.", None),
    "GO:0016740": ("MARK_AS_OVER_ANNOTATED", "Generic transferase activity is less informative than the histidine kinase terms.", None),
    "GO:0016772": ("MARK_AS_OVER_ANNOTATED", "This broad phosphorus-transfer term is less informative than protein histidine kinase activity.", None),
}


RESPONSE_REGULATOR_REVIEWS = {
    "GO:0000156": ("ACCEPT", "The receiver-domain protein is a phosphorelay response regulator.", None),
    "GO:0000160": ("ACCEPT", "The protein acts in a two-component phosphorelay system.", None),
    "GO:0000976": ("ACCEPT", "The OmpR/PhoB-type DNA-binding domain supports transcription cis-regulatory region binding.", None),
    "GO:0003677": ("MARK_AS_OVER_ANNOTATED", "Generic DNA binding is less informative than transcription cis-regulatory region binding.", None),
    "GO:0005737": ("ACCEPT", "A cytoplasmic location is appropriate for a soluble bacterial response regulator.", None),
    "GO:0005829": ("KEEP_AS_NON_CORE", "Cytosol is compatible with cytoplasmic response-regulator function but is not the preferred core location.", None),
    "GO:0006355": ("ACCEPT", "The DNA-binding response regulator controls transcription of target genes.", None),
    "GO:0032993": ("KEEP_AS_NON_CORE", "Protein-DNA complex membership is transient context for a DNA-bound regulator, not the core function.", None),
}


SIGMA_REVIEWS = {
    "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is plausible for the sigma factor-containing holoenzyme but is less informative than sigma factor activity.", None),
    "GO:0003700": ("MARK_AS_OVER_ANNOTATED", "By GO convention bacterial sigma factors should be represented by sigma factor activity rather than DNA-binding transcription factor activity.", [TERMS["sigma_factor"]]),
    "GO:0006352": ("ACCEPT", "Sigma factors direct RNA polymerase promoter selection during DNA-templated transcription initiation.", None),
    "GO:0006355": ("KEEP_AS_NON_CORE", "Regulation of transcription is correct but broad relative to initiation-specific sigma factor function.", None),
    "GO:0016987": ("ACCEPT", "Sigma factor activity is the defining molecular function of this ECF sigma factor.", None),
    "GO:2000142": ("ACCEPT", "Sigma factor activity regulates which promoters initiate transcription.", None),
}


FEC_R_REVIEWS = {
    "GO:0016989": ("ACCEPT", "The FecR-domain transmembrane sensor is an anti-sigma/sigma-factor antagonist component.", None),
    "GO:0045892": ("ACCEPT", "A sigma-factor antagonist negatively regulates transcription by restraining sigma-factor-dependent initiation.", None),
}


GENES = {
    "pfeS-I": {
        "description": (
            "pfeS-I encodes a predicted membrane sensory histidine kinase in Pseudomonas putida KT2440. "
            "Its HAMP, HisKA, and HATPase domains support a two-component sensor role, and its ppu02020 "
            "partition with the adjacent PfeR-like response regulator places it in an iron/siderophore "
            "uptake regulatory context."
        ),
        "uniprot": "RecName: Full=histidine kinase",
        "uniprot_extra": "DR   InterPro; IPR005467; His_kinase_dom.",
        "asta": "Protein Description:** RecName: Full=histidine kinase",
        "term_reviews": SENSOR_REVIEWS,
        "core_functions": [
            {
                "description": "Predicted membrane sensor kinase for a PfeR-like iron/siderophore uptake regulatory system.",
                "molecular_function": TERMS["sensor_kinase"],
                "directly_involved_in": [TERMS["phosphorelay"]],
                "locations": [TERMS["plasma_membrane"]],
            }
        ],
        "question": "What iron or ferric-siderophore signal activates the pfeS-I/PfeR-like regulatory pair?",
        "experiment": "Measure pfeR-target promoter activity in pfeS-I mutant and complemented strains across iron-replete, iron-limited, and siderophore-supplemented media.",
    },
    "PP_0534": {
        "description": (
            "PP_0534 encodes a predicted PfeR/OmpR-family response regulator in Pseudomonas putida KT2440. "
            "The protein has a receiver domain and an OmpR/PhoB-type DNA-binding domain, consistent with "
            "a cytoplasmic transcription regulator paired with the nearby pfeS-I sensor kinase."
        ),
        "uniprot": "SubName: Full=Transcriptional regulator PfeR",
        "uniprot_extra": "DR   InterPro; IPR001867; OmpR/PhoB-type_DNA-bd.",
        "asta": "Protein Description:** SubName: Full=Transcriptional regulator PfeR",
        "term_reviews": RESPONSE_REGULATOR_REVIEWS,
        "core_functions": [
            {
                "description": "PfeR-like phosphorelay response regulator controlling transcription in an iron/siderophore uptake context.",
                "molecular_function": TERMS["response_regulator"],
                "directly_involved_in": [TERMS["phosphorelay"], TERMS["transcription_reg"]],
                "locations": [TERMS["cytoplasm"]],
            },
            {
                "description": "OmpR/PhoB-family cis-regulatory DNA binding for transcriptional control.",
                "molecular_function": TERMS["cis_binding"],
                "directly_involved_in": [TERMS["transcription_reg"]],
                "locations": [TERMS["cytoplasm"]],
            },
        ],
        "question": "Which outer-membrane receptor or siderophore-uptake genes are directly regulated by PP_0534?",
        "experiment": "Compare transcript levels and promoter occupancy in wild-type, PP_0534 deletion, and complemented strains under iron limitation.",
    },
    "PP_1651": {
        "description": (
            "PP_1651 encodes a predicted two-component response regulator in Pseudomonas putida KT2440. "
            "Receiver and OmpR/PhoB-type DNA-binding domains support a cytoplasmic transcription-regulator "
            "role, likely paired with the adjacent pfeS-II sensor kinase in an iron-uptake regulatory locus."
        ),
        "uniprot": "SubName: Full=Two-component response regulator",
        "uniprot_extra": "DR   InterPro; IPR001867; OmpR/PhoB-type_DNA-bd.",
        "asta": "Protein Description:** SubName: Full=Two-component response regulator",
        "term_reviews": RESPONSE_REGULATOR_REVIEWS,
        "core_functions": [
            {
                "description": "PfeR-like phosphorelay response regulator controlling transcription in an iron/siderophore uptake context.",
                "molecular_function": TERMS["response_regulator"],
                "directly_involved_in": [TERMS["phosphorelay"], TERMS["transcription_reg"]],
                "locations": [TERMS["cytoplasm"]],
            },
            {
                "description": "OmpR/PhoB-family cis-regulatory DNA binding for transcriptional control.",
                "molecular_function": TERMS["cis_binding"],
                "directly_involved_in": [TERMS["transcription_reg"]],
                "locations": [TERMS["cytoplasm"]],
            },
        ],
        "question": "Does PP_1651 regulate the same iron-uptake target class as PP_0534 or a distinct receptor system?",
        "experiment": "Use RNA-seq or promoter reporters in PP_1651 and pfeS-II mutants during iron limitation and ferric-siderophore exposure.",
    },
    "pfeS-II": {
        "description": (
            "pfeS-II encodes a predicted membrane sensory histidine kinase in Pseudomonas putida KT2440. "
            "Its HAMP, HisKA, and HATPase domains support a two-component sensor role, and it is paired "
            "with the adjacent PP_1651 response regulator in the ppu02020 iron-uptake partition."
        ),
        "uniprot": "RecName: Full=histidine kinase",
        "uniprot_extra": "DR   InterPro; IPR005467; His_kinase_dom.",
        "asta": "Protein Description:** RecName: Full=histidine kinase",
        "term_reviews": SENSOR_REVIEWS,
        "core_functions": [
            {
                "description": "Predicted membrane sensor kinase for a PP_1651 response-regulator iron/siderophore uptake system.",
                "molecular_function": TERMS["sensor_kinase"],
                "directly_involved_in": [TERMS["phosphorelay"]],
                "locations": [TERMS["plasma_membrane"]],
            }
        ],
        "question": "Which iron-source signal is sensed by the pfeS-II/PP_1651 two-component pair?",
        "experiment": "Test pfeS-II-dependent PP_1651 phosphorylation and target promoter activity under defined iron-source conditions.",
    },
    "fepA": {
        "description": (
            "fepA encodes a TonB-dependent outer-membrane ferric-siderophore receptor in Pseudomonas putida "
            "KT2440. Its plug and beta-barrel TonB-dependent receptor domains support high-affinity "
            "siderophore-iron uptake across the Gram-negative outer membrane."
        ),
        "uniprot": "SubName: Full=Ferric enterobactin transport system outer membrane subunit",
        "uniprot_extra": "DR   InterPro; IPR000531; Beta-barrel_TonB.",
        "asta": "Protein Description:** SubName: Full=Ferric enterobactin transport system outer membrane subunit",
        "term_reviews": {
            "GO:0009279": ("ACCEPT", "FepA is a TonB-dependent beta-barrel receptor in the cell outer membrane.", None),
            "GO:0015343": ("ACCEPT", "Siderophore-iron transmembrane transporter activity captures the core TonB-dependent receptor function.", None),
            "GO:0015344": ("ACCEPT", "Siderophore uptake transporter activity is appropriate for the TonB-dependent outer-membrane receptor.", None),
            "GO:0015891": ("ACCEPT", "FepA participates in siderophore transport.", None),
            "GO:0033214": ("ACCEPT", "FepA mediates siderophore-iron import into the cell envelope/cell.", None),
            "GO:0038023": ("KEEP_AS_NON_CORE", "Some TonB-dependent receptors participate in cell-surface signaling, but transport is the core function for this first pass.", None),
            "GO:0044718": ("ACCEPT", "FepA participates in siderophore transmembrane transport.", None),
        },
        "core_functions": [
            {
                "description": "TonB-dependent ferric-siderophore uptake across the cell outer membrane.",
                "molecular_function": TERMS["siderophore_iron_transporter"],
                "directly_involved_in": [TERMS["siderophore_iron_import"], TERMS["siderophore_transmembrane_transport"]],
                "locations": [TERMS["outer_membrane"]],
            }
        ],
        "question": "Which siderophore ligands are transported by KT2440 FepA under iron limitation?",
        "experiment": "Measure uptake and growth rescue with ferric enterobactin, pyoverdine, and heterologous siderophores in fepA mutant and complemented strains.",
    },
    "PP_3576": {
        "description": (
            "PP_3576 encodes a predicted FecR-family transmembrane anti-sigma/sensor protein in "
            "Pseudomonas putida KT2440. Its FecR and ferric-dicitrate sensor transmembrane domains "
            "support a role in controlling a nearby ECF sigma factor in an iron-uptake regulatory system."
        ),
        "uniprot": "SubName: Full=Transmembrane sensor",
        "uniprot_extra": "DR   InterPro; IPR006860; FecR.",
        "asta": "Protein Description:** SubName: Full=Transmembrane sensor",
        "term_reviews": FEC_R_REVIEWS,
        "core_functions": [
            {
                "description": "FecR-family transmembrane anti-sigma/sensor control of an ECF sigma factor.",
                "molecular_function": TERMS["sigma_antagonist"],
                "directly_involved_in": [TERMS["negative_transcription_reg"]],
            }
        ],
        "question": "Which outer-membrane receptor signal is transduced through PP_3576 to the adjacent FecI-like sigma factor?",
        "experiment": "Assay fecI-dependent promoter activity in PP_3576 mutant and complemented strains exposed to ferric-siderophore ligands.",
    },
    "fecI": {
        "description": (
            "fecI encodes an ECF-family sigma factor in Pseudomonas putida KT2440. Its sigma-70 region 2 "
            "and region 4 domains support promoter-specific RNA polymerase recruitment, likely for an "
            "iron-uptake regulon controlled by an adjacent FecR-family transmembrane sensor."
        ),
        "uniprot": "SubName: Full=RNA polymerase, sigma 19 factor",
        "uniprot_extra": "DR   InterPro; IPR007627; RNA_pol_sigma70_r2.",
        "asta": "Protein Description:** SubName: Full=RNA polymerase, sigma 19 factor",
        "term_reviews": SIGMA_REVIEWS,
        "core_functions": [
            {
                "description": "ECF sigma factor directing RNA polymerase to iron-uptake regulon promoters.",
                "molecular_function": TERMS["sigma_factor"],
                "directly_involved_in": [TERMS["transcription_initiation"], TERMS["transcription_initiation_reg"]],
            }
        ],
        "question": "Which promoters are directly recognized by FecI in KT2440?",
        "experiment": "Map FecI-dependent transcription start sites and promoter motifs during iron limitation and ferric-siderophore exposure.",
    },
    "PP_4607": {
        "description": (
            "PP_4607 encodes a predicted FecR-family transmembrane anti-sigma/sensor protein in "
            "Pseudomonas putida KT2440. Its FecR and ferric-dicitrate sensor transmembrane domains "
            "support a role in envelope-to-cytoplasm signaling for iron-uptake gene expression."
        ),
        "uniprot": "SubName: Full=Transmembrane sensor",
        "uniprot_extra": "DR   InterPro; IPR006860; FecR.",
        "asta": "Protein Description:** SubName: Full=Transmembrane sensor",
        "term_reviews": FEC_R_REVIEWS,
        "core_functions": [
            {
                "description": "FecR-family transmembrane anti-sigma/sensor control of an ECF sigma factor.",
                "molecular_function": TERMS["sigma_antagonist"],
                "directly_involved_in": [TERMS["negative_transcription_reg"]],
            }
        ],
        "question": "Does PP_4607 control PP_4611, another ECF sigma factor, or a separate iron-uptake locus?",
        "experiment": "Construct PP_4607 and PP_4611 mutants and compare ECF-sigma-dependent promoter activity under iron-source perturbations.",
    },
    "PP_4611": {
        "description": (
            "PP_4611 encodes an ECF-family sigma factor in Pseudomonas putida KT2440. Its sigma-70 region "
            "2 and region 4 domains support promoter-specific RNA polymerase recruitment, likely in an "
            "iron-uptake or cell-surface signaling regulon adjacent to FecR-family proteins."
        ),
        "uniprot": "SubName: Full=RNA polymerase sigma-70 factor, ECF subfamily",
        "uniprot_extra": "DR   InterPro; IPR007627; RNA_pol_sigma70_r2.",
        "asta": "Protein Description:** SubName: Full=RNA polymerase sigma-70 factor, ECF subfamily",
        "term_reviews": SIGMA_REVIEWS,
        "core_functions": [
            {
                "description": "ECF sigma factor directing RNA polymerase to condition-specific promoters in an iron-uptake regulatory context.",
                "molecular_function": TERMS["sigma_factor"],
                "directly_involved_in": [TERMS["transcription_initiation"], TERMS["transcription_initiation_reg"]],
            }
        ],
        "question": "Which PP_4611-dependent promoters and iron-source conditions define this ECF sigma regulon?",
        "experiment": "Perform promoter reporter and RNA-seq comparisons of wild-type and PP_4611 deletion strains during iron limitation.",
    },
    "PP_4612": {
        "description": (
            "PP_4612 encodes a predicted FecR-family transmembrane anti-sigma protein in Pseudomonas "
            "putida KT2440. Its FecR and ferric-dicitrate sensor transmembrane domains support a role "
            "in controlling ECF sigma factor availability for iron-uptake gene expression."
        ),
        "uniprot": "SubName: Full=FecR protein",
        "uniprot_extra": "DR   InterPro; IPR006860; FecR.",
        "asta": "Protein Description:** SubName: Full=FecR protein",
        "term_reviews": FEC_R_REVIEWS,
        "core_functions": [
            {
                "description": "FecR-family anti-sigma control of ECF sigma-factor-dependent transcription.",
                "molecular_function": TERMS["sigma_antagonist"],
                "directly_involved_in": [TERMS["negative_transcription_reg"]],
            }
        ],
        "question": "Is PP_4612 the cognate anti-sigma/sensor partner for PP_4611?",
        "experiment": "Measure PP_4611 activity and stability in PP_4612 mutant and complemented strains under iron-limited conditions.",
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

    for annotation in data["existing_annotations"]:
        go_id = annotation["term"]["id"]
        if go_id not in cfg["term_reviews"]:
            raise KeyError(f"Unhandled annotation {go_id} for {gene}")
        annotation["review"] = make_review(gene, cfg, rows, go_id)

    for core in cfg["core_functions"]:
        core["supported_by"] = supported_by_for_core(gene, cfg)
    data["core_functions"] = cfg["core_functions"]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": cfg["question"]}]
    data["suggested_experiments"] = [
        {
            "description": cfg["experiment"],
            "experiment_type": "targeted iron-uptake regulatory or transport assay",
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
        "id": "MODULE:iron_uptake_regulation_boundary",
        "title": "Iron uptake regulation boundary",
        "description": (
            "Boundary module for the ppu02020 iron-uptake regulation partition in Pseudomonas putida "
            "KT2440. It captures PfeS/PfeR-like two-component regulators, TonB-dependent ferric "
            "siderophore receptor activity, and FecI/FecR-like ECF sigma/anti-sigma signaling. This is "
            "a partition of the broad KEGG two-component-system map, not a single linear pathway."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02020",
                "title": "Two-component system - Pseudomonas putida KT2440",
                "statement": (
                    "KEGG ppu02020 supplies the umbrella two-component-system membership; the iron "
                    "uptake genes are curated here as a smaller boundary module."
                ),
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.tsv",
                "title": "PSEPK ppu02020 partition table",
                "statement": (
                    "The partition table groups pfeS-I, PP_0534, PP_1651, pfeS-II, fepA, PP_3576, "
                    "fecI, PP_4607, PP_4611, and PP_4612 into the iron uptake regulation bucket."
                ),
            },
        ],
        "notes": (
            "The bucket mixes canonical two-component regulators with FecI/FecR ECF sigma signaling and "
            "TonB-dependent outer-membrane receptor context. The module therefore records a boundary "
            "around iron uptake regulation rather than treating all members as His-Asp phosphorelay proteins."
        ),
        "module": {
            "id": "iron_uptake_regulation_boundary",
            "label": "Iron uptake regulation boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                {"preferred_term": t["label"], "term": t}
                for t in [
                    TERMS["phosphorelay"],
                    TERMS["transcription_reg"],
                    TERMS["sigma_factor"],
                    TERMS["sigma_antagonist"],
                    TERMS["siderophore_iron_import"],
                    TERMS["siderophore_transport"],
                ]
            ],
            "context": {
                "cellular_components": [
                    {"preferred_term": "cytoplasm", "term": TERMS["cytoplasm"]},
                    {"preferred_term": "membrane", "term": TERMS["membrane"]},
                    {"preferred_term": "cell outer membrane", "term": TERMS["outer_membrane"]},
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "PfeS/PfeR-like two-component iron-uptake regulators",
                    "node": {
                        "id": "pfe_two_component_regulators",
                        "label": "PfeS/PfeR-like two-component regulators",
                        "module_type": "REGULATORY_STEP",
                        "description": (
                            "Two predicted membrane sensor kinases and two OmpR/PhoB-family response "
                            "regulators provide His-Asp regulatory context for iron or ferric-siderophore "
                            "uptake genes."
                        ),
                        "annotons": [
                            annoton("pfeS-I", "pfeS-I: iron-uptake sensor kinase", TERMS["sensor_kinase"], [TERMS["phosphorelay"]], [TERMS["plasma_membrane"]], "Predicted PfeS-family membrane sensor kinase."),
                            annoton("PP_0534", "PP_0534/PfeR: response regulator", TERMS["response_regulator"], [TERMS["phosphorelay"], TERMS["transcription_reg"]], [TERMS["cytoplasm"]], "Predicted PfeR-like DNA-binding response regulator."),
                            annoton("pfeS-II", "pfeS-II: iron-uptake sensor kinase", TERMS["sensor_kinase"], [TERMS["phosphorelay"]], [TERMS["plasma_membrane"]], "Predicted PfeS-family membrane sensor kinase."),
                            annoton("PP_1651", "PP_1651: response regulator", TERMS["response_regulator"], [TERMS["phosphorelay"], TERMS["transcription_reg"]], [TERMS["cytoplasm"]], "Predicted DNA-binding response regulator."),
                        ],
                        "connections": [
                            {"source": "pfes_i_iron_uptake_sensor_kinase", "target": "pp_0534_pfer_response_regulator", "connection_type": "PROVIDES_INPUT_FOR", "description": "pfeS-I and PP_0534 are the paired sensor/regulator in the PP_0533-PP_0534 locus."},
                            {"source": "pfes_ii_iron_uptake_sensor_kinase", "target": "pp_1651_response_regulator", "connection_type": "PROVIDES_INPUT_FOR", "description": "pfeS-II and PP_1651 are the paired sensor/regulator in the PP_1651-PP_1652 locus."},
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "TonB-dependent ferric-siderophore receptor context",
                    "node": {
                        "id": "fepA_ferric_siderophore_receptor",
                        "label": "FepA ferric-siderophore receptor",
                        "module_type": "TRANSPORT_STEP",
                        "description": "FepA is the TonB-dependent outer-membrane receptor context for siderophore-iron uptake.",
                        "annotons": [
                            annoton("fepA", "fepA: ferric-siderophore receptor", TERMS["siderophore_iron_transporter"], [TERMS["siderophore_iron_import"], TERMS["siderophore_transmembrane_transport"]], [TERMS["outer_membrane"]], "TonB-dependent outer-membrane ferric-siderophore receptor."),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "FecI/FecR-like ECF sigma/anti-sigma iron-uptake regulation",
                    "node": {
                        "id": "fecir_like_ecf_sigma_regulation",
                        "label": "FecI/FecR-like ECF sigma regulation",
                        "module_type": "REGULATORY_STEP",
                        "description": (
                            "FecR-family transmembrane proteins and ECF sigma factors provide an "
                            "alternative envelope-to-transcription iron-uptake signaling architecture."
                        ),
                        "annotons": [
                            annoton("PP_3576", "PP_3576: FecR-like anti-sigma sensor", TERMS["sigma_antagonist"], [TERMS["negative_transcription_reg"]], [TERMS["membrane"]], "FecR-family anti-sigma/sensor protein."),
                            annoton("fecI", "fecI: ECF sigma factor", TERMS["sigma_factor"], [TERMS["transcription_initiation"], TERMS["transcription_initiation_reg"]], [TERMS["cytoplasm"]], "ECF sigma factor for condition-specific transcription initiation."),
                            annoton("PP_4607", "PP_4607: FecR-like anti-sigma sensor", TERMS["sigma_antagonist"], [TERMS["negative_transcription_reg"]], [TERMS["membrane"]], "FecR-family anti-sigma/sensor protein."),
                            annoton("PP_4611", "PP_4611: ECF sigma factor", TERMS["sigma_factor"], [TERMS["transcription_initiation"], TERMS["transcription_initiation_reg"]], [TERMS["cytoplasm"]], "ECF sigma factor for condition-specific transcription initiation."),
                            annoton("PP_4612", "PP_4612: FecR-like anti-sigma protein", TERMS["sigma_antagonist"], [TERMS["negative_transcription_reg"]], [TERMS["membrane"]], "FecR-family anti-sigma protein."),
                        ],
                        "connections": [
                            {"source": "pp_3576_fecr_like_anti_sigma_sensor", "target": "feci_ecf_sigma_factor", "connection_type": "PROVIDES_INPUT_FOR", "description": "PP_3576 is the adjacent FecR-like partner for fecI."},
                            {"source": "pp_4612_fecr_like_anti_sigma_protein", "target": "pp_4611_ecf_sigma_factor", "connection_type": "PROVIDES_INPUT_FOR", "description": "PP_4612 is the adjacent FecR-like partner for PP_4611."},
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
