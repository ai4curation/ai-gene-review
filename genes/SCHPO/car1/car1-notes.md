# car1 (SPBP26C9.02c, UniProt P37818) notes

## Identity and naming
- PomBase car1 = arginase (EC 3.5.3.1), ortholog of S. cerevisiae CAR1. Paralog aru1 (SPAC3H1.07, Q10066), which is called "car3" in PMID:20435771 [PMID:20435771 "In fission yeast, the open-reading frame car3 + ( SPAC3H1.07 ) encodes a protein that exhibits high homology with arginase Car1 (87.9% identity and 93.5% similarity)."]
- Both in PANTHER PTHR43782:SF3.

## Function
- Cloned by complementation of S. cerevisiae car1 [PMID:7985419 "we cloned the gene by functional complementation of a car1 mutant"]; arginase synthesis induced at transcription level [PMID:7985419 "that the induction of arginase synthesis operates at a transcriptional level"].
- Arginase activity in extracts depends on car1 + aru1 [PMID:20435771 "Regardless of the iron status, all extracts possessed arginase activity except in the case of car1Δ car3Δ cell lysate."]; car1 transcription and Car1 activity repressed by iron (Fep1), linking arginase-derived ornithine to ferrichrome synthesis.
- Arginine conversion (to proline, glutamate, glutamine, lysine) needs arginase: single car1Δ still converts; aru1 is the major arginase; double deletion abolishes [PMID:20460254 "This suggests that Aru1 is the major arginase in fission yeast."], [PMID:20460254 "Interestingly, however, conversion was almost completely prevented in a car1Δ aru1Δ double deletion strain"], confirmed for Arg-10 in PMID:26075619.
- Mn2+ cofactor, homotrimer by similarity [UniProt:P37818].

## Location
- Cytosol and nucleus in ORFeome screen (HDA, PMID:16823372); PomBase GO-CAM 678073a900003902 cytosol.

## Curation points
- Urea cycle rows (IBA, IEA, and PomBase IGI from PMID:20435771): S. pombe has OTC (mitochondrial arg3) and the cytosolic ASS/ASL, but arginase acts in arginine catabolism (nitrogen use, ornithine supply), not a ureotelic cycle. MODIFY to GO:0006527, consistent with the yeast CAR1 review and the module note. PomBase GO-CAM also uses urea cycle — flag for curator.
- No S. pombe evidence for the arginase–OTC "epiarginase" complex described for budding-yeast CAR1/ARG3; S. pombe OTC is mitochondrial, so this regulatory complex probably cannot form. Not asserted.
