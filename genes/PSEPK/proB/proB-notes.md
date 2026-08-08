# proB (Q88Q07) — Pseudomonas putida KT2440 glutamate 5-kinase

## Summary

proB (PP_0691) encodes the reviewed cytoplasmic glutamate 5-kinase (EC 2.7.2.11)
that catalyzes the first committed step of L-proline biosynthesis: ATP-dependent
phosphorylation of L-glutamate to L-glutamyl 5-phosphate. The acyl-phosphate
product is subsequently reduced by ProA to L-glutamate 5-semialdehyde, which
cyclizes non-enzymatically to P5C (glutamate-to-P5C branch).

- Reaction: L-glutamate + ATP = L-glutamyl 5-phosphate + ADP
  [file:PSEPK/proB/proB-uniprot.txt "Reaction=L-glutamate + ATP = L-glutamyl 5-phosphate + ADP"]
- Pathway: Amino-acid biosynthesis; L-proline biosynthesis
  [file:PSEPK/proB/proB-uniprot.txt "PATHWAY: Amino-acid biosynthesis; L-proline biosynthesis"]
- Localization: Cytoplasm
  [file:PSEPK/proB/proB-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm"]

## PUA domain and the RNA-binding over-annotation

ProB carries a C-terminal PUA domain (UniProt FT DOMAIN 280..358; InterPro
IPR002478 / IPR036974; Pfam PF01472; HAMAP-Rule MF_00456). In glutamate
5-kinase this PUA domain is an allosteric proline-feedback regulatory module,
not a nucleic-acid-binding element.

The IEA annotation GO:0003723 (RNA binding; DR GO;GO:0003723; F:RNA binding;
IEA:InterPro; GO_REF:0000002) is propagated purely from the PUA domain signature.
PUA -> RNA-binding is a well-known over-propagated InterPro inference for
metabolic ProB proteins, and there is no evidence that ProB binds RNA in vivo.
This annotation is therefore marked MARK_AS_OVER_ANNOTATED in the review (it is
not merely non-core: KEEP_AS_NON_CORE would require positive supporting
evidence, which is absent).
