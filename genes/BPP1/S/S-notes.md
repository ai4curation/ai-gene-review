# S (P22588) Curation Notes — Escherichia phage P1

## Functional Summary
- **Gene symbol**: `S` (second gene of the late `R-S-U` tail-fiber operon, transcribed from `LP_S`).
- **Protein**: Tail fiber protein S (`gpS`, `Sc-Sv` isoform in C(+) orientation; 980 aa, ~104.2 kDa) [PMID:2526777, PMID:15489417].
- **Biological role & C-segment inversion**:
  - `gpS` is the major structural protein of the six P1 tail fibers (`GO:0098024` `virus tail, fiber`) and mediates host receptor recognition (`GO:0019062` `virion attachment to host cell`) [PMID:2526777, PMID:15489417, PMID:35458408].
  - Its constant N-terminal region (`Sc`, residues 1–609, encoded outside the invertible C-segment) anchors the tail fiber to the baseplate, while its variable C-terminal region (`Sv` or `S'v`, residues 610–980, encoded within the 4.2-kb Cin-invertible C-segment) forms the distal receptor-binding tip that recognizes specific lipopolysaccharide (LPS) core structures on the bacterial host surface [PMID:6327269, PMID:2526777, PMID:1534556, PMID:15489417].
  - Site-specific DNA inversion of the C-segment by the Cin recombinase switches the C-terminal coding region of `S` in-frame between `Sv` (co-transcribed with assembly chaperone `U`, enabling infection of *E. coli* K-12 and C strains) and `S'v` (co-transcribed with assembly chaperone `U'`, conferring an alternative host range) [PMID:6327269, PMID:2526777, PMID:15489417].
  - LC-MS/MS proteomics of CsCl-purified P1 virions confirmed `gpS` as a structural tail fiber component [PMID:35458408].

## Review of Existing GOA Annotations
- `GO:0019062` (`virion attachment to host cell`, IEA, `GO_REF:0000043`): **ACCEPT**. Core function of the gpS tail fiber, whose C-terminal receptor-binding region binds the bacterial cell surface LPS receptor [PMID:2526777, PMID:15489417].
- `GO:0046718` (`symbiont entry into host cell`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by `GO:0019062` (`virion attachment to host cell`, which is `part_of` `GO:0046718`).
- `GO:0098015` (`virus tail`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by the more specific component annotation `GO:0098024` (`virus tail, fiber`, which is `part_of` `GO:0098015`).
- `GO:0098024` (`virus tail, fiber`, IEA, `GO_REF:0000044`): **ACCEPT**. `gpS` is the major structural subunit of the P1 tail fiber [PMID:2526777, PMID:15489417, PMID:35458408].
