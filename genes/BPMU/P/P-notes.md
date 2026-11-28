# Curation Notes for P (P08558) — Phage Mu Baseplate hub protein gp44 (Mup44 / BH2)

## Biological Summary
- **Gene / Protein**: `P` (Ordered locus name `Mup44`; UniProt `P08558`, 380 aa; also known as `gp44` or `BH2`).
- **Structure and Function**:
  - Structural homolog of phage T4 gp27 (`PDB:1WRU`, `PDB:9KI1`, `InterPro:IPR013047`). Forms a ring-shaped trimeric central hub (inner diameter ~25 Å) that serves as a conduit extending the tail tube channel for viral DNA release during contractile tail ejection (`file:BPMU/P/P-uniprot.txt`, "-!- FUNCTION: Forms the central cylindrical hub of the baseplate and plays an important role in baseplate and tail assembly (Probable). Core component of the initiator complex that triggers the tail tube polymerization during tail assembly (Probable). Forms a conduit that probably functions as an extension of the tail tube allowing viral DNA release during ejection.").
  - In [PMID:27555589], `Mup44` (`BH2`) and `Mup43` (`N` / `BH1`) assemble at a 3:3 stoichiometry to form the central hub of the phage Mu baseplate before recruiting three dimeric `Mup46`/`Mup47`/`Mup48` baseplate wedges (3:3:6:6:6 ratio).

## Annotation Decisions
- **ACCEPT**:
  - `GO:0098025` (`virus tail, baseplate`): Core subcellular localization as the central cylindrical hub of the baseplate ([PMID:27555589]).
  - `GO:0098003` (`viral tail assembly`): Essential baseplate hub component required for baseplate and tail assembly ([PMID:27555589]).
  - `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`): Forms the 25-Å central cylindrical conduit extending the tail tube channel through which viral DNA passes during ejection.
- **KEEP_AS_NON_CORE**:
  - `GO:0030430` (`host cell cytoplasm`): Site of synthesis and pre-virion assembly in the infected bacterium.
- **TOO_GENERAL**:
  - `GO:0098015` (`virus tail`): Entailed by the more specific accepted component term `GO:0098025` (`virus tail, baseplate`).
  - `GO:0046718` (`symbiont entry into host cell`): Entailed by the more specific accepted process term `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`).
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, `enables`): Directly supported by [PMID:27555589] and crystal/cryo-EM structures showing `Mup44` (`P`) is the core cylindrical hub subunit of the phage Mu baseplate.
