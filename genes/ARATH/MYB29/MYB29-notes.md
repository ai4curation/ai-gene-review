# MYB29 review notes

## 2026-10-28 session

- fetch-gene resolved Q9FLR1 (MYB29_ARATH, TAIR AT5G07690, GeneID 830662) as expected; 31 GOA rows.
- Cached the UniProt-cited papers PMID:20348214, PMID:18446225, PMID:23792303, PMID:23943862,
  PMID:23580754 in addition to the GOA references. PMID:23144921 full text read (drought induces
  MYB29 about two-fold; aphids repress it).
- PMID:28167700 (RAO7/MYB29, AOX1a) is abstract-only: rows from it were not removed. The
  GO:0009644 "response to high light intensity" rows are UNDECIDED because the abstract describes
  combined moderate light plus drought; recorded a SUSPECTED source defect (TAIR).
- GO:0006355 IEP (PMID:17420480) MODIFIED to positive and negative regulation of DNA-templated
  transcription; IEP code flagged as a suspected wrong evidence code.
- GO:0010438 sulfur starvation (TAS) marked over-annotated: expression responsiveness only
  [PMID:17420480 "Under sulfur-deficiency conditions, the expression of PMG1 / Myb28 , PMG2 / Myb29 , and ATR1 / Myb34 was down-regulated, presumably to shut down GSL biosynthesis"].
- Bare protein binding (SRO5, PMID:32612234) removed per policy.
- No NEW annotations: defence phenotypes are indirect (via glucosinolates), and expression data
  do not meet the NEW bar. Proposed an aliphatic-specific positive regulation of glucosinolate
  biosynthesis term (mirrors MYB34 indole proposal).
- GO has no negative regulation of mitochondria-nucleus signaling pathway term (checked OAK).
