# Tap42 review notes (DROME, Q9VJZ5)

## Session 1 (create review)

- fetch-gene resolved Q9VJZ5 (TrEMBL, unreviewed); 11 GOA rows.
- No deep-research provider available; literature summary in Tap42-deep-research-manual.md.
- Full text read: PMID:22701670 (Wang et al. 2012, PLoS One), PMID:15802506 (Cygnar et al. 2005).
  Abstract only: PMID:17570358, PMID:38944040. PMID:37061542 full text has no Tap42-specific text
  (data in supplementary tables).

### Decisions

- TOR signaling (IBA): REMOVE. Direct target-specific evidence of divergence: Drosophila Tap42
  is not required for TOR signaling [PMID:15802506 "Tap42 does not contribute significantly to TOR signaling in Drosophila"],
  corroborated by S6K phosphorylation being unaffected on knockdown [PMID:17570358].
  The PAINT node (seeded by Arabidopsis TAP46 AT5G53000) may hold for yeast/plants; the fly
  lineage appears to have lost/never had the TOR link. Expert flag.
- regulation of signal transduction (IEA InterPro2GO): MARK_AS_OVER_ANNOTATED; the IPR007304
  mapping is a TOR-derived generalization; fly evidence on JNK/HH/DPP is knockdown phenotype only.
- protein binding x2 (IPI, interactome; partner Mts/P23696): MODIFY to protein phosphatase 2A
  binding (GO:0051721), which the co-IP data in PMID:22701670 and PMID:15802506 support.
- PP2A complex (IDA): KEEP_AS_NON_CORE. Co-IP shows Tap42-catalytic subunit complexes, not
  the A/B/C holoenzyme defined by GO:0000159; alpha4-family proteins bind PP2Ac apart from the
  scaffold. Defer to curator but flag the definitional mismatch as a question.
- protein phosphatase regulator activity (IBA, IMP): ACCEPT; core MF.
- protein phosphatase inhibitor activity (IGI with mts): KEEP_AS_NON_CORE; direction inferred
  only genetically (mts hypomorph suppression), and other data (mitotic arrest resembling PP2A
  loss) argue for context-dependent positive roles too.
- cytosol (IBA): ACCEPT; consistent with Tap42 retaining PP2Ac in the cytoplasm.
- mitotic spindle organization (IMP), wing disc morphogenesis (IMP): KEEP_AS_NON_CORE
  (pleiotropic downstream consequences of PP2A-family misregulation).
- No NEW process terms proposed (phenotype data alone do not meet the bar).
