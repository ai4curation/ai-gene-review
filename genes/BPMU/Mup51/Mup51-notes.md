# Curation Notes for Mup51 (P0DJY5) — Phage Mu Tail fiber assembly protein U' (gpU' / gp51)

## Biological Summary
- **Gene / Protein**: `Mup51` (Gene name `U'`, Ordered locus name `Mup51`; UniProt `P0DJY5`, 177 aa; also designated `gpU'` or `gp51`). Note: `gene_symbol: Mup51` is retained per repository conventions to avoid apostrophe path issues.
- **Structure and Function**:
  - Tail fiber assembly protein / molecular chaperone (`Pfam:PF02413` `Caudo_TAP`, `InterPro:IPR003458` `Phage_T4_Gp38_tail_assem`) encoded within the invertible 3-kb G-segment and expressed when the G-segment is in the `G(-)` orientation downstream of `S'` (`Mup52`).
  - Folds and solubilizes the `G(-)` tail fiber subunit `S'` (`gp52` / `Mup52`) and is also functionally interchangeable with `U` (`gp50`) in vitro, forming soluble `gp49`-`gp51` as well as `gp52`-`gp51` complexes ([PMID:31504613]).
  - Remains associated with the assembled tail fiber (`file:BPMU/Mup51/Mup51-uniprot.txt`, "-!- FUNCTION: Chaperone involved in tail fiber assembly. Remains associated to the tail fiber and participates in the host receptor binding. Binds to the primary receptor (Probable). Two alternate tail fiber assembly proteins U and U' are encoded extending the host range of the virus.").

## Annotation Decisions
- **ACCEPT**:
  - `GO:0044183` (`protein folding chaperone`): Experimentally demonstrated molecular chaperone activity for folding Mu tail fiber subunits (`gp52` and `gp49`, [PMID:31504613]).
  - `GO:0006457` (`protein folding`): Directly involved in folding tail fiber subunits into soluble complexes ([PMID:31504613]).
  - `GO:0098004` (`virus tail fiber assembly`): Required for folding and assembling functional `G(-)` tail fibers ([PMID:31504613], `file:BPMU/Mup51/Mup51-uniprot.txt`).
  - `GO:0030430` (`host cell cytoplasm`): Compartment where U' folds nascent tail fiber subunits during late lytic infection.
  - `GO:0098024` (`virus tail, fiber`): Remains stably associated with the tail fiber ([PMID:31504613], `file:BPMU/Mup51/Mup51-uniprot.txt`).
- **KEEP_AS_NON_CORE**:
  - `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`): Remains associated with the tail fiber and participates in host receptor binding (`file:BPMU/Mup51/Mup51-uniprot.txt`).
  - `GO:0098678` (`viral tropism switching`): Co-expressed with `S'` in the `G(-)` orientation of the Gin-invertible G-segment.
- **TOO_GENERAL**:
  - `GO:0098003` (`viral tail assembly`): Entailed by `GO:0098004` (`virus tail fiber assembly`).
  - `GO:0098015` (`virus tail`): Entailed by `GO:0098024` (`virus tail, fiber`).
  - `GO:0019062` (`virion attachment to host cell`) and `GO:0046718` (`symbiont entry into host cell`): Broad ancestor processes entailed by `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`).
