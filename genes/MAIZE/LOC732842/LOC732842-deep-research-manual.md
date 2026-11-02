# LOC732842 (Zea mays) — manual literature research

Deep-research API providers were not available for this session; this file records a manual
literature review from cached publications and PubMed searches.

## Identity

- UniProt K7TTR0 (unreviewed, 474 aa), gene name LOC732842, NCBI GeneID 732842, EnsemblPlants
  Zm00001eb173100 (chromosome 4). NCBI Gene (esummary, queried in this session) names the locus
  "orange pericarp 1" with aliases ZEAMMB73_Zm00001d049610, GRMZM2G169593, TSB1 and orp1, i.e.
  tryptophan synthase beta chain 1. The Swiss-Prot entry for the same product is P43283
  (TRPB1_MAIZE; N-terminal fragment from the 1992 cDNA), 99.7% identical to K7TTR0
  (bioinformatics RESULTS.md). The duplicate gene orp2/TSB2 is LOC732803 (K7TR93, chromosome 10).

## Genetics: orange pericarp

- [PMID:1356534 "orange pericarp (orp) is a seedling lethal mutant of maize caused by mutations
  in the duplicate unlinked recessive loci orp1 and orp2."]
- [PMID:1356534 "Results from feeding studies and enzyme assays indicate that the orp mutant is
  defective in tryptophan synthase beta activity."]
- [PMID:1356534 "Together, the biochemical, genetic, and molecular data verify the identity of
  orp1 and orp2 as duplicate structural genes for the beta subunit of tryptophan synthase."]
- [PMID:1356534 "RNA analysis indicates that both genes are expressed in all tissues examined
  from normal plants."]
- The orp mutant was later used to argue for tryptophan-independent IAA synthesis
  (PMID:17731524, abstract only, not cached); this concerns auxin biosynthesis, not a function
  of TSB1, and supports no annotation here.

## Biochemistry: Kriechbaumer et al. 2008 (PMID:18430213, full text)

- Nomenclature: [PMID:18430213 "the double mutant orange pericarp (orp1 = Zmtsb1, orp2 =
  Zmtsb2) is tryptophan auxotroph"] and [PMID:18430213 "ZmTSB1 and ZmTSB2 are functionally
  redundant active TSB enzymes."]
- Recombinant ZmTSB1 was expressed without its plastid-targeting sequence
  [PMID:18430213 "for ZmTSB1 expression an NdeI/BamHI-fragment of the coding sequence
  excluding plastid-targeting sequences was amplified by PCR."]
- Beta-reaction of TSB1 alone (Table 1): indole Km 24 µM, kcat 0.29 s-1; with ZmTSA, Km 28 µM,
  kcat 0.44 s-1 [PMID:18430213 "In contrast, no significant activation of the maize β-subunit by
  ZmTSA was observed (Table 1)."]
- Complex: [PMID:18430213 "ZmTSA and ZmTSB1 formed a complex of approximately 160 kD (Figure 3A)
  that according to SDS-PAGE analysis (data not shown) contained both proteins in a 1:1
  stoichiometry."] [PMID:18430213 "These results are consistent with formation of a
  ZmTSA2ZmTSB12 heterotetramer."] TSB1 increases ZmTSA catalytic efficiency
  [PMID:18430213 "Heteromerisation with ZmTSB1 resulted in a 32-fold increase of the catalytic
  efficiency of ZmTSA."] The reconstituted complex performs the overall alpha-beta reaction
  (Table 1, IGP Km 47 µM, kcat 0.45 s-1).
- Alone, TSB1 forms homodimers [PMID:18430213 "ZmTSB1 apparently formed dimers of approximately
  90 kD (Figure 3B,C)."] and does not bind the other TSA homologs
  [PMID:18430213 "No interaction of ZmTSB1 with ZmTSAlike, BX1, or IGL was detectable."]
- In vivo: a 160 kD complex with alpha and beta activity was found in leaf extracts, and
  [PMID:18430213 "For ZmTSB1 the specific peptide QALNVFR was identified."]; [PMID:18430213 "In
  summary, ZmTSA and ZmTSB1 were identified by LC-ESI-ToF-MSas constituents of TS complexes."]
  Note: our own sequence comparison finds QALNVFR in TSB2 (K7TR93) too (RESULTS.md), so the
  peptide does not discriminate the paralogs; but the tsb2 single-mutant extracts (TSB1 only)
  still had beta activity in both the 90 kD and 160 kD fractions [PMID:18430213 "Here, the
  respective single mutants Zmtsb1 (orp1 +/orp1 orp2) and Zmtsb2 (orp1 orp2/+ orp2) were
  tested and each yielded β-activity in both the 90 kD and the 160 kD complex fractions
  (Figure 4D)."]
- Possible role of free TSB dimers: [PMID:18430213 "In addition, TSB dimers that have been
  observed in leaf extracts (Figure 4) and in vitro (Figure 3), which possibly function in
  salvage of indole by its conversion to tryptophan."] (speculative).
- Location: no direct localization of TSB1 was done; the alpha partner is plastid by GFP
  [PMID:18430213 "In case of ZmTSA GFP fluorescence coincided with the chlorophyll
  autofluorescence of the chloroplasts (Figure 2A–C), demonstrating plastidic localization of
  ZmTSA."] and plant aromatic amino acid synthesis is plastidic [PMID:18430213 "Based on import
  studies, subcellular fractionation, and target sequence prediction, it is suggested that in
  plants the biosynthesis of aromatic amino acids is predominantly localized in plastids (for
  review, see [29])."]

## Type-2 TSB (not this gene)

- [PMID:20701934 "In microorganisms two subfamilies of TSBs (here designated as type 1 and type
  2) are known, which are only distantly related."] The maize "TSBtype2" in that paper is a
  different gene; K7TTR0 is type 1 (HAMAP MF_00133, NCBIfam TIGR00263 trpB).
