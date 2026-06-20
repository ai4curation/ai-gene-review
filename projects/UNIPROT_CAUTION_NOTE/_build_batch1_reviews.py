#!/usr/bin/env python3
"""Build full gene reviews for the four remaining CAUTION batch-1 stubs:
RHBDF1, SUMF2, PANK4, NAALADL2.

For each gene: load the fetched stub, apply ordered per-annotation reviews
(asserting term id + reference to fail fast on any drift), and add description,
references (PMID titles pulled from the publications/ cache), aliases,
core_functions and suggestions. Validated afterwards with `ai-gene-review validate`.
"""
from pathlib import Path
import yaml

PUB = Path("publications")

def title(pmid):
    txt = (PUB / f"PMID_{pmid}.md").read_text()
    return yaml.safe_load(txt.split("---", 2)[1])["title"]

def ref(pmid, *findings, review=None):
    r = {"id": f"PMID:{pmid}", "title": title(pmid),
         "findings": [{"statement": s, "supporting_text": q} for s, q in findings]}
    if review:
        r["reference_review"] = review
    return r

def goref(rid, t): return {"id": rid, "title": t, "findings": []}
def reactome(rid, t): return {"id": rid, "title": t, "findings": []}
def sb(rid, text): return [{"reference_id": rid, "supporting_text": text}]

HIGH_V = {"relevance": "HIGH", "correctness": "VERIFIED"}
LOW_V = {"relevance": "LOW", "correctness": "VERIFIED",
         "review_notes": "High-throughput interactome; supports only generic protein binding."}

def build(gene, anns_reviews, top):
    P = Path(f"genes/human/{gene}/{gene}-ai-review.yaml")
    d = yaml.safe_load(P.read_text())
    A = d["existing_annotations"]
    assert len(A) == len(anns_reviews), f"{gene}: {len(A)} vs {len(anns_reviews)}"
    for a, (tid, rid, body) in zip(A, anns_reviews):
        assert a["term"]["id"] == tid, f"{gene} term drift {a['term']['id']} != {tid}"
        assert str(a.get("original_reference_id")) == rid, f"{gene} ref drift @{tid}: {a.get('original_reference_id')} != {rid}"
        rv = {"summary": body["summary"], "action": body["action"], "reason": body["reason"]}
        if body.get("supported_by"):
            rv["supported_by"] = body["supported_by"]
        a["review"] = rv
    d.update(top)
    P.write_text("# yaml-language-server: $schema=../../../src/ai_gene_review/schema/gene_review.yaml\n" +
                 yaml.dump(d, sort_keys=False, default_flow_style=False, allow_unicode=True, width=100))
    print(f"{gene}: wrote {len(A)} reviewed annotations")

# ============================== RHBDF1 ==============================
U = "file:human/RHBDF1/RHBDF1-uniprot.txt"
CAU = "Lacks serine protease activity as it lacks the catalytic Ser"
A_serprot = dict(action="ACCEPT",
  summary="NOT (negated): RHBDF1 (iRhom1) does NOT have serine-type endopeptidase activity. Although it belongs to the rhomboid peptidase S54 family, it is an inactive rhomboid (pseudoprotease) lacking the catalytic Ser (position 720).",
  reason="Correct and important negation. iRhom1 is a catalytically dead rhomboid; the curated NOT faithfully encodes the loss of protease activity flagged by the UniProt CAUTION. Retain.",
  supported_by=sb(U, CAU))
PB_iRhom = dict(action="KEEP_AS_NON_CORE",
  summary="IPI 'protein binding'; iRhom1 acts as a scaffold and interacts with functionally relevant partners (ADAM17/TACE, FRMD8/iTAP, PAC1/2). The interaction supports its adapter role but the generic term is uninformative.",
  reason="Real, functionally meaningful interaction underpinning the scaffold function, but 'protein binding' itself is uninformative (curation guideline); keep as non-core supporting evidence.",
  supported_by=sb(U, "Belongs to the peptidase S54 family"))
PB_screen = dict(action="MARK_AS_OVER_ANNOTATED",
  summary="Generic 'protein binding' from a large-scale binary interactome screen; no specific functional signal.",
  reason="High-throughput interactome protein binding; uninformative about molecular function. Over-annotation.")
ER_loc = dict(action="ACCEPT", summary="ER membrane localization, the principal residence of iRhom1.",
  reason="Well supported by multiple EXP/IDA lines and UniProt; core localization.",
  supported_by=sb(U, "Endoplasmic reticulum membrane"))
Golgi_loc = dict(action="ACCEPT", summary="Golgi membrane localization; iRhom1 traffics ADAM17 through the secretory pathway.",
  reason="Supported by EXP/IDA evidence; consistent with its trafficking role.", supported_by=None)
EGFR = dict(action="ACCEPT",
  summary="Regulation of EGFR signaling pathway. iRhom1 controls maturation/trafficking of ADAM17, the sheddase that releases EGFR ligands, thereby regulating EGFR signaling.",
  reason="Core biological process, supported experimentally (IMP) and by phylogenetic inference. Central to iRhom1 function.",
  supported_by=sb(U, "Regulates ADAM17 protease, a sheddase of the epidermal growth"))
SECR = dict(action="ACCEPT",
  summary="Regulation of protein secretion: iRhom1 governs the maturation of ADAM17 and shedding/secretion of its substrates.",
  reason="Core process tied to the iRhom/ADAM17 sheddase axis; experimentally supported.",
  supported_by=sb(U, "Regulates ADAM17 protease, a sheddase of the epidermal growth"))
NEG_SECR = dict(action="ACCEPT",
  summary="Negative regulation of protein secretion (IDA, PMID:21439629): rhomboid pseudoproteases use ER quality-control to retain/regulate secretion of client proteins.",
  reason="Experimentally supported core regulatory process for an inactive rhomboid.",
  supported_by=sb("PMID:21439629", "Rhomboid family pseudoproteases use the ER quality control machinery to regulate intercellular signaling"))
NONCORE_loc_broad = dict(action="KEEP_AS_NON_CORE", summary="Broad membrane/endomembrane/cytoplasm localization by IEA.",
  reason="Correct but non-specific; the precise compartments (ER and Golgi membranes) are separately annotated.", supported_by=None)
rhbdf1 = [
 ("GO:0004252","GO_REF:0000033", A_serprot),
 ("GO:0005789","GO_REF:0000033", ER_loc),
 ("GO:0042058","GO_REF:0000033", EGFR),
 ("GO:0050708","GO_REF:0000033", SECR),
 ("GO:0000139","GO_REF:0000044", Golgi_loc),
 ("GO:0005737","GO_REF:0000117", NONCORE_loc_broad),
 ("GO:0005789","GO_REF:0000044", ER_loc),
 ("GO:0012505","GO_REF:0000117", NONCORE_loc_broad),
 ("GO:0016020","GO_REF:0000120", NONCORE_loc_broad),
 ("GO:0005515","PMID:32296183", PB_screen),
 ("GO:0005515","PMID:26109405", PB_iRhom),
 ("GO:0005783","PMID:26109405", dict(action="ACCEPT", summary="ER localization (IDA).", reason="Direct evidence; consistent with core ER residence.", supported_by=None)),
 ("GO:0051131","PMID:26109405", dict(action="KEEP_AS_NON_CORE",
   summary="Chaperone-mediated protein complex assembly: iRhom1 regulates proteasome assembly via PAC1/2 under ER stress (PMID:26109405).",
   reason="Experimentally supported but a specialized stress-context role, non-core relative to the iRhom/ADAM17 axis.",
   supported_by=sb("PMID:26109405","iRhom1 regulates proteasome activity via PAC1/2 under ER stress"))),
 ("GO:0005515","PMID:29897333", PB_iRhom),
 ("GO:0000139","PMID:15965977", Golgi_loc),
 ("GO:0005789","PMID:15965977", ER_loc),
 ("GO:0005515","PMID:29897336", PB_iRhom),
 ("GO:0000139","PMID:18832597", Golgi_loc),
 ("GO:0005789","PMID:18832597", ER_loc),
 ("GO:0008283","PMID:18832597", dict(action="KEEP_AS_NON_CORE",
   summary="Cell population proliferation (IMP) in head-and-neck cancer cells via GPCR-EGFR transactivation.",
   reason="Downstream physiological/disease phenotype, non-core relative to the molecular regulatory role.", supported_by=None)),
 ("GO:0016477","PMID:18832597", dict(action="KEEP_AS_NON_CORE",
   summary="Cell migration (IMP), a downstream phenotype of iRhom1/EGFR signaling in cancer cells.",
   reason="Downstream physiological phenotype; non-core.", supported_by=None)),
 ("GO:0042058","PMID:18832597", EGFR),
 ("GO:0050708","PMID:18832597", SECR),
 ("GO:0005789","PMID:21439629", ER_loc),
 ("GO:0050709","PMID:21439629", NEG_SECR),
 ("GO:0061136","PMID:21439629", dict(action="KEEP_AS_NON_CORE",
   summary="Regulation of proteasomal protein catabolic process (IDA): iRhom1 routes clients to ER-associated degradation / regulates proteasome activity.",
   reason="Experimentally supported but a non-core facet relative to the ADAM17/EGFR sheddase-regulation function.",
   supported_by=sb("PMID:21439629","Rhomboid family pseudoproteases use the ER quality control machinery to regulate intercellular signaling"))),
 ("GO:0004252","PMID:21439629", A_serprot),
]
rhbdf1_top = dict(
 status="DRAFT",
 description=(
   "RHBDF1 (iRhom1; inactive rhomboid protein 1) is an endoplasmic-reticulum / Golgi "
   "membrane protein of the rhomboid peptidase S54 family. Unlike active rhomboid "
   "intramembrane serine proteases, iRhom1 is a catalytically dead pseudoprotease: it lacks "
   "the catalytic serine and has no serine-type endopeptidase activity. Instead it functions "
   "as a regulatory scaffold for the metalloprotease ADAM17/TACE, controlling ADAM17 "
   "maturation, ER-to-Golgi trafficking, stability and substrate selectivity (together with "
   "partners such as FRMD8/iTAP), and thereby governing the shedding of EGFR ligands and "
   "TNF, i.e. regulation of EGFR signaling and regulated protein secretion. Acting through "
   "the ER quality-control machinery, it also influences ER-associated degradation and, under "
   "ER stress, proteasome assembly via PAC1/2. It is widely expressed (notably cerebellum, "
   "cerebrum, heart) and its dysregulation promotes proliferation and migration in epithelial "
   "cancers."),
 aliases=["iRhom1","RHO","DIST1","C16orf8","p100hRho","Inactive rhomboid protein 1"],
 references=[
   goref("GO_REF:0000033","Annotation inferences using phylogenetic trees"),
   goref("GO_REF:0000044","GO annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping"),
   goref("GO_REF:0000117","Automatic GO annotation from UniProtKB-KW mapping"),
   goref("GO_REF:0000120","Combined Automated Annotation using Multiple IEA Methods"),
   ref("15965977", ("iRhom1 interacts with TGF-alpha family ligands and is an ER/Golgi membrane rhomboid homolog.","Characterization of a human rhomboid homolog, p100hRho/RHBDF1"), review=HIGH_V),
   ref("18832597", ("RHBDF1 participates in GPCR-mediated transactivation of EGFR growth signals in cancer cells.","Human rhomboid family-1 gene RHBDF1 participates in GPCR-mediated transactivation of EGFR growth signals in head and neck squamous cancer cells"), review=HIGH_V),
   ref("21439629", ("Rhomboid pseudoproteases use ER quality control to regulate intercellular (EGF/ADAM17) signaling; iRhom1 has no protease activity.","Rhomboid family pseudoproteases use the ER quality control machinery to regulate intercellular signaling"), review=HIGH_V),
   ref("26109405", ("iRhom1 regulates proteasome activity via PAC1/2 under ER stress.","iRhom1 regulates proteasome activity via PAC1/2 under ER stress"), review={"relevance":"MEDIUM","correctness":"VERIFIED"}),
   ref("29897333", ("iTAP/FRMD8 is an iRhom interactor controlling TNF secretion by stabilizing iRhom/TACE.","iTAP, a novel iRhom interactor, controls TNF secretion by policing the stability of iRhom/TACE"), review={"relevance":"MEDIUM","correctness":"VERIFIED"}),
   ref("29897336", ("FRMD8 stabilizes the iRhom/ADAM17 sheddase complex to promote inflammatory and growth-factor signaling.","FRMD8 promotes inflammatory and growth factor signalling by stabilising the iRhom/ADAM17 sheddase complex"), review={"relevance":"MEDIUM","correctness":"VERIFIED"}),
   ref("32296183", review=LOW_V),
   {"id":U,"title":"UniProt entry Q96CC6 (RHBDF1)","findings":[
     {"statement":"iRhom1 lacks serine protease activity (no catalytic Ser-720).","supporting_text":CAU},
     {"statement":"Regulates ADAM17, a sheddase of EGF-receptor ligands.","supporting_text":"Regulates ADAM17 protease, a sheddase of the epidermal growth"}]},
 ],
 core_functions=[
   {"description":(
     "Catalytically inactive rhomboid (pseudoprotease) that acts as an ER/Golgi membrane "
     "scaffold regulating ADAM17/TACE maturation, trafficking and activity, thereby controlling "
     "shedding of EGFR ligands and TNF (regulation of EGFR signaling and protein secretion)."),
    "directly_involved_in":[{"id":"GO:0042058","label":"regulation of epidermal growth factor receptor signaling pathway"},
                            {"id":"GO:0050708","label":"regulation of protein secretion"}],
    "locations":[{"id":"GO:0005789","label":"endoplasmic reticulum membrane"},
                 {"id":"GO:0000139","label":"Golgi membrane"}],
    "supported_by":[{"reference_id":"PMID:21439629","supporting_text":"Rhomboid family pseudoproteases use the ER quality control machinery to regulate intercellular signaling"},
                    {"reference_id":U,"supporting_text":"Regulates ADAM17 protease, a sheddase of the epidermal growth"}]},
 ],
 suggested_questions=[
   {"question":"Do iRhom1 and iRhom2 (RHBDF2) have distinct ADAM17 substrate repertoires, or are they largely redundant in EGFR-ligand vs TNF shedding?"}],
 suggested_experiments=[
   {"hypothesis":"iRhom1 selectively controls shedding of a subset of ADAM17 substrates.",
    "description":"Quantify shedding of a panel of ADAM17 substrates (EGF-family ligands, TNF) in RHBDF1-knockout vs RHBDF2-knockout cells with rescue constructs."}],
)

# ============================== SUMF2 ==============================
US = "file:human/SUMF2/SUMF2-uniprot.txt"
SUMF2_FUNC = "Inhibits the activation of sulfatases by SUMF1"
sumf2 = [
 ("GO:0005783","GO_REF:0000033", dict(action="ACCEPT", summary="ER localization (IBA); SUMF2 is an ER-luminal protein.", reason="Correct core localization.", supported_by=sb(US,"Endoplasmic reticulum lumen"))),
 ("GO:0005788","GO_REF:0000120", dict(action="ACCEPT", summary="ER lumen localization (IEA).", reason="Correct, supported by UniProt and EXP evidence.", supported_by=sb(US,"Endoplasmic reticulum lumen"))),
 ("GO:0005515","PMID:15962010", dict(action="KEEP_AS_NON_CORE",
   summary="IPI 'protein binding'; the partner is SUMF1. The SUMF2-SUMF1 interaction is the basis of SUMF2's function (it inhibits SUMF1).",
   reason="Functionally central interaction, but the generic 'protein binding' term is uninformative; the specific regulatory role is captured by enzyme inhibitor activity and in core_functions. Keep as supporting non-core.",
   supported_by=sb(US, SUMF2_FUNC))),
 ("GO:0005515","PMID:32814053", dict(action="MARK_AS_OVER_ANNOTATED", summary="Generic protein binding from a large neurodegenerative-disease interactome.", reason="High-throughput, uninformative; over-annotation.")),
 ("GO:0005515","PMID:32838362", dict(action="MARK_AS_OVER_ANNOTATED", summary="Generic protein binding from a SARS-CoV-2 virus-host interactome screen.", reason="High-throughput viral interactome; uninformative about native function; over-annotation.")),
 ("GO:0005515","PMID:33845483", dict(action="MARK_AS_OVER_ANNOTATED", summary="Generic protein binding from a SARS-CoV-2 host-perturbation proteomics screen.", reason="High-throughput; uninformative; over-annotation.")),
 ("GO:0005515","PMID:36217030", dict(action="MARK_AS_OVER_ANNOTATED", summary="Generic protein binding from a comprehensive SARS-CoV-2-human interactome.", reason="High-throughput viral interactome; over-annotation.")),
 ("GO:0042802","PMID:15962010", dict(action="KEEP_AS_NON_CORE", summary="Identical protein binding: SUMF2 forms homodimers.", reason="Real (homodimer) but generic; non-core.", supported_by=sb(US,"Homodimer and heterodimer with SUMF1"))),
 ("GO:0042802","GO_REF:0000120", dict(action="KEEP_AS_NON_CORE", summary="Identical protein binding (homodimer), IEA.", reason="Consistent with the homodimer; non-core.", supported_by=sb(US,"Homodimer and heterodimer with SUMF1"))),
 ("GO:0043687","Reactome:R-HSA-163841", dict(action="KEEP_AS_NON_CORE",
   summary="Post-translational protein modification (TAS): pathway context of sulfatase Cys->formylglycine maturation that SUMF2 modulates.",
   reason="Pathway-level context; SUMF2 modulates rather than performs this PTM. Non-core.", supported_by=None)),
 ("GO:0046479","Reactome:R-HSA-9840310", dict(action="KEEP_AS_NON_CORE",
   summary="Glycosphingolipid catabolic process (TAS): downstream consequence of sulfatase activity, which SUMF2 indirectly modulates by inhibiting SUMF1.",
   reason="Indirect/downstream pathway context; non-core.", supported_by=None)),
 ("GO:0004857","Reactome:R-HSA-1614336", dict(action="ACCEPT",
   summary="Enzyme inhibitor activity: SUMF2 inhibits the sulfatase-activating (formylglycine-generating) activity of SUMF1 via heterodimerization. This is SUMF2's defining molecular role.",
   reason="Core molecular function. Although catalytically dead as an FGE, SUMF2 acts as a negative regulator (inhibitor) of SUMF1, consistent with the UniProt FUNCTION statement.",
   supported_by=sb(US, SUMF2_FUNC))),
 ("GO:0005788","PMID:18266766", dict(action="ACCEPT", summary="ER lumen localization (EXP); SUMF2 is retained in the ER by canonical and non-canonical signals.", reason="Direct experimental support for core localization.", supported_by=sb(US,"Endoplasmic reticulum lumen"))),
 ("GO:0005783","PMID:18266766", dict(action="ACCEPT", summary="ER localization (IDA).", reason="Direct experimental support; consistent.", supported_by=None)),
 ("GO:0005788","Reactome:R-HSA-1614336", dict(action="ACCEPT", summary="ER lumen localization (TAS).", reason="Consistent core localization.", supported_by=None)),
]
sumf2_top = dict(
 status="DRAFT",
 description=(
   "SUMF2 (inactive C-alpha-formylglycine-generating enzyme 2) is an endoplasmic-reticulum-"
   "luminal paralog of SUMF1/FGE in the sulfatase-modifying-factor family. Unlike SUMF1, which "
   "converts an active-site cysteine of newly synthesized sulfatases into C-alpha-formylglycine "
   "(activating them), SUMF2 lacks the catalytic cysteine residues and has no formylglycine-"
   "generating activity. Its function is regulatory: SUMF2 forms homodimers and heterodimers "
   "with SUMF1 and inhibits SUMF1-mediated sulfatase activation, thereby acting as a negative "
   "modulator of cellular sulfatase activity (and downstream processes such as glycosaminoglycan "
   "and glycosphingolipid catabolism). It is broadly expressed and retained in the ER by "
   "canonical and non-canonical retention signals."),
 aliases=["pFGE","C7orf11","SUMF2 inactive FGE paralog"],
 references=[
   goref("GO_REF:0000033","Annotation inferences using phylogenetic trees"),
   goref("GO_REF:0000120","Combined Automated Annotation using Multiple IEA Methods"),
   ref("15962010", ("Sulfatase activities are regulated by SUMF1-SUMF2 interaction; SUMF2 inhibits SUMF1-mediated sulfatase activation.","Sulphatase activities are regulated by the interaction of sulphatase-modifying factor 1 with SUMF2"), review=HIGH_V),
   ref("18266766", ("SUMF2 (paralog of FGE) is retained in the ER by canonical and non-canonical signals.","Paralog of the formylglycine-generating enzyme--retention in the endoplasmic reticulum by canonical and noncanonical signals"), review=HIGH_V),
   ref("32814053", review=LOW_V),
   ref("32838362", review=LOW_V),
   ref("33845483", review=LOW_V),
   ref("36217030", review=LOW_V),
   reactome("Reactome:R-HSA-163841","Cysteine to formylglycine conversion (sulfatase maturation)"),
   reactome("Reactome:R-HSA-9840310","Glycosphingolipid metabolism / catabolism"),
   reactome("Reactome:R-HSA-1614336","Sulfatase activation by SUMF1 (FGE)"),
   {"id":US,"title":"UniProt entry Q8NBJ7 (SUMF2)","findings":[
     {"statement":"SUMF2 lacks formylglycine-generating activity and inhibits sulfatase activation by SUMF1.","supporting_text":SUMF2_FUNC},
     {"statement":"SUMF2 forms a homodimer and a heterodimer with SUMF1.","supporting_text":"Homodimer and heterodimer with SUMF1"}]},
 ],
 core_functions=[
   {"description":(
     "Catalytically inactive FGE paralog that negatively regulates SUMF1: by hetero-dimerizing "
     "with SUMF1 it inhibits formylglycine-generating (sulfatase-activating) activity, tuning "
     "cellular sulfatase output. Resides in the ER lumen."),
    "molecular_function":{"id":"GO:0004857","label":"enzyme inhibitor activity"},
    "locations":[{"id":"GO:0005788","label":"endoplasmic reticulum lumen"}],
    "supported_by":[{"reference_id":US,"supporting_text":SUMF2_FUNC},
                    {"reference_id":"PMID:15962010","supporting_text":"Sulphatase activities are regulated by the interaction of sulphatase-modifying factor 1 with SUMF2"}]},
 ],
 suggested_questions=[
   {"question":"Is SUMF2's inhibition of SUMF1 physiologically tuned (e.g. tissue-specific SUMF1:SUMF2 ratios) to set sulfatase activity set-points?"}],
 suggested_experiments=[
   {"hypothesis":"SUMF2 sets a rheostat on cellular sulfatase activation via the SUMF1:SUMF2 ratio.",
    "description":"Titrate SUMF2:SUMF1 expression ratios and measure formylglycine content and activity of multiple client sulfatases (e.g. ARSA, ARSB, SGSH)."}],
)

# ============================== PANK4 ==============================
UP = "file:human/PANK4/PANK4-uniprot.txt"
PANK4_NOT = dict(action="ACCEPT",
  summary="NOT (negated): PANK4 does NOT have pantothenate kinase activity. Although it belongs to the type II pantothenate kinase family, its kinase domain is degenerate; PANK4 is a 'pseudo-pantothenate kinase'.",
  reason="Correct, well-supported negation (IMP, PMID:30927326 'pseudo-pantothenate kinase'). The CAUTION flags the degenerate PanK domain. Retain.",
  supported_by=sb("PMID:30927326","Human pantothenate kinase 4 is a pseudo-pantothenate kinase"))
PANK4_PHOS = dict(action="ACCEPT",
  summary="Phosphatase activity: PANK4's C-terminal damage-control (DUF89) domain is a metal-dependent phosphatase that dephosphorylates 4'-phosphopantetheine (and related metabolites), a metabolite-repair / CoA-pathway regulatory activity.",
  reason="Core molecular function with direct experimental support (EXP, PMID:27322068; UniProt RecName '4'-phosphopantetheine phosphatase'). This is the protein's real activity, distinct from the dead PanK domain.",
  supported_by=sb(UP,"Phosphatase which shows a preference for 4'-"))
pank4 = [
 ("GO:0004594","GO_REF:0000033", PANK4_NOT),
 ("GO:0005634","GO_REF:0000033", dict(action="KEEP_AS_NON_CORE",
   summary="Nucleus (IBA, is_active_in). UniProt records PANK4 as cytoplasmic; the nuclear assignment is a phylogenetic inference not corroborated by the curated subcellular location.",
   reason="Likely over-propagated by IBA. PANK4 is reported cytoplasmic (UniProt); keep as non-core pending direct evidence rather than asserting it as a core location.",
   supported_by=sb(UP,"Cytoplasm"))),
 ("GO:0005829","GO_REF:0000033", dict(action="ACCEPT", summary="Cytosol (IBA), consistent with the curated cytoplasmic localization.", reason="Correct core localization.", supported_by=sb(UP,"Cytoplasm"))),
 ("GO:0016791","GO_REF:0000033", PANK4_PHOS),
 ("GO:0005524","GO_REF:0000002", dict(action="KEEP_AS_NON_CORE",
   summary="ATP binding (IEA) from the (degenerate) pantothenate-kinase domain signature.",
   reason="Plausible nucleotide binding by the kinase-like fold, but not the demonstrated catalytic activity (which is metal-dependent phosphatase). Non-core.", supported_by=None)),
 ("GO:0005737","GO_REF:0000044", dict(action="ACCEPT", summary="Cytoplasm (IEA).", reason="Correct, matches UniProt.", supported_by=sb(UP,"Cytoplasm"))),
 ("GO:0015937","GO_REF:0000002", dict(action="KEEP_AS_NON_CORE",
   summary="Coenzyme A biosynthetic process (IEA): PANK4's 4'-phosphopantetheine phosphatase activity acts on a CoA-pathway intermediate (metabolite repair / regulation).",
   reason="Correct pathway association via the phosphatase activity, but PANK4 modulates rather than performs core CoA biosynthesis; non-core.", supported_by=None)),
 ("GO:0015939","Reactome:R-HSA-199220", dict(action="KEEP_AS_NON_CORE",
   summary="Pantothenate metabolic process (TAS), pathway context (CoA/pantothenate).",
   reason="Pathway-level association; non-core.", supported_by=None)),
 ("GO:0016791","PMID:27322068", PANK4_PHOS),
 ("GO:0005737","GO_REF:0000024", dict(action="ACCEPT", summary="Cytoplasm (ISS).", reason="Consistent core localization.", supported_by=sb(UP,"Cytoplasm"))),
 ("GO:0004594","PMID:30927326", PANK4_NOT),
 ("GO:0005829","Reactome:R-HSA-9837419", dict(action="ACCEPT", summary="Cytosol (TAS).", reason="Consistent core localization.", supported_by=None)),
]
pank4_top = dict(
 status="DRAFT",
 description=(
   "PANK4 is a two-domain cytoplasmic enzyme of the pantothenate kinase family. Its N-terminal "
   "type II pantothenate-kinase-like domain is catalytically degenerate: PANK4 has no "
   "pantothenate kinase activity and is a 'pseudo-pantothenate kinase'. Its functional activity "
   "resides in the C-terminal damage-control (DUF89) domain, a metal-dependent (Mg2+/Mn2+) "
   "phosphatase that dephosphorylates 4'-phosphopantetheine and related metabolites (e.g. "
   "pantetheine-phosphate sulfonate). Through this 4'-phosphopantetheine phosphatase activity "
   "PANK4 participates in coenzyme-A pathway homeostasis / metabolite repair. It is widely "
   "expressed, with high levels in muscle, and forms homodimers. PANK4 thus illustrates a "
   "domain-swap pseudoenzyme: a dead ancestral catalytic domain alongside a retained, distinct "
   "enzymatic activity."),
 aliases=["Pantothenate kinase 4","Pseudo-pantothenate kinase","4'-phosphopantetheine phosphatase"],
 references=[
   goref("GO_REF:0000002","GO annotation through association of InterPro records with GO terms"),
   goref("GO_REF:0000024","Manual transfer of experimentally-verified annotations to orthologs by curator judgment (ISS)"),
   goref("GO_REF:0000033","Annotation inferences using phylogenetic trees"),
   goref("GO_REF:0000044","GO annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping"),
   ref("27322068", ("PANK4 belongs to a family of metal-dependent phosphatases implicated in metabolite damage-control; it dephosphorylates 4'-phosphopantetheine.","A family of metal-dependent phosphatases implicated in metabolite damage-control"), review=HIGH_V),
   ref("30927326", ("Human PANK4 is a pseudo-pantothenate kinase (no PanK activity).","Human pantothenate kinase 4 is a pseudo-pantothenate kinase"), review=HIGH_V),
   reactome("Reactome:R-HSA-199220","Pantothenate and CoA biosynthesis"),
   reactome("Reactome:R-HSA-9837419","Metabolism / cytosolic reaction (PANK4)"),
   {"id":UP,"title":"UniProt entry Q9NVE7 (PANK4)","findings":[
     {"statement":"PANK4 is a phosphatase preferring 4'-phosphopantetheine; its PanK domain is degenerate.","supporting_text":"Phosphatase which shows a preference for 4'-"}]},
 ],
 core_functions=[
   {"description":(
     "Metal-dependent 4'-phosphopantetheine phosphatase (damage-control/metabolite-repair "
     "enzyme) acting in coenzyme-A pathway homeostasis. The ancestral pantothenate-kinase "
     "domain is catalytically dead."),
    "molecular_function":{"id":"GO:0016791","label":"phosphatase activity"},
    "locations":[{"id":"GO:0005829","label":"cytosol"}],
    "supported_by":[{"reference_id":"PMID:27322068","supporting_text":"A family of metal-dependent phosphatases implicated in metabolite damage-control"},
                    {"reference_id":UP,"supporting_text":"Phosphatase which shows a preference for 4'-"}]},
 ],
 suggested_questions=[
   {"question":"What is the precise physiological substrate spectrum of PANK4's phosphatase activity, and does it regulate CoA levels in vivo (e.g. in muscle)?"}],
 suggested_experiments=[
   {"hypothesis":"PANK4 phosphatase activity regulates intracellular CoA/4'-phosphopantetheine pools.",
    "description":"Measure 4'-phosphopantetheine and CoA levels in PANK4-knockout vs wild-type cells/tissues, with rescue by phosphatase-dead PANK4."}],
)

# ============================== NAALADL2 ==============================
UN = "file:human/NAALADL2/NAALADL2-uniprot.txt"
naaladl2 = [
 ("GO:0016020","GO_REF:0000044", dict(action="ACCEPT",
   summary="Membrane localization (IEA); UniProt predicts a single-pass type II membrane protein.",
   reason="Consistent with predicted topology; core localization.", supported_by=sb(UN,"Single-pass type II"))),
 ("GO:0005515","PMID:25416956", dict(action="MARK_AS_OVER_ANNOTATED",
   summary="Generic 'protein binding' from a large-scale binary interactome screen (HuRI).",
   reason="High-throughput, uninformative about molecular function; over-annotation.")),
 ("GO:0005654","GO_REF:0000052", dict(action="KEEP_AS_NON_CORE",
   summary="Nucleoplasm (IDA from immunofluorescence/HPA). This conflicts with the UniProt prediction of a single-pass type II membrane protein; the antibody-based localization is not obviously reconcilable with the predicted topology.",
   reason="Experimental (IDA) localization that is hard to reconcile with the predicted membrane topology; retain as non-core but flag the discrepancy. Confirmation with orthogonal methods is needed before treating nuclear localization as established.",
   supported_by=sb(UN,"Single-pass type II"))),
]
naaladl2_top = dict(
 status="DRAFT",
 description=(
   "NAALADL2 (inactive N-acetylated-alpha-linked acidic dipeptidase-like protein 2) is a "
   "predicted single-pass type II membrane glycoprotein of the M28 metallopeptidase family "
   "(M28B subfamily, related to glutamate carboxypeptidase II / NAALADase / PSMA). Unlike "
   "active family members, NAALADL2 lacks the conserved zinc-binding and active-site residues "
   "and is predicted to be catalytically inactive (no peptidase/hydrolase activity). Its "
   "molecular function is not established. The gene spans a very large, structurally variable "
   "locus and has been linked through genetic association to several traits and cancers, but a "
   "defined biochemical or cellular role for the protein remains unknown."),
 aliases=["NAALADASEL2","Inactive NAALADase-like protein 2"],
 references=[
   goref("GO_REF:0000044","GO annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping"),
   goref("GO_REF:0000052","GO annotation based on curation of immunofluorescence data (HPA)"),
   ref("25416956", review=LOW_V),
   {"id":UN,"title":"UniProt entry Q58DX5 (NAALADL2)","findings":[
     {"statement":"NAALADL2 is related to the M28 peptidase family but lacks zinc-binding/active sites and may be catalytically inactive.","supporting_text":"May be catalytically inactive"}]},
 ],
 core_functions=[
   {"description":(
     "Molecular function not established. NAALADL2 is a predicted catalytically inactive member "
     "of the M28B metallopeptidase subfamily (it lacks the zinc-binding/active-site residues of "
     "active NAALADases such as GCPII/PSMA); no specific enzymatic, binding, or signaling "
     "function has been experimentally defined."),
    "supported_by":[{"reference_id":UN,"supporting_text":"May be catalytically inactive"}]},
 ],
 suggested_questions=[
   {"question":"Does NAALADL2 retain any residual substrate binding (without catalysis), and what is its true subcellular localization given the conflict between predicted membrane topology and the reported nucleoplasm staining?"}],
 suggested_experiments=[
   {"hypothesis":"NAALADL2 is a catalytically dead membrane protein with a non-enzymatic (e.g. adhesion/scaffold) role.",
    "description":"Determine NAALADL2 topology and localization with tagged constructs and confirm absence of NAALADase activity in a peptidase assay; pull down interactors to probe for a scaffolding function."}],
)

build("RHBDF1", rhbdf1, rhbdf1_top)
build("SUMF2", sumf2, sumf2_top)
build("PANK4", pank4, pank4_top)
build("NAALADL2", naaladl2, naaladl2_top)
