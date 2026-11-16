# OPN1LW (P04000) review notes

## Identity

- UniProt P04000 OPSR_HUMAN, long-wave-sensitive (red, L) cone opsin, 364 aa, HGNC:9936.
  The X-linked array holds one OPN1LW followed by one or more OPN1MW copies; UniProt keeps
  the extra M copies (OPN1MW2, OPN1MW3) as separate entries. Every row reviewed here is on
  P04000; no evidence was merged from the M-opsin entries. L and M differ at 15 of 364
  residues [PMID:8185948 "The human red and green color vision pigments are identical at all but 15 of their 364 amino acids"].

## Function and what was assayed

- Transducin activation: human red cone opsin expressed in COS-1 cells, assayed with rod
  transducin purified from bovine retina [PMID:21314100 "Human red cone opsin was transiently expressed in COS-1 cells as described previously"].
  11-cis-retinal is the chromophore and an inverse agonist [PMID:21314100 "11-cis-Retinal (1) both serves as the chromophore of the opsins and as an inverse agonist that holds the visual pigment protein in an inactive conformation"].
- Pigment formation with 11-cis-retinal, lambda max 560 nm, plasma membrane in COS cells
  [PMID:9860863 "wild-type red opsin undergoes N-linked glycosylation, forms a light-sensitive pigment with absorption maximum at 560 nm upon reconstitution with 11-cis-retinal, and is transported to the plasma membrane"].
- Native human cones: microspectrophotometry of cone outer segments, red cones 558 nm
  [PMID:6140680 "red cones, 558.4 +/- 5.2 nm"]. This is the only direct human tissue evidence
  for the outer-segment location in the cited set.
- Spectral tuning (S116Y, S180A, ... red to green) mapped by mutagenesis in cultured cells
  [PMID:8185948].
- Organism level: loss of all L/M genes (LCR deletion, C203R) gives blue cone monochromacy
  [PMID:8213841 "One inactivating mutation, Cys203-to-Arg, was found in 15 probands"].

## Decisions in brief

- MF: GO:0008020 G protein-coupled photoreceptor activity (definition: combining with light
  and activating a heterotrimeric G protein by GDP/GTP exchange). GO:0009881 photoreceptor
  activity and GO:0004930 GPCR activity are its ancestors: MODIFY to GO:0008020. Added
  GO:0005502 11-cis retinal binding as NEW, matching RHO.
- BP: GO:0141190 transducin-mediated opsin signaling pathway (carried, IDA). Ancestors
  (GPCR signalling, phototransduction, cellular response to light, signal transduction)
  MODIFY to it, as in the RHO review. Visual perception and absorption of visible light ACCEPT.
- CC: GO:0120201 cone photoreceptor disc membrane. Cone discs are evaginations contiguous
  with the plasma membrane (GO:0120201 is_a GO:0005886), so plasma membrane, membrane and
  photoreceptor disc membrane rows MODIFY to it. This differs from RHO (rod discs are sealed)
  for a principled reason.
- Positive regulation of cytokinesis (HeLa siRNA screen, PMID:22888021): MARK_AS_OVER_ANNOTATED.
- PMID:7643192 (rod neurite sprouting in RP) does not concern OPN1LW; the visual perception
  TAS row it backs is accepted on other evidence.
- Agrees with GO-CAM gomodel:68fac5ed00003872 (GO:0008020, GO:0141190, GO:0016038,
  GO:0120201) and the visual_phototransduction module annoton (GO:0008020).
