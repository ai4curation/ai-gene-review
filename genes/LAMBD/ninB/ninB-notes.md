# Curation Notes for Escherichia phage lambda `ninB` (P03765)

## Summary of Gene Product
Bacteriophage lambda recombination protein NinB (`ninB`, also known as `orf` or `ORF146`, UniProt `P03765`, 146 AA, `InterPro:IPR008711` `Recombinase_NinB`) is a homodimeric functional analog of the *Escherichia coli* RecF, RecO, and RecR recombination mediator complex (`RecFOR`) encoded within the `ninR` region between genes `P` and `Q` [file:LAMBD/ninB/ninB-uniprot.txt]. During phage recombination via the host RecBC-independent (`RecF`) or phage Red pathways, NinB (Orf) functions as a recombination mediator that binds single-stranded DNA (`GO:0003697`) and interacts with *E. coli* single-stranded DNA-binding protein (`SSB`), facilitating the loading of recombinases onto SSB-coated single-stranded DNA gaps and overhangs (`GO:0006310`, `DNA recombination`).

## Structural and Mechanistic Architecture
- **Asymmetric homodimer with central ssDNA-binding channel (`PDB:1PC6`)**: The 2.51-A X-ray crystal structure of lambda NinB (`PDB:1PC6`, residues 1–146) [file:LAMBD/ninB/ninB-uniprot.txt] reveals a crescent-shaped homodimer (`InterPro:IPR008711`) with a positively charged central groove that binds single-stranded DNA preferentially over double-stranded DNA, flanked by C-terminal alpha-helices involved in host SSB interaction.

## Review of Existing GO Annotations
- `existing_annotations` is currently empty (`[]`) in GOA for `P03765`.
- **Core function**: `GO:0003697` (`single-stranded DNA binding`) directly involved in `GO:0006310` (`DNA recombination`), supported by its structural and domain characterization (`PDB:1PC6`, `InterPro:IPR008711`) in the UniProt record [file:LAMBD/ninB/ninB-uniprot.txt].
