# LEP (leptin) curation notes

Deep research: `LEP-deep-research-falcon.md` (Falcon, second attempt; the first timed out) completed after
the review was drafted and is consistent with it; the review was written from cached publications and UniProt, with
literature located through PubMed.

## Core biology

- Leptin is a secreted four-helix-bundle cytokine-like hormone made mainly by adipocytes
  [PMID:7984236 "The ob gene product may function as part of a signalling pathway from adipose tissue that acts to regulate the size of the body fat depot."].
- It circulates in plasma and acts as an endocrine signal of fat stores; recombinant protein
  reduces food intake and raises energy expenditure in ob/ob mice
  [PMID:7624777 "The protein reduced food intake and increased energy expenditure in ob/ob mice."].
- Receptor: LEPR (OB-R), a class I cytokine receptor
  [PMID:8548812 "OB-R is a single membrane-spanning receptor most related to the gp130 signal-transducing component of the IL-6 receptor"].
  Leptin assembles 3:3 LEPR complexes
  [PMID:36959263 "Leptin induces type I cytokine receptor assemblies featuring 3:3 stoichiometry"].
- Human genetics: homozygous LEP frameshift causes severe early-onset obesity
  [PMID:9202122 "The severe obesity found in these congenitally leptin-deficient subjects provides the first genetic evidence that leptin is an important regulator of energy balance in humans."].
- Leptin replacement corrects appetite, puberty (via gonadotropins), thyroid axis and T cell defects
  [PMID:12393845 "Leptin deficiency was associated with reduced numbers of circulating CD4(+) T cells and impaired T cell proliferation and cytokine release"].

## Curation approach

- Core: hormone activity / leptin receptor binding (MF); leptin-mediated signaling pathway,
  negative regulation of appetite by leptin-mediated signaling pathway, energy homeostasis (BP);
  extracellular region (CC).
- Reproductive, immune, angiogenic, bone and other peripheral effects are kept as non-core:
  they are real consequences of LEPR activation in target cells.
- Ortholog-transferred "response to X" terms mostly describe regulation of LEP expression
  (leptin levels respond to nutrition, insulin, hormones), not leptin function; marked over-annotated.
- Cytosol and DNA binding contradict a signal-peptide secreted hormone; removed.
- "cellular response to leptin stimulus" (IDA, MCF7) describes the responding cells, not the
  ligand; modified to leptin-mediated signaling pathway.
- Two IDA annotations from PMID:17957153 (placenta development; positive regulation of
  developmental growth) cannot be reconciled with the cached abstract (cord leptin unrelated to
  neonatal feeding); left UNDECIDED rather than removed, since the full text is not cached.
- GO:0005615 extracellular space is obsolete in the current GO release; core location uses
  GO:0005576 extracellular region.
