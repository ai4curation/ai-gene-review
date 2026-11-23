# ZNF788P notes

## 2026-10-04 Tier 3 over-annotation audit (claude-code)

### Identity and existence
- UniProt Q6ZQV5 (ZN788_HUMAN), "Putative KRAB domain-containing protein ZNF788", 82 aa,
  **PE5 (uncertain)**, CAUTION "Could be the product of a pseudogene". Both FLJ cDNAs
  (BAC87366/AK128282 = FLJ46419, BAC87578/AK128700) are flagged "Wrong choice of CDS".
  Keyword "Proteomics identification" (PeptideAtlas/MassIVE cross-refs); I did not
  determine which peptides, or whether they are unique given the highly similar chr19
  ZNF paralogs.
- HGNC (REST, 2026-10-04): HGNC:33112, "zinc finger family member 788, pseudogene",
  locus_type **pseudogene**, 19p13.2, previous symbol ZNF788, alias FLJ46419.
- Ensembl ENSG00000214189: transcribed_unprocessed_pseudogene; the single transcript has
  no translation.
- Literature: PubMed ZNF788P/ZNF788 returns only methylation-marker papers (anal
  cancer, colorectal cancer, eGFR in HIV, kidney transplant). These are CpG associations
  at the locus, not protein function.

### Sequence history (bioinformatics, ZNF788P-bioinformatics/RESULTS.md)
- Sequence versions 1-2 (2004-2018): 615-aa protein with 14 C2H2 zinc fingers and no
  KRAB. Version 3 (since 2018): 82-aa truncated KRAB-A with 0 zinc fingers.
- KRAB-A aligns to ZNF10 KRAB 48% identity but ends at the ZNF10 equivalent of residue
  68. There is no B box. DV is retained; MLE becomes MQE.
- In AK128700 the KRAB exon and the zinc-finger ORF are in the same frame but separated
  by a stop codon. The locus looks like a KZFP whose KRAB and zinc-finger parts are no
  longer joined.

### Source of the nucleus HDA row (PMID:16791210)
- This was NOT an overexpression study. Abstract: [PMID:16791210 "each tagged with yellow
  fluorescent protein (YFP) at its endogenous chromosomal location"].
- Full text (author-hosted PDF, Carpenter-Singh lab site
  https://carpenter-singh-lab.broadinstitute.org/files/anne/files/20-Sigal_NatMethods_2006.pdf;
  not in the publications cache, which is abstract-only): CD-tagging inserts a
  promoterless, start-codon-less YFP exon into introns in H1299 cells, and "The
  YFP-tagged protein in each clone was identified by 3' RACE". Fig. 3 panel (q) is
  "uncharacterized protein FLJ46419", one of the 20 nuclear proteins studied. FLJ46419
  is the HGNC alias of ZNF788P.
- Implication: a YFP fusion expressed from this locus (or from a transcript that 3' RACE
  assigned to it) is nuclear in H1299 cells. YFP has no ATG, so the upstream exons must
  be translated in frame, and 3' RACE reads the downstream sequence. The tagged product
  therefore most likely includes downstream (zinc-finger) sequence, not the 82-aa KRAB
  fragment. The GOA row is dated 2015-01-22, when the entry was the 615-aa zinc-finger
  sequence (version 2).
- Conflict: real endogenous evidence that the locus makes a nuclear protein, versus
  HGNC/Ensembl pseudogene status and the 2018 UniProt remodelling to an 82-aa fragment.
  I cannot tell from here whether the 3' RACE read was unique to ZNF788P rather than a
  paralogous chr19 zinc-finger gene. -> UNDECIDED.

### IEA regulation of DNA-templated transcription (InterPro IPR001909/IPR036051)
- KRAB repression is DNA-binding-dependent: [PMID:8183939 "the KRAB domain functions as a
  DNA binding-dependent transcriptional repressor when fused to a heterologous DNA-binding
  domain from the yeast GAL4 protein"]. The 82-aa product has no DNA-binding domain and
  comes from an annotated pseudogene. -> REMOVE.

### Propagation route
- GO:0006355 comes from InterPro2GO on the KRAB signature (IPR001909, IPR036051). The
  mapping triggers on any KRAB-A match, including truncated fragments with no zinc
  fingers.
- GO:0005634 is HDA, assigned by UniProt (2015) against the former 615-aa sequence and
  carried over when the sequence was replaced in 2018.
