# sta-2 (C. elegans) notes

## Literature review integration (2026-10-04)

Added two reviews (full text cached) to the review YAML:

- Taffoni & Pujol 2015 (PMID:26716073), review of epidermal innate immunity:
  - STA-2 and ELT-3 are needed for nlp AMP transcription [PMID:26716073 "Both the STAT family protein STA-2 and the GATA transcription factor ELT-3 are required for the transcription of nlps"].
    Added to GO:0006357, GO:0010628 and the core function.
  - SNF-12 binds STA-2 in endocytic vesicles [PMID:26716073 "SNF-12 physically interacts with the transcription factor STA-2 and they have been found to colocalise in dyn-1-dependent-endocytic vesicles"]. Added to GO:0030139.
  - STA-2 is nuclear and hemidesmosome-associated [PMID:26716073 "STA-2 was found in the nucleus but also associated with hemidesmosomes (CeHDs)"]
    and binds MUP-4 [PMID:26716073 "Zhang et al. showed that STA-2 physically interacts with one apical component of CeHDs, MUP-4 a transmembrane multidomain protein."].
    Added to GO:0030056, GO:0098733 and the nucleus IDA.
  - The severe-injury response is p38-independent but needs STA-2 [PMID:26716073 "upregulation of nlp-29 and cnc-2 could occur in a p38 independent, but STA-2 dependent way"]. Added to GO:0009611.
  - Activation is non-canonical and not fully understood [PMID:26716073 "It is still not clear how p38 MAPK-dependent STA-2 activation and trafficking are regulated in C. elegans epidermis."]. Added to the GO:0007259 REMOVE.
- Wang & Levy 2012 (PMID:24058748). Its F58E6.1 is sta-2 (UniProt ORFNames F58E6.1).
  - STA-2 is a divergent paralog from a nematode-specific duplication [PMID:24058748 "Therefore, F58E6.1 is very different from STA-1 and is unlikely to be a bona fide member of the STAT family."]. Added to the GO:0007259 REMOVE.
  - Caveat for the DNA-binding terms: only a weak DNA-binding domain match [PMID:24058748 "F58E6.1 might contain two protein domains, SH2 (E-value, 1.3e-14) and DNA binding (E-value 4.1e-05)"],
    and no STAT-motif binding in an unpublished (data not shown) EMSA [PMID:24058748 "failed to show any DNA binding activities using a STAT consensus DNA sequence motif"].
    Added as a caveat to the GO:0000978 reason. The action stays ACCEPT, but GO:0000978 may be worth revisiting (see suggested_questions on STA-2 binding sites).
- Liongue & Ward 2013 (PMID:24058787) was not added. It makes no STA-2-specific point beyond what the sta-1 review already cites.
- Also added the missing propagation_review (PTN000927860, LINEAGE_OR_TAXON_MISMATCH) to the GO:0007259 IBA REMOVE.
- No actions changed.

Cross-gene briefing for GO editors and PAINT curators: https://claude.ai/artifact/4MLfbbbWWnLchDvspwdPuM
