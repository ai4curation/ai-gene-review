# IL1A notes

## Literature search (manual; no deep-research provider available)

Sources checked (2026-11-04):
- UniProt P01583 record (`IL1A-uniprot.txt`), curated FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and PTM comments.
- All GOA-cited publications cached via `just fetch-gene-pmids human IL1A` (abstracts for most;
  full text for PMID:26439902 and PMID:23847621).
- Added PMID:33391283 (Chan & Schroder-style review of alternative IL-1 activation, full text
  cached) for cell-surface IL-1alpha.
- Context only, not evidence: GO-CAM gomodel:59cc772c00000000 (IL1B-centred; IL1A not modelled). (IL-1
  signalling module/GO-CAM review proposed in ai4curation/ai-gene-review#5904.)

## Key findings

- IL-1alpha is one of two IL-1 agonists. Unlike pro-IL-1beta, the IL-1alpha precursor binds IL1R1
  without processing [PMID:2950091 "the initial translation product of IL-1 alpha mRNA can bind to the
  IL-1 receptor without further proteolytic processing"].
- Same receptor and outputs as IL-1beta [PMID:33482337 "The cytokine binds the IL-1 receptor 1
  (IL-1R1), as does IL-1β, and induces the same pro-inflammatory effects."].
- Alarmin: constitutive intracellular precursor released on necrosis [PMID:33482337 "The IL-1α
  precursor is constitutively present in nearly all cell types in health, but is released upon
  necrotic cell death as a bioactive mediator."].
- Leaderless; unconventional secretion routes: S100A13/Cu2+-dependent stress export
  [PMID:12746488], caspase-1-dependent secretion [PMID:18329368], TMED10 channel into ERGIC
  [PMID:32272059].
- Nuclear pool via NLS in the N-terminal propiece, binds HAX1 [PMID:11554782, PMID:16971486];
  DNA damage sensing and secretion without loss of integrity [PMID:26439902 "Together, this data
  shows that IL-1α can localize to DNA damage sites and can be secreted without the loss of
  cellular integrity."].
- Decoy receptor IL1R2 captures IL-1alpha, including pro-IL-1alpha in the cytosol [PMID:23847621].
- Processing by calpain increases activity ~50-fold affinity [PMID:33391283].

## Curation observations

- The NAS rows from PMID:23847621 (assigned by ComplexPortal, ECO:0005547 inferred from complex
  membership) on negative regulation of IL-1 signalling, IL-1alpha production, inflammation and
  monocyte differentiation describe the IL1R2 decoy complex. IL-1alpha is the captured ligand in
  that complex and performs none of the inhibition; those rows were removed.
- GO:0045323 interleukin-1 receptor complex is defined as the receptor (alpha and beta subunits)
  that binds IL-1; the ligand is not a subunit.
- No IL1A-specific evidence for apoptotic process participation (IL-1 is processed/released during
  apoptosis, PMID:1924307, it does not execute it).
