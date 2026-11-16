# E. coli recJ (P21893) notes

## 2026-11-13 review session

Context: 5'->3' excision exonuclease candidate for the MMR module.

### Function summary (with provenance)

- ssDNA-specific 5'-3' exonuclease, no dsDNA exo/endo activity [PMID:2649886 "The RecJ nuclease degraded linear single-stranded DNA but did not have exonuclease activity on linear double-stranded substrates"; "greater activity on duplex DNA molecules with 5'-rather than 3'-single-stranded tails"].
- Required for RecF-pathway recombination [PMID:6317649 "a gene essential for the RecF pathway of recombination"].
- Daughter-strand gap repair after UV [PMID:3286613 "the recJ mutation produced a deficiency in the repair of daughter strand gaps in uvrB recB cells"]; RecJ ExoVII double mutant extremely UV sensitive [PMID:9584082].
- MMR excision, redundant with ExoVII, ExoI, ExoX [PMID:11418610; PMID:11381137 "These observations confirm involvement of the four exonucleases in methyl-directed mismatch repair in vivo"].

### Decisions

- GO:0006281 DNA repair IEA -> MODIFY to GO:0006298 mismatch repair and GO:0000725 recombinational repair (both is_a DNA repair, verified with runoak). IMP row (PMID:3286613) -> MODIFY to GO:0000725. GO:0006301 was considered but is now "DNA damage tolerance", not a repair child.
- GO:0008409 -> MODIFY to GO:0045145; GO:0003676 -> MODIFY to GO:0003697; GO:0003824 -> TOO_GENERAL.
- TopB protein-binding rows -> REMOVE.
- GO:0010165 response to X-ray (PMID:27718375): abstract does not name recJ; KEEP_AS_NON_CORE deferring to curator.
