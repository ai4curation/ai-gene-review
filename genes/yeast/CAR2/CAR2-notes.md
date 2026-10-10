# CAR2 (YLR438W, P07991) notes

Evidence journal (no paid deep research run; built from UniProt and cached publications).

- Ornithine aminotransferase (OTAse), EC 2.6.1.13, class-III PLP-dependent aminotransferase; transaminates L-ornithine with 2-oxoglutarate to L-glutamate 5-semialdehyde + L-glutamate, the second step of arginine degradation [UniProt:P07991].
- Gene identity: "The cargB or CAR2 gene, coding for ornithine aminotransferase, was isolated by functional complementation of a cargB- mutation in Saccharomyces cerevisiae" [PMID:3036506].
- Regulation: inducible; "The cargB transcript was not detected in the wild-type strain grown under non-induced conditions"; Ty1 insertions upstream give constitutive, mating-type-dependent expression [PMID:3036506]. UniProt: regulated by arginine and urea.
- Location: soluble (cytosolic) fraction [PMID:205532 "the two first catabolic enzymes, arginase and ornithine aminotransferase, were in the"]. Contrast with mammalian/plant OAT (mitochondrial matrix).

## Curation decisions
- Core MF GO:0004587; BP GO:0006527; CC GO:0005829.
- Mitochondrion IBA (PTN000241155, animal/plant mitochondrial OATs; no fungal seed): REMOVE - yeast OAT is soluble/cytosolic by fractionation in which mitochondrial matrix enzymes of the acetylated cycle sedimented with mitochondria.
- L-proline biosynthetic process (UniPathway IEA): KEEP_AS_NON_CORE. The GSA/P5C product can in principle be reduced to proline, but in yeast arginine nitrogen is routed via P5C to glutamate (PUT2); the arginase-2 MetaCyc framing (to proline) is the YeastCyc pathway context.
