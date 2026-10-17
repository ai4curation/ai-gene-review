# BPP2 S (P36934 / VPS_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `S`
- **UniProt ID**: `P36934` (`VPS_BPP2`)
- **Protein**: Tail completion protein S / gpS (150 aa, 17.5 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:8178426** (Linderoth et al., 1994, *Virology*):
   - Sequenced P2 tail genes `R` and `S` and mapped amber mutations `Sam75` and `Sam89` to the `S` open reading frame.
   - Proposed that `gpR` and `gpS` are tail completion proteins essential for terminating tail polymerization at the proper length and enabling stable attachment of finished tails to DNA-filled heads (analogous to T4 gp15 and gp3).
   - Quotes:
     - `"The sequences of two previously known tail genes, R and S, of the temperate bacteriophage P2 and the sequence of an additional open reading frame (orf-30) located between S and V, were determined."`
     - `"Amber mutations mapping within R and S, Ram3, Ram42, Ram23, Sam75, and Sam89 were sequenced and found to be within their corresponding open reading frames."`
     - `"However, the R protein contains a small region homologous to one in the phage T4 tail protein gp15, which is required for T4 tails to bind heads. We propose that R and S are tail completion proteins that are essential for stable head joining."`

## Annotation Review Decisions
- No existing GOA annotations (`existing_annotations: []` in stub).
- **NEW** `GO:0039660` (`structural constituent of virion`, IMP, `PMID:8178426`): gpS is a structural tail completion subunit at the proximal (head-binding) end of the P2 tail.
- **NEW** `GO:0098003` (`viral tail assembly`, IMP, `PMID:8178426`): `Sam75` and `Sam89` mutations disrupt normal tail completion and length control during P2 tail morphogenesis.
- **NEW** `GO:0098005` (`viral head-tail joining`, IMP, `PMID:8178426`): gpS is required at the final stage of tail synthesis so that finished tails can stably join to DNA-filled heads.
- **NEW** `GO:0098015` (`virus tail`, IMP, `PMID:8178426`): gpS localizes to the proximal neck/top end of the virion tail.
