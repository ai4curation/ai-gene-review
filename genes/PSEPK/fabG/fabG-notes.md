# fabG curation notes

- UniProt accession Q88LL6 identifies the NADPH-dependent reduction of
  beta-ketoacyl-ACP in the fatty-acid elongation cycle
  [file:PSEPK/fabG/fabG-uniprot.txt,
  "Catalyzes the NADPH-dependent reduction of beta-ketoacyl-ACP"].
- The exact FabG molecular function, fatty-acid elongation, and fatty-acid
  biosynthesis annotations are accepted.
- Generic `NAD binding` is replaced by `NADP binding` because the recorded
  reaction uses NADPH/NADP+.

## 2026-11-11

Re-checked all four GOA rows while promoting this review to COMPLETE (fabG is
the reference protein of `interpro/panther/PTHR42879`, needed by the
`ketone_body_oxidation` module through HbdH, which sits in the same PANTHER
subfamily SF2). Added the FabG-specific NCBIfam TIGR01830 match as support for
GO:0004316; the UniProt FUNCTION and catalytic-activity lines rest on RuleBase
RU366074 (with an ARBA co-source for FUNCTION). Actions unchanged.
