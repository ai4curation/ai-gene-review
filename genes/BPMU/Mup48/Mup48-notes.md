# Curation Notes for Mup48 (Q9T1V1) — Phage Mu Baseplate protein gp48 (BW3 / gpR)

## Biological Summary
- **Gene / Protein**: `Mup48` (UniProt `Q9T1V1`, 180 aa; also designated `gp48`, `gpR`, or baseplate wedge protein 3 `BW3` in [PMID:27555589]).
- **Structure and Function**:
  - Homolog of phage T4 gp7/gp53 wedge component (`BW3`, `Pfam:PF10076` `Phage_Mu_Gp48`). Essential core subunit of the phage Mu baseplate wedge (`Mup46`/`Mup47`/`Mup48`, i.e. `BW1`/`BW2`/`BW3`).
  - In [PMID:27555589], `Mup48` (`BW3`) forms a binary complex with `Mup47` (`BW2`) in the initial step of baseplate wedge assembly before `Mup46` (`BW1`) joins to form the complete wedge (`Mup46`/`47`/`48`, 6 copies of each per baseplate, `PDB:9KI1`).
  - Required for tail synthesis (`file:BPMU/Mup48/Mup48-uniprot.txt`, "-!- DISRUPTION PHENOTYPE: No tail is synthesized.").

## Annotation Decisions
- **ACCEPT**:
  - `GO:0098025` (`virus tail, baseplate`): Core structural subunit of the phage Mu baseplate wedge ([PMID:27555589]).
  - `GO:0098003` (`viral tail assembly`): Essential for baseplate wedge assembly and tail morphogenesis ([PMID:27555589], `file:BPMU/Mup48/Mup48-uniprot.txt`).
- **KEEP_AS_NON_CORE**:
  - `GO:0030430` (`host cell cytoplasm`): Compartment of late protein synthesis and virion assembly.
- **TOO_GENERAL**:
  - `GO:0098015` (`virus tail`): Entailed by `GO:0098025` (`virus tail, baseplate`).
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, `enables`): Directly supported by [PMID:27555589] showing `Mup48` (`BW3`) is one of the five essential structural components of the phage Mu baseplate.
