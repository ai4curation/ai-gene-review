# hfq (PA4944, Q9HUM0) notes

## Identity

- UniProt Q9HUM0 (Swiss-Prot, PE 1), RNA-binding protein Hfq, Sm-like homohexamer (HAMAP MF_00436).
  PANTHER Hfq family; InterPro IPR005001.

## Function

- RNA chaperone that binds sRNAs and mRNAs [UniProt CC FUNCTION, HAMAP MF_00436].
- Hfq affects about 5% of PAO1 transcripts; it stimulates rhlI translation indirectly by binding and
  stabilising the regulatory RNA RsmY, which sequesters the translational repressor RsmA
  [PMID:16468994 abstract "We demonstrate that Hfq binds to and stabilizes the regulatory RNA RsmY"; "an
  alleviation of the negative effect of RsmA accounts for the observed stimulation of rhlI expression by
  Hfq"]. Abstract only in the cache.
- Hfq is the principal post-transcriptional regulator of carbon catabolite repression in PAO1: it binds
  A-rich sequences in the amiE ribosome binding site and represses translation in vitro and in vivo; the
  regulatory RNA CrcZ binds Hfq with high affinity and acts as a decoy that relieves repression
  [PMID:24945892 "Hfq is shown to bind to A-rich sequences within the ribosome binding site of the model
  mRNA amiE, and to repress translation in vitro and in vivo"; "CrcZ RNA acts as a decoy for Hfq"].

## Annotation decisions

- GO:0003723 RNA binding (IBA, IEA): ACCEPT, core MF.
- GO:0005829 cytosol (IBA): ACCEPT.
- GO:0043487 regulation of RNA stability (IMP PseudoCAP, IBA): ACCEPT; Hfq binding stabilises RsmY.
- GO:0045974 regulation of translation, ncRNA-mediated (IDA PseudoCAP, IBA): ACCEPT. In the CrcZ paper
  Hfq itself represses amiE translation and the ncRNA CrcZ titrates it; Hfq does the work of a
  regulation in which an ncRNA is the modulating component. The E. coli co-seed (Hfq-dependent sRNA
  regulation) is the canonical case.
- GO:0006417 regulation of translation (IDA): MODIFY to GO:0017148 negative regulation of translation
  (direct in vitro repression of amiE).
- GO:0043609 regulation of carbon utilization (IDA): KEEP_AS_NON_CORE; Hfq directly represses
  translation of catabolic mRNAs under CCR.
- GO:0009372 quorum sensing (IMP): MARK_AS_OVER_ANNOTATED; effect on rhlI is indirect via RsmY/RsmA, and
  Hfq is not a component of QS signalling.
- GO:0006355 regulation of DNA-templated transcription (InterPro2GO IEA): REMOVE; Hfq acts
  post-transcriptionally.

## PseudoCAP IBA-seed assessment

PTN002164223 has 20 leaves (19 taxa, local PAINT leaf GAF 2026-10-28): Hfq of proteobacteria and of
Firmicutes (B. subtilis, S. aureus, Listeria, B. anthracis, C. botulinum), Aquifex, Thermotoga and
Leptospira.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002164223 | GO:0043487 regulation of RNA stability | 1 (sole) | 20 (19 taxa) | GO:0043487, IMP, PMID:16468994 (PseudoCAP) | SOUND | Hfq binds RsmY and its loss destabilises RsmY; protecting a bound RNA from decay is Hfq's own chaperone activity, not a distant phenotype. Hfq-mediated sRNA protection and mRNA turnover are also established in E. coli. Caveat: in Firmicutes Hfq has weaker, often undetectable roles in sRNA regulation, so the term's transfer to those leaves is less certain, though the binding activity is conserved. |
| PTN002164223 | GO:0045974 regulation of translation, ncRNA-mediated | 2 | 20 (19 taxa) | GO:0045974, IDA, PMID:24945892 (PseudoCAP); co-seed E. coli Hfq P0A6X3 | SOUND | Hfq represses amiE translation directly and the ncRNA CrcZ modulates it by sequestering Hfq. Same Firmicutes caveat. |
