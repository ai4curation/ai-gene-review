# ERG1 notes

## C. glabrata ERG1 re-review, 2026-11-22

`just fetch-gene CANGA ERG1` seeded 13 current GOA rows for the reviewed
UniProt entry `O13306`: EC/Rhea/InterPro/budding-yeast transfers for squalene
monooxygenase activity, ER and ER-membrane localization, lipid-droplet
localization, sterol/ergosterol biosynthetic processes, FAD binding, and two
CGD IMP rows from Tsai et al. 2004.

O13306 is in `PTHR10835:SF0`, the active squalene monooxygenase subfamily that
also contains S. cerevisiae Erg1, S. pombe Erg1, C. albicans Erg1, A. fumigatus
Erg1/ErgA, mammalian SQLE, and some plant squalene epoxidases. The current
PTHR10835 PAINT file places squalene monooxygenase activity, ER localization,
and a broad sterol biosynthetic process on `PANTHER:PTN000089417`; the fungal
ergosterol-biosynthesis process is placed more narrowly on
`PANTHER:PTN000851137`, seeded by CGD and SGD.

The key C. glabrata paper is Tsai et al. 2004. The local cache is abstract-only
because PMC full text access was restricted, but the abstract directly reports
that the Cgerg1 transposon mutant decreases ergosterol by 50%, accumulates the
squalene precursor, increases susceptibility to fluconazole, itraconazole and
terbinafine, increases amphotericin resistance, increases rhodamine 6G and
fluconazole uptake, blocks low-oxygen growth, and is restored to wild-type drug
susceptibility by complementation [PMID:15215098, "Interruption following codon
475 of CgErg1p decreased the ergosterol content by 50%; caused accumulation of
the squalene precursor"].

I searched PubMed for `(Candida glabrata OR Nakaseomyces glabratus) AND (ERG1
OR squalene epoxidase OR squalene monooxygenase)`. The 2025 hits were
ergosterol-pathway or compound-perturbation papers, including tunicamycin and
thymol studies, rather than direct CgErg1 biochemical or localization studies
that would change this review. The 2022-2025 papers likewise use sterol uptake
or ergosterol-biosynthesis context rather than assigning a new ERG1-specific
activity.

The CGD `GO:0071466 cellular response to xenobiotic stimulus` IMP row is a
drug-susceptibility phenotype of an ergosterol-pathway mutant. It is useful
experimental support for the pathway lesion but should not be a core ERG1
process because CgErg1 supplies membrane sterol and does not execute a
xenobiotic-response program directly.
