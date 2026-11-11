# Gene 8 (P03728) Notes — Escherichia phage T7 (`BPT7`)

## Overview
- **Gene symbol**: `8`
- **UniProtKB accession**: `P03728` (`PORTL_BPT7`, Portal protein / Head-to-tail joining protein / Connector protein)
- **Length**: 536 amino acids (~59.1 kDa)
- **Structures**: `PDB:3J4A`, `PDB:6QWP`, `PDB:6R21`, `PDB:9JYZ` (high-resolution cryo-EM structures of the dodecameric portal ring in open and closed conformations and within the portal-tail complex).
- **Domains**: `HAMAP:MF_04120` (`Phage_portal_T7`), `InterPro:IPR020991` (`Connector_podovirus`) / `InterPro:IPR038995` (`Portal_prot_Caudovirale`) / `Pfam:PF12236` (`Head-tail_con`).

## Literature & Function Summary
- **Homododecameric portal connector at the unique 5-fold vertex of the T=7 capsid** (`PMID:15784250`, `PMID:23580619`, `PMID:23632014`, `PMID:23884409`):
  - Agirrezabala et al. (2005) (`PMID:15784250`) and Cuervo et al. (2013) (`PMID:23884409`) showed that 12 monomers of gp8 assemble into a toroidal homododecameric portal ring with a central axial channel (~40 Å diameter) comprising stem, wing, crown, and clip domains.
  - Embedded at a single 5-fold vertex of the gp10 icosahedral shell (`PMID:23580619`), the gp8 portal serves as the docking site for the internal core stack (gp14, gp15, gp16) inside the capsid (`PMID:23580619`), couples with the pentameric gp19 terminase motor to translocate genomic dsDNA into the procapsid (`PMID:23632014`), and binds the dodecameric gp11 tail adaptor ring after DNA packaging (`PMID:23884409`).
  - During host infection, the portal channel serves as the conduit for ejection of the internal core proteins and viral dsDNA genome through the short tail (`GO:0099002`).

## Curation Decisions
- **ACCEPT**:
  - `GO:0046798` (`viral portal complex`, IDA `PMID:23884409` and IEA `GO_REF:0000120`, `part_of`; placed in `core_functions.in_complex`).
  - `GO:0019073` (`viral DNA genome packaging`, IDA `PMID:23580619` and IEA `GO_REF:0000104`, `involved_in`).
  - `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`, IEA `GO_REF:0000120`, `involved_in`).
- **MODIFY**:
  - `GO:0019028` (`viral capsid`, IEA `GO_REF:0000120`) -> `GO:0046798` (`viral portal complex`, a more specific complex term already present on gp8).
  - `GO:0046718` (`symbiont entry into host cell`, IEA `GO_REF:0000043`) -> `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`).
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, `enables`, IDA `PMID:23884409`).
