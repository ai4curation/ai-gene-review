# Gene 11 (P03746) Notes — Escherichia phage T7 (`BPT7`)

## Overview
- **Gene symbol**: `11`
- **UniProtKB accession**: `P03746` (`TUBE1_BPT7`, Tail tubular protein gp11 / Gatekeeper protein)
- **Length**: 196 amino acids (~22.3 kDa)
- **Structures**: `PDB:3J4B`, `PDB:6R21`, `PDB:9JYZ` (cryo-EM structures of the dodecameric gp11 adaptor ring in the T7 portal-tail complex).
- **InterPro / Pfam**: `InterPro:IPR033767` / `Pfam:PF17212` (`Tube`, Tail tubular protein, phage T7-like).

## Literature & Function Summary
- **Dodecameric tail adaptor (gatekeeper) ring of the T7 short tail** (`PMID:23884409`):
  - Cuervo et al. (2013) (`PMID:23884409`) demonstrated that gp11 is monomeric in solution and oligomerizes into a 12-subunit toroidal ring only upon docking onto the distal clip domain of the dodecameric gp8 portal connector after DNA packaging is completed.
  - The dodecameric gp11 adaptor ring extends the central DNA-ejection channel below the portal vertex, stabilizes packaged dsDNA within the head, provides the docking platform for the hexameric gp12 lower tail nozzle, and together with gp12 forms the attachment interface for the six gp17 tail fiber trimers (`PMID:23884409`, `file:genes/BPT7/11/11-uniprot.txt`).

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
