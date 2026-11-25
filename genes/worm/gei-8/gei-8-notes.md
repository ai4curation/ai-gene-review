# gei-8 review notes

## 2026-10-26 initial review

- Fetched with `just fetch-gene worm gei-8`; UniProt P34333 (NCOR1_CAEEL) confirmed.
- Deep research providers unavailable; literature compiled manually in gei-8-deep-research-manual.md.
- Key paper PMID:23484030 (full text): GEI-8 is the NCoR/SMRT orthologue; C-terminal region I binds GST-NHR-60 [PMID:23484030 "the C-terminal region I of GEI-8 that includes the predicted NR1 binding site showed affinity to GST-NHR-60"]; ok1671 deletion gives developmental, gonad, locomotion and cholinergic defects; microarray shows bidirectional deregulation.
- PMID:22078881: muscle-specific gei-8 RNAi increases mitochondria and O2 consumption [PMID:22078881 "the muscle-specific knockdown of gei-8 enhanced O2 consumption in these NR350 worms"].
- GOA has only 5 rows (2 IBA, 2 IEA, 1 IPI protein binding with GEX-3).
- Decisions: accept nucleus, chromatin and regulation of transcription by RNA pol II (the worm data show both up- and downregulation, so the general regulation term is kept rather than refined to negative regulation); remove bare protein binding (GEX-3 Y2H) per the repository protein-binding policy (uninformative MF, interaction not disputed); keep protein-containing complex as non-core (no worm evidence for a specific complex).
- NEW: nuclear receptor binding (GO:0016922) from the GST-NHR-60 pull-down (direct binding assay, MF).
- Did not propose transcription corepressor activity as NEW: in worm it is inferred from orthology and NHR binding only; recorded as core function MF with that caveat and as a suggested question.
- Phenotype-derived processes (gonad development, locomotion, mitochondrial regulation) not proposed as NEW: these are pleiotropic downstream effects of a transcriptional coregulator.
