# RTL5 (SIRH8 / Retrotransposon Gag-like 5) — curation notes

RTL5 is a eutherian *sushi-ichi*/Ty3-gypsy-derived (Gag-like) domesticated gene.
Human review is by orthology to the mouse functional studies; no human
experimental data exist, so functional annotations are ISS.

## Function
- A **pre-made, secreted microglial factor** that is stored in secretory
  granules and released into the extracellular space to capture viral
  nucleic-acid PAMPs (dsRNA)
  [PMID:37834332 "The RTL5 and RTL6 proteins in the secretory granules of microglia are secreted into the extracellular space and there await their targets, such as dsRNA and LPS"].
- Mouse *Rtl5* knockout delays clearance of injected dsRNA from the brain, with
  LPS clearance unaffected, i.e. a dsRNA-specific antiviral role
  [PMID:36162816 "Experiments using Rtl6 or Rtl5 knockout mice provided additional evidence that RTL6 and RTL5 act as factors against LPS and dsRNA, respectively, in the brain"].
- Framed as contributing to removal of viral-derived PAMPs from the brain
  [PMID:42511665 "These findings suggest that SIRH3/RTL6 and SIRH8/RTL5 contribute to the elimination of bacterial- and viral-derived PAMPs from the brain"].

## Curation decisions
- Because RTL5 is the effector that traps the PAMP (not a cell responding to it),
  the review uses GO:0051607 defense response to virus rather than a
  cellular-response term.
- The standalone GO:0045087 innate immune response proposal was dropped as adding
  little over the specific defense-response term.
