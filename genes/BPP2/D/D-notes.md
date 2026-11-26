# BPP2 D (P10312 / BPD_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `D`
- **UniProt ID**: `P10312` (`BPD_BPP2`)
- **Protein**: Probable baseplate hub protein gpD (387 aa, 42.8 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:12426340** (Christie et al., 2002, *J. Bacteriol.*):
   - Sequenced the `FII-E-T-U-D` tail operon and mapped the amber mutation `Dam6` (C to T at nt 23592), which truncates the 388-codon reading frame to 267 aa (29.4 kDa), consistent with prior SDS-PAGE characterization of `Dam6` mutants.
   - Quotes:
     - `"Sequence analysis of the remainder of this operon and the locations of amber mutations Eam30, Tam5, Tam64, Tam215, Uam25, Uam77, Uam92, and Dam6 and missense mutation Ets55 identified the coding regions for genes E, T, U, and D, completing the sequence determination of the P2 genome."`
     - `"Overlapping the termination codon of gene U is a start codon for an open reading frame of 388 aa, encoding a protein with a molecular mass of 42.8 kDa. The D am 6 mutation (C to T at nt 23592) is in this reading frame and would generate a protein of 267 aa (29.4 kDa), consistent with the reported reduction in size ( 29 )."`
2. **PMID:24097944** (Maxwell et al., 2013, *J. Virol.*):
   - Summarizes comparative structural analyses demonstrating that P2 gpD is the central baseplate hub protein homologous to T4 gp27 (and Mu gp47/gp48).
   - Quote: `"Among the P2 baseplate constituents, gpD, the baseplate hub protein, and gpV, the tail spike protein, are homologues of the T4 proteins performing the same functions, gp27 and gp5, respectively ( 7 )."`
3. **PMID:22297511** (Leiman & Shneider, 2012, *Adv. Exp. Med. Biol.*):
   - Review of contractile tail machines identifying P2 gpD as the central baseplate hub protein bridging the central spike (`gpV`) and the tail tube (`gpFII`).

## Annotation Review Decisions
- `GO:0098025` (`virus tail, baseplate`, IEA): **ACCEPT** — gpD forms the central hub of the P2 baseplate.
- `GO:0098015` (`virus tail`, IEA): **MODIFY** to `GO:0098025` (`virus tail, baseplate`) for higher anatomical specificity.
- **NEW** `GO:0039660` (`structural constituent of virion`, IMP, `PMID:12426340`): gpD is an essential structural component of the virion tail baseplate hub.
- **NEW** `GO:0098003` (`viral tail assembly`, IMP, `PMID:12426340`): `D` amber mutants (`Dam6`) fail to assemble functional contractile tails.
