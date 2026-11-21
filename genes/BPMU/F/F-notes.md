# Curation Notes: Escherichia phage Mu `F` (`Q01259`, Putative capsid assembly protein F / Mup30)

## Summary of Function
- **Product**: Putative capsid assembly protein F (`Mup30` / `gp30` / `gpF`, 439 aa, 49.4 kDa; `IPR006528` / `PF04233` `Phage_Mu_F` / `TIGR01641` `phageSPP1_gp7`).
- **Role in Morphogenesis**: Encoded immediately downstream of the portal gene `H` (`Mup29`), gpF is a late morphogenetic protein involved in viral capsid assembly (`GO:0019069`) that localizes to the host cytoplasm (`GO:0030430`) and remains associated with the mature virion capsid (`GO:0019028`) as a minor capsid protein (homologous to the portal-associated minor head protein gp7 of phage SPP1).

## Annotation Review Decisions
- **ACCEPT**:
  - `GO:0030430` (`host cell cytoplasm`, IEA): Site of viral capsid assembly.
- **NEW**:
  - `GO:0019069` (`viral capsid assembly`, `involved_in`, `GO_REF:0000043` supported by `file:BPMU/F/F-uniprot.txt`).
  - `GO:0019028` (`viral capsid`, `located_in`, `GO_REF:0000043` supported by `file:BPMU/F/F-uniprot.txt`).
