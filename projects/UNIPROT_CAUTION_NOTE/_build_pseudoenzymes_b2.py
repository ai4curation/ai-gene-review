#!/usr/bin/env python3
"""Build full reviews for four net-new pseudoenzymes flagged by the UniProt-wide
query: ILK (pseudokinase scaffold), ROR1 (pseudokinase Wnt coreceptor),
CASP12 (pseudo-caspase), AZIN2 (dead ODC paralog / antizyme inhibitor).

Each gene supplies an OVERRIDE table for its meaningful terms (catalytic REMOVEs,
NOT ACCEPTs, core MF/BP); generic binding/location/process annotations are handled
by shared rules. References pull titles from the publications/ cache.
"""
from pathlib import Path
import yaml
from collections import Counter

PUB = Path("publications")
def title(pmid):
    return yaml.safe_load((PUB/f"PMID_{pmid}.md").read_text().split("---",2)[1])["title"]

SCREENS = {"25416956","28514442","29892012","31515488","32296183","33961781",
           "32814053","21516116","40205054"}

def build(gene, U, desc, aliases, overrides, core_loc, core_bp, core_funcs,
          questions, experiments, screens=SCREENS):
    P = Path(f"genes/human/{gene}/{gene}-ai-review.yaml")
    d = yaml.safe_load(P.read_text())
    pmids = set(); react = set()
    for a in d["existing_annotations"]:
        t = a["term"]["id"]; lab = a["term"]["label"]; ev = a["evidence_type"]
        qual = a.get("qualifier",""); neg = bool(a.get("negated"))
        ref = str(a.get("original_reference_id","")); pm = ref.split(":")[-1]
        key = (t, neg)
        if key in overrides:
            act, summ, rea, sb = overrides[key]
        elif t == "GO:0005515":
            if pm in screens:
                act, summ, rea, sb = ("MARK_AS_OVER_ANNOTATED",
                    f"Generic 'protein binding' from a high-throughput interactome screen ({ref}).",
                    "High-throughput protein binding is uninformative about molecular function (curation guideline). Over-annotation.", None)
            else:
                act, summ, rea, sb = ("KEEP_AS_NON_CORE",
                    f"Specific protein interaction ({ref}) consistent with {gene}'s scaffold/adapter role.",
                    "Real interaction kept as non-core supporting evidence; the generic 'protein binding' term is itself uninformative.", None)
        elif t == "GO:0042802":
            act, summ, rea, sb = ("KEEP_AS_NON_CORE", f"Identical protein binding ({lab}).",
                "Real but generic; non-core.", None)
        elif qual.endswith("involved_in") or qual.startswith("acts_upstream"):
            if t in core_bp:
                act, summ, rea, sb = ("ACCEPT", f"{lab}: a core biological process for {gene}.",
                    f"Core process consistent with {gene}'s established function.", None)
            else:
                act, summ, rea, sb = ("KEEP_AS_NON_CORE", f"{lab}: process annotation for {gene}.",
                    "Valid but non-core / secondary.", None)
        elif qual.startswith("located_in") or qual.startswith("is_active_in") or qual.startswith("part_of") or qual.startswith("colocalizes"):
            if t in core_loc:
                act, summ, rea, sb = ("ACCEPT", f"{lab}: a core subcellular location for {gene}.",
                    "Correct core localization.", None)
            else:
                act, summ, rea, sb = ("KEEP_AS_NON_CORE", f"{lab}: a secondary/broad localization for {gene}.",
                    "Plausible but non-core (broad term or context-specific).", None)
        else:
            act, summ, rea, sb = ("KEEP_AS_NON_CORE", f"{lab}.", "Retained as non-core.", None)
        rv = {"summary": summ, "action": act, "reason": rea}
        if sb: rv["supported_by"] = sb
        a["review"] = rv
        if ref.startswith("PMID:"): pmids.add(pm)
        if ref.startswith("Reactome:"): react.add(ref)

    d["status"] = "DRAFT"; d["description"] = desc; d["aliases"] = aliases
    refs = [
        {"id":"GO_REF:0000002","title":"GO annotation through association of InterPro records with GO terms","findings":[]},
        {"id":"GO_REF:0000024","title":"Manual transfer of experimentally-verified annotations to orthologs by curator judgment","findings":[]},
        {"id":"GO_REF:0000033","title":"Annotation inferences using phylogenetic trees","findings":[]},
        {"id":"GO_REF:0000044","title":"GO annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping","findings":[]},
        {"id":"GO_REF:0000052","title":"GO annotation based on curation of immunofluorescence data (HPA)","findings":[]},
        {"id":"GO_REF:0000107","title":"Automatic transfer of experimentally verified manual GO annotation data to orthologs using Ensembl Compara","findings":[]},
        {"id":"GO_REF:0000108","title":"Automatic assignment of GO terms using logical inference, based on inter-ontology links","findings":[]},
        {"id":"GO_REF:0000117","title":"Automatic GO annotation from UniProtKB-KW mapping","findings":[]},
        {"id":"GO_REF:0000120","title":"Combined Automated Annotation using Multiple IEA Methods","findings":[]},
        {"id":U,"title":f"UniProt entry for {gene}","findings":[]},
    ]
    for pm in sorted(pmids):
        refs.append({"id":f"PMID:{pm}","title":title(pm),"findings":[]})
    for r in sorted(react):
        refs.append({"id":r,"title":"Reactome pathway","findings":[]})
    d["references"] = refs
    d["core_functions"] = core_funcs
    d["suggested_questions"] = questions
    d["suggested_experiments"] = experiments
    P.write_text("# yaml-language-server: $schema=../../../src/ai_gene_review/schema/gene_review.yaml\n"
                 + yaml.dump(d, sort_keys=False, default_flow_style=False, allow_unicode=True, width=100))
    print(f"{gene}: {len(d['existing_annotations'])} anns",
          dict(Counter(a['review']['action'] for a in d['existing_annotations'])))

def ov(action, summary, reason, sb=None): return (action, summary, reason, sb)

# ============================ ILK ============================
UILK="file:human/ILK/ILK-uniprot.txt"
ILK_CAU="Now thought to be a pseudokinase which does not have kinase activity and which functions solely as a scaffold protein"
ilk_over = {
 ("GO:0004674", True): ov("ACCEPT",
   "NOT: ILK does not have protein serine/threonine kinase activity. Structural and biochemical work established it as a pseudokinase scaffold (UniProt now names it 'Scaffold protein ILK').",
   "Correct, important negation supported by direct evidence (IDA). Retain.",
   [{"reference_id":UILK,"supporting_text":ILK_CAU}]),
 ("GO:0004672", False): ov("REMOVE",
   "Positive 'protein kinase activity' (IEA) propagated from the protein-kinase-superfamily (TKL) signature. ILK is a pseudokinase with a degenerate catalytic site and no kinase activity.",
   "Electronic over-propagation refuted on biological grounds: ILK is established as a catalytically dead scaffold (the curated NOT|ser/thr kinase). Remove.",
   [{"reference_id":UILK,"supporting_text":ILK_CAU}]),
 ("GO:0030674", False): ov("ACCEPT",
   "Protein-macromolecule adaptor activity: ILK's actual molecular function as the scaffold of the IPP (ILK-PINCH-PARVIN) complex linking integrins to the actin cytoskeleton.",
   "Core molecular function for the pseudokinase scaffold. Retain.",
   [{"reference_id":UILK,"supporting_text":"Scaffold protein which mediates protein-protein interactions"}]),
 ("GO:0005524", False): ov("KEEP_AS_NON_CORE",
   "ATP binding: ILK's pseudokinase domain still binds ATP/Mg despite lacking catalytic activity (IDA).",
   "Real (structurally demonstrated) nucleotide binding but not catalytic; non-core for a scaffold.", None),
 ("GO:0000287", False): ov("KEEP_AS_NON_CORE",
   "Magnesium ion binding (IDA) by the pseudokinase domain, associated with ATP binding.",
   "Real but non-core (no catalytic role).", None),
 ("GO:0005178", False): ov("ACCEPT",
   "Integrin binding (IDA): ILK binds integrin beta cytoplasmic tails, central to its focal-adhesion scaffold role.",
   "Core, experimentally supported interaction defining ILK's adhesion function.", None),
 ("GO:0019901", False): ov("KEEP_AS_NON_CORE",
   "Protein kinase binding (IPI): ILK scaffolds/associates with kinases at adhesions.",
   "Specific interaction supporting the scaffold role; non-core.", None),
}
ILK_CORE_LOC = {"GO:0005925","GO:0005737","GO:0005829","GO:0005886","GO:0005938","GO:0030017"}
ILK_CORE_BP = {"GO:0007229","GO:0007160","GO:0034446","GO:1900026","GO:0072697"}

# ============================ ROR1 ============================
UROR="file:human/ROR1/ROR1-uniprot.txt"
ROR_CAU="The kinase domain has very low catalytic activity in vitro"
ror_over = {
 ("GO:0004714", True): ov("ACCEPT",
   "NOT: ROR1 does not have transmembrane receptor tyrosine kinase activity. Its kinase domain is degenerate (very low activity in vitro; does not bind ATP) - an inactive/pseudokinase RTK.",
   "Correct, important negation. Retain.",
   [{"reference_id":UROR,"supporting_text":ROR_CAU}]),
 ("GO:0007169", True): ov("ACCEPT",
   "NOT: ROR1 is not involved in cell-surface receptor protein tyrosine kinase signaling (as a catalytic RTK).",
   "Correct negation, consistent with the inactive kinase domain. Retain.", None),
 ("GO:0005524", True): ov("ACCEPT",
   "NOT: ROR1 does not bind ATP (IDA) - its degenerate kinase domain lacks nucleotide binding.",
   "Correct negation with direct evidence; underpins the pseudokinase classification. Retain.",
   [{"reference_id":UROR,"supporting_text":"Does not bind ATP"}]),
 ("GO:0004672", False): ov("REMOVE",
   "Positive 'protein kinase activity' (IEA) from the protein-kinase-superfamily signature. ROR1 is an inactive/pseudokinase receptor.",
   "Electronic over-propagation contradicted by the curated NOTs and the CAUTION (degenerate kinase, no ATP binding). Remove.",
   [{"reference_id":UROR,"supporting_text":ROR_CAU}]),
 ("GO:0004714", False): ov("REMOVE",
   "Legacy positive transmembrane RTK activity (TAS, PMID:8875995) from the original cloning report, superseded by the demonstration that the kinase domain is inactive.",
   "Outdated enzymatic claim, contradicted by the curated NOT|RTK activity and the CAUTION. Remove.",
   [{"reference_id":UROR,"supporting_text":ROR_CAU}]),
 ("GO:0007169", False): ov("REMOVE",
   "Legacy positive cell-surface RTK signaling (TAS) tied to the now-refuted catalytic-receptor model.",
   "Superseded process annotation, contradicted by the curated NOT. Remove.", None),
 ("GO:0042813", False): ov("ACCEPT",
   "Wnt receptor activity (IMP): ROR1 acts as a receptor/coreceptor for Wnt ligands (notably Wnt5a) - its real signaling function.",
   "Core molecular function for ROR1 as a (non-catalytic) Wnt receptor. Retain.", None),
 ("GO:0017147", False): ov("ACCEPT",
   "Wnt-protein binding: ROR1 binds Wnt ligands via its extracellular CRD, central to its coreceptor role.",
   "Core, ligand-binding function. Retain.", None),
 ("GO:0015026", False): ov("ACCEPT",
   "Coreceptor activity: ROR1 functions as a Wnt coreceptor in non-canonical Wnt signaling.",
   "Core function consistent with the Wnt-receptor role. Retain.", None),
 ("GO:0038023", False): ov("ACCEPT",
   "Signaling receptor activity (IDA): ROR1 transduces signals as a cell-surface receptor independent of catalytic activity.",
   "Core receptor function. Retain.", None),
}
ROR_CORE_LOC = {"GO:0005886","GO:0030424","GO:0043679","GO:0043235","GO:0016020"}
ROR_CORE_BP = {"GO:0016055","GO:0043123","GO:0048839","GO:0007605","GO:0008283"}

# ============================ CASP12 ============================
UCAS="file:human/CASP12/CASP12-uniprot.txt"
cas_over = {
 ("GO:0004197", True): ov("ACCEPT",
   "NOT: CASP12 does not have cysteine-type endopeptidase activity (IKR, inferred from key catalytic residues). Human caspase-12 is an inactive 'pseudo-caspase'.",
   "Correct negation based on key active-site residues. Retain.", None),
 ("GO:0004197", False): ov("REMOVE",
   "Positive cysteine-type endopeptidase activity (IBA) propagated phylogenetically from active caspases. CASP12 is catalytically inactive (it directly conflicts with the curated NOT for the same term).",
   "Phylogenetic over-propagation of caspase activity onto an inactive pseudo-caspase; contradicted by the IKR NOT. Remove.", None),
 ("GO:0008234", False): ov("REMOVE",
   "Positive 'cysteine-type peptidase activity' (IEA), the parent of the NOT-ed caspase activity, from the peptidase C14A family signature.",
   "Electronic over-propagation of peptidase activity onto an inactive family member. Remove.", None),
 ("GO:0006508", False): ov("REMOVE",
   "Proteolysis (IEA) inferred from the (absent) peptidase activity.",
   "Process annotation dependent on catalytic activity the protein lacks. Remove.", None),
 ("GO:0050729", False): ov("KEEP_AS_NON_CORE",
   "Positive regulation of inflammatory response (IBA), phylogenetically propagated from active inflammatory caspases. Human CASP12 is reported instead as a negative/dominant-negative modulator of caspase-1/inflammasome signaling, so the direction is uncertain for this inactive member.",
   "Direction of effect is debated for the inactive human protein; keep as non-core pending direct evidence rather than asserting it as a core pro-inflammatory function.", None),
 ("GO:0070269", False): ov("KEEP_AS_NON_CORE",
   "Pyroptotic inflammatory response (IBA), propagated from active caspases. Pyroptosis requires catalytic gasdermin cleavage, which an inactive caspase cannot perform.",
   "Phylogenetic over-propagation onto a catalytically dead member; keep as non-core (no catalytic basis).", None),
}
CAS_CORE_LOC = {"GO:0005737","GO:0005829","GO:0005783"}
CAS_CORE_BP = set()

# ============================ AZIN2 ============================
UAZ="file:human/AZIN2/AZIN2-uniprot.txt"
AZ_CAU="but it was later found that the mouse ortholog does not possess either of them"
az_over = {
 ("GO:0004586", True): ov("ACCEPT",
   "NOT: AZIN2 does not have ornithine decarboxylase activity. It is a catalytically dead paralog of ODC in the Orn/Lys/Arg decarboxylase family.",
   "Correct, important negation. Retain.",
   [{"reference_id":UAZ,"supporting_text":AZ_CAU}]),
 ("GO:0003824", False): ov("REMOVE",
   "Generic 'catalytic activity' (IEA) from the decarboxylase-family signature. AZIN2 has no demonstrated catalytic activity; its function (antizyme inhibition / ODC activation) is regulatory, not catalytic.",
   "Electronic over-propagation onto a catalytically dead paralog. Remove.",
   [{"reference_id":UAZ,"supporting_text":AZ_CAU}]),
 ("GO:0016831", False): ov("REMOVE",
   "Positive 'carboxy-lyase activity' (IEA), the parent of decarboxylase activity, from the family signature.",
   "Electronic over-propagation of decarboxylase activity onto AZIN2, which lacks it (curated NOT|ODC). Remove.", None),
 ("GO:0008792", False): ov("REMOVE",
   "Legacy positive arginine decarboxylase activity (TAS, Reactome). The CAUTION notes AZIN2 was initially reported to have ODC/ADC activity but the ortholog has neither.",
   "Superseded enzymatic claim, contradicted by the CAUTION. Remove.",
   [{"reference_id":UAZ,"supporting_text":AZ_CAU}]),
 ("GO:0042978", False): ov("ACCEPT",
   "Ornithine decarboxylase activator activity: AZIN2's real molecular function - it binds antizymes (OAZ1/2/3) and sequesters them, releasing/stabilizing active ODC.",
   "Core molecular function (a regulatory, non-catalytic activity). Retain.", None),
 ("GO:0042177", False): ov("ACCEPT",
   "Negative regulation of protein catabolic process: by sequestering antizyme, AZIN2 prevents antizyme-mediated proteasomal degradation of ODC.",
   "Core process tied to the antizyme-inhibitor function. Retain.", None),
 ("GO:0043085", False): ov("ACCEPT",
   "Positive regulation of catalytic activity: AZIN2 increases ODC activity by relieving antizyme inhibition.",
   "Core regulatory process consistent with the activator function. Retain.", None),
 ("GO:0008792", True): ov("ACCEPT","NOT arginine decarboxylase.","Correct negation.",None),
 ("GO:0097055", False): ov("REMOVE",
   "Agmatine biosynthetic process (TAS, Reactome) - the product of arginine decarboxylase, an activity AZIN2 lacks.",
   "Process annotation dependent on the defunct arginine-decarboxylase activity (UniProt CAUTION). Remove.",
   [{"reference_id":UAZ,"supporting_text":AZ_CAU}]),
}
AZ_CORE_LOC = {"GO:0005737","GO:0005829","GO:0005634"}
AZ_CORE_BP = {"GO:1902269","GO:0007283"}

build("ILK", UILK,
  ("ILK (integrin-linked kinase; now annotated by UniProt as 'Scaffold protein ILK') is a focal-adhesion "
   "protein of the protein-kinase superfamily that is catalytically dead - a pseudokinase. Rather than "
   "phosphorylating substrates, it functions as the central scaffold of the heterotrimeric IPP "
   "(ILK-PINCH-PARVIN) complex, linking integrin cytoplasmic tails to the actin cytoskeleton and "
   "coordinating cell-matrix adhesion, spreading, and integrin/growth-factor signaling. Its pseudokinase "
   "domain still binds ATP/Mg but performs no catalysis. ILK is essential for focal-adhesion organization, "
   "actin filament assembly, and is implicated in cardiac/muscle function and cancer."),
  ["ILK1","ILK2","P59-ILK","Integrin-linked protein kinase","Scaffold protein ILK"],
  ilk_over, ILK_CORE_LOC, ILK_CORE_BP,
  [{"description":("Catalytically dead pseudokinase that acts as the scaffold of the IPP "
    "(ILK-PINCH-PARVIN) complex at focal adhesions, coupling integrins to the actin cytoskeleton and "
    "coordinating cell-matrix adhesion and spreading."),
    "molecular_function":{"id":"GO:0030674","label":"protein-macromolecule adaptor activity"},
    "directly_involved_in":[{"id":"GO:0007229","label":"integrin-mediated signaling pathway"},
                            {"id":"GO:0007160","label":"cell-matrix adhesion"}],
    "locations":[{"id":"GO:0005925","label":"focal adhesion"}],
    "supported_by":[{"reference_id":UILK,"supporting_text":ILK_CAU}]}],
  [{"question":"Given ILK is a pseudokinase, are any residual phenotypes attributed to 'ILK kinase activity' in older literature explained entirely by its scaffolding of bona fide kinases?"}],
  [{"hypothesis":"ILK's adhesion functions are scaffold-dependent and kinase-activity-independent.",
    "description":"Rescue ILK-null cells with wild-type vs IPP-binding-deficient ILK and assess focal-adhesion assembly and spreading."}])

build("ROR1", UROR,
  ("ROR1 (inactive tyrosine-protein kinase transmembrane receptor ROR1) is a single-pass receptor of the "
   "ROR family with an extracellular cysteine-rich (Frizzled-like) and kringle domain and an intracellular "
   "pseudokinase domain. Its tyrosine-kinase domain is catalytically inactive (very low activity in vitro; "
   "it does not bind ATP), so ROR1 signals non-catalytically as a receptor/coreceptor for Wnt ligands "
   "(notably Wnt5a) in non-canonical Wnt signaling, regulating cell polarity, migration and proliferation. "
   "It is an oncofetal antigen, re-expressed in many cancers (e.g. CLL), making it a prominent immunotherapy target."),
  ["NTRKR1","Inactive tyrosine-protein kinase transmembrane receptor ROR1","Neurotrophic tyrosine kinase receptor-related 1"],
  ror_over, ROR_CORE_LOC, ROR_CORE_BP,
  [{"description":("Catalytically inactive (pseudokinase) receptor tyrosine kinase that functions as a Wnt "
    "(Wnt5a) receptor/coreceptor in non-canonical Wnt signaling, transducing signals non-catalytically."),
    "molecular_function":{"id":"GO:0042813","label":"Wnt receptor activity"},
    "directly_involved_in":[{"id":"GO:0016055","label":"Wnt signaling pathway"}],
    "locations":[{"id":"GO:0005886","label":"plasma membrane"}],
    "supported_by":[{"reference_id":UROR,"supporting_text":ROR_CAU}]}],
  [{"question":"Does ROR1 signaling require heterodimerization with a catalytically active partner (e.g. ROR2, RYK, or MuSK) to compensate for its dead kinase domain?"}],
  [{"hypothesis":"ROR1 transduces Wnt5a signals independently of any kinase activity.",
    "description":"Compare Wnt5a-dependent signaling/migration in cells expressing wild-type ROR1 vs an extracellular-CRD mutant that cannot bind Wnt."}])

build("CASP12", UCAS,
  ("Caspase-12 (CASP12) in humans is an inactive 'pseudo-caspase' of the peptidase C14A family. In the "
   "reference human genome a nonsense polymorphism truncates the protein, and even the rare full-length "
   "variant lacks key catalytic-site residues, so it has no cysteine-type endopeptidase activity. Rather "
   "than cleaving substrates, CASP12 acts as a dominant-negative modulator of inflammatory caspase / "
   "inflammasome signaling (dampening caspase-1-dependent responses), and has reported roles in ER-stress "
   "responses; the full-length allele is associated with altered sepsis susceptibility."),
  ["CASP-12","Inactive caspase-12"],
  cas_over, CAS_CORE_LOC, CAS_CORE_BP,
  [{"description":("Catalytically inactive caspase (pseudo-caspase) that acts as a non-enzymatic, "
    "dominant-negative modulator of inflammatory-caspase / inflammasome (caspase-1) signaling rather than "
    "as a protease; localizes to the ER."),
    "locations":[{"id":"GO:0005783","label":"endoplasmic reticulum"}],
    "supported_by":[{"reference_id":UCAS,"supporting_text":"negative regulator of inflammatory"}]}],
  [{"question":"Through what protein interactions does inactive CASP12 modulate caspase-1/inflammasome activity, and is the direction (positive vs negative regulation) context-dependent?"}],
  [{"hypothesis":"Full-length CASP12 dampens caspase-1 activation by competitive, non-catalytic binding.",
    "description":"Reconstitute inflammasome activation with and without full-length vs truncated CASP12 and measure caspase-1 activity and IL-1B release."}])

build("AZIN2", UAZ,
  ("Antizyme inhibitor 2 (AZIN2, also ADC/ODC-paralogue) is a catalytically dead member of the "
   "Orn/Lys/Arg decarboxylase class-II family. Despite early reports of ornithine or arginine "
   "decarboxylase activity, it has neither. Its function is regulatory: AZIN2 binds ornithine-decarboxylase "
   "antizymes (OAZ1/2/3) and sequesters them, thereby relieving antizyme-mediated inhibition and "
   "degradation of ornithine decarboxylase (ODC), positively regulating polyamine biosynthesis. AZIN2 is "
   "expressed in brain and testis, associates with the ER-Golgi/secretory and vesicular compartments, and "
   "has roles in vesicle trafficking and spermatogenesis."),
  ["ADC","AZIN2","Antizyme inhibitor 2","ODC-paralogue","Arginine decarboxylase"],
  az_over, AZ_CORE_LOC, AZ_CORE_BP,
  [{"description":("Catalytically dead ODC paralog that acts as an antizyme inhibitor: it binds and "
    "sequesters ornithine-decarboxylase antizymes, stabilizing and activating ODC to promote polyamine biosynthesis."),
    "molecular_function":{"id":"GO:0042978","label":"ornithine decarboxylase activator activity"},
    "directly_involved_in":[{"id":"GO:0042177","label":"negative regulation of protein catabolic process"}],
    "locations":[{"id":"GO:0005737","label":"cytoplasm"}],
    "supported_by":[{"reference_id":UAZ,"supporting_text":AZ_CAU}]}],
  [{"question":"Do the AZIN1 and AZIN2 paralogs have distinct antizyme preferences or subcellular sites of ODC activation?"}],
  [{"hypothesis":"AZIN2 activates ODC purely by antizyme sequestration, with no intrinsic decarboxylase activity.",
    "description":"Assay purified AZIN2 for ODC/ADC activity (negative control) and measure ODC stabilization in cells co-expressing AZIN2 and antizyme."}])
