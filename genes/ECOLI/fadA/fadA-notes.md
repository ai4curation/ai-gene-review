# Curation notes: *Escherichia coli* K-12 fadA (P21151, b3845)

Reviewed as the E. coli exemplar of the FadA thiolase step in
`modules/bacterial_fatty_acid_beta_oxidation.yaml`.

## Sources

- No provider deep-research report was generated for this gene in this session;
  the review rests on the reviewed UniProt entry and the cached GOA-cited
  publications. No `-deep-research-*.md` file exists for it.
- Cached publications are abstract-only (PMID:368024, PMID:8454629,
  PMID:3286611, PMID:334745, PMID:12535077) or title-only (PMID:4861587,
  PMID:4919548, PMID:4928881). For the title-only papers the experimental
  rows are accepted by deferring to the EcoCyc curator, because the claimed
  function is independently established for FadA.

## Decisions

- GO:0003988 acetyl-CoA C-acyltransferase activity is the core function
  (UniProt reaction with physiological direction right-to-left, Km values from
  PMID:8454629).
- GO:0010124 phenylacetate catabolic process (IBA, PTN001823071) is removed:
  the only seed for that term is E. coli PaaJ (P0C7L2), the paa-pathway
  thiolase, and FadA is in the FadA-specific subfamily PTHR43853:SF11. Recorded
  as a GO_CENTRAL source defect. The local PAINT snapshot
  (`interpro/panther/PTHR43853/PTHR43853-paint.tsv`) does not list this IBD,
  so the node assertion is visible only in the GOA row.
- GO:0005515 protein binding (IPI with FadB) is removed under the
  protein-binding policy; complex membership is kept through GO:0036125.
- Broad parents (acyltransferase, fatty acid metabolic process, fatty acid
  catabolic process, lipid catabolic process) are TOO_GENERAL beside the
  accepted GO:0003988 and GO:0006635.
