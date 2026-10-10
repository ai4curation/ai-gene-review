# arg6 (SPBC725.14, UniProt O94330) notes

## Identity and naming
- PomBase arg6 = mitochondrial N-acetylglutamate synthase (NAGS, EC 2.3.1.1), ortholog of S. cerevisiae ARG2 (P40360). [UniProt:O94330 "RecName: Full=Amino-acid acetyltransferase, mitochondrial;"]
- Naming trap: S. cerevisiae ARG6 is part of the ARG5,6 kinase/reductase polyprotein (S. pombe arg11), not NAGS.
- PANTHER PTHR23342:SF4 "AMINO-ACID ACETYLTRANSFERASE, MITOCHONDRIAL"; InterPro IPR011190 (fungal NAGS) and IPR006855 (vertebrate-like GNAT). Predicted transit peptide 1..19. [UniProt:O94330]

## Function
- Catalysis: [UniProt:O94330 "Reaction=L-glutamate + acetyl-CoA = N-acetyl-L-glutamate + CoA + H(+);"] — by similarity only; no S. pombe enzyme assay in the cached literature.
- Pathway: first step of the acetylated ornithine route [UniProt:O94330 "N-acetylglutamate synthase involved in arginine biosynthesis."]
- Genetic: PomBase EXP annotation to arginine biosynthesis from PMID:17248775 (1977 genetic mapping paper, abstract only; the abstract does not name arg6, presumably the arg6 auxotrophic marker is mapped in the full text); also PomBase EXP from the deletion-library arginine-auxotroph screen [PMID:32896087 "As expected, these arginine‐auxotroph mutants included those with impaired arginine biosynthesis."]

## Location
- Mitochondrion by ORFeome YFP screen [UniProt:O94330 "SUBCELLULAR LOCATION: Mitochondrion {ECO:0000269|PubMed:16823372}."]; PomBase GO-CAM 6690711d00000916 places arg6 NAGS in mitochondrial matrix, causally upstream of arg11 acetylglutamate kinase.

## Curation points
- GO:0097054 L-glutamate biosynthetic process (NAS, keyword mapping GO_REF:0000051) is wrong in direction: NAGS consumes glutamate. Remove.
- Core MF GO:0004042, BP GO:0006526 (and GO:0006592 ornithine biosynthesis, IBA), CC mitochondrial matrix — same as yeast ARG2 review.
- Yeast ARG2 is in the NAGS/NAGK complex (GO:0106098) with Arg5,6; no S. pombe evidence for arg6–arg11 complex in cached literature, so in_complex not asserted.
