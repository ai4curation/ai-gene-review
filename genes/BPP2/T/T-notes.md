# BPP2 T (O64314 / TMP_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `T`
- **UniProt ID**: `O64314` (`TMP_BPP2`)
- **Protein**: Probable tape measure protein gpT (815 aa, 86.4 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:12426340** (Christie et al., 2002, *J. Bacteriol.*):
   - Sequenced P2 gene `T` (815 aa, 86.4 kDa) in the `FI-FII-E-T-U-D` tail operon and mapped amber mutations `Tam5`, `Tam64`, and `Tam215`.
   - Demonstrated that `gpT` is preceded by the `E/E'` programmed -1 frameshift chaperone pair and is the only P2 tail protein large enough to span the 135-nm length of the P2 tail shaft, establishing `gpT` as the tail length tape measure protein.
   - Quotes:
     - `"Sequence analysis of the remainder of this operon and the locations of amber mutations Eam30, Tam5, Tam64, Tam215, Uam25, Uam77, Uam92, and Dam6 and missense mutation Ets55 identified the coding regions for genes E, T, U, and D, completing the sequence determination of the P2 genome."`
     - `"The most likely role for gpT is that of tail length determination. It is the only P2 tail protein that is large enough to span the length of the P2 tail shaft."`
     - `"The T open reading frame is preceded by a pair of overlapping reading frames that resemble those between the major tail protein and the tape measure protein in bacteriophage λ ( 25 ) and many other phages with contractile or noncontractile tails ( 44 )."`

## Annotation Review Decisions
- `GO:0098003` (`viral tail assembly`, IEA): **ACCEPT** — `gpT` serves as the scaffold and molecular ruler for tail tube (`gpFII`) polymerization and tail length determination.
- **NEW** `GO:0039660` (`structural constituent of virion`, IDA, `PMID:12426340`): `gpT` (~90 kDa) is a structural component residing within the central lumen of the mature P2 tail shaft.
- **NEW** `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`, IMP, `PMID:12426340`): During contractile tail infection, the tape measure protein is ejected from the tail tube lumen into the host cell envelope ahead of viral DNA to facilitate channel formation and genome delivery.
- **NEW** `GO:0098015` (`virus tail`, IDA, `PMID:12426340`): `gpT` spans the central lumen of the virion tail shaft.
