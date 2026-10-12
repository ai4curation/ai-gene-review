# BNA6 (YFR047C, QPT1) notes

## Identity and activity
- Quinolinate phosphoribosyltransferase (QPRTase, EC 2.4.2.19): quinolinate + PRPP -> nicotinate D-ribonucleotide (NaMN) + CO2 + PPi [UniProt:P43619 "Reaction=nicotinate beta-D-ribonucleotide + CO2 + diphosphate ="].
- Confirmed by Panozzo et al.: [PMID:12062417 "for BNA5 (YLR231c) and BNA6 (YFR047c) confirmed that they encode kynureninase and quinolinate phosphoribosyl transferase respectively"]. Kynurenine-pathway mutants are synthetically lethal with npt1 [PMID:12062417 "deletion of genes encoding kynurenine pathway enzymes are co-lethal with the Deltanpt1"].
- Hexamer of 3 homodimers (structure PMID:18321072, cited by UniProt) [UniProt:P43619].
- BNA6 is the convergence point where the de novo (tryptophan/kynurenine) route enters NaMN; it does not degrade tryptophan itself.

## Location
- GFP: cytoplasm and nucleus [UniProt:P43619, PMID:14562095].

## Annotation observations
- YeastPathways places Bna6 in "L-tryptophan degradation III (eukaryotic)" -> RCA GO:0006569. Quinolinate is formed non-enzymatically from ACMS after tryptophan breakdown; QPRT converts it into a nucleotide (NAD biosynthesis). Tryptophan catabolism is superpathway inflation.
- GO:0034354 obsolete; replaced_by GO:0034628 is defined from L-aspartate -> not applicable; use GO:0009435.
- IBA GO:0034213 quinolinate catabolic process: formally true (consumes quinolinate) but framing is from human QPRT clearance of neurotoxic quinolinate; non-core.
