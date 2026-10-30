# BPP2 W (P51768 / BPW_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `W`
- **UniProt ID**: `P51768` (`BPW_BPP2`)
- **Protein**: Baseplate protein W / gpW (115 aa, 12.8 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:7483254** (Haggård-Ljungquist et al., 1995, *Virology*):
   - Sequenced P2 gene `W` (located between `V` and `J` in the `V-W-J-I-H-G` tail operon) and demonstrated that `W` is an essential tail gene.
   - Quote: `"The sequences of two previously defined tail genes, V and J, of the temperate bacteriophage P2, and those of two new essential tail genes, W and I, were determined."`
2. **PMID:24097944** (Maxwell et al., 2013, *J. Virol.*):
   - Demonstrated that `gpW` is an orthologue of the bacteriophage T4 baseplate wedge subunit `gp25` (the sheath initiator / inner baseplate component).
   - Using electron microscopy of P2 virions incorporating an `MBP-gpW` fusion protein, localized `gpW` to the top of the baseplate near the baseplate-tail tube/sheath junction (adjacent to `gpX`), and showed that `Wam` mutant lysates contain DNA-filled heads but no tail-related structures.
   - Quote: `"Like the P2 particles that incorporated MBP-gpX fusion protein, particles bearing the MBP-gpW fusion also displayed a region of extra density near the baseplate-tail tube junction ( Fig. 1 ). These data imply that gpW and gpX are located near each other in the baseplate structure. Like the Xam phage, lysates of cells infected with a P2 Wam phage contained filled heads but no tail-related structures (data not shown)."`

## Annotation Review Decisions
- `GO:0098003` (`viral tail assembly`, IEA): **ACCEPT** — `Wam` mutant lysates lack any tail-related structures (`PMID:24097944`).
- `GO:0098015` (`virus tail`, IEA): **MODIFY** to `GO:0098025` (`virus tail, baseplate`).
- `GO:0098025` (`virus tail, baseplate`, IDA `PMID:24097944` & IEA `GO_REF:0000043`): **ACCEPT** — EM of `MBP-gpW` virions directly localized `gpW` to the top of the P2 baseplate.
- **NEW** `GO:0039660` (`structural constituent of virion`, IDA, `PMID:24097944`): EM of `MBP-gpW`-labeled virions directly demonstrates that `gpW` is a structural subunit of the P2 virion baseplate.
