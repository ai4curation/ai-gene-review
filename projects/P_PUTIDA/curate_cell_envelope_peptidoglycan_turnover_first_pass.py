#!/usr/bin/env python3
"""First-pass curate PSEPK cell-envelope peptidoglycan turnover candidates."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"


TERM = {
    "GO:0000270": {"id": "GO:0000270", "label": "peptidoglycan metabolic process"},
    "GO:0004553": {"id": "GO:0004553", "label": "hydrolase activity, hydrolyzing O-glycosyl compounds"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0005886": {"id": "GO:0005886", "label": "plasma membrane"},
    "GO:0006508": {"id": "GO:0006508", "label": "proteolysis"},
    "GO:0008233": {"id": "GO:0008233", "label": "peptidase activity"},
    "GO:0008745": {"id": "GO:0008745", "label": "N-acetylmuramoyl-L-alanine amidase activity"},
    "GO:0008932": {"id": "GO:0008932", "label": "lytic endotransglycosylase activity"},
    "GO:0008933": {"id": "GO:0008933", "label": "peptidoglycan lytic transglycosylase activity"},
    "GO:0009002": {"id": "GO:0009002", "label": "serine-type D-Ala-D-Ala carboxypeptidase activity"},
    "GO:0009252": {"id": "GO:0009252", "label": "peptidoglycan biosynthetic process"},
    "GO:0009253": {"id": "GO:0009253", "label": "peptidoglycan catabolic process"},
    "GO:0009254": {"id": "GO:0009254", "label": "peptidoglycan turnover"},
    "GO:0009279": {"id": "GO:0009279", "label": "cell outer membrane"},
    "GO:0016020": {"id": "GO:0016020", "label": "membrane"},
    "GO:0016787": {"id": "GO:0016787", "label": "hydrolase activity"},
    "GO:0016810": {
        "id": "GO:0016810",
        "label": "hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds",
    },
    "GO:0016829": {"id": "GO:0016829", "label": "lyase activity"},
    "GO:0016837": {
        "id": "GO:0016837",
        "label": "carbon-oxygen lyase activity, acting on polysaccharides",
    },
    "GO:0016998": {"id": "GO:0016998", "label": "cell wall macromolecule catabolic process"},
    "GO:0019867": {"id": "GO:0019867", "label": "outer membrane"},
    "GO:0030234": {"id": "GO:0030234", "label": "enzyme regulator activity"},
    "GO:0031241": {"id": "GO:0031241", "label": "periplasmic side of cell outer membrane"},
    "GO:0042834": {"id": "GO:0042834", "label": "peptidoglycan binding"},
    "GO:0071555": {"id": "GO:0071555", "label": "cell wall organization"},
}


ORIGINAL_REFERENCE_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def first_line(path: Path, *needles: str) -> str:
    for line in read_lines(path):
        if all(needle in line for needle in needles):
            return line
    raise ValueError(f"No line in {path} contains all needles: {needles}")


def maybe_first_line(path: Path, *needles: str) -> str | None:
    try:
        return first_line(path, *needles)
    except ValueError:
        return None


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def go_support(gene: str, term_id: str, label: str) -> dict[str, str]:
    return support(file_id(gene, "goa.tsv"), f"{term_id}\t{label}")


def common_support(gene: str, *, go_term: str | None = None, domain: str | None = None) -> list[dict[str, str]]:
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    goa = GENE_ROOT / gene / f"{gene}-goa.tsv"
    data: list[dict[str, str]] = []
    if go_term:
        goa_snippet = f"{go_term}\t{TERM[go_term]['label']}"
        if goa.exists() and goa_snippet in goa.read_text(encoding="utf-8"):
            data.append(go_support(gene, go_term, TERM[go_term]["label"]))
    data.append(support(file_id(gene, "uniprot.txt"), first_line(uniprot, "DE   ")))
    if domain:
        data.append(support(file_id(gene, "uniprot.txt"), first_line(uniprot, domain)))
    asta_description = first_line(asta, "- **Protein Description:**")
    data.append(support(file_id(gene, "deep-research-asta.md"), asta_description))
    return data


def reference_list(existing_refs: list[dict], gene: str, accession: str) -> list[dict]:
    refs: list[dict] = []
    seen = set()
    for ref in existing_refs:
        ref_id = ref["id"]
        seen.add(ref_id)
        refs.append(ref)
    for ref_id in (file_id(gene, "goa.tsv"), file_id(gene, "uniprot.txt"), file_id(gene, "deep-research-asta.md")):
        if ref_id in seen:
            continue
        title = {
            file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({accession})",
            file_id(gene, "uniprot.txt"): f"UniProtKB entry for {gene} ({accession})",
            file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({accession})",
        }[ref_id]
        refs.append({"id": ref_id, "title": title, "findings": []})
    return refs


def review(
    gene: str,
    term_id: str,
    summary: str,
    action: str,
    reason: str,
    *,
    support_go: str | None = None,
    support_domain: str | None = None,
    replacements: list[str] | None = None,
) -> dict:
    term_for_support = support_go or term_id
    obj = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": common_support(gene, go_term=term_for_support, domain=support_domain),
    }
    if replacements:
        obj["proposed_replacement_terms"] = [TERM[replacement] for replacement in replacements]
    return obj


def new_annotation(
    gene: str,
    term_id: str,
    qualifier: str,
    summary: str,
    reason: str,
    *,
    support_domain: str,
) -> dict:
    return {
        "term": TERM[term_id],
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": common_support(gene, domain=support_domain),
        },
    }


GENES = {
    "amiD": {
        "accession": "Q88RJ9",
        "symbol": "amiD",
        "description": "amiD (PP_0130) encodes an N-acetylmuramoyl-L-alanine amidase-family peptidoglycan hydrolase in Pseudomonas putida KT2440. The protein carries amidase and peptidoglycan-binding domains and is inferred to cleave the amide bond between N-acetylmuramate and L-alanine during peptidoglycan turnover or cell-wall remodeling.",
        "domain": "NAMLAA_amidase_2",
        "reviews": {
            "GO:0008745": ("N-acetylmuramoyl-L-alanine amidase activity is the core molecular function.", "ACCEPT", "The UniProt name, EC 3.5.1.28, amidase domains, and GOA all support N-acetylmuramoyl-L-alanine amidase activity.", None, ["NAMLAA_amidase_2"]),
            "GO:0009253": ("Peptidoglycan catabolic process is appropriate process context.", "ACCEPT", "The amidase reaction cleaves peptidoglycan-derived MurNAc-L-Ala linkages, supporting peptidoglycan catabolism as first-pass process context.", None, ["NAMLAA_amidase_2"]),
            "GO:0009254": ("Peptidoglycan turnover is appropriate process context.", "ACCEPT", "TreeGrafter, PANTHER, the amidase family, and the peptidoglycan-binding domain support a turnover/remodeling role.", None, ["Peptidoglycan-bd-like"]),
            "GO:0019867": ("Outer-membrane localization is plausible but remains lower-confidence first-pass context.", "KEEP_AS_NON_CORE", "The outer-membrane annotation is TreeGrafter/PANTHER-derived and fits an envelope amidase candidate, but the local UniProt record does not provide a direct subcellular-location comment.", None, ["Peptidoglycan-bd-like"]),
        },
        "core": [{
            "description": "N-acetylmuramoyl-L-alanine amidase-family enzyme inferred to participate in peptidoglycan turnover/remodeling.",
            "molecular_function": TERM["GO:0008745"],
            "directly_involved_in": [TERM["GO:0009254"], TERM["GO:0009253"]],
        }],
        "question": "What is the envelope localization and physiological peptidoglycan substrate of AmiD in P. putida KT2440?",
        "experiment": "Assay purified AmiD against defined muropeptide substrates and compare muropeptide profiles of wild-type and amiD deletion strains.",
    },
    "ampD": {
        "accession": "Q88PQ9",
        "symbol": "ampD",
        "description": "ampD (PP_0789) encodes a cytoplasmic AmpD-family 1,6-anhydro-N-acetylmuramyl-L-alanine amidase in Pseudomonas putida KT2440. It is inferred to process peptidoglycan recycling products by cleaving the MurNAc-L-Ala amide bond and is kept distinct from envelope-localized wall hydrolases.",
        "domain": "NAMLAA_amidase_2",
        "reviews": {
            "GO:0005737": ("Cytoplasmic localization is appropriate for AmpD.", "ACCEPT", "UniProt places PP_0789 in the cytoplasm, consistent with AmpD processing soluble peptidoglycan recycling products.", None, ["Cytoplasm"]),
            "GO:0008745": ("N-acetylmuramoyl-L-alanine amidase activity is the core molecular function.", "ACCEPT", "The UniProt name, EC 3.5.1.28, amidase domains, and GOA all support AmpD-family amidase activity.", None, ["NAMLAA_amidase_2"]),
            "GO:0009253": ("Peptidoglycan catabolic process is appropriate process context.", "ACCEPT", "AmpD-family amidases hydrolyze peptidoglycan-derived MurNAc-L-Ala bonds during muropeptide turnover.", None, ["NAMLAA_amidase_2"]),
            "GO:0009254": ("Peptidoglycan turnover is appropriate process context.", "ACCEPT", "TreeGrafter and the AmpD-family assignment support a role in soluble peptidoglycan turnover/recycling.", None, ["NAMLAA_amidase_2"]),
            "GO:0016810": ("The broad carbon-nitrogen hydrolase annotation is correct but less informative than the amidase term.", "MODIFY", "The specific supported function is N-acetylmuramoyl-L-alanine amidase activity.", None, ["NAMLAA_amidase_2"], ["GO:0008745"]),
        },
        "core": [{
            "description": "Cytoplasmic AmpD-family amidase that processes peptidoglycan recycling products.",
            "molecular_function": TERM["GO:0008745"],
            "directly_involved_in": [TERM["GO:0009254"], TERM["GO:0009253"]],
            "locations": [TERM["GO:0005737"]],
        }],
        "question": "Does P. putida AmpD feed a canonical muropeptide-recycling and beta-lactam-response circuit, or is its role limited to basal peptidoglycan turnover?",
        "experiment": "Measure soluble muropeptide accumulation and beta-lactam response phenotypes in ampD deletion and complemented strains.",
    },
    "rlpA__Q88PC1": {
        "accession": "Q88PC1",
        "symbol": "rlpA",
        "description": "rlpA (PP_0929; UniProt Q88PC1) encodes one of two KT2440 RlpA-family endolytic peptidoglycan transglycosylase paralogs. The protein is a predicted membrane lipoprotein with an RlpA-like DPBB domain and is inferred to cleave peptidoglycan glycan strands as part of cell-wall remodeling.",
        "domain": "RlpA.",
        "reviews": {
            "GO:0000270": ("Peptidoglycan metabolic process is appropriate broad process context.", "ACCEPT", "The RlpA-family lytic transglycosylase function supports peptidoglycan metabolism; the molecular-function term captures the specific chemistry.", None, ["RlpA."]),
            "GO:0005886": ("Plasma-membrane localization is appropriate first-pass localization.", "ACCEPT", "UniProt places this RlpA paralog at the cell membrane and the protein is annotated as a membrane lipoprotein.", None, ["Cell membrane"]),
            "GO:0008932": ("Lytic endotransglycosylase activity is the core molecular function.", "ACCEPT", "The UniProt function statement, RlpA family assignment, and GOA all support lytic endotransglycosylase activity.", None, ["RlpA."]),
            "GO:0016829": ("Generic lyase activity is correct but should be replaced by lytic endotransglycosylase activity.", "MODIFY", "The RlpA-family enzyme class specifies lytic endotransglycosylase chemistry.", None, ["RlpA."], ["GO:0008932"]),
        },
        "core": [{
            "description": "RlpA-family membrane lipoprotein inferred to act as a lytic endotransglycosylase in peptidoglycan remodeling.",
            "molecular_function": TERM["GO:0008932"],
            "directly_involved_in": [TERM["GO:0000270"]],
            "locations": [TERM["GO:0005886"]],
        }],
        "question": "How does the PP_0929 RlpA paralog differ in localization, substrate preference, or expression from PP_4804/RlpA?",
        "experiment": "Compare PP_0929 and PP_4804 deletion strains and purified proteins for septal localization, muropeptide cleavage products, and growth or morphology phenotypes.",
    },
    "mltF": {
        "accession": "Q88P17",
        "symbol": "mltF",
        "description": "mltF (PP_1036) encodes membrane-bound lytic murein transglycosylase F in Pseudomonas putida KT2440. UniProt describes an outer-membrane peripheral enzyme that degrades murein glycan strands with SLT-family transglycosylase domains, supporting a role in peptidoglycan turnover and cell-wall macromolecule catabolism.",
        "domain": "MltF.",
        "reviews": {
            "GO:0000270": ("Peptidoglycan metabolic process is appropriate but broad.", "KEEP_AS_NON_CORE", "MltF acts on peptidoglycan glycan strands; the specific activity and catabolic/turnover process terms are more informative.", None, ["MltF."]),
            "GO:0008933": ("Peptidoglycan lytic transglycosylase activity is the core molecular function.", "ACCEPT", "The UniProt name, function statement, SLT-family domains, and GOA support peptidoglycan lytic transglycosylase activity.", None, ["Transglycosylase_SLT_dom_1"]),
            "GO:0009253": ("Peptidoglycan catabolic process is appropriate process context.", "ACCEPT", "UniProt states that MltF degrades murein glycan strands, supporting peptidoglycan catabolism.", None, ["Transglycosylase_SLT_dom_1"]),
            "GO:0009279": ("Cell outer membrane localization is appropriate.", "ACCEPT", "UniProt places MltF at the cell outer membrane as a peripheral membrane protein.", None, ["Cell outer membrane"]),
            "GO:0016020": ("Generic membrane localization is correct but less informative than cell outer membrane.", "KEEP_AS_NON_CORE", "The specific outer-membrane annotation captures the localization better than the generic membrane term.", None, ["Cell outer membrane"]),
            "GO:0016837": ("Generic polysaccharide carbon-oxygen lyase activity is correct but should be replaced by lytic endotransglycosylase activity.", "MODIFY", "The supported chemistry is lytic transglycosylase/endotransglycosylase activity on peptidoglycan.", None, ["Transglycosylase_SLT_dom_1"], ["GO:0008932"]),
            "GO:0016998": ("Cell-wall macromolecule catabolic process is appropriate broad process context.", "KEEP_AS_NON_CORE", "MltF degrades murein glycan strands; this broad term is true but less specific than peptidoglycan catabolic process.", None, ["Transglycosylase_SLT_dom_1"]),
        },
        "core": [{
            "description": "Outer-membrane/peripheral lytic murein transglycosylase involved in peptidoglycan turnover.",
            "molecular_function": TERM["GO:0008932"],
            "directly_involved_in": [TERM["GO:0009253"]],
            "locations": [TERM["GO:0009279"]],
        }],
        "question": "Which peptidoglycan cleavage products are generated by P. putida MltF, and is its activity coordinated with specific PBPs or elongation/septation states?",
        "experiment": "Profile muropeptides from an mltF deletion strain and from in vitro reactions with purified MltF and defined peptidoglycan sacculi.",
    },
    "PP_1325": {
        "accession": "Q88N87",
        "symbol": "PP_1325",
        "description": "PP_1325 encodes an outer-membrane lipoprotein with LpoA/LppC and periplasmic-binding-protein-like domains. PANTHER assigns it to the penicillin-binding protein activator LpoA family, supporting first-pass curation as a periplasmic-side outer-membrane regulator/activator context for peptidoglycan biosynthesis.",
        "domain": "LpoA.",
        "reviews": {
            "GO:0009252": ("Peptidoglycan biosynthetic process is appropriate for an LpoA-family PBP activator candidate.", "ACCEPT", "The LpoA/PANTHER family and peptidoglycan-synthesis keyword support a role in peptidoglycan biosynthesis context.", None, ["LpoA."]),
            "GO:0030234": ("Enzyme regulator activity is appropriate but broad.", "ACCEPT", "LpoA-family lipoproteins regulate/activate class A PBPs; no more specific GOA molecular-function annotation is present for this protein.", None, ["LpoA."]),
            "GO:0031241": ("Periplasmic side of cell outer membrane is appropriate first-pass localization.", "ACCEPT", "The PANTHER-derived GOA location and UniProt outer-membrane lipoprotein keywords support periplasmic-side outer-membrane context.", None, ["LpoA."]),
        },
        "core": [{
            "description": "Outer-membrane LpoA-family lipoprotein candidate that regulates or activates peptidoglycan biosynthesis enzymes.",
            "molecular_function": TERM["GO:0030234"],
            "directly_involved_in": [TERM["GO:0009252"]],
            "locations": [TERM["GO:0009279"]],
        }],
        "new_annotations": [
            ("GO:0009279", "located_in", "Cell outer membrane is added as a parent location for the periplasmic-side outer-membrane annotation.", "GOA already records the more specific periplasmic side of cell outer membrane term, and UniProt keywords support outer-membrane lipoprotein context.", "LpoA."),
        ],
        "question": "Which class A penicillin-binding protein is regulated by PP_1325 in KT2440?",
        "experiment": "Test PP_1325 interaction with MrcA/MrcB/PbpC and assay PBP glycosyltransferase activity with and without PP_1325.",
    },
    "PP_2147": {
        "accession": "Q88KZ2",
        "symbol": "PP_2147",
        "description": "PP_2147 encodes a signal-peptide-bearing CsiV-domain peptidoglycan-binding protein candidate in Pseudomonas putida KT2440. The protein has no current GOA annotations, so it is retained as a candidate peptidoglycan-binding/remodeling context gene pending localization and substrate evidence.",
        "domain": "CsiV.",
        "reviews": {},
        "core": [{
            "description": "CsiV-domain peptidoglycan-binding protein candidate with no current GOA annotations.",
            "molecular_function": TERM["GO:0042834"],
            "directly_involved_in": [TERM["GO:0071555"]],
        }],
        "new_annotations": [
            ("GO:0042834", "enables", "PP_2147 should be represented as a peptidoglycan-binding candidate.", "UniProt names PP_2147 as a peptidoglycan-binding protein CsiV and the protein carries CsiV domains.", "CsiV."),
            ("GO:0071555", "involved_in", "PP_2147 should be represented as candidate cell-wall organization context.", "The product name and CsiV-domain assignment support conservative cell-wall organization context pending direct assays.", "CsiV."),
        ],
        "question": "Does PP_2147 bind peptidoglycan directly, and does it affect envelope integrity or cell-wall remodeling?",
        "experiment": "Test purified PP_2147 for peptidoglycan binding and assay PP_2147 deletion or depletion for morphology and envelope-stress phenotypes.",
    },
    "PP_3562": {
        "accession": "Q88H03",
        "symbol": "PP_3562",
        "description": "PP_3562 encodes a signal-peptide-bearing cell-wall hydrolase SleB-domain protein in Pseudomonas putida KT2440. Current GOA only provides a broad hydrolase term, so the first-pass review treats it as a candidate cell-wall hydrolase/remodeling protein without assigning a specific substrate or reaction.",
        "domain": "Cell_wall_hydrolase_SleB",
        "reviews": {
            "GO:0016787": ("Broad hydrolase activity is plausible but not specific enough to define the core function.", "KEEP_AS_NON_CORE", "The SleB-domain product name supports hydrolase-family context, but current evidence does not identify the precise cell-wall substrate or hydrolytic reaction.", None, ["Cell_wall_hydrolase_SleB"]),
        },
        "core": [{
            "description": "SleB-domain cell-wall hydrolase candidate likely involved in envelope or peptidoglycan remodeling.",
            "directly_involved_in": [TERM["GO:0071555"]],
        }],
        "new_annotations": [
            ("GO:0071555", "involved_in", "PP_3562 should be represented as candidate cell-wall organization/remodeling context.", "The signal-peptide-bearing SleB-domain cell-wall hydrolase product supports conservative cell-wall organization context, but exact substrate specificity remains unresolved.", "Cell_wall_hydrolase_SleB"),
        ],
        "question": "What cell-wall substrate is cleaved by PP_3562, if any, in P. putida KT2440?",
        "experiment": "Purify PP_3562 and assay activity against purified sacculi and defined muropeptides; compare cell-wall phenotypes of a deletion strain.",
    },
    "pbpG": {
        "accession": "Q88GD0",
        "symbol": "pbpG",
        "description": "pbpG (PP_3794) encodes a predicted periplasmic murein D-alanyl-D-alanine endopeptidase/serine-type D-Ala-D-Ala carboxypeptidase-family protein. It carries peptidase S11 and beta-lactam/transpeptidase-like domains and is inferred to participate in peptidoglycan maturation or remodeling rather than cytosolic precursor synthesis.",
        "domain": "Peptidase_S11",
        "reviews": {
            "GO:0006508": ("Proteolysis is a broad parent-process annotation for the peptidase-domain assignment.", "KEEP_AS_NON_CORE", "The biologically relevant target is peptidoglycan stem peptides rather than general protein turnover.", None, ["Peptidase_S11"]),
            "GO:0008233": ("Generic peptidase activity is correct but should be replaced by the specific D-Ala-D-Ala carboxypeptidase term.", "MODIFY", "InterPro and PANTHER support a peptidase S11 D-Ala-D-Ala carboxypeptidase/endopeptidase-family enzyme.", None, ["Peptidase_S11"], ["GO:0009002"]),
            "GO:0009002": ("Serine-type D-Ala-D-Ala carboxypeptidase activity is the best current molecular-function annotation.", "ACCEPT", "The peptidase S11 and PANTHER D-Ala-D-Ala endopeptidase/carboxypeptidase assignments support this activity.", None, ["Peptidase_S11"]),
        },
        "core": [{
            "description": "Periplasmic peptidase S11-family PBP/remodeling enzyme with D-Ala-D-Ala carboxypeptidase/endopeptidase activity.",
            "molecular_function": TERM["GO:0009002"],
            "directly_involved_in": [TERM["GO:0071555"]],
        }],
        "new_annotations": [
            ("GO:0071555", "involved_in", "pbpG should be represented as cell-wall organization/remodeling context.", "The peptidase S11, beta-lactam/transpeptidase-like, and murein D-alanyl-D-alanine endopeptidase assignments support peptidoglycan remodeling context.", "Peptidase_S11"),
        ],
        "question": "Does PbpG act primarily as a D-Ala-D-Ala carboxypeptidase, an endopeptidase, or both during peptidoglycan remodeling?",
        "experiment": "Assay purified PbpG against pentapeptide and cross-linked muropeptide substrates and profile muropeptides in a pbpG mutant.",
    },
    "rlpA__Q88DM1": {
        "accession": "Q88DM1",
        "symbol": "rlpA",
        "description": "rlpA (PP_4804; UniProt Q88DM1) encodes the second KT2440 RlpA-family endolytic peptidoglycan transglycosylase paralog. This copy has RlpA/DPBB and SPOR-like domains, supporting lytic endotransglycosylase activity plus peptidoglycan-binding context during cell-wall remodeling.",
        "domain": "RlpA.",
        "reviews": {
            "GO:0000270": ("Peptidoglycan metabolic process is appropriate broad process context.", "ACCEPT", "The RlpA-family lytic transglycosylase activity supports peptidoglycan metabolism; the molecular-function term captures the specific chemistry.", None, ["RlpA."]),
            "GO:0005886": ("Plasma-membrane localization is appropriate first-pass localization.", "ACCEPT", "UniProt places this RlpA paralog at the cell membrane and the protein is a membrane lipoprotein.", None, ["Cell membrane"]),
            "GO:0008932": ("Lytic endotransglycosylase activity is the core molecular function.", "ACCEPT", "The UniProt function statement, RlpA family assignment, and GOA all support lytic endotransglycosylase activity.", None, ["RlpA."]),
            "GO:0009279": ("Outer-membrane localization is plausible but less directly supported than the UniProt cell-membrane annotation.", "KEEP_AS_NON_CORE", "The outer-membrane annotation is TreeGrafter/PANTHER-derived; UniProt itself records cell membrane for this copy.", None, ["SPOR-like_dom"]),
            "GO:0016829": ("Generic lyase activity is correct but should be replaced by lytic endotransglycosylase activity.", "MODIFY", "The RlpA-family enzyme class specifies lytic endotransglycosylase chemistry.", None, ["RlpA."], ["GO:0008932"]),
            "GO:0042834": ("Peptidoglycan binding is appropriate non-core context for the SPOR-domain copy.", "KEEP_AS_NON_CORE", "The SPOR-like domain supports peptidoglycan-binding context, while the catalytic role is captured by lytic endotransglycosylase activity.", None, ["SPOR-like_dom"]),
        },
        "core": [{
            "description": "RlpA-family membrane lipoprotein with lytic endotransglycosylase activity and SPOR-domain peptidoglycan-binding context.",
            "molecular_function": TERM["GO:0008932"],
            "directly_involved_in": [TERM["GO:0000270"]],
            "locations": [TERM["GO:0005886"]],
        }],
        "question": "Does the SPOR-domain PP_4804 RlpA paralog specialize for septal peptidoglycan relative to PP_0929?",
        "experiment": "Compare localization of tagged PP_4804 and PP_0929 during growth and septation and test their cleavage preferences on intact sacculi.",
    },
    "PP_4971": {
        "accession": "Q88D56",
        "symbol": "PP_4971",
        "description": "PP_4971 encodes a membrane-bound lytic murein transglycosylase A/MltA-family protein in Pseudomonas putida KT2440. The MltA/RlpA-like domains and GOA support a peptidoglycan lytic transglycosylase role in peptidoglycan turnover, with outer-membrane localization inferred from InterPro.",
        "domain": "MltA.",
        "reviews": {
            "GO:0004553": ("O-glycosyl hydrolase activity is a misleading broad parent for a lytic transglycosylase.", "MODIFY", "Lytic murein transglycosylases cleave peptidoglycan glycan strands by transglycosylase/lyase chemistry; the supported replacement is lytic endotransglycosylase activity.", None, ["MltA."], ["GO:0008932"]),
            "GO:0008933": ("Peptidoglycan lytic transglycosylase activity is the core molecular function.", "ACCEPT", "The UniProt name, MltA domains, PANTHER family, and GOA all support lytic murein transglycosylase activity.", None, ["MltA."]),
            "GO:0009253": ("Peptidoglycan catabolic process is appropriate process context.", "ACCEPT", "UniProt describes PP_4971 as a murein-degrading enzyme that may function in recycling of muropeptides.", None, ["MltA."]),
            "GO:0009254": ("Peptidoglycan turnover is appropriate process context.", "ACCEPT", "The MltA-family assignment and UniProt recycling comment support a peptidoglycan-turnover role.", None, ["MltA."]),
            "GO:0016829": ("Generic lyase activity is correct but should be replaced by lytic endotransglycosylase activity.", "MODIFY", "The specific supported chemistry is lytic endotransglycosylase activity.", None, ["MltA."], ["GO:0008932"]),
            "GO:0019867": ("Outer-membrane localization is plausible first-pass localization.", "ACCEPT", "The InterPro-derived GOA localization and membrane-bound MltA product assignment support envelope/outer-membrane context.", None, ["MltA."]),
        },
        "core": [{
            "description": "MltA-family lytic murein transglycosylase involved in peptidoglycan turnover/recycling.",
            "molecular_function": TERM["GO:0008932"],
            "directly_involved_in": [TERM["GO:0009254"], TERM["GO:0009253"]],
            "locations": [TERM["GO:0019867"]],
        }],
        "question": "Does PP_4971 generate muropeptide products used for recycling, or does it primarily remodel envelope peptidoglycan locally?",
        "experiment": "Profile muropeptides in PP_4971 mutants and test purified PP_4971 on sacculi to identify cleavage products.",
    },
    "PP_5354": {
        "accession": "Q88C29",
        "symbol": "PP_5354",
        "description": "PP_5354 encodes a SUKH_5/Knr4-Smi1-like cell wall assembly protein candidate in Pseudomonas putida KT2440. The protein has no current GOA annotations, so it is retained as a conservative cell-wall organization candidate pending direct evidence for localization, binding partners, or activity.",
        "domain": "SUKH_5",
        "reviews": {},
        "core": [{
            "description": "SUKH_5/Knr4-Smi1-like candidate protein provisionally associated with cell-wall assembly or organization.",
            "directly_involved_in": [TERM["GO:0071555"]],
        }],
        "new_annotations": [
            ("GO:0071555", "involved_in", "PP_5354 should be represented as candidate cell-wall organization context.", "UniProt names PP_5354 as a cell wall assembly protein and records a SUKH_5/Knr4-Smi1-like domain assignment.", "SUKH_5"),
        ],
        "question": "Does PP_5354 affect cell-wall assembly, envelope integrity, or morphology in KT2440?",
        "experiment": "Construct PP_5354 deletion/depletion strains and assay morphology, envelope-stress sensitivity, and genetic interaction with peptidoglycan synthesis/remodeling genes.",
    },
}


def apply_reviews(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["gene_symbol"] = cfg["symbol"]
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]

    existing_refs = data.get("references") or []
    data["references"] = reference_list(existing_refs, gene, cfg["accession"])
    configured_new_terms = {term_id for term_id, *_ in cfg.get("new_annotations", [])}
    if configured_new_terms:
        data["existing_annotations"] = [
            annotation
            for annotation in (data.get("existing_annotations") or [])
            if not (
                annotation.get("term", {}).get("id") in configured_new_terms
                and annotation.get("review", {}).get("action") == "NEW"
            )
        ]

    seen_terms = set()
    for annotation in data.get("existing_annotations") or []:
        term_id = annotation["term"]["id"]
        seen_terms.add(term_id)
        if term_id not in cfg["reviews"]:
            raise ValueError(f"No review configured for {gene} {term_id}")
        summary, action, reason, support_go, support_domains, *replacement_data = cfg["reviews"][term_id]
        replacements = replacement_data[0] if replacement_data else None
        support_domain = support_domains[0] if support_domains else cfg["domain"]
        annotation["review"] = review(
            gene,
            term_id,
            summary,
            action,
            reason,
            support_go=support_go,
            support_domain=support_domain,
            replacements=replacements,
        )

    missing_reviews = set(cfg["reviews"]) - seen_terms
    if missing_reviews:
        raise ValueError(f"Configured reviews not found in {gene}: {sorted(missing_reviews)}")

    for term_id, qualifier, summary, reason, support_domain in cfg.get("new_annotations", []):
        data.setdefault("existing_annotations", []).append(
            new_annotation(
                gene,
                term_id,
                qualifier,
                summary,
                reason,
                support_domain=support_domain,
            )
        )

    core_functions = []
    for core in cfg["core"]:
        core = dict(core)
        supported = []
        if "molecular_function" in core:
            supported += common_support(gene, go_term=core["molecular_function"]["id"], domain=cfg["domain"])
        else:
            supported += common_support(gene, domain=cfg["domain"])
        core["supported_by"] = supported
        core_functions.append(core)
    data["core_functions"] = core_functions

    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": cfg["question"]}]
    data["suggested_experiments"] = [
        {"description": cfg["experiment"], "experiment_type": "targeted cell-wall phenotype and biochemical assay"}
    ]

    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str, cfg: dict) -> None:
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    product_line = first_line(uniprot, "DE   ")
    domain_line = first_line(uniprot, cfg["domain"])
    asta_product = first_line(asta, "- **Protein Description:**")
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-09 PDT / 2026-07-10 UTC: First-pass peptidoglycan turnover/remodeling curation.",
        cfg["description"],
        "",
        f"Primary provenance: UniProt product/domain evidence [{file_id(gene, 'uniprot.txt')} \"{product_line}\"; "
        f"{file_id(gene, 'uniprot.txt')} \"{domain_line}\"]. Asta was retrieval-only and mainly confirmed the same "
        f"metadata-level identity [{file_id(gene, 'deep-research-asta.md')} \"{asta_product}\"].",
        "",
        "Decision: " + cfg["core"][0]["description"],
    ]
    (GENE_ROOT / gene / f"{gene}-notes.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    for gene, cfg in GENES.items():
        apply_reviews(gene, cfg)
        write_notes(gene, cfg)
        print(f"Curated {gene}")


if __name__ == "__main__":
    main()
