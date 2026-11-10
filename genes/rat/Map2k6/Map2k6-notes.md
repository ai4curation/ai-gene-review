# Map2k6 (rat) review notes

## Session 2026-10-28

- `just fetch-gene` had already been run; the UniProt id is A0ABK0M3C5 (TrEMBL, RGD:620666),
  matching the task. GOA has 35 rows, all keyed to A0ABK0M3C5.
- Cached and read: PMID:20550965 (full text; the key rat paper), PMID:12649265, 12029621,
  11328854, 16755153 (abstract only), plus mouse/human donor papers PMID:20551513, 11593045,
  15767678, 29021624 (full text), 19141286 (full text), 9768359, 11279118, 8622669,
  10097111 (full text).
- No deep-research provider; literature synthesis in `Map2k6-deep-research-manual.md`.

### Key evidence

- Rat MKK6 MAPKK activity: endogenous MKK6 immunoprecipitated from perfused heart assayed with
  GST-p38 + GST-ATF2 [PMID:20550965 "1 μg GST-p38 and 4 μg GST-ATF2 for MKK3 and MKK6"].
- Ischaemia activates MKK6 late; ASK1 preferentially activates MKK6 [PMID:20550965 "activation
  of ASK1 leads to preferential activation of MKK6 and consequent activation of p38"].
- Human function statement [file:human/MAP2K6/MAP2K6-uniprot.txt "Dual specificity protein
  kinase which acts as an essential"].

### Decisions

- Generic kinase/transferase/Ser-Thr kinase MF rows MODIFY -> GO:0004708 (already on gene).
  GO:0004708 is under GO:0004712, not GO:0004674 (OAK).
- MAPK cascade rows MODIFY -> GO:0038066 p38MAPK cascade (is_a descendant, OAK).
- positive regulation of MAPK cascade MODIFY -> GO:1900745, as in rat Map2k3.
- identical protein binding MODIFY -> GO:0042803 protein homodimerization activity
  (autoinhibitory dimer, PMID:19141286), as in the human MAP2K6 review.
- cardiac muscle contraction rows: donor is the MKK6bE gain-of-function transgene
  (PMID:11593045) -> MARK_AS_OVER_ANNOTATED.
- IEP rows: response to ischemia and sorbitol (activity measured) -> KEEP_AS_NON_CORE;
  ovulation cycle process and response to xenobiotic stimulus (correlative activation/level
  changes, abstract only) -> MARK_AS_OVER_ANNOTATED.
- Rat IMP rows (prostaglandin secretion, apoptosis) -> KEEP_AS_NON_CORE (downstream outcomes,
  dominant-negative MKK6 experiments).
- No NEW rows proposed.
- The automatic UniProt name "Serine/threonine-protein" (PROSITE-ProRule) is truncated and the
  EC 2.7.11.1 is the generic one; the established reaction is EC 2.7.12.2. Not a GO row; noted
  as a suggested question.
