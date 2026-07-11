#!/usr/bin/env python3
"""First-pass curation for membrane signaling, channel, and c-di-GMP spillovers."""

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
    "module_transport_membrane_efflux_membrane_signaling_channels_c_di_gmp_spillovers.tsv"
)
MODULE_PATH = ROOT / "modules/c_di_gmp_turnover_boundary.yaml"

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
    "GO:0003677": "DNA binding",
    "GO:0003700": "DNA-binding transcription factor activity",
    "GO:0003824": "catalytic activity",
    "GO:0005886": "plasma membrane",
    "GO:0006351": "DNA-templated transcription",
    "GO:0006352": "DNA-templated transcription initiation",
    "GO:0006355": "regulation of DNA-templated transcription",
    "GO:0006811": "monoatomic ion transport",
    "GO:0006821": "chloride transport",
    "GO:0007165": "signal transduction",
    "GO:0008381": "mechanosensitive monoatomic ion channel activity",
    "GO:0009992": "intracellular water homeostasis",
    "GO:0015108": "chloride transmembrane transporter activity",
    "GO:0016020": "membrane",
    "GO:0016301": "kinase activity",
    "GO:0016987": "sigma factor activity",
    "GO:0016989": "sigma factor antagonist activity",
    "GO:0034220": "monoatomic ion transmembrane transport",
    "GO:0043709": "cell adhesion involved in single-species biofilm formation",
    "GO:0045892": "negative regulation of DNA-templated transcription",
    "GO:0052621": "diguanylate cyclase activity",
    "GO:0055085": "transmembrane transport",
    "GO:0071111": "cyclic-guanylate-specific phosphodiesterase activity",
    "GO:0071470": "cellular response to osmotic stress",
    "GO:0071732": "cellular response to nitric oxide",
    "GO:1902201": "negative regulation of bacterial-type flagellum-dependent cell motility",
    "GO:1902476": "chloride transmembrane transport",
    "GO:2000142": "regulation of DNA-templated transcription initiation",
}

PROFILE: dict[str, dict[str, Any]] = {
    "PP_0131": {
        "class": "pde",
        "group": "EAL cyclic-guanylate phosphodiesterase candidates",
        "primary": "GO:0071111",
        "locations": ["GO:0005886"],
        "description": "PP_0131 encodes a membrane cyclic-guanylate-specific phosphodiesterase candidate with CSS and EAL-domain signatures, supporting c-di-GMP hydrolysis context.",
        "needles": ["Cyclic-di-GMP_PDE-like", "EAL_dom", "CSS-motif_dom", "KW   c-di-GMP"],
    },
    "PP_0165": {
        "class": "pde",
        "group": "EAL cyclic-guanylate phosphodiesterase candidates",
        "primary": "GO:0071111",
        "processes": ["GO:0007165"],
        "locations": ["GO:0016020"],
        "description": "PP_0165 encodes a membrane HAMP/LapD-like GGDEF-EAL signaling protein, curated in this first pass as a cyclic-guanylate phosphodiesterase candidate rather than a resolved diguanylate cyclase.",
        "needles": ["Cyclic-di-GMP_PDE-like", "EAL_dom", "GGDEF_dom", "HAMP_dom"],
    },
    "PP_0197": {
        "class": "mechanosensitive_channel",
        "group": "MscS/MscL mechanosensitive channel spillovers",
        "primary": "GO:0008381",
        "processes": ["GO:0034220"],
        "locations": ["GO:0005886"],
        "description": "PP_0197 encodes a small-conductance MscS-family mechanosensitive inner-membrane channel involved in ion flux during membrane-stretch or osmotic stress.",
        "needles": ["Belongs to the MscS", "MscS_channel_2nd", "MS_channel_2nd", "KW   Ion channel"],
    },
    "PP_0218": {
        "class": "pde",
        "group": "EAL cyclic-guanylate phosphodiesterase candidates",
        "primary": "GO:0071111",
        "locations": ["GO:0016020"],
        "description": "PP_0218 encodes a membrane GGDEF-EAL cyclic-guanylate-specific phosphodiesterase candidate with EC-backed c-di-GMP hydrolysis annotation.",
        "needles": ["EC=3.1.4.52", "Biofilm_reg_signaling", "EAL_dom", "GGDEF_dom"],
    },
    "PP_0369": {
        "class": "dgc",
        "group": "GGDEF diguanylate cyclase candidates",
        "primary": "GO:0052621",
        "locations": ["GO:0005886"],
        "description": "PP_0369 encodes a membrane GGDEF-domain diguanylate cyclase that synthesizes c-di-GMP, with biofilm and flagellar-motility annotations retained as regulatory-output context.",
        "needles": ["EC=2.7.7.65", "Diguanylate_Cyclase", "GGDEF_dom", "GGDEF (PF00990)"],
    },
    "PP_0668": {
        "class": "fecr_sensor",
        "group": "FecR/ECF sigma membrane regulatory spillovers",
        "primary": "GO:0016989",
        "processes": ["GO:0045892"],
        "locations": ["GO:0016020"],
        "description": "PP_0668 encodes a FecR-family transmembrane anti-sigma regulatory sensor, supporting sigma-factor antagonist and transcriptional repression context.",
        "needles": ["Transmembrane sensor", "FecR.", "Ferrdict_sens_TM", "KW   Membrane"],
    },
    "PP_0672": {
        "class": "pde",
        "group": "EAL cyclic-guanylate phosphodiesterase candidates",
        "primary": "GO:0071111",
        "locations": ["GO:0005886"],
        "description": "PP_0672 encodes a membrane sensory GGDEF-EAL cyclic-guanylate-specific phosphodiesterase candidate, with nitric-oxide response retained as c-di-GMP signaling context.",
        "needles": ["EC=3.1.4.52", "Biofilm_reg_signaling", "EAL_dom", "GGDEF_dom"],
    },
    "PP_0700": {
        "class": "fecr_sensor",
        "group": "FecR/ECF sigma membrane regulatory spillovers",
        "primary": "GO:0016989",
        "processes": ["GO:0045892"],
        "locations": ["GO:0016020"],
        "description": "PP_0700 encodes a FecR-family transmembrane anti-sigma regulatory sensor, supporting sigma-factor antagonist and transcriptional repression context.",
        "needles": ["Transmembrane sensor", "FecR.", "Ferrdict_sens_TM", "KW   Membrane"],
    },
    "PP_0707": {
        "class": "mechanosensitive_channel",
        "group": "MscS/MscL mechanosensitive channel spillovers",
        "primary": "GO:0008381",
        "processes": ["GO:0034220"],
        "locations": ["GO:0005886"],
        "description": "PP_0707 encodes an MscS-family membrane channel candidate with mechanosensitive monoatomic ion channel and transmembrane-transport annotations.",
        "needles": ["Belongs to the MscS", "MscS-like_channel", "MS_channel_C", "KW   Signal"],
    },
    "PP_0798": {
        "class": "dgc",
        "group": "GGDEF diguanylate cyclase candidates",
        "primary": "GO:0052621",
        "locations": ["GO:0005886"],
        "description": "PP_0798 encodes a membrane GGDEF-domain diguanylate cyclase with a histidine-kinase-like sensory input domain, supporting c-di-GMP synthesis context.",
        "needles": ["EC=2.7.7.65", "Diguanylate_Cyclase", "His-kinase-like_sensor", "GGDEF_dom"],
    },
    "PP_1144": {
        "class": "pde",
        "group": "EAL cyclic-guanylate phosphodiesterase candidates",
        "primary": "GO:0071111",
        "locations": ["GO:0005886"],
        "description": "PP_1144 encodes a membrane MHYT/GGDEF-EAL diguanylate phosphodiesterase candidate, supporting c-di-GMP hydrolysis context while leaving sensor input unresolved.",
        "needles": ["Diguanylate phosphodiesterase", "Biofilm_reg_signaling", "EAL_dom", "MHYT_dom"],
    },
    "PP_1154": {
        "class": "domain_only_c_di_gmp_sensor",
        "group": "Domain-only c-di-GMP signaling candidates",
        "primary": None,
        "locations": ["GO:0005886"],
        "description": "PP_1154 encodes a membrane CHASE/PAS/GGDEF-EAL sensory box protein with c-di-GMP signaling-domain architecture, but the first pass does not resolve whether the GGDEF or EAL active site is catalytically active.",
        "needles": ["Sensory box protein", "Biofilm_reg_signaling", "CHASE4", "EAL_dom", "GGDEF_dom"],
    },
    "PP_1155": {
        "class": "dgc",
        "group": "GGDEF diguanylate cyclase candidates",
        "primary": "GO:0052621",
        "locations": ["GO:0005886"],
        "description": "PP_1155 encodes a membrane MASE2/GGDEF diguanylate cyclase that synthesizes c-di-GMP, with biofilm and flagellar-motility annotations retained as regulatory-output context.",
        "needles": ["EC=2.7.7.65", "Diguanylate_Cyclase", "MASE2", "GGDEF_dom"],
    },
    "PP_1353": {
        "class": "mechanosensitive_channel",
        "group": "MscS/MscL mechanosensitive channel spillovers",
        "primary": "GO:0008381",
        "processes": ["GO:0034220"],
        "locations": ["GO:0005886"],
        "description": "PP_1353 encodes a small-conductance MscS-family mechanosensitive inner-membrane channel involved in ion flux during membrane-stretch or osmotic stress.",
        "needles": ["Belongs to the MscS", "MscS_archaea/bacteria_type", "MS_channel_1st", "KW   Ion channel"],
    },
    "PP_1411": {
        "class": "dgc",
        "group": "GGDEF diguanylate cyclase candidates",
        "primary": "GO:0052621",
        "locations": ["GO:0005886"],
        "description": "PP_1411 encodes a membrane GGDEF-domain diguanylate cyclase that synthesizes c-di-GMP.",
        "needles": ["EC=2.7.7.65", "Diguanylate_Cyclase", "GGDEF_dom", "GGDEF (PF00990)"],
    },
    "PP_1728": {
        "class": "mechanosensitive_channel",
        "group": "MscS/MscL mechanosensitive channel spillovers",
        "primary": "GO:0008381",
        "processes": ["GO:0034220"],
        "locations": ["GO:0005886"],
        "description": "PP_1728 encodes an MscS-family mechanosensitive ion channel protein predicted to mediate membrane-stretch-responsive ion flux.",
        "needles": ["Belongs to the MscS", "MscS_channel_2nd", "MS_channel_1st", "KW   Membrane"],
    },
    "yegE": {
        "class": "dgc_dual_domain",
        "group": "GGDEF diguanylate cyclase candidates",
        "primary": "GO:0052621",
        "locations": ["GO:0005886"],
        "description": "yegE encodes a membrane PAS/GGDEF-EAL c-di-GMP signaling protein, curated in this first pass as a diguanylate cyclase with an associated phosphodiesterase-domain architecture.",
        "needles": ["Diguanylate cyclase with phosphodiesterase domain", "Biofilm_reg_signaling", "EAL_dom", "GGDEF_dom"],
    },
    "cmpX": {
        "class": "mechanosensitive_channel",
        "group": "MscS/MscL mechanosensitive channel spillovers",
        "primary": "GO:0008381",
        "processes": ["GO:0034220"],
        "locations": ["GO:0005886"],
        "description": "cmpX encodes a small-conductance MscS-family mechanosensitive inner-membrane channel involved in ion flux during membrane-stretch or osmotic stress.",
        "needles": ["Belongs to the MscS", "MSC_TM_helix", "MscS_channel_2nd", "KW   Ion channel"],
    },
    "PP_2097": {
        "class": "dgc",
        "group": "GGDEF diguanylate cyclase candidates",
        "primary": "GO:0052621",
        "processes": ["GO:0007165"],
        "locations": ["GO:0005886"],
        "description": "PP_2097 encodes a CHASE-domain membrane GGDEF diguanylate cyclase candidate that links sensory input to c-di-GMP synthesis.",
        "needles": ["EC=2.7.7.65", "CHASE_dom", "Diguanylate_Cyclase", "GGDEF_dom"],
    },
    "PP_2192": {
        "class": "sigma_fecR_fusion",
        "group": "FecR/ECF sigma membrane regulatory spillovers",
        "primary": "GO:0016987",
        "processes": ["GO:0006352"],
        "locations": [],
        "description": "PP_2192 encodes an ECF sigma-factor and FecR-like transmembrane-sensor fusion candidate, supporting transcription-initiation and sigma-regulatory context rather than a resolved transporter role.",
        "needles": ["RNA polymerase sigma-70 factor", "RNA_pol_sigma-70_dom", "FecR.", "Ferrdict_sens_TM"],
    },
    "PP_2413": {
        "class": "dgc",
        "group": "GGDEF diguanylate cyclase candidates",
        "primary": "GO:0052621",
        "locations": ["GO:0005886"],
        "description": "PP_2413 encodes a dCache/GGDEF membrane diguanylate cyclase candidate that links periplasmic sensing to c-di-GMP synthesis.",
        "needles": ["EC=2.7.7.65", "dCache_1", "Diguanylate_Cyclase", "GGDEF_dom"],
    },
    "PP_2741": {
        "class": "mechanosensitive_channel",
        "group": "MscS/MscL mechanosensitive channel spillovers",
        "primary": "GO:0008381",
        "processes": ["GO:0034220"],
        "locations": ["GO:0005886"],
        "description": "PP_2741 encodes a small-conductance MscS-family mechanosensitive inner-membrane channel involved in ion flux during membrane-stretch or osmotic stress.",
        "needles": ["Belongs to the MscS", "MscS_archaea/bacteria_type", "MS_channel_C", "KW   Ion channel"],
    },
    "PP_3242": {
        "class": "dgc",
        "group": "GGDEF diguanylate cyclase candidates",
        "primary": "GO:0052621",
        "locations": ["GO:0005886"],
        "description": "PP_3242 encodes a membrane GGDEF-domain diguanylate cyclase with a histidine-kinase-like sensory input domain, supporting c-di-GMP synthesis context.",
        "needles": ["EC=2.7.7.65", "Diguanylate_Cyclase", "His-kinase-like_sensor", "GGDEF_dom"],
    },
    "PP_3315": {
        "class": "low_confidence_dgc_name",
        "group": "Domain-only c-di-GMP signaling candidates",
        "primary": None,
        "locations": ["GO:0005886"],
        "description": "PP_3315 encodes a multi-pass membrane protein with a weak automated diguanylate-cyclase product name but only PsiE-like domain evidence, so this first pass retains membrane context without assigning a c-di-GMP enzyme activity.",
        "needles": ["Diguanylate cyclase", "P_starv_induced_PsiE-like", "PsiE", "KW   Cell membrane"],
    },
    "PP_3348": {
        "class": "dgc",
        "group": "GGDEF diguanylate cyclase candidates",
        "primary": "GO:0052621",
        "locations": ["GO:0005886"],
        "description": "PP_3348 encodes a membrane GGDEF-domain diguanylate cyclase that synthesizes c-di-GMP.",
        "needles": ["EC=2.7.7.65", "Diguanylate_Cyclase", "GGDEF_dom", "GGDEF (PF00990)"],
    },
    "PP_3360": {
        "class": "mechanosensitive_channel",
        "group": "MscS/MscL mechanosensitive channel spillovers",
        "primary": "GO:0008381",
        "processes": ["GO:0034220"],
        "locations": ["GO:0005886"],
        "description": "PP_3360 encodes an MscS-family mechanosensitive ion channel protein predicted to mediate membrane-stretch-responsive ion flux.",
        "needles": ["Belongs to the MscS", "Mechanosensitive ion channel protein MscS", "MscS_channel_2nd", "MS_channel_1st"],
    },
    "PP_3432": {
        "class": "low_confidence_css_pde_name",
        "group": "Domain-only c-di-GMP signaling candidates",
        "primary": None,
        "locations": ["GO:0016020"],
        "description": "PP_3432 encodes a membrane CSS-motif protein with a putative cyclic-diguanylate phosphodiesterase product name but without EAL or HD-GYP support, so this first pass keeps it as a low-confidence c-di-GMP signaling candidate.",
        "needles": ["Putative cyclic diguanylate phosphodiesterase", "CSS-motif_dom", "CSS-motif", "KW   Membrane"],
    },
    "PP_3435": {
        "class": "pde",
        "group": "EAL cyclic-guanylate phosphodiesterase candidates",
        "primary": "GO:0071111",
        "locations": ["GO:0005886"],
        "description": "PP_3435 encodes a membrane CSS/EAL cyclic-guanylate-specific phosphodiesterase candidate, supporting c-di-GMP hydrolysis context.",
        "needles": ["EC=3.1.4.52", "Cyclic-di-GMP_PDE-like", "EAL_dom", "CSS-motif_dom"],
    },
    "PP_3452": {
        "class": "dgc",
        "group": "GGDEF diguanylate cyclase candidates",
        "primary": "GO:0052621",
        "locations": ["GO:0005886"],
        "description": "PP_3452 encodes a membrane GGDEF-domain diguanylate cyclase that synthesizes c-di-GMP.",
        "needles": ["EC=2.7.7.65", "Diguanylate_Cyclase", "GGDEF_dom", "GGDEF (PF00990)"],
    },
    "PP_3555": {
        "class": "fecr_sensor",
        "group": "FecR/ECF sigma membrane regulatory spillovers",
        "primary": "GO:0016989",
        "processes": ["GO:0045892"],
        "locations": ["GO:0016020"],
        "description": "PP_3555 encodes a FecR-family transmembrane anti-sigma regulatory sensor, supporting sigma-factor antagonist and transcriptional repression context.",
        "needles": ["Transmembrane sensor", "FecR.", "Ferrdict_sens_TM", "KW   Membrane"],
    },
    "htrG": {
        "class": "low_info_signal_membrane",
        "group": "Low-information membrane signal-transduction side nodes",
        "primary": None,
        "locations": ["GO:0016020"],
        "description": "htrG encodes a membrane signal-transduction protein with SH3-like bacterial domains, but no resolved ligand, pathway, or molecular activity in this first pass.",
        "needles": ["Signal transduction protein", "SH3-like_bac-type", "SH3_dom_pro", "KW   Membrane"],
    },
    "PP_3663": {
        "class": "dgc",
        "group": "GGDEF diguanylate cyclase candidates",
        "primary": "GO:0052621",
        "locations": ["GO:0005886"],
        "description": "PP_3663 encodes a membrane GGDEF-domain diguanylate cyclase that synthesizes c-di-GMP.",
        "needles": ["EC=2.7.7.65", "Diguanylate_Cyclase", "GGDEF_dom", "GGDEF (PF00990)"],
    },
    "PP_3932": {
        "class": "dgc",
        "group": "GGDEF diguanylate cyclase candidates",
        "primary": "GO:0052621",
        "locations": ["GO:0005886"],
        "description": "PP_3932 encodes a membrane GGDEF-domain diguanylate cyclase that synthesizes c-di-GMP.",
        "needles": ["EC=2.7.7.65", "Diguanylate_Cyclase", "GGDEF_dom", "GGDEF (PF00990)"],
    },
    "PP_3959": {
        "class": "chloride_channel",
        "group": "Chloride and bestrophin channel spillovers",
        "primary": "GO:0015108",
        "processes": ["GO:1902476", "GO:0006821"],
        "locations": ["GO:0016020"],
        "description": "PP_3959 encodes a ClC-family membrane chloride channel or transporter candidate involved in chloride transmembrane transport.",
        "needles": ["Voltage-gated chloride channel", "ClC-type_chloride_channel", "Cl-channel_core", "Voltage_CLC"],
    },
    "mscMB": {
        "class": "mechanosensitive_channel",
        "group": "MscS/MscL mechanosensitive channel spillovers",
        "primary": "GO:0008381",
        "processes": ["GO:0034220", "GO:0071470"],
        "locations": ["GO:0005886"],
        "description": "mscMB encodes a YbdG/MscS-family mechanosensitive channel homolog that contributes to membrane-stretch-responsive ion flux and osmotic-stress response.",
        "needles": ["Mechanosensing system component YbdG", "Belongs to the MscS", "YbdG.", "KW   Stress response"],
    },
    "PP_4598": {
        "class": "bestrophin_channel",
        "group": "Chloride and bestrophin channel spillovers",
        "primary": "GO:0015108",
        "locations": ["GO:0005886"],
        "description": "PP_4598 encodes a bestrophin-family multi-pass membrane protein, curated as a candidate chloride/anion channel pending direct substrate-specific evidence.",
        "needles": ["Bestrophin", "anion channel-forming bestrophin", "YneE/VCCN1/2-like", "Bestrophin_2"],
    },
    "mscL": {
        "class": "mechanosensitive_channel",
        "group": "MscS/MscL mechanosensitive channel spillovers",
        "primary": "GO:0008381",
        "processes": ["GO:0034220"],
        "locations": ["GO:0005886"],
        "description": "mscL encodes the large-conductance mechanosensitive inner-membrane channel that opens under membrane stretch to relieve osmotic pressure.",
        "needles": ["Large-conductance mechanosensitive channel", "Belongs to the MscL family", "MscL_channel", "MscL (PF01741)"],
        "skip_gene_rewrite": True,
    },
    "kefA": {
        "class": "mechanosensitive_channel",
        "group": "MscS/MscL mechanosensitive channel spillovers",
        "primary": "GO:0008381",
        "processes": ["GO:0034220", "GO:0009992"],
        "locations": ["GO:0005886"],
        "description": "kefA encodes an intermediate-conductance MscS-like mechanosensitive channel associated with K+ efflux, membrane-stretch-responsive ion flux, and intracellular water homeostasis.",
        "needles": ["Mechanosensitive channel protein", "Belongs to the MscS", "K+ efflux", "MscS-like_channel"],
    },
    "PP_5256": {
        "class": "mechanosensitive_channel",
        "group": "MscS/MscL mechanosensitive channel spillovers",
        "primary": "GO:0008381",
        "processes": ["GO:0034220"],
        "locations": ["GO:0005886"],
        "description": "PP_5256 encodes a small-conductance MscS-family mechanosensitive channel candidate with cyclic-nucleotide-binding and membrane-channel domains.",
        "needles": ["Belongs to the MscS", "Small-conductance mechanosensitive channel", "cNMP-bd_ion_channel", "MscS_archaea/bacteria_type"],
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
        return review(
            info,
            "Bacterial plasma-membrane localization is appropriate for this membrane signaling or channel protein.",
            "ACCEPT",
            "UniProt membrane/transmembrane evidence and the GOA cellular-component annotation support plasma-membrane context.",
        )
    if go_id == "GO:0016020":
        if "GO:0005886" in info.get("go_ids", []):
            return review(
                info,
                "Generic membrane localization is true but less informative than the plasma-membrane annotation.",
                "MARK_AS_OVER_ANNOTATED",
                "A more specific plasma-membrane annotation is also present for this bacterial membrane protein.",
            )
        return review(
            info,
            "Membrane localization is appropriate for this predicted transmembrane signaling or channel protein.",
            "ACCEPT",
            "UniProt keyword, transmembrane-feature, or product evidence supports membrane localization.",
        )
    raise ValueError(f"Unhandled location term {go_id}")


def existing_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    go_id = ann["term"]["id"]
    label = ann["term"]["label"]
    cls = info["profile"]["class"]
    primary = info["profile"].get("primary")

    if go_id in {"GO:0005886", "GO:0016020"}:
        return location_review(info, go_id)

    if go_id == "GO:0003824":
        if primary:
            return review(
                info,
                "Generic catalytic activity is too broad for this domain-resolved signaling enzyme candidate.",
                "MARK_AS_OVER_ANNOTATED",
                f"{TERMS[primary]} captures the supported nucleotide-turnover activity more specifically.",
                [primary],
            )
        return review(
            info,
            "Generic catalytic activity is too broad for this domain-only c-di-GMP signaling candidate.",
            "MARK_AS_OVER_ANNOTATED",
            "The protein has GGDEF/EAL-like signaling-domain architecture, but this first pass does not resolve an active catalytic site or substrate-specific reaction.",
        )

    if cls in {"pde", "domain_only_c_di_gmp_sensor", "low_confidence_css_pde_name"}:
        if go_id == "GO:0071111":
            return review(
                info,
                "Cyclic-guanylate-specific phosphodiesterase activity is appropriate for this EAL-domain c-di-GMP hydrolysis candidate.",
                "ACCEPT",
                "Product, EC, InterPro/Pfam, and GOA evidence support cyclic di-GMP phosphodiesterase context.",
            )
        if go_id == "GO:0007165":
            return review(
                info,
                "Signal transduction is appropriate but secondary to the c-di-GMP turnover domain architecture.",
                "KEEP_AS_NON_CORE",
                "The HAMP/GGDEF/EAL architecture supports membrane-linked signaling context, but the molecular c-di-GMP turnover activity is more informative.",
            )
        if go_id == "GO:0071732":
            return review(
                info,
                "Cellular response to nitric oxide is retained as possible signaling-output context rather than the core molecular function.",
                "KEEP_AS_NON_CORE",
                "The cyclic-guanylate phosphodiesterase activity is the core molecular-function call; nitric-oxide response may be pathway context but is not resolved in this first pass.",
            )

    if cls in {"dgc", "dgc_dual_domain", "low_confidence_dgc_name"}:
        if go_id == "GO:0052621":
            return review(
                info,
                "Diguanylate cyclase activity is the supported c-di-GMP synthesis molecular function.",
                "ACCEPT",
                "Product, EC, GGDEF-domain, and GOA evidence support c-di-GMP synthesis from GTP.",
            )
        if go_id == "GO:0043709":
            return review(
                info,
                "Biofilm-related cell adhesion is plausible c-di-GMP regulatory-output context but not the core molecular function.",
                "KEEP_AS_NON_CORE",
                "Diguanylate cyclase activity is the direct role; biofilm attachment is a downstream process influenced by c-di-GMP signaling.",
            )
        if go_id == "GO:1902201":
            return review(
                info,
                "Negative regulation of flagellum-dependent motility is plausible c-di-GMP regulatory-output context but not the core molecular function.",
                "KEEP_AS_NON_CORE",
                "Diguanylate cyclase activity is the direct role; motility regulation is a downstream c-di-GMP signaling effect.",
            )
        if go_id == "GO:0007165":
            return review(
                info,
                "Signal transduction is appropriate but secondary to the GGDEF diguanylate-cyclase role.",
                "KEEP_AS_NON_CORE",
                "The CHASE or other sensory architecture places the enzyme in signaling, while the enzyme activity is the more specific molecular function.",
            )
        if go_id == "GO:0006355":
            return review(
                info,
                "Regulation of DNA-templated transcription is too indirect for this c-di-GMP enzyme candidate in the current evidence set.",
                "MARK_AS_OVER_ANNOTATED",
                "The protein is better represented as a c-di-GMP signaling enzyme; direct transcriptional regulation is not established here.",
                ["GO:0052621"] if primary == "GO:0052621" else None,
            )

    if cls == "mechanosensitive_channel":
        if go_id == "GO:0008381":
            return review(
                info,
                "Mechanosensitive monoatomic ion channel activity is the supported channel molecular function.",
                "ACCEPT",
                "MscS/MscL-family product, family, and GOA evidence support membrane-stretch-gated ion-channel activity.",
            )
        if go_id == "GO:0034220":
            return review(
                info,
                "Monoatomic ion transmembrane transport is appropriate process context for a mechanosensitive membrane channel.",
                "ACCEPT",
                "The channel activity directly mediates transmembrane ion flux during mechanosensitive gating.",
            )
        if go_id == "GO:0006811":
            return review(
                info,
                "Monoatomic ion transport is true but broader than the transmembrane mechanosensitive channel process.",
                "MARK_AS_OVER_ANNOTATED",
                "GO:0034220 monoatomic ion transmembrane transport and GO:0008381 mechanosensitive channel activity capture the function more specifically.",
                ["GO:0034220"],
            )
        if go_id == "GO:0055085":
            return review(
                info,
                "Transmembrane transport is retained as broad channel process context.",
                "KEEP_AS_NON_CORE",
                "The more informative process is monoatomic ion transmembrane transport coupled to mechanosensitive channel activity.",
            )
        if go_id == "GO:0009992":
            return review(
                info,
                "Intracellular water homeostasis is appropriate physiological context for the KefA/MscS-like mechanosensitive channel.",
                "ACCEPT",
                "Mechanosensitive channels relieve osmotic and turgor stress by permitting solute or ion flux that affects water balance.",
            )
        if go_id == "GO:0071470":
            return review(
                info,
                "Cellular response to osmotic stress is appropriate physiological context for this MscS/YbdG-family mechanosensitive channel.",
                "ACCEPT",
                "The mechanosensitive channel role directly supports osmotic-stress response.",
            )

    if cls == "chloride_channel":
        if go_id == "GO:0015108":
            return review(
                info,
                "Chloride transmembrane transporter activity is the supported ClC-family molecular function.",
                "ACCEPT",
                "Product, ClC-domain, PANTHER-family, and GOA evidence support chloride transport across the membrane.",
            )
        if go_id in {"GO:0006821", "GO:1902476"}:
            return review(
                info,
                f"{label} is appropriate chloride-transport process context for this ClC-family membrane protein.",
                "ACCEPT",
                "The ClC-family product/domain evidence supports chloride transmembrane transport.",
            )
        if go_id == "GO:0055085":
            return review(
                info,
                "Transmembrane transport is retained as broad context for the chloride channel/transporter role.",
                "KEEP_AS_NON_CORE",
                "The chloride-specific activity and process terms are more informative.",
            )

    if cls in {"fecr_sensor", "sigma_fecR_fusion"}:
        if go_id == "GO:0016989":
            action = "ACCEPT" if cls == "fecr_sensor" else "KEEP_AS_NON_CORE"
            return review(
                info,
                "Sigma factor antagonist activity is consistent with the FecR-family anti-sigma regulatory domain.",
                action,
                "FecR-family membrane sensors regulate ECF sigma-factor activity; in the sigma-domain fusion this is retained as secondary regulatory context.",
            )
        if go_id == "GO:0045892":
            action = "ACCEPT" if cls == "fecr_sensor" else "KEEP_AS_NON_CORE"
            return review(
                info,
                "Negative regulation of DNA-templated transcription is consistent with anti-sigma regulatory context.",
                action,
                "FecR-like anti-sigma regulation affects sigma-dependent transcription; this is direct context for FecR sensors and secondary context for the sigma-domain fusion.",
            )
        if go_id == "GO:0016987":
            return review(
                info,
                "Sigma factor activity is the core molecular-function call for the ECF sigma-domain fusion candidate.",
                "ACCEPT",
                "The product name and sigma-70 domain evidence support RNA polymerase sigma-factor activity.",
            )
        if go_id == "GO:0006352":
            return review(
                info,
                "DNA-templated transcription initiation is appropriate process context for a sigma-factor domain protein.",
                "ACCEPT",
                "Sigma factors direct RNA polymerase promoter recognition during transcription initiation.",
            )
        if go_id == "GO:2000142":
            return review(
                info,
                "Regulation of DNA-templated transcription initiation is appropriate sigma-regulatory process context.",
                "ACCEPT",
                "The ECF sigma and FecR-like regulatory architecture supports transcription-initiation regulation.",
            )
        if go_id == "GO:0003700":
            return review(
                info,
                "DNA-binding transcription factor activity is retained as broad sigma-factor transcription-regulatory context.",
                "KEEP_AS_NON_CORE",
                "Sigma factor activity is the more precise molecular-function term.",
                ["GO:0016987"],
            )
        if go_id == "GO:0003677":
            return review(
                info,
                "DNA binding is a broad molecular-function parent and is less informative than sigma factor activity.",
                "MARK_AS_OVER_ANNOTATED",
                "The sigma-factor activity term captures the specific DNA/RNA-polymerase promoter-recognition role.",
                ["GO:0016987"],
            )
        if go_id in {"GO:0006351", "GO:0006355"}:
            return review(
                info,
                f"{label} is true but broad transcriptional process context for the sigma-factor/fecR-like fusion.",
                "KEEP_AS_NON_CORE",
                "DNA-templated transcription initiation and sigma-factor activity are more specific for this protein architecture.",
            )

    if cls == "low_info_signal_membrane" and go_id == "GO:0016020":
        return location_review(info, go_id)

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
        out.append(
            new_annotation(
                info,
                primary,
                "enables",
                f"Adds {TERMS[primary]} for this membrane signaling or channel protein.",
                "UniProt product/domain evidence and Asta retrieval context support this conservative first-pass assignment.",
            )
        )
    for process in info["profile"].get("processes", []):
        if process not in go_ids:
            out.append(
                new_annotation(
                    info,
                    process,
                    "involved_in",
                    f"Adds {TERMS[process]} process context.",
                    "The supported product, family, or domain context implies this conservative process annotation.",
                )
            )
    for location in info["profile"].get("locations", []):
        if location not in go_ids:
            out.append(
                new_annotation(
                    info,
                    location,
                    "located_in",
                    f"Adds {TERMS[location]} localization context.",
                    "UniProt membrane, compartment, or transmembrane evidence supports this localization.",
                )
            )
    return out


def references(info: GeneInfo) -> list[dict[str, Any]]:
    refs: dict[str, dict[str, Any]] = {}
    for ref_id, ref in info["existing_refs"].items():
        refs[ref_id] = ref
    for ref_id, title in GO_REF_TITLES.items():
        if ref_id in refs:
            refs[ref_id]["title"] = title
    gene = info["gene"]
    refs[ref_file(gene, "goa.tsv")] = {
        "id": ref_file(gene, "goa.tsv"),
        "title": f"QuickGO GOA annotations for {gene}",
        "findings": [],
    }
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
    core: dict[str, Any] = {
        "description": profile["description"],
        "supported_by": base_support(info),
    }
    primary = profile.get("primary")
    if primary:
        core["molecular_function"] = term(primary)
    if profile.get("processes"):
        core["directly_involved_in"] = [term(go_id) for go_id in profile["processes"]]
    if profile.get("locations"):
        core["locations"] = [term(go_id) for go_id in profile["locations"]]
    return core


def write_preserved_gene(info: GeneInfo) -> GeneInfo:
    gene = info["gene"]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    info["go_ids"] = [ann["term"]["id"] for ann in doc.get("existing_annotations", [])]
    info["existing_refs"] = {ref["id"]: ref for ref in doc.get("references", []) if "id" in ref}
    doc["status"] = "COMPLETE"
    doc["references"] = references(info)
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def curate_gene(row: dict[str, str]) -> GeneInfo:
    info = load_info(row)
    if info["profile"].get("skip_gene_rewrite"):
        return write_preserved_gene(info)
    gene = info["gene"]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    goa_annotations = [
        ann
        for ann in doc.get("existing_annotations", [])
        if not (
            ann.get("original_reference_id") == ref_file(gene, "uniprot.txt")
            and (ann.get("review") or {}).get("action") == "NEW"
        )
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
    reflected_ids = {
        ann["term"]["id"]
        for ann in doc["existing_annotations"]
        if (ann.get("review") or {}).get("action") in {"ACCEPT", "NEW"}
    }
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
        {
            "question": "What is the direct substrate, gating cue, ligand input, partner protein, or physiological condition for this KT2440 membrane signaling or channel protein?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Test purified proteins and targeted mutants for c-di-GMP synthesis or hydrolysis, channel conductance and gating, chloride or anion selectivity, sigma-factor partner regulation, and condition-specific biofilm, motility, osmotic, or transcriptional phenotypes as appropriate.",
            "experiment_type": "targeted biochemical, electrophysiological, and condition-specific genetics",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    safe_gene = re.sub(r"[^A-Za-z0-9_]+", "_", gene)
    annoton: dict[str, Any] = {
        "id": f"{safe_gene}_membrane_signaling_channel_context",
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
    concepts = doc.get("module", {}).get("concepts", [])
    return {
        concept.get("term", {}).get("id")
        for concept in concepts
        if concept.get("term", {}).get("id")
    }


def remove_current_annotons(doc: dict[str, Any], genes: set[str]) -> None:
    for part in doc.get("module", {}).get("parts", []):
        node = part.get("node", {})
        kept = []
        for annoton in node.get("annotons", []):
            preferred = annoton.get("participant", {}).get("gene", {}).get("preferred_term")
            if preferred not in genes:
                kept.append(annoton)
        node["annotons"] = kept


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
    group_to_part: dict[str, dict[str, Any]] = {}
    for part in parts:
        group_to_part[part.get("role", "")] = part
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
                    "module_type": "SIGNALING_PATHWAY",
                    "description": f"First-pass membrane signaling/channel subgroup: {group}.",
                    "annotons": [],
                },
            }
            next_order += 1
            parts.append(part)
        annotons = part.setdefault("node", {}).setdefault("annotons", [])
        annotons.extend(module_annoton(info) for info in group_infos)

    needed_concepts = {
        go_id
        for info in infos
        for go_id in ([info["profile"].get("primary")] + info["profile"].get("processes", []) + info["profile"].get("locations", []))
        if go_id
    }
    existing_concepts = concept_ids_from_module(doc)
    concepts = doc.setdefault("module", {}).setdefault("concepts", [])
    for go_id in sorted(needed_concepts - existing_concepts):
        concepts.append(descriptor(go_id, "Concept used for first-pass membrane signaling/channel/c-di-GMP curation."))

    evidence = doc.setdefault("evidence", [])
    source_id = f"file:{BATCH_PATH.relative_to(ROOT)}"
    if not any(item.get("source_id") == source_id for item in evidence):
        evidence.append(
            {
                "source_id": source_id,
                "title": "PSEPK transport-bucket membrane signaling, channel, and c-di-GMP spillover batch",
                "statement": "The batch table records 39 PSEPK transport/membrane/efflux-bucket genes assigned to c-di-GMP turnover enzymes, mechanosensitive channels, chloride/bestrophin channel candidates, FecR/ECF sigma regulatory sensors, and low-information membrane signaling side nodes.",
            }
        )
    doc["description"] = (
        "Boundary module for PSEPK c-di-GMP and cyclic-nucleotide turnover proteins plus adjacent membrane signaling and channel spillovers. "
        "It keeps established GGDEF diguanylate cyclases and EAL cyclic-guanylate phosphodiesterases together with lower-confidence GGDEF/EAL/CSS/PsiE candidates, "
        "and records neighboring mechanosensitive-channel, chloride/bestrophin-channel, and FecR/ECF-sigma regulatory proteins that entered the transport bucket through membrane, signaling, or channel evidence."
    )
    doc["notes"] = (
        "First-pass interpretation: treat this as a reusable boundary/spillover module, not a single satisfiable pathway. "
        "EC/product/GOA-supported c-di-GMP synthesis and hydrolysis calls are retained as core enzyme functions. "
        "Biofilm, motility, nitric-oxide, and broad signal-transduction terms are kept as downstream or non-core signaling context unless direct gene-specific evidence is present. "
        "Mechanosensitive and chloride/bestrophin channels are separated from c-di-GMP turnover, and FecR/ECF-sigma membrane sensors are kept as regulatory spillovers. "
        "Domain-only CSS/PsiE/GGDEF-EAL candidates remain low-confidence until active-site, ligand, partner, or phenotype evidence is available."
    )
    normalize_term_labels(doc)
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    infos = [curate_gene(row) for row in load_rows()]
    build_module(infos)
    print(f"Curated or carried forward {len(infos)} genes")
    print(f"Wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
