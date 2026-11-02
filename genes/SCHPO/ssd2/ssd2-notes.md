# ssd2 (SPAC139.05, UniProt Q9UTM8) notes

## Identity
- UniProt: "Succinate-semialdehyde dehydrogenase [NADP(+)] 2", EC 1.2.1.16 by similarity to S. cerevisiae UGA2 (P38067) [UniProt:Q9UTM8 "EC=1.2.1.16 {ECO:0000250|UniProtKB:P38067}"].
- Paralog: ssd1 (SPAC1002.12c, Q9US47). Naming trap: S. cerevisiae SSD1 is an unrelated RNA-binding protein; the S. cerevisiae SSADH is UGA2 (UGA5/YBR006W).
- PANTHER PTHR43353:SF12 "SUCCINATE-SEMIALDEHYDE DEHYDROGENASE C139.05 [NADP(+)]-RELATED"; InterPro IPR010102 Succ_semiAld_DH [UniProt:Q9UTM8].

## Function (all by similarity; no S. pombe biochemistry found)
- UniProt function: "Catalyzes the oxidation of succinate semialdehyde to succinate. Can utilize both NAD(+) or NADP(+) as a coenzyme." (ECO:0000250 from P38067) [UniProt:Q9UTM8].
- The S. cerevisiae ortholog Uga2 is NAD(P)+-dependent with NAD+ preferred (see genes/yeast/UGA2 review, PMID:25092794). Cofactor preference of ssd2 itself is untested; GO:0009013 (NAD(P)+) is the cofactor-neutral term and is used as the core MF, consistent with the UGA2 review.
- Pathway: GABA degradation (UniPathway 4-aminobutanoate degradation). S. pombe lacks glutamate decarboxylase, so ssd2 participates in GABA catabolism (GO:0009450) rather than in a complete GABA shunt.

## Location
- Experimental (HTP): cytoplasm/cytosol, ORFeome YFP screen [PMID:16823372 "we determined the localization of 4,431 proteins"; UniProt "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16823372}."].
- PomBase IC (GO_REF:0000111, from GO:0004777) and ARBA IEA assign mitochondrial matrix; the PomBase GO-CAM 696022cd00001857 places ssd2 in the mitochondrial matrix. The N-terminus (MAPQFKRPELFGFDKSHAQ...) does not look like a classical cleavable presequence (by inspection only, no predictor run), and the budding-yeast ortholog Uga2 is cytosolic. Conflict unresolved -> both mitochondrial matrix annotations (IC and ARBA IEA) left UNDECIDED; cytosol (HDA) used as core location.

## GO-CAM
- 696022cd00001857 (GABA catabolic process): ssd2 enables GO:0004777 (NAD+), occurs_in GO:0005759 mitochondrial matrix (IC), part_of GO:0009450. Evidence for MF is IBA + Rhea IEA; NAD+-specific typing is not supported by S. pombe data.
