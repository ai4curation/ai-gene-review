# Curation Notes for Escherichia phage lambda Gene tfa (gpTfa, P03740)

## Summary of Gene Product Function
Gene `tfa` encodes the tail fiber assembly protein gpTfa (UniProt: `P03740`, 194 aa, ~22.1 kDa), a dedicated molecular chaperone located immediately downstream of `stf` in the bacteriophage lambda genome that facilitates the folding, trimerization, and assembly of the long jointed side tail fibers (`gpStf`) (`PMID:1439823`, `file:LAMBD/tfa/tfa-uniprot.txt`). Homologous to bacteriophage P2 `gpG`, Mu `gpU`, and T4 `gp38` tail fiber assembly chaperones, gpTfa is required to produce functional side tail fibers in `Ur-lambda` (and in `lambda PaPa`, where `tfa` remains intact even though upstream `stf` is disrupted by a laboratory frameshift mutation) (`PMID:1439823`).

## Literature & Structural Evidence
- **Role in Ur-lambda side tail fiber assembly (`PMID:1439823`, UniProt `P03740`)**: Hendrix & Duda (1992) identified `gpTfa` alongside `gpStf` as the two proteins required for the formation of the thin, jointed side tail fibers of `Ur-lambda`, with `gpTfa` implicated in facilitating tail fiber assembly by homology to T4 `gp38` / Mu `gpU` (`PMID:2960666` cited in UniProt `P03740`) [PMID:1439823, "The Ur-lambda virions have thin, jointed tail fibers that are absent from lambda wild type. Two novel proteins of Ur-lambda constitute the fibers: the product of stf, the gene that is disrupted in lambda wild type by the frameshift mutation, and the product of gene tfa, a protein that is implicated in facilitating tail fiber assembly."; file:LAMBD/tfa/tfa-uniprot.txt, "CC   -!- FUNCTION: Chaperone that acts in assembly of the long tail fibers.\nCC       {ECO:0000269|PubMed:2960666}."].

## Review of Existing GO Annotations
- `GO:0098004` (`virus tail fiber assembly`, `IEA` from `GO_REF:0000043`): **ACCEPT**. gpTfa is the dedicated chaperone for assembly of the bacteriophage lambda side tail fibers (`gpStf`).
- `GO:0098003` (`viral tail assembly`, `IEA` from `GO_REF:0000043`): **MODIFY** to `GO:0098004` (`virus tail fiber assembly`), which is a more specific child term (`GO:0098004 is_a GO:0098003`) already annotated to this gene.
