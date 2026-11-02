# Bacillus cereus phnW curation notes

## 2026-10-25

`just fetch-gene BACCE phnW` resolved to Q8RLU1 (PHNW_BACCE), not a strain-specific substitute. The UniProt record links the nucleotide sequence to B. cereus ATCC 43881 / AI-2 and Baker's 1996 thesis. It assigns the PhnW class-V aminotransferase subfamily with HAMAP MF_01376, InterPro IPR012703 and PANTHER PTHR42778:SF1. These support an inferred catalytic role in the first step of PhnWX 2-aminoethylphosphonate degradation.

**Sequence limitation:** the reviewed record is 344 aa and has a C-terminal NON_TER feature, a probable-fragment caution, and a frameshift caution on AAL83669.1. [UniProtKB:Q8RLU1, CC:CAUTION, "Upon comparison to orthologs, this is probably a fragment."] Do not use this accession as evidence for an experimentally active intact Bacillus PhnW, and do not interpret the sequence warning as proof that the native bacterial gene is nonfunctional. Resolving that distinction requires resequencing the original isolate.

The two GOA assertions are retained as inferred gene-function assignments. The reaction and process are supported by specific curated family classification rather than by the protein name, GO lines, or another gene's annotations. No location annotation is invented.

[PMID:12107130, The 2-aminoethylphosphonate-specific transaminase of the 2-aminoethylphosphonate degradation pathway, "Substrate specificity tests revealed a high degree of discrimination"] characterizes the Salmonella protein. Its results ground the family function but are not Bacillus Q8RLU1 measurements. [PMID:37836707, The Microbial Degradation of Natural and Anthropogenic Phosphonates, "The PhnWX pathway was initially described in Bacillus cereus"] supplies comparative pathway context. The earlier Bacillus pathway experiments establish species-level biochemistry without proving that the presently deposited sequence fragment was tested.

Manual literature work was used because this session's `just deep-research-falcon BACCE phnX --fallback perplexity-lite` had already failed with Falcon authentication failure and Perplexity insufficient quota. No redundant call to the same unavailable providers was made for phnW, and no provider-labelled report was fabricated. `just fetch-gene-pmids BACCE phnW` found no seeded PMIDs (the GOA sources are GO_REF records). `just fetch-fitness BACCE phnW` found no configured BACCE mapping or reachable FEBA data source, so no fitness artifact was created.
