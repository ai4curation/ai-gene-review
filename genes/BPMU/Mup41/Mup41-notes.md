# Mup41 (P79680) — Probable tail assembly protein gp41

## Summary
- **UniProt**: `P79680` (`TAC_BPMU`), 144 aa, locus tag `Mup41`, synonym `N` (or `G`-like chaperone).
- **Function**: Tail assembly chaperone produced by conventional translation of `Mup41` mRNA (`P79680-1`), whereas a programmed -2 ribosomal frameshift within `Mup41` produces the extended isoform `FS-gp41` (`P0DJY4-1`, analogous to phage lambda gpG/gpGT) ([PMID:15469818](../../../publications/PMID_15469818.md); [file:BPMU/Mup41/Mup41-uniprot.txt](Mup41-uniprot.txt)). Together with FS-gp41, gp41 acts as a cytosolic tail assembly chaperone that coats the tape measure protein (gp42) and recruits the tail tube protein (gpM / gp40) to promote polymerization of a tail shaft of the proper length ([file:BPMU/Mup41/Mup41-uniprot.txt](Mup41-uniprot.txt)).

## Key References
- **PMID:15469818**: Xu, Hendrix & Duda (2004), *J. Mol. Biol.* — "Conserved translational frameshift in dsDNA bacteriophage tail assembly genes." Demonstrates that dsDNA phage tail assembly chaperone genes lying between the major tail shaft subunit and the tape measure gene utilize a conserved programmed translational frameshift (specifically an unusual -2 frameshift in phage Mu) to produce two overlapping proteins (gp41 and FS-gp41) required for tail assembly.
- **file:BPMU/Mup41/Mup41-uniprot.txt**: Swiss-Prot record documenting conventional translation of isoform gp41, programmed ribosomal frameshifting to produce FS-gp41, and the chaperone role in mediating TMP–TTP interaction during tail assembly in the host cytoplasm.

## Annotation Decisions
- `GO:0098003` (`viral tail assembly`, IEA, `GO_REF:0000043`): **ACCEPT** — core biological process of gp41 as a tail assembly chaperone.
- `GO:0030430` (`host cell cytoplasm`, IEA, `GO_REF:0000044`): **ACCEPT** — as a non-structural assembly chaperone not incorporated into the mature virion, gp41 functions in the host cell cytoplasm.
- `GO:0075523` (`viral translational frameshifting`, IEA, `GO_REF:0000043`): **REMOVE** — mapped from UniProt keyword `KW-0688` (`Ribosomal frameshifting`), which describes how the `Mup41` transcript is translated by the host ribosome to yield `FS-gp41`. Per GO guidelines, a gene product is `involved_in` a process only if the protein itself performs part of that process; gp41 is a translation product and tail assembly chaperone, not a factor that catalyzes or regulates ribosomal frameshifting.
