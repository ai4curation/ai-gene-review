# Arrb2 (rat) review notes

## Session 1 (2026-10-28)

- Fetched with `just fetch-gene rat Arrb2`: P29067 (ARRB2_RAT, reviewed), RGD:2157,
  GeneID 25388. 127 GOA rows.
- No deep-research API; literature synthesis in `Arrb2-deep-research-manual.md`.
- Key papers read in full text: PMID:19171933 (BAD anti-apoptotic signalling, rat VSMC),
  PMID:19254952 (AT1R ERK/EGFR transactivation, rat VSMC), PMID:20650893 (TRPV4; beta-arrestin-2
  knockdown increases TRPV4 ubiquitination), PMID:19008961, PMID:19200235, PMID:19014370,
  PMID:21078978, PMID:23911909, PMID:24719556, PMID:14757828.

### Decisions

- Core: phosphorylated-GPCR binding, desensitization, clathrin-cargo adaptor role in GPCR
  internalization (AP-2/clathrin), and signalling scaffold for ERK1/2 (and AKT).
- Generic terms (signaling receptor binding, enzyme binding, molecular adaptor activity,
  endocytosis, cytoplasmic vesicle, regulation of GPCR signalling) modified to specific terms.
- Bare protein binding rows modified to kinase binding / ubiquitin protein ligase binding /
  PKB binding.
- Phenotype-level process terms (sensory perception, pain, walking behaviour, circadian
  rhythm from expression, gene expression, cardiac differentiation, RNA pol II transcription)
  marked as over-annotations.
- HTR2A: positive (human receptor) and NOT (rat receptor) are both true (primate-specific ASK
  motif, PMID:19919577); recorded with consistency_exception.

### Source defects flagged (RGD)

- PMID:157224 -> PMID:1517224 (dropped digit), rows GO:0007186 and GO:0045211.
- PMID:12890920 for GO:0019904 with Drd2: paper is about dystrophin; reference likely wrong.
- PMID:24719556 for GO:1904037: no epithelial apoptosis data in full text.

No NEW annotations proposed.
