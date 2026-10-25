# BPP2 X (P51772 / BPX_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `X`
- **UniProt ID**: `P51772` (`BPX_BPP2`)
- **Protein**: Baseplate protein X / gpX (67 aa, 7.3 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:8051010** (Ziermann et al., 1994, *J. Bacteriol.*):
   - Identified and sequenced P2 gene `X` (`gpX`, 67 aa) located at the 5' end of the `X-Y-K-lysA-lysB-R-S` operon and showed via complementation that `gpX` is an essential tail gene.
   - Quote: `"It also provides a previously missing function that is essential for synthesis of P2 tails and has been designated gene X."`
2. **PMID:24097944** (Maxwell et al., 2013, *J. Virol.*):
   - Solved the NMR solution structure of `gpX` (showing a LysM-like αββαβ fold), tested peptidoglycan binding (finding that monomeric `gpX` does not bind peptidoglycan in vitro), and used electron microscopy of `MBP-gpX` fusion virions to localize `gpX` to the top of the baseplate near the baseplate-tail tube junction (adjacent to `gpW`).
   - Showed that `Xam` mutant lysates contain an abundance of DNA-filled free heads but no mature virions or tail-like structures, demonstrating that `gpX` acts early in tail assembly prior to tail tube and sheath polymerization.
   - Quotes:
     - `"Electron microscopy of P2 phage particles with an incorporated gpX-maltose binding protein fusion revealed that gpX is located at the top of the baseplate, near the junction of the baseplate and tail tube."`
     - `"An abundance of DNA-filled free heads were observed in these lysates, but no mature viral particles or tail-like particles were found (data not shown). These data imply that the activity of gpX in tail assembly takes place early in the process, before tail tube and tail sheath polymerization."`
     - `"These results indicate that purified monomeric gpX does not bind to peptidoglycan under these assay conditions."`

## Annotation Review Decisions
- `GO:0098015` (`virus tail`, IEA): **MODIFY** to `GO:0098025` (`virus tail, baseplate`).
- `GO:0098025` (`virus tail, baseplate`, IDA `PMID:24097944` & IEA `GO_REF:0000043`): **ACCEPT** — EM of `MBP-gpX` virions directly localized `gpX` to the top of the P2 baseplate.
- **NEW** `GO:0039660` (`structural constituent of virion`, IDA, `PMID:24097944`): EM of `MBP-gpX`-incorporated virions directly demonstrates that `gpX` is a structural component of the mature P2 baseplate.
- **NEW** `GO:0098003` (`viral tail assembly`, IMP, `PMID:24097944`): `Xam` mutant lysates contain DNA-filled heads but no tail-like structures, proving `gpX` is essential for early tail morphogenesis (`PMID:8051010`, `PMID:24097944`).
