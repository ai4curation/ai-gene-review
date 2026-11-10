# Map2k3 (mouse) review notes

## 2026-10-26 - initial review

- Fetched with `just fetch-gene mouse Map2k3`; UniProt O09110 (MP2K3_MOUSE) confirmed. 48 GOA rows.
- No deep-research API keys; manual synthesis in `Map2k3-deep-research-manual.md`.
- Full text read: PMID:10097111, PMID:17438131, PMID:18948261, PMID:20550965. Abstract only: PMID:8900184, PMID:10202148, PMID:11593045, PMID:15767678.
- Core: MAP kinase kinase activity (GO:0004708) toward p38 [PMID:10097111 "The MKK3 and MKK6 protein kinases are specific for p38 MAP kinase"]; process p38MAPK cascade (GO:0038066).
- Decisions:
  - Generic kinase MF rows (protein kinase / tyrosine / serine kinase activity) -> MODIFY to GO:0004708, consistent with human MAP2K3 review.
  - MAPK cascade, stress-activated protein kinase signaling cascade, positive regulation of MAPK cascade -> MODIFY to p38MAPK cascade (MKK3 is a step of the cascade, not a regulator of it; JIP4 paper shows requirement of MKK3/MKK6 for JIP4-induced p38 activation [PMID:15767678]).
  - Cardiac muscle contraction (IMP, PMID:11593045) is from overexpression of constitutively active MKK3bE; marked as over-annotated, as is the ARBA IEA.
  - protein kinase binding rows -> MODIFY to MAPKKK binding (GO:0031435; ASK1 [PMID:18948261]) and MAPK binding (GO:0051019; p38 substrate).
  - protein binding with alpha-4/Igbp1 (PMID:17438131) -> MODIFY to protein phosphatase 2A binding (GO:0051721), since MEK3 co-precipitated PP2Ac in an alpha-4-dependent complex.
  - Downstream physiological contexts (inflammation, cytokine production, LPS, VEGF, endothelial migration, hippo, UV-B, NLRP1) kept as non-core.
- PMID:20550965 (rat ischaemic heart) is not a GOA source for mouse; used as context for activation of MKK3 by ischaemia.
- No NEW terms proposed.
