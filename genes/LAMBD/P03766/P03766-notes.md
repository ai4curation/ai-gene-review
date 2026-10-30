# Curation Notes for Escherichia phage lambda `P03766` (ORF290 / ninC)

## Summary of Gene Product
Bacteriophage lambda uncharacterized `nin` region protein `ORF290` (`P03766`, also known as `ninC`, `Y290_LAMBD`, 290 AA) is an early-expressed protein encoded in the `ninR` region between `ninB` and `ninF` on the rightward `pR` transcript [file:LAMBD/P03766/P03766-uniprot.txt]. Sequence and structural domain analyses (`InterPro:IPR002500` `PAPS_reduct_dom`, `InterPro:IPR014729` `Rossmann-like_a/b/a_fold`, `Pfam:PF01507` `PAPS_reduct` covering residues 67–252) show that ORF290 contains a Rossmann-like alpha/beta/alpha catalytic domain homologous to the PAPS reductase / PP-loop ATP pyrophosphatase / DNA-modification enzyme superfamily [file:LAMBD/P03766/P03766-uniprot.txt].

## Structural and Mechanistic Architecture
- **Rossmann-like PAPS reductase / PP-loop superfamily fold (`InterPro:IPR002500`, `InterPro:IPR014729`)**: Residues 67–252 adopt a conserved Rossmann-like nucleotide-binding fold found in 3'-phosphoadenosine-5'-phosphosulfate (PAPS) reductases, tRNA/DNA sulfur- or methyl-modifying enzymes, and phage-encoded nucleotide/DNA-modifying enzymes [file:LAMBD/P03766/P03766-uniprot.txt]. Its exact physiological substrate in lambda-infected *E. coli* has not yet been experimentally determined.

## Review of Existing GO Annotations
- **`GO:0003824` (`catalytic activity`, IEA `GO_REF:0000002` via `InterPro:IPR002500`)**: `ACCEPT`. Because `P03766` (`ORF290`) has not been biochemically assayed for a specific substrate reaction in phage lambda, `GO:0003824` (`catalytic activity`) inferred from the conserved `PAPS_reduct_dom` enzymatic domain (`InterPro:IPR002500`) is as specific as currently warranted by the evidence [file:LAMBD/P03766/P03766-uniprot.txt].
