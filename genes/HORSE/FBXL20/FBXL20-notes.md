# FBXL20 (horse, A0A9L0TR23) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Benchmark target for the ProtNLM2 DONKEY40 / DONKEY40_HORSE_PARTNER cohort; it is the horse
partner of donkey FBXL20 (genes/EQUAS/FBXL20, A0A9L0IQA3). No ProtNLM2 file was opened.

### Setup
- Folder created with `just fetch-gene HORSE A0A9L0TR23 --alias FBXL20`; the stub id is
  A0A9L0TR23. GOA has 3 rows: cytoplasm (IEA SubCell), and SCF ubiquitin ligase complex and
  SCF-dependent proteasomal catabolism (both IBA, PAINT node PTN002547163).
- Deep research: `just deep-research HORSE FBXL20 --provider falcon --fallback perplexity-lite`
  FAILED. Falcon gave "Failed to authenticate" and Perplexity returned HTTP 401 for
  insufficient quota. No deep-research file was written. Instead I used the
  primary literature, which I cached: PMID:17803915 (mouse SCRAPPER, full text) and
  PMID:25593308 (human FBXL20-VPS34, full text), plus the human review's cached papers
  PMID:34731788 and PMID:33234069.

### Identity
- A0A9L0TR23 is 436 aa, the same length as the reviewed human canonical isoform Q96IG2-1 and
  identical to it at every position (FBXL20-bioinformatics/RESULTS.md, compare_horse_human.py).
  The F-box (22-68), the LRR array and the C-terminal ...CRCCIIL CAAX-type motif are all
  intact. It is the canonical full-length product, not a fragment, isoform or alternative
  gene model.
- PANTHER: UniProt places horse, human (Q96IG2), mouse (Q9CZV8) and bovine (Q58DG6) FBXL20 in
  PTHR13318:SF47 "F-BOX_LRR-REPEAT PROTEIN 20". This licenses transferring
  FBXL20-subfamily functions.
- Placement oddity: in interpro/panther/PTHR13318/PTHR13318-entries.csv, rat Fbxl20 Q9QZH7
  (276 aa, a shorter entry) is listed under PTHR13318:SF95 "F-BOX PROTEIN YLR352W", not SF47.
  This looks like a fragment or misclassification affecting only that rat entry. It does not
  bear on the horse protein. There is no FamilyReview (`PTHR13318-review.yaml`) for this family.

### Literature (evolutionary grounding = same PANTHER subfamily SF47)
- Mouse SCRAPPER: [PMID:17803915 "SCRAPPER formed an SCF complex with Skp1 and Cullin1 in mouse
  brain lysates"]; [PMID:17803915 "SCRAPPER directly binds and ubiquitinates RIM1"];
  [PMID:17803915 "the carboxyl-terminal prenylation signal is important for the distinct
  localization"].
- Human FBXL20: [PMID:25593308 "promote its ubiquitination and proteasomal degradation mediated
  by FBXL20 (an F-box protein) and the associated Skp1 (S-phase kinase-associated
  protein-1)-Cullin1 complex"]; FBXL20 is a p53 target. PR55alpha is a further substrate
  (PMID:34731788).
- Family context: [PMID:33234069 "In mammals, Fbxl20 is considered a paralogue for Fbxl2"].

### Decisions
- cytoplasm IEA: ACCEPT.
- SCF ubiquitin ligase complex IBA: ACCEPT. The target sits inside the IBD clade, and there
  is direct SF47 evidence.
- SCF-dependent proteasomal protein catabolism IBA: ACCEPT. The donor list includes mouse
  Fbxl20 (MGI:1919429).
- NEW ubiquitin-like ligase-substrate adaptor activity (GO:1990756), ISS from human/mouse
  SF47. This matches the human review.
- Not added: synapse/presynapse terms and synaptic-vesicle-exocytosis regulation. They are
  neuron-specific mouse observations, and the human review keeps them only as non-core
  Ensembl-Compara IEAs. Regulation of autophagy is also not added; no PAINT node propagates it,
  and I raised it as a suggested question instead.

### Relative
- Closest characterized relatives are human FBXL20 (Q96IG2, identical, same SF47) and mouse
  SCRAPPER (Q9CZV8, SF47). genes/human/FBXL20 has a COMPLETE review. No mouse Fbxl20 review
  exists.
- Modules: none include FBXL20. modules/mitophagy.yaml uses PTHR13318 only for FBXL4
  (SF152).
