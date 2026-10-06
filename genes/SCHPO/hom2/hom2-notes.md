# hom2 (SPCC1827.06c, UniProt P78780) notes

Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), PTHR46718:SF1.

- [UniProt:P78780 "Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-"]; [UniProt:P78780 "FUNCTION: Catalyzes the NADPH-dependent formation of L-aspartate 4-"] (by similarity to S. cerevisiae Hom2 P13663).
- Location: [UniProt:P78780 "SUBCELLULAR LOCATION: Cytoplasm, cytosol {ECO:0000269|PubMed:16823372}."] plus nucleus (ORFeome GFP).
- S. cerevisiae: [PMID:2570346 "In Saccharomyces cerevisiae the HOM2 gene encodes aspartic semi-aldehyde"] dehydrogenase.
- Lysine: InterPro2GO maps IPR012080 to L-lysine biosynthesis (bacterial/plant DAP pathway: [PMID:11352712 "The aspartate pathway is responsible for the biosynthesis of lysine, threonine, isoleucine, and methionine in most plants and microorganisms."]). Fungi use the alpha-aminoadipate pathway (S. pombe lys4 homocitrate synthase is in PomBase GO-CAM gomodel:67c10cc400000148). REMOVE, as for S. cerevisiae HOM2.
- NAD binding (IPR000534 domain name) -> over-annotation, as in HOM2 review.

## Naming/label note
- GO:0004073 current label is "aspartate-semialdehyde dehydrogenase activity" (GOA file still says "(NADP+) activity"); used the current label in core_functions, left GOA labels untouched.
- Core = GO:0004073 / GO:0009090 / cytosol; agrees with HOM2 review and GO-CAM 678073a900003175.
