# erg-6 notes

- UniProt Q7S4Z6 records `erg-6` as the primary name, `erg9` as a synonym, and
  `NCU06054` as the ORF name. The protein is assigned to PANTHER
  `PTHR11626:SF2`, the squalene synthase subfamily.
- The local PTHR11626 family review treats the SF2 fungal, animal and plant
  single-copy enzymes as canonical squalene synthases, while flagging only
  Arabidopsis `SQS2` in SF3 and several Botryococcus SF2 members as exceptions.
  The PAINT node that supports `GO:0051996` and `GO:0045338`
  (`PTN001700951`) is therefore sound for Neurospora `erg-6`, and the fungal
  `GO:0006696` ergosterol biosynthesis node (`PTN000907895`) is also scoped to
  the right lineage.
- The `GO:0005789` IBA follows from a eukaryotic ER-membrane PAINT node. The
  UniProt record independently calls Q7S4Z6 an endoplasmic-reticulum
  multi-pass membrane protein, so both ER-membrane rows can be accepted.
- Seiler and Plamann's Neurospora morphology screen mapped a complementation
  group with swollen conidia or bulbous germ tubes to `erg-9 (NCU06054.1) ERG9
  (squalene synthase)` in the PMC full text of PMID:12960438. The locally
  cached abstract only says that the study identified 45 defective genes in its
  mutant collection, so the PMID is useful as direct Neurospora context but not
  as a cached exact quote for squalene synthase activity.
- PMID:23755044 is expression and azole-response context. It found several
  Neurospora ergosterol biosynthesis genes to respond transcriptionally to
  ketoconazole, but the mutant and sterol-accumulation experiments were about
  `erg5`; it should not be used as direct evidence for `erg-6` enzymatic
  activity.
