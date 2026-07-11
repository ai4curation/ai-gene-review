#!/usr/bin/env python3
"""First-pass curation for the ppu02020 nutrient-homeostasis TCS bucket."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
MODULE_PATH = ROOT / "modules/inorganic_nutrient_homeostasis_regulation_boundary.yaml"
SPECIES = "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "response_regulator": {"id": "GO:0000156", "label": "phosphorelay response regulator activity"},
    "sensor_kinase": {"id": "GO:0000155", "label": "phosphorelay sensor kinase activity"},
    "phosphorelay": {"id": "GO:0000160", "label": "phosphorelay signal transduction system"},
    "histidine_kinase": {"id": "GO:0004673", "label": "protein histidine kinase activity"},
    "phosphoprotein_phosphatase": {"id": "GO:0004721", "label": "phosphoprotein phosphatase activity"},
    "cis_binding": {"id": "GO:0000976", "label": "transcription cis-regulatory region binding"},
    "dna_binding": {"id": "GO:0003677", "label": "DNA binding"},
    "transcription_reg": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "protein_dna_complex": {"id": "GO:0032993", "label": "protein-DNA complex"},
    "nitrogen_utilization": {"id": "GO:0006808", "label": "regulation of nitrogen utilization"},
    "pii_utase": {"id": "GO:0008773", "label": "[protein-PII] uridylyltransferase activity"},
    "phosphodiester_hydrolase": {"id": "GO:0008081", "label": "phosphoric diester hydrolase activity"},
    "nucleotidyltransferase": {"id": "GO:0016779", "label": "nucleotidyltransferase activity"},
    "phosphate_transport": {"id": "GO:0006817", "label": "phosphate ion transport"},
    "phosphate_transport_reg": {"id": "GO:0010966", "label": "regulation of phosphate transport"},
    "phosphate_starvation": {"id": "GO:0016036", "label": "cellular response to phosphate starvation"},
    "potassium_transport": {"id": "GO:0006813", "label": "potassium ion transport"},
    "potassium_transmembrane": {"id": "GO:0071805", "label": "potassium ion transmembrane transport"},
    "potassium_transport_reg": {"id": "GO:0043266", "label": "regulation of potassium ion transport"},
    "ptype_k_transporter": {"id": "GO:0008556", "label": "P-type potassium transmembrane transporter activity"},
    "ptype_ion_transporter": {"id": "GO:0015662", "label": "P-type ion transporter activity"},
    "transmembrane_transport": {"id": "GO:0055085", "label": "transmembrane transport"},
    "potassium_binding": {"id": "GO:0030955", "label": "potassium ion binding"},
    "atp_binding": {"id": "GO:0005524", "label": "ATP binding"},
    "nucleotide_binding": {"id": "GO:0000166", "label": "nucleotide binding"},
    "atp_hydrolysis": {"id": "GO:0016887", "label": "ATP hydrolysis activity"},
    "magnesium_binding": {"id": "GO:0000287", "label": "magnesium ion binding"},
    "cytoplasm": {"id": "GO:0005737", "label": "cytoplasm"},
    "cytosol": {"id": "GO:0005829", "label": "cytosol"},
    "plasma_membrane": {"id": "GO:0005886", "label": "plasma membrane"},
    "membrane": {"id": "GO:0016020", "label": "membrane"},
}


GENES = {
    "glnD": {
        "description": (
            "glnD encodes the bifunctional PII uridylyltransferase/uridylyl-removing enzyme in "
            "Pseudomonas putida KT2440. The protein senses nitrogen status through glutamine and "
            "controls the uridylylation state of PII proteins, thereby regulating nitrogen "
            "assimilation and metabolism."
        ),
        "uniprot": "Full=Bifunctional uridylyltransferase/uridylyl-removing enzyme",
        "uniprot_extra": "Modifies, by uridylylation and deuridylylation, the PII",
        "asta": "Protein Description:** RecName: Full=Bifunctional uridylyltransferase/uridylyl-removing enzyme",
        "term_reviews": {
            "GO:0006808": ("ACCEPT", "GlnD controls nitrogen-utilization regulation through reversible PII modification.", None),
            "GO:0008081": ("ACCEPT", "The broad phosphoric diester hydrolase term captures the deuridylyl-removing activity of the bifunctional enzyme.", None),
            "GO:0008773": ("ACCEPT", "PII uridylyltransferase activity is a core molecular function of GlnD.", None),
            "GO:0016779": ("MARK_AS_OVER_ANNOTATED", "This parent nucleotidyltransferase term is less informative than the specific PII uridylyltransferase activity.", None),
        },
        "core_functions": [
            {
                "description": "Bifunctional control of PII protein uridylylation state during nitrogen regulation.",
                "molecular_function": TERMS["pii_utase"],
                "directly_involved_in": [TERMS["nitrogen_utilization"]],
            },
            {
                "description": "Deuridylyl-removing phosphodiesterase activity toward PII-UMP under nitrogen-replete conditions.",
                "molecular_function": TERMS["phosphodiester_hydrolase"],
                "directly_involved_in": [TERMS["nitrogen_utilization"]],
            },
        ],
        "question": "Which PII proteins are the dominant GlnD substrates in KT2440 under defined nitrogen sources?",
        "experiment": "Measure GlnB/GlnK uridylylation in glnD mutant and complemented strains during nitrogen upshift and downshift.",
    },
    "glnL": {
        "description": (
            "glnL encodes NtrB, the sensory histidine kinase/phosphatase of the NtrB/NtrC "
            "two-component system in Pseudomonas putida KT2440. It autophosphorylates under "
            "nitrogen limitation, transfers phosphoryl groups to NtrC/GlnG, and can dephosphorylate "
            "NtrC when nitrogen is available."
        ),
        "uniprot": "Full=Sensory histidine kinase/phosphatase NtrB",
        "uniprot_extra": "Under conditions of nitrogen limitation, NtrB autophosphorylates",
        "asta": "Protein Description:** RecName: Full=Sensory histidine kinase/phosphatase NtrB",
        "term_reviews": {
            "GO:0000155": ("ACCEPT", "NtrB is the sensor kinase in the NtrB/NtrC phosphorelay.", None),
            "GO:0000160": ("ACCEPT", "The protein acts in the NtrB/NtrC phosphorelay signal-transduction system.", None),
            "GO:0004673": ("ACCEPT", "The histidine kinase activity is the catalytic mechanism for NtrC phosphorylation.", None),
            "GO:0005737": ("ACCEPT", "UniProt places this NtrB/NtrC sensor kinase in the cytoplasm.", None),
            "GO:0006355": ("ACCEPT", "The NtrB/NtrC system regulates nitrogen-responsive transcription through NtrC.", None),
            "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than phosphorelay signal transduction.", None),
            "GO:0016301": ("MARK_AS_OVER_ANNOTATED", "Generic kinase activity is less informative than phosphorelay sensor kinase and protein histidine kinase activity.", None),
            "GO:0016740": ("MARK_AS_OVER_ANNOTATED", "Generic transferase activity is less informative than the histidine kinase terms.", None),
            "GO:0016772": ("MARK_AS_OVER_ANNOTATED", "This broad phosphorus-transfer term is less informative than protein histidine kinase activity.", None),
        },
        "core_functions": [
            {
                "description": "NtrB sensor kinase/phosphatase control of NtrC in nitrogen-responsive phosphorelay signaling.",
                "molecular_function": TERMS["sensor_kinase"],
                "directly_involved_in": [TERMS["phosphorelay"], TERMS["nitrogen_utilization"]],
                "locations": [TERMS["cytoplasm"]],
            }
        ],
        "new_annotations": [
            {
                "term": TERMS["nitrogen_utilization"],
                "qualifier": "involved_in",
                "summary": "NtrB should be represented in regulation of nitrogen utilization through its control of NtrC.",
                "reason": "UniProt describes NtrB/NtrC as controlling expression of nitrogen-regulated genes in response to nitrogen limitation.",
            }
        ],
        "question": "How do glutamine, PII state, and nitrogen source alter the kinase/phosphatase balance of KT2440 NtrB?",
        "experiment": "Assay NtrB autophosphorylation, phosphotransfer to NtrC, and NtrC dephosphorylation using purified KT2440 proteins under varying PII and nitrogen-metabolite conditions.",
    },
    "phoB": {
        "description": (
            "phoB encodes the PhoB response regulator of the PhoR/PhoB phosphate-starvation system "
            "in Pseudomonas putida KT2440. It is a cytoplasmic OmpR/PhoB-family DNA-binding regulator "
            "that activates the phosphate regulon when phosphate is limited."
        ),
        "uniprot": "Full=Phosphate regulon transcriptional regulatory protein PhoB",
        "uniprot_extra": "positive regulator for the phosphate",
        "asta": "Protein Description:** RecName: Full=Phosphate regulon transcriptional regulatory protein PhoB",
        "term_reviews": {
            "GO:0000156": ("ACCEPT", "PhoB is the response regulator of the PhoR/PhoB phosphorelay.", None),
            "GO:0000160": ("ACCEPT", "PhoB acts in a two-component phosphorelay with PhoR.", None),
            "GO:0000976": ("ACCEPT", "PhoB is an OmpR/PhoB-family DNA-binding transcription regulator.", None),
            "GO:0003677": ("MARK_AS_OVER_ANNOTATED", "Generic DNA binding is less informative than transcription cis-regulatory region binding.", None),
            "GO:0005737": ("ACCEPT", "UniProt places PhoB in the cytoplasm.", None),
            "GO:0005829": ("KEEP_AS_NON_CORE", "Cytosol is compatible with cytoplasmic response-regulator function, but cytoplasm is retained as the core location.", None),
            "GO:0006355": ("ACCEPT", "PhoB regulates phosphate-regulon transcription.", None),
            "GO:0006817": ("MODIFY", "PhoB regulates phosphate transport genes rather than transporting phosphate itself.", [TERMS["phosphate_transport_reg"], TERMS["phosphate_starvation"]]),
            "GO:0032993": ("KEEP_AS_NON_CORE", "Protein-DNA complex membership is transient context for a DNA-bound regulator, not the core function.", None),
        },
        "core_functions": [
            {
                "description": "PhoB response-regulator activity in the phosphate-starvation phosphorelay.",
                "molecular_function": TERMS["response_regulator"],
                "directly_involved_in": [TERMS["phosphorelay"], TERMS["phosphate_starvation"]],
                "locations": [TERMS["cytoplasm"]],
            },
            {
                "description": "PhoB-dependent transcriptional regulation of the phosphate regulon.",
                "molecular_function": TERMS["cis_binding"],
                "directly_involved_in": [TERMS["transcription_reg"], TERMS["phosphate_transport_reg"]],
                "locations": [TERMS["cytoplasm"]],
            },
        ],
        "question": "Which PSEPK phosphate-import and phosphate-scavenging loci are direct PhoB targets?",
        "experiment": "Map PhoB binding sites by ChIP-seq or DNA affinity profiling during phosphate limitation and test promoter activity in phoB mutant and complemented strains.",
    },
    "phoR": {
        "description": (
            "phoR encodes the membrane-associated PhoR sensor histidine kinase of the PhoR/PhoB "
            "phosphate-starvation system in Pseudomonas putida KT2440. It phosphorylates PhoB in "
            "response to phosphate limitation and links extracellular phosphate status to phosphate-regulon expression."
        ),
        "uniprot": "Full=Phosphate regulon sensor protein PhoR",
        "uniprot_extra": "PhoR may function as a membrane-associated protein kinase",
        "asta": "Protein Description:** RecName: Full=Phosphate regulon sensor protein PhoR",
        "term_reviews": {
            "GO:0000155": ("ACCEPT", "PhoR is the sensor kinase in the PhoR/PhoB phosphorelay.", None),
            "GO:0000160": ("ACCEPT", "PhoR acts in the PhoR/PhoB phosphorelay signal-transduction system.", None),
            "GO:0004673": ("ACCEPT", "Protein histidine kinase activity is the catalytic mechanism for PhoB phosphorylation.", None),
            "GO:0004721": ("ACCEPT", "PhoR-family sensors can act as phosphatases as part of regulator reset and phosphate-response control.", None),
            "GO:0005886": ("ACCEPT", "PhoR is a membrane-associated sensor kinase.", None),
            "GO:0006355": ("ACCEPT", "PhoR controls phosphate-regulon transcription through PhoB phosphorylation.", None),
            "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than phosphorelay signal transduction.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than plasma membrane for this bacterial sensor.", None),
            "GO:0016036": ("ACCEPT", "The PhoR/PhoB system mediates cellular response to phosphate starvation.", None),
            "GO:0016301": ("MARK_AS_OVER_ANNOTATED", "Generic kinase activity is less informative than sensor histidine kinase activity.", None),
            "GO:0016740": ("MARK_AS_OVER_ANNOTATED", "Generic transferase activity is less informative than the histidine kinase terms.", None),
            "GO:0016772": ("MARK_AS_OVER_ANNOTATED", "This broad phosphorus-transfer term is less informative than protein histidine kinase activity.", None),
        },
        "core_functions": [
            {
                "description": "PhoR membrane sensor kinase control of PhoB during phosphate starvation.",
                "molecular_function": TERMS["sensor_kinase"],
                "directly_involved_in": [TERMS["phosphorelay"], TERMS["phosphate_starvation"]],
                "locations": [TERMS["plasma_membrane"]],
            },
            {
                "description": "PhoR phosphatase/reset activity in phosphate-regulon signal control.",
                "molecular_function": TERMS["phosphoprotein_phosphatase"],
                "directly_involved_in": [TERMS["phosphate_starvation"]],
                "locations": [TERMS["plasma_membrane"]],
            },
        ],
        "question": "Which phosphate-limitation inputs tune PhoR kinase versus phosphatase output in KT2440?",
        "experiment": "Measure PhoR-dependent PhoB phosphorylation and PhoB-regulated promoter output in phosphate-replete and phosphate-limited media.",
    },
    "kdpD": {
        "description": (
            "kdpD encodes the membrane sensor histidine kinase of the Kdp potassium-homeostasis system "
            "in Pseudomonas putida KT2440. Together with the already curated KdpE response regulator, it "
            "links potassium or osmotic stress signals to regulation of the adjacent Kdp potassium-transport operon."
        ),
        "uniprot": "Full=histidine kinase",
        "uniprot_extra": "SUBCELLULAR LOCATION: Membrane",
        "asta": "Protein Description:** RecName: Full=histidine kinase",
        "term_reviews": {
            "GO:0000155": ("ACCEPT", "KdpD is a KdpD-family phosphorelay sensor kinase.", None),
            "GO:0000160": ("ACCEPT", "KdpD functions in His-Asp phosphorelay signaling with KdpE.", None),
            "GO:0004673": ("ACCEPT", "Protein histidine kinase activity is the catalytic mechanism for KdpE phosphorylation.", None),
            "GO:0005737": ("KEEP_AS_NON_CORE", "KdpD has cytoplasmic domains, but the core location for the full protein is the plasma membrane.", None),
            "GO:0005886": ("ACCEPT", "KdpD is a multi-pass bacterial membrane sensor.", None),
            "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than phosphorelay signal transduction.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than plasma membrane for this sensor kinase.", None),
            "GO:0016301": ("MARK_AS_OVER_ANNOTATED", "Generic kinase activity is less informative than sensor histidine kinase activity.", None),
            "GO:0016740": ("MARK_AS_OVER_ANNOTATED", "Generic transferase activity is less informative than the histidine kinase terms.", None),
            "GO:0016772": ("MARK_AS_OVER_ANNOTATED", "This broad phosphorus-transfer term is less informative than protein histidine kinase activity.", None),
        },
        "core_functions": [
            {
                "description": "KdpD membrane sensor kinase control of the KdpE potassium-homeostasis regulator.",
                "molecular_function": TERMS["sensor_kinase"],
                "directly_involved_in": [TERMS["phosphorelay"], TERMS["potassium_transport_reg"]],
                "locations": [TERMS["plasma_membrane"]],
            }
        ],
        "new_annotations": [
            {
                "term": TERMS["potassium_transport_reg"],
                "qualifier": "involved_in",
                "summary": "KdpD should be represented as part of regulation of potassium ion transport.",
                "reason": "The KdpD sensor kinase functions with KdpE in the local kdp potassium transporter regulatory system.",
            }
        ],
        "question": "Does KT2440 KdpD respond primarily to potassium limitation, osmotic stress, or both?",
        "experiment": "Monitor KdpE-dependent kdp promoter activity in kdpD mutant and complemented strains across potassium and osmotic-stress gradients.",
    },
    "kdpC": {
        "description": (
            "kdpC encodes the KdpC accessory subunit of the high-affinity ATP-driven Kdp potassium "
            "transport system in Pseudomonas putida KT2440. Reviewed UniProt/HAMAP annotation describes "
            "KdpC as an inner-membrane catalytic chaperone that increases the ATP-binding affinity of KdpB."
        ),
        "uniprot": "Full=Potassium-transporting ATPase KdpC subunit",
        "uniprot_extra": "acts as a catalytic chaperone that increases the ATP-binding affinity",
        "asta": "Protein Description:** RecName: Full=Potassium-transporting ATPase KdpC subunit",
        "term_reviews": {
            "GO:0005524": ("MARK_AS_OVER_ANNOTATED", "KdpC increases ATP-binding affinity of KdpB, but KdpB is the ATP-hydrolyzing subunit.", None),
            "GO:0005886": ("ACCEPT", "KdpC is an inner-membrane Kdp transporter subunit.", None),
            "GO:0006813": ("ACCEPT", "KdpC participates in high-affinity potassium transport as part of the Kdp complex.", None),
            "GO:0008556": ("ACCEPT", "KdpC contributes to the P-type potassium transporter complex activity.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than plasma membrane.", None),
            "GO:0071805": ("ACCEPT", "KdpC participates in potassium transmembrane transport as part of the Kdp complex.", None),
        },
        "core_functions": [
            {
                "description": "Catalytic chaperone/accessory subunit contributing to Kdp P-type potassium transport.",
                "contributes_to_molecular_function": TERMS["ptype_k_transporter"],
                "directly_involved_in": [TERMS["potassium_transmembrane"]],
                "locations": [TERMS["plasma_membrane"]],
            }
        ],
        "question": "Is KdpC essential for KdpB activity in KT2440 under potassium limitation?",
        "experiment": "Compare potassium uptake and KdpB ATPase activity in kdpC deletion, complemented, and wild-type strains.",
    },
    "kdpB": {
        "description": (
            "kdpB encodes the ATP-binding and ATP-hydrolyzing energy-coupling subunit of the Kdp "
            "high-affinity potassium transporter in Pseudomonas putida KT2440. HAMAP annotation assigns "
            "EC 7.2.2.6 and the ATP-driven electrogenic import of potassium into the cytoplasm."
        ),
        "uniprot": "Full=Potassium-transporting ATPase ATP-binding subunit",
        "uniprot_extra": "Reaction=K(+)(out) + ATP + H2O = K(+)(in) + ADP + phosphate + H(+)",
        "asta": "Protein Description:** RecName: Full=Potassium-transporting ATPase ATP-binding subunit",
        "term_reviews": {
            "GO:0000166": ("MARK_AS_OVER_ANNOTATED", "Generic nucleotide binding is less informative than ATP binding and Kdp-specific transporter activity.", None),
            "GO:0000287": ("ACCEPT", "Magnesium binding is consistent with P-type ATPase catalytic chemistry.", None),
            "GO:0005524": ("ACCEPT", "KdpB is the ATP-binding subunit of the Kdp transporter.", None),
            "GO:0005886": ("ACCEPT", "KdpB is a multi-pass inner-membrane transporter subunit.", None),
            "GO:0006813": ("ACCEPT", "KdpB powers potassium ion import.", None),
            "GO:0008556": ("ACCEPT", "P-type potassium transmembrane transporter activity is the core molecular function of KdpB.", None),
            "GO:0015662": ("MARK_AS_OVER_ANNOTATED", "P-type ion transporter activity is less informative than the potassium-specific term.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than plasma membrane.", None),
            "GO:0016887": ("ACCEPT", "ATP hydrolysis is the energy-coupling chemistry for KdpB-mediated potassium transport.", None),
            "GO:0055085": ("MARK_AS_OVER_ANNOTATED", "Generic transmembrane transport is less informative than potassium ion transmembrane transport.", None),
            "GO:0071805": ("ACCEPT", "KdpB mediates ATP-driven potassium ion transmembrane transport.", None),
        },
        "core_functions": [
            {
                "description": "ATP-driven P-type potassium transporter activity in the Kdp complex.",
                "molecular_function": TERMS["ptype_k_transporter"],
                "directly_involved_in": [TERMS["potassium_transmembrane"]],
                "locations": [TERMS["plasma_membrane"]],
            },
            {
                "description": "ATP hydrolysis that powers Kdp potassium import.",
                "molecular_function": TERMS["atp_hydrolysis"],
                "directly_involved_in": [TERMS["potassium_transmembrane"]],
                "locations": [TERMS["plasma_membrane"]],
            },
        ],
        "question": "What potassium affinities and induction thresholds define KT2440 KdpB-dependent import?",
        "experiment": "Measure KdpB-dependent ATPase and potassium uptake activities in membrane preparations or whole cells under low-potassium conditions.",
    },
    "kdpA": {
        "description": (
            "kdpA encodes the potassium-binding and translocating membrane subunit of the Kdp high-affinity "
            "potassium transport system in Pseudomonas putida KT2440. Reviewed HAMAP annotation states that "
            "KdpA binds periplasmic potassium ions and delivers them to the KdpB membrane domain."
        ),
        "uniprot": "Full=Potassium-transporting ATPase potassium-binding subunit",
        "uniprot_extra": "binds the periplasmic potassium ions and delivers the ions",
        "asta": "Protein Description:** RecName: Full=Potassium-transporting ATPase potassium-binding subunit",
        "term_reviews": {
            "GO:0005886": ("ACCEPT", "KdpA is a multi-pass inner-membrane Kdp transporter subunit.", None),
            "GO:0006813": ("ACCEPT", "KdpA participates in Kdp-dependent potassium ion transport.", None),
            "GO:0008556": ("ACCEPT", "KdpA contributes directly to the P-type potassium transmembrane transporter activity.", None),
            "GO:0030955": ("ACCEPT", "Potassium ion binding is the specific subunit function described for KdpA.", None),
            "GO:0071805": ("ACCEPT", "KdpA participates in potassium ion transmembrane transport.", None),
        },
        "core_functions": [
            {
                "description": "Potassium-binding and translocating subunit of the Kdp transporter.",
                "molecular_function": TERMS["potassium_binding"],
                "contributes_to_molecular_function": TERMS["ptype_k_transporter"],
                "directly_involved_in": [TERMS["potassium_transmembrane"]],
                "locations": [TERMS["plasma_membrane"]],
            }
        ],
        "question": "Which residues in KT2440 KdpA determine potassium affinity and selectivity?",
        "experiment": "Mutate conserved KdpA ion-binding residues and measure potassium uptake and low-potassium growth complementation.",
    },
    "kdpF": {
        "description": (
            "kdpF encodes a very small predicted membrane subunit of the Kdp potassium transport system in "
            "Pseudomonas putida KT2440. Its KdpF/Potass_KdpF domain and local kdpDEABC locus support an "
            "accessory role in the Kdp P-type potassium transporter complex."
        ),
        "uniprot": "Full=Potassium-transporting ATPase F",
        "uniprot_extra": "InterPro; IPR011726; KdpF.",
        "asta": "Protein Description:** SubName: Full=Potassium-transporting ATPase F",
        "term_reviews": {
            "GO:0005886": ("ACCEPT", "KdpF is a predicted single-pass membrane component of the Kdp system.", None),
            "GO:0008556": ("ACCEPT", "KdpF contributes to the Kdp P-type potassium transporter complex.", None),
            "GO:0071805": ("ACCEPT", "KdpF participates in Kdp-associated potassium transmembrane transport.", None),
        },
        "core_functions": [
            {
                "description": "Small membrane accessory subunit contributing to Kdp P-type potassium transport.",
                "contributes_to_molecular_function": TERMS["ptype_k_transporter"],
                "directly_involved_in": [TERMS["potassium_transmembrane"]],
                "locations": [TERMS["plasma_membrane"]],
            }
        ],
        "question": "Is KT2440 KdpF required for stable Kdp complex assembly or maximal potassium uptake?",
        "experiment": "Compare Kdp complex abundance and potassium uptake in kdpF deletion, complemented, and wild-type strains.",
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
        review["summary"] = f"{label} is true or plausible but too broad for the curated first-pass role."
    return review


def make_new_annotation(gene: str, cfg: dict, item: dict) -> dict:
    term = item["term"]
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": uniprot_ref(gene),
        "qualifier": item["qualifier"],
        "review": {
            "summary": item["summary"],
            "action": "NEW",
            "reason": item["reason"],
            "supported_by": [
                support(uniprot_ref(gene), cfg["uniprot"]),
                support(uniprot_ref(gene), cfg["uniprot_extra"]),
                support(asta_ref(gene), cfg["asta"]),
            ],
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
        if go_id in cfg["term_reviews"]:
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
            "experiment_type": "targeted nutrient-homeostasis regulatory and transport assay",
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
        "id": "MODULE:inorganic_nutrient_homeostasis_regulation_boundary",
        "title": "Inorganic nutrient homeostasis regulation boundary",
        "description": (
            "Boundary module for the ppu02020 nutrient-homeostasis partition in Pseudomonas putida "
            "KT2440. It captures nitrogen regulation through GlnD and the NtrB/NtrC pair, "
            "phosphate starvation regulation through PhoR/PhoB, and potassium homeostasis through "
            "KdpD/KdpE and the KdpFABC transporter. This is a partition of the broad KEGG "
            "two-component-system map, not a single linear pathway."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02020",
                "title": "Two-component system - Pseudomonas putida KT2440",
                "statement": (
                    "KEGG ppu02020 supplies the umbrella two-component-system membership, but the nutrient "
                    "homeostasis genes are curated here as a smaller boundary module."
                ),
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.tsv",
                "title": "PSEPK ppu02020 partition table",
                "statement": (
                    "The partition table groups glnD, glnL/glnG, phoB/phoR, and the kdp genes into the "
                    "nitrogen, phosphate, and potassium homeostasis bucket."
                ),
            },
        ],
        "notes": (
            "The kdpE response regulator was curated earlier in the ppu02024 QseBC-like regulatory bucket; "
            "it is included here as the cognate KdpD partner for module completeness without creating a "
            "duplicate gene review."
        ),
        "module": {
            "id": "inorganic_nutrient_homeostasis_regulation_boundary",
            "label": "Inorganic nutrient homeostasis regulation boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                {"preferred_term": t["label"], "term": t}
                for t in [
                    TERMS["nitrogen_utilization"],
                    TERMS["phosphate_starvation"],
                    TERMS["phosphate_transport_reg"],
                    TERMS["potassium_transport_reg"],
                    TERMS["phosphorelay"],
                    TERMS["ptype_k_transporter"],
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
                    "role": "GlnD and NtrB/NtrC nitrogen-utilization regulation",
                    "node": {
                        "id": "nitrogen_utilization_regulation",
                        "label": "GlnD-NtrB-NtrC nitrogen-utilization regulation",
                        "module_type": "REGULATORY_STEP",
                        "description": (
                            "GlnD controls PII uridylylation state, and NtrB/NtrC converts nitrogen status "
                            "into phosphorelay-dependent transcriptional regulation."
                        ),
                        "annotons": [
                            annoton("glnD", "glnD: PII uridylyltransferase", TERMS["pii_utase"], [TERMS["nitrogen_utilization"]], [TERMS["cytoplasm"]], "Bifunctional PII uridylylation-state enzyme."),
                            annoton("glnL", "glnL/NtrB: nitrogen sensor kinase", TERMS["sensor_kinase"], [TERMS["phosphorelay"], TERMS["nitrogen_utilization"]], [TERMS["cytoplasm"]], "Sensor kinase/phosphatase for NtrC."),
                            annoton("ntrC", "ntrC/GlnG: nitrogen response regulator", TERMS["response_regulator"], [TERMS["phosphorelay"], TERMS["nitrogen_utilization"]], [TERMS["cytoplasm"]], "DNA-binding response regulator for nitrogen-responsive transcription."),
                        ],
                        "connections": [
                            {"source": "glnd_pii_uridylyltransferase", "target": "glnl_ntrb_nitrogen_sensor_kinase", "connection_type": "PROVIDES_INPUT_FOR", "description": "PII uridylylation state feeds nitrogen-regulatory signaling context."},
                            {"source": "glnl_ntrb_nitrogen_sensor_kinase", "target": "ntrc_glng_nitrogen_response_regulator", "connection_type": "PROVIDES_INPUT_FOR", "description": "NtrB phosphorylates or dephosphorylates NtrC depending on nitrogen state."},
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "PhoR/PhoB phosphate-starvation regulation",
                    "node": {
                        "id": "phosphate_starvation_regulation",
                        "label": "PhoR-PhoB phosphate-starvation regulation",
                        "module_type": "REGULATORY_STEP",
                        "description": (
                            "PhoR/PhoB regulates phosphate-regulon transcription and phosphate-transport "
                            "responses when phosphate is limited."
                        ),
                        "annotons": [
                            annoton("phoR", "phoR: phosphate sensor kinase", TERMS["sensor_kinase"], [TERMS["phosphorelay"], TERMS["phosphate_starvation"]], [TERMS["plasma_membrane"]], "Membrane sensor kinase for phosphate starvation."),
                            annoton("phoB", "phoB: phosphate response regulator", TERMS["response_regulator"], [TERMS["phosphorelay"], TERMS["phosphate_starvation"], TERMS["phosphate_transport_reg"]], [TERMS["cytoplasm"]], "DNA-binding response regulator for the phosphate regulon."),
                        ],
                        "connections": [
                            {"source": "phor_phosphate_sensor_kinase", "target": "phob_phosphate_response_regulator", "connection_type": "PROVIDES_INPUT_FOR", "description": "PhoR is the upstream sensor kinase for PhoB."},
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "KdpD/KdpE regulation and KdpFABC potassium import",
                    "node": {
                        "id": "potassium_homeostasis_kdp_system",
                        "label": "KdpD-KdpE-KdpFABC potassium homeostasis system",
                        "module_type": "TRANSPORT_STEP",
                        "description": (
                            "KdpD/KdpE regulates the Kdp high-affinity potassium transporter, whose KdpA, "
                            "KdpB, KdpC, and KdpF subunits mediate ATP-driven potassium import."
                        ),
                        "annotons": [
                            annoton("kdpD", "kdpD: Kdp sensor kinase", TERMS["sensor_kinase"], [TERMS["phosphorelay"], TERMS["potassium_transport_reg"]], [TERMS["plasma_membrane"]], "Membrane sensor kinase for KdpE and potassium-homeostasis control."),
                            annoton("kdpE", "kdpE: Kdp response regulator", TERMS["response_regulator"], [TERMS["phosphorelay"], TERMS["potassium_transport_reg"]], [TERMS["cytoplasm"]], "DNA-binding response regulator previously curated in the ppu02024 regulatory bucket."),
                            annoton("kdpA", "kdpA: potassium-binding transporter subunit", TERMS["potassium_binding"], [TERMS["potassium_transmembrane"]], [TERMS["plasma_membrane"]], "Potassium-binding and translocating subunit."),
                            annoton("kdpB", "kdpB: ATP-driven potassium transporter subunit", TERMS["ptype_k_transporter"], [TERMS["potassium_transmembrane"]], [TERMS["plasma_membrane"]], "ATP-hydrolyzing energy-coupling subunit."),
                            annoton("kdpC", "kdpC: Kdp catalytic chaperone subunit", TERMS["ptype_k_transporter"], [TERMS["potassium_transmembrane"]], [TERMS["plasma_membrane"]], "Accessory subunit that supports KdpB ATP binding."),
                            annoton("kdpF", "kdpF: small Kdp membrane subunit", TERMS["ptype_k_transporter"], [TERMS["potassium_transmembrane"]], [TERMS["plasma_membrane"]], "Small KdpF accessory membrane subunit."),
                        ],
                        "connections": [
                            {"source": "kdpd_kdp_sensor_kinase", "target": "kdpe_kdp_response_regulator", "connection_type": "PROVIDES_INPUT_FOR", "description": "KdpD is the plausible upstream phosphodonor for KdpE."},
                            {"source": "kdpe_kdp_response_regulator", "target": "kdpa_potassium_binding_transporter_subunit", "connection_type": "POSITIVELY_REGULATES", "description": "KdpE regulates the kdp transporter operon in the Kdp system model."},
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
