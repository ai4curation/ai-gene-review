# ubiA (PP_5318, Q88C65) - Pseudomonas putida KT2440 - curation notes

## 2026-11-11 audit (ubiquinone_biosynthesis module)

No Perplexity/Falcon/OpenAI deep research available (no provider keys); the existing
OpenScientist report was read. Evidence: reviewed UniProt entry (HAMAP MF_01635) and E. coli
UbiA literature. No experiment on the KT2440 protein.

- E. coli genetics: [PMID:4552989 "The ubiA(-) mutants were found to lack
  4-hydroxybenozate octaprenyltransferase activity"] and [PMID:4552989 "Both the side-chain
  precursor and 4-hydroxybenzoate octaprenyltransferase were shown to be membrane-bound."]
- Donor flexibility: [PMID:8155731 "Geranyldiphosphate (GPP), all-trans-farnesyldiphosphate
  (FPP) and all-trans-solanesyldiphosphate (SPP) are accepted as side chain precursors."]
  Solanesyl = C45, the ubiquinone-9 chain of P. putida.
- UniProt FUNCTION text says "ubiquinone-8 (UQ-8)" and "3-octaprenyl-4-hydroxybenzoate":
  HAMAP rule wording from E. coli; KT2440 makes UQ-9. Not a functional error; GO:0008412 is
  chain-length neutral. Recorded here rather than as a source defect.
- PAINT (PTHR11048): PTN001666047 GO:0008412 (Gammaproteobacteria, seed E. coli P0AGK1);
  PTN000114231 GO:0016765 + GO:0006744; PTN000114159 GO:0005886 + GO:0016740. No IBA rows
  for KT2440 in GOA.
- Decisions: GO:0008412, GO:0006744, GO:0005886 ACCEPT; generic MF rows (GO:0004659,
  GO:0016740, GO:0016765) MODIFY to GO:0008412; GO:0016020 MODIFY to GO:0005886.

Module agreement: matches `hydroxybenzoate_polyprenyltransferase_activity` (GO:0008412,
plasma membrane).
