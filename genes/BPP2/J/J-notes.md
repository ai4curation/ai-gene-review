# BPP2 J (P51767 / BPJ_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `J`
- **UniProt ID**: `P51767` (`BPJ_BPP2`)
- **Protein**: Baseplate protein J / gpJ (302 aa, 33.0 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:7483254** (Haggård-Ljungquist et al., 1995, *Virology*):
   - Sequenced P2 gene `J` and used immunoelectron microscopy with anti-gpJ antibodies to localize `gpJ` to the outer periphery (edge) of the P2 baseplate.
   - Quotes:
     - `"The sequences of two previously defined tail genes, V and J, of the temperate bacteriophage P2, and those of two new essential tail genes, W and I, were determined."`
     - `"The V gene product is the small spike at the tip of the tail, and the J gene product lies at the edge of the baseplate."`
2. **PMID:24097944** (Maxwell et al., 2013, *J. Virol.*):
   - Notes that P2 proteins `gpI` and `gpJ` comprise the peripheral baseplate wedges, with `gpJ` localized at the baseplate periphery.
   - Quote: `"The P2 proteins gpI and gpJ are believed to comprise the baseplate wedges ( 7 ), and gpJ has been detected at the periphery of the P2 baseplate ( 9 )."`

## Annotation Review Decisions
- `GO:0098015` (`virus tail`, IEA): **MODIFY** to `GO:0098025` (`virus tail, baseplate`).
- `GO:0098025` (`virus tail, baseplate`, IDA `PMID:7483254` & IEA `GO_REF:0000043`): **ACCEPT** — immunoelectron microscopy directly localized gpJ to the edge of the P2 baseplate.
- **NEW** `GO:0039660` (`structural constituent of virion`, IDA, `PMID:7483254`): gpJ is a major structural protein at the periphery of the P2 virion baseplate.
- **NEW** `GO:0098003` (`viral tail assembly`, IMP, `PMID:7483254`): `J` is an essential tail morphogenetic gene required for baseplate and tail assembly.
