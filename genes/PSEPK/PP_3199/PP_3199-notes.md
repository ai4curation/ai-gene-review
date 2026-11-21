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
- A committed global alignment gives 40.4% identity between Q88I03 and D8J0W9
  [file:PSEPK/PP_3199/PP_3199-bioinformatics/RESULTS.md "Pairwise identity over
  aligned residue pairs: 40.4%"]. MMseqs searches against both complete
  proteomes recover the pair as reciprocal best hits
  [file:PSEPK/PP_3199/PP_3199-bioinformatics/RESULTS.md "Reciprocal best-hit
  relationship: true"], substantially strengthening the ISS assignment.
- The report also overstates exact motif conservation: only its cited `GADG`
  motif is identical in both sequences. The target-specific substrate range,
  C-8 regioselectivity, cofactor preference, and localization therefore remain
  predictions rather than direct annotations.
- GO:0016709 captures the supported monooxygenase reaction class. GO:0009812 is
  used for the predicted pathway role because no flavonoid-catabolic child is
  present in the local ontology. No cellular-component assertion is made.

## 2026-11-06 comparative audit

Current KEGG K26180 bulk, PP_3199 entry and gene-to-KO queries no longer carry the historical KO assignment (source endpoints and dated results in `analysis/module_audits/bacterial_flavonoid_degradation/taxonomy-snapshot.json`). This is not a negative functional assay. The committed reciprocal-best-hit comparison and FAD-monooxygenase architecture still support the qualified FdeE inference; exact substrate and native flux remain untested. The earlier GO:0009812 note above is historical: the current review carries the more specific GO:0046275 flavonoid catabolic process proposal. No raw source or annotation payload was changed.
