# LCT notes

The review was written from the cached publications and the UniProt record. A falcon
deep-research report (`LCT-deep-research-falcon.md`) arrived afterwards; it agrees that
lactose digestion is the established physiological function and that the in-vivo
importance of the phlorizin/glycosylceramidase site is less securely defined, which is
consistent with leaving the glycosylceramidase annotations UNDECIDED / over-annotated.

## Function

- Lactase-phlorizin hydrolase (LPH) is a brush-border beta-glycosidase with two catalytic
  sites in one mature polypeptide [PMID:9762914 "Brush border lactase-phlorizin hydrolase
  carries two catalytic sites."; "In the human enzyme lactase comprises Glu-1749, phlorizin
  hydrolase Glu-1273."].
- Domain structure: signal peptide, large pro region absent from mature LPH, mature enzyme
  with both activities, C-terminal membrane anchor, Nout-Cin topology [PMID:2460343 "the
  mature LPH, which contains both the lactase and phlorizin hydrolase activities in a single
  polypeptide chain"; "the protein has an Nout-Cin orientation"].
- Substrate range of purified human jejunal lactase [PMID:3929764 "Lactase hydrolyzes,
  besides lactose, cellobiose and the synthetic substrates"; "but it does not hydrolyze
  glucocerebroside"]. This negative result is why the ortholog-based (rabbit Q02401)
  glycosylceramidase annotations were not accepted.
- Flavonoid glucoside deglycosylation [PMID:12594539 "The absorption of dietary flavonoid
  glycosides in humans involves a critical deglycosylation step that is mediated by
  epithelial beta-glucosidases"]. LPH releases quercetin from quercetin glucosides; this is
  not quercetin catabolism, hence MODIFY of GO:1901733.
- Dimerisation in the ER is needed for transport [PMID:9593732 "dimerization and transport
  of pro-LPH implicate a stretch of 87 amino acids in the ectodomain"].

## Disease

- Congenital lactase deficiency: coding mutations inactivate the enzyme [PMID:16400612 "the
  severe infancy form represents the outcome of mutations affecting the structure of the
  protein inactivating the enzyme"].
- Adult-type hypolactasia / lactase persistence is regulatory: the C/T-13910 variant sits in
  MCM6 intron 13 and acts as a cis enhancer of the LCT promoter (see dismech
  `Adult-Type_Hypolactasia`). This affects LCT expression, not LPH activity per molecule, so
  it does not alter the GO function annotations here.

## Modules

No ai-gene-review module covers intestinal disaccharide digestion. LCT supplies galactose
to the Leloir pathway (`modules/galactose_leloir_pathway.yaml`) but is upstream of that
module's boundary, not a part of it.
