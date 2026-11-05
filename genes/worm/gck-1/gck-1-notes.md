# gck-1 review notes

- 2026-10-28: Fetched (H2L099 confirmed, Swiss-Prot entry GCK1_CAEEL, WormBase T19A5.2a). 21 GOA rows.
- PMID:25743393 (excretory canal; source of 12 GOA rows) is abstract-only in cache and has no PMC copy;
  experimental rows from it are kept/accepted deferring to the WormBase curator, except the GTPase-activity
  regulation row, which is marked over-annotated as an indirect readout (reduced CDC-42 activation).
- PMID:12213836 (Gruneberg 2002, CeCDC-14) read: only an RNAi screen result for T19A5.2 (germline degeneration);
  no GO annotation comes from it; cited as background.
- Full text read: PMID:19826475 (MPK-1 binding, germline), PMID:28285996 (bridges), PMID:32491957 (cytokinetic ring).
- Rows on apical plasma membrane (IEA, EXP) MODIFY to the more specific cytoplasmic side of apical plasma membrane
  (GO:0098592) that the gene already carries by IDA.
- NEW CC: actomyosin contractile ring (GCK-1::GFP localization in zygote, PMID:32491957
  "GCK-1/CCM-3 localize to the cytokinetic ring and cortical pulses downstream of the master regulator RhoA").
- No NEW BP terms: perturbation-only data (bridge stability, contractility, katanin) do not meet the NEW bar.
- STRIPAK membership (GO:0090443) recorded in core_functions in_complex, not as NEW row (abstract-level evidence).
