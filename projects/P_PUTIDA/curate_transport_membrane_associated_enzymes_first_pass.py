#!/usr/bin/env python3
"""First-pass curation for transport-bucket membrane-associated enzyme side nodes."""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = (
    ROOT
    / "projects/P_PUTIDA/batches/"
    "module_transport_membrane_efflux_membrane_associated_enzymes_and_side_nodes.tsv"
)
MODULE_PATH = ROOT / "modules/transport_membrane_enzyme_spillover_boundary.yaml"

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000003": "Gene Ontology annotation based on Enzyme Commission mapping",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000108": "Automatic transfer of experimentally verified manual GO annotation data to orthologs using Ensembl Compara",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0000155": "phosphorelay sensor kinase activity",
    "GO:0000160": "phosphorelay signal transduction system",
    "GO:0000271": "polysaccharide biosynthetic process",
    "GO:0004252": "serine-type endopeptidase activity",
    "GO:0004364": "glutathione transferase activity",
    "GO:0004519": "endonuclease activity",
    "GO:0004671": "protein C-terminal S-isoprenylcysteine carboxyl O-methyltransferase activity",
    "GO:0004673": "protein histidine kinase activity",
    "GO:0004674": "protein serine/threonine kinase activity",
    "GO:0004722": "protein serine/threonine phosphatase activity",
    "GO:0004842": "ubiquitin-protein transferase activity",
    "GO:0005524": "ATP binding",
    "GO:0005576": "extracellular region",
    "GO:0005737": "cytoplasm",
    "GO:0005886": "plasma membrane",
    "GO:0006508": "proteolysis",
    "GO:0006629": "lipid metabolic process",
    "GO:0007165": "signal transduction",
    "GO:0008233": "peptidase activity",
    "GO:0008955": "peptidoglycan glycosyltransferase activity",
    "GO:0009252": "peptidoglycan biosynthetic process",
    "GO:0009927": "histidine phosphotransfer kinase activity",
    "GO:0010468": "regulation of gene expression",
    "GO:0016020": "membrane",
    "GO:0016301": "kinase activity",
    "GO:0016491": "oxidoreductase activity",
    "GO:0016567": "protein ubiquitination",
    "GO:0016717": "oxidoreductase activity, acting on paired donors, with oxidation of a pair of donors resulting in the reduction of molecular oxygen to two molecules of water",
    "GO:0016740": "transferase activity",
    "GO:0016746": "acyltransferase activity",
    "GO:0016747": "acyltransferase activity, transferring groups other than amino-acyl groups",
    "GO:0016757": "glycosyltransferase activity",
    "GO:0016772": "transferase activity, transferring phosphorus-containing groups",
    "GO:0016783": "sulfurtransferase activity",
    "GO:0016787": "hydrolase activity",
    "GO:0016791": "phosphatase activity",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0030163": "protein catabolic process",
    "GO:0030288": "outer membrane-bounded periplasmic space",
    "GO:0046872": "metal ion binding",
    "GO:0050479": "glyceryl-ether monooxygenase activity",
    "GO:0055085": "transmembrane transport",
    "GO:0061630": "ubiquitin protein ligase activity",
    "GO:0070573": "metallodipeptidase activity",
}

PROFILE: dict[str, dict[str, Any]] = {
    "nfeD": {
        "class": "peptidase",
        "group": "Membrane peptidase and protease side nodes",
        "primary": "GO:0008233",
        "processes": ["GO:0006508"],
        "locations": ["GO:0016020"],
        "description": "nfeD encodes an NfeD-family membrane-associated peptidase/protease-domain protein, curated conservatively as a broad membrane peptidase side node.",
        "needles": ["Membrane bound peptidase", "Membrane_assoc_protease", "NfeD-like_C", "KW   Membrane"],
    },
    "desA": {
        "class": "desaturase",
        "group": "Membrane lipid oxidoreductase and hydroxylase side nodes",
        "primary": "GO:0016717",
        "processes": ["GO:0006629"],
        "locations": ["GO:0016020"],
        "description": "desA encodes a membrane delta-9 fatty acid desaturase-family protein associated with lipid metabolism.",
        "needles": ["Delta-9 fatty acid desaturase", "fatty acid desaturase type 2", "FA_desaturase", "KW   Lipid metabolism"],
    },
    "PP_0332": {
        "class": "acyltransferase",
        "group": "Membrane acyltransferase and lipid-transfer side nodes",
        "primary": "GO:0016746",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_0332 encodes a membrane glycerol/phospholipid acyltransferase-family protein with unresolved substrate specificity.",
        "needles": ["Acyltransferase", "Plipid/glycerol_acylTrfase", "Acyltransferase (PF01553)", "KW   Acyltransferase"],
    },
    "PP_0923": {
        "class": "acyltransferase",
        "group": "Membrane acyltransferase and lipid-transfer side nodes",
        "primary": "GO:0016746",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_0923 encodes a membrane glycerol/phospholipid acyltransferase-family protein with lipid-metabolism context but unresolved substrate specificity.",
        "needles": ["Acyltransferase", "Plipid/glycerol_acylTrfase", "Acyltransferase (PF01553)", "KW   Lipid metabolism"],
    },
    "PP_1033": {
        "class": "hydrolase",
        "group": "Sulfatase and broad hydrolase side nodes",
        "primary": "GO:0016787",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_1033 encodes a membrane sulfatase-domain hydrolase candidate; substrate and pathway are unresolved in this first pass.",
        "needles": ["Sulfatase domain protein", "Sulfatase_N", "Sulfatase (PF00884)", "KW   Membrane"],
    },
    "PP_1058": {
        "class": "peptidoglycan_gtase",
        "group": "Peptidoglycan and cell-envelope glycosyltransferase side nodes",
        "primary": "GO:0008955",
        "processes": ["GO:0009252"],
        "locations": ["GO:0030288"],
        "description": "PP_1058 encodes a bifunctional-looking peptidoglycan glycosyltransferase/transpeptidase-family protein, supporting peptidoglycan biosynthesis context rather than transport.",
        "needles": ["peptidoglycan glycosyltransferase", "Glyco_trans_51", "PBP_transglycosylase", "Beta-lactam/transpept-like"],
    },
    "degS": {
        "class": "serine_endopeptidase",
        "group": "Membrane peptidase and protease side nodes",
        "primary": "GO:0004252",
        "processes": ["GO:0006508"],
        "locations": ["GO:0016020"],
        "description": "degS encodes a membrane quality-control DegS-family serine endoprotease involved in proteolysis.",
        "needles": ["Quality control serine endoprotease DegS", "peptidase S1C", "Peptidase_S1C", "PDZ"],
    },
    "PP_1368": {
        "class": "glycosyltransferase",
        "group": "Peptidoglycan and cell-envelope glycosyltransferase side nodes",
        "primary": "GO:0016757",
        "processes": [],
        "locations": ["GO:0005886"],
        "description": "PP_1368 encodes a membrane glycosyltransferase-domain protein in an L-PG synthase/AglD-like family, with substrate unresolved.",
        "needles": ["glycosyltransferase domain", "L-PG_synthase/AglD", "LPG_synthase_TM", "KW   Cell membrane"],
    },
    "PP_1415": {
        "class": "regulatory_side_node",
        "group": "Regulatory and low-information membrane side nodes",
        "primary": None,
        "processes": ["GO:0010468"],
        "locations": ["GO:0016020"],
        "description": "PP_1415 encodes an AbrB-family membrane-associated regulatory protein rather than a resolved membrane enzyme.",
        "needles": ["Membrane associated enzyme subunit", "AbrB_dup", "AbrB_fam", "AbrB (PF05145)"],
    },
    "PP_1695": {
        "class": "histidine_kinase",
        "group": "Membrane kinase and phosphatase signaling side nodes",
        "primary": "GO:0000155",
        "processes": ["GO:0000160", "GO:0007165"],
        "locations": ["GO:0005886"],
        "description": "PP_1695 encodes a membrane histidine-sensor kinase with receiver and HATPase domains; transporter rows are treated as over-propagated sensor-transporter-family context.",
        "needles": ["histidine kinase", "His_kinase_dom", "HATPase_dom", "sodium:solute symporter"],
    },
    "PP_1781": {
        "class": "o_acyltransferase",
        "group": "Membrane acyltransferase and lipid-transfer side nodes",
        "primary": "GO:0016747",
        "processes": ["GO:0000271"],
        "locations": ["GO:0016020"],
        "description": "PP_1781 encodes a membrane O-acyltransferase-family protein, likely acting in a cell-envelope polysaccharide or lipid acylation context.",
        "needles": ["O-acyltransferase", "Acyl_transf_3_dom", "Acyltransferase_3", "Acyl_transf_3 (PF01757)"],
    },
    "PP_1908": {
        "class": "peptidase",
        "group": "Membrane peptidase and protease side nodes",
        "primary": "GO:0008233",
        "processes": ["GO:0006508"],
        "locations": ["GO:0016020"],
        "description": "PP_1908 encodes a membrane peptidase S49-family protein, curated as a broad peptidase/proteolysis side node.",
        "needles": ["Peptidase", "peptidase S49", "Peptidase_S49", "CLP_protease"],
    },
    "PP_2014": {
        "class": "serine_endopeptidase",
        "group": "Membrane peptidase and protease side nodes",
        "primary": "GO:0004252",
        "processes": ["GO:0006508"],
        "locations": ["GO:0016020"],
        "description": "PP_2014 encodes a rhomboid-family intramembrane serine protease candidate.",
        "needles": ["Rhomboid family intramembrane serine protease", "peptidase S54", "Rhomboid_protease_S54", "Peptidase_S54_rhomboid_dom"],
    },
    "PP_2091": {
        "class": "ser_thr_kinase",
        "group": "Membrane kinase and phosphatase signaling side nodes",
        "primary": "GO:0004674",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_2091 encodes a membrane serine/threonine-protein kinase with kinase and PPM-like phosphatase domain signatures.",
        "needles": ["Serine/threonine-protein kinase", "Prot_kinase_dom", "Pkinase (PF00069)", "PPM-type_phosphatase-like_dom"],
    },
    "PP_2377": {
        "class": "o_acyltransferase",
        "group": "Membrane acyltransferase and lipid-transfer side nodes",
        "primary": "GO:0016747",
        "processes": ["GO:0000271"],
        "locations": ["GO:0016020"],
        "description": "PP_2377 encodes a membrane acetyltransferase/O-acyltransferase-family protein, likely acting in cell-envelope polysaccharide or lipid acylation context.",
        "needles": ["Acetyltransferase Act", "Acyl_transf_3_dom", "Acyltransferase_3", "Acyl_transf_3 (PF01757)"],
    },
    "PP_2394": {
        "class": "e3_ligase",
        "group": "Secreted or toxin-associated transferase/nuclease side nodes",
        "primary": "GO:0061630",
        "processes": ["GO:0016567"],
        "locations": [],
        "description": "PP_2394 encodes a bacterial LRR/NEL/RING-like E3 ubiquitin ligase candidate, retained as a virulence/toxin-associated transferase side node rather than transport context.",
        "needles": ["RING-type E3 ubiquitin transferase", "LRR-containing bacterial E3 ligase", "NEL_dom", "ToxA_N"],
    },
    "PP_2401": {
        "class": "oxidoreductase",
        "group": "Membrane lipid oxidoreductase and hydroxylase side nodes",
        "primary": "GO:0016491",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_2401 encodes a membrane ferric-reductase-domain oxidoreductase candidate with unresolved physiological electron donor and acceptor.",
        "needles": ["Ferric oxidoreductase domain-containing protein", "Fe3_Rdtase_TM_dom", "Ferric_reduct", "KW   Membrane"],
    },
    "PP_2419": {
        "class": "acyltransferase",
        "group": "Membrane acyltransferase and lipid-transfer side nodes",
        "primary": "GO:0016746",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_2419 encodes a membrane HGSNAT-like N-acetyltransferase-domain protein with unresolved bacterial substrate.",
        "needles": ["Heparan-alpha-glucosaminide N-acetyltransferase", "HGSNAT_cat", "HGSNAT_cat (PF07786)", "KW   Membrane"],
    },
    "PP_2654": {
        "class": "glutathione_transferase",
        "group": "Membrane detoxification and sulfur-transfer side nodes",
        "primary": "GO:0004364",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_2654 encodes a MAPEG/microsomal glutathione S-transferase-family membrane protein.",
        "needles": ["Microsomal glutathione S-transferase", "MAPEG-like_dom_sf", "Membr-assoc_MAPEG", "MGST1-like"],
    },
    "PP_2852": {
        "class": "hydrolase",
        "group": "Sulfatase and broad hydrolase side nodes",
        "primary": "GO:0016787",
        "processes": [],
        "locations": ["GO:0005886"],
        "description": "PP_2852 encodes a membrane sulfatase_N/OpgB-LTA-synthase-like hydrolase-domain protein with unresolved substrate.",
        "needles": ["Sulfatase domain protein", "OpgB/LTA_synthase_biosynth", "Sulfatase_N", "Sulfatase (PF00884)"],
    },
    "PP_3108": {
        "class": "nuclease_toxin",
        "group": "Secreted or toxin-associated transferase/nuclease side nodes",
        "primary": "GO:0004519",
        "processes": [],
        "locations": [],
        "description": "PP_3108 encodes an Rhs/PAAR-associated colicin-pyocin nuclease-family protein, curated as a toxin-associated endonuclease side node.",
        "needles": ["Rhs-related protein", "colicin/pyosin nuclease", "Colicin/pyocin_DNase", "PAAR_motif"],
    },
    "PP_3169": {
        "class": "low_info_membrane",
        "group": "Regulatory and low-information membrane side nodes",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_3169 encodes a membrane YdjM-like protein with conflicting hydrolase and transcription-regulator signals, left unresolved in this first pass.",
        "needles": ["Hydrolase", "Transcription_regulator", "YdjM-like", "YdjM (PF04307)"],
    },
    "PP_3453": {
        "class": "histidine_kinase",
        "group": "Membrane kinase and phosphatase signaling side nodes",
        "primary": "GO:0000155",
        "processes": ["GO:0000160", "GO:0007165"],
        "locations": ["GO:0005886"],
        "description": "PP_3453 encodes a membrane two-component histidine-sensor kinase with HAMP/HATPase/HisKA domains.",
        "needles": ["histidine kinase", "2C_sensor_his_kinase", "HAMP_dom", "His_kinase_dom"],
    },
    "PP_3797": {
        "class": "peptidase",
        "group": "Membrane peptidase and protease side nodes",
        "primary": "GO:0008233",
        "processes": ["GO:0006508"],
        "locations": ["GO:0016020"],
        "description": "PP_3797 encodes a PepSY-associated membrane peptidase-domain protein with unresolved catalytic class.",
        "needles": ["Peptidase", "PepSY-ass_TM", "PepSY_TM", "KW   Membrane"],
    },
    "sohB": {
        "class": "serine_endopeptidase",
        "group": "Membrane peptidase and protease side nodes",
        "primary": "GO:0004252",
        "processes": ["GO:0006508"],
        "locations": ["GO:0005886"],
        "description": "sohB encodes an inner-membrane S49-family serine peptidase associated with proteolysis.",
        "needles": ["Inner membrane peptidase", "peptidase S49", "Peptidase_S49", "Peptidase_S49_N_proteobac"],
    },
    "PP_3972": {
        "class": "oxidoreductase",
        "group": "Membrane lipid oxidoreductase and hydroxylase side nodes",
        "primary": "GO:0016491",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_3972 encodes a membrane short-chain dehydrogenase/reductase-family oxidoreductase candidate with unresolved substrate.",
        "needles": ["short chain dehydrogenase/reductase", "short-chain dehydrogenases/reductases", "SDR_fam", "adh_short"],
    },
    "PP_4118": {
        "class": "hydrolase",
        "group": "Sulfatase and broad hydrolase side nodes",
        "primary": "GO:0016787",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_4118 encodes a TMEM86/YhhN-family membrane hydrolase-domain protein with unresolved substrate.",
        "needles": ["Membrane protein", "TMEM86 family", "TMEM86B-like", "YhhN"],
    },
    "PP_4168": {
        "class": "hydrolase",
        "group": "Sulfatase and broad hydrolase side nodes",
        "primary": "GO:0016787",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_4168 encodes a membrane protein annotated as a lipase, but the first pass leaves substrate specificity unresolved.",
        "needles": ["Lipase", "DUF4389", "PF14333", "KW   Membrane"],
    },
    "pvdM": {
        "class": "metallodipeptidase",
        "group": "Membrane peptidase and protease side nodes",
        "primary": "GO:0070573",
        "processes": ["GO:0006508"],
        "locations": ["GO:0016020"],
        "description": "pvdM encodes a membrane M19-family metallodipeptidase associated with proteolysis and likely pyoverdine-pathway maturation context.",
        "needles": ["Dipeptidase", "Metal_Hydrolase", "Pept_M19", "Peptidase_M19"],
    },
    "PP_4560": {
        "class": "low_info_membrane",
        "group": "Regulatory and low-information membrane side nodes",
        "primary": None,
        "processes": [],
        "locations": ["GO:0005886"],
        "description": "PP_4560 encodes a BrkB-family inner-membrane protein with a ribonuclease BN product name but no RNase-domain support in this first pass.",
        "needles": ["Ribonuclease BN", "Virul_fac_BrkB", "BrkB", "KW   Cell membrane"],
    },
    "PP_4610": {
        "class": "peptidase",
        "group": "Membrane peptidase and protease side nodes",
        "primary": "GO:0008233",
        "processes": ["GO:0006508"],
        "locations": ["GO:0016020"],
        "description": "PP_4610 encodes a PepSY-associated membrane peptidase-domain protein with unresolved catalytic class.",
        "needles": ["Peptidase", "PepSY-ass_TM", "PepSY_TM", "KW   Membrane"],
    },
    "PP_4631": {
        "class": "oxidoreductase",
        "group": "Membrane lipid oxidoreductase and hydroxylase side nodes",
        "primary": "GO:0016491",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_4631 encodes an antibiotic-biosynthesis-monooxygenase-like membrane oxidoreductase candidate with unresolved substrate.",
        "needles": ["Antibiotic biosynthesis monooxygenase", "ABM_predict", "Dimeric_a/b-barrel", "Y2318_C"],
    },
    "hflC": {
        "class": "hflk_hflc",
        "group": "FtsH protease modulator and band-7 membrane side nodes",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "hflC encodes a band-7/SPFH-family membrane protein that modulates Hfl/FtsH protease-complex context rather than acting as a catalytic hydrolase.",
        "needles": ["Protein HflC", "HflC subfamily", "Band_7", "Stomatin_HflK_fam"],
    },
    "hflK": {
        "class": "hflk_hflc",
        "group": "FtsH protease modulator and band-7 membrane side nodes",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "hflK encodes a band-7/SPFH-family membrane protein that modulates Hfl/FtsH protease-complex context rather than acting as a catalytic hydrolase.",
        "needles": ["Protein HflK", "HflK subfamily", "Band7/mec-2_domain", "Membrane_HflK_N"],
    },
    "PP_4939": {
        "class": "glycosyltransferase",
        "group": "Peptidoglycan and cell-envelope glycosyltransferase side nodes",
        "primary": "GO:0016757",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_4939 encodes a GT2/nucleotide-diphosphosugar transferase-family membrane glycosyltransferase candidate with unresolved acceptor substrate.",
        "needles": ["Glycosyltransferase family 2", "Nucleotide-diphossugar_trans", "KW   Membrane"],
    },
    "PP_5055": {
        "class": "sulfurtransferase",
        "group": "Membrane detoxification and sulfur-transfer side nodes",
        "primary": "GO:0016783",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_5055 encodes a membrane rhodanese-like sulfurtransferase-domain protein with unresolved sulfur-acceptor substrate.",
        "needles": ["Sulfurtransferase", "GlpE_sulfurtransferase", "Rhodanese-like_dom", "Rhodanese (PF00581)"],
    },
    "PP_5219": {
        "class": "fatty_acid_hydroxylase",
        "group": "Membrane lipid oxidoreductase and hydroxylase side nodes",
        "primary": "GO:0016491",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_5219 encodes a membrane fatty-acid-hydroxylase/sterol-desaturase-like oxidoreductase candidate; glyceryl-ether monooxygenase specificity is not established.",
        "needles": ["Fatty acid hydroxylase", "Fatty_acid_hydroxylase", "FA_hydroxylase", "Sterol_desaturase/TMEM195"],
    },
    "PP_5254": {
        "class": "oxidoreductase",
        "group": "Membrane lipid oxidoreductase and hydroxylase side nodes",
        "primary": "GO:0016491",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_5254 encodes an antibiotic-biosynthesis-monooxygenase-like membrane oxidoreductase candidate with unresolved substrate.",
        "needles": ["Antibiotic biosynthesis monooxygenase", "Y2318_C", "KW   Membrane"],
    },
    "PP_5293": {
        "class": "low_info_membrane",
        "group": "Regulatory and low-information membrane side nodes",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_5293 encodes a MamF/MmsF-family membrane protein with an automated orotate phosphoribosyltransferase product name but no supporting catalytic-domain evidence.",
        "needles": ["Orotate phosphoribosyltransferase", "MamF_MmsF", "KW   Membrane"],
    },
    "PP_5389": {
        "class": "methyltransferase",
        "group": "Membrane acyltransferase and lipid-transfer side nodes",
        "primary": "GO:0004671",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_5389 encodes an ICMT-family isoprenylcysteine carboxyl methyltransferase membrane protein.",
        "needles": ["Isoprenylcysteine carboxyl methyltransferase", "ICMT_MeTrfase", "ICMT (PF04140)", "KW   Membrane"],
    },
    "PP_5433": {
        "class": "low_info_membrane",
        "group": "Regulatory and low-information membrane side nodes",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_5433 encodes a low-information NADH:ubiquinone oxidoreductase subunit-2-like membrane protein without domain or GOA support for a resolved activity in this first pass.",
        "needles": ["NADH:ubiquinone oxidoreductase subunit 2", "KW   Membrane", "FT   TRANSMEM"],
    },
    "PP_5712": {
        "class": "phosphatase",
        "group": "Membrane kinase and phosphatase signaling side nodes",
        "primary": "GO:0016791",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_5712 encodes a membrane histidine-phosphatase-superfamily protein with unresolved substrate.",
        "needles": ["Histidine phosphatase family protein", "His_Pase_superF_clade-1", "His_PPase_superfam", "KW   Membrane"],
    },
}


class GeneInfo(dict[str, Any]):
    gene: str


def term(go_id: str) -> dict[str, str]:
    return {"id": go_id, "label": TERMS[go_id]}


def descriptor(go_id: str, description: str | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {"preferred_term": TERMS[go_id], "term": term(go_id)}
    if description:
        item["description"] = description
    return item


def ref_file(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def dedupe(items: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    out: list[dict[str, str]] = []
    for item in items:
        key = (item["reference_id"], item["supporting_text"])
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def first_line(lines: list[str], needle: str, optional: bool = False) -> str | None:
    for line in lines:
        if needle in line:
            return line
    if optional:
        return None
    raise ValueError(f"Could not find {needle!r}")


def first_de_line(lines: list[str]) -> str:
    for line in lines:
        if line.startswith("DE   RecName") or line.startswith("DE   SubName"):
            return line
    for line in lines:
        if line.startswith("DE   "):
            return line
    raise ValueError("No UniProt DE line found")


def load_rows() -> list[dict[str, str]]:
    with BATCH_PATH.open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_info(row: dict[str, str]) -> GeneInfo:
    gene = row["gene"]
    uniprot_lines = (GENE_ROOT / gene / f"{gene}-uniprot.txt").read_text(encoding="utf-8").splitlines()
    asta_lines = (GENE_ROOT / gene / f"{gene}-deep-research-asta.md").read_text(encoding="utf-8").splitlines()
    review_doc = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text(encoding="utf-8"))
    info = GeneInfo(
        gene=gene,
        accession=row["uniprot_accession"],
        product=row["protein_name"],
        profile=PROFILE[gene],
        uniprot_lines=uniprot_lines,
        asta_lines=asta_lines,
        existing_refs={ref["id"]: ref for ref in review_doc.get("references", []) if "id" in ref},
    )
    info["de"] = first_de_line(uniprot_lines)
    info["asta_product"] = first_line(asta_lines, "- **Protein Description:**")
    info["asta_domains"] = first_line(asta_lines, "- **Key Domains:**")
    info["location"] = first_line(uniprot_lines, "SUBCELLULAR LOCATION", optional=True)
    return info


def base_support(info: GeneInfo) -> list[dict[str, str]]:
    gene = info["gene"]
    out = [
        support(ref_file(gene, "uniprot.txt"), info["de"]),
        support(ref_file(gene, "deep-research-asta.md"), info["asta_product"]),
        support(ref_file(gene, "deep-research-asta.md"), info["asta_domains"]),
    ]
    if info.get("location"):
        out.append(support(ref_file(gene, "uniprot.txt"), info["location"]))
    for needle in info["profile"].get("needles", []):
        line = first_line(info["uniprot_lines"], needle, optional=True)
        if line:
            out.append(support(ref_file(gene, "uniprot.txt"), line))
    return dedupe(out)


def goa_support(info: GeneInfo, go_id: str, label: str) -> dict[str, str]:
    return support(ref_file(info["gene"], "goa.tsv"), f"{go_id}\t{label}")


def review(
    info: GeneInfo,
    summary: str,
    action: str,
    reason: str,
    replacement_ids: list[str] | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": base_support(info),
    }
    if replacement_ids:
        item["proposed_replacement_terms"] = [term(go_id) for go_id in replacement_ids]
    return item


def location_review(info: GeneInfo, go_id: str) -> dict[str, Any]:
    if go_id == "GO:0005886":
        return review(info, "Plasma-membrane localization is appropriate for this bacterial membrane enzyme or side-node protein.", "ACCEPT", "UniProt/GOA membrane and transmembrane evidence supports bacterial plasma-membrane context.")
    if go_id == "GO:0016020":
        if "GO:0005886" in info.get("go_ids", []):
            return review(info, "Generic membrane localization is true but less informative than plasma membrane.", "MARK_AS_OVER_ANNOTATED", "A more specific plasma-membrane annotation is present.")
        return review(info, "Membrane localization is appropriate for this membrane-associated enzyme or side-node protein.", "ACCEPT", "UniProt membrane/transmembrane evidence supports membrane localization.")
    if go_id == "GO:0030288":
        return review(info, "Outer membrane-bounded periplasmic-space localization is appropriate context for this peptidoglycan enzyme.", "ACCEPT", "Peptidoglycan polymerization occurs in the bacterial envelope/periplasmic space.")
    if go_id in {"GO:0005576", "GO:0005737"}:
        return review(info, f"{TERMS[go_id]} is retained as secondary localization context for this predicted secreted/toxin-associated protein.", "KEEP_AS_NON_CORE", "The core review focuses on the transferase/nuclease activity; localization is less certain in this first pass.")
    raise ValueError(f"Unhandled location term {go_id}")


def existing_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    go_id = ann["term"]["id"]
    label = ann["term"]["label"]
    cls = info["profile"]["class"]
    primary = info["profile"].get("primary")

    if go_id in {"GO:0005886", "GO:0016020", "GO:0030288", "GO:0005576", "GO:0005737"}:
        return location_review(info, go_id)
    if go_id in {"GO:0005524", "GO:0046872"}:
        return review(info, f"{label} is retained as non-core cofactor or catalytic-domain context.", "KEEP_AS_NON_CORE", "The enzyme activity captures the core molecular role more directly than ligand or metal binding alone.")
    if go_id in {"GO:0016301", "GO:0016740", "GO:0016772"}:
        if primary:
            return review(info, f"{label} is true but less informative than the resolved enzyme-family term.", "MARK_AS_OVER_ANNOTATED", f"{TERMS[primary]} is the more specific molecular-function call for this protein.", [primary])
        return review(info, f"{label} is broad enzyme-domain context.", "KEEP_AS_NON_CORE", "The first pass does not resolve a sharper substrate-specific activity.")

    if cls in {"peptidase", "serine_endopeptidase", "metallodipeptidase"}:
        if go_id == "GO:0008233":
            if primary == "GO:0004252":
                return review(info, "Broad peptidase activity is true but less specific than serine-type endopeptidase activity.", "MARK_AS_OVER_ANNOTATED", "The serine endopeptidase term better captures the supported catalytic class.", ["GO:0004252"])
            if primary == "GO:0070573":
                return review(info, "Broad peptidase activity is true but less specific than metallodipeptidase activity.", "MARK_AS_OVER_ANNOTATED", "The M19-family metallodipeptidase term better captures the supported catalytic class.", ["GO:0070573"])
            return review(info, "Peptidase activity is appropriate for this membrane peptidase-family protein.", "ACCEPT", "Product and domain evidence support a protease role while substrate and catalytic class remain unresolved.")
        if go_id == "GO:0004252":
            return review(info, "Serine-type endopeptidase activity is appropriate for this DegS/SohB/rhomboid protease-family protein.", "ACCEPT", "Product/family evidence supports serine endopeptidase or intramembrane serine protease activity.")
        if go_id == "GO:0070573":
            return review(info, "Metallodipeptidase activity is appropriate for this PvdM/M19-family dipeptidase.", "ACCEPT", "Product/domain evidence supports metallodipeptidase activity.")
        if go_id == "GO:0006508":
            return review(info, "Proteolysis is appropriate process context for this protease or peptidase.", "ACCEPT", "The supported peptidase activity implies proteolysis.")

    if cls in {"desaturase", "oxidoreductase", "fatty_acid_hydroxylase"}:
        if go_id == "GO:0016717":
            return review(info, "This oxidoreductase term is appropriate for the fatty-acid desaturase-family assignment.", "ACCEPT", "The product and fatty-acid desaturase domains support membrane lipid desaturation/oxidoreductase chemistry.")
        if go_id == "GO:0016491":
            return review(info, "Generic oxidoreductase activity is appropriate first-pass context for this membrane oxidoreductase candidate.", "ACCEPT", "Product/domain evidence supports oxidoreductase chemistry but not a resolved substrate.")
        if go_id == "GO:0050479":
            return review(info, "Glyceryl-ether monooxygenase activity is too specific for this fatty-acid-hydroxylase-domain protein.", "MODIFY", "The product and domain evidence support broader membrane oxidoreductase/hydroxylase context, not a specific glyceryl-ether substrate.", ["GO:0016491"])
        if go_id == "GO:0006629":
            return review(info, "Lipid metabolic process is appropriate context for the membrane fatty-acid desaturase.", "ACCEPT", "Fatty-acid desaturase activity contributes to lipid metabolism.")

    if cls in {"acyltransferase", "o_acyltransferase", "methyltransferase", "glutathione_transferase", "e3_ligase", "sulfurtransferase"}:
        if go_id == "GO:0016746":
            return review(info, "Acyltransferase activity is appropriate for this membrane acyltransferase-family protein.", "ACCEPT", "Product/domain evidence supports acyltransferase context while substrate specificity remains unresolved.")
        if go_id == "GO:0016747":
            return review(info, "O-acyltransferase activity is appropriate for this membrane acyltransferase-3 family protein.", "ACCEPT", "Product/domain evidence supports O-acyltransferase/acyltransferase-3 context.")
        if go_id == "GO:0000271":
            return review(info, "Polysaccharide biosynthetic process is retained as likely cell-envelope acylation context.", "KEEP_AS_NON_CORE", "The acyltransferase activity is the direct molecular role; the exact polysaccharide substrate remains unresolved.")
        if go_id == "GO:0004364":
            return review(info, "Glutathione transferase activity is appropriate for this MAPEG/MGST-family membrane protein.", "ACCEPT", "Product, EC, and MAPEG-family evidence support glutathione transferase activity.")
        if go_id in {"GO:0004842", "GO:0061630"}:
            return review(info, f"{label} is appropriate for this bacterial LRR/NEL/RING-like E3 ligase candidate.", "ACCEPT", "Product, EC, and family/domain evidence support ubiquitin-ligase transferase activity.")
        if go_id == "GO:0016567":
            return review(info, "Protein ubiquitination is appropriate process context for the E3 ubiquitin ligase candidate.", "ACCEPT", "The transferase activity supports protein ubiquitination context.")
        if go_id == "GO:0004671":
            return review(info, "Isoprenylcysteine carboxyl methyltransferase activity is appropriate for this ICMT-family membrane protein.", "ACCEPT", "Product and ICMT-domain evidence support the methyltransferase assignment.")

    if cls in {"glycosyltransferase", "peptidoglycan_gtase"}:
        if go_id == "GO:0008955":
            return review(info, "Peptidoglycan glycosyltransferase activity is appropriate for this PBP/transglycosylase-family protein.", "ACCEPT", "Product, EC, and glycosyltransferase-domain evidence support peptidoglycan polymerization.")
        if go_id == "GO:0009252":
            return review(info, "Peptidoglycan biosynthetic process is appropriate process context for the peptidoglycan glycosyltransferase.", "ACCEPT", "The enzyme activity contributes directly to peptidoglycan biosynthesis.")

    if cls == "histidine_kinase":
        if go_id in {"GO:0000155", "GO:0004673"}:
            return review(info, f"{label} is appropriate for this membrane two-component histidine kinase.", "ACCEPT", "HATPase/HisKA and receiver-domain evidence supports histidine kinase activity.")
        if go_id == "GO:0009927":
            return review(info, "Histidine phosphotransfer kinase activity is retained as related phosphorelay context.", "KEEP_AS_NON_CORE", "The sensor kinase and phosphorelay annotations capture the core signaling role more directly.")
        if go_id in {"GO:0000160", "GO:0007165"}:
            return review(info, f"{label} is appropriate process context for this two-component sensor kinase.", "ACCEPT", "The histidine-kinase/receiver architecture supports phosphorelay signal transduction.")
        if go_id in {"GO:0022857", "GO:0055085"}:
            return review(info, f"{label} appears over-propagated from membrane transporter-like family context.", "MARK_AS_OVER_ANNOTATED", "The supported core role is sensor histidine kinase/phosphorelay signaling; no substrate-specific transporter role is established.", ["GO:0000155"])

    if cls == "ser_thr_kinase":
        if go_id in {"GO:0004674", "GO:0004722"}:
            return review(info, f"{label} is consistent with the kinase/PPM-like domain architecture.", "ACCEPT", "The protein carries protein kinase and PPM-like phosphatase domain evidence.")

    if cls == "nuclease_toxin" and go_id == "GO:0004519":
        return review(info, "Endonuclease activity is appropriate for this Rhs/colicin-pyocin nuclease-family protein.", "ACCEPT", "Product/family/domain evidence supports toxin-associated nuclease context.")
    if cls == "regulatory_side_node" and go_id == "GO:0010468":
        return review(info, "Regulation of gene expression is appropriate for this AbrB-domain regulatory side node.", "ACCEPT", "AbrB-family domains support gene-expression regulatory context.")
    if cls == "hydrolase" and go_id == "GO:0016787":
        return review(info, "Broad hydrolase activity is acceptable first-pass context for this membrane hydrolase-domain protein.", "ACCEPT", "Product/domain evidence supports hydrolase-family context, but substrate specificity is unresolved.")

    raise ValueError(f"No review rule for {info['gene']} {go_id} {label}")


def new_annotation(info: GeneInfo, go_id: str, qualifier: str, summary: str, reason: str) -> dict[str, Any]:
    gene = info["gene"]
    return {
        "term": term(go_id),
        "evidence_type": "IEA",
        "original_reference_id": ref_file(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": base_support(info),
        },
    }


def suggested_new_annotations(info: GeneInfo) -> list[dict[str, Any]]:
    go_ids = set(info["go_ids"])
    out: list[dict[str, Any]] = []
    primary = info["profile"].get("primary")
    if primary and primary not in go_ids:
        out.append(new_annotation(info, primary, "enables", f"Adds {TERMS[primary]} for this membrane enzyme side node.", "UniProt product/domain evidence and Asta retrieval context support this conservative first-pass assignment."))
    for process in info["profile"].get("processes", []):
        if process not in go_ids:
            out.append(new_annotation(info, process, "involved_in", f"Adds {TERMS[process]} process context.", "The supported product, family, or domain context implies this conservative process annotation."))
    for location in info["profile"].get("locations", []):
        if location not in go_ids:
            out.append(new_annotation(info, location, "located_in", f"Adds {TERMS[location]} localization context.", "UniProt membrane, compartment, or transmembrane evidence supports this localization."))
    return out


def references(info: GeneInfo) -> list[dict[str, Any]]:
    refs: dict[str, dict[str, Any]] = {}
    for ref_id, ref in info["existing_refs"].items():
        refs[ref_id] = ref
    for ref_id, title in GO_REF_TITLES.items():
        if ref_id in refs:
            refs[ref_id]["title"] = title
    gene = info["gene"]
    refs[ref_file(gene, "goa.tsv")] = {"id": ref_file(gene, "goa.tsv"), "title": f"QuickGO GOA annotations for {gene}", "findings": []}
    refs[ref_file(gene, "uniprot.txt")] = {
        "id": ref_file(gene, "uniprot.txt"),
        "title": f"UniProtKB entry for {gene} ({info['accession']})",
        "findings": [{"supporting_text": info["de"]}],
    }
    refs[ref_file(gene, "deep-research-asta.md")] = {
        "id": ref_file(gene, "deep-research-asta.md"),
        "title": f"Asta retrieval report for {gene} ({info['accession']})",
        "findings": [{"supporting_text": info["asta_product"]}, {"supporting_text": info["asta_domains"]}],
    }
    return list(refs.values())


def core_function(info: GeneInfo) -> dict[str, Any]:
    profile = info["profile"]
    core: dict[str, Any] = {"description": profile["description"], "supported_by": base_support(info)}
    if profile.get("primary"):
        core["molecular_function"] = term(profile["primary"])
    if profile.get("processes"):
        core["directly_involved_in"] = [term(go_id) for go_id in profile["processes"]]
    if profile.get("locations"):
        core["locations"] = [term(go_id) for go_id in profile["locations"]]
    return core


def curate_gene(row: dict[str, str]) -> GeneInfo:
    info = load_info(row)
    gene = info["gene"]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    goa_annotations = [
        ann
        for ann in doc.get("existing_annotations", [])
        if not (ann.get("original_reference_id") == ref_file(gene, "uniprot.txt") and (ann.get("review") or {}).get("action") == "NEW")
    ]
    info["go_ids"] = [ann["term"]["id"] for ann in goa_annotations]
    for ann in goa_annotations:
        ann["review"] = existing_review(info, ann)
        ann["review"]["supported_by"].insert(0, goa_support(info, ann["term"]["id"], ann["term"]["label"]))
        ann["review"]["supported_by"] = dedupe(ann["review"]["supported_by"])
    doc["existing_annotations"] = goa_annotations + suggested_new_annotations(info)
    doc["description"] = info["profile"]["description"]
    doc["status"] = "COMPLETE"
    doc["references"] = references(info)
    reflected_ids = {ann["term"]["id"] for ann in doc["existing_annotations"] if (ann.get("review") or {}).get("action") in {"ACCEPT", "NEW"}}
    core = core_function(info)
    if "molecular_function" in core and core["molecular_function"]["id"] not in reflected_ids:
        core.pop("molecular_function")
    for slot in ("directly_involved_in", "locations"):
        if slot in core:
            core[slot] = [item for item in core[slot] if item["id"] in reflected_ids]
            if not core[slot]:
                core.pop(slot)
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {"question": "What is the direct substrate, envelope pathway partner, and physiological condition for this KT2440 membrane-associated enzyme or side-node protein?"}
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Test targeted mutants and purified or membrane-enriched proteins for enzyme activity, substrate specificity, membrane/envelope localization, and condition-specific envelope, lipid, stress, or regulatory phenotypes as appropriate.",
            "experiment_type": "membrane enzyme biochemistry and condition-specific genetics",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    safe_gene = re.sub(r"[^A-Za-z0-9_]+", "_", gene)
    annoton: dict[str, Any] = {
        "id": f"{safe_gene}_membrane_enzyme_side_context",
        "label": f"{gene}: {info['product']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": f"{gene}: {info['product']}",
    }
    primary = info["profile"].get("primary")
    if primary:
        annoton["function"] = descriptor(primary)
    if info["profile"].get("processes"):
        annoton["processes"] = [descriptor(go_id) for go_id in info["profile"]["processes"]]
    if info["profile"].get("locations"):
        annoton["locations"] = [descriptor(go_id) for go_id in info["profile"]["locations"]]
    return annoton


def node_id(group: str) -> str:
    return group.lower().replace("/", "_").replace(" ", "_").replace("-", "_")


def concept_ids_from_module(doc: dict[str, Any]) -> set[str]:
    return {
        concept.get("term", {}).get("id")
        for concept in doc.get("module", {}).get("concepts", [])
        if concept.get("term", {}).get("id")
    }


def remove_current_annotons(doc: dict[str, Any], genes: set[str]) -> None:
    for part in doc.get("module", {}).get("parts", []):
        node = part.get("node", {})
        node["annotons"] = [
            annoton
            for annoton in node.get("annotons", [])
            if annoton.get("participant", {}).get("gene", {}).get("preferred_term") not in genes
        ]


def normalize_term_labels(value: Any) -> None:
    if isinstance(value, dict):
        term_id = value.get("id")
        if term_id in TERMS and "label" in value:
            value["label"] = TERMS[term_id]
        nested_term = value.get("term")
        if isinstance(nested_term, dict):
            nested_id = nested_term.get("id")
            if nested_id in TERMS:
                nested_term["label"] = TERMS[nested_id]
                if "preferred_term" in value:
                    value["preferred_term"] = TERMS[nested_id]
        for child in value.values():
            normalize_term_labels(child)
    elif isinstance(value, list):
        for item in value:
            normalize_term_labels(item)


def build_module(infos: list[GeneInfo]) -> None:
    doc = yaml.safe_load(MODULE_PATH.read_text(encoding="utf-8"))
    genes = {info["gene"] for info in infos}
    remove_current_annotons(doc, genes)
    parts = doc.setdefault("module", {}).setdefault("parts", [])
    group_to_part = {part.get("role", ""): part for part in parts}
    next_order = max((part.get("order", 0) for part in parts), default=0) + 1
    grouped: dict[str, list[GeneInfo]] = defaultdict(list)
    for info in infos:
        grouped[info["profile"]["group"]].append(info)
    for group, group_infos in grouped.items():
        if group in group_to_part:
            part = group_to_part[group]
        else:
            part = {
                "order": next_order,
                "role": group,
                "node": {
                    "id": node_id(group),
                    "label": group,
                    "module_type": "TRANSPORT_STEP",
                    "description": f"First-pass membrane-associated enzyme subgroup: {group}.",
                    "annotons": [],
                },
            }
            next_order += 1
            parts.append(part)
        part.setdefault("node", {}).setdefault("annotons", []).extend(module_annoton(info) for info in group_infos)

    needed_concepts = {
        go_id
        for info in infos
        for go_id in ([info["profile"].get("primary")] + info["profile"].get("processes", []) + info["profile"].get("locations", []))
        if go_id
    }
    existing_concepts = concept_ids_from_module(doc)
    concepts = doc.setdefault("module", {}).setdefault("concepts", [])
    for go_id in sorted(needed_concepts - existing_concepts):
        concepts.append(descriptor(go_id, "Concept used for first-pass membrane-associated enzyme side-node curation."))

    evidence = doc.setdefault("evidence", [])
    source_id = f"file:{BATCH_PATH.relative_to(ROOT)}"
    if not any(item.get("source_id") == source_id for item in evidence):
        evidence.append(
            {
                "source_id": source_id,
                "title": "PSEPK transport-bucket membrane-associated enzyme side-node batch",
                "statement": "The batch table records 42 PSEPK transport/membrane/efflux-bucket genes assigned to membrane-associated hydrolase, peptidase, transferase, oxidoreductase, kinase, and low-information enzyme side-node contexts rather than transport systems.",
            }
        )
    doc["description"] = (
        "Boundary module for PSEPK membrane-associated enzyme and side-node proteins pulled into transport buckets by membrane or enzyme keywords. "
        "It combines earlier ion/metal membrane metalloenzyme and envelope side nodes with broader peptidase, acyltransferase, glycosyltransferase, oxidoreductase, kinase/phosphatase, detoxification, toxin-associated, HflK/HflC, and low-information membrane-enzyme candidates."
    )
    doc["notes"] = (
        "First-pass interpretation: keep this as a spillover boundary, not a transporter module. "
        "Enzyme-family calls are retained when product/domain and GOA agree; transporter rows inherited by histidine-kinase sensor proteins are marked as over-annotated. "
        "HflK/HflC and several domain-only membrane proteins are kept as side-node or location context rather than catalytic hydrolases. "
        "Substrate-specific calls are avoided for domain-only sulfatase, acyltransferase, oxidoreductase, sulfurtransferase, phosphatase, and low-information membrane proteins."
    )
    normalize_term_labels(doc)
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    infos = [curate_gene(row) for row in load_rows()]
    build_module(infos)
    print(f"Curated {len(infos)} genes")
    print(f"Wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
