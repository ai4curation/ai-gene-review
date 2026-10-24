# Curation Notes for Mycobacteriophage L5 Gene 24 (Tail assembly protein Gp24, Q05231)

## Summary
- **Gene symbol**: `24`
- **UniProt ID**: `Q05231` (`VG24_BPML5`, 132 aa, 14.8 kDa)
- **Alternative products**: Conventional translation of gene `24` produces the 132-aa isoform `Q05231-1` (Gp24), while a programmed -1 ribosomal frameshift near the 3' end of `24` produces the 272-aa fusion protein `Q05232-1` (Gp25 / gp24-gp25) [PMID:15469818].
- **Function**: Siphoviral tail assembly chaperone (functional analog of bacteriophage lambda gpG). Together with the frameshifted gp24-gp25 product, Gp24 coats the linear tape measure protein (gp26) to form a scaffold required for polymerization of the major tail tube protein (gp23), dissociating prior to virion maturation [PMID:15469818, PMID:8459766].
- **Curation decisions**:
  - `GO:0098003` (`viral tail assembly`, IEA): `ACCEPT`. Core biological role of this tail assembly chaperone.
  - `GO:0075523` (`viral translational frameshifting`, IEA from `UniProtKB-KW:KW-0688`): `REMOVE`. Programmed ribosomal frameshifting is a cis-acting property of the viral mRNA slippery sequence during translation by the host ribosome, not a biological process performed by the translated Gp24 protein product.
