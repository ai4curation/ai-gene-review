# Kdr (rat) review notes

## 2026-10-28 session

- `just fetch-gene rat Kdr` resolved O08775 (VGFR2_RAT, RGD:2965, GeneID 25589); GOA has
  168 rows, almost all ISO/ISS transfers from human KDR (P35968) and mouse Kdr (P35918).
- No deep research API; literature synthesis written by hand in
  `Kdr-deep-research-manual.md`. All rat experimental papers in the cache are
  abstract-only except PMID:20187850, PMID:25942475 and PMID:20097747 (full text).
- PMID:20097747 (requested key paper) only shows that a hyaluronan-butyrate-retinoate
  ester raises kdr mRNA in rat cardiomyocytes and Stro-1 cells
  [PMID:20097747 "significantly enhanced the gene expression of VEGF, kdr (encoding a major
  VEGF receptor), HGF, akt, and pim-1"]. No GOA row cites it; it supports nothing about
  Kdr protein function, so no annotation was derived from it.
- RGD:731072 (WITH for the IPI growth factor binding and IGI blood-pressure rows) is human
  VEGFA (RGD REST lookup), so the IPI row is VEGF binding.

## Decisions

- Core MF: GO:0005021 VEGF receptor activity (is_a transmembrane receptor PTK activity).
  Generic kinase rows (GO:0004672, GO:0004713, GO:0004714) MODIFIED to it.
- GO:0019838 growth factor binding rows MODIFIED to GO:0038085 VEGF binding. GO:0019955
  cytokine binding kept non-core: the mouse donor is gremlin-1 binding, not VEGF.
- GO:0048010 VEGFR signalling rows MODIFIED to GO:0036324 VEGFR-2 signalling pathway;
  GO:0007169 likewise.
- Generic cell proliferation / migration rows (GO:0008284, GO:0030335) kept non-core: rat
  evidence shows Kdr is also mitogenic/motogenic for glioma cells and neural progenitors
  (PMID:17881084, PMID:17360578); endothelial descendants are accepted separately.
- Expression-only rows (PMID:20187850 axon injury, PMID:15885787 human pterygium) marked
  over-annotated; PMID:15885787 is human tissue, recorded as a source defect (CHECK).
- PMID:14612527 endochondral bone growth: inhibitor also blocks FGFR (IC50 9 nM), abstract
  only, left UNDECIDED.
- No NEW terms proposed.
