# PP_3199 curation notes

- UniProt Q88I03 identifies an unreviewed monooxygenase with FAD-binding
  architecture but gives no substrate or pathway assignment
  [file:PSEPK/PP_3199/PP_3199-uniprot.txt "SubName: Full=Monooxygenase"].
- Hsero_1007/FdeE is experimentally implicated in the first naringenin
  monooxygenation step [PMID:27059806 "naringenin remained unaltered, suggesting
  that the FdeE protein is involved in the initial step of naringenin
  degradation."]. Its purified enzyme accepts several flavonoid classes
  [PMID:39107441 "the fdeE, the FMO from Herbaspirillum seropedicae SmR1 that is
  a part of the naringenin degradation pathway and is active towards a wide
  range of flavonoids-flavanones, flavones, isoflavones, and flavonols."].
- A committed global alignment reproduces 40.4% identity between Q88I03 and
  D8J0W9 [file:PSEPK/PP_3199/PP_3199-bioinformatics/RESULTS.md "Pairwise identity
  over aligned residue pairs: 40.4%"]. This supports ISS but is lower than the
  report's unreproduced 41.4% figure.
- The report also overstates exact motif conservation: only its cited `GADG`
  motif is identical in both sequences. The target-specific substrate range,
  C-8 regioselectivity, cofactor preference, and localization therefore remain
  predictions rather than direct annotations.
- GO:0016709 captures the supported monooxygenase reaction class. GO:0009812 is
  used for the predicted pathway role because no flavonoid-catabolic child is
  present in the local ontology. No cellular-component assertion is made.
