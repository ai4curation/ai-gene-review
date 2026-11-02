# DCL3 review notes

2026-10-28. Fetched with `just fetch-gene ARATH DCL3`; UniProt Q9LXW7 (Swiss-Prot,
GeneID 823508, TAIR AT3G43920) confirmed. 26 GOA rows. No deep-research provider was
available; manual synthesis is in `DCL3-deep-research-manual.md`.

## Key decisions

- Core MF: ribonuclease III activity (GO:0004525), producing 24-nt heterochromatic siRNAs
  from Pol IV-RDR2 dsRNA [PMID:24214956; PMID:34648373; PMID:31398324]. Added a NEW IDA
  row from the structure/biochemistry paper PMID:34648373, since GOA only has IBA/IEA
  for the catalytic activity.
- Core BP: siRNA processing (GO:0030422) and gene silencing by siRNA-directed DNA methylation
  (GO:0080188). The TAIR IMP row for GO:0044027 (CpG island methylation) is modified to
  GO:0080188: DCL3 loss affects asymmetric non-CG methylation at repeats/transposons
  [PMID:15024409 "In the dcl3-1 mutant, however, cytosine methylation was decreased only at
  asymmetric sites"], not promoter CpG islands. Recorded as a WRONG_TERM source defect
  (PROBABLE).
- DCL3 does the work in RdDM (it catalyses the siRNA biogenesis phase that GO:0080188's
  definition includes), so the process term passes the NEW/participation bar.
- Cytoplasm IBA: DCL3-GFP is exclusively nuclear [PMID:15024409]; marked over-annotated
  (inherited from cytoplasmic paralogs DCL1/DCL2/DCL4 seeds).
- ta-siRNA processing: DCL3 only contributes in the absence of DCL4 [PMID:16040244];
  kept as non-core.
- Antiviral rows: non-core; RNA-virus evidence mostly from triple dcl2 dcl3 dcl4 mutants.
- ATP binding: P-loop motif present; ATP-dependence of dicing is disputed between
  PMID:24214956 (ATP needed, not hydrolysis) and PMID:34648373 (ATP-independent).
  Kept as non-core.
- Protein binding (GO:0005515) rows removed per policy.
- Residue numbering in PMID:34648373 is offset (~10) from the current canonical sequence;
  no residue claims recorded.
- PMID:22772985 (IBM1) read in full: concerns epigenetic control of DCL3 transcription,
  used in the description as context only.
