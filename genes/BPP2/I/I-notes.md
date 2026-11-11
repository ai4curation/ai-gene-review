# BPP2 I (P26701 / BPI_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `I`
- **UniProt ID**: `P26701` (`BPI_BPP2`)
- **Protein**: Baseplate protein I / gpI (176 aa, 19.8 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:7483254** (Haggård-Ljungquist et al., 1995, *Virology*):
   - Sequenced the essential P2 tail gene `I` (located between `J` and `H` in the `V-W-J-I-H-G` operon), identified the `I` gene product as a structural protein of the phage tail, and showed that `I` is an essential tail gene.
   - Quote: `"The sequences of two previously defined tail genes, V and J, of the temperate bacteriophage P2, and those of two new essential tail genes, W and I, were determined."`
2. **PMID:24097944** (Maxwell et al., 2013, *J. Virol.*):
   - Summarizes comparative structural analyses indicating that P2 `gpI` and `gpJ` form the peripheral baseplate wedges (homologous to T4 gp6/gp7 wedge components and Mu gp45/gp46).
   - Quote: `"The P2 proteins gpI and gpJ are believed to comprise the baseplate wedges ( 7 ), and gpJ has been detected at the periphery of the P2 baseplate ( 9 )."`
3. **PMID:22297511** (Leiman & Shneider, 2012, *Adv. Exp. Med. Biol.*):
   - Assigns P2 gpI as one of the two core wedge subunits (with gpJ) of the contractile tail baseplate.

## Annotation Review Decisions
- `GO:0098003` (`viral tail assembly`, IEA): **ACCEPT** — `I` is an essential tail morphogenesis gene required to build the baseplate.
- `GO:0098015` (`virus tail`, IEA): **MODIFY** to `GO:0098025` (`virus tail, baseplate`).
- `GO:0098025` (`virus tail, baseplate`, IEA): **ACCEPT**.
- **NEW** `GO:0039660` (`structural constituent of virion`, IDA, `PMID:7483254`): `PMID:7483254` identified gpI directly as a structural protein of the P2 virion tail baseplate.
