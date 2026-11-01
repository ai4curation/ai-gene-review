# BPP2 R (P36933 / VPR_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `R`
- **UniProt ID**: `P36933` (`VPR_BPP2`)
- **Protein**: Tail completion protein R / gpR (155 aa, 17.5 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:8178426** (Linderoth et al., 1994, *Virology*):
   - Sequenced P2 tail genes `R` and `S` and mapped amber mutations `Ram3`, `Ram42`, and `Ram23` to the `R` open reading frame.
   - Identified sequence homology between a conserved region of P2 `gpR` and bacteriophage T4 tail completion protein `gp15` (which caps the T4 tail tube/sheath top to allow stable head-tail joining), and proposed that `gpR` and `gpS` are tail completion proteins essential for stable head-tail joining and preventing aberrant tail elongation.
   - Quotes:
     - `"The sequences of two previously known tail genes, R and S, of the temperate bacteriophage P2 and the sequence of an additional open reading frame (orf-30) located between S and V, were determined."`
     - `"Amber mutations mapping within R and S, Ram3, Ram42, Ram23, Sam75, and Sam89 were sequenced and found to be within their corresponding open reading frames."`
     - `"However, the R protein contains a small region homologous to one in the phage T4 tail protein gp15, which is required for T4 tails to bind heads. We propose that R and S are tail completion proteins that are essential for stable head joining."`

## Annotation Review Decisions
- No existing GOA annotations (`existing_annotations: []` in stub).
- **NEW** `GO:0039660` (`structural constituent of virion`, IMP, `PMID:8178426`): gpR is a structural tail completion protein at the head-binding neck/top of the P2 tail (homologous to T4 gp15).
- **NEW** `GO:0098003` (`viral tail assembly`, IMP, `PMID:8178426`): `Ram` mutants fail to complete normal tail morphogenesis, producing abnormally elongated tail structures.
- **NEW** `GO:0098005` (`viral head-tail joining`, IMP, `PMID:8178426`): gpR is required at the final stage of tail synthesis to cap the tail so that finished tails can stably join to DNA-filled heads.
- **NEW** `GO:0098015` (`virus tail`, IMP, `PMID:8178426`): gpR localizes to the proximal neck/top end of the virion tail.
