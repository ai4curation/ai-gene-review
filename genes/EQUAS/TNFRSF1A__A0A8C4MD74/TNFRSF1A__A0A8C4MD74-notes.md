# TNFRSF1A (donkey, A0A8C4MD74) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Target: A0A8C4MD74, the 453-aa product of the Ensembl canonical transcript ENSEAST00005025834 of
donkey gene ENSEASG00005016176. The folder is `TNFRSF1A__A0A8C4MD74` because `genes/EQUAS/TNFRSF1A/`
already holds the review of the exon-3-skipping model A0A9L0JKX4 (410 aa) from the same gene. No
ProtNLM2 output was opened or used.

Setup: `just fetch-gene EQUAS A0A8C4MD74 --alias TNFRSF1A__A0A8C4MD74` (35 GOA rows, all IEA:
Ensembl Compara GO_REF:0000107, combined GO_REF:0000120 incl. TreeGrafter PTN001499618, InterPro2GO
GO_REF:0000002, ARBA GO_REF:0000117).

Deep research: `just deep-research-falcon EQUAS A0A8C4MD74 --alias TNFRSF1A__A0A8C4MD74 --fallback
perplexity-lite` FAILED: falcon "Failed to authenticate" (Edison client); perplexity-lite HTTP 401
insufficient_quota. No deep-research file was written. Continued from cached publications on human
TNFR1 (PMIDs 9435233, 8387891, 7758105, 8565075, 12887920, 1698610, 17010968, 2158863, 25816133;
all quotes re-located in `publications/`). A web search found no experimental study of donkey TNFR1.

Evolutionary grounding:
- UniProt: PANTHER PTHR46861:SF1 (the TNFRSF1A family has a single subfamily), same as human P19438
  and mouse P25118. PAINT IBD node PTN002930098 (Euteleostomi) carries GO:0005031, GO:0043120,
  GO:0043235, GO:0045121, GO:0006954 (`interpro/panther/PTHR46861/PTHR46861-paint.tsv`). Donkey is
  inside this clade. PAINT did not propagate the mouse phenotype-derived terms (valve development,
  cardiac hypertrophy, blood-brain barrier, etc.) although mouse seeds the node; treated as deliberate.
- Own analysis (`TNFRSF1A__A0A8C4MD74-bioinformatics/RESULTS.md`): 76.1% identity to human over 448
  aligned positions; CRD1-4 73-91% identical; 24/24 human ectodomain cysteines conserved; TM 86%;
  death domain 88%. 98.2% identical to horse A0A5F5Q204. The UniProt CAUTION about PRU00206 reflects
  PROSITE calling only two CRD repeats, not a real loss of cysteines.

Decisions: accept the core receptor terms (TNF receptor activity, TNF binding, TNF-mediated
signalling, NF-kappaB, inflammatory response, plasma membrane, cell surface, membrane raft, TNFRSF
complex); MODIFY general terms (signaling receptor activity -> GO:0005031; signal transduction ->
GO:0033209; apoptotic process -> GO:0008625; signaling receptor complex -> GO:0002947); mark mouse
knockout phenotypes, ARBA high-level terms, LPS response, gene expression, prostaglandin metabolism,
mechanical stimulus and protein localization to PM (cargo) as over-annotated; keep JAK-STAT,
transcription, astrocyte activation, negative regulation of inflammation, execution phase of
apoptosis, endothelial barrier, Golgi and extracellular region as non-core. Every function in this
review is inferred by orthology; none is experimentally established in donkey.
