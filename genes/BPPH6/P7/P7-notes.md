# P7 (P11123) — Pseudomonas phage phi6

## Overview
- **Gene symbol**: P7
- **UniProt ID**: P11123 (`P7_BPPH6`)
- **Product**: Assembly protein P7 (161 AA, 17.3 kDa), encoded on dsRNA segment L.

## Literature & Functional Evidence
- **Inner procapsid assembly cofactor and packaging stabilizer at the three-fold axis**:
  - P7 is one of the four structural proteins (P1, P2, P4, P7) of the phi6 procapsid (polymerase complex). Cryo-EM difference mapping of P7-null vs wild-type procapsids demonstrates that P7 localizes on the interior surface of the unexpanded P1 procapsid shell around the 20 three-fold symmetry axes, overlapping the positions of the P2 RdRP and stabilizing P2 and procapsid assembly [PMID:23077625, "Difference maps parsed out the density rigid-bodies attributable to P7 and P2. Our result indicates that P7 forms a monomeric structure around the three-fold axis in packaged traces (12 to 20 copies per particle), and locates near the three-fold axis on the inner surface of the P1 shell."]; [PMID:23077625, "Noticeably, the locations of P7 overlap with the density from P2, the RdRP, in a mutually exclusive manner, indicating that P7 might mechanically stabilize P2 in the unexpanded PC."].
  - UniProt curates that P7 is required for efficient procapsid assembly, necessary for stable viral RNA genome packaging, and involved in regulating plus-strand synthesis (transcription) [file:BPPH6/P7/P7-uniprot.txt, "FUNCTION: Assembly protein part of the packaging complex that packages the viral RNA segments, replicate them into a double-stranded form and transcribe them. Required for efficient procapsid assembly. Necessary for stable packaging. May stabilize the RNA-dependent RNA polymerase (RdRP) in its position at the three-fold axis on the inner side of empty-unexpanded procapsids. Could play a role in viral RNA recognition. Seems to be involved in the regulation of plus strand synthesis (transcription) as a fidelity factor."].

## Curation Decisions
- **Existing GOA annotations**: None (0 annotations in GOA).
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, IC from `file:BPPH6/P7/P7-uniprot.txt`): P7 is an essential structural protein of the viral procapsid/inner capsid.
  - `GO:0019069` (`viral capsid assembly`, IC from `file:BPPH6/P7/P7-uniprot.txt`): P7 accelerates and stabilizes assembly of the P1-P2-P4-P7 procapsid core.
  - `GO:0019072` (`viral genome packaging`, IC from `file:BPPH6/P7/P7-uniprot.txt`): P7 is necessary for stable packaging of the three viral ssRNA genome segments into the procapsid.
  - `GO:0019030` (`icosahedral viral capsid`, IC from `file:BPPH6/P7/P7-uniprot.txt`): P7 localizes to the inner surface of the icosahedral P1 procapsid/capsid near the three-fold symmetry axes (`PMID:23077625`).
