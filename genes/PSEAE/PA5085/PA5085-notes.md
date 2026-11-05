# PA5085 (Q9HU98) notes

## Identity

- PA5085 is *dguR*, the LysR-type regulator of the divergent *dguR-dguABC* D-glutamate/D-glutamine
  utilization locus (Pseudomonas Genome Database: PA5084 *dguA*, PA5083 *dguB*, PA5082 *dguC*).
- Domains (UniProt Q9HU98): LysR HTH (PROSITE PS50931, residues 17-74, HTH motif 34-53) and LysR
  substrate-binding domain (Pfam PF03466). PANTHER PTHR30427.

## Literature

- [PMID:25082951 "The function of DguR as a transcriptional activator of the dguABC operon was demonstrated
  by promoter activity measurements in vivo and by mobility shift assays with purified His-tagged DguR in
  vitro."]
- [PMID:25082951 "binding of DguR to a highly conserved 19 bp sequence motif was further demonstrated"] —
  direct sequence-specific DNA binding by the purified protein.
- [PMID:25082951 "Although the DNA-binding activity of DguR did not require D-Glu, the presence of D-Glu,
  but not D-Gln, in the binding reaction was found to stabilize a preferred nucleoprotein complex."] —
  D-Glu is the co-inducer.
- [PMID:25082951 "Growth of the dguR and dguA mutants was abolished completely on D-Glu or retarded on
  D-Gln as the sole source of carbon and/or nitrogen."] — DguR is required for D-Glu catabolism, but as
  a regulator, not as a catalyst.
- Abstract only in the cache; the abstract is detailed enough to support the DNA-binding and activator
  claims.

## Annotation decisions

- GO:0043565 sequence-specific DNA binding (IDA PseudoCAP; IBA): ACCEPT.
- GO:0003700 DNA-binding transcription factor activity (IEA InterPro): ACCEPT; core MF.
- GO:0003677 DNA binding (IEA UniRule): MODIFY to GO:0043565.
- GO:0006355 regulation of DNA-templated transcription (IEA): MODIFY to GO:0045893 positive regulation
  of DNA-templated transcription (activator of dguABC).
- GO:0010628 positive regulation of gene expression (IBA, PTN001576694, seeded by E. coli LysR P03030):
  MODIFY to GO:0045893; correct direction, more specific term supported.
- GO:0006351 DNA-templated transcription (IEA UniRule): MARK_AS_OVER_ANNOTATED; DguR regulates
  transcription, it is not part of the transcription machinery.
- Not proposed as NEW: D-glutamate catabolic process. DguR is required for it (growth phenotype) but
  performs no catabolic step; DguA (PA5084) does. Per CLAUDE.md, necessity is not participation.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001576694 | GO:0043565 sequence-specific DNA binding | 1 (sole) | 11 (7 taxa) | GO:0043565, IDA, PMID:25082951 (PseudoCAP) | SOUND | EMSA with purified His-DguR, including binding to a conserved 19 bp operator motif, is direct evidence. Sequence-specific DNA binding via the LysR HTH is a property of essentially every LysR-family regulator, so the term is safe for the clade (the operator sequence itself is not propagated). |
