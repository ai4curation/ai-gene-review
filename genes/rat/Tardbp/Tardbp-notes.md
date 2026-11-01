# Tardbp (rat) review notes

## 2026-10-28 session

- Fetched with `just fetch-gene rat Tardbp`; UniProt A0A8I6GLU8 confirmed (RGD:1310906,
  GeneID 298648); GOA file has 65 rows, all keyed to A0A8I6GLU8.
- No deep-research provider; literature work is in `Tardbp-deep-research-manual.md`.
- Rat experimental rows:
  - RNA binding IDA [PMID:21051541] - RIP-seq in rat cortical neurons; binding in introns and
    3'-UTRs. Refined to pre-mRNA intronic binding + mRNA 3'-UTR binding.
  - Perichromatin fibrils / nuclear speck / interchromatin granule IDA [PMID:19539030] -
    abstract only; perichromatin fibrils is the strong site, speckle labelling is "weak".
  - Positive regulation of insulin secretion IMP [PMID:21127054] - full text is about
    PI3K-C2alpha only, TDP-43 never mentioned. Removed; source defect (wrong gene product) for RGD.
  - Response to ER stress IEP [PMID:21608013] - misfolding by amino-acid analogues raises TDP-43
    levels; ER not examined. Modified to response to misfolded protein; WRONG_TERM defect.
- Mouse UniProt IDA (PMID:28585542) for positive regulation of protein import into nucleus: the
  paper shows CHCHD10 retains TDP-43 in the nucleus, so TDP-43 is the cargo. Rat ISO/IEA rows
  removed; defect recorded for UniProt.
- Mouse MGI IDA (PMID:18836447) for RNA pol II cis-regulatory sequence-specific DNA binding: the
  cached full text does not name TDP-43 (likely in a supplementary SBE2 pull-down list). Kept as
  non-core because human TDP-43 binding of promoter TAR DNA is independently documented.
- Core functions: intronic pre-mRNA binding driving regulation of alternative splicing (incl.
  cryptic exon repression); 3'-UTR binding driving mRNA destabilisation (autoregulation);
  condensate scaffolding by the CTD.
