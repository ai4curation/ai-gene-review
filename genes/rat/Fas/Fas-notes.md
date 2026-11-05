# Fas (rat) review notes

## Session 1

- Fetched with `just fetch-gene rat Fas`; UniProt Q63199 (TNR6_RAT), 134 GOA rows.
- Cached all GOA PMIDs plus PMID:16987298 (requested as a key paper). On reading, PMID:16987298
  is a glioblastoma pharmacology paper; for rat it only shows Fas protein induction in RG2
  glioma cells by n-butylidenephthalide [PMID:16987298 "BP significantly induced Fas expression
  (from one to 41.3-fold vs. one to 7.7-fold in DBTRG-05MG and RG2 cells, respectively)"].
  Recorded as a low-relevance reference; no annotation rests on it.
- No deep-research API; literature synthesis in `Fas-deep-research-manual.md`.

### Decisions

- MF: all GO:0005031 (TNF receptor activity) and GO:0004888 rows MODIFY to GO:0005035 death
  receptor activity (Fas binds FASLG, not TNF), matching the human FAS review.
- Apoptotic BP rows (apoptotic process, apoptotic signaling pathway, extrinsic apoptotic
  signaling pathway) MODIFY to GO:0008625; generic signal transduction and the
  TNF-mediated signaling IEA MODIFY to GO:0036337 Fas signaling pathway.
- `death-inducing signaling complex` MODIFY to `CD95 death-inducing signaling complex`.
- IEP rows: KEEP_AS_NON_CORE where the same paper also shows Fas mediates the response
  (blocking antibody, ligand sensitisation); MARK_AS_OVER_ANNOTATED where only expression
  changed. None removed, because IEP response-to terms are formally allowed.
- PMID:29970988: full text read; only Faslg was perturbed. Schwann-cell IMP rows REMOVEd
  with a source defect (wrong gene) - flagged for expert check.
- No NEW terms proposed.
