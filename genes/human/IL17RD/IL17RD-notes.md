# IL17RD (SEF, hSef, IL17RLM) — curation notes

UniProt Q8NFM7; human; 739 aa type I single-pass transmembrane glycoprotein (signal peptide,
Ig-like/FnIII extracellular region, TM, cytoplasmic SEFIR domain). Isoform 4 (hSef-b) lacks the
signal peptide and is cytosolic.

## Identity / history
- Zebrafish sef identified as an FGF synexpression-group gene and FGF-induced feedback antagonist
  [PMID:11802164 "Sef expression is positively regulated by FGF, and ectopic expression of sef in zebrafish or Xenopus laevis embryos specifically inhibits FGF signalling"]
  [PMID:11802165 "in zebrafish, Sef functions as a feedback-induced antagonist of Ras/Raf/MEK/MAPK-mediated FGF signalling"].
- Named IL17RD because the intracellular domain resembles IL-17 receptors (SEFIR domain), not because of a demonstrated IL-17 ligand
  [PMID:33436016 "it was designated as a member of the IL17 receptor family (IL17RD) based on sequence homology with other IL17 receptors"].

## FGFR inhibition (core)
- Human hSEF: co-IP with FGFR1, homomeric complexes, inhibits FGF-induced reporter; acts on ERK without MEK inhibition; requires intracellular domain
  [PMID:12807873 "this receptor is capable of forming homomeric complexes and can interact with fibroblast growth factor (FGF) receptor 1"]
  [PMID:12807873 "This appears to occur as a result of specific inhibition of p42/p44 ERK in the absence of upstream MEK inhibition"].
- Human hSef binds FGFR1 and FGFR2 (not FGFR3), acts upstream of Ras in PC-12 cells
  [PMID:12958313 "hSef interacts with FGFR1 and FGFR2 but not FGFR3"]
  [PMID:12958313 "possibly functioning upstream of the Ras molecule"].
- Mouse Sef: cytoplasmic domain mediates FGFR1 association; reduces FGFR1 and FRS2 Tyr phosphorylation; blocks ERK activation by constitutively active FGFR1 but not active Ras
  [PMID:12604616 "Sef exerts its inhibitory effects at the level of FGFR and upstream of Ras"].
  Extracellular+TM domains also contribute and associate with FGFR1 [PMID:16603339 "SefECTM associated with FGFR1"].
- Human disease variants (Kallmann syndrome, HH18) assayed for loss of inhibition of FGF8b/FGFR1c AP-1 reporter
  [PMID:23643382 "cells coexpressing WT IL17RD exhibited markedly lower activity (70% inhibition)"].
- Review: interaction with FGFR is ligand-independent; site of action debated
  [PMID:33436016 "The interaction of SEF with FGFR is independent of factors such as ligand stimulation, FGFR dimerization and kinase activity"]
  [PMID:23643382 "The mechanisms by which IL17RD inhibits FGF signaling are contentious"].

**Direct binding?** All FGFR-binding evidence is co-immunoprecipitation/co-localisation in
overexpression systems (zebrafish, mouse, human). No purified-protein, SPR or structural data
show a direct IL17RD–FGFR contact. Best described as "associates with FGFR1/FGFR2 (co-IP),
directness not established".

## Spatial MEK–ERK regulation (second mechanism)
- Human hSef binds activated MEK, retains the MEK–ERK complex, blocks ERK nuclear translocation, spares cytoplasmic RSK2
  [PMID:15239952 "hSef binds to activated forms of MEK, inhibits the dissociation of the MEK-ERK complex, and blocks nuclear translocation of activated ERK"].
  siRNA of endogenous hSef enhances ERK nuclear entry and Elk-1 activity.
  Reactome places this at the Golgi membrane (R-HSA-5674366, R-HSA-5674373).
- No GO term for "ERK nuclear import"; protein sequestering activity (GO:0140311) is a reasonable MF fit.

## IL-17 signalling (non-core, modulatory)
- Human IL17RD co-IPs/colocalises with IL17RA, a 24p3 reporter assay shows IL17RD mediates signalling; IL17RD associates with TRAF6
  [PMID:19079364 "IL-17RD is a part of the IL-17 receptor signaling complex"].
- Mouse KO: loss of IL-17A-induced neutrophilia, reduced p38/MIP-2, increased NF-kB/IL-6/KC; disrupts Act1–TRAF6
  [PMID:23047677 "Interleukin-17 receptor D disrupts the interaction of Act1 and TRAF6"].
- No direct IL-17 ligand binding by IL17RD has been shown; it is still referred to as an
  "orphan receptor" in 2012/2015 titles. So GO:0030368 interleukin-17 receptor activity (ligand
  binding + transduction) is an over-annotation; participation in IL-17-mediated signalling as a
  receptor-complex modulator is supported.

## TLR signalling (non-core)
- [PMID:25808990 "the intracellular Sef/IL-17R (SEFIR) domain of IL-17RD targets TIR adaptor proteins to inhibit TLR downstream signalling"]

## Other
- TAK1 interaction and JNK activation/apoptosis (overexpression) [PMID:15277532].
- hSef potentiates EGF signalling via EGFR trafficking [PMID:18096367] — context dependent.
- Lens EMT: Sef overexpression in rat lens explants blocks TGFb-induced EMT [PMID:25576668 "we have established a novel role for Spry, Spred and Sef as negative regulators of TGFβ-induced EMT"].
  Abstract-only; the readout is EMT morphology/alpha-SMA. Source of the mouse IDA and the human ISS/IEA rows.
- Localisation: hSef-a at cell surface, hSef-b cytosolic [PMID:14742870 "hSef-b product was cytosolic, whereas the hSef-a product was located at the cell surface"];
  Golgi and endosomes reported in overexpression systems [PMID:33436016].

## Annotation decisions (summary)
- Golgi membrane/Golgi apparatus/plasma membrane: ACCEPT.
- cytoplasm (IEA from isoform 4 note): KEEP_AS_NON_CORE.
- protein binding (RRN3, HT screens): REMOVE (uninformative).
- IL-17 receptor activity (IBA, IEA): MARK_AS_OVER_ANNOTATED.
- IL-17-mediated signalling (IBA): KEEP_AS_NON_CORE.
- neg reg EMT (ISS/IEA from mouse): KEEP_AS_NON_CORE.
- neg reg TGFb receptor signalling (ISS/IEA): UNDECIDED (abstract-only source; readout appears to be EMT not pathway).
- NEW: negative regulation of FGFR signalling pathway (GO:0040037); negative regulation of TLR signalling (GO:0034122).
- No NOT annotations in GOA for this gene.
