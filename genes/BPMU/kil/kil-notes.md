# Curation Notes for Escherichia phage Mu kil (P03046)

## Summary of Gene Function
- **Gene symbol**: `kil` (locus tag `Mup05`; UniProt `P03046`, Protein kil)
- **Organism**: *Escherichia phage Mu* (`NCBITaxon:2681603`)
- **Function**: Protein kil (`Mup05`, 74 aa) is an early non-essential accessory protein encoded immediately downstream of `B` in the early lytic transcript of bacteriophage Mu [file:BPMU/kil/kil-uniprot.txt]. Expression of `kil` in *Escherichia coli* induces pronounced morphological changes in the host cell, causing cells to become enlarged and predominantly spherical and leading to loss of cell viability [file:BPMU/kil/kil-uniprot.txt]. UniProt notes that these cell-shape perturbations may involve a direct or indirect interaction with the bacterial actin-like cytoskeletal protein MreB, although the precise molecular mechanism and direct binding partner of Mu Kil remain experimentally unverified (UniProt protein existence level `PE 2: Evidence at transcript level`) [file:BPMU/kil/kil-uniprot.txt].

## Annotation Review Decisions
- `GO:0030430` (`host cell cytoplasm`, IEA, `GO_REF:0000044`): `ACCEPT` (Kil acts inside the *E. coli* host cytoplasm).
- Following curation guidelines not to over-annotate or fabricate molecular functions unsupported by direct evidence, no molecular function is asserted (`core_functions: []`), and only the well-supported biological process `GO:0044071` (`symbiont-mediated perturbation of host cell cycle progression`, or keeping only the existing `GO:0030430` annotation) is considered. Because `kil-uniprot.txt` has `PE 2: Evidence at transcript level` and states `"Expression of the kil gene induces dramatic morphological changes in the host cell, which becomes enlarged and predominantly spherical and possibly dies. These changes might involved a direct or indirect interaction with host actin-like protein MreB"`, we keep the review conservative and grounded strictly in `file:BPMU/kil/kil-uniprot.txt`.
