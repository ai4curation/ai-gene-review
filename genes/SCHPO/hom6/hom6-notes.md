# hom6 (SPBC776.03, UniProt O94671) notes

Homoserine dehydrogenase (EC 1.1.1.3), monofunctional, PTHR43070:SF5.

- [UniProt:O94671 "Reaction=L-homoserine + NADP(+) = L-aspartate 4-semialdehyde + NADPH +"]; also NAD(+) reaction (RHEA:15757); both by similarity to S. cerevisiae Hom6 (P31116).
- [UniProt:O94671 "FUNCTION: Catalyzes the conversion of L-aspartate-beta-semialdehyde (L-"]; homoserine is the threonine/methionine branch point [UniProt:O94671 "point in the pathway as it can either be O-phosphorylated for"].
- S. cerevisiae Hom6: [PMID:11341914 "HSD efficiently reduces aspartate semialdehyde to homoserine (Hse) using either NADH or NADPH"].
- No S. pombe experimental annotation; cytosol only by PomBase IC from GO-CAM 678073a900003175.

## Decisions
- GO:0004022 alcohol dehydrogenase (NAD+) from Rhea2GO of RHEA:15757: MODIFY -> GO:0004412 (checked: GO:0004412 is not is_a GO:0004022; ancestors are oxidoreductase CH-OH/NAD(P) classes). Same as S. cerevisiae HOM6 review.
- Core = GO:0004412 / GO:0009090 / cytosol (same as HOM6 review).
