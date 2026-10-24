# A0A3B6RKV1 (LOC123148885, wheat) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 prediction files and prediction-evidence folders were not opened or used.

### Identity
- A0A3B6RKV1 is the full-length 511-aa product of TraesCS7A02G443400 (chr 7A). It is not a
  fragment or an isoform: the protein is collinear with Arabidopsis JMJ22 (Q67XX3, 502 aa)
  over its full length (494 aligned columns, 62.6% identity), and it keeps the F-box (89-135),
  the JmjC domain (285-445) and all three Fe(II) ligands. There is no reviewed/canonical
  wheat entry, so this TrEMBL entry is the canonical wheat product (PE 3).
- Homeologs on 7B (A0A3B6SQ95) and 7D (A0A3B6TWS8) come from the earlier review and the
  generated OpenScientist report; I did not re-verify them.

### Phylogenetic placement (file:WHEAT/A0A3B6RKV1/A0A3B6RKV1-bioinformatics/RESULTS-rereview.md)
- PANTHER PTHR12480:SF21 = "JMJC DOMAIN-CONTAINING PROTEIN 8" (JMJD8-related). The wheat
  protein, AtJMJ22 (Q67XX3) and HsJMJD8 (Q96S16) are all in SF21. The earlier review called
  SF21 the "JMJD6 subfamily", which is wrong: JMJD6 is SF32.
- AtJMJ20 (Q67ZB6), JMJ22's redundant partner in Cho et al. 2012, is in SF6 (JMJD4-like), so
  it is a paralog. The ortholog is JMJ22.
- Within SF21 the F-box/JmjC architecture belongs to the plant branch. Human JMJD8 is 264 aa,
  has no F-box, and is curated by UniProt as ER-lumen/cytoplasm (PubMed:29133832,
  PubMed:27199445).
- Fe(II) ligands: JMJ22 H324/D326/H407 map to wheat H330/D332/H413. The earlier review gave
  "His362" as the third ligand, which is incorrect.

### UniProt "JARID1 histone demethylase family" similarity
- The earlier description said this was an error. The same text appears in the Swiss-Prot
  JMJ22 entry (ECO:0000305), so it is UniProt's family naming for this group, not an
  architectural claim. It is still misleading: the falcon deep-research report took it to
  mean KDM5/H3K4 demethylase, which is wrong for this protein (no JmjN/ARID/PHD/FYR domains).
  I treat the falcon report as MISCITED for subfamily and do not use it as support.

### PAINT (PTN001753861; interpro/panther/PTHR12480/PTHR12480-paint.tsv)
- IBD terms are nucleus (donors AT5G06550, Q386V9, Q96S16) and GO:0000987 (donor AT5G06550
  only).
- JMJ22's GO:0032452 histone demethylase activity (TAIR IGI) and its process terms
  (seed germination, photomorphogenesis, red light, GA signaling, epigenetic regulation) were
  NOT propagated. I treat that as a deliberate curator decision. The earlier review's MODIFY
  of metal ion binding to histone demethylase activity, and its core-function assertions of
  histone demethylase activity and epigenetic regulation, are withdrawn. In their place the
  review asserts NEW GO:0016706 2-oxoglutarate-dependent dioxygenase activity (ISS from
  conserved catalytic residues plus JMJ22 Rhea reaction ECO:0000269) and MODIFY of metal ion
  binding to ferrous iron binding.

### GO:0000987 cis-regulatory region sequence-specific DNA binding (IBA)
- The donor is a TAIR IDA on JMJ22 from PMID:22483719, which is abstract-only in the cache.
  The abstract says SOMNUS directly represses JMJ20/JMJ22, so the EMSA keyword may refer to
  SOMNUS binding the JMJ promoters. A Y1H network paper (PMID:25533953) also recovered JMJ22
  as a promoter binder (TAIR GO:0000976 IPI). I cannot resolve this from the abstract. I left
  the row UNDECIDED and did not remove it, and raised it as a suggested question.

### Modules / relative
- No modules/ files reference PTHR12480, JMJ22 or JMJD8.
- Relative to review next: Arabidopsis JMJ22 (Q67XX3, ARATH). It is in the same PANTHER
  subfamily and is experimentally characterised. The repo has no review for it.
- The family review interpro/panther/PTHR12480/PTHR12480-review.yaml agrees with SF21
  placement (wheat + JMJ22 share F-box/JmjC and subfamily). No disagreement.
