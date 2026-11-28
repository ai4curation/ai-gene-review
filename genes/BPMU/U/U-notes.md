# Curation Notes for U (Q9T1U9) — Phage Mu Tail fiber assembly protein U (Mup50 / gp50 / gpU)

## Biological Summary
- **Gene / Protein**: `U` (Ordered locus name `Mup50`; UniProt `Q9T1U9`, 175 aa; also designated `gp50` or `gpU`).
- **Structure and Function**:
  - Tail fiber assembly protein / dedicated molecular chaperone (`PDB:5YVQ`, `Pfam:PF02413` `Caudo_TAP`, `InterPro:IPR003458` `Phage_T4_Gp38_tail_assem`) expressed in the `G(+)` orientation of the invertible G-segment downstream of gene `S` (`Mup49`).
  - Essential for folding and trimerization of the tail fiber subunit `S` (`gp49`) into soluble, baseplate-competent tail fibers ([PMID:27555589], [PMID:31504613]).
  - Remarkably, [PMID:31504613] demonstrated that `U` (`gp50`) and `U'` (`gp51` / `Mup51`) are functionally interchangeable (fungible) in vitro: `gp50` can also bind and fold the alternate tail fiber subunit `S'` (`gp52` / `Mup52`) into a stable `gp52`-`gp50` complex (`"However, heterologous overexpression results for gp49 or gp52 (tail fibre subunit) together with gp51 and gp50, respectively, were also effective in producing soluble Mu tail fibres. Moreover, we successfully purified non-native gp49-gp51 and gp52-gp50 complexes. These facts showed that gp50 and gp51 were fungible and functional for both gp49 and gp52 each other."`).
  - Remains associated with the assembled tail fiber and participates in host receptor binding (`file:BPMU/U/U-uniprot.txt`, "-!- FUNCTION: Chaperone involved in tail fiber assembly. Remains associated to the tail fiber and participates in the host receptor binding. Binds to the primary receptor (Probable). Two alternate tail fiber assembly proteins U and U' are encoded extending the host range of the virus.").

## Annotation Decisions
- **ACCEPT**:
  - `GO:0044183` (`protein folding chaperone`): Experimentally demonstrated molecular chaperone activity required to fold tail fiber subunits into soluble fibers ([PMID:31504613]).
  - `GO:0006457` (`protein folding`): Directly involved in folding the tail fiber protein S ([PMID:31504613]).
  - `GO:0098004` (`virus tail fiber assembly`): Essential for assembling functional tail fibers ([PMID:27555589], [PMID:31504613], `file:BPMU/U/U-uniprot.txt`).
  - `GO:0030430` (`host cell cytoplasm`): Compartment where U folds nascent tail fiber subunits during late lytic infection.
  - `GO:0098024` (`virus tail, fiber`): Remains stably associated with the tail fiber (`gp49`-`gp50` complex, [PMID:31504613], `file:BPMU/U/U-uniprot.txt`).
- **KEEP_AS_NON_CORE**:
  - `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`): Participates alongside S in tail-fiber-mediated host receptor binding (`file:BPMU/U/U-uniprot.txt`).
  - `GO:0098678` (`viral tropism switching`): Co-switched with S as part of the G(+) vs G(-) bicistronic operon (`S-U` vs `S'-U'`), although the DNA inversion is catalyzed by Gin (`P03015`).
- **TOO_GENERAL**:
  - `GO:0098003` (`viral tail assembly`): Entailed by the more specific accepted annotation `GO:0098004` (`virus tail fiber assembly`).
  - `GO:0098015` (`virus tail`): Entailed by `GO:0098024` (`virus tail, fiber`).
  - `GO:0019062` (`virion attachment to host cell`) and `GO:0046718` (`symbiont entry into host cell`): Broad ancestor processes entailed by `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`).
