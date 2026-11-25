# Tbc1d4 (rat) review notes

## Session 2026-10-28
- `just fetch-gene rat Tbc1d4` resolved D3Z881 (TrEMBL, RGD:1561609, GeneID 306117), as
  expected. 9 GOA rows: cytoplasm (IEA), cytosol (ISO), vesicle-mediated transport (ISO),
  negative regulation of vesicle fusion (IMP), vesicle (IDA), cellular response to insulin
  stimulus (IDA, IEA, ISO x2).
- Cached and read PMID:21454690 (full text). Also cached PMID:15971998 (full text),
  PMID:21041651 (full text), PMID:12637568 and PMID:15616009 (abstract only).
- Key rat findings [PMID:21454690 "we found that, in rat adipocytes, there was an
  insulin-dependent increase in the level of AS160 associated with GLUT4 vesicles"];
  [PMID:21454690 "AS160 remains in its GAP-active form, the associated Rab remains in the
  GDP form, and fusion activity is therefore low"].
- Rat lacks any MF row. GTPase activator activity is well established for the human
  ortholog [PMID:15971998 "The GAP domain was active against Rabs 2A, 8A, 10 and 14."] and
  the catalytic fingers are conserved in rat (bioinformatics/RESULTS.md); proposed as NEW
  ISS. Rat L6 data support Rab8A/Rab13 as AS160 targets [PMID:21041651].
- The IDA "vesicle" row is GLUT4 vesicles immunoisolated from rat adipocytes; refined
  to GO:0032593 insulin-responsive compartment (is_a ... vesicle, checked with OAK).
- Cytoplasm IEA refined to cytosol (already carried by ISO row).
- No PAINT IBA rows for rat; the human IBD at PTN002742831 (cytosol, vesicle-mediated
  transport) is seeded by O60343 only.
- No NEW process terms proposed (NEW bar). 14-3-3 binding left as a question.
