# Curation Notes for Mycobacteriophage L5 Gene 25 (Tail assembly protein Gp25, Q05232)

## Summary
- **Gene symbol**: `25`
- **UniProt ID**: `Q05232` (`TAP25_BPML5`, 272 aa, 30.9 kDa)
- **Alternative products**: Produced via a programmed -1 ribosomal frameshift during translation of gene `24`, yielding a 272-aa transframe fusion protein (`Q05232-1`) sharing its N-terminal domain with Gp24 (`Q05231-1`) and containing a C-terminal extension encoded by ORF `25` [PMID:15469818].
- **Function**: Siphoviral tail assembly chaperone (functional analog of bacteriophage lambda gpGT). Together with Gp24 (`Q05231`), Gp25 wraps the linear tape measure protein (Gp26) and recruits/scaffolds the major tail tube subunit (Gp23) during tail tube polymerization, dissociating before virion maturation [PMID:15469818, PMID:8459766].
- **Curation decisions**:
  - `GO:0098003` (`viral tail assembly`, IEA): `ACCEPT`. Core biological role of this transframe tail assembly chaperone.
  - `GO:0075523` (`viral translational frameshifting`, IEA from `UniProtKB-KW:KW-0688`): `REMOVE`. Programmed ribosomal frameshifting is a cis-acting mRNA translation mechanism that generates Gp25, not a biological process performed by the Gp25 protein product.
