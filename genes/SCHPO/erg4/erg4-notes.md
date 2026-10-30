# erg4 (SPAC20G4.07c; UniProt P36209) notes

- NAMING TRAP: UniProt gene name is sts1 (GN Name=sts1; staurosporine supersensitive), PomBase symbol erg4. `just fetch-gene SCHPO erg4` failed ("Could not find any UniProt ID"); fetched with `-u P36209` and moved. Verified ID ERG4_SCHPO, AC P36209.
- Reaction: [UniProt:P36209 "Reaction=ergosterol + NADP(+) = ergosta-5,7,22,24(28)-tetraen-3beta-ol"] (physiological direction right-to-left) EC 1.3.1.71.
- sts1 cloned as staurosporine-supersensitive gene [PMID:1320960 "By gene disruption we demonstrate that the sts1+ gene is not essential for viability."]; sts1 disruptants have the Erg4 defect [PMID:8125337 "strains carrying disruptions of sts1+ or YGL022 have ergosterol biosynthesis defects in the enzyme, sterol C-24(28) reductase"].
- No ergosterol in deletion [PMID:23145048 "Consistently, no ergosterol peak was observed in Δsts1 cells."]; accumulates ergosta-5,7,22,24(28)-tetraenol (UniProt disruption phenotype).
- ER membrane multi-pass (UniProt ECO:0000305).
- Budding-yeast ERG4 review core: GO:0000246, ER membrane. Consistent.
- GO-CAM 66c7d41500002088: erg4 GO:0000246 in ER membrane; terminal step, no outgoing edge. Agrees.
