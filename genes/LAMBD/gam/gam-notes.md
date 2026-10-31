# Curation Notes for Escherichia phage lambda `gam` (P03702)

## Summary of Gene Product
Bacteriophage lambda host-nuclease inhibitor protein Gam (`gam`, UniProt `P03702`, 138 AA) is a homodimeric double-stranded DNA mimic that binds directly to the *Escherichia coli* RecBCD helicase-nuclease complex and inhibits all of its enzymatic activities—including ATP-dependent dsDNA and ssDNA exonuclease, ATP-independent ssDNA endonuclease, and ATP-dependent DNA helicase activities [file:LAMBD/gam/gam-uniprot.txt; PMID:4275917; PMID:1653221; PMID:17544443]. By blocking RecBCD from binding linear duplex DNA ends, Gam protects linear concatameric lambda DNA intermediates generated during late rolling-circle replication from host RecBCD-mediated exonucleolytic degradation, enabling Red-mediated recombination and packaging of mature phage genomes [file:LAMBD/gam/gam-uniprot.txt; PMID:4275917; PMID:126236].

## Alternative Translation Initiation Products
- **GamL (`P03702-1`, 138 AA)**: Full-length isoform translated from the upstream AUG start codon [file:LAMBD/gam/gam-uniprot.txt].
- **GamS (`P03702-2`, 98 AA, lacking residues 1–40)**: Shorter isoform translated from an internal AUG at `Met41`; retains full homodimerization and RecBCD-inhibitory activity via molecular mimicry of B-form dsDNA (`PDB:1K4T`, `PDB:5MBV`) [file:LAMBD/gam/gam-uniprot.txt; PMID:17544443].

## Structural and Mechanistic Architecture
- **B-form dsDNA structural mimicry (`PDB:1K4T`, `PDB:5MBV`)**: The crystal structure of GamS (`PMID:17544443`) and cryo-EM structure of the GamS-RecBCD complex reveal an intertwined homodimer of alpha-helices presenting an array of surface acidic residues (`Asp` and `Glu`) whose spacing matches the phosphodiester backbone of B-form double-stranded DNA. Gam inserts directly into the DNA-binding channel of RecBCD without displacing any of the RecB, RecC, or RecD subunits, competitively sterically blocking DNA substrate entry [file:LAMBD/gam/gam-uniprot.txt; PMID:1653221; PMID:17544443].

## Review of Existing GO Annotations
- **`GO:0060703` (`deoxyribonuclease inhibitor activity`, 3 rows: IDA `PMID:4275917`, IEA `GO_REF:0000002`, IMP `PMID:4275917`)**: `ACCEPT` all three rows. Directly demonstrated with purified Gam protein and host RecBCD enzyme (`PMID:4275917`, `PMID:1653221`, `PMID:126236`, `PMID:17544443`).
- **`GO:0099016` (`symbiont-mediated evasion of DNA end degradation by host`, IEA `GO_REF:0000043`)**: `ACCEPT`. Exact biological process describing how lambda Gam protects linear viral DNA ends (specifically rolling-circle tails and double-strand breaks) from host RecBCD exonucleolytic degradation [file:LAMBD/gam/gam-uniprot.txt].
- **`GO:0052170` (`symbiont-mediated suppression of host innate immune response`, IEA `GO_REF:0000043`)** and **`GO:0052031` (`symbiont-mediated perturbation of host defense response`, IEA `GO_REF:0000043`)**: `TOO_GENERAL`. Both are broad host-defense perturbation terms from keyword mappings that are entailed by or less specific than `GO:0099016` (`symbiont-mediated evasion of DNA end degradation by host`).
