# FKBP65 (ROF2) review notes

## 2026-10-28 initial review

- fetch-gene resolved Q9FJL3 (Swiss-Prot, GeneID 834913, TAIR AT5G48570); 14 GOA rows.
- Literature work is in FKBP65-deep-research-manual.md (no deep-research API keys).
- Key papers: PMID:19876748 (thermotolerance, abstract only in cache), PMID:17080288 (expression,
  abstract only), PMID:22268595 (pH homeostasis, abstract only), PMID:24440291 (P. syringae,
  abstract only), PMID:23133621 (PI(3,5)P2 affinity, ROF1 paper, full text),
  PMID:38250364 (proteomics review/primary, full text).

Decisions
- PPIase activity (IBA, IEA) ACCEPT: three FKBP domains, ROF1 FKBD1 active
  [PMID:23133621 "ROF1 contains an FK506 Binding Domain (FKBD) with PPIase activity, (FKBD1)"]; no ROF2 assay found.
- Protein binding (IPI, ROF1 partner) -> MODIFY to protein heterodimerization activity
  [PMID:19876748 "ROF2 has been shown to interact with ROF1, to form heterodimers"].
- cellular heat acclimation (IMP, ARBA IEA): rof2 knockouts are MORE thermotolerant, so ROF2
  is a negative modulator. No "negative regulation of cellular heat acclimation" term exists in
  GO (checked go.db); nearest term GO:1900035 negative regulation of cellular response to heat.
  MODIFY (sign correction) with source_defects to UniProt (assigned_by of both rows).
- protein folding IBA: KEEP_AS_NON_CORE; no folding client demonstrated.
- Vacuole and plastid HDA rows: MARK_AS_OVER_ANNOTATED; soluble cytosolic/nuclear protein,
  no targeted evidence.
- No NEW rows: pH homeostasis, defense, salt germination phenotypes are mutant/overexpression
  phenotypes; the bar in CLAUDE.md is not met.
