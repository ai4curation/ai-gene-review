# Curation Notes for Mup52 (P0DJY6) — Phage Mu Tail fiber protein S' (gpS' / gp52)

## Biological Summary
- **Gene / Protein**: `Mup52` (Gene name `S'`, Ordered locus name `Mup52`; UniProt `P0DJY6`, 328 aa annotated C-terminal segment or full chimeric protein `gpS'` / `gp52`). Note: `gene_symbol: Mup52` is retained per repository conventions.
- **Structure and Function**:
  - Receptor-binding tail fiber protein expressed when the invertible 3-kb G-segment of phage Mu is in the `G(-)` orientation (`PDB:8JU3`, `Pfam:PF12604` `gp37_C`, `InterPro:IPR022246` `Phage_T7_Gp17_C`).
  - Confers host specificity for bacterial strains such as *Citrobacter freundii*, *Shigella sonnei*, *Erwinia*, and *Escherichia coli* B/C by binding distinct cell-surface lipopolysaccharide (LPS) receptors (`file:BPMU/Mup52/Mup52-uniprot.txt`, "-!- FUNCTION: Component of the tail fiber that acts as a receptor binding protein. Binds to the primary receptor, thereby determining the host range. Two alternate tail fiber S and S' proteins are encoded extending the host range of the virus.").
  - Requires a tail fiber assembly chaperone (`U'` / `gp51` natively, or `U` / `gp50` in heterologous co-expression, [PMID:31504613]) to fold into soluble trimeric tail fibers.

## Annotation Decisions
- **ACCEPT**:
  - `GO:0098024` (`virus tail, fiber`): Forms the `G(-)` virion tail fiber ([PMID:31504613], `file:BPMU/Mup52/Mup52-uniprot.txt`).
  - `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`): Primary receptor-binding protein mediating attachment of `G(-)` phage Mu virions to susceptible host cells (`file:BPMU/Mup52/Mup52-uniprot.txt`, [PMID:31504613]).
- **KEEP_AS_NON_CORE**:
  - `GO:0030430` (`host cell cytoplasm`): Compartment of late protein synthesis and chaperone-assisted folding prior to virion assembly.
  - `GO:0098678` (`viral tropism switching`): S' (`Mup52`) is the `G(-)` receptor-binding effector produced upon Gin-mediated inversion of the G-segment (`file:BPMU/Mup52/Mup52-uniprot.txt`).
- **TOO_GENERAL**:
  - `GO:0098015` (`virus tail`): Entailed by `GO:0098024` (`virus tail, fiber`).
  - `GO:0019062` (`virion attachment to host cell`) and `GO:0046718` (`symbiont entry into host cell`): Broad ancestor processes entailed by `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`).
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, `enables`): Forms the structural tail fiber subunit of `G(-)` phage Mu virions ([PMID:31504613], `file:BPMU/Mup52/Mup52-uniprot.txt`).
