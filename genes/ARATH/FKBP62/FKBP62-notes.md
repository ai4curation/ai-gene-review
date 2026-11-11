# FKBP62 (ROF1) review notes

## Session 1 (2026-10-26)

- Fetched with `just fetch-gene ARATH FKBP62`; UniProt Q38931 confirmed (FKB62_ARATH, At3g25230).
- No deep-research API keys; manual literature synthesis in FKBP62-deep-research-manual.md.
- Additional PMIDs cached: 17080288 (ROF1/ROF2 bind HSP90), 32967551 (NBR1 autophagy of ROF1),
  38250364 (rof proteomics), 22268595 (ROF2 pH homeostasis).

### Key reasoning
- Core: TPR-domain HSP90 co-chaperone [PMID:19366428 "ROF1 binds heat shock proteins HSP90.1 via its
  tetratricopeptide repeat domain"] sustaining HsfA2-dependent sHSP expression during long-term
  acquired thermotolerance; FKBD1 is the canonical PPIase domain [PMID:23133621].
- PPIase activity is by similarity only (no direct assay found); IBA placement in the FKBP4/5 clade is
  sound, accept.
- protein binding IPI rows: HSP90.1 row -> MODIFY to Hsp90 protein binding (GO:0051879).
  FKBP65 heterodimer and AGO1 copurification rows kept as non-core.
- cytoplasm rows -> MODIFY to cytosol (HDA support from two cytosol fractionation proteomics papers).
- response to heat -> MODIFY to cellular heat acclimation (GO:0070370 is_a heat acclimation, is_a
  cellular response to heat), which the gene already carries by IMP.
- Seed germination phenotype is only seen under salt/osmotic stress
  [PMID:23133621 "no difference was recorded on the germination rate of plants grown on media without NaCl"]
  -> non-core.
- PI(3)P / PI(3,5)P2 binding only by lipid overlay; physiological relevance unproven -> non-core.
- No NEW terms proposed. Considered "protein import into nucleus" style terms for heat-induced
  relocalization but ROF1 is cargo, not machinery; not proposed.
