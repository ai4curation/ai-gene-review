# benA (P07769, Acinetobacter baylyi ADP1) notes

## Provenance of this review

- Created as a cross-genus representative member of
  `modules/benzoate_upper_pathway.yaml`, so the module is grounded beyond
  Pseudomonas putida KT2440.
- Deep research: `just deep-research-falcon ACIAD benA` was attempted and failed with
  "Failed to authenticate" (provider credentials rejected), so there is no
  `-deep-research-*.md` file and none was written by hand. The review rests on
  the UniProt entry and the cached publications: PMID:1885518, PMID:2824437, PMID:12949084.
- Every quotation is verbatim from those cached sources; several are
  abstract-only, flagged with `full_text_unavailable` on the reference.

## This gene

- Reviewed Swiss-Prot entry. The catalytic centres are curated as features: four
  `FT BINDING` positions for the Rieske `[2Fe-2S]` cluster (95, 97, 115, 118,
  PROSITE-ProRule) and three for the mononuclear Fe cation (224, 229, 376,
  ECO:0000250). That is why both cofactor annotations are ACCEPTed rather than
  argued from family membership alone.
- The ADP1 oxygenase was purified and reconstituted with BenC, and prefers
  benzoate over substituted benzoates [PMID:12949084 "Reconstituted BADO ADP1
  utilized four of the seven tested benzoates in the following order of apparent
  specificity: benzoate > 3-methylbenzoate > 3-chlorobenzoate >
  2-methylbenzoate."]. Subunit-swap hybrids place the principal
  substrate-specificity determinants in this alpha subunit.
- GO:0043639 is added as NEW with IDA: BenA itself catalyses a step of the
  pathway, and the conversion was assayed directly in the heterologous host.
