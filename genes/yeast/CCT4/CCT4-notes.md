# CCT4 review notes

## 2026-10-01 current GOA re-review

- Re-fetched CCT4 against current GOA, which now has 15 rows that collapse to 14 exact review signatures because the SGD and ComplexPortal PMID:16762366 protein-folding rows share the same term/evidence/reference/qualifier signature.
- Preserved all 19 frozen baseline review rows and marked nine source assertions as retired because they are no longer emitted by the current GOA refresh:
  - GO:0051082 / IBA / GO_REF:0000033
  - GO:0000166 / IEA / GO_REF:0000043
  - GO:0005524 / IEA / GO_REF:0000120
  - GO:0051082 / IEA / GO_REF:0000120
  - GO:0005515 / IPI / PMID:16554755
  - GO:0005515 / IPI / PMID:19536198
  - GO:0005515 / IPI / PMID:27107014
  - GO:0005515 / IPI / PMID:37968396
  - GO:0051082 / IDA / PMID:16762366
- Filled four current GOA rows added by the refresh:
  - GO:0005524 / GO_REF:0000002 / current InterPro ATP-binding row: ACCEPT.
  - GO:0005832 / PMID:21701561 / yeast CCT-actin structural row: ACCEPT.
  - GO:0071944 / PMID:26101841 / CCTdelta/Cct4 cell-periphery row: KEEP_AS_NON_CORE because it captures a monomeric, subunit-specific activity rather than the canonical cytosolic TRiC/CCT folding chamber.
  - GO:0140662 / PMID:18272176 / CCT4 G345D allostery row: ACCEPT.
- The GO_REF:0000033 PAINT rows remain aligned with current PTHR11353 semantics: the inherited protein-folding and CCT-complex nodes are accepted, while the older GO:0051082 molecular-function IBD is retired from current PAINT.
- 2025-2026 web/PubMed searching for exact yeast CCT4/Cct4/YDL143W papers found no newer budding-yeast CCT4 primary paper that changed the GO decisions. The useful new hits were 2025 complex-level TRiC summaries and mammalian/nematode CCT4 papers, which were kept as context rather than cited as yeast-specific GO evidence.
