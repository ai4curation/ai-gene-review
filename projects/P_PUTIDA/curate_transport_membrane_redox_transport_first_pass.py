#!/usr/bin/env python3
"""First-pass curation for the transport-bucket membrane redox tranche."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = (
    ROOT
    / "projects/P_PUTIDA/batches/"
    "module_transport_membrane_efflux_membrane_redox_electron_transfer_proteins.tsv"
)
MODULE_PATH = ROOT / "modules/membrane_redox_electron_transfer_boundary.yaml"

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0003824": "catalytic activity",
    "GO:0005737": "cytoplasm",
    "GO:0005829": "cytosol",
    "GO:0005886": "plasma membrane",
    "GO:0006457": "protein folding",
    "GO:0008961": "phosphatidylglycerol-prolipoprotein diacylglyceryl transferase activity",
    "GO:0009055": "electron transfer activity",
    "GO:0010181": "FMN binding",
    "GO:0015035": "protein-disulfide reductase activity",
    "GO:0015036": "disulfide oxidoreductase activity",
    "GO:0015038": "glutathione disulfide oxidoreductase activity",
    "GO:0015232": "heme transmembrane transporter activity",
    "GO:0015886": "heme transport",
    "GO:0016020": "membrane",
    "GO:0016491": "oxidoreductase activity",
    "GO:0016682": "oxidoreductase activity, acting on diphenols and related substances as donors, oxygen as acceptor",
    "GO:0017004": "cytochrome complex assembly",
    "GO:0019646": "aerobic electron transport chain",
    "GO:0020037": "heme binding",
    "GO:0022900": "electron transport chain",
    "GO:0030058": "aliphatic amine dehydrogenase activity",
    "GO:0030313": "cell envelope",
    "GO:0033539": "fatty acid beta-oxidation using acyl-CoA dehydrogenase",
    "GO:0034599": "cellular response to oxidative stress",
    "GO:0042158": "lipoprotein biosynthetic process",
    "GO:0042597": "periplasmic space",
    "GO:0045454": "cell redox homeostasis",
    "GO:0046395": "carboxylic acid catabolic process",
    "GO:0047134": "protein-disulfide reductase [NAD(P)H] activity",
    "GO:0050660": "flavin adenine dinucleotide binding",
    "GO:0055085": "transmembrane transport",
    "GO:0070069": "cytochrome complex",
}

PROFILE: dict[str, dict[str, Any]] = {
    "dsbB2": {
        "class": "dsbb",
        "group": "DsbB membrane disulfide-formation oxidoreductases",
        "primary": "GO:0015035",
        "processes": ["GO:0006457"],
        "locations": ["GO:0005886"],
        "description": "dsbB2 encodes an inner-membrane DsbB-family oxidoreductase that reoxidizes periplasmic DsbA-family proteins during disulfide-bond formation and transfers electrons into the quinone/electron-transfer chain.",
        "needles": ["Required for disulfide bond formation", "Belongs to the DsbB family", "KW   Electron transport"],
    },
    "PP_0251": {
        "class": "pap2_hpo_membrane",
        "group": "Low-information membrane redox/enzyme side nodes",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_0251 encodes a multi-pass membrane protein with a PAP2/haloperoxidase-domain signature, but no GOA-supported catalytic substrate or pathway assignment in this first pass.",
        "needles": ["PAP2/HPO.", "KW   Membrane", "FT   TRANSMEM"],
    },
    "trx": {
        "class": "thioredoxin",
        "group": "Thioredoxin and glutaredoxin soluble redox proteins",
        "primary": "GO:0015035",
        "processes": ["GO:0045454"],
        "locations": ["GO:0005737"],
        "description": "trx encodes a cytoplasmic thioredoxin-family redox protein that reduces protein disulfides and contributes to cellular redox homeostasis.",
        "needles": ["Belongs to the thioredoxin family", "Thioredoxin.", "KW   Redox-active center"],
    },
    "dsbD-I": {
        "class": "dsbd",
        "group": "DsbD membrane thiol-disulfide reductases",
        "primary": "GO:0047134",
        "processes": ["GO:0017004", "GO:0045454"],
        "locations": ["GO:0005886"],
        "description": "dsbD-I encodes an inner-membrane DsbD thiol-disulfide interchange protein that transfers reducing equivalents across the membrane for periplasmic disulfide isomerization and c-type cytochrome maturation.",
        "needles": ["Required to facilitate the formation of correct disulfide", "Belongs to the thioredoxin family. DsbD subfamily", "Cyt_c_assmbl_TM_dom"],
    },
    "dsbB1": {
        "class": "dsbb",
        "group": "DsbB membrane disulfide-formation oxidoreductases",
        "primary": "GO:0015035",
        "processes": ["GO:0006457"],
        "locations": ["GO:0005886"],
        "description": "dsbB1 encodes an inner-membrane DsbB-family oxidoreductase that reoxidizes periplasmic DsbA-family proteins during disulfide-bond formation and transfers electrons into the quinone/electron-transfer chain.",
        "needles": ["Required for disulfide bond formation", "Belongs to the DsbB family", "KW   Electron transport"],
    },
    "PP_1093": {
        "class": "rnf_nqr_membrane",
        "group": "Rnf/Nqr membrane ion-translocating oxidoreductase subunits",
        "primary": None,
        "processes": ["GO:0022900"],
        "locations": ["GO:0005886"],
        "description": "PP_1093 encodes an NqrDE/RnfAE-family multi-pass membrane subunit of an Rnf/Nqr-like ion-translocating oxidoreductase complex.",
        "needles": ["Electron transport complex protein", "NqrDE/RnfAE", "KW   Translocase"],
    },
    "rnfG": {
        "class": "rnf_fmn",
        "group": "Rnf/Nqr membrane ion-translocating oxidoreductase subunits",
        "primary": "GO:0009055",
        "processes": ["GO:0022900"],
        "locations": ["GO:0005886"],
        "description": "rnfG encodes the FMN-binding RnfG subunit of a membrane-bound ion-translocating oxidoreductase complex that couples electron transfer to ion translocation.",
        "needles": ["Part of a membrane-bound complex that couples electron", "Belongs to the RnfG family", "Ion_transpt_RnfG/RsxG"],
    },
    "rnfD": {
        "class": "rnf_nqr_membrane",
        "group": "Rnf/Nqr membrane ion-translocating oxidoreductase subunits",
        "primary": None,
        "processes": ["GO:0022900", "GO:0055085"],
        "locations": ["GO:0005886"],
        "description": "rnfD encodes a multi-pass RnfD/NqrB-family subunit of a membrane-bound ion-translocating oxidoreductase complex.",
        "needles": ["Part of a membrane-bound complex that couples electron", "Belongs to the NqrB/RnfD family", "NqrB/RnfD"],
    },
    "PP_1096": {
        "class": "rnf_nqr_membrane",
        "group": "Rnf/Nqr membrane ion-translocating oxidoreductase subunits",
        "primary": None,
        "processes": ["GO:0022900"],
        "locations": ["GO:0005886"],
        "description": "PP_1096 encodes an NqrDE/RnfAE-family multi-pass membrane subunit of an Rnf/Nqr-like ion-translocating oxidoreductase complex.",
        "needles": ["Electron transport complex protein", "NqrDE/RnfAE", "Rnf-Nqr"],
    },
    "PP_1460": {
        "class": "hemx_ypjd",
        "group": "Cytochrome c maturation proteins",
        "primary": None,
        "processes": ["GO:0017004"],
        "locations": ["GO:0005886"],
        "description": "PP_1460 encodes a YpjD/HemX-family membrane protein with a cytochrome-c assembly domain, curated as cytochrome-complex assembly context rather than a defined transporter.",
        "needles": ["Cyt_c_assembly", "YpjD/HemX", "Cytochrom_C_asm"],
    },
    "grx": {
        "class": "glutaredoxin",
        "group": "Thioredoxin and glutaredoxin soluble redox proteins",
        "primary": "GO:0015038",
        "processes": ["GO:0045454", "GO:0034599"],
        "locations": ["GO:0005737"],
        "description": "grx encodes a cytoplasmic glutaredoxin-family redox protein with glutathione-disulfide oxidoreductase activity in cellular redox homeostasis and oxidative-stress response.",
        "needles": ["Has a glutathione-disulfide oxidoreductase activity", "Belongs to the glutaredoxin family", "Glutaredoxin."],
    },
    "PP_3338": {
        "class": "cytochrome_bd",
        "group": "Membrane respiratory cytochrome oxidase subunits",
        "primary": "GO:0016682",
        "processes": ["GO:0019646"],
        "locations": ["GO:0005886"],
        "description": "PP_3338 encodes a membrane cytochrome bd-type quinol oxidase subunit associated with aerobic respiratory electron transfer.",
        "needles": ["Cytochrome bd-type quinol oxidase", "cytochrome ubiquinol oxidase subunit 2", "Cyt-d_oxidase_su2"],
    },
    "qhnDH": {
        "class": "qhamdh_gamma",
        "group": "Quinohemoprotein amine dehydrogenase redox subunits",
        "primary": "GO:0030058",
        "processes": [],
        "locations": ["GO:0042597"],
        "description": "qhnDH encodes the periplasmic CTQ-bearing gamma subunit of quinohemoprotein amine dehydrogenase, providing the redox catalytic center for aliphatic amine oxidation in the assembled holoenzyme.",
        "needles": ["Quinohemoprotein amine dehydrogenase subunit gamma", "QH-AmDH_gsu_dom", "SUBCELLULAR LOCATION: Periplasm"],
        "skip_gene_rewrite": True,
    },
    "etfA": {
        "class": "etf",
        "group": "Electron transfer flavoprotein carrier subunits",
        "primary": "GO:0009055",
        "processes": ["GO:0033539"],
        "locations": ["GO:0005737"],
        "description": "etfA encodes the alpha subunit of electron transfer flavoprotein, a soluble flavoprotein carrier that accepts electrons from dehydrogenases such as acyl-CoA dehydrogenases and relays them to downstream oxidoreductases.",
        "needles": ["The electron transfer flavoprotein serves as a specific", "Belongs to the ETF alpha-subunit/FixB family", "ETF_a/FixB"],
    },
    "etfB": {
        "class": "etf",
        "group": "Electron transfer flavoprotein carrier subunits",
        "primary": "GO:0009055",
        "processes": [],
        "locations": ["GO:0005737"],
        "description": "etfB encodes the beta subunit of electron transfer flavoprotein, a soluble flavoprotein electron carrier paired with EtfA.",
        "needles": ["Belongs to the ETF beta-subunit/FixA family", "ETF_b.", "ET-Flavoprotein_bsu_CS"],
    },
    "dsbD-II": {
        "class": "dsbd",
        "group": "DsbD membrane thiol-disulfide reductases",
        "primary": "GO:0047134",
        "processes": ["GO:0017004", "GO:0045454"],
        "locations": ["GO:0005886"],
        "description": "dsbD-II encodes an inner-membrane DsbD thiol-disulfide interchange protein that transfers reducing equivalents across the membrane for periplasmic disulfide isomerization and c-type cytochrome maturation.",
        "needles": ["Required to facilitate the formation of correct disulfide", "Belongs to the thioredoxin family. DsbD subfamily", "Cyt_c_assmbl_TM_dom"],
    },
    "PP_4236": {
        "class": "dsbe_lgt_fusion",
        "group": "DsbE/Lgt membrane redox-lipoprotein biogenesis proteins",
        "primary": "GO:0008961",
        "processes": ["GO:0042158", "GO:0045454"],
        "locations": ["GO:0030313"],
        "description": "PP_4236 encodes a membrane protein with Lgt and DsbE/redoxin signatures, supporting lipoprotein diacylglyceryl transferase context plus a cell-envelope redox-homeostasis role.",
        "needles": ["Thiol:disulfide interchange protein dsbE", "Lgt.", "Redoxin."],
    },
    "PP_4260": {
        "class": "fixh",
        "group": "Low-information membrane redox/enzyme side nodes",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_4260 encodes a single-pass FixH-family membrane protein; no GOA-supported molecular function or process was available in this first pass.",
        "needles": ["FixH family protein", "FixH.", "KW   Membrane"],
    },
    "ccoS": {
        "class": "ccos",
        "group": "Cytochrome oxidase maturation proteins",
        "primary": None,
        "processes": ["GO:0017004"],
        "locations": ["GO:0016020"],
        "description": "ccoS encodes a membrane cbb3-type cytochrome oxidase maturation protein with a FixS/cytochrome-oxidase-maturation domain.",
        "needles": ["Cytochrome oxidase maturation protein, cbb3-type", "Cyt_oxidase_maturation_cbb3", "FixS"],
    },
    "cycH": {
        "class": "ccm",
        "group": "Cytochrome c maturation proteins",
        "primary": None,
        "processes": ["GO:0017004"],
        "locations": ["GO:0030313"],
        "description": "cycH encodes a cell-envelope cytochrome c-type biogenesis protein with CcmI/CycH domains, curated as cytochrome-complex maturation context.",
        "needles": ["Cytochrome c-type biogenesis protein", "C-type_cytochrome_biogenesis", "Cyt_c_biogenesis_CcmI"],
    },
    "ccmF": {
        "class": "ccmf",
        "group": "Cytochrome c maturation proteins",
        "primary": "GO:0015232",
        "processes": ["GO:0015886", "GO:0017004"],
        "locations": ["GO:0005886"],
        "description": "ccmF encodes an inner-membrane holocytochrome c synthetase/CcmF-family component required for c-type cytochrome biogenesis and heme handling during cytochrome c maturation.",
        "needles": ["Required for the biogenesis of c-type cytochromes", "Belongs to the CcmF/CycK/Ccl1/NrfE/CcsA family", "Cyt_c_biogenesis_CcmF"],
    },
    "grxC": {
        "class": "glutaredoxin",
        "group": "Thioredoxin and glutaredoxin soluble redox proteins",
        "primary": "GO:0015038",
        "processes": ["GO:0045454", "GO:0034599"],
        "locations": ["GO:0005737"],
        "description": "grxC encodes a cytoplasmic glutaredoxin-family redox protein with glutathione-disulfide oxidoreductase activity in cellular redox homeostasis and oxidative-stress response.",
        "needles": ["Has a glutathione-disulfide oxidoreductase activity", "Belongs to the glutaredoxin family", "Glutaredoxin."],
    },
    "trxC": {
        "class": "thioredoxin",
        "group": "Thioredoxin and glutaredoxin soluble redox proteins",
        "primary": "GO:0015035",
        "processes": ["GO:0045454"],
        "locations": ["GO:0005737"],
        "description": "trxC encodes a thioredoxin-family redox protein that reduces protein disulfides and contributes to cellular redox homeostasis.",
        "needles": ["Thioredoxin 2", "Thioredoxin-like_sf", "Thioredoxin_domain"],
    },
    "trxA": {
        "class": "thioredoxin",
        "group": "Thioredoxin and glutaredoxin soluble redox proteins",
        "primary": "GO:0015035",
        "processes": ["GO:0045454"],
        "locations": ["GO:0005737"],
        "description": "trxA encodes a thioredoxin-family redox protein that reduces protein disulfides and contributes to cellular redox homeostasis.",
        "needles": ["Belongs to the thioredoxin family", "Thioredoxin.", "KW   Redox-active center"],
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


def existing_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    go_id = ann["term"]["id"]
    label = ann["term"]["label"]
    cls = info["profile"]["class"]
    primary = info["profile"].get("primary")

    if go_id == "GO:0005886":
        return review(info, "Plasma-membrane localization is appropriate for this bacterial membrane redox or maturation protein.", "ACCEPT", "UniProt membrane/transmembrane evidence and GOA localization support the inner/plasma membrane context.")
    if go_id == "GO:0016020":
        if "GO:0005886" in info.get("go_ids", []):
            return review(info, "Generic membrane localization is true but less informative than the plasma-membrane annotation.", "MARK_AS_OVER_ANNOTATED", "A more specific plasma-membrane annotation is also present.")
        return review(info, "Membrane localization is appropriate for this predicted transmembrane protein.", "ACCEPT", "UniProt transmembrane/keyword evidence supports membrane localization.")
    if go_id in {"GO:0005737", "GO:0005829", "GO:0030313", "GO:0042597"}:
        return review(info, f"{label} localization is appropriate but secondary to the redox, maturation, or enzyme role.", "KEEP_AS_NON_CORE", "The location supports the functional context but is not the core molecular activity.")
    if go_id in {"GO:0010181", "GO:0020037", "GO:0050660", "GO:0070069"}:
        return review(info, f"{label} is retained as cofactor, heme, or complex context rather than the core activity.", "KEEP_AS_NON_CORE", "The core role is better captured by electron transfer, oxidoreductase activity, cytochrome maturation, or heme handling.")

    if go_id == "GO:0006457":
        return review(info, "Protein folding is appropriate process context for DsbB-mediated oxidative protein folding.", "ACCEPT", "DsbB-family proteins drive disulfide-bond formation in periplasmic proteins via DsbA redox cycling.")
    if go_id == "GO:0015035":
        return review(info, f"{label} is appropriate for the thioredoxin/Dsb redox role.", "ACCEPT", "Product, family, and domain evidence support protein-disulfide redox chemistry.")
    if go_id == "GO:0015036":
        return review(info, f"{label} is appropriate redox context for this DsbD/thioredoxin-family protein.", "ACCEPT", "The redoxin/thioredoxin-domain evidence supports disulfide oxidoreductase activity.")
    if go_id == "GO:0047134":
        return review(info, "Protein-disulfide reductase (NAD(P)H) activity is the most specific DsbD molecular-function annotation in GOA.", "ACCEPT", "DsbD-family proteins transfer reducing equivalents across the membrane for periplasmic disulfide isomerization and cytochrome maturation.")
    if go_id == "GO:0009055":
        return review(info, f"{label} is appropriate for this electron-transfer or disulfide-redox protein.", "ACCEPT", "The product/domain context and GOA agree on redox electron transfer.")
    if go_id == "GO:0045454":
        return review(info, "Cell redox homeostasis is appropriate process context for this thioredoxin, glutaredoxin, DsbD, or DsbE-like redox protein.", "ACCEPT", "The redoxin/glutaredoxin/disulfide-redox role contributes to cellular redox balance.")
    if go_id == "GO:0017004":
        return review(info, "Cytochrome complex assembly is appropriate for this DsbD/Ccm/CycH/HemX cytochrome maturation context.", "ACCEPT", "The product or domain context supports c-type cytochrome or cytochrome oxidase maturation.")

    if go_id == "GO:0003824":
        return review(info, "Generic catalytic activity is true but too broad for glutaredoxin.", "MARK_AS_OVER_ANNOTATED", "Glutathione disulfide oxidoreductase activity captures the core activity more precisely.", ["GO:0015038"])
    if go_id == "GO:0015038":
        return review(info, "Glutathione disulfide oxidoreductase activity is the core glutaredoxin molecular function.", "ACCEPT", "UniProt and GOA support glutaredoxin-family glutathione-disulfide redox chemistry.")
    if go_id == "GO:0034599":
        return review(info, "Cellular response to oxidative stress is appropriate process context for glutaredoxin redox homeostasis.", "ACCEPT", "Glutaredoxin activity supports oxidative-stress redox buffering.")

    if go_id == "GO:0022900":
        return review(info, "Electron transport chain is appropriate process context for this Rnf/Nqr or electron-transfer protein.", "ACCEPT", "The Rnf/Nqr family or electron-transfer carrier context supports electron-transport-chain involvement.")
    if go_id == "GO:0055085":
        return review(info, "Transmembrane transport is broad but appropriate for the ion-translocating Rnf/Nqr membrane complex context.", "ACCEPT", "Rnf/Nqr complexes couple electron transfer to membrane ion translocation, although the exact transported ion is not specified here.")

    if go_id == "GO:0016682":
        return review(info, "This oxidoreductase term is appropriate for the cytochrome bd-type quinol oxidase subunit context.", "ACCEPT", "Cytochrome bd-type quinol oxidase transfers electrons from quinol/diphenol-like donors to oxygen in aerobic respiration.")
    if go_id == "GO:0019646":
        return review(info, "Aerobic electron transport chain is appropriate process context for cytochrome bd oxidase.", "ACCEPT", "The cytochrome bd-type quinol oxidase product/domain context supports aerobic respiratory electron transfer.")

    if go_id == "GO:0033539":
        return review(info, "Fatty-acid beta-oxidation using acyl-CoA dehydrogenase is appropriate process context for EtfA.", "ACCEPT", "Electron transfer flavoprotein accepts electrons from acyl-CoA dehydrogenases during beta-oxidation.")
    if go_id == "GO:0046395":
        return review(info, "Carboxylic acid catabolic process is retained as broad metabolic context for EtfB.", "KEEP_AS_NON_CORE", "The core role is electron transfer by the ETF carrier rather than a specific catabolic pathway assignment.")

    if go_id == "GO:0008961":
        return review(info, "Phosphatidylglycerol-prolipoprotein diacylglyceryl transferase activity is supported by the Lgt domain in this membrane protein.", "ACCEPT", "The protein carries an Lgt signature in addition to redoxin/DsbE context, so the lipoprotein-biogenesis activity is retained in this first pass.")
    if go_id == "GO:0042158":
        return review(info, "Lipoprotein biosynthetic process is appropriate process context for the Lgt-domain assignment.", "ACCEPT", "The Lgt domain supports prolipoprotein diacylglyceryl-transferase function in lipoprotein biogenesis.")
    if go_id == "GO:0016491":
        if cls == "dsbe_lgt_fusion":
            return review(info, "Generic oxidoreductase activity is true but less specific than the DsbE/redoxin disulfide-redox annotation.", "MARK_AS_OVER_ANNOTATED", "Disulfide oxidoreductase activity is the more informative redox term for the redoxin domain.", ["GO:0015036"])
        return review(info, "Generic oxidoreductase activity is broad but consistent with the redox context.", "KEEP_AS_NON_CORE", "The specific electron-transfer or disulfide-redox role is more informative.")

    if go_id == "GO:0015232":
        return review(info, "Heme transmembrane transporter activity is appropriate CcmF heme-handling context.", "ACCEPT", "CcmF-family proteins are membrane components of c-type cytochrome maturation and heme delivery.")
    if go_id == "GO:0015886":
        return review(info, "Heme transport is appropriate process context for CcmF-mediated heme handling in cytochrome c maturation.", "ACCEPT", "The CcmF family and heme-transporter GOA annotation support this process.")

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
                f"Adds {TERMS[primary]} for this redox or maturation protein.",
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


def curate_gene(row: dict[str, str]) -> GeneInfo:
    info = load_info(row)
    if info["profile"].get("skip_gene_rewrite"):
        return info
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
            "question": "What are the direct electron donor, electron acceptor, membrane partner, cofactor occupancy, and physiological condition for this KT2440 redox or maturation protein?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Test targeted mutants and purified proteins for electron-transfer partners, redox/cofactor content, membrane-complex association, and condition-specific phenotypes under respiratory shift, oxidative stress, cytochrome maturation demand, or envelope redox stress as appropriate.",
            "experiment_type": "redox biochemistry and condition-specific genetics",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    annoton: dict[str, Any] = {
        "id": f"{gene}_redox_electron_transfer_context",
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
                    "module_type": "TRANSPORT_STEP",
                    "description": f"First-pass membrane redox/electron-transfer subgroup: {group}.",
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
        concepts.append(descriptor(go_id, "Concept used for first-pass membrane redox/electron-transfer curation."))

    evidence = doc.setdefault("evidence", [])
    source_id = f"file:{BATCH_PATH.relative_to(ROOT)}"
    if not any(item.get("source_id") == source_id for item in evidence):
        evidence.append(
            {
                "source_id": source_id,
                "title": "PSEPK transport-bucket membrane redox/electron-transfer batch",
                "statement": "The batch table records 24 PSEPK transport/membrane/efflux-bucket genes assigned to Dsb, thioredoxin/glutaredoxin, Rnf/Nqr, ETF, cytochrome bd, Ccm/Cco, and low-information membrane redox/enzyme contexts.",
            }
        )
    doc["description"] = (
        "Boundary module for PSEPK cytochromes, ferredoxins, blue-copper electron carriers, Dsb/thioredoxin/glutaredoxin redox proteins, "
        "Rnf/Nqr ion-translocating oxidoreductase components, ETF electron carriers, cytochrome c/oxidase maturation proteins, MsrQ/Hmp redox "
        "detoxification nodes, and related membrane redox/enzyme side nodes pulled into transport buckets by metal-binding, heme, iron-sulfur, "
        "membrane, or electron-transport evidence."
    )
    doc["notes"] = (
        "First-pass interpretation: treat this as a boundary/spillover module, not a single canonical pathway. "
        "Specific electron-transfer, disulfide-redox, glutaredoxin/thioredoxin, ion-translocating Rnf/Nqr, ETF carrier, cytochrome-maturation, "
        "heme-handling, iron-transport, nitric-oxide-detoxification, protein-repair, and multicopper-oxidase calls are retained where product/family "
        "and GOA agree; broad metal/heme/FAD/Fe-S binding and low-information membrane terms are kept as supporting context rather than standalone core functions."
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
