# GPER1 (G protein-coupled estrogen receptor 1; GPR30; CMKRL2) review notes

**Deep research status:** falcon (Edison) deep research failed with an authentication
error on 2026-10-24, and no other deep-research provider key was usable. No
`-deep-research-*.md` file exists for this gene. The notes below come from the cached
publications in `publications/`, the UniProt record (`GPER1-uniprot.txt`), cached
Reactome entries, GO term definitions (oaklib, `sqlite:obo:go`) and a web search.

## Why this gene was reviewed

Flagged by rule FRR:0009 (projects/FUNCTION_REQUIREMENT_RULES.md): GPER1 carries
`GO:0030284 nuclear estrogen receptor activity` (IDA x2, IBA, IEA), a descendant of
`GO:0003700 DNA-binding transcription factor activity`, while having no DNA-binding domain.

GO definition check (oaklib, go.db):
- GO:0030284 nuclear estrogen receptor activity: "A nuclear receptor activity regulated
  by estrogen binding and modulating the transcription of specific gene sets transcribed
  by RNA polymerase II." Parent GO:0003707 nuclear steroid receptor activity; GO:0003700
  is an ancestor (confirmed).
- GO:0038054 G protein-coupled estrogen receptor activity: "Combining with estrogen and
  transmitting the signal across the membrane by activating an associated G-protein..."
  is_a GO:0004930 G protein-coupled receptor activity. This is the term that matches GPER1.
- GO:0030520 estrogen receptor signaling pathway and GO:0030518 are both defined as
  nuclear-receptor-mediated pathways; GO:0043401 steroid hormone receptor signaling
  pathway is the receptor-type-neutral parent.
- GO:1903924 estradiol binding exists (is_a steroid binding).

## Domain architecture / family

- UniProt: "Belongs to the G protein-coupled receptor 1 family" (PROSITE-ProRule PRU00521);
  Pfam PF00001 7tm_1; InterPro IPR000276/IPR017452 (rhodopsin-like GPCR), IPR047143
  GPER1-like; PANTHER PTHR24226:SF2 (G-protein coupled estrogen receptor 1), family
  PTHR24226 (GPR182 and GPER1). No nuclear-receptor zinc finger or ligand-binding domain.
- 375 aa; 7 TM helices; C-terminal PDZ-binding motif (-SSAV) [PMID:38211639 "Deleting the GPR30 C-terminal PDZ motif (-SSAV) does not interfere with the receptor complex"].

## Receptor activity and ligand binding

- [PMID:15539556 "GPR30, an orphan receptor unrelated to nuclear estrogen receptors, has all the binding and signaling characteristics of a mER"]
- [PMID:15539556 "E2 treatment of transfected cell membranes caused activation of a stimulatory G protein that is directly coupled to the receptor, indicating GPR30 is a G protein-coupled receptor (GPCR), and also increased adenylyl cyclase activity"]
- Kd ~2.7 nM in SKBR3 membranes [PMID:15539556 "A high-affinity (dissociation constant 2.7 nm), limited capacity, displaceable, single binding site specific for estrogens was detected in plasma membranes of SKBR3 breast cancer cells"].
- [PMID:15705806 "GPR30 is uniquely localized to the endoplasmic reticulum, where it specifically binds estrogen and fluorescent estrogen derivatives"]; [PMID:15705806 "Activating GPR30 by estrogen resulted in intracellular calcium mobilization and synthesis of phosphatidylinositol 3,4,5-trisphosphate in the nucleus"].
  NB: the abstract describes PIP3 (a lipid), whereas GOA annotates
  GO:0032962 positive regulation of *inositol trisphosphate* biosynthetic process from this paper (likely term error; recorded as a source defect, CHECK).
- Conserved in fish: [PMID:19931550 "croaker and human GPER have very similar estrogen binding characteristics, typical of estrogen membrane receptors, and activate the same estrogen signaling pathways via stimulatory G proteins (Gs) resulting in increased cAMP production"].
- Contrary evidence: [PMID:18566127 "using radioactive estradiol, we observed only saturable, specific binding to the classical ER but not to GPR30"]; [PMID:18566127 "we draw the conclusion that GPR30 is still an orphan receptor"]. UniProt CAUTION notes conflicting data. Web search (PMC7137379, "Does GPER really function as a G protein-coupled estrogen receptor in vivo?", Front Endocrinol 2020) summarises ongoing debate; IUPHAR named the receptor GPER in 2007. Not cached; used as context only.
- Reactome models GPER as a Gs- and Gi-coupled GPCR for estradiol [Reactome:R-HSA-9036301 "Binding of E2 to GPER induces the exchange of GDP for GTP on the G alpha (s) heterotrimer G protein, activating it"].
- UniProt also states aldosterone receptor function (by similarity) - contested.

## Signalling outputs (downstream; mostly non-core)

- UniProt FUNCTION: cAMP, calcium mobilization, Src -> HB-EGF release -> EGFR transactivation -> PI3K/Akt and ERK.
- CAFs: [PMID:20551055 "E2 stimulates a physical interaction between GPR30 and phosphorylated EGFR, recruiting them to the cyclin D1 gene promoter"] - the basis of chromatin binding / transcription annotations. A 7TM receptor acting on chromatin is unusual and not independently established; treated as over-annotation.
- Myometrium: [PMID:21427217 "estrogen membrane receptor activation increased the myometrial contractile response to oxytocin"].
- Endothelium: [PMID:23285008 "Treatment with the selective GPR30 agonist G-1 partially attenuated the TNF induced upregulation of pro-inflammatory proteins"]; leukocytes themselves were not assayed.
- Coronary artery SMCs: [PMID:23840305 "GPER activation inhibits CASMC proliferation by suppressing cell cycle progression via inhibition of ERK1/2 and Akt phosphorylation"] - note opposite sign to ERK activation in other cells; context dependent.

## Localization

- Plasma membrane: cAMP and beta-arrestin2 recruitment at PM [PMID:21149639 "We conclude that GPER1-mediated stimulation of cAMP production and β-arrestin2 recruitment occur in the PM"].
- Constitutive endocytosis, recycling endosomes, TGN, proteasomal degradation [PMID:21540189 "GPER constitutively buds intracellularly into EEA-1+ endosomes from clathrin-coated pits"]; [PMID:21540189 "endocytosed GPER does not recycle to the cell surface, but instead returns to the trans-Golgi network (TGN) and does not re-enter the ER"]. This explains low steady-state surface levels and resolves the PM-vs-ER controversy; hence the NOT|plasma membrane row from PMID:15705806 is contradicted.
- ER: [PMID:18566127 "we confirmed that the receptor localized to the endoplasmic reticulum"].
- Keratin filaments [PMID:21149639 "One such intracellular structure was identified as cytokeratin (CK) intermediate filaments, including those composed of CK7 and CK8"].
- Nucleus in HUVEC [PMID:23285008 "We found that GPR30 was located predominantly in the endothelial cell nuclei"] and in CAFs (PMID:20551055).

## Interactions

- RAMP3 [PMID:23674134 "we show that GPR30 and RAMP3 interact"]; RAMP1/2/3 screen (PMID:39083597).
- NHERF1 via PDZ [PMID:27448983 "This interaction was mediated by the PDZ2 domain of NHERF1 and the carboxyl terminal PDZ binding motif of GPER"].
- beta1AR/MAGUK/AKAP5 complex (PMID:38211639).
- KRT7/KRT8 (PMID:21149639); EGFR (PMID:20551055).

## Decisions summary

- GO:0030284 (all four rows): MODIFY -> GO:0038054 G protein-coupled estrogen receptor activity; source_defects WRONG_TERM against UniProt (IDA), GO_Central/PAINT PTN002795969 (IBA) and MGI (source of the Ensembl Compara IEA).
- GO:0004930 rows: MODIFY -> GO:0038054 (more specific, supported).
- steroid binding / steroid hormone binding: MODIFY -> GO:1903924 estradiol binding.
- GO:0030518 / GO:0030520 (nuclear-receptor pathways): MODIFY -> GO:0043401.
- GO:0045745 positive regulation of GPCR signaling: MODIFY -> GO:0007189 / GO:0007186 (GPER is the receptor itself).
- Downstream signalling/physiology terms: mostly KEEP_AS_NON_CORE; terms implying GPER responds to TNF, oxytocin or glucose, or executes apoptotic nuclear changes or action potentials: MARK_AS_OVER_ANNOTATED.
- Generic protein binding: REMOVE, except NHERF1 -> MODIFY to PDZ domain binding.
