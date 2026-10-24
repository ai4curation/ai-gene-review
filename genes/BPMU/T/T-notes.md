# T (Q9T1W1) — Major capsid protein (Mup34 / gpT)

## Summary
- **UniProt**: `Q9T1W1` (`CAPSD_BPMU`), 305 aa, locus tag `Mup34`, gene `T`.
- **Function**: Major capsid protein of bacteriophage Mu that self-assembles around the scaffolding protein Z and the portal-protease initiator complex to form the ~54 nm icosahedral procapsid/head shell, dependent on host GroEL/GroES chaperonin machinery ([file:BPMU/T/T-uniprot.txt](T-uniprot.txt); [PMID:6213090](../../../publications/PMID_6213090.md)).
- **Structure**: High-resolution cryo-EM structures of the phage Mu capsid (`PDB:9KHY`, `PDB:9KHZ`) confirm the HK97-fold major capsid subunit (`PF05065` / `IPR006444`) organized into an icosahedral head shell (`T=7`).

## Key References
- **PMID:6213090**: Shore & Howe (1982), *Virology* — "Bacteriophage Mu T mutants are defective in synthesis of the major head polypeptide." Demonstrates that gene *T* encodes the major head polypeptide of phage Mu.
- **file:BPMU/T/T-uniprot.txt**: Swiss-Prot curated entry documenting self-assembly into a ~54 nm icosahedral capsid, procapsid assembly with portal, protease I, and scaffolding protein Z, dependence on host GroEL/GroES, and virion/host cytoplasm localization.

## Annotation Decisions
- `GO:0098017` (`viral capsid, major subunit`, IMP, `PMID:6213090`): **ACCEPT** — directly supported by mutant analysis showing *T* encodes the major head subunit.
- `GO:0019028` (`viral capsid`, IEA, `GO_REF:0000043`): **TOO_GENERAL** — true but broader than retained `GO:0098017` (`viral capsid, major subunit`) and proposed `GO:0019030` (`icosahedral viral capsid`).
- `GO:0030430` (`host cell cytoplasm`, IEA, `GO_REF:0000044`): **KEEP_AS_NON_CORE** — procapsid assembly occurs in the host cytoplasm with host GroEL/GroES, while the mature protein's core structural role is in the icosahedral viral capsid.
- `GO:0039660` (`structural constituent of virion`, `enables`): **NEW** — captures the core molecular function of the major capsid subunit.
- `GO:0019069` (`viral capsid assembly`, `involved_in`): **NEW** — captures self-assembly into the icosahedral procapsid/head shell.
- `GO:0019030` (`icosahedral viral capsid`, `located_in`): **NEW** — captures the specific icosahedral capsid localization documented in UniProt (`FUNCTION: Capsid protein that self-assembles to form an icosahedral capsid, about 54 nm in diameter.`).
