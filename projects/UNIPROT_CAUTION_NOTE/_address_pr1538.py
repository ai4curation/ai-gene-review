#!/usr/bin/env python3
"""Address PR #1538 review comments by surgically editing the CURRENT review YAMLs
(post-shepherd commit ac2c107b7). Does NOT re-run the generators (which would clobber
the shepherd's fixes). Each edit maps to a specific reviewer finding.
"""
import yaml
from pathlib import Path

def load(g): return yaml.safe_load(Path(f"genes/human/{g}/{g}-ai-review.yaml").read_text())
def save(g, d):
    Path(f"genes/human/{g}/{g}-ai-review.yaml").write_text(
        "# yaml-language-server: $schema=../../../src/ai_gene_review/schema/gene_review.yaml\n"
        + yaml.dump(d, sort_keys=False, default_flow_style=False, allow_unicode=True, width=100))

def set_action(d, term_id, evidence, action, reason, summary=None):
    n=0
    for a in d["existing_annotations"]:
        if a["term"]["id"]==term_id and a["evidence_type"]==evidence and not a.get("negated"):
            a["review"]["action"]=action; a["review"]["reason"]=reason
            if summary: a["review"]["summary"]=summary
            n+=1
    assert n>0, f"no match {term_id}/{evidence}"
    return n

def set_action_by_ref(d, ref, action, reason):
    n=0
    for a in d["existing_annotations"]:
        if str(a.get("original_reference_id"))==ref:
            a["review"]["action"]=action; a["review"]["reason"]=reason; n+=1
    assert n>0, f"no match ref {ref}"
    return n

# ---- IMPORTANT: CRMP1 GO:0150052 regulation of postsynapse assembly ACCEPT -> KEEP_AS_NON_CORE
d=load("CRMP1")
set_action(d,"GO:0150052","IEA","KEEP_AS_NON_CORE",
  "Ortholog-transferred electronic (IEA) annotation with no CRMP1-specific evidence for postsynaptic assembly regulation; demoted to non-core for consistency with the postsynapse (GO:0098794) localization, which is also KEEP_AS_NON_CORE.",
  "Regulation of postsynapse assembly (IEA, ortholog transfer): a peripheral, electronically inferred role, not an established core CRMP1 function.")
# suggestion F: add a molecular_function to CRMP1 core_functions (filamin binding is annotated)
d["core_functions"][0]["molecular_function"]={"id":"GO:0031005","label":"filamin binding"}
save("CRMP1",d)

# ---- IMPORTANT: DPYSL4 core_functions add MF + (only GO:0007399 BP is annotated) ; suggestion: DPYSL3 MF too
for g in ("DPYSL4","DPYSL3"):
    d=load(g)
    d["core_functions"][0]["molecular_function"]={"id":"GO:0031005","label":"filamin binding"}
    save(g,d)

# ---- SUGGESTION: ILK borderline large-scale interactome papers -> MARK_AS_OVER_ANNOTATED
d=load("ILK")
set_action_by_ref(d,"PMID:26496610","MARK_AS_OVER_ANNOTATED",
  "Large-scale quantitative interactome study ('A human interactome in three quantitative dimensions'); generic protein binding from a high-throughput screen is uninformative about molecular function. Grouped with the other HT-screen over-annotations.")
set_action_by_ref(d,"PMID:23455922","MARK_AS_OVER_ANNOTATED",
  "Large-scale standardized AP-MS protein-complex study; high-throughput generic protein binding, grouped with the other HT-screen over-annotations for consistency.")
save("ILK",d)

# ---- SUGGESTION: ROR1 cell population proliferation -> KEEP_AS_NON_CORE (consistency w/ RHBDF1)
d=load("ROR1")
set_action(d,"GO:0008283","IDA","KEEP_AS_NON_CORE",
  "Cell population proliferation is a downstream physiological/oncogenic phenotype of ROR1 signaling rather than its core molecular role; kept as non-core for consistency with how the same phenotype is treated elsewhere (e.g. RHBDF1).")
# ---- IMPORTANT: ROR1 references backfill findings + reference_review
ROR_REFS = {
 "PMID:24107129": (
   "ROR1 is classified as a pseudokinase that does not bind nucleotide, supporting the NOT ATP binding annotation.",
   "A robust methodology to subclassify pseudokinases based on their nucleotide-binding properties",
   "HIGH","VERIFIED","Supports the pseudokinase classification and the curated NOT|ATP binding."),
 "PMID:25029443": (
   "The ROR1 kinase domain has very low catalytic activity in vitro, consistent with an inactive/pseudokinase receptor.",
   "low catalytic activity in vitro",
   "HIGH","UNVERIFIED","Cited by the UniProt CAUTION as evidence of very low in vitro kinase activity; abstract not in cache."),
 "PMID:18287027": (
   "ROR1 is an oncofetal antigen and a receptor for Wnt5a, supporting its Wnt-protein binding / Wnt receptor function.",
   "identify ROR1 as an oncofetal antigen and receptor for Wnt5a",
   "HIGH","VERIFIED","Primary evidence for ROR1 as a Wnt5a receptor."),
 "PMID:27162350": (
   "ROR1 is essential for innervation of auditory hair cells and hearing, and acts as a Wnt receptor (supports Wnt receptor activity and sensory perception of sound).",
   "ROR1 is essential for proper innervation of auditory hair cells and hearing",
   "HIGH","VERIFIED","Source of the IMP Wnt receptor activity and inner-ear/hearing annotations."),
 "PMID:36949068": (
   "IGFBP5 is a ROR1 ligand; ROR1 functions as a signaling receptor promoting invasion via a ROR1/HER2-CREB axis (supports signaling receptor activity).",
   "IGFBP5 is an ROR1 ligand promoting glioblastoma invasion via ROR1/HER2-CREB signaling axis",
   "MEDIUM","VERIFIED","Supports signaling-receptor activity and a proliferation/invasion phenotype."),
 "PMID:8875995": (
   "Original report describing Ror1 as a receptor tyrosine kinase family member (the legacy RTK classification later superseded by the pseudokinase finding).",
   "a member of the receptor tyrosine kinase",
   "MEDIUM","VERIFIED","Basis of the legacy TAS 'transmembrane RTK activity' annotation now REMOVEd as superseded."),
 "PMID:22439932": (
   "ROR1 sustains EGFR survival signaling in lung adenocarcinoma (a protein-interaction / signaling context).",
   "ROR1 is required to sustain EGFR survival signaling in lung adenocarcinoma",
   "LOW","VERIFIED","Disease/interaction context; supports protein binding only."),
 "PMID:23382219": (
   "ROR1 is an endosomal-trafficking cargo of PX-FERM proteins (membrane/localization context).",
   "endosomal trafficking of diverse transmembrane cargos by PX-FERM proteins",
   "LOW","VERIFIED","Trafficking/localization context (signaling receptor complex)."),
 "PMID:24431302": (
   "Review of Wnt signaling in dopaminergic neuron development; cited for ROR1 coreceptor activity.",
   "Wnt signaling in midbrain dopaminergic neuron development",
   "LOW","VERIFIED","Review supporting the coreceptor-activity TAS annotation."),
 "PMID:1334494": (
   "Early characterization placing ROR1 as a cell-surface receptor tyrosine kinase (legacy classification).",
   "receptor tyrosine kinase",
   "LOW","UNVERIFIED","Legacy RTK reference; basis of a TAS PTK-signaling annotation now REMOVEd."),
 "PMID:32619402": (
   "ROR1 does not bind ATP, supporting the inactive-kinase / pseudokinase classification.",
   "Does not bind ATP",
   "MEDIUM","UNVERIFIED","Cited by the CAUTION for absence of ATP binding; abstract not in cache."),
}
for r in d["references"]:
    rid=r["id"]
    if rid in ROR_REFS:
        stmt,supp,rel,corr,notes=ROR_REFS[rid]
        r["findings"]=[{"statement":stmt,"supporting_text":supp}]
        r["reference_review"]={"relevance":rel,"correctness":corr,"review_notes":notes}
save("ROR1",d)

# ---- SUGGESTION: gene-specific suggested_questions / suggested_experiments for the CRMP family
CRMP_QE = {
 "DPYSL2": (
   "How does CRMP2 (DPYSL2) select tubulin heterodimers to promote microtubule assembly, and how do sequential GSK3B/CDK5/ROCK phosphorylations switch this binding off during semaphorin-3A-induced growth-cone collapse?",
   "Map the CRMP2 phospho-states that toggle tubulin binding.",
   "Reconstitute microtubule assembly with purified CRMP2 phospho-mimetic/phospho-dead variants and measure tubulin-heterodimer binding and axon outgrowth in neurons."),
 "DPYSL3": (
   "How does CRMP4 (DPYSL3) coordinate F-actin bundling and filopodium dynamics, and is this actin role separable from the microtubule functions of its paralog CRMP2?",
   "DPYSL3 acts primarily through F-actin bundling rather than microtubules.",
   "Assay F-actin bundling and filopodium formation with wild-type vs actin-binding-deficient DPYSL3 in neurons, comparing to DPYSL2."),
 "DPYSL4": (
   "What is the role of CRMP3 (DPYSL4) and its filamin interaction in dendritic/neurite development, and how does it differ functionally from the other CRMPs within hetero-tetramers?",
   "DPYSL4 contributes to dendritic development via filamin-dependent cytoskeletal coupling.",
   "Test dendrite/neurite outgrowth with wild-type vs filamin-binding-deficient DPYSL4 and in DPYSL4-depleted neurons."),
 "CRMP1": (
   "By what mechanism does CRMP1 mediate Sema3A-induced growth-cone collapse, and how does this relate to its reported invasion-suppressor activity in cancer?",
   "CRMP1's Sema3A growth-cone-collapse function underlies its invasion-suppressor activity.",
   "Compare Sema3A-induced growth-cone collapse and tumour-cell invasion in cells expressing wild-type vs signaling-deficient CRMP1."),
}
for g,(q,hyp,exp) in CRMP_QE.items():
    d=load(g)
    d["suggested_questions"]=[{"question":q}]
    d["suggested_experiments"]=[{"hypothesis":hyp,"description":exp}]
    save(g,d)

print("done")
