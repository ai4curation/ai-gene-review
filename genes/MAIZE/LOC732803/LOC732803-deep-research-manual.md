# LOC732803 (Zea mays) — manual literature research

Deep-research API providers were not available for this session; this file records a
manual literature review from cached publications and PubMed searches.

## Identity

- UniProt K7TR93 (unreviewed, 479 aa), gene name LOC732803, NCBI GeneID 732803,
  EnsemblPlants Zm00001eb416990 (chromosome 10). NCBI Gene describes the locus as
  "orange pericarp 2" with aliases TSB2 and orp2, i.e. tryptophan synthase beta chain 2,
  chloroplastic. The Swiss-Prot entry for the same gene product is P43284 (TRPB2_MAIZE,
  an N-terminal fragment from the 1992 cDNA). The duplicate gene orp1/TSB1 is LOC732842
  (K7TTR0, chromosome 4; Swiss-Prot P43283).
- A second UniProt entry, A0A804RDH5 (464 aa), is the alternative transcript model
  Zm00001eb416990_P002 of the same gene; symbol-based fetching resolved to it first.

## Genetics: orange pericarp

- [PMID:1356534 "orange pericarp (orp) is a seedling lethal mutant of maize caused by
  mutations in the duplicate unlinked recessive loci orp1 and orp2."]
- [PMID:1356534 "Results from feeding studies and enzyme assays indicate that the orp
  mutant is defective in tryptophan synthase beta activity."]
- [PMID:1356534 "Together, the biochemical, genetic, and molecular data verify the identity
  of orp1 and orp2 as duplicate structural genes for the beta subunit of tryptophan
  synthase."]
- [PMID:1356534 "RNA analysis indicates that both genes are expressed in all tissues
  examined from normal plants."]
- The orp mutant was used to show tryptophan-independent IAA synthesis
  [PMID:17731524 "These results establish that IAA can be produced de novo without
  tryptophan as an intermediate."]. This bears on auxin biosynthesis, not on a TSB2
  function, and does not justify any auxin process annotation for TSB2.

## Biochemistry: the maize tryptophan synthase complex (PMID:18430213, full text)

- [PMID:18430213 "ZmTSB1 and ZmTSB2 are functionally redundant active TSB enzymes."]
- Recombinant ZmTSA forms an alpha2beta2 complex with ZmTSB1 (the orp1 product); TSB2 was
  not expressed recombinantly. [PMID:18430213 "These results are consistent with formation
  of a ZmTSA2ZmTSB12 heterotetramer."]
- In vivo: [PMID:18430213 "The Zmtsb1 Zmtsb2 (orp1 orp2) double mutant is devoid of
  β-activity and shows severe growth defects [15]."] and [PMID:18430213 "Here, the
  respective single mutants Zmtsb1 (orp1 +/orp1 orp2) and Zmtsb2 (orp1 orp2/+ orp2) were
  tested and each yielded β-activity in both the 90 kD and the 160 kD complex fractions
  (Figure 4D)."] In the Zmtsb1 line, the remaining beta activity, in both the beta2-dimer
  and the alpha2beta2-complex fractions, must come from TSB2.
- [PMID:18430213 "This indicates that ZmTSB1 and ZmTSB2 are functionally redundant and may
  both form active β-dimers as well as active αββα TS complexes."]
- [PMID:18430213 "However, based on Zmtsb1 mutant analysis (Figure 4) it is very likely that
  also ZmTSB2 is present in TS complexes in vivo."]
- [PMID:18430213 "We propose that, despite the availability of the highly active monomers
  BX1 and IGL, in maize tryptophan is predominantly synthesized through a tryptophan
  synthase complex containing ZmTSA and ZmTSB1 or ZmTSB2, respectively."]
- Note (own analysis, see LOC732803-bioinformatics/RESULTS.md): the peptide QALNVFR, which
  the authors assigned to ZmTSB1, also occurs as a tryptic peptide in K7TR93.

## Localization

- No direct localization assay of TSB2 has been reported. Swiss-Prot P43284 annotates a
  predicted chloroplast transit peptide (residues <1..45, ECO:0000255) and a chloroplast
  location by curator inference (ECO:0000305). The alpha partner ZmTSA is plastidic by GFP
  fusion [PMID:18430213 "In case of ZmTSA GFP fluorescence coincided with the chlorophyll
  autofluorescence of the chloroplasts (Figure 2A–C), demonstrating plastidic localization
  of ZmTSA."], and Arabidopsis TSB1 is plastidic [PMID:18430213 "AtTSA1 and AtTSB1 are both
  localized in the plastid [11,13,14]."].

## Not this gene

- PMID:20701934 characterises "ZmTSBtype2", a distantly related type-2 TSB. Despite the
  name, that is not TSB2/orp2; LOC732803 is a type-1 (complex-forming) TSB
  (HAMAP MF_00133, TIGR00263, PIRSF001413).
- PMID:15834137 compares the genomic Orp1/Orp2 regions (synteny), with no functional data.
- Other hits for the PubMed query (carotenoids, fiber gums, pericarp pigmentation) are
  irrelevant.
