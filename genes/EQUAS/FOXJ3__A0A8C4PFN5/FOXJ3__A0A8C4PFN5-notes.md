# FOXJ3 (donkey, A0A8C4PFN5) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: full-length donkey FOXJ3 model A0A8C4PFN5 (623 aa, TrEMBL, PE 4). Folder is
`FOXJ3__A0A8C4PFN5` because `genes/EQUAS/FOXJ3` holds the exon-skipped benchmark model
A0A9L0JKH1 from the same Ensembl gene (ENSEASG00005001210). No ProtNLM2 files were
opened or used.

### Deep research

`just deep-research-falcon EQUAS FOXJ3__A0A8C4PFN5 --fallback perplexity-lite` failed:
falcon "Failed to authenticate"; perplexity-lite HTTP 401 (insufficient quota). The
review is built from primary literature found by a PubMed `foxj3[tiab]` search (cached in
`publications/`) and UniProt records.

### Evolutionary grounding

- Donkey, mouse Q8BUR3 and human Q9UPW0 all map to PANTHER PTHR46078:SF3 (FORKHEAD BOX
  PROTEIN J3); FOXJ2 (Q9P0K8) is PTHR46078:SF1. Donkey is 95.3% identical to mouse and
  98.2% to human over the full length, fork-head domain 95/96 and 91/92 identical
  [file:EQUAS/FOXJ3__A0A8C4PFN5/FOXJ3__A0A8C4PFN5-bioinformatics/RESULTS.md].
- PAINT (node PTN002918318, seen on mouse/human IBA rows in QuickGO) propagates
  GO:0000978, GO:0000981, GO:0006357 and nucleus across FOXJ2/FOXJ3, but NOT the mouse
  IMP terms spermatogenesis / male meiosis I. Treated as a deliberate decision: the
  donkey's meiosis/spermatogenesis rows come only from Ensembl Compara one-to-one
  ortholog transfer (GO_REF:0000107) of mouse IMP PMID:27739607.

### Literature (mouse / human / Xenopus; nothing on donkey)

- Mouse Foxj3 activates Mef2c via a conserved forkhead binding site; ChIP and reporter
  assays in C2C12 [PMID:19914232 "Transcriptional assays in C2C12 myoblasts revealed that
  Foxj3 transcriptionally activates the Mef2c gene in a dose dependent fashion and binds
  to the conserved FBS."]. Mutants have fewer type I fibres and impaired regeneration.
- Mouse germ-cell cKOs: Mvh-Cre -> Sertoli-cell-only; Stra8-Cre -> meiotic arrest with
  reduced mRNA of Rad51, Dmc1, Hormad1 etc. [PMID:27739607 "Thus, we conclude that FOXJ3
  is required for the survival of spermatogonia and participates in spermatocyte
  meiosis."]. Abstract-only in cache. This is necessity evidence for a TF; the meiotic
  machinery itself is executed by its target genes.
- Human FOXJ3 knockdown abolishes cell-cycle oscillation of a forkhead-site reporter
  [PMID:22740631]. Human SELEX/methyl-SELEX motifs [PMID:23332764, PMID:28473536]
  (cache text does not name FOXJ3; these are only the source references of human IDA rows).
- Mouse cortex: FOXJ3 nuclear, ChIP-seq targets include Pten [PMID:41803108].
- Brown fat: Foxj3 induces PGC-1alpha/UCP1 [PMID:37939221]. Xenopus: Foxj3 represses
  Activin/Nodal and BMP responsive transcription [PMID:40522413] - so FOXJ3 is not purely
  an activator; context dependent.

### Decisions

Core: RNA Pol II sequence-specific DNA-binding transcription factor, nucleus, positive
regulation of Pol II transcription. Broad DNA binding / DNA-binding TF activity /
regulation of DNA-templated transcription -> TOO_GENERAL. Spermatogenesis ->
KEEP_AS_NON_CORE (inferred from mouse only). Male meiosis I -> MARK_AS_OVER_ANNOTATED
(transcriptional requirement, not participation; stage I not resolvable from abstract;
PAINT declined it). No NEW terms: muscle fibre type, thermogenesis and cortical
development are mouse knockout/knockdown phenotypes and are not transferred.
