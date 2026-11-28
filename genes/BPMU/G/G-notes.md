# Curation Notes: Escherichia phage Mu `G` (`Q01261`, Putative capsid assembly protein G / Mup31)

## Summary of Function
- **Product**: Putative capsid assembly protein G (`Mup31` / `gp31` / `gpG`, 156 aa, 17.2 kDa; `IPR006522` / `PF05069` `Phage_tail_S` / `TIGR01635` `tail_comp_S`).
- **Role in Morphogenesis**: Encoded between `F` (`Mup30`) and `I`/`Z` (`Mup32`/`Mup33`) and translated from a non-canonical `GUG` start codon during late infection. Annotated in UniProtKB as involved in viral capsid assembly (`GO:0019069`) and localized to the virion capsid (`GO:0019028`) and host cytoplasm (`GO:0030430`) based on Grimaud (1996) (`PubMed:8599204`). Its domain homology (`PF05069` / `TIGR01635`, homologous to phage P2 head-completion protein S) indicates a role at the head-tail connector/portal vertex after DNA packaging.

## Annotation Review Decisions
- **ACCEPT**:
  - `GO:0030430` (`host cell cytoplasm`, IEA): Site of viral morphogenesis.
- **NEW**:
  - `GO:0019069` (`viral capsid assembly`, `involved_in`, `GO_REF:0000043` supported by `file:BPMU/G/G-uniprot.txt`).
  - `GO:0019028` (`viral capsid`, `located_in`, `GO_REF:0000043` supported by `file:BPMU/G/G-uniprot.txt`).
