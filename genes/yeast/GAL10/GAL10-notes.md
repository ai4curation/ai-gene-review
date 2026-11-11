# GAL10 (YBR019C, P04397) notes

## Domain architecture / activities
- Bifunctional: N-terminal UDP-glucose 4-epimerase (EC 5.1.3.2) and C-terminal aldose 1-epimerase/mutarotase (EC 5.1.3.3) [UniProt:P04397 "RecName: Full=Bifunctional protein GAL10;"].
- Majumdar et al. 2004 [PMID:14764091 "Sequence analysis indicates that the yeast epimerase has an N-terminal domain (residues 1-377) that shows significant similarity with Escherichia coli and human UDPgalactose 4-epimerase, and a C-terminal domain (residues 378-699), which shows extensive identity to either the bacterial or human aldose 1-epimerase (mutarotase)."].
- Purified Gal10 has intrinsic mutarotase activity [PMID:14764091 "Size exclusion chromatography experiments confirmed that the mutarotase activity is an intrinsic property of the yeast epimerase and not due to a copurifying endogenous mutarotase."]; two separate active sites [PMID:14764091 "The active sites for these two enzymatic activities are located in different regions of the epimerase holoenzyme."].
- Both activities induced by galactose [PMID:14764091 "Induction of cells with galactose led to simultaneous enhancement of both epimerase and mutarotase activities."].
- NAD+ cofactor for epimerase domain [UniProt:P04397 "Name=NAD(+); Xref=ChEBI:CHEBI:57540;"].
- Classical genetics (Douglas & Hawthorne 1964, title only cached) [PMID:14158615 "ENZYMATIC EXPRESSION AND GENETIC LINKAGE OF GENES CONTROLLING GALACTOSE UTILIZATION"].

## Assessment
- Core: two Leloir steps -- beta->alpha galactose anomerization (feeding Gal1) and UDP-galactose -> UDP-glucose epimerization (regenerating the UDP-glucose for Gal7). Cytosolic.
- YeastPathways assignment of EC 5.1.3.2 and 5.1.3.3 both correct. Note YeastPathways writes beta-D-galactose -> alpha-D-galactose, whereas the UniProt Rhea xref is glucose anomerization (RHEA:10264); both anomers are substrates.
- General IEA terms (isomerase, carbohydrate binding, hexose metabolic process) are true but uninformative.
