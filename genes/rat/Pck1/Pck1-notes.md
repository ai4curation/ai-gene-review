# Pck1 (rat) review notes

## Session 1 (2026-10-28)

- `just fetch-gene rat Pck1` resolved P07379 (PCKGC_RAT, RGD:3267, GeneID 362282). 124 GOA rows.
- No deep-research provider available; literature synthesis is in `Pck1-deep-research-manual.md`.
- Almost all cached PMIDs are abstract-only. Full text was available for PMID:19635791
  (PEPCK-M in beta cells; shows PEPCK-C absent from islets) and PMID:21486814.
- Compared with existing reviews `genes/human/PCK1` and `genes/mouse/Pck1`.

### Decisions

- GO:0004613 PEPCK (GTP) activity: ACCEPT throughout. GO:0004611 (parent) rows MODIFY to GO:0004613.
- Cytosol ACCEPT; cytoplasm (IDA, PMID:4186849) MODIFY to cytosol.
- Mitochondrion IBA: REMOVE. Donors are PCK2 (MGI:1860456, Q16822); rat liver PEPCK-C is
  >90% cytosolic [PMID:6049928] and islets lacking PEPCK-C have only mitochondrial PEPCK
  [PMID:19635791]. Source defect recorded against GO_Central.
- ER rows, protein serine kinase (GTP), peptidyl-serine phosphorylation, positive regulation
  of lipid biosynthetic process: KEEP_AS_NON_CORE. All derive from one human HCC study
  (PMID:32322062); Ser90 exists in rat (UniProt mutagenesis, PMID:30193097). Regulation of
  lipid biosynthetic process (parent) MODIFY to the positive child.
- GO:0072350 tricarboxylic acid metabolic process: MODIFY to GO:0006107 (oxaloacetate is a
  dicarboxylic acid; GO:0006107 is not a descendant of GO:0072350, so this is a lateral fix).
  Source defect on the human UniProt IDA.
- GO:0006114 glycerol biosynthetic process: MODIFY to GO:0046167 glycerol-3-phosphate
  biosynthetic process; glyceroneogenesis produces glycerol 3-phosphate, not free glycerol.
- GO:0004550 NDP kinase (Reactome EXP, carbovir): MARK_AS_OVER_ANNOTATED; source defect
  SUSPECTED (likely PEPCK's reverse reaction phosphorylating a GDP analogue, not NDP kinase).
- Expression (IEP) rows: hormone/fasting responses (insulin, glucagon, cAMP, glucose,
  dexamethasone, starvation) KEEP_AS_NON_CORE; incidental exposures (osmotic, raffinose,
  PMA, cytokines, LPS, hypoxia, retinoic acid, fructose, methionine, diet, exercise,
  bacterium) MARK_AS_OVER_ANNOTATED.
- Memory T cell differentiation: MARK_AS_OVER_ANNOTATED (metabolic supplier, not a
  regulator; no rat data). Hepatocyte differentiation IBA: MARK_AS_OVER_ANNOTATED.
- Positive regulation of transcription by RNA pol II (ISO from mouse IDA PMID:19458124):
  MARK_AS_OVER_ANNOTATED; the mouse study measures PEPCK mRNA as a readout.
