# darA (O21970) Curation Notes — Escherichia phage P1

## Functional Summary
- **Gene symbol**: `darA` (fourth gene of the late `LP_dar` operon: `lydA-lydB-hdf-darA-ddrA-ddrB-ulx`).
- **Protein**: Defense against restriction protein A (`DarA`; synthesized as a 629-aa, ~69.6 kDa precursor and proteolytically processed during head maturation by the `pro` morphogenetic protease function into a ~68 kDa / 47.5 kDa mature head protein and an N-terminal ~9 kDa peptide) [PMID:3029954, PMID:3029955, PMID:15489417, PMID:35458408].
- **Biological role**:
  - **Antirestriction (`GO:0099018` `symbiont-mediated evasion of host restriction-modification system`)**: Packaged in high copy number into the P1 capsid (`GO:0019028` `viral capsid`) and co-ejected with the phage DNA into the host cell upon infection, where it acts in *cis* to protect P1 and transduced DNA against host Type I restriction-modification systems (`EcoA`, `EcoB`, `EcoK`) by occluding restriction sites on injected DNA [PMID:3029954, PMID:15489417, PMID:28509398].
  - **Capsid morphogenesis (`GO:0019069` `viral capsid assembly`)**: Together with `DdrA` and `Hdf`, `DarA` plays a direct structural role in formatting the P1 capsid, controlling the proportion of normal big-headed (`P1B`) versus small-headed (`P1S`) virions, and recruiting the remaining injectable Dar system proteins (`DarB`, `DdrB`, `Ulx`) into the procapsid via an N-terminal capsid-targeting sequence [PMID:28509398, PMID:35458408].

## Review of Existing GOA Annotations
- `GO:0019028` (`viral capsid`, IEA, `GO_REF:0000043` and `GO_REF:0000044`): **ACCEPT**. Mature proteolytically processed DarA is an abundant internal protein of the P1 head (~320–400 copies per capsid) [PMID:3029954, PMID:3029955, PMID:15489417, PMID:28509398].
- `GO:0019069` (`viral capsid assembly`, IEA, `GO_REF:0000043`): **ACCEPT**. Deletion of `darA` alters the ratio of big (`P1B`) and small (`P1S`) capsid morphotypes and abolishes packaging of `DarB`, `DdrB`, and `Ulx` into the head [PMID:28509398].
- `GO:0052031` (`modulation by symbiont of host process`, IEA, `GO_REF:0000119`): **TOO_GENERAL**. Entailed by `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`).
- `GO:0052170` (`symbiont-mediated suppression of host innate immune response`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by the more specific child term `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`) present on this gene.
- `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`, IEA, `GO_REF:0000043`): **ACCEPT**. Core function of DarA in protecting injected viral or transduced DNA against host Type I restriction endonucleases (`EcoA`, `EcoB`, `EcoK`) [PMID:3029954, PMID:15489417, PMID:28509398].
