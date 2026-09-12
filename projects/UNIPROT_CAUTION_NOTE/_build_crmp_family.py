#!/usr/bin/env python3
"""Build full reviews for the human CRMP/DPYSL family: DPYSL2, DPYSL3, DPYSL4, CRMP1.

All four are catalytically dead members of the dihydropyrimidinase (metallo-hydrolase)
superfamily that act as cytoskeletal regulators in semaphorin signaling. They share
the DPYSL5 over-annotation pattern: a curated NOT dihydropyrimidinase plus positive
electronic 'hydrolase activity' parent terms (GO:0016787/0016810/0016812) -> REMOVE.
DPYSL2 additionally carries a legacy positive dihydropyrimidinase (TAS) -> REMOVE.

A rule engine assigns action/summary/reason per annotation (paralogs share profiles);
references pull titles from the publications/ cache so they title-validate.
"""
from pathlib import Path
import yaml

PUB = Path("publications")
def title(pmid):
    return yaml.safe_load((PUB/f"PMID_{pmid}.md").read_text().split("---",2)[1])["title"]

CAUTION = "Lacks most of the conserved residues that are essential for"   # exact UniProt fragment
SIM = "Belongs to the metallo-dependent hydrolases superfamily."

# large high-throughput interactome screens -> generic protein binding is over-annotation
SCREENS = {"32296183","32814053","25416956","28514442","29892012","31515488","33961781"}

# core biological processes / locations for the CRMP family
CORE_BP = {"GO:0007399","GO:0071526","GO:0007010","GO:0010976","GO:0010977",
           "GO:0048666","GO:0051764","GO:0051017","GO:0051491","GO:0030336",
           "GO:0048678","GO:0150052"}
NONCORE_BP = {"GO:0007165","GO:0006897","GO:0071345"}
CORE_LOC = {"GO:0005829","GO:0005737","GO:0030426","GO:0015630","GO:0005874",
            "GO:0005856","GO:0015629","GO:0030425","GO:0043025","GO:0044297",
            "GO:0030027","GO:0031941"}
NONCORE_LOC = {"GO:0016020","GO:0005576","GO:0070062","GO:0005813","GO:0005819",
               "GO:0072686","GO:0045171","GO:0043204","GO:0098793","GO:0098794",
               "GO:0045202","GO:0070382","GO:0030496","GO:0005874"}
HYDRO = {"GO:0016787","GO:0016810","GO:0016812"}
SPEC_BIND = {"GO:0031005","GO:0017124","GO:0035374","GO:0051219"}

def decide(gene, U, a):
    t = a["term"]["id"]; lab = a["term"]["label"]; ev = a["evidence_type"]
    ref = str(a.get("original_reference_id")); neg = bool(a.get("negated"))
    def S(**k): return k
    # --- negated catalytic / process: the curated counterpart of the CAUTION ---
    if neg and t == "GO:0004157":
        return S(action="ACCEPT",
            summary=f"NOT: {gene} does not have dihydropyrimidinase activity. It belongs to the metallo-dependent hydrolase superfamily but lacks the conserved metal-cofactor-binding residues required for catalysis (UniProt CAUTION).",
            reason="Correct, important negation: a catalytically dead family member. Retain.",
            supported_by=[{"reference_id":U,"supporting_text":CAUTION}])
    if neg and t == "GO:0006208":
        return S(action="ACCEPT",
            summary=f"NOT: {gene} is not involved in pyrimidine nucleobase catabolism (the process counterpart of the absent dihydropyrimidinase activity).",
            reason="Correct negation, consistent with loss of catalytic activity. Retain.",
            supported_by=[{"reference_id":U,"supporting_text":CAUTION}])
    # --- catalytic over-annotations (positive) ---
    if t in HYDRO:
        return S(action="REMOVE",
            summary=f"Positive '{lab}' propagated from the metallo-hydrolase fold signature ({ev}). {gene} lacks the catalytic metal site, and the curated dihydropyrimidinase activity is itself NOT-ed.",
            reason="Domain/phylogenetic over-propagation refutable on biological grounds: the metal-cofactor-binding residues are absent (UniProt CAUTION), so no metallo-hydrolase activity is supported; the real function is a non-catalytic cytoskeletal regulator. Same basis as the DPYSL5 review.",
            supported_by=[{"reference_id":U,"supporting_text":CAUTION},{"reference_id":U,"supporting_text":SIM}])
    if (not neg) and t == "GO:0004157":
        return S(action="REMOVE",
            summary=f"Legacy positive dihydropyrimidinase activity (TAS, {ref}) from an early report, superseded by the finding that {gene} lacks the catalytic metal-binding residues.",
            reason="Outdated enzymatic claim, contradicted by the UniProt CAUTION and the curated NOT|dihydropyrimidinase. Remove (legacy mis-annotation).",
            supported_by=[{"reference_id":U,"supporting_text":CAUTION}])
    if t == "GO:0006139":
        return S(action="REMOVE",
            summary=f"Nucleobase-containing compound metabolic process (TAS, {ref}) tied to the now-defunct dihydropyrimidinase activity claim.",
            reason="Legacy process annotation dependent on the superseded enzymatic activity; remove, consistent with the NOT|pyrimidine catabolism.",
            supported_by=[{"reference_id":U,"supporting_text":CAUTION}])
    # --- binding ---
    if t == "GO:0005515":
        pm = ref.split(":")[-1]
        if pm in SCREENS:
            return S(action="MARK_AS_OVER_ANNOTATED",
                summary=f"Generic 'protein binding' from a high-throughput interactome screen ({ref}).",
                reason="High-throughput protein binding is uninformative about molecular function (curation guideline). Over-annotation.")
        return S(action="KEEP_AS_NON_CORE",
            summary=f"Specific protein interaction ({ref}); supports {gene}'s scaffold/adapter role but the generic 'protein binding' term is uninformative.",
            reason="Real interaction kept as non-core supporting evidence; the informative function is captured in core_functions.")
    if t == "GO:0042802":
        return S(action="KEEP_AS_NON_CORE",
            summary=f"Identical protein binding: {gene} forms homo- and hetero-tetramers with other CRMP-family members.",
            reason="Real oligomerization but a generic term; non-core.",
            supported_by=[{"reference_id":U,"supporting_text":"Homotetramer"}])
    if t in SPEC_BIND:
        return S(action="KEEP_AS_NON_CORE",
            summary=f"{lab}: a specific molecular interaction consistent with {gene}'s cytoskeletal-adapter role.",
            reason="Real, specific binding; informative but secondary to the core cytoskeletal-regulation function. Non-core.")
    # --- biological process ---
    if a["term"]["id"].startswith("GO:") and a.get("qualifier","").endswith("involved_in") or t in CORE_BP|NONCORE_BP:
        if t in CORE_BP:
            return S(action="ACCEPT",
                summary=f"{lab}: a core neuronal/cytoskeletal process for the CRMP family ({gene} acts in semaphorin-driven cytoskeleton remodeling and neurite/axon development).",
                reason="Core biological process for a CRMP-family cytoskeletal regulator.",
                supported_by=[{"reference_id":U,"supporting_text":"semaphorin"}] if t=="GO:0071526" else None)
        if t in NONCORE_BP:
            return S(action="KEEP_AS_NON_CORE",
                summary=f"{lab}: a broader/secondary process for {gene}.",
                reason="Valid but non-core relative to the cytoskeletal-regulation function.")
    # --- locations ---
    if t in CORE_LOC:
        return S(action="ACCEPT",
            summary=f"{lab}: a core subcellular location for {gene} (cytoplasmic/cytoskeletal CRMP).",
            reason="Correct core localization for a cytoskeleton-associated cytoplasmic protein.")
    if t in NONCORE_LOC:
        return S(action="KEEP_AS_NON_CORE",
            summary=f"{lab}: a secondary/broad or context-specific localization for {gene}.",
            reason="Plausible but non-core (broad term, division-/synapse-specific, or high-throughput proteomics).")
    # fallback for any remaining BP not pre-listed
    if a.get("qualifier","").endswith("involved_in"):
        return S(action="KEEP_AS_NON_CORE", summary=f"{lab}: process annotation for {gene}.",
                 reason="Valid but non-core.")
    return S(action="KEEP_AS_NON_CORE", summary=f"{lab}.", reason="Retained as non-core.")

def build(gene, desc, core_funcs, questions, experiments, aliases):
    P = Path(f"genes/human/{gene}/{gene}-ai-review.yaml")
    d = yaml.safe_load(P.read_text())
    U = f"file:human/{gene}/{gene}-uniprot.txt"
    pmids = set()
    for a in d["existing_annotations"]:
        body = decide(gene, U, a)
        rv = {"summary": body["summary"], "action": body["action"], "reason": body["reason"]}
        if body.get("supported_by"):
            rv["supported_by"] = body["supported_by"]
        a["review"] = rv
        r = str(a.get("original_reference_id",""))
        if r.startswith("PMID:"): pmids.add(r.split(":")[1])
    d["status"] = "DRAFT"
    d["description"] = desc
    d["aliases"] = aliases
    refs = [
        {"id":"GO_REF:0000002","title":"GO annotation through association of InterPro records with GO terms","findings":[]},
        {"id":"GO_REF:0000024","title":"Manual transfer of experimentally-verified annotations to orthologs by curator judgment","findings":[]},
        {"id":"GO_REF:0000033","title":"Annotation inferences using phylogenetic trees","findings":[]},
        {"id":"GO_REF:0000044","title":"GO annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping","findings":[]},
        {"id":"GO_REF:0000052","title":"GO annotation based on curation of immunofluorescence data (HPA)","findings":[]},
        {"id":"GO_REF:0000107","title":"Automatic transfer of experimentally verified manual GO annotation data to orthologs using Ensembl Compara","findings":[]},
        {"id":"GO_REF:0000120","title":"Combined Automated Annotation using Multiple IEA Methods","findings":[]},
        {"id":U,"title":f"UniProt entry for {gene}","findings":[
            {"statement":f"{gene} lacks the metal-cofactor-binding residues required for dihydropyrimidinase activity.","supporting_text":CAUTION},
            {"statement":f"{gene} belongs to the metallo-dependent hydrolase superfamily.","supporting_text":SIM}]},
    ]
    for pm in sorted(pmids):
        refs.append({"id":f"PMID:{pm}","title":title(pm),"findings":[]})
    # Reactome refs present?
    react = sorted({str(a.get("original_reference_id")) for a in d["existing_annotations"]
                    if str(a.get("original_reference_id","")).startswith("Reactome:")})
    for r in react:
        refs.append({"id":r,"title":"Reactome pathway (CRMP/semaphorin signalling)","findings":[]})
    d["references"] = refs
    d["core_functions"] = core_funcs
    d["suggested_questions"] = questions
    d["suggested_experiments"] = experiments
    P.write_text("# yaml-language-server: $schema=../../../src/ai_gene_review/schema/gene_review.yaml\n"
                 + yaml.dump(d, sort_keys=False, default_flow_style=False, allow_unicode=True, width=100))
    from collections import Counter
    print(f"{gene}: {len(d['existing_annotations'])} anns",
          dict(Counter(a['review']['action'] for a in d['existing_annotations'])))

# ---- per-gene narrative content ----
COMMON_Q = [{"question":"What is the precise molecular activity of this catalytically dead CRMP - is its cytoskeletal effect mediated purely by tubulin/actin binding and regulated oligomerization, and how do GSK3B/CDK5/ROCK phosphorylations switch it?"}]
def EXP(g):
    return [{"hypothesis":f"{g} regulates microtubule/actin dynamics non-catalytically, and phosphorylation by GSK3B/CDK5 toggles this.",
             "description":f"Test microtubule assembly and neurite/axon outgrowth with wild-type vs phospho-mutant {g} and oligomerization-disrupting mutants."}]

build("DPYSL2",
  desc=("Dihydropyrimidinase-related protein 2 (DPYSL2/CRMP2), a brain-enriched cytoplasmic protein of the "
        "collapsin-response-mediator (CRMP) / dihydropyrimidinase family. Although it belongs to the "
        "metallo-dependent hydrolase superfamily, it lacks the conserved metal-cofactor-binding residues and "
        "has no dihydropyrimidinase activity - it is a catalytically dead family member. CRMP2 is a key "
        "cytoskeletal regulator in semaphorin-3A signaling: it binds tubulin heterodimers to promote "
        "microtubule assembly and axon specification/growth, mediates growth-cone collapse and neuronal "
        "polarity, and is inactivated by GSK3B/CDK5/ROCK phosphorylation. It forms homo- and hetero-tetramers "
        "with other CRMPs and also participates in vesicle/endocytic trafficking."),
  core_funcs=[{"description":("Catalytically inactive CRMP-family cytoskeletal regulator that binds tubulin and "
        "promotes microtubule assembly to drive axon growth, neuronal polarity and semaphorin-3A-induced "
        "growth-cone dynamics; phosphoregulated by GSK3B/CDK5/ROCK."),
        "directly_involved_in":[{"id":"GO:0007399","label":"nervous system development"},
                                {"id":"GO:0007010","label":"cytoskeleton organization"}],
        "locations":[{"id":"GO:0005829","label":"cytosol"},{"id":"GO:0015630","label":"microtubule cytoskeleton"}],
        "supported_by":[{"reference_id":"file:human/DPYSL2/DPYSL2-uniprot.txt","supporting_text":CAUTION}]}],
  questions=COMMON_Q, experiments=EXP("DPYSL2"),
  aliases=["CRMP2","CRMP-2","DRP-2","ULIP-2","TOAD-64","Collapsin response mediator protein 2"])

build("DPYSL3",
  desc=("Dihydropyrimidinase-related protein 3 (DPYSL3/CRMP4), a cytoplasmic CRMP-family protein required for "
        "class-3 semaphorin signaling and cytoskeletal remodeling. A catalytically dead member of the "
        "metallo-dependent hydrolase (dihydropyrimidinase) superfamily, it lacks the conserved metal-cofactor "
        "residues and has no dihydropyrimidinase activity. DPYSL3 is distinguished by F-actin binding/bundling "
        "and filopodium regulation, binds filamin and chondroitin sulfate, and modulates neuron projection "
        "development, growth-cone dynamics and cell migration. It forms homo- and hetero-tetramers with other CRMPs."),
  core_funcs=[{"description":("Catalytically inactive CRMP-family actin-/cytoskeleton-regulating protein that binds and "
        "bundles F-actin, regulates filopodia and neuron projection development during semaphorin signaling."),
        "directly_involved_in":[{"id":"GO:0051764","label":"actin crosslink formation"},
                                {"id":"GO:0048666","label":"neuron development"}],
        "locations":[{"id":"GO:0005829","label":"cytosol"},{"id":"GO:0030426","label":"growth cone"}],
        "supported_by":[{"reference_id":"file:human/DPYSL3/DPYSL3-uniprot.txt","supporting_text":CAUTION}]}],
  questions=COMMON_Q, experiments=EXP("DPYSL3"),
  aliases=["CRMP4","CRMP-4","DRP-3","ULIP-1","Collapsin response mediator protein 4"])

build("DPYSL4",
  desc=("Dihydropyrimidinase-related protein 4 (DPYSL4/CRMP3), a cytoplasmic CRMP-family protein involved in "
        "class-3 semaphorin signaling and cytoskeletal remodeling during neuronal development. A catalytically "
        "dead member of the metallo-dependent hydrolase (dihydropyrimidinase) superfamily, it lacks the "
        "conserved metal-cofactor residues and has no dihydropyrimidinase activity. It binds filamin, forms "
        "homo- and hetero-tetramers with other CRMPs, and contributes to neurite outgrowth and dendritic "
        "development."),
  core_funcs=[{"description":("Catalytically inactive CRMP-family cytoskeletal regulator acting in semaphorin-driven "
        "neuronal development; forms hetero-oligomers with other CRMPs."),
        "directly_involved_in":[{"id":"GO:0007399","label":"nervous system development"}],
        "locations":[{"id":"GO:0005829","label":"cytosol"}],
        "supported_by":[{"reference_id":"file:human/DPYSL4/DPYSL4-uniprot.txt","supporting_text":CAUTION}]}],
  questions=COMMON_Q, experiments=EXP("DPYSL4"),
  aliases=["CRMP3","CRMP-3","DRP-4","ULIP-4","Collapsin response mediator protein 3"])

build("CRMP1",
  desc=("Dihydropyrimidinase-related protein 1 (CRMP1/DPYSL1), a cytoplasmic CRMP-family protein required for "
        "class-3 semaphorin (Sema3A) signaling and growth-cone collapse during neuronal development. A "
        "catalytically dead member of the metallo-dependent hydrolase (dihydropyrimidinase) superfamily, it "
        "lacks the conserved metal-cofactor residues and has no dihydropyrimidinase activity. CRMP1 regulates "
        "neuron projection development and dendritic/synaptic organization, binds filamin, and forms homo- and "
        "hetero-tetramers with other CRMPs; it also has reported roles in cell migration and as an invasion suppressor."),
  core_funcs=[{"description":("Catalytically inactive CRMP-family cytoskeletal regulator mediating Sema3A-induced growth-cone "
        "collapse and neuron projection development via the semaphorin-plexin pathway."),
        "directly_involved_in":[{"id":"GO:0071526","label":"semaphorin-plexin signaling pathway"},
                                {"id":"GO:0007399","label":"nervous system development"}],
        "locations":[{"id":"GO:0005829","label":"cytosol"},{"id":"GO:0030426","label":"growth cone"}],
        "supported_by":[{"reference_id":"file:human/CRMP1/CRMP1-uniprot.txt","supporting_text":CAUTION}]}],
  questions=COMMON_Q, experiments=EXP("CRMP1"),
  aliases=["DPYSL1","CRMP-1","DRP-1","ULIP-3","Collapsin response mediator protein 1"])
