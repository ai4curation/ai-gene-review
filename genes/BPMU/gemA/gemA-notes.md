# Curation Notes for Escherichia phage Mu gemA (Q38494)

## Summary of Gene Function
- **Gene symbol**: `gemA` (locus tag `Mup16`; UniProt `Q38494`, GemA protein)
- **Organism**: *Escherichia phage Mu* (`NCBITaxon:2681603`)
- **Function**: GemA (`Mup16`, 144 aa) is a homodimeric semi-early protein of bacteriophage Mu that acts in the bacterial host cytoplasm (`GO:0030430` `host cell cytoplasm`) to decrease host DNA gyrase activity and promote relaxation of the *Escherichia coli* chromosome [file:BPMU/gemA/gemA-uniprot.txt]. By altering bacterial DNA supercoiling, GemA modulates the transcription of supercoiling-sensitive host genes, including DNA replication and cell division determinants, thereby perturbing host cell cycle progression (`GO:0044071` `symbiont-mediated perturbation of host cell cycle progression`) [file:BPMU/gemA/gemA-uniprot.txt].

## Annotation Review Decisions
- `GO:0030430` (`host cell cytoplasm`, IEA): `ACCEPT`.
- `GO:0044071` (`symbiont-mediated perturbation of host cell cycle progression`, IEA): `ACCEPT`.
- Because the direct biochemical binding target or catalytic mechanism by which GemA decreases host DNA gyrase activity is not yet resolved at the molecular-function level in the available cached literature, `core_functions` is left empty (`core_functions: []`) rather than speculating on a molecular function term.
