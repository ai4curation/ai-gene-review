# dak1 (SPAC22A12.11, UniProt O13902) notes

## Identity and naming trap
- Dihydroxyacetone kinase 1, 580 aa, DAK family (DhaK + DhaL domains), PANTHER PTHR28629:SF14 [UniProt:O13902].
- Itoh et al. 1999 cloned "dak1" encoding DHAK isoenzyme I from strain IFO 0354
  [PMID:10091325 "The gene dak1 encoding a dihydroxyacetone kinase (DHAK) isoenzyme I, one of two isoenzymes in the Schizosaccharomyces pombe IFO 0354 strain, was cloned and sequenced."]
  [PMID:10091325 "The dak1 gene comprises 1743 bp and encodes a protein of 62,245 Da."]. 1743 bp = 580 codons + stop, i.e. O13902.
- TRAP: Kimura et al. 1998 used "SpDAK1"/"SpDAK2" for two different 591-aa, 99.8%-identical genes from IFO 0354, of which only
  SpDAK1 is in 972h- [PMID:9804990 "The open reading frames of both genes encode 591 amino acids"]
  [PMID:9804990 "indicated the presence of SpDAK1 and the absence of SpDAK2 in a standard laboratory strain, S. pombe 972h-."].
  The 591-aa protein in 972 is PomBase dak2 (SPAC977.16c, O74215), which UniProt lists with synonym "dak1". So Kimura's
  "SpDAK1" = PomBase dak2, not PomBase dak1. A pairwise global alignment (BLOSUM62, Biopython, run during this review) of
  O13902 vs O74215 gives 257 identical positions (~44% over 580 aa): dak1 and dak2 are distinct paralogs.

## Activity
- Recombinant dak1 purified and characterized; UniProt records Km 0.01 mM for DHA, homodimer [UniProt:O13902 "KM=0.01 mM for dihydroxyacetone"].
- DHAK I and II purified from IFO 0354; both also act weakly on DL-glyceraldehyde and glycerol
  [PMID:16535475 "both of the enzymes had some affinity for glycerol and dl-glyceraldehyde in addition to dihydroxyacetone and glyceraldehyde"].
  PomBase maps this IDA to both dak1 and dak2.

## Physiology
- dak1 deletion strongly impairs growth on glycerol and DHA; dak1 is the major DHA kinase because it is more highly expressed
  [PMID:20396879 "The dak1 Delta strain showed a more severe reduction of growth on glycerol and DHA than the dak2 Delta strain"]
- Glucose repressed [PMID:20396879 "expression of the gld1 (+), dak1 (+), and dak2 (+) genes was repressed at a high concentration of glucose"].
- Note the contrasting older enzymology claim that DHAK II is kinetically more important [PMID:16535475 "DHAK II plays a more important role than DHAK I in dissimilation of glycerol via dihydroxyacetone."].

## Localization
- Cytosol (ORFeome HDA) and cytoplasm (HDA, PMID:10759889 Ding et al. 2000 GFP library). UniProt attributes the Ding 2000 GFP clone
  sequence to dak2 (O74215 residues 103-168), so the dak1 cytoplasm HDA from PMID:10759889 may belong to dak2; the
  term is right for dak1 anyway (ORFeome cytosol).

## Comparison with S. cerevisiae DAK1/DAK2 reviews
- Same core MF (GO:0004371), BP (GO:0019563) and location (cytosol). Difference: yeast reviews leave triokinase
  (GO:0050354) UNDECIDED; for S. pombe purified-enzyme data show activity on DL-glyceraldehyde, so kept as non-core.
- GO-CAM gomodel:6796b94c00004743: dak1 enables GO:0004371 in cytosol, part of GO:0019563 (agrees).
