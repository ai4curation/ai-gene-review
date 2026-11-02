# Gene 9 (P03716) Notes — Escherichia phage T7 (`BPT7`)

## Overview
- **Gene symbol**: `9`
- **UniProtKB accession**: `P03716` (`SCAF_BPT7`, Capsid assembly scaffolding protein)
- **Length**: 307 amino acids (~33.8 kDa; N-terminal initiator Met1 cleaved, mature chain residues 2–307)
- **InterPro / Pfam**: `InterPro:IPR008768` / `Pfam:PF05396` (`Phage_T7_Capsid`, Bacteriophage T7 capsid assembly protein).

## Literature & Function Summary
- **Scaffolding protein for T=7 procapsid assembly** (`PMID:13677051`, `PMID:16211007`, `PMID:25313071`):
  - Cerritelli and Studier (1996) (`PMID:13677051`) demonstrated that ~240 copies of gp9 co-assemble with the major capsid protein gp10 (`P19726`) and the portal ring gp8 (`P03728`) to direct assembly of the T=7 procapsid (prohead I), locking gp10 hexamers into a morphogenetically productive curvature; gp9 is subsequently expelled without extensive proteolysis as the procapsid expands into the mature polyhedral capsid during DNA packaging.
  - Agirrezabala et al. (2007) (`PMID:16211007`) localized the gp9 scaffolding shell by cryo-EM as a concentric inner protein layer between the internal core stack and the inner surface of the gp10 procapsid shell, contacting the wing domain of the gp8 portal connector.
  - Guo et al. (2014) (`PMID:25313071`) resolved at subnanometer cryo-EM resolution that the N-terminal six-turn helix of each skewed gp10 hexamer on the inner surface of the procapsid shell interacts with two gp9 scaffolding molecules.

## Curation Decisions
- `GO:0019069` (`viral capsid assembly`, IEA `GO_REF:0000002`, `involved_in`) -> `ACCEPT` (supported by `PMID:13677051`, `PMID:16211007`, `PMID:25313071`).
