# erg1 notes

## Workflow

- `just fetch-gene ASPFU erg1` seeded E9R5G2 / AFUA_5G07780 and 11 current GOA rows.
- `just deep-research-falcon ASPFU erg1` failed because `falcon` is not available in this environment. No `erg1-deep-research-falcon.md` file was created.
- Web/PubMed search found two direct *A. fumigatus* ERG1/ergA terbinafine-resistance papers beyond the UniProt-cited pathway papers: Liu et al. 2004 (PMID:15215099) and Rocha et al. 2006 (PMID:16801438). The Liu 2004 PMC full text was not available to the fetcher, but the abstract directly identifies A. fumigatus ERG1 as the squalene epoxidase gene whose extra copies confer terbinafine resistance. Rocha 2006 is full-text cached and reports that an engineered F389L substitution in A. fumigatus ErgA is sufficient for terbinafine resistance.

## Evidence Summary

- UniProt E9R5G2 places A. fumigatus erg1 in PANTHER `PTHR10835:SF0`, the same squalene monooxygenase subfamily as S. cerevisiae ERG1, S. pombe erg1, C. albicans ERG1, C. glabrata ERG1, and human SQLE.
- `PTHR10835	PTN000089417	GO:0004506	F	IBD	false` is the PAINT root placement for squalene monooxygenase activity across fungal and animal descendants; A. fumigatus Erg1 is inside this clade.
- `PTHR10835	PTN000089417	GO:0005783	C	IBD	false` places ER localization on the same PAINT node, consistent with UniProt's inferred ER/microsomal multi-pass membrane localization.
- `PTHR10835	PTN000851137	GO:0006696	P	IBD	false` is the fungal ergosterol-biosynthesis placement seeded by Candida and budding yeast ERG1; no Aspergillus-specific loss or divergence is apparent.
- InterPro2GO `GO:0016020 membrane` is true but generic for an ER-membrane sterol enzyme, while ARBA `GO:0016125 sterol metabolic process` and combined `GO:0016126 sterol biosynthetic process` are broader parents of the specific fungal ergosterol process.
