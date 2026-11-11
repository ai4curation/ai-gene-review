# wts-1 review notes

## Session 1 (create)

- fetch-gene resolved O45797 (WARTS_CAEEL), 31 GOA rows. 
- PMID:12213836 (Gruneberg et al. 2002, CeCDC-14) was flagged as a key paper. Full text read: it only mentions
  wts-1 as ORF T20F10.1, a putative Dbf2p homologue whose RNAi gives F1 L1 arrest
  [PMID:12213836 "Depletion of the ORF T20F10.1, one of the putative Dbf2p homologues, caused the offspring of injected worms to arrest at an early larval stage (L1)."].
  It is not cited by any GOA row; used only as a historical phenotype reference.
- Cached additional papers: PMID:31358532 (Lee 2019, full text), PMID:41746831 (Huynh 2026, full text),
  PMID:40178516 (Lee 2025, full text), PMID:34817059 (Zhang 2021, abstract only).
- Three GOA-cited papers (19605499, 19737560, 23396260) are abstract-only. Experimental rows from them are not
  overruled; where a row describes a downstream phenotype I marked it non-core or over-annotated rather than removed.

## Decisions

- Core: protein serine/threonine kinase acting on YAP-1 (binding via N-terminal PPxY / YAP-1 WW), retaining YAP-1
  in the cytoplasm, in hippo signaling, localized at the subapical cortex of intestinal cells.
- IBA G1/S transition, positive regulation of apoptotic process, regulation of organ growth: MARK_AS_OVER_ANNOTATED.
  The PAINT node is correct for vertebrate/fly LATS but C. elegans WTS-1 has no proliferation/apoptosis role
  [PMID:19605499 "The wts-1 phenotype was not caused by cell proliferation or apoptosis defects."].
- defecation IMP: MARK_AS_OVER_ANNOTATED (likely secondary to loss of intestinal lumen integrity). Expert check advised,
  since full text was not available.
- No NEW terms. Candidates considered and rejected under the NEW bar: maintenance of apical/basal polarity
  (WTS-1 acts via YAP-1/EGL-44 transcriptional repression, i.e. regulatory, single-lab), sorting endosome
  (single abstract-only report), neuron maintenance (mutant phenotype only).
