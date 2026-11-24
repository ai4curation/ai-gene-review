# Enterobacteria Phage P4 Gene cI (Immunity Region Locus cI / seqB) — Curation Notes

## Overview
Enterobacteria satellite phage P4 entry `cI` (`P05462`, 137 aa, ~15.4 kDa) corresponds to the open reading frame originally proposed by Lin (1984) (`PMID:6095206`) to encode a 15 kDa immunity repressor based on the location of the `cI405` and `ash` clear-plaque mutations [PMID:6095206, PMID:2183201].

## Crucial Discovery: P4 Immunity Is Mediated by an Antisense RNA (CI RNA / `seqB`), Not a 15 kDa Protein
- **Historical Context (`PMID:6095206`)**: Lin (1984) sequenced the essential region of phage P4 and noted that `cI405`, a recessive clear-plaque mutation affecting lysogenic immunity, mapped within a sequence capable of coding for a 137-aa (~15 kDa) polypeptide (`P05462`) [PMID:6095206, "cI405, a proposed repressor gene mutation, is located in a sequence capable of coding for a 15 kd protein. A new class of P4 mutations, ash, is located in the neighborhood of cI405."].
- **Subsequent Resolution (`PMID:2183201` and UniProt Caution)**: Subsequent genetic and molecular analyses (Ghisotti et al., Dehò et al., summarized in the UniProt `P05462` `FUNCTION` and `CAUTION` comments) demonstrated that P4 immunity (`cI` locus) is actually mediated by a small stable catalytic/regulatory **antisense RNA** (`CI RNA`, transcribed from the `seqB` region within the early rightward operon) that promotes premature transcription termination upstream of the `alpha` replication gene by base-pairing with `seqA`! The putative 137-aa ORF (`P05462`) overlapping this RNA locus is not the immunity repressor and has no demonstrated protein function (`PE=4`).

## GO Annotation Review
- No experimental or computational GO annotations are currently assigned in GOA; `existing_annotations` and `core_functions` are therefore left empty pending experimental characterization.
