# BNA2 (YJR078W, P47125) notes

## Identity
- Heme indoleamine 2,3-dioxygenase family; first step of the kynurenine pathway (L-Trp -> N-formyl-L-kynurenine). S. cerevisiae has a single IDO and no TDO [PMID:21170645 "In fungi, the IDO homologue is thought to be expressed constitutively and supply NAD(+), as TDO is absent from their genomes."; "The yeast, Saccharomyces cerevisiae has only one IDO gene"].
- UniProt lists both RHEA:24536 (L-Trp) and RHEA:14189 (D-Trp) reactions.

## Ontology note (important for module)
- In current GO, GO:0033754 "indoleamine 2,3-dioxygenase activity" is defined on D-tryptophan (RHEA:14189), while GO:0004833 "L-tryptophan 2,3-dioxygenase activity" is the L-Trp reaction (RHEA:24536, EC 1.13.11.11). The physiological NAD-pathway reaction for Bna2 is the L-Trp one, so GO:0004833 is chosen as core MF despite the IDO protein family name. YeastPathways gives the L-Trp reaction (EC 1.13.11.11, 1.13.11.52) but maps it to GO:0033754.
- GO:0034354 obsolete; replaced_by GO:0034628.

## Pathway evidence
- Kynurenine pathway genes required for de novo NAD [PMID:12062417].
- Cytoplasm in the localization survey [PMID:11914276].
