# Curation Notes for Mup47 (Q9T1V2) — Phage Mu Baseplate protein gp47 (BW2 / gpW)

## Biological Summary
- **Gene / Protein**: `Mup47` (UniProt `Q9T1V2`, 360 aa; also designated `gp47`, `gpW`, or baseplate wedge protein 2 `BW2` in [PMID:27555589]).
- **Structure and Function**:
  - Homolog of phage T4 gp6 (`BW2`, `Pfam:PF04865` `Baseplate_J`). Essential core subunit of the phage Mu baseplate wedge (`Mup46`/`Mup47`/`Mup48`, i.e. `BW1`/`BW2`/`BW3`).
  - In [PMID:27555589], `Mup47` (`BW2`) binds directly to `Mup48` (`BW3`) in the first step of wedge assembly, before recruiting `Mup46` (`BW1`) to form the dimeric baseplate wedge (6 copies of `Mup47` per baseplate, `PDB:9KI1`).
  - Required for tail synthesis (`file:BPMU/Mup47/Mup47-uniprot.txt`, "-!- DISRUPTION PHENOTYPE: No tail is synthesized.").

## Annotation Decisions
- **ACCEPT**:
  - `GO:0098025` (`virus tail, baseplate`): Core structural subunit of the phage Mu baseplate wedge ([PMID:27555589]).
  - `GO:0098003` (`viral tail assembly`): Essential for baseplate wedge assembly and tail morphogenesis ([PMID:27555589], `file:BPMU/Mup47/Mup47-uniprot.txt`).
- **KEEP_AS_NON_CORE**:
  - `GO:0030430` (`host cell cytoplasm`): Compartment of late protein synthesis and virion assembly.
- **TOO_GENERAL**:
  - `GO:0098015` (`virus tail`): Entailed by `GO:0098025` (`virus tail, baseplate`).
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, `enables`): Directly supported by [PMID:27555589] showing `Mup47` (`BW2`) is an essential structural subunit of the phage Mu baseplate wedge.
