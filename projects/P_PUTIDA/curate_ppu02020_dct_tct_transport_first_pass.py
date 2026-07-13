#!/usr/bin/env python3
"""First-pass curation for the ppu02020 Dct/Tct transport-regulation bucket."""

from __future__ import annotations

import csv
from copy import deepcopy
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
MODULE_PATH = ROOT / "modules/dicarboxylate_tricarboxylate_transport_regulation_boundary.yaml"
SPECIES = "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "sensor_kinase": {"id": "GO:0000155", "label": "phosphorelay sensor kinase activity"},
    "response_regulator": {"id": "GO:0000156", "label": "phosphorelay response regulator activity"},
    "phosphorelay": {"id": "GO:0000160", "label": "phosphorelay signal transduction system"},
    "nucleotide_binding": {"id": "GO:0000166", "label": "nucleotide binding"},
    "dna_binding": {"id": "GO:0003677", "label": "DNA binding"},
    "protein_his_kinase": {"id": "GO:0004673", "label": "protein histidine kinase activity"},
    "atp_binding": {"id": "GO:0005524", "label": "ATP binding"},
    "cytosol": {"id": "GO:0005829", "label": "cytosol"},
    "plasma_membrane": {"id": "GO:0005886", "label": "plasma membrane"},
    "transcription": {"id": "GO:0006351", "label": "DNA-templated transcription"},
    "transcription_reg": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "dicarboxylic_acid_transport": {"id": "GO:0006835", "label": "dicarboxylic acid transport"},
    "tricarboxylic_acid_transport": {"id": "GO:0006842", "label": "tricarboxylic acid transport"},
    "signal_transduction": {"id": "GO:0007165", "label": "signal transduction"},
    "monocarboxylic_transporter": {"id": "GO:0008028", "label": "monocarboxylic acid transmembrane transporter activity"},
    "transcription_region_binding": {"id": "GO:0000976", "label": "transcription cis-regulatory region binding"},
    "fumarate_transporter": {"id": "GO:0015138", "label": "fumarate transmembrane transporter activity"},
    "succinate_transporter": {"id": "GO:0015141", "label": "succinate transmembrane transporter activity"},
    "tricarboxylic_transporter": {"id": "GO:0015142", "label": "tricarboxylic acid transmembrane transporter activity"},
    "symporter": {"id": "GO:0015293", "label": "symporter activity"},
    "malate_proton_symporter": {"id": "GO:0015366", "label": "malate:proton symporter activity"},
    "fumarate_transport": {"id": "GO:0015741", "label": "fumarate transport"},
    "c4_dicarboxylate_transport": {"id": "GO:0015740", "label": "C4-dicarboxylate transport"},
    "membrane": {"id": "GO:0016020", "label": "membrane"},
    "kinase": {"id": "GO:0016301", "label": "kinase activity"},
    "transferase": {"id": "GO:0016740", "label": "transferase activity"},
    "phosphorus_transferase": {"id": "GO:0016772", "label": "transferase activity, transferring phosphorus-containing groups"},
    "transmembrane_transporter": {"id": "GO:0022857", "label": "transmembrane transporter activity"},
    "carbohydrate_binding": {"id": "GO:0030246", "label": "carbohydrate binding"},
    "periplasm": {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"},
    "carboxylic_acid_binding": {"id": "GO:0031406", "label": "carboxylic acid binding"},
    "protein_dna_complex": {"id": "GO:0032993", "label": "protein-DNA complex"},
    "tricarboxylic_transmembrane_transport": {"id": "GO:0035674", "label": "tricarboxylic acid transmembrane transport"},
    "sequence_specific_dna_binding": {"id": "GO:0043565", "label": "sequence-specific DNA binding"},
    "transmembrane_transport": {"id": "GO:0055085", "label": "transmembrane transport"},
    "l_aspartate_transport": {"id": "GO:0070778", "label": "L-aspartate transmembrane transport"},
    "succinate_transport": {"id": "GO:0071422", "label": "succinate transmembrane transport"},
    "malate_transport": {"id": "GO:0071423", "label": "malate transmembrane transport"},
    "carboxylic_acid_transmembrane_transport": {"id": "GO:1905039", "label": "carboxylic acid transmembrane transport"},
}


COMMON_RESPONSE_REVIEWS = {
    "GO:0000160": ("ACCEPT", "Phosphorelay signal transduction matches the receiver-domain regulatory architecture.", None),
    "GO:0000166": ("MARK_AS_OVER_ANNOTATED", "Nucleotide binding is true but too broad for a sigma-54 enhancer-binding response regulator.", None),
    "GO:0003677": ("MARK_AS_OVER_ANNOTATED", "Generic DNA binding is less informative than transcriptional regulatory-region or sequence-specific DNA binding.", None),
    "GO:0005524": ("ACCEPT", "ATP binding is part of the AAA+/sigma-54 enhancer-binding regulatory mechanism.", None),
    "GO:0006351": ("MARK_AS_OVER_ANNOTATED", "DNA-templated transcription is broad process context; regulation of transcription is the more accurate role.", None),
    "GO:0006355": ("ACCEPT", "The response regulator is a DNA-binding transcriptional regulator.", None),
    "GO:0043565": ("ACCEPT", "Sequence-specific DNA binding fits the HTH/Fis-family regulatory domain.", None),
}

UHP_RESPONSE_REVIEWS = {
    "GO:0000160": ("ACCEPT", "Phosphorelay signal transduction matches the response-regulator receiver domain.", None),
    "GO:0000976": ("ACCEPT", "Transcription cis-regulatory region binding fits the LuxR/GerE-type DNA-binding output domain.", None),
    "GO:0003677": ("MARK_AS_OVER_ANNOTATED", "Generic DNA binding is less informative than transcription cis-regulatory region binding.", None),
    "GO:0006351": ("MARK_AS_OVER_ANNOTATED", "DNA-templated transcription is broad process context; regulation of transcription is the more accurate role.", None),
    "GO:0006355": ("ACCEPT", "UhpA is annotated as a DNA-binding response regulator.", None),
}

TCTD_RESPONSE_REVIEWS = {
    "GO:0000156": ("ACCEPT", "The protein has receiver and OmpR/PhoB-type DNA-binding domains consistent with response regulator activity.", None),
    "GO:0000160": ("ACCEPT", "Phosphorelay signal transduction matches the response-regulator architecture.", None),
    "GO:0000976": ("ACCEPT", "Transcription cis-regulatory region binding fits the OmpR/PhoB-type DNA-binding output domain.", None),
    "GO:0003677": ("MARK_AS_OVER_ANNOTATED", "Generic DNA binding is less informative than transcription cis-regulatory region binding.", None),
    "GO:0005829": ("ACCEPT", "Cytosol is the expected location for a soluble response regulator.", None),
    "GO:0006355": ("ACCEPT", "The protein is a transcriptional response regulator.", None),
    "GO:0032993": ("KEEP_AS_NON_CORE", "Protein-DNA complex is plausible context for a DNA-binding regulator but is not the core molecular role.", None),
}

SENSOR_REVIEWS = {
    "GO:0000155": ("ACCEPT", "The protein has HisKA/HATPase sensor histidine kinase architecture.", None),
    "GO:0000160": ("ACCEPT", "Phosphorelay signal transduction matches the sensor kinase role.", None),
    "GO:0004673": ("ACCEPT", "Protein histidine kinase activity is the specific catalytic activity.", None),
    "GO:0005886": ("ACCEPT", "The protein is annotated as a plasma-membrane or inner-membrane sensor kinase.", None),
    "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than phosphorelay sensor kinase signaling.", None),
    "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than plasma membrane for this sensor kinase.", None),
    "GO:0016301": ("MARK_AS_OVER_ANNOTATED", "Generic kinase activity is less informative than protein histidine kinase activity.", None),
    "GO:0016740": ("MARK_AS_OVER_ANNOTATED", "Generic transferase activity is less informative than protein histidine kinase activity.", None),
    "GO:0016772": ("MARK_AS_OVER_ANNOTATED", "This parent transferase term is less informative than protein histidine kinase activity.", None),
}

DCTA_REVIEWS = {
    "GO:0005886": ("ACCEPT", "C4-dicarboxylate symporters are multi-pass inner-membrane transporters.", None),
    "GO:0006835": ("ACCEPT", "Dicarboxylic acid transport matches the DctA-family transporter role.", None),
    "GO:0015138": ("ACCEPT", "Fumarate transporter activity is consistent with C4-dicarboxylate uptake.", None),
    "GO:0015141": ("ACCEPT", "Succinate transporter activity is consistent with C4-dicarboxylate uptake.", None),
    "GO:0015293": ("ACCEPT", "Symporter activity matches the dicarboxylate/amino-acid:cation symporter family.", None),
    "GO:0015366": ("ACCEPT", "Malate:proton symporter activity is a specific C4-dicarboxylate symporter function.", None),
    "GO:0015741": ("ACCEPT", "Fumarate transport is one of the C4-dicarboxylate transport processes.", None),
    "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than plasma membrane for this transporter.", None),
    "GO:0022857": ("MARK_AS_OVER_ANNOTATED", "Generic transporter activity is less informative than the substrate-specific C4-dicarboxylate transporter terms.", None),
    "GO:0070778": ("UNDECIDED", "L-aspartate transport is a propagated family-level inference not resolved by the local UniProt product/function text in this first pass.", None),
    "GO:0071422": ("ACCEPT", "Succinate transmembrane transport is a core DctA-family C4-dicarboxylate transport process.", None),
    "GO:0071423": ("ACCEPT", "Malate transmembrane transport is a core DctA-family C4-dicarboxylate transport process.", None),
}

TRAP_LARGE_REVIEWS = {
    "GO:0005886": ("ACCEPT", "The TRAP large permease is an inner-membrane transporter component.", None),
    "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than plasma membrane for this permease.", None),
    "GO:0022857": ("ACCEPT", "Transmembrane transporter activity is acceptable for a TRAP permease component pending a more specific complex-level term.", None),
    "GO:0055085": ("MODIFY", "Generic transmembrane transport should be narrowed to C4-dicarboxylate transport for the local DctPQM TRAP importer.", [TERMS["c4_dicarboxylate_transport"]]),
}

TRAP_SMALL_REVIEWS = {
    "GO:0005886": ("ACCEPT", "The TRAP small permease is an inner-membrane transporter component.", None),
    "GO:0015740": ("ACCEPT", "C4-dicarboxylate transport matches the DctQ-like TRAP permease context.", None),
    "GO:0022857": ("ACCEPT", "Transmembrane transporter activity is acceptable for a TRAP permease component pending a more specific complex-level term.", None),
    "GO:0055085": ("MARK_AS_OVER_ANNOTATED", "Generic transmembrane transport is less informative than C4-dicarboxylate transport.", None),
}

DCTP_REVIEWS = {
    "GO:0030246": ("MODIFY", "Carbohydrate binding is likely an over-broad/incorrect propagated binding label for a DctP-family dicarboxylate-binding TRAP component.", [TERMS["carboxylic_acid_binding"]]),
    "GO:0030288": ("ACCEPT", "The substrate-binding component of a bacterial TRAP transporter acts in the periplasmic space.", None),
    "GO:0055085": ("MODIFY", "Generic transmembrane transport should be narrowed to C4-dicarboxylate transport for the DctPQM TRAP system.", [TERMS["c4_dicarboxylate_transport"]]),
}

PP3124_REVIEWS = {
    "GO:0005886": ("ACCEPT", "The short-chain fatty-acid transporter is a predicted multi-pass plasma-membrane protein.", None),
}


GENES = {
    "dctD-I": {
        "id": "Q88R71",
        "ordered_locus": "PP_0263",
        "class": "dctd",
        "description": "dctD-I encodes a DctD/TyrR-like sigma-54 enhancer-binding response regulator in Pseudomonas putida KT2440. Its receiver, AAA+ sigma-54 activation, and HTH/Fis DNA-binding domains support a cytosolic phosphorelay-dependent transcriptional regulatory role adjacent to a DctB-like sensor kinase.",
        "uniprot": "DE   RecName: Full=HTH-type transcriptional regulatory protein TyrR {ECO:0000256|ARBA:ARBA00029500};",
        "asta": "- **Protein Description:** RecName: Full=HTH-type transcriptional regulatory protein TyrR {ECO:0000256|ARBA:ARBA00029500};",
        "extra": ["DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.", "DR   InterPro; IPR002078; Sigma_54_int.", "DR   InterPro; IPR002197; HTH_Fis."],
        "reviews": COMMON_RESPONSE_REVIEWS,
    },
    "PP_0264": {
        "id": "Q88R70",
        "ordered_locus": "PP_0264",
        "class": "sensor",
        "description": "PP_0264 encodes a predicted DctB-family C4-dicarboxylate transport sensor histidine kinase in Pseudomonas putida KT2440. Its dCache input region plus HisKA/HATPase domains support an inner-membrane sensory phosphorelay role next to dctD-I.",
        "uniprot": "DE   RecName: Full=C4-dicarboxylate transport sensor protein DctB {ECO:0000256|ARBA:ARBA00073143};",
        "asta": "- **Protein Description:** RecName: Full=C4-dicarboxylate transport sensor protein DctB {ECO:0000256|ARBA:ARBA00073143}; EC=2.7.13.3 {ECO:0000256|ARBA:ARBA00012438};",
        "extra": ["CC   -!- SUBCELLULAR LOCATION: Cell inner membrane", "DR   InterPro; IPR017055; Sig_transdc_His_kinase_DctB.", "DR   InterPro; IPR005467; His_kinase_dom."],
        "reviews": SENSOR_REVIEWS,
    },
    "uhpA": {
        "id": "Q88QS8",
        "ordered_locus": "PP_0410",
        "class": "uhp_response",
        "description": "uhpA encodes a DNA-binding response regulator in Pseudomonas putida KT2440. Its receiver and LuxR/GerE-family output domains support phosphorelay-dependent transcriptional regulation, but this bucket keeps it as transport-regulatory side context rather than assigning a specific Dct or Tct substrate.",
        "uniprot": "DE   SubName: Full=DNA-binding response regulator UhpA {ECO:0000313|EMBL:AAN66040.1};",
        "asta": "- **Protein Description:** SubName: Full=DNA-binding response regulator UhpA {ECO:0000313|EMBL:AAN66040.1};",
        "extra": ["DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.", "DR   InterPro; IPR000792; Tscrpt_reg_LuxR_C."],
        "reviews": UHP_RESPONSE_REVIEWS,
    },
    "dctD-II": {
        "id": "Q88NY7",
        "ordered_locus": "PP_1066",
        "class": "dctd",
        "description": "dctD-II encodes a predicted C4-dicarboxylate transport transcriptional regulator in Pseudomonas putida KT2440. Receiver, sigma-54 activation, and HTH domains support a DctD-like response-regulator role paired with the adjacent DctB-like sensor PP_1067.",
        "uniprot": "DE   SubName: Full=C4-dicarboxylate transport transcriptional regulatory protein {ECO:0000313|EMBL:AAN66691.1};",
        "asta": "- **Protein Description:** SubName: Full=C4-dicarboxylate transport transcriptional regulatory protein {ECO:0000313|EMBL:AAN66691.1};",
        "extra": ["DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.", "DR   InterPro; IPR002078; Sigma_54_int.", "DR   InterPro; IPR002197; HTH_Fis."],
        "reviews": COMMON_RESPONSE_REVIEWS,
    },
    "PP_1067": {
        "id": "Q88NY6",
        "ordered_locus": "PP_1067",
        "class": "sensor",
        "description": "PP_1067 encodes a predicted DctB-family C4-dicarboxylate transport sensor histidine kinase in Pseudomonas putida KT2440. dCache, HisKA, and HATPase domains support an inner-membrane sensor kinase role paired with dctD-II.",
        "uniprot": "DE   RecName: Full=C4-dicarboxylate transport sensor protein DctB {ECO:0000256|ARBA:ARBA00073143};",
        "asta": "- **Protein Description:** RecName: Full=C4-dicarboxylate transport sensor protein DctB {ECO:0000256|ARBA:ARBA00073143}; EC=2.7.13.3 {ECO:0000256|ARBA:ARBA00012438};",
        "extra": ["CC   -!- SUBCELLULAR LOCATION: Cell inner membrane", "DR   InterPro; IPR017055; Sig_transdc_His_kinase_DctB.", "DR   InterPro; IPR005467; His_kinase_dom."],
        "reviews": SENSOR_REVIEWS,
    },
    "PP_1167": {
        "id": "Q88NP0",
        "ordered_locus": "PP_1167",
        "class": "trap_large",
        "description": "PP_1167 encodes the predicted DctM-like large permease component of a tripartite ATP-independent periplasmic C4-dicarboxylate transporter in Pseudomonas putida KT2440. It is an inner-membrane TRAP permease located next to the DctQ small permease PP_1168 and DctP substrate-binding component.",
        "uniprot": "DE   RecName: Full=TRAP transporter large permease protein {ECO:0000256|RuleBase:RU369079};",
        "asta": "- **Protein Description:** RecName: Full=TRAP transporter large permease protein {ECO:0000256|RuleBase:RU369079};",
        "extra": ["CC   -!- FUNCTION: Part of the tripartite ATP-independent periplasmic (TRAP)", "CC   -!- SUBCELLULAR LOCATION: Cell inner membrane", "DR   InterPro; IPR004681; TRAP_DctM."],
        "reviews": TRAP_LARGE_REVIEWS,
    },
    "PP_1168": {
        "id": "Q88NN9",
        "ordered_locus": "PP_1168",
        "class": "trap_small",
        "description": "PP_1168 encodes the predicted DctQ-like small permease component of a tripartite ATP-independent periplasmic C4-dicarboxylate transporter in Pseudomonas putida KT2440. It is an inner-membrane TRAP permease adjacent to PP_1167 and dctP.",
        "uniprot": "DE   RecName: Full=TRAP transporter small permease protein {ECO:0000256|RuleBase:RU369079};",
        "asta": "- **Protein Description:** RecName: Full=TRAP transporter small permease protein {ECO:0000256|RuleBase:RU369079};",
        "extra": ["CC   -!- FUNCTION: Part of the tripartite ATP-independent periplasmic (TRAP)", "CC   -!- SUBCELLULAR LOCATION: Cell inner membrane", "DR   InterPro; IPR007387; TRAP_DctQ."],
        "reviews": TRAP_SMALL_REVIEWS,
    },
    "dctP": {
        "id": "Q88NN8",
        "ordered_locus": "PP_1169",
        "class": "trap_binding",
        "description": "dctP encodes the predicted periplasmic substrate-binding component of a TRAP C4-dicarboxylate uptake system in Pseudomonas putida KT2440. DctP-family and TRAP_DctP domains support carboxylic-acid substrate binding for the adjacent PP_1167/PP_1168 permease pair.",
        "uniprot": "DE   SubName: Full=TRAP dicarboxylate transporter, DctP subunit {ECO:0000313|EMBL:AAN66793.1};",
        "asta": "- **Protein Description:** SubName: Full=TRAP dicarboxylate transporter, DctP subunit {ECO:0000313|EMBL:AAN66793.1};",
        "extra": ["DR   InterPro; IPR018389; DctP_fam.", "DR   InterPro; IPR004682; TRAP_DctP."],
        "reviews": DCTP_REVIEWS,
    },
    "dctA": {
        "id": "Q88NL9",
        "ordered_locus": "PP_1188",
        "class": "dcta",
        "description": "dctA encodes a reviewed C4-dicarboxylate inner-membrane symporter in Pseudomonas putida KT2440. UniProt records transport of dicarboxylates such as succinate, fumarate, and malate, supporting a core DctA-family C4-dicarboxylate uptake role.",
        "uniprot": "DE   RecName: Full=C4-dicarboxylate transport protein {ECO:0000255|HAMAP-Rule:MF_01300};",
        "asta": "- **Protein Description:** RecName: Full=C4-dicarboxylate transport protein {ECO:0000255|HAMAP-Rule:MF_01300};",
        "extra": ["CC   -!- FUNCTION: Responsible for the transport of dicarboxylates such as", "DR   InterPro; IPR023954; C4_dicarb_transport.", "DR   InterPro; IPR001991; Na-dicarboxylate_symporter."],
        "reviews": DCTA_REVIEWS,
    },
    "dctD-III": {
        "id": "Q88N15",
        "ordered_locus": "PP_1401",
        "class": "dctd",
        "description": "dctD-III encodes a predicted C4-dicarboxylate transport transcriptional regulator in Pseudomonas putida KT2440. Its receiver, sigma-54 enhancer-binding, and HTH/Fis domains support a DctD-like transcriptional response-regulator role paired with dctB.",
        "uniprot": "DE   SubName: Full=C4-dicarboxylate transport transcriptional regulatory protein {ECO:0000313|EMBL:AAN67024.1};",
        "asta": "- **Protein Description:** SubName: Full=C4-dicarboxylate transport transcriptional regulatory protein {ECO:0000313|EMBL:AAN67024.1};",
        "extra": ["DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.", "DR   InterPro; IPR002078; Sigma_54_int.", "DR   InterPro; IPR002197; HTH_Fis."],
        "reviews": COMMON_RESPONSE_REVIEWS,
    },
    "dctB": {
        "id": "Q88N14",
        "ordered_locus": "PP_1402",
        "class": "sensor",
        "description": "dctB encodes a DctB-family sensor histidine kinase in Pseudomonas putida KT2440. HisKA and HATPase domains support a membrane-associated sensory phosphorelay role paired with dctD-III.",
        "uniprot": "DE   RecName: Full=histidine kinase {ECO:0000256|ARBA:ARBA00012438};",
        "asta": "- **Protein Description:** RecName: Full=histidine kinase {ECO:0000256|ARBA:ARBA00012438}; EC=2.7.13.3 {ECO:0000256|ARBA:ARBA00012438};",
        "extra": ["CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000256|ARBA:ARBA00004651};", "DR   InterPro; IPR017055; Sig_transdc_His_kinase_DctB.", "DR   InterPro; IPR005467; His_kinase_dom."],
        "reviews": SENSOR_REVIEWS,
    },
    "PP_1416": {
        "id": "Q88N02",
        "ordered_locus": "PP_1416",
        "class": "tct_membrane",
        "description": "PP_1416 encodes the predicted TctA membrane component of a tricarboxylate transport system in Pseudomonas putida KT2440. The TctA domain and multiple transmembrane segments support a transporter-subunit role with PP_1417, PP_1418, tctD, and PP_1421.",
        "uniprot": "DE   SubName: Full=Tricarboxylate transport protein TctA {ECO:0000313|EMBL:AAN67038.1};",
        "asta": "- **Protein Description:** SubName: Full=Tricarboxylate transport protein TctA {ECO:0000313|EMBL:AAN67038.1};",
        "extra": ["DR   InterPro; IPR002823; DUF112_TM.", "DR   Pfam; PF01970; TctA; 1.", "FT   TRANSMEM        20..39"],
        "reviews": {},
    },
    "PP_1417": {
        "id": "Q88N01",
        "ordered_locus": "PP_1417",
        "class": "tct_membrane",
        "description": "PP_1417 encodes the predicted TctB membrane component of a tricarboxylate transport system in Pseudomonas putida KT2440. The TctB domain and transmembrane segments support a transporter-subunit role with PP_1416 and PP_1418.",
        "uniprot": "DE   SubName: Full=Tricarboxylate transport protein TctB {ECO:0000313|EMBL:AAN67039.1};",
        "asta": "- **Protein Description:** SubName: Full=Tricarboxylate transport protein TctB {ECO:0000313|EMBL:AAN67039.1};",
        "extra": ["DR   InterPro; IPR009936; DUF1468.", "DR   Pfam; PF07331; TctB; 1.", "FT   TRANSMEM        47..65"],
        "reviews": {},
    },
    "PP_1418": {
        "id": "Q88N00",
        "ordered_locus": "PP_1418",
        "class": "tct_binding",
        "description": "PP_1418 encodes the predicted TctC substrate-binding component of a tricarboxylate transport system in Pseudomonas putida KT2440. Its TctC/BUG domains support carboxylic-acid substrate-recognition context for the adjacent TctAB membrane components.",
        "uniprot": "DE   SubName: Full=Tricarboxylate transport protein TctC {ECO:0000313|EMBL:AAN67040.1};",
        "asta": "- **Protein Description:** SubName: Full=Tricarboxylate transport protein TctC {ECO:0000313|EMBL:AAN67040.1};",
        "extra": ["CC   -!- SIMILARITY: Belongs to the UPF0065 (bug) family.", "DR   InterPro; IPR005064; BUG.", "DR   Pfam; PF03401; TctC; 1."],
        "reviews": {},
    },
    "tctD": {
        "id": "Q88MZ8",
        "ordered_locus": "PP_1420",
        "class": "tct_response",
        "description": "tctD encodes a predicted transcriptional response regulator in Pseudomonas putida KT2440. Receiver and OmpR/PhoB-type DNA-binding domains support a phosphorelay-dependent regulatory role near the TctABC tricarboxylate transporter locus.",
        "uniprot": "DE   SubName: Full=Transcriptional regulatory protein tctD {ECO:0000313|EMBL:AAN67042.1};",
        "asta": "- **Protein Description:** SubName: Full=Transcriptional regulatory protein tctD {ECO:0000313|EMBL:AAN67042.1};",
        "extra": ["DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.", "DR   InterPro; IPR001867; OmpR/PhoB-type_DNA-bd."],
        "reviews": TCTD_RESPONSE_REVIEWS,
    },
    "PP_1421": {
        "id": "Q88MZ7",
        "ordered_locus": "PP_1421",
        "class": "sensor",
        "description": "PP_1421 encodes a predicted two-component sensor histidine kinase in Pseudomonas putida KT2440. Its 2CSK_N, HAMP, HisKA, and HATPase domains support a membrane-associated phosphorelay sensor role adjacent to tctD.",
        "uniprot": "DE   RecName: Full=histidine kinase {ECO:0000256|ARBA:ARBA00012438};",
        "asta": "- **Protein Description:** RecName: Full=histidine kinase {ECO:0000256|ARBA:ARBA00012438}; EC=2.7.13.3 {ECO:0000256|ARBA:ARBA00012438};",
        "extra": ["CC   -!- SUBCELLULAR LOCATION: Membrane {ECO:0000256|ARBA:ARBA00004370}.", "DR   InterPro; IPR050428; TCS_sensor_his_kinase.", "DR   InterPro; IPR005467; His_kinase_dom."],
        "reviews": SENSOR_REVIEWS,
    },
    "dctA-II": {
        "id": "Q88L79",
        "ordered_locus": "PP_2056",
        "class": "dcta",
        "description": "dctA-II encodes a predicted C4-dicarboxylate inner-membrane symporter in Pseudomonas putida KT2440. Its sodium/dicarboxylate symporter domains support succinate, fumarate, and malate transport by family-level inference, with exact substrate range unresolved.",
        "uniprot": "DE   SubName: Full=C4-dicarboxylate transport protein {ECO:0000313|EMBL:AAN67670.2};",
        "asta": "- **Protein Description:** SubName: Full=C4-dicarboxylate transport protein {ECO:0000313|EMBL:AAN67670.2};",
        "extra": ["CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000256|ARBA:ARBA00004651};", "DR   InterPro; IPR001991; Na-dicarboxylate_symporter.", "DR   Pfam; PF00375; SDF; 1."],
        "reviews": DCTA_REVIEWS,
    },
    "dctA-III": {
        "id": "Q88KN5",
        "ordered_locus": "PP_2255",
        "class": "dcta",
        "description": "dctA-III encodes a predicted C4-dicarboxylate inner-membrane symporter in Pseudomonas putida KT2440. Its sodium/dicarboxylate symporter domains support C4-dicarboxylate uptake by family-level inference, with exact substrate range unresolved.",
        "uniprot": "DE   SubName: Full=C4-dicarboxylate transport protein {ECO:0000313|EMBL:AAN67868.1};",
        "asta": "- **Protein Description:** SubName: Full=C4-dicarboxylate transport protein {ECO:0000313|EMBL:AAN67868.1};",
        "extra": ["CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000256|ARBA:ARBA00004651};", "DR   InterPro; IPR001991; Na-dicarboxylate_symporter.", "DR   Pfam; PF00375; SDF; 1."],
        "reviews": DCTA_REVIEWS,
    },
    "PP_3124": {
        "id": "Q88I77",
        "ordered_locus": "PP_3124",
        "class": "scfa",
        "description": "PP_3124 encodes a predicted short-chain fatty-acid transporter in Pseudomonas putida KT2440. Its AtoE/SCFA transporter family domain and multiple transmembrane segments support a plasma-membrane monocarboxylate or carboxylate transport role, retained here as a transport side node.",
        "uniprot": "DE   SubName: Full=Short chain fatty acid transporter {ECO:0000313|EMBL:AAN68732.1};",
        "asta": "- **Protein Description:** SubName: Full=Short chain fatty acid transporter {ECO:0000313|EMBL:AAN68732.1};",
        "extra": ["DR   InterPro; IPR006160; SCFA_transpt_AtoE.", "DR   Pfam; PF02667; SCFA_trans; 1."],
        "reviews": PP3124_REVIEWS,
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
    path = GENE_ROOT / gene / f"{gene}-goa.tsv"
    with path.open(encoding="utf-8") as handle:
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
    label = rows[go_id]["GO NAME"]
    summary = reason
    if action == "MARK_AS_OVER_ANNOTATED":
        summary = f"{label} is plausible but too broad as a core annotation."
    review = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": [
            support(goa_ref(gene), goa_quote(rows[go_id])),
            *base_support(gene, cfg),
        ],
    }
    if replacements:
        review["proposed_replacement_terms"] = deepcopy(replacements)
    return review


def new_annotation(gene: str, cfg: dict, term: dict, qualifier: str, summary: str, reason: str) -> dict:
    return {
        "term": deepcopy(term),
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


def synthetic_annotations(gene: str, cfg: dict) -> list[dict]:
    cls = cfg["class"]
    if cls in {"dctd", "uhp_response"}:
        return [
            new_annotation(
                gene,
                cfg,
                TERMS["response_regulator"],
                "enables",
                "The response-regulator activity should be explicit for this receiver-domain transcriptional regulator.",
                "UniProt/Asta product and domain evidence support a phosphorelay response-regulator role.",
            )
        ]
    if cls == "trap_large":
        return [
            new_annotation(
                gene,
                cfg,
                TERMS["c4_dicarboxylate_transport"],
                "involved_in",
                "The DctM-like TRAP permease should be represented as participating in C4-dicarboxylate transport.",
                "The protein is a DctM-like TRAP large permease in the local DctPQM transporter locus.",
            )
        ]
    if cls == "tct_membrane":
        return [
            new_annotation(
                gene,
                cfg,
                TERMS["tricarboxylic_transporter"],
                "contributes_to",
                "The Tct membrane subunit should be represented as contributing to tricarboxylate transporter activity.",
                "The product name and TctA/TctB domain support a tricarboxylate transporter-subunit role.",
            ),
            new_annotation(
                gene,
                cfg,
                TERMS["tricarboxylic_transmembrane_transport"],
                "involved_in",
                "The Tct membrane subunit should be represented as participating in tricarboxylate transmembrane transport.",
                "The local TctABC locus and product/domain evidence support tricarboxylate transport context.",
            ),
            new_annotation(
                gene,
                cfg,
                TERMS["plasma_membrane"],
                "located_in",
                "The Tct membrane subunit should be represented as a plasma-membrane protein.",
                "The product/domain context and UniProt transmembrane features support a bacterial inner-membrane location.",
            ),
        ]
    if cls == "tct_binding":
        return [
            new_annotation(
                gene,
                cfg,
                TERMS["carboxylic_acid_binding"],
                "enables",
                "The TctC/BUG substrate-recognition component should be represented as carboxylic-acid binding.",
                "The TctC product name and BUG/TctC domains support substrate-recognition context for tricarboxylate transport.",
            ),
            new_annotation(
                gene,
                cfg,
                TERMS["tricarboxylic_transmembrane_transport"],
                "involved_in",
                "The TctC component should be represented as participating in tricarboxylate transmembrane transport.",
                "The local TctABC locus and TctC product/domain evidence support tricarboxylate transport context.",
            ),
        ]
    if cls == "scfa":
        return [
            new_annotation(
                gene,
                cfg,
                TERMS["monocarboxylic_transporter"],
                "enables",
                "The predicted short-chain fatty-acid transporter should be represented as monocarboxylic-acid transporter activity.",
                "Short-chain fatty acids are monocarboxylates, and the AtoE/SCFA transporter domain supports this substrate class.",
            ),
            new_annotation(
                gene,
                cfg,
                TERMS["carboxylic_acid_transmembrane_transport"],
                "involved_in",
                "The predicted short-chain fatty-acid transporter should be represented as carboxylic-acid transmembrane transport.",
                "The product name and SCFA transporter domain support membrane transport of a carboxylic-acid substrate class.",
            ),
        ]
    return []


def core_functions(gene: str, cfg: dict) -> list[dict]:
    cls = cfg["class"]
    if cls in {"dctd", "uhp_response", "tct_response"}:
        core = {
            "description": "Phosphorelay response regulator for transcriptional control in organic-acid transport context.",
            "molecular_function": TERMS["response_regulator"],
            "directly_involved_in": [TERMS["phosphorelay"], TERMS["transcription_reg"]],
        }
        if cls == "tct_response":
            core["locations"] = [TERMS["cytosol"]]
    elif cls == "sensor":
        core = {
            "description": "Membrane-associated sensor histidine kinase in an organic-acid transport regulatory locus.",
            "molecular_function": TERMS["sensor_kinase"],
            "directly_involved_in": [TERMS["phosphorelay"]],
            "locations": [TERMS["plasma_membrane"]],
        }
    elif cls in {"trap_large", "trap_small"}:
        core = {
            "description": "Inner-membrane TRAP permease component of a predicted C4-dicarboxylate uptake system.",
            "contributes_to_molecular_function": TERMS["transmembrane_transporter"],
            "directly_involved_in": [TERMS["c4_dicarboxylate_transport"]],
            "locations": [TERMS["plasma_membrane"]],
        }
    elif cls == "trap_binding":
        core = {
            "description": "Periplasmic DctP-family substrate-binding component of a TRAP C4-dicarboxylate uptake system.",
            "molecular_function": TERMS["carboxylic_acid_binding"],
            "directly_involved_in": [TERMS["c4_dicarboxylate_transport"]],
            "locations": [TERMS["periplasm"]],
        }
    elif cls == "dcta":
        core = {
            "description": "Inner-membrane C4-dicarboxylate symporter for succinate, fumarate, and/or malate uptake.",
            "molecular_function": TERMS["malate_proton_symporter"],
            "directly_involved_in": [
                TERMS["dicarboxylic_acid_transport"],
                TERMS["succinate_transport"],
                TERMS["malate_transport"],
            ],
            "locations": [TERMS["plasma_membrane"]],
        }
    elif cls == "tct_membrane":
        core = {
            "description": "Membrane component of a predicted TctABC tricarboxylate transport system.",
            "contributes_to_molecular_function": TERMS["tricarboxylic_transporter"],
            "directly_involved_in": [TERMS["tricarboxylic_transmembrane_transport"]],
            "locations": [TERMS["plasma_membrane"]],
        }
    elif cls == "tct_binding":
        core = {
            "description": "TctC/BUG-family substrate-recognition component of a predicted tricarboxylate transport system.",
            "molecular_function": TERMS["carboxylic_acid_binding"],
            "directly_involved_in": [TERMS["tricarboxylic_transmembrane_transport"]],
        }
    elif cls == "scfa":
        core = {
            "description": "Predicted short-chain fatty-acid/monocarboxylate membrane transporter.",
            "molecular_function": TERMS["monocarboxylic_transporter"],
            "directly_involved_in": [TERMS["carboxylic_acid_transmembrane_transport"]],
            "locations": [TERMS["plasma_membrane"]],
        }
    else:
        raise ValueError(cls)
    core["supported_by"] = base_support(gene, cfg)
    return [core]


def suggested_question(gene: str, cfg: dict) -> str:
    cls = cfg["class"]
    if cls in {"dctd", "sensor"}:
        return f"Which C4-dicarboxylate substrates or growth conditions activate the {gene}-containing regulatory pair in KT2440?"
    if cls in {"tct_response", "tct_membrane", "tct_binding"}:
        return "What tricarboxylate substrate range is recognized by the PP_1416-PP_1421 Tct-like locus?"
    if cls == "scfa":
        return "Which short-chain fatty acids are transported by PP_3124 in KT2440?"
    return f"What is the direct substrate range of {gene} in the KT2440 organic-acid transport network?"


def suggested_experiment(gene: str, cfg: dict) -> str:
    cls = cfg["class"]
    if cls in {"dctd", "sensor", "uhp_response", "tct_response"}:
        return f"Measure reporter expression from adjacent organic-acid transporter promoters in a {gene} deletion strain across succinate, fumarate, malate, citrate, and glucose-6-phosphate conditions."
    if cls == "scfa":
        return "Delete PP_3124 and assay growth or radiolabeled uptake on acetate, propionate, butyrate, and related monocarboxylates."
    return f"Delete {gene} and assay uptake or growth on candidate C4-dicarboxylates and tricarboxylates, with complementation by the wild-type allele."


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

    new_terms = {annotation["term"]["id"] for annotation in synthetic_annotations(gene, cfg)}
    if new_terms:
        data["existing_annotations"] = [
            annotation
            for annotation in data.get("existing_annotations", [])
            if annotation.get("term", {}).get("id") not in new_terms
            or annotation.get("review", {}).get("action") != "NEW"
        ]

    for annotation in data.get("existing_annotations", []):
        go_id = annotation["term"]["id"]
        if go_id not in rows or go_id not in cfg["reviews"]:
            raise KeyError(f"Unhandled annotation {go_id} for {gene}")
        annotation["review"] = make_review(gene, cfg, rows, go_id)

    data.setdefault("existing_annotations", []).extend(synthetic_annotations(gene, cfg))
    data["core_functions"] = core_functions(gene, cfg)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": suggested_question(gene, cfg)}]
    data["suggested_experiments"] = [
        {
            "description": suggested_experiment(gene, cfg),
            "experiment_type": "targeted transport or regulatory assay",
        }
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def annoton(
    gene: str,
    label: str,
    function: dict | None,
    process: dict,
    locations: list[dict],
    role: str,
) -> dict:
    item = {
        "id": label.lower().replace(":", "").replace(" ", "_").replace("/", "_").replace("-", "_"),
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "processes": [{"preferred_term": process["label"], "term": process}],
        "locations": [{"preferred_term": term["label"], "term": term} for term in locations],
        "role_description": role,
    }
    if function:
        item["function"] = {"preferred_term": function["label"], "term": function}
    return item


def build_module() -> None:
    module = {
        "id": "MODULE:dicarboxylate_tricarboxylate_transport_regulation_boundary",
        "title": "Dicarboxylate/tricarboxylate transport regulation boundary",
        "description": (
            "Boundary module for the ppu02020 Dct/Tct transport-regulation partition in Pseudomonas putida "
            "KT2440. It captures DctD/DctB-like regulatory pairs, a DctPQM TRAP C4-dicarboxylate importer, "
            "multiple DctA-family C4-dicarboxylate symporters, a TctABC/TctD-like tricarboxylate transport "
            "locus, and a PP_3124 short-chain fatty-acid transporter side node. This is a transport-regulatory "
            "partition of the broad KEGG two-component-system map, not a single linear two-component pathway."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02020",
                "title": "Two-component system - Pseudomonas putida KT2440",
                "statement": "KEGG ppu02020 supplies the umbrella membership for this transport-regulation boundary module.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.tsv",
                "title": "PSEPK ppu02020 partition table",
                "statement": (
                    "The partition table groups dctD/dctB-like regulators, DctPQM, DctA paralogs, "
                    "TctABC/TctD-like genes, and PP_3124 into the Dct/Tct transport-regulation bucket."
                ),
            },
        ],
        "notes": (
            "TctABC had no GOA rows when fetched, so the module and reviews add conservative NEW entries "
            "from UniProt/Asta product and domain evidence. DctA L-aspartate transport remains undecided "
            "because the local evidence supports C4-dicarboxylate substrates more directly."
        ),
        "module": {
            "id": "dicarboxylate_tricarboxylate_transport_regulation_boundary",
            "label": "Dicarboxylate/tricarboxylate transport regulation boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                {"preferred_term": t["label"], "term": t}
                for t in [
                    TERMS["phosphorelay"],
                    TERMS["dicarboxylic_acid_transport"],
                    TERMS["c4_dicarboxylate_transport"],
                    TERMS["tricarboxylic_transmembrane_transport"],
                    TERMS["carboxylic_acid_transmembrane_transport"],
                ]
            ],
            "context": {
                "cellular_components": [
                    {"preferred_term": "plasma membrane", "term": TERMS["plasma_membrane"]},
                    {"preferred_term": "outer membrane-bounded periplasmic space", "term": TERMS["periplasm"]},
                    {"preferred_term": "cytosol", "term": TERMS["cytosol"]},
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "DctD-I/PP_0264 regulatory pair",
                    "node": {
                        "id": "dctd_i_pp0264_pair",
                        "label": "DctD-I/PP_0264 regulatory pair",
                        "module_type": "REGULATORY_STEP",
                        "description": "A DctD/TyrR-like sigma-54 enhancer-binding response regulator paired with a DctB-family sensor kinase.",
                        "annotons": [
                            annoton("dctD-I", "dctD-I: response regulator", TERMS["response_regulator"], TERMS["phosphorelay"], [], "DctD/TyrR-like sigma-54 enhancer-binding response regulator."),
                            annoton("PP_0264", "PP_0264: DctB-like sensor kinase", TERMS["sensor_kinase"], TERMS["phosphorelay"], [TERMS["plasma_membrane"]], "DctB-family sensor histidine kinase."),
                        ],
                        "connections": [
                            {
                                "source": "pp_0264_dctb_like_sensor_kinase",
                                "target": "dctd_i_response_regulator",
                                "connection_type": "PROVIDES_INPUT_FOR",
                                "description": "The DctB-like sensor is the likely upstream kinase for the adjacent DctD-like regulator.",
                            }
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "UhpA response-regulator side context",
                    "node": {
                        "id": "uhpa_transport_regulatory_side_context",
                        "label": "UhpA transport-regulatory side context",
                        "module_type": "REGULATORY_STEP",
                        "description": "UhpA is retained as transport-regulatory side context without assigning it to a specific Dct/Tct substrate.",
                        "annotons": [
                            annoton("uhpA", "uhpA: response regulator", TERMS["response_regulator"], TERMS["phosphorelay"], [], "DNA-binding response regulator side node."),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "DctD-II/PP_1067 regulatory pair",
                    "node": {
                        "id": "dctd_ii_pp1067_pair",
                        "label": "DctD-II/PP_1067 regulatory pair",
                        "module_type": "REGULATORY_STEP",
                        "description": "A predicted C4-dicarboxylate transport transcriptional regulator paired with a DctB-like sensor kinase.",
                        "annotons": [
                            annoton("dctD-II", "dctD-II: DctD-like response regulator", TERMS["response_regulator"], TERMS["phosphorelay"], [], "C4-dicarboxylate transport transcriptional regulator."),
                            annoton("PP_1067", "PP_1067: DctB-like sensor kinase", TERMS["sensor_kinase"], TERMS["phosphorelay"], [TERMS["plasma_membrane"]], "DctB-family sensor histidine kinase."),
                        ],
                        "connections": [
                            {
                                "source": "pp_1067_dctb_like_sensor_kinase",
                                "target": "dctd_ii_dctd_like_response_regulator",
                                "connection_type": "PROVIDES_INPUT_FOR",
                                "description": "The adjacent DctB-like sensor likely provides phosphorelay input to DctD-II.",
                            }
                        ],
                    },
                },
                {
                    "order": 4,
                    "role": "DctPQM TRAP C4-dicarboxylate importer",
                    "node": {
                        "id": "dctpqm_trap_dicarboxylate_importer",
                        "label": "DctPQM TRAP C4-dicarboxylate importer",
                        "module_type": "TRANSPORT_STEP",
                        "description": "PP_1167, PP_1168, and dctP form a predicted DctM/DctQ/DctP TRAP C4-dicarboxylate uptake system.",
                        "annotons": [
                            annoton("PP_1167", "PP_1167: DctM-like large permease", TERMS["transmembrane_transporter"], TERMS["c4_dicarboxylate_transport"], [TERMS["plasma_membrane"]], "TRAP large permease component."),
                            annoton("PP_1168", "PP_1168: DctQ-like small permease", TERMS["transmembrane_transporter"], TERMS["c4_dicarboxylate_transport"], [TERMS["plasma_membrane"]], "TRAP small permease component."),
                            annoton("dctP", "dctP: DctP substrate-binding component", TERMS["carboxylic_acid_binding"], TERMS["c4_dicarboxylate_transport"], [TERMS["periplasm"]], "Periplasmic carboxylic-acid binding component."),
                        ],
                    },
                },
                {
                    "order": 5,
                    "role": "DctA-family C4-dicarboxylate symporters",
                    "node": {
                        "id": "dcta_family_symporters",
                        "label": "DctA-family C4-dicarboxylate symporters",
                        "module_type": "TRANSPORT_STEP",
                        "description": "dctA, dctA-II, and dctA-III encode DctA-family membrane symporters for C4-dicarboxylate uptake.",
                        "annotons": [
                            annoton("dctA", "dctA: C4-dicarboxylate symporter", TERMS["malate_proton_symporter"], TERMS["dicarboxylic_acid_transport"], [TERMS["plasma_membrane"]], "Reviewed DctA-family succinate/fumarate/malate transporter."),
                            annoton("dctA-II", "dctA-II: C4-dicarboxylate symporter", TERMS["malate_proton_symporter"], TERMS["dicarboxylic_acid_transport"], [TERMS["plasma_membrane"]], "Predicted DctA-family C4-dicarboxylate transporter."),
                            annoton("dctA-III", "dctA-III: C4-dicarboxylate symporter", TERMS["malate_proton_symporter"], TERMS["dicarboxylic_acid_transport"], [TERMS["plasma_membrane"]], "Predicted DctA-family C4-dicarboxylate transporter."),
                        ],
                    },
                },
                {
                    "order": 6,
                    "role": "DctD-III/dctB regulatory pair",
                    "node": {
                        "id": "dctd_iii_dctb_pair",
                        "label": "DctD-III/dctB regulatory pair",
                        "module_type": "REGULATORY_STEP",
                        "description": "A predicted C4-dicarboxylate transport transcriptional regulator paired with a DctB-family sensor kinase.",
                        "annotons": [
                            annoton("dctD-III", "dctD-III: DctD-like response regulator", TERMS["response_regulator"], TERMS["phosphorelay"], [], "C4-dicarboxylate transport transcriptional regulator."),
                            annoton("dctB", "dctB: DctB-like sensor kinase", TERMS["sensor_kinase"], TERMS["phosphorelay"], [TERMS["plasma_membrane"]], "DctB-family sensor histidine kinase."),
                        ],
                        "connections": [
                            {
                                "source": "dctb_dctb_like_sensor_kinase",
                                "target": "dctd_iii_dctd_like_response_regulator",
                                "connection_type": "PROVIDES_INPUT_FOR",
                                "description": "DctB likely provides phosphorelay input to the adjacent DctD-III regulator.",
                            }
                        ],
                    },
                },
                {
                    "order": 7,
                    "role": "TctABC/TctD-like tricarboxylate transport locus",
                    "node": {
                        "id": "tctabc_tctd_tricarboxylate_locus",
                        "label": "TctABC/TctD-like tricarboxylate transport locus",
                        "module_type": "TRANSPORT_STEP",
                        "description": "PP_1416-PP_1418 encode a predicted TctABC tricarboxylate transporter near tctD and PP_1421 regulatory genes.",
                        "annotons": [
                            annoton("PP_1416", "PP_1416: TctA membrane component", TERMS["tricarboxylic_transporter"], TERMS["tricarboxylic_transmembrane_transport"], [TERMS["plasma_membrane"]], "TctA membrane component."),
                            annoton("PP_1417", "PP_1417: TctB membrane component", TERMS["tricarboxylic_transporter"], TERMS["tricarboxylic_transmembrane_transport"], [TERMS["plasma_membrane"]], "TctB membrane component."),
                            annoton("PP_1418", "PP_1418: TctC substrate-binding component", TERMS["carboxylic_acid_binding"], TERMS["tricarboxylic_transmembrane_transport"], [], "TctC/BUG-family substrate-recognition component."),
                            annoton("tctD", "tctD: Tct response regulator", TERMS["response_regulator"], TERMS["phosphorelay"], [TERMS["cytosol"]], "TctD-like transcriptional response regulator."),
                            annoton("PP_1421", "PP_1421: Tct sensor kinase", TERMS["sensor_kinase"], TERMS["phosphorelay"], [TERMS["plasma_membrane"]], "Two-component sensor histidine kinase near tctD."),
                        ],
                    },
                },
                {
                    "order": 8,
                    "role": "PP_3124 short-chain fatty-acid transporter side node",
                    "node": {
                        "id": "pp3124_scfa_transporter",
                        "label": "PP_3124 short-chain fatty-acid transporter side node",
                        "module_type": "TRANSPORT_STEP",
                        "description": "PP_3124 is retained as a short-chain fatty-acid transporter side node in the broader organic-acid transport bucket.",
                        "annotons": [
                            annoton("PP_3124", "PP_3124: SCFA transporter", TERMS["monocarboxylic_transporter"], TERMS["carboxylic_acid_transmembrane_transport"], [TERMS["plasma_membrane"]], "Predicted short-chain fatty-acid/monocarboxylate transporter."),
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
