#!/usr/bin/env python3
"""First-pass curation for the transport residual generic ABC split."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = ROOT / "projects/P_PUTIDA/batches/module_transport_membrane_efflux_generic_abc_transporters.tsv"
MODULE_PATH = ROOT / "modules/generic_abc_transport_boundary.yaml"

TAXON = {
    "id": "NCBITaxon:160488",
    "label": "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)",
}

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on inter-ontology links",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0000166": "nucleotide binding",
    "GO:0003333": "amino acid transmembrane transport",
    "GO:0005524": "ATP binding",
    "GO:0005886": "plasma membrane",
    "GO:0006865": "amino acid transport",
    "GO:0009228": "thiamine biosynthetic process",
    "GO:0010438": "cellular response to sulfur starvation",
    "GO:0015421": "ABC-type oligopeptide transporter activity",
    "GO:0015424": "ABC-type amino acid transporter activity",
    "GO:0015889": "cobalamin transport",
    "GO:0016020": "membrane",
    "GO:0016887": "ATP hydrolysis activity",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0030313": "cell envelope",
    "GO:0031419": "cobalamin binding",
    "GO:0034040": "ATPase-coupled lipid transmembrane transporter activity",
    "GO:0042626": "ATPase-coupled transmembrane transporter activity",
    "GO:0042918": "alkanesulfonate transmembrane transport",
    "GO:0043190": "ATP-binding cassette (ABC) transporter complex",
    "GO:0055085": "transmembrane transport",
    "GO:0071111": "cyclic-guanylate-specific phosphodiesterase activity",
    "GO:0071732": "cellular response to nitric oxide",
    "GO:0090374": "oligopeptide export from mitochondrion",
    "GO:0120010": "intermembrane phospholipid transfer",
    "GO:0140359": "ABC-type transporter activity",
    "GO:1902495": "transmembrane transporter complex",
}


def term(go_id: str) -> dict[str, str]:
    return {"id": go_id, "label": TERMS[go_id]}


def ref_file(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def load_rows() -> list[dict[str, str]]:
    with BATCH_PATH.open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def first_de_line(lines: list[str]) -> str:
    for line in lines:
        if line.startswith("DE   RecName") or line.startswith("DE   SubName"):
            return line
    for line in lines:
        if line.startswith("DE   "):
            return line
    raise ValueError("No UniProt DE line found")


def first_line(lines: list[str], needle: str, optional: bool = False) -> str | None:
    for line in lines:
        if needle in line:
            return line
    if optional:
        return None
    raise ValueError(f"Could not find {needle!r}")


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


CATEGORY = {
    "PP_0386": "c_di_gmp_pde",
    "PP_0506": "macb_permease",
    "PP_0507": "macb_atpase",
    "PP_1737": "mlaA",
    "PP_1760": "fused_abcb_exporter",
    "yadG": "generic_atpase",
    "PP_2119": "fused_abcb_exporter",
    "PP_2316": "macb_permease",
    "ybbA": "macb_atpase",
    "PP_2418": "cobalamin_binding",
    "PP_2578": "transport_aux_lipoprotein",
    "PP_2668": "generic_atpase",
    "PP_3210": "bp_dependent_permease",
    "PP_3211": "generic_atpase",
    "PP_3213": "thi5_like",
    "PP_3466": "fused_abcb_exporter",
    "PP_3597": "amino_acid_atpase",
    "PP_3635": "sulfonate_permease",
    "PP_3636": "sulfonate_binding",
    "PP_3637": "sulfonate_atpase",
    "PP_3733": "macb_aux_lipoprotein",
    "PP_3734": "macb_permease",
    "PP_3735": "macb_atpase",
    "PP_3954": "c4_dicarboxylate_binding",
    "PP_4172": "substrate_binding",
    "PP_4425": "amino_acid_atpase",
    "hmuV": "hemin_atpase",
    "PP_4911": "transport_aux_lipoprotein",
    "glnQ": "amino_acid_atpase",
    "rbbA": "ribosome_associated_atpase",
    "PP_5538": "amino_acid_binding",
    "PP_5668": "abc2_permease",
    "PP_5669": "abc2_atpase",
}

GROUP = {
    "c_di_gmp_pde": "Transport-bucket outliers",
    "mlaA": "Transport-bucket outliers",
    "thi5_like": "Transport-bucket outliers",
    "ribosome_associated_atpase": "Transport-bucket outliers",
    "macb_permease": "ABC-3/MacB-like efflux or export components",
    "macb_atpase": "ABC-3/MacB-like efflux or export components",
    "macb_aux_lipoprotein": "ABC-3/MacB-like efflux or export components",
    "abc2_permease": "ABC-2/various-function transporter pair",
    "abc2_atpase": "ABC-2/various-function transporter pair",
    "fused_abcb_exporter": "Fused ABCB/type-I-exporter-like transporters",
    "generic_atpase": "Generic unresolved ABC ATPase components",
    "transport_aux_lipoprotein": "Generic unresolved ABC auxiliary lipoproteins",
    "bp_dependent_permease": "Binding-protein-dependent importer candidates",
    "cobalamin_binding": "Binding-protein-dependent importer candidates",
    "c4_dicarboxylate_binding": "Binding-protein-dependent importer candidates",
    "substrate_binding": "Binding-protein-dependent importer candidates",
    "amino_acid_binding": "Binding-protein-dependent importer candidates",
    "amino_acid_atpase": "Amino-acid ABC ATPase spillover",
    "sulfonate_permease": "Sulfonate ABC importer candidate",
    "sulfonate_binding": "Sulfonate ABC importer candidate",
    "sulfonate_atpase": "Sulfonate ABC importer candidate",
    "hemin_atpase": "Heme/hemin ABC importer spillover",
}


class GeneInfo(dict[str, Any]):
    gene: str


def load_info(row: dict[str, str]) -> GeneInfo:
    gene = row["gene"]
    uniprot_path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    asta_path = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    review_path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    uniprot_lines = uniprot_path.read_text(encoding="utf-8").splitlines()
    asta_lines = asta_path.read_text(encoding="utf-8").splitlines()
    review_doc = yaml.safe_load(review_path.read_text(encoding="utf-8"))
    info = GeneInfo(
        gene=gene,
        accession=row["uniprot_accession"],
        product=row["protein_name"],
        category=CATEGORY[gene],
        group=GROUP[CATEGORY[gene]],
        uniprot_lines=uniprot_lines,
        asta_lines=asta_lines,
        go_ids=[ann["term"]["id"] for ann in review_doc.get("existing_annotations", [])],
        existing_refs={ref["id"]: ref for ref in review_doc.get("references", []) if "id" in ref},
    )
    info["de"] = first_de_line(uniprot_lines)
    info["asta_product"] = first_line(asta_lines, "- **Protein Description:**")
    return info


SUPPORT_NEEDLES = {
    "c_di_gmp_pde": ["EAL_dom", "GGDEF_dom", "KW   c-di-GMP"],
    "mlaA": ["Belongs to the MlaA family", "DR   InterPro; IPR007428; MlaA."],
    "thi5_like": ["NMT1/THI5", "SsuA/THI5"],
    "ribosome_associated_atpase": ["ABC2_perm_RbbA", "ABC2_TM", "ABC_transporter-like_ATP-bd"],
    "macb_permease": ["ABC3_permease_C", "MacB_PCD"],
    "macb_atpase": ["ABC_transporter-like_ATP-bd", "MacB-like_ATP-bd"],
    "macb_aux_lipoprotein": ["AttH_dom", "Lipoprotein"],
    "abc2_permease": ["Membrane", "Transmembrane"],
    "abc2_atpase": ["ABC_transporter-like_ATP-bd", "ABC_Transporter_VariousFunc"],
    "fused_abcb_exporter": ["ABC1_TM_dom", "ABC_transporter-like_ATP-bd", "Type_1_exporter"],
    "generic_atpase": ["ABC_transporter-like_ATP-bd", "P-loop_NTPase"],
    "transport_aux_lipoprotein": ["ABC_trans_aux"],
    "bp_dependent_permease": ["MetI-like", "BPD_transp_1"],
    "cobalamin_binding": ["ABC_Transporter_SBP", "ABC_transptr_periplasmic_BD"],
    "c4_dicarboxylate_binding": ["TRAP_TAXI", "NMT1_3"],
    "substrate_binding": ["ABC_transpt-TYRBP-like"],
    "amino_acid_binding": ["BCAA_transport", "Leu-bd"],
    "amino_acid_atpase": ["MetN_ABC_transporter-like", "Amino-acid transport"],
    "sulfonate_permease": ["MetI-like", "BPD_transp_1"],
    "sulfonate_binding": ["NrtA/CpmA_ABC-bd_dom", "TAT_signal"],
    "sulfonate_atpase": ["ABC_transporter-like_ATP-bd", "ABC_transporter_ATP-bind"],
    "hemin_atpase": ["Part of the ABC transporter complex HmuTUV involved in hemin", "Heme (hemin)"],
}


def base_support(info: GeneInfo, extra_needles: list[str] | None = None) -> list[dict[str, str]]:
    gene = info["gene"]
    out = [
        support(ref_file(gene, "uniprot.txt"), info["de"]),
        support(ref_file(gene, "deep-research-asta.md"), info["asta_product"]),
    ]
    for needle in [*(SUPPORT_NEEDLES.get(info["category"], [])), *(extra_needles or [])]:
        line = first_line(info["uniprot_lines"], needle, optional=True)
        if line:
            out.append(support(ref_file(gene, "uniprot.txt"), line))
    return dedupe(out)


def goa_support(info: GeneInfo, go_id: str, label: str) -> dict[str, str]:
    return support(ref_file(info["gene"], "goa.tsv"), f"{go_id}\t{label}")


def replacement(go_id: str) -> list[dict[str, str]]:
    return [term(go_id)]


def review(
    info: GeneInfo,
    summary: str,
    action: str,
    reason: str,
    replacement_ids: list[str] | None = None,
    extra_needles: list[str] | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": base_support(info, extra_needles),
    }
    if replacement_ids:
        item["proposed_replacement_terms"] = [term(go_id) for go_id in replacement_ids]
    return item


def default_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    go_id = ann["term"]["id"]
    label = ann["term"]["label"]
    category = info["category"]
    if go_id == "GO:0000166":
        return review(
            info,
            "Nucleotide binding is true but less specific than ATP binding for an ABC-family ATPase.",
            "MODIFY",
            "The protein carries ABC/P-loop ATP-binding features; ATP binding is the more informative nucleotide-binding term.",
            ["GO:0005524"],
        )
    if go_id == "GO:0005524":
        return review(
            info,
            "ATP binding is supported but is less informative than ATP hydrolysis or transporter-component function.",
            "KEEP_AS_NON_CORE",
            "The ABC ATP-binding domain supports ATP binding, but ATP hydrolysis better captures the energy-coupling chemistry.",
        )
    if go_id == "GO:0016887":
        return review(
            info,
            "ATP hydrolysis activity is appropriate for the ABC ATPase component.",
            "ACCEPT",
            "The ABC transporter ATP-binding and P-loop features support ATP hydrolysis as the conserved energy-coupling activity.",
        )
    if go_id == "GO:0005886":
        if category == "c_di_gmp_pde":
            return review(
                info,
                "Plasma membrane localization is appropriate for this membrane-associated c-di-GMP signaling protein.",
                "ACCEPT",
                "UniProt predicts membrane association for this EAL/GGDEF-domain c-di-GMP phosphodiesterase.",
            )
        return review(
            info,
            "Plasma membrane localization is appropriate for this bacterial membrane transporter or transporter-associated component.",
            "ACCEPT",
            "The product and transporter-domain context support association with the bacterial cytoplasmic/plasma membrane transporter system.",
        )
    if go_id == "GO:0016020":
        action = "MARK_AS_OVER_ANNOTATED" if "GO:0005886" in info["go_ids"] else "KEEP_AS_NON_CORE"
        reason = (
            "A more specific plasma-membrane annotation is present, so generic membrane localization adds little."
            if action == "MARK_AS_OVER_ANNOTATED"
            else "Membrane association is plausible but is broad context rather than the core function."
        )
        return review(info, "Membrane localization is broad context for this transporter-associated protein.", action, reason)
    if go_id == "GO:0022857":
        action = "MARK_AS_OVER_ANNOTATED" if category == "ribosome_associated_atpase" else "ACCEPT"
        reason = (
            "RbbA is named as a ribosome-associated ATPase; the current metadata does not justify a transporter-activity assertion."
            if action == "MARK_AS_OVER_ANNOTATED"
            else "The product and transporter-domain evidence support broad transmembrane transporter activity while substrate remains unresolved."
        )
        return review(info, "Broad transmembrane transporter activity is reviewed against the component evidence.", action, reason)
    if go_id == "GO:0055085":
        if category == "ribosome_associated_atpase":
            return review(
                info,
                "Transmembrane transport is likely over-propagated for this ribosome-associated ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The product is named ribosome-associated ATPase, and current lightweight evidence does not establish a transported substrate.",
            )
        if category == "sulfonate_permease":
            return review(
                info,
                "Transmembrane transport is correct but broader than the sulfonate-transport annotation.",
                "MARK_AS_OVER_ANNOTATED",
                "The product names a sulfonate ABC permease, and GOA already provides alkanesulfonate transmembrane transport.",
                ["GO:0042918"],
            )
        return review(
            info,
            "Transmembrane transport is broad but defensible for this unresolved ABC transporter component.",
            "ACCEPT",
            "The transporter product/domain evidence supports transmembrane transport while the exact transported substrate remains unresolved.",
        )
    if go_id == "GO:0140359":
        action = "MARK_AS_OVER_ANNOTATED" if category == "ribosome_associated_atpase" else "ACCEPT"
        reason = (
            "The product is a ribosome-associated ATPase, so generic ABC-type transporter activity is not established as its core activity."
            if action == "MARK_AS_OVER_ANNOTATED"
            else "The fused membrane/ATPase ABC architecture supports generic ABC-type transporter activity, with substrate unresolved."
        )
        return review(info, "ABC-type transporter activity is reviewed at the broad component level.", action, reason)
    if go_id == "GO:0043190":
        action = "MARK_AS_OVER_ANNOTATED" if category == "ribosome_associated_atpase" else "KEEP_AS_NON_CORE"
        reason = (
            "Current metadata supports an ABC-like ribosome-associated ATPase, but not membership in a canonical ABC transporter complex."
            if action == "MARK_AS_OVER_ANNOTATED"
            else "ABC transporter complex membership is useful component context, but substrate and partner boundaries remain unresolved."
        )
        return review(info, "ABC transporter complex membership is broad component context.", action, reason)
    if go_id == "GO:1902495":
        return review(
            info,
            "Transmembrane transporter complex membership is broad context for this ABC ATPase component.",
            "KEEP_AS_NON_CORE",
            "The product and MacB-like ABC ATPase domains support transporter-system context, but the exact complex and substrate are unresolved.",
        )
    if go_id == "GO:0034040":
        return review(
            info,
            "Lipid-transporter activity is more specific than the current evidence supports.",
            "MODIFY",
            "The fused ABCB/type-I-exporter-like architecture supports ATPase-coupled ABC transport, but no lipid substrate is established.",
            ["GO:0140359"],
        )
    if go_id == "GO:0042626":
        return review(
            info,
            "ATPase-coupled transmembrane transporter activity is appropriate for this fused ABC membrane ATPase.",
            "ACCEPT",
            "The protein combines ABC ATPase and transmembrane transporter domains.",
        )
    if go_id == "GO:0015421":
        return review(
            info,
            "Oligopeptide transporter activity is too specific for the available fused ABCB-like evidence.",
            "MODIFY",
            "The current product and domain evidence support a broad ABC-type transporter, not a resolved oligopeptide substrate.",
            ["GO:0140359"],
        )
    if go_id == "GO:0090374":
        return review(
            info,
            "Mitochondrial oligopeptide export is not appropriate for this bacterial protein.",
            "REMOVE",
            "Pseudomonas putida lacks mitochondria, and the product/domain evidence does not support an oligopeptide-export role.",
            ["GO:0055085"],
        )
    if go_id == "GO:0015424":
        return review(
            info,
            "ABC-type amino-acid transporter activity is appropriate as component-level context for this amino-acid ABC ATPase.",
            "ACCEPT",
            "The product and UniProt keywords identify an amino-acid ABC transporter ATP-binding component.",
        )
    if go_id == "GO:0031419":
        return review(
            info,
            "Cobalamin binding is appropriate for the predicted periplasmic cobalamin ABC transporter component.",
            "ACCEPT",
            "The product name and periplasmic binding-protein domains support cobalamin-binding substrate-capture context.",
        )
    if go_id == "GO:0003333":
        return review(
            info,
            "Amino acid transmembrane transport is appropriate broad process context for this amino-acid ABC ATPase component.",
            "ACCEPT",
            "The product and UniProt amino-acid-transport keyword support amino-acid ABC transport context while exact substrate remains unresolved.",
        )
    if go_id == "GO:0042918":
        return review(
            info,
            "Alkanesulfonate transmembrane transport is appropriate for the sulfonate ABC permease.",
            "ACCEPT",
            "The product names a sulfonate ABC transporter permease and the local trio contains sulfonate-binding and ATPase partners.",
        )
    if go_id == "GO:0010438":
        return review(
            info,
            "Sulfur-starvation response is physiological context rather than the transporter component's core function.",
            "KEEP_AS_NON_CORE",
            "Sulfonate uptake can support sulfur-starvation adaptation, but the direct function of this gene product is transporter-component activity.",
        )
    if go_id == "GO:0009228":
        return review(
            info,
            "Thiamine biosynthetic process is retained for this SsuA/THI5-like protein.",
            "ACCEPT",
            "The NMT1/THI5 and SsuA/THI5 domain evidence supports thiamine-biosynthesis context rather than an ABC transporter role.",
        )
    if go_id == "GO:0071111":
        return review(
            info,
            "Cyclic-guanylate-specific phosphodiesterase activity is the core supported molecular function.",
            "ACCEPT",
            "The UniProt product name and EAL/GGDEF c-di-GMP signaling domain architecture support c-di-GMP phosphodiesterase activity.",
        )
    if go_id == "GO:0071732":
        return review(
            info,
            "Nitric-oxide response is not established as the core role from the lightweight evidence.",
            "MARK_AS_OVER_ANNOTATED",
            "The protein is best supported as a c-di-GMP signaling phosphodiesterase; the current evidence does not resolve nitric oxide as the stimulus.",
            ["GO:0071111"],
        )
    if go_id == "GO:0120010":
        return review(
            info,
            "Intermembrane phospholipid transfer is appropriate for the MlaA-family protein.",
            "ACCEPT",
            "The MlaA family/domain evidence supports envelope phospholipid-transfer context.",
        )
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
    category = info["category"]
    if category in {"macb_permease", "abc2_permease"} and "GO:0022857" not in info["go_ids"]:
        return [
            new_annotation(
                info,
                "GO:0022857",
                "contributes_to",
                "Adds broad transporter activity for the predicted ABC membrane permease component.",
                "The product/domain evidence supports an ABC-family membrane permease, but substrate specificity remains unresolved.",
            ),
            new_annotation(
                info,
                "GO:0055085",
                "involved_in",
                "Adds broad transmembrane-transport process context for the predicted ABC permease component.",
                "The protein is a predicted membrane component of an ABC transporter, with no resolved substrate.",
            ),
        ]
    if category in {"generic_atpase", "abc2_atpase"} and "GO:0016887" not in info["go_ids"]:
        return [
            new_annotation(
                info,
                "GO:0016887",
                "enables",
                "Adds ATP hydrolysis activity for the ABC ATPase component.",
                "The product/domain evidence supports a P-loop ABC ATPase, but no substrate-specific transporter activity.",
            )
        ]
    if category == "transport_aux_lipoprotein" and "GO:0022857" not in info["go_ids"]:
        return [
            new_annotation(
                info,
                "GO:0022857",
                "contributes_to",
                "Adds broad transporter contribution for the predicted ABC auxiliary lipoprotein component.",
                "The ABC transport auxiliary lipoprotein domain supports component-level transporter context, but no substrate is resolved.",
            )
        ]
    if category == "macb_aux_lipoprotein" and "GO:0022857" not in info["go_ids"]:
        return [
            new_annotation(
                info,
                "GO:0022857",
                "contributes_to",
                "Adds broad transporter contribution for the predicted lipoprotein component near MacB-like ABC transporter genes.",
                "The product name and adjacent MacB-like permease/ATPase context support transporter-associated component status.",
            )
        ]
    if category == "cobalamin_binding" and "GO:0031419" not in info["go_ids"]:
        return [
            new_annotation(
                info,
                "GO:0031419",
                "enables",
                "Adds cobalamin binding for the predicted periplasmic cobalamin ABC transporter component.",
                "The product name and periplasmic binding-protein domains support cobalamin-binding substrate-capture context.",
            )
        ]
    if category in {"c4_dicarboxylate_binding", "substrate_binding"} and "GO:0022857" not in info["go_ids"]:
        return [
            new_annotation(
                info,
                "GO:0022857",
                "contributes_to",
                "Adds broad transporter contribution for the predicted substrate-binding component.",
                "The current evidence supports a solute-binding transporter component, but not a resolved substrate-specific transporter term.",
            )
        ]
    if category == "sulfonate_binding" and "GO:0042918" not in info["go_ids"]:
        return [
            new_annotation(
                info,
                "GO:0042918",
                "involved_in",
                "Adds alkanesulfonate transport context for the sulfonate-binding component.",
                "The product identifies a periplasmic sulfonate-binding protein adjacent to sulfonate permease and ATPase components.",
            )
        ]
    if category == "sulfonate_atpase" and "GO:0042918" not in info["go_ids"]:
        return [
            new_annotation(
                info,
                "GO:0042918",
                "involved_in",
                "Adds alkanesulfonate transport context for the sulfonate ABC ATPase component.",
                "The ATPase is adjacent to sulfonate permease and binding-protein components.",
            )
        ]
    if category == "amino_acid_binding" and "GO:0015424" not in info["go_ids"]:
        return [
            new_annotation(
                info,
                "GO:0015424",
                "contributes_to",
                "Adds amino-acid ABC transporter contribution for the substrate-binding protein.",
                "The leucine/BCAA-binding family evidence supports amino-acid ABC importer component context.",
            )
        ]
    return []


def core_function(info: GeneInfo) -> dict[str, Any]:
    category = info["category"]
    support_lines = base_support(info)
    if category == "c_di_gmp_pde":
        return {
            "description": "Membrane-associated c-di-GMP signaling protein with cyclic-guanylate phosphodiesterase activity.",
            "molecular_function": term("GO:0071111"),
            "locations": [term("GO:0005886")],
            "supported_by": support_lines,
        }
    if category == "mlaA":
        return {
            "description": "MlaA-family envelope protein involved in intermembrane phospholipid transfer.",
            "directly_involved_in": [term("GO:0120010")],
            "locations": [term("GO:0016020")],
            "supported_by": support_lines,
        }
    if category == "thi5_like":
        return {
            "description": "SsuA/THI5-like protein associated with thiamine biosynthesis rather than ABC transport.",
            "directly_involved_in": [term("GO:0009228")],
            "supported_by": support_lines,
        }
    if category == "ribosome_associated_atpase":
        return {
            "description": "Ribosome-associated ABC-like ATPase; transporter substrate context is not established.",
            "molecular_function": term("GO:0016887"),
            "locations": [term("GO:0016020")],
            "supported_by": support_lines,
        }
    if category in {"fused_abcb_exporter"}:
        return {
            "description": "Fused ABCB/type-I-exporter-like membrane transporter of unresolved substrate specificity.",
            "molecular_function": term("GO:0140359"),
            "directly_involved_in": [term("GO:0055085")],
            "locations": [term("GO:0005886")],
            "supported_by": support_lines,
        }
    if category in {"macb_permease", "abc2_permease", "bp_dependent_permease"}:
        return {
            "description": "Membrane permease component of a predicted ABC-family transporter with unresolved substrate specificity.",
            "contributes_to_molecular_function": term("GO:0022857"),
            "directly_involved_in": [term("GO:0055085")],
            "locations": [term("GO:0005886")],
            "in_complex": term("GO:0043190"),
            "supported_by": support_lines,
        }
    if category in {"macb_atpase", "generic_atpase", "abc2_atpase"}:
        return {
            "description": "ATP-hydrolyzing component of an unresolved ABC-family transporter.",
            "molecular_function": term("GO:0016887"),
            "in_complex": term("GO:0043190"),
            "supported_by": support_lines,
        }
    if category in {"transport_aux_lipoprotein", "macb_aux_lipoprotein"}:
        return {
            "description": "Auxiliary lipoprotein-like component of an unresolved ABC-family transporter system.",
            "contributes_to_molecular_function": term("GO:0022857"),
            "in_complex": term("GO:0043190"),
            "supported_by": support_lines,
        }
    if category == "cobalamin_binding":
        return {
            "description": "Predicted cobalamin-binding component of an ABC importer.",
            "molecular_function": term("GO:0031419"),
            "directly_involved_in": [term("GO:0015889")],
            "locations": [term("GO:0030313")],
            "supported_by": support_lines,
        }
    if category in {"c4_dicarboxylate_binding", "substrate_binding"}:
        return {
            "description": "Predicted solute-binding component of an unresolved transporter system.",
            "contributes_to_molecular_function": term("GO:0022857"),
            "directly_involved_in": [term("GO:0055085")],
            "locations": [term("GO:0030313")],
            "supported_by": support_lines,
        }
    if category == "amino_acid_binding":
        return {
            "description": "Predicted amino-acid substrate-binding component of an ABC importer.",
            "contributes_to_molecular_function": term("GO:0015424"),
            "directly_involved_in": [term("GO:0006865")],
            "locations": [term("GO:0030313")],
            "supported_by": support_lines,
        }
    if category == "amino_acid_atpase":
        return {
            "description": "ATP-hydrolyzing component of an amino-acid ABC transporter.",
            "molecular_function": term("GO:0016887"),
            "contributes_to_molecular_function": term("GO:0015424"),
            "directly_involved_in": [term("GO:0003333")],
            "locations": [term("GO:0005886")],
            "in_complex": term("GO:0043190"),
            "supported_by": support_lines,
        }
    if category == "sulfonate_permease":
        return {
            "description": "Membrane permease component of a predicted alkanesulfonate ABC importer.",
            "contributes_to_molecular_function": term("GO:0022857"),
            "directly_involved_in": [term("GO:0042918")],
            "locations": [term("GO:0005886")],
            "in_complex": term("GO:0043190"),
            "supported_by": support_lines,
        }
    if category == "sulfonate_binding":
        return {
            "description": "Periplasmic sulfonate-binding component of a predicted alkanesulfonate ABC importer.",
            "contributes_to_molecular_function": term("GO:0022857"),
            "directly_involved_in": [term("GO:0042918")],
            "locations": [term("GO:0030313")],
            "supported_by": support_lines,
        }
    if category == "sulfonate_atpase":
        return {
            "description": "ATP-hydrolyzing component of a predicted alkanesulfonate ABC importer.",
            "molecular_function": term("GO:0016887"),
            "contributes_to_molecular_function": term("GO:0022857"),
            "directly_involved_in": [term("GO:0042918")],
            "in_complex": term("GO:0043190"),
            "supported_by": support_lines,
        }
    if category == "hemin_atpase":
        return {
            "description": "ATP-hydrolyzing HmuV component of a heme/hemin ABC importer.",
            "molecular_function": term("GO:0016887"),
            "directly_involved_in": [term("GO:0055085")],
            "locations": [term("GO:0005886")],
            "in_complex": term("GO:0043190"),
            "supported_by": support_lines,
        }
    raise ValueError(f"Unhandled category {category}")


def description(info: GeneInfo) -> str:
    gene = info["gene"]
    product = info["product"]
    category = info["category"]
    if category == "c_di_gmp_pde":
        return (
            f"{gene} encodes a large membrane-associated c-di-GMP signaling protein with EAL and GGDEF domains. "
            "The best-supported activity is cyclic-guanylate-specific phosphodiesterase activity; the sensor input is unresolved."
        )
    if category == "mlaA":
        return f"{gene} encodes an MlaA-family membrane protein implicated in intermembrane phospholipid transfer and envelope lipid asymmetry."
    if category == "thi5_like":
        return f"{gene} encodes an SsuA/THI5-like protein associated with thiamine biosynthesis; it is not supported as an ABC transporter component."
    if category == "ribosome_associated_atpase":
        return f"{gene} encodes a ribosome-associated ABC-like ATPase with membrane-spanning features; transported-substrate context is not established."
    if category == "hemin_atpase":
        return f"{gene} encodes HmuV, the ATP-binding energy-coupling component of a predicted HmuTUV heme/hemin ABC importer."
    if category in {"amino_acid_atpase", "amino_acid_binding"}:
        return f"{gene} encodes {product}, a predicted amino-acid ABC transporter component with unresolved exact substrate specificity."
    if category.startswith("sulfonate"):
        return f"{gene} encodes {product}, a component of a predicted alkanesulfonate ABC importer."
    if category == "cobalamin_binding":
        return f"{gene} encodes a predicted periplasmic cobalamin-binding component of an ABC importer."
    if category in {"c4_dicarboxylate_binding", "substrate_binding"}:
        return f"{gene} encodes {product}, a predicted solute-binding transporter component with unresolved partner transporter and substrate specificity."
    if category in {"transport_aux_lipoprotein", "macb_aux_lipoprotein"}:
        return f"{gene} encodes {product}, an auxiliary lipoprotein-like component associated with an unresolved ABC-family transporter context."
    if category in {"macb_permease", "macb_atpase"}:
        return f"{gene} encodes {product}, a MacB/ABC-3-like ABC transporter component with unresolved substrate specificity."
    if category in {"abc2_permease", "abc2_atpase"}:
        return f"{gene} encodes {product}, part of an ABC-2/various-function transporter pair with unresolved substrate specificity."
    if category == "fused_abcb_exporter":
        return f"{gene} encodes {product}, a fused ABCB/type-I-exporter-like membrane ATPase transporter with unresolved substrate specificity."
    return f"{gene} encodes {product}, an unresolved ABC-family transporter component."


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
        "findings": [{"supporting_text": info["asta_product"]}],
    }
    return list(refs.values())


def curate_gene(row: dict[str, str]) -> GeneInfo:
    info = load_info(row)
    gene = info["gene"]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    goa_annotations = [
        ann
        for ann in doc.get("existing_annotations", [])
        if ann.get("original_reference_id") != ref_file(gene, "uniprot.txt")
    ]
    info["go_ids"] = [ann["term"]["id"] for ann in goa_annotations]
    for ann in goa_annotations:
        ann["review"] = default_review(info, ann)
        ann["review"]["supported_by"].insert(0, goa_support(info, ann["term"]["id"], ann["term"]["label"]))
        ann["review"]["supported_by"] = dedupe(ann["review"]["supported_by"])
    doc["existing_annotations"] = goa_annotations + suggested_new_annotations(info)
    doc["description"] = description(info)
    doc["status"] = "COMPLETE"
    doc["references"] = references(info)
    core = core_function(info)
    reflected_ids = {
        ann["term"]["id"]
        for ann in doc["existing_annotations"]
        if (ann.get("review") or {}).get("action") in {"ACCEPT", "NEW"}
    }
    for slot in ("directly_involved_in", "locations"):
        if slot in core:
            core[slot] = [item for item in core[slot] if item["id"] in reflected_ids]
            if not core[slot]:
                core.pop(slot)
    if core.get("in_complex", {}).get("id") not in reflected_ids:
        core.pop("in_complex", None)
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "What are the transported substrate, partner subunits, and physiological conditions for this unresolved "
                "ABC-family or transport-bucket component in Pseudomonas putida KT2440?"
            )
        }
    ]
    if info["category"] in {"c_di_gmp_pde", "mlaA", "thi5_like", "ribosome_associated_atpase"}:
        doc["suggested_questions"] = [
            {
                "question": "Should this transport-bucket outlier be reassigned to a more specific non-ABC module after neighboring-gene and pathway-context review?"
            }
        ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Combine locus-neighborhood analysis with targeted deletion/complementation and substrate-uptake or stress-condition assays "
                "to resolve the transported substrate or non-transport physiological role."
            ),
            "experiment_type": "ABC transporter genetics and uptake/context assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_function_for(info: GeneInfo) -> str | None:
    category = info["category"]
    if category == "c_di_gmp_pde":
        return "GO:0071111"
    if category in {"fused_abcb_exporter"}:
        return "GO:0140359"
    if category in {"macb_permease", "abc2_permease", "bp_dependent_permease", "transport_aux_lipoprotein", "macb_aux_lipoprotein", "c4_dicarboxylate_binding", "substrate_binding", "sulfonate_permease", "sulfonate_binding"}:
        return "GO:0022857"
    if category in {"macb_atpase", "generic_atpase", "abc2_atpase", "amino_acid_atpase", "sulfonate_atpase", "hemin_atpase", "ribosome_associated_atpase"}:
        return "GO:0016887"
    if category == "cobalamin_binding":
        return "GO:0031419"
    if category == "amino_acid_binding":
        return "GO:0015424"
    return None


def module_processes_for(info: GeneInfo) -> list[str]:
    category = info["category"]
    if category == "mlaA":
        return ["GO:0120010"]
    if category == "thi5_like":
        return ["GO:0009228"]
    if category in {"amino_acid_atpase", "amino_acid_binding"}:
        return ["GO:0006865"]
    if category.startswith("sulfonate"):
        return ["GO:0042918"]
    if category == "cobalamin_binding":
        return ["GO:0015889"]
    if category in {"c_di_gmp_pde", "ribosome_associated_atpase"}:
        return []
    return ["GO:0055085"]


def module_locations_for(info: GeneInfo) -> list[str]:
    category = info["category"]
    if category in {"cobalamin_binding", "c4_dicarboxylate_binding", "substrate_binding", "amino_acid_binding", "sulfonate_binding", "transport_aux_lipoprotein", "macb_aux_lipoprotein"}:
        return ["GO:0030313"]
    if category in {"generic_atpase", "abc2_atpase", "macb_atpase", "sulfonate_atpase"}:
        return []
    if category == "thi5_like":
        return []
    if category == "mlaA":
        return ["GO:0016020"]
    if category == "ribosome_associated_atpase":
        return ["GO:0016020"]
    return ["GO:0005886"]


def descriptor(go_id: str) -> dict[str, Any]:
    return {"preferred_term": TERMS[go_id], "term": term(go_id)}


def build_module(infos: list[GeneInfo]) -> None:
    grouped: dict[str, list[GeneInfo]] = defaultdict(list)
    for info in infos:
        grouped[info["group"]].append(info)

    concept_ids = [
        "GO:0016887",
        "GO:0140359",
        "GO:0022857",
        "GO:0043190",
        "GO:0055085",
        "GO:0042918",
        "GO:0015424",
        "GO:0031419",
        "GO:0015889",
        "GO:0120010",
        "GO:0071111",
        "GO:0009228",
    ]
    parts = []
    for order, (group, group_infos) in enumerate(grouped.items(), start=1):
        annotons = []
        for info in group_infos:
            gene = info["gene"]
            annoton: dict[str, Any] = {
                "id": f"{gene}_generic_abc_residual_context",
                "label": f"{gene}: {info['product']}",
                "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
                "role_description": f"{gene}: {info['product']} ({info['category'].replace('_', ' ')})",
            }
            function_id = module_function_for(info)
            if function_id:
                annoton["function"] = descriptor(function_id)
            processes = [descriptor(go_id) for go_id in module_processes_for(info)]
            if processes:
                annoton["processes"] = processes
            locations = [descriptor(go_id) for go_id in module_locations_for(info)]
            if locations:
                annoton["locations"] = locations
            annotons.append(annoton)
        parts.append(
            {
                "order": order,
                "role": group,
                "node": {
                    "id": group.lower().replace("/", "_").replace(" ", "_").replace("-", "_"),
                    "label": group,
                    "module_type": "TRANSPORT_STEP",
                    "description": f"First-pass residual transport-bucket subgroup: {group}.",
                    "annotons": annotons,
                },
            }
        )

    doc = {
        "id": "MODULE:generic_abc_transport_boundary",
        "title": "Generic and residual ABC/transporter component boundary",
        "description": (
            "Boundary module for the PSEPK transport/membrane/efflux generic ABC residual split. "
            "The batch is not a single substrate pathway: it contains MacB/ABC-3-like efflux components, "
            "fused ABCB/type-I-exporter-like proteins, binding-protein-dependent importer pieces, named sulfonate, "
            "amino-acid, cobalamin, and heme/hemin spillover components, plus non-ABC outliers."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_transport_membrane_efflux_generic_abc_transporters.tsv",
                "title": "PSEPK transport/membrane/efflux generic ABC transporter batch",
                "statement": "The partition groups 33 residual ABC-family or ABC-like transport-bucket genes for first-pass curation.",
            }
        ],
        "notes": (
            "First-pass interpretation: keep functions component-level. Several genes are spillovers from better biological modules "
            "(c-di-GMP signaling, MlaA phospholipid transfer, thiamine biosynthesis, amino-acid/sulfonate/cobalamin/hemin import) "
            "but are represented here to close the residual transport split without asserting one generic ABC pathway."
        ),
        "module": {
            "id": "generic_abc_transport_boundary",
            "label": "Generic and residual ABC/transporter component boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                {
                    "preferred_term": TERMS[go_id],
                    "term": term(go_id),
                    "description": "Concept used in first-pass component-level curation of the residual ABC/transporter split.",
                }
                for go_id in concept_ids
            ],
            "parts": parts,
        },
    }
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    infos = [curate_gene(row) for row in load_rows()]
    build_module(infos)
    print(f"Curated {len(infos)} genes")
    print(f"Wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
