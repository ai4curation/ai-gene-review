# Gene 12 (P03747) Notes — Escherichia phage T7 (`BPT7`)

## Overview
- **Gene symbol**: `12`
- **UniProtKB accession**: `P03747` (`TUBE2_BPT7`, Tail tubular protein gp12 / Tail nozzle protein)
- **Length**: 794 amino acids (~89.3 kDa)
- **Structures**: `PDB:6R21`, `PDB:9JYZ` (atomic cryo-EM structures of the hexameric gp12 nozzle in the T7 portal-tail complex).
- **InterPro / Pfam**: `InterPro:IPR058003` / `Pfam:PF25675` (`Phage_nozzle`, Tail tubular protein gp12, phage T7-like).

## Literature & Function Summary
- **Hexameric tail nozzle and lower tubular channel of the T7 short tail** (`PMID:23884409`):
  - Cuervo et al. (2013) (`PMID:23884409`) demonstrated that six monomers of gp12 assemble onto the distal face of the dodecameric gp11 adaptor ring to form the conical lower tail tube and distal nozzle of the T7 virion (`PDB:6R21`, `9JYZ`).
  - In the mature virion, internal beta-hairpin loops of the gp12 hexamer close the distal exit of the axial tail channel to retain the packaged dsDNA and internal core proteins, while the exterior gp11-gp12 interface forms the docking site for the six trimeric gp17 tail fibers (`PMID:23884409`, `file:genes/BPT7/12/12-uniprot.txt`).
  - Upon host receptor recognition, the gp12 nozzle opens to allow ejection of the internal core proteins (gp6.7, gp7.3, gp14, gp15, gp16) and viral genomic dsDNA into the host cell (`GO:0099002`).

## Curation Decisions
- **ACCEPT**:
  - `GO:0098026` (`virus tail, tube`, IEA `GO_REF:0000043`, `part_of`).
  - `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`, IEA `GO_REF:0000043`, `involved_in`).
- **MODIFY**:
  - `GO:0098015` (`virus tail`, IEA `GO_REF:0000043`) -> `GO:0098026` (`virus tail, tube`, more specific descendant already present).
  - `GO:0046718` (`symbiont entry into host cell`, IEA `GO_REF:0000043`) -> `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`, more specific descendant already present).
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, `enables`, IDA `PMID:23884409`).
  - `GO:0098003` (`viral tail assembly`, `involved_in`, IDA `PMID:23884409`).
