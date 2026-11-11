# Bacteriophage P2 Gene Q (Portal protein gpQ; UniProt P25480)

## Overview
Gene **Q** of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes the 344-amino-acid portal (connector) protein gpQ (39.1 kDa; `UniProt:P25480`) (`PMID:1837355`, `PMID:8178458`, `PMID:17049269`). During morphogenesis, gpQ undergoes N-terminal proteolytic processing (removing the first 25 amino acids to generate the mature 319-aa portal subunit `h6`, residues 26–344) and self-assembles into a 12-subunit (dodecameric) ring structure (135 Å outer diameter with a central 25 Å DNA channel) located at the unique 5-fold vertex of both P2 and satellite P4 icosahedral capsids (`PMID:8178458`, `PMID:17049269`). The gpQ portal complex serves as the conduit for terminase-driven viral DNA packaging into the procapsid, the docking site for head-completion/neck proteins (`gpL`) and the contractile tail, and the exit channel for viral DNA ejection into the bacterial host during infection (`file:BPP2/Q/Q-uniprot.txt`).

## Key Literature & Experimental Evidence
- **PMID:8178458** (*Bacteriophage P2 and P4 morphogenesis: identification and characterization of the portal protein.*):
  - `"Here we present evidence that P2 gene Q codes for the P2 and P4 portal protein. First, microsequencing shows that capsid protein h6 is derived from gpQ, most probably by proteolytic cleavage. Second, antibodies against gpQ bind to the portal structure in disrupted P2 phage virions, as observed by electron microscopy. Third, gpQ partially purified from an overexpressing plasmid assembles into portal-like structures."`
- **PMID:17049269** (*The gpQ portal protein of bacteriophage P2 forms dodecameric connectors in crystals.*):
  - `"The gpQ connector protein from bacteriophage P2 has been overexpressed in Escherichia coli and purified by sucrose gradient centrifugation. Negative stain electron microscopy and image analysis revealed a 135 A diameter dodecameric ring structure with a central 25 A hole."`

## Curation Decisions
- **Molecular Function**:
  - `GO:0039660` (`structural constituent of virion`): **NEW** supported by `PMID:8178458` and `PMID:17049269`.
- **Biological Process**:
  - `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`, IEA): **ACCEPT**
  - `GO:0046718` (`symbiont entry into host cell`, IEA): **MODIFY** to `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`).
  - `GO:0019073` (`viral DNA genome packaging`) and `GO:0019069` (`viral capsid assembly`): **NEW** supported by `PMID:8178458` and `PMID:17049269`.
- **Cellular Component / Complex**:
  - `GO:0019028` (`viral capsid`, IEA): **ACCEPT** (put in `locations` in `core_functions`).
  - `GO:0046798` (`viral portal complex`): **NEW** (`part_of`, `PMID:17049269` and `PMID:8178458`; put in `in_complex` in `core_functions`!).
