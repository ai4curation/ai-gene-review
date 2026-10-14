# FGFR3 (human, P22607) curation notes

## 2026-09-30 initial review (claude-code)

### Identity and core biology
- FGFR3 is a single-pass type I receptor tyrosine kinase of the FGFR family
  (EC 2.7.10.1): three Ig-like ectodomains (D1-D3), TM helix, split tyrosine
  kinase domain [file:human/FGFR3/FGFR3-uniprot.txt "Tyrosine-protein kinase that acts as a cell-surface receptor"].
- Ligand (FGF) + heparan sulfate binding drives dimerization and trans-autophosphorylation
  [file:human/FGFR3/FGFR3-uniprot.txt "Ligand binding leads to dimerization and activation by"];
  [PMID:11294897 "Activation of FGFR3, through mutation or ligand stimulation, results in autophosphorylation of multiple tyrosine residues within the intracellular domain."].
- Structural: FGF1-FGFR3c crystal structure; D1/D1-D2 linker autoinhibit FGF and heparin binding
  [PMID:14732692 "the three-Ig form of FGFR3c exhibits lower affinity for both FGF1 and heparin"].
  TM-domain dimer [PMID:24120763 "the two transmembrane helices pack into a symmetric left-handed dimer"];
  kinase trans-phosphorylation captured in crystal [PMID:23972473 "the mutant FGFR3 kinases are caught in the act of trans-phosphorylation on a kinase insert autophosphorylation site"].
- Ligand specificity: engineered BaF3 mitogenic assays of all FGFR splice variants
  [PMID:8663044 "These studies demonstrate that FGF 1 is the only FGF that can activate all FGF receptor splice variants."].
- Downstream: FRS2/GRB2/SOS -> RAS-ERK; PLCG1; PI3K; STAT1/3 (STAT activation by activated receptor)
  [PMID:10918587 "Phosphorylation of Shp2, PLC-gamma, and MAPK was also stimulated"];
  [PMID:11294897 "Addition of a single tyrosine residue, Y724, restored its ability to stimulate cellular transformation, phosphatidylinositol 3-kinase activation, and phosphorylation of Shp2, MAPK, Stat1, and Stat3."].

### Paralog-specific physiology: growth restraint in the growth plate
- Fgfr3 knockout mice show skeletal overgrowth with expanded proliferating and hypertrophic
  chondrocyte zones [PMID:8601314 "FGFR-3 appears to regulate endochondral ossification by an essentially negative mechanism, limiting rather than promoting osteogenesis."].
- Gain-of-function human alleles (ACH, HCH, TD1/2, SADDAN) -> dwarfism; partial LOF (CATSHL) -> tall stature
  [PMID:20582225 "Recently partial loss-of-function mutation of FGFR3 was found to cause camptodactyly, tall stature, scoliosis, and hearing loss (CATSHL) syndrome"].
- STAT1 arm inhibits chondrocyte proliferation; ERK arm inhibits differentiation
  [PMID:15748888 "STAT1 phosphorylation seems to be involved in inhibition of chondrocyte proliferation while activation of the ERK pathway inhibits chondrocyte differentiation and B-cell proliferation"].
- Chondrocyte apoptosis via PLCgamma-STAT1 [PMID:17561467 "we conclude that a PLCgamma-STAT1 pathway mediates apoptotic signaling by FGFR3."].
- The context-dependence matters for GO: in BaF3/NIH3T3/myeloma the receptor is mitogenic
  (positive regulation of proliferation), whereas in growth-plate chondrocytes it is anti-proliferative.
  Proliferation-positive rows are therefore kept, but as non-core.

### Localization
- PM is the site of function. ER/Golgi reflect biosynthetic maturation (N-glycan becomes Endo H
  resistant in Golgi) and ER retention of severe mutants [PMID:17561467]; vesicles reflect
  post-activation internalization [file:human/FGFR3/FGFR3-uniprot.txt "intracellular vesicles after internalization of the autophosphorylated"].
- Isoform 3 (FGFR3deltaTM) is secreted [file:human/FGFR3/FGFR3-uniprot.txt "[Isoform 3]: Secreted."].
- PMID:18061161 (FGFRL1 paper) is abstract-only in cache; the FGFR3 IDA rows (PM, Golgi, transport
  vesicle) presumably come from FGFR3 used as comparator in the full text. Not verifiable; plausible,
  so deferred to curator (not removed).

### Decisions
- 313 `protein binding` IPI rows: 300 from one Y2H neurodegeneration interactome (PMID:32814053),
  plus HSP90AB1/CDC37 chaperone-client captures, BioPlex, RTK BioID, IgSF ELISA. All REMOVE as
  uninformative, except FGF1 (PMID:14732692), MODIFY -> GO:0017134 fibroblast growth factor binding.
- JAK-STAT (GO:0007259) MODIFY -> GO:0097696 receptor signaling pathway via STAT: STAT activation by
  FGFR3 is receptor-driven (and PLCgamma-dependent in chondrocytes), JAK involvement not shown in cited paper.
- MAPK cascade TAS -> MODIFY to positive regulation of MAPK cascade (receptor is upstream, not a cascade component).
- chondrocyte proliferation TAS -> MODIFY to negative regulation of chondrocyte proliferation (GO:1902731).
- chondrocyte differentiation TAS -> MODIFY to negative regulation of chondrocyte differentiation (GO:0032331).
- focal adhesion (colocalizes_with, TAS from review PMID:15748888, abstract-only; abstract silent) -> UNDECIDED.
- NEW: heparin binding (GO:0008201), measured by SPR in PMID:14732692.
- No NEW process terms proposed; the growth-restraint role is already captured by existing
  rows after MODIFY (GO:1902731, GO:0032331) and GO:0048640 (ISS).

### Module relevance (modules/fgfr_signaling.yaml)
- Module FGFR3 variant asserts GO:0005007 at plasma membrane: consistent with this review.
- Paralog-distinguishing biology to note: FGFR3 is the growth-plate brake (negative regulation of
  chondrocyte proliferation/differentiation, negative regulation of developmental growth) and
  signals to STAT1 (PLCgamma-dependent) to induce chondrocyte growth arrest/apoptosis;
  also required for inner-ear development (CATSHL hearing loss).
