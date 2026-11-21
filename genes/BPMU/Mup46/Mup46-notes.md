# Curation Notes for Mup46 (Q9T1V3) — Phage Mu Baseplate protein gp46 (BW1 / gpV)

## Biological Summary
- **Gene / Protein**: `Mup46` (UniProt `Q9T1V3`, 145 aa; also designated `gp46`, `gpV`, or baseplate wedge protein 1 `BW1` in [PMID:27555589]).
- **Structure and Function**:
  - Homolog of phage T4 gp25 (`BW1`). Essential subunit of the phage Mu baseplate wedge (`Mup46`/`Mup47`/`Mup48`, i.e. `BW1`/`BW2`/`BW3`).
  - As shown by [PMID:27555589], `Mup47` (`BW2`) and `Mup48` (`BW3`) first interact to form an intermediate complex, followed by addition of `Mup46` (`BW1`) to complete the baseplate wedge (`Mup46`/`47`/`48` dimer of trimers, 6 copies of each per baseplate). Three dimeric wedges then dock onto the central `Mup43`/`Mup44` (`N`/`P`) hub at a 3:3:6:6:6 stoichiometry (`PDB:9KI1`).
  - Acts as the connector between the baseplate hub/wedge and the contractile tail sheath and is required for tail assembly (`file:BPMU/Mup46/Mup46-uniprot.txt`, "-!- DISRUPTION PHENOTYPE: No tail is synthesized.").

## Annotation Decisions
- **ACCEPT**:
  - `GO:0098025` (`virus tail, baseplate`): Essential structural subunit of the phage Mu baseplate wedge ([PMID:27555589]).
  - `GO:0098003` (`viral tail assembly`): Required for baseplate wedge completion and tail synthesis ([PMID:27555589], `file:BPMU/Mup46/Mup46-uniprot.txt`).
- **KEEP_AS_NON_CORE**:
  - `GO:0030430` (`host cell cytoplasm`): Compartment of late protein synthesis and virion morphogenesis.
- **TOO_GENERAL**:
  - `GO:0098015` (`virus tail`): Entailed by `GO:0098025` (`virus tail, baseplate`).
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, `enables`): Directly supported by [PMID:27555589] demonstrating `Mup46` (`BW1`) is one of the five essential structural components of the phage Mu baseplate (6 copies per baseplate).
