# NAI1 review notes

## 2026-10-28 session

- Fetched Q8S3F1 (matches requested accession; TAIR AT2G22770, GeneID 816807). 10 GOA rows.
- Deep research API unavailable; wrote NAI1-deep-research-manual.md from cached literature.
- PMID:23155454 (ERMO3/MVP1/GOLD36 paper, full text) is the source of the two TAIR IMP rows.
  The paper's NAI1 data: ermo3-1 nai1-1 double mutant lacks ER aggregates
  [PMID:23155454 "Depletion of NAI1 in ermo3-1 suppressed the formation of ER-aggregates"],
  and NAI2/PYK10 expression is positively regulated by NAI1
  [PMID:23155454 "the expression of both of these proteins is positively regulated by NAI1 (Figure S4B)"].
- DNA binding and promoter activation: PMID:33315514 (abstract only)
  ["NAI1 binds to the promoter region of NAI2 and activates the NAI2 promoter"; "Subcellular localization of NAI1 was evident in the nucleus"].

## Decisions

- GO:0003700 (ISS x2) -> MODIFY to GO:0001216 DNA-binding transcription activator activity (PMID:33315514).
- GO:0006355 (IBA, IMP, TAS) -> MODIFY to GO:0045893 positive regulation of DNA-templated transcription.
- GO:0000976 IBA -> ACCEPT (G-box binding, PMID:33315514).
- Nucleus (IEA, ISM) -> ACCEPT (GFP-NAI1 nuclear in PMID:33315514).
- GO:0046983 IEA -> KEEP_AS_NON_CORE (bHLH dimerization inferred, not shown).
- GO:0007029 ER organization IMP (acts_upstream_of_or_within) -> KEEP_AS_NON_CORE: true as upstream
  genetic requirement; NAI1 does not do ER-remodelling work itself.
- No NEW process terms. GO:0080119 ER body organization is not a descendant of GO:0007029
  (OLS ancestors: organelle organization only), and NAI1 is a transcriptional regulator of the
  ER-body gene battery rather than a participant; there is no "regulation of ER body organization"
  term. Logged as a proposed new term / question.
- No upstream source defects identified.
