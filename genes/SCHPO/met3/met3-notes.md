# met3 (O74314, SPBC15D4.09c) review notes

## 2026-11-13 audit and promotion to COMPLETE (methionine_biosynthesis module)

Existing DRAFT review audited row by row; all 11 GOA rows were already present and reviewed.

### Evidence situation

- No S. pombe-specific biochemistry or genetics for met3 was found (EuropePMC search for "SPBC15D4.09c" or
  "cystathionine gamma-synthase" with pombe returned no met3 paper). UniProt PE level 3; FUNCTION by similarity.
- Negative crude-extract result: [PMID:6526818 "A crude extract of Schizosaccharomyces pombe cells catalyzed sulfhydrylation of both O-acetyl-L-serine and O-acetyl-L-homoserine with H2S, but did not synthesize cystathionine from O-acetyl-L-homoserine and L-cysteine."]
  Read as low expression/activity under those growth conditions; it does not test met3 directly. Recorded
  as a caveat on the IBA ACCEPT and as a suggested question.
- S. pombe lacks reverse trans-sulfuration: [PMID:11754480 "Schizosaccharomyces pombe, in contrast to Saccharomyces cerevisiae and Aspergillus nidulans, lacks cystathionine beta-synthase and cystathionine gamma-lyase, two enzymes in the pathway from methionine to cysteine."]

### Decisions changed in this audit

- GO:0019344 L-cysteine biosynthetic process (PomBase IC, with GO:0003962): kept as lateral MODIFY to
  GO:0071269 L-homocysteine biosynthetic process, now supported by PMID:11754480 (S. pombe cannot make
  cysteine via cystathionine at all), and recorded as a PomBase source defect (WRONG_TERM, PROBABLE). The
  same part_of edge is in GO-CAM 66a3e0bb00001342 (met3 activity part_of GO:0019344).
- Nucleus HDA (is_active_in): kept KEEP_AS_NON_CORE, added a SUSPECTED WRONG_QUALIFIER source defect
  (localisation screen supports located_in, not activity).
- Replaced UniProt CATALYTIC ACTIVITY quotes as support for ACCEPT rows with the family SIMILARITY line and
  the PLP-lysine feature; the reaction line is by similarity and names the bacterial O-succinyl ester.
- Added a SUSPECTED UniProt source defect on the FUNCTION comment (O-succinyl vs fungal O-acetyl), matching
  the STR2 review.
- Description rewritten to state that activity is inferred, not assayed, and that met17 direct
  sulfhydrylation is the main homocysteine route.

### Module notes

- PANTHER (UniProt DR): PTHR42699, subfamily PTHR42699:SF1 (CYSTATHIONINE GAMMA-SYNTHASE-RELATED).
  PAINT node PTN000928825 (taxon Eukaryota) carries GO:0003962 (seeds STR2, A. nidulans C8VHB0).
  Note: different PANTHER family from bacterial MetB (PTHR11808) and plant CGS1 (PTHR43379).
- Physiological co-substrate expected to be O-acetyl-L-homoserine (made by fungal homoserine O-acetyltransferase), not
  O-succinyl-L-homoserine; unmeasured.
- Protein is 610 aa (longer than bacterial MetB, 386 aa).
