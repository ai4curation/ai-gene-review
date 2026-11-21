# FS-gp41 (P0DJY4) — Probable tail assembly protein FS-gp41

## Summary
- **UniProt**: `P0DJY4` (`TACF_BPMU`), 188 aa, gene `FS-gp41`, locus tag `Mup41`.
- **Function**: Extended tail assembly chaperone isoform (`P0DJY4-1`, analogous to phage lambda gpGT) produced via a programmed -2 ribosomal frameshift at residue 136 during translation of the `Mup41` mRNA ([PMID:15469818](../../../publications/PMID_15469818.md); [file:BPMU/FS-gp41/FS-gp41-uniprot.txt](FS-gp41-uniprot.txt)). Together with conventionally translated gp41 (`P79680`), FS-gp41 acts as a chaperone that bridges the tape measure protein (gp42) and the tail tube protein (gpM / gp40) to assemble a functional tail shaft in the host cytoplasm ([file:BPMU/FS-gp41/FS-gp41-uniprot.txt](FS-gp41-uniprot.txt)).

## Key References
- **PMID:15469818**: Xu, Hendrix & Duda (2004), *J. Mol. Biol.* — "Conserved translational frameshift in dsDNA bacteriophage tail assembly genes." Identifies the conserved programmed -2 translational frameshift in phage Mu that produces the overlapping tail assembly chaperones gp41 and FS-gp41.
- **file:BPMU/FS-gp41/FS-gp41-uniprot.txt**: Swiss-Prot record documenting -2 ribosomal frameshift biogenesis (`FT TRANS_REG 136`), host cytoplasm localization, and co-chaperone function with gp41 in tail shaft assembly.

## Annotation Decisions
- `GO:0098003` (`viral tail assembly`, IEA, `GO_REF:0000043`): **ACCEPT** — core biological process of FS-gp41 as a tail assembly chaperone.
- `GO:0030430` (`host cell cytoplasm`, IEA, `GO_REF:0000044`): **ACCEPT** — functions as a cytosolic chaperone during viral tail assembly inside the host bacterium.
- `GO:0075523` (`viral translational frameshifting`, IEA, `GO_REF:0000043`): **REMOVE** — automatic mapping from UniProt keyword `KW-0688` (`Ribosomal frameshifting`). FS-gp41 is the protein *product* generated when host ribosomes undergo a -2 frameshift on the `Mup41` mRNA; the FS-gp41 protein itself does not execute or regulate translational frameshifting.
