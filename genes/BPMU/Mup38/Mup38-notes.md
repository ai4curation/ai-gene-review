# Mup38 (P79677) — Putative sheath terminator protein gp38

## Summary
- **UniProt**: `P79677` (`VG38_BPMU`), 67 aa, locus tag `Mup38`.
- **Function**: Putative tail sheath terminator protein of bacteriophage Mu (`PF11191` / `IPR024197`). Encoded immediately upstream of the tail sheath gene *L* (`Mup39`), gp38 is proposed to cap the polymerizing tail sheath once it reaches its requisite length, preventing sheath depolymerization and interacting with both the tail tube and tail sheath proteins ([file:BPMU/Mup38/Mup38-uniprot.txt](Mup38-uniprot.txt)).

## Key References
- **file:BPMU/Mup38/Mup38-uniprot.txt**: Swiss-Prot record documenting putative sheath terminator function, virion tail and host cytoplasm localization, late-phase transcriptional induction by protein C, and `Phage_Mu_gp38` (`PF11191` / `IPR024197`) family membership.

## Annotation Decisions
- `GO:0098003` (`viral tail assembly`, IEA, `GO_REF:0000043`): **ACCEPT** — caps the polymerizing tail sheath during viral tail assembly.
- `GO:0098015` (`virus tail`, IEA, `GO_REF:0000043`): **ACCEPT** — localizes to the phage tail as the sheath-capping component.
- `GO:0030430` (`host cell cytoplasm`, IEA, `GO_REF:0000044`): **KEEP_AS_NON_CORE** — synthesized and assembled in the host cytoplasm during late infection, while functioning structurally in the virion tail.
- `GO:0039660` (`structural constituent of virion`, `enables`): **NEW** — structural cap subunit of the virion tail sheath.
