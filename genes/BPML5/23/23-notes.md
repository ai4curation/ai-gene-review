# Curation Notes for Mycobacteriophage L5 Gene 23 (Major tail protein Gp23, Q05229)

## Summary
- **Gene symbol**: `23`
- **UniProt ID**: `Q05229` (`VG23_BPML5`, 198 aa, 21.5 kDa; initiator methionine cleaved)
- **Experimental evidence**: Identified by N-terminal amino acid sequencing (residues 2-17) of purified L5 virion proteins as the abundant major tail subunit [PMID:8459766].
- **Domain architecture**: Contains the conserved Bxb1_TTP-like siphoviral tail tube protein domain (`IPR058154` / `PF25681`, `Phage_TTP_17`).
- **Curation decisions**:
  - `GO:0019028` (`viral capsid`, IEA from `UniProtKB-KW:KW-0167`): `MODIFY` -> `GO:0098015` (`viral tail`). UniProt historically assigned the Legacy keyword `Capsid protein` (`KW-0167`) and synonym `Major coat protein` to gp23, whereas the primary recommended name (`Major tail protein Gp23`), N-terminal sequencing of virion tail polypeptides [PMID:8459766], and classification in the phage tail tube protein family (`IPR058154` Bxb1_TTP-like / `PF25681` Phage_TTP_17) establish that gp23 is the major tail tube subunit rather than the capsid subunit (which is encoded by gene `17`).
  - Add `NEW` `GO:0098015` (`viral tail`), `GO:0005198` (`structural molecule activity`), and `GO:0098003` (`viral tail assembly`).
