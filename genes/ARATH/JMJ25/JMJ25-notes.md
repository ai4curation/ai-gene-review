# JMJ25 (IBM1) review notes

- 2026-10-28: fetched with `just fetch-gene ARATH JMJ25`; accession Q9SSE9 confirmed (TAIR AT3G07610,
  GeneID 819952). 25 GOA rows. See JMJ25-deep-research-manual.md for literature synthesis.
- Full text read: PMID:22772985 (Fan 2012), PMID:27697902, PMID:19262562, PMID:24404182,
  PMID:33986281, PMID:41036628. Abstract-only: PMID:18218897, PMID:20834229, PMID:22580822,
  PMID:28400174, PMID:18713399.
- Core: H3K9me2/me1 demethylase (GO:0140683), nuclear/chromatin, epigenetic regulation of gene
  expression by keeping transcribed genes free of H3K9me2/CHG methylation
  [PMID:20834229 "Loss-of-function ibm1 mutation results in ectopic H3K9me and non-CG methylation in thousands of genes."].
- PMID:22772985 does not perform an in vitro demethylase assay; it shows H3K9me2 increases at
  RDR2/DCL3 in ibm1 and YFP-IBM1 occupancy by ChIP, and cites earlier work for catalysis
  [PMID:22772985 "IBM1 was also shown to catalyze H3K9me2 and H3K9me1 demethylation in Arabidopsis (26)"].
  The "chromatin DNA binding" IDA rests on ChIP association, not on direct DNA binding.
- ARBA "heterochromatin formation" has the sign wrong: IBM1 removes heterochromatic marks from genes.
- UniProt FUNCTION says IBM1 "Contributes to the silencing of transposable elements (TEs)
  (PubMed:41036628)"; the cited paper attributes TE silencing to GyrB3/HDA6, and describes IBM1 as
  preventing heterochromatic marks on genes. Recorded as a SUSPECTED source defect on the
  heterochromatin-formation row.
