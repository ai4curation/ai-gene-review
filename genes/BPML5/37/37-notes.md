# Curation Notes for Mycobacteriophage L5 Gene 37 (gp37, Q05247)

## Summary
- **Gene symbol**: `37`
- **UniProt ID**: `Q05247` (`VG37_BPML5`, 114 aa, 12.5 kDa)
- **Genomic context**: Encoded in the left-arm early/integration region of Mycobacteriophage L5 immediately upstream of the excisionase gene `XIS` (`36`) [PMID:8459766].
- **Domain architecture**: Contains a conserved all-alpha MazG-like nucleotide pyrophosphatase domain (`IPR004518` `MazG-like_dom`, `IPR011379` `MazG-related_GP37`, `PF03819` `MazG`, `CDD:cd11541` `NTP-PPase_u4`, `SSF101386` `all-alpha NTP pyrophosphatases`).
- **Function**: Putative MazG-like nucleotide pyrophosphatase (nucleoside triphosphate pyrophosphohydrolase). Phage-encoded MazG homologs hydrolyze canonical or non-canonical nucleoside triphosphates ( or alarmones such as (p)ppGpp) to modulate host nucleotide pools or stringent response signaling during infection.
- **Curation decisions**:
  - Propose `NEW` `GO:0004551` (`nucleotide diphosphatase activity`) (or `GO:0016787` `hydrolase activity`) supported by `file:genes/BPML5/37/37-uniprot.txt`. Let's include `GO:0016787` (`hydrolase activity`) in `existing_annotations` and `core_functions`.
