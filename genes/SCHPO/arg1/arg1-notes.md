# arg1 (SPCC777.09c, UniProt O74548) notes

## Naming trap
- S. pombe arg1 = acetylornithine aminotransferase (ortholog of S. cerevisiae ARG8). S. cerevisiae ARG1 (argininosuccinate synthase) = S. pombe arg12.

## Identity / activity
- [UniProt:O74548 "RecName: Full=Probable acetylornithine aminotransferase, mitochondrial;"], class-III PLP aminotransferase, PTHR11986:SF79; activity by similarity [UniProt:O74548 "Reaction=N(2)-acetyl-L-ornithine + 2-oxoglutarate = N-acetyl-L-"].
- Matrix location by similarity (transit peptide predicted) [UniProt:O74548 "SUBCELLULAR LOCATION: Mitochondrion matrix {ECO:0000250}."].

## Genetics
- Mercier & Labbe 2010: [PMID:20435771 "which encodes an acetylornithine aminotransferase essential to mitochondrial ornithine production"]; [PMID:20435771 "The arginine auxotrophy of the arg1Δ and arg1Δ car1Δ car3Δ strains was validated by their inability to grow on arginine-free minimal medium"]. arg1 car1 car3 lose all ornithine; matters for ferrichrome under iron starvation.
- Ma et al. 2007 marker screen: [PMID:17622533 "New alleles of arg1 (+), lys3 (+) and met6 (+) were"].
- Deletion screen PMID:32896087 (EXP).

## Decisions
- urea cycle EXP (PMID:20435771) MARK_AS_OVER_ANNOTATED: aminotransferase is upstream of ornithine, not a urea-cycle reaction.
- Did not add GO:0006592 (ornithine biosynthesis) as NEW; ARG8 carries it as TAS but PomBase did not annotate it.
- Core: GO:0003992, GO:0006526, mitochondrial matrix (= ARG8 core minus the ornithine BP).
