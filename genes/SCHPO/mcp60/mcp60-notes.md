# mcp60 review notes

## Manual deep research

Perplexity deep research failed in this runtime because the wrapper reported `Provider 'perplexity' not available`; the PomBase/MOD description recipe skipped `SCHPO`, which has no configured MOD provider. I kept the review serial and used this manual note together with the seeded GOA rows, UniProt, cached publication abstracts and full texts, PubMed lookup of the original cloning paper, and the GO-CAM source.

## Function synthesis

S. pombe mcp60/hsp60 encodes the mitochondrial Hsp60/Cpn60 chaperonin, a conserved ATP-dependent protein-folding chaperone imported as an N-terminally targeted precursor and matured in the matrix. Yoshida et al. isolated the fission-yeast gene, found that the inferred 582-aa protein is similar to mitochondrial Hsp60 proteins and bacterial GroEL, and showed that mcp60 is essential for viability [PMID:8566770 "mcp60 is essential for cell viability at all temperatures"]. UniProt likewise places the protein in the HSP60 chaperonin family and annotates a predicted mitochondrial transit peptide.

The direct S. pombe molecular-function evidence is the Mtf1 paper. Sun et al. reported that "Mtf1 binds to Hsp60 in vivo and in vitro" and proposed that Hsp60 folds mitochondrial Mtf1 into a functional transcription factor [PMID:23035257 "Mtf1 binds to Hsp60 in vivo and in vitro"]. This supports the existing PomBase `GO:0044183 protein folding chaperone` row and the more specific InterPro2GO `GO:0140662 ATP-dependent protein folding chaperone` row.

The direct S. pombe localization evidence is broader than the core matrix function. Matsuyama et al. localized the ORF product to mitochondria at proteome scale [PMID:16823372 "we determined the localization of 4,431 proteins"]. Di et al. used Hsp60 in mitochondrial import or fractionation experiments around Ptc4 and oxidative stress; their discussion notes that "H 2 O 2 mildly inhibits cleavage of the Hsp60 MTS" [PMID:22139357], which confirms mitochondrial import and MTS processing but does not make mature Hsp60 an inner-membrane or intermembrane-space resident. The Chen et al. spliceosome purification detected Mcp60/Hsp60 in a mass-spectrometry table [PMID:24442611], but its established biology is mitochondrial and the cached full text provides no mechanistic spliceosomal role.

## GO-CAM context

GO-CAM 69729a3800007453 uses mcp60 as an ATP-dependent protein folding chaperone that occurs in the mitochondrial matrix and is part of protein import into the mitochondrial matrix. This agrees with the core Hsp60 activity if `part_of GO:0030150` is interpreted as folding matrix proteins after TIM23/PAM-dependent translocation rather than as direct participation in the translocation channel or motor.
