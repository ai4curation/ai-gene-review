# BIRC2 manual curation notes

## 2026-11-27 PTHR10044 cIAP review

- Reviewed BIRC2/cIAP1 as the human PTHR10044:SF79 member, alongside BIRC3/cIAP2
  and the existing XIAP, BIRC7, and BIRC8 reviews. `just deep-research human BIRC2
  --provider perplexity-lite` failed because the requested provider was unavailable;
  no provider-branded deep-research file was fabricated.
- BIRC2 is centered on RING E3 ubiquitin-protein ligase activity. The direct evidence
  supports cIAP1 ubiquitination of TRAF2 downstream of TNFR2 (PMID:11907583) and broad
  cIAP1/cIAP2 ubiquitination of RIPK1, RIPK2, RIPK3, and RIPK4 (PMID:21931591).
- The TNF receptor rows are consistent with Reactome and ComplexPortal assemblies in
  which cIAP1/2 are recruited to the cytosolic face of activated TNF receptor signaling
  complexes by TRAF proteins, ubiquitinate RIPK1 or TRAF3, and thereby balance canonical
  NF-kappaB, non-canonical NF-kappaB, apoptosis, and necroptosis.
- The direct nuclear and cell-cycle rows were kept as BIRC2-specific non-core biology.
  PMID:15665297 localizes cIAP1 to the nucleus and midbody in mitotic cells; PMID:21653699
  supports cIAP1 cooperation with E2F1 at cyclin promoters.
- The PAINT caspase-inhibitor row at PTN000953271 is not retained for cIAP1. The cIAP
  branch has BIR domains and can bind SMAC/CASP9 peptides, but the direct human rows
  reviewed here establish E3 ligase activity toward RIPK, TRAF, or BCL10-family signaling
  substrates rather than an XIAP-like cysteine-type endopeptidase inhibitor activity.
- Most `GO:0005515 protein binding` rows are removed under the project bare-binding
  policy. The review keeps one existing annotation per GOA line, including rows that
  differ only by `WITH/FROM`.
- The Ensembl Compara transfers from rat Q6P6S1 for response to hypoxia, XY body,
  response to ethanol, response to cAMP, and response to bleomycin were treated as
  rodent orthology side annotations rather than cIAP1 core functions; the human
  review found no direct BIRC2 evidence for those endpoint terms.
- The Ensembl Compara GO:0044877 protein-containing complex binding row from rat
  Q6P6S1 is an uninformative transfer; the accepted BIRC2 complex biology is
  represented by TNF receptor complex and RIP/TRAF ubiquitin-ligase rows.
