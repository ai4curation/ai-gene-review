# Curation Notes: Escherichia phage Mu `H` (`Q9T1W5`, Portal protein H / Mup29)

## Summary of Function
- **Product**: Portal protein H (`Mup29` / `gp29` / `gpH`, 512 aa, 56.9 kDa; `IPR009279` / `PF06074`, `TCDB 1.W.9.1.1`; cryo-EM structures `PDB:9KHX`, `PDB:9KNU`).
- **Role in Morphogenesis & Infection**: Multimerizes into a ring-shaped homododecamer (`GO:0046798`, `GO:0039660`) located at a unique 5-fold vertex of the icosahedral capsid (`GO:0019028`). Forms an early 25S initiator complex with protease I (`gp32`) in a host `GroEL`/`GroES`-dependent pathway to nucleate assembly of the scaffolding protein Z (`gp33`) and major capsid protein T (`gp34`) into immature proheads (`GO:0019069`). Cleavage of the C-terminus of gp29 by protease I yields mature procapsids competent to dock the `gp27`-`gp28` terminase complex for headful viral DNA genome packaging (`GO:0019073`). After packaging, gp29 serves as the connector for neck/tail attachment and forms the central channel for genome ejection through the host cell envelope (`GO:0099000`).

## Annotation Review Decisions
- **ACCEPT**:
  - `GO:0019028` (`viral capsid`, IEA): Located at the unique 5-fold vertex of the capsid.
  - `GO:0030430` (`host cell cytoplasm`, IEA): Site of prohead assembly and maturation.
  - `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`, IEA): Central portal conduit for DNA ejection.
- **TOO_GENERAL**:
  - `GO:0046718` (`symbiont entry into host cell`, IEA): Entailed by `GO:0099000`.
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, `enables`), `GO:0019069` (`viral capsid assembly`, `involved_in`), `GO:0019073` (`viral DNA genome packaging`, `involved_in`), `GO:0046798` (`viral portal complex`, `part_of`).
