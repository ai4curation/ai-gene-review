# Curation Notes for Mup45 (Q9T1V4) — Phage Mu Baseplate puncturing device gp45 (Baseplate spike protein / gpQ)

## Biological Summary
- **Gene / Protein**: `Mup45` (UniProt `Q9T1V4`, 197 aa; also known as `gp45`, `gpQ`, or baseplate spike `BS`).
- **Structure and Function**:
  - Homotrimeric central needle-like baseplate spike (`PDB:3VTN`, `PDB:3VTO`, `PDB:9KI1`) with an intertwined beta-sheet, triple beta-helix, and a C-terminal metal-binding tip that coordinates 1 `Ca(2+)`, 1 `Fe` cation, and 1 `Cl(-)` ion per trimer (`file:BPMU/Mup45/Mup45-uniprot.txt`).
  - Punctures the host cell envelope during contractile tail sheath contraction, serves as the distal plug of the tail tube channel, and requires the bound `Ca(2+)` ion (coordinated by Asp-188) for host membrane interaction (`FT   MUTAGEN 188: D->A: Loss of membrane-binding ability.`).
  - In [PMID:27555589], `Mup45` (`BS`) was shown to associate weakly with the Mup43/44/46/47/48 baseplate complex (requiring chemical cross-linking to be co-isolated in vitro), though in vivo amber mutations in gene 45 abolish tail synthesis (`-!- DISRUPTION PHENOTYPE: No tail is synthesized.`).

## Annotation Decisions
- **ACCEPT**:
  - `GO:0046872` (`metal ion binding`): Binds 1 Ca(2+) and 1 Fe cation per homotrimer at the C-terminal spike tip; Ca(2+) is required for host cell membrane binding (`file:BPMU/Mup45/Mup45-uniprot.txt`).
  - `GO:0098025` (`virus tail, baseplate`): Central spike component of the phage Mu baseplate ([PMID:27555589]; `PDB:9KI1`).
  - `GO:0098003` (`viral tail assembly`): Amber mutants in gene 45 synthesize no tail in vivo (`file:BPMU/Mup45/Mup45-uniprot.txt`).
  - `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`): Central needle-like spike that punctures the host cell membrane during contractile tail entry.
- **KEEP_AS_NON_CORE**:
  - `GO:0030430` (`host cell cytoplasm`): Site of synthesis in the infected host cell prior to virion assembly.
- **TOO_GENERAL**:
  - `GO:0098015` (`virus tail`): Entailed by `GO:0098025` (`virus tail, baseplate`).
  - `GO:0046718` (`symbiont entry into host cell`): Entailed by `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`).
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, `enables`): Forms the homotrimeric central needle-like spike of the phage Mu virion baseplate ([PMID:27555589], `file:BPMU/Mup45/Mup45-uniprot.txt`).
