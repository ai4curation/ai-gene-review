# J (Q9T1V9) — Gene product J (Mup36 / gpJ)

## Summary
- **UniProt**: `Q9T1V9` (`VPJ_BPMU`), 141 aa, locus tag `Mup36`, gene `J`.
- **Function**: Essential head-to-tail joining (neck/adaptor) protein of bacteriophage Mu (`PF07030` / `IPR009752`). Disruption of gene *J* results in the accumulation of unattached tails and DNA-filled heads (`DISRUPTION PHENOTYPE: Accumulation of unattached tails and full heads. {ECO:0000269|PubMed:3904174}.`), demonstrating its essential role in joining mature heads and tails during virion assembly ([file:BPMU/J/J-uniprot.txt](J-uniprot.txt)).
- **Structure**: Solved by X-ray crystallography (`PDB:5YDN`, residues 1–109) and in situ cryo-EM of the phage Mu neck complex (`PDB:9KHX`, `PDB:9KNU`), where 12 copies of gpJ (`A–L` / `M–X`, residues 1–141) form a dodecameric neck ring connecting the portal/head to the tail ([file:BPMU/J/J-uniprot.txt](J-uniprot.txt)).

## Key References
- **file:BPMU/J/J-uniprot.txt**: Swiss-Prot record documenting late-phase expression, the head-tail joining disruption phenotype (`PubMed:3904174`), X-ray and cryo-EM structures (`5YDN`, `9KHX`, `9KNU`), and `Phage_Mu_GpJ` (`IPR009752` / `PF07030`) domain membership.

## Annotation Decisions
- `GO:0030430` (`host cell cytoplasm`, IEA, `GO_REF:0000044`): **ACCEPT** — gpJ is synthesized and mediates head-to-tail joining in the host cell cytoplasm during late lytic assembly.
- `GO:0039660` (`structural constituent of virion`, `enables`): **NEW** — supported by dodecameric incorporation into the mature virion neck in cryo-EM structures (`PDB:9KHX`, `PDB:9KNU`) and its structural requirement for head-tail attachment.
- `GO:0019068` (`virion assembly`, `involved_in`): **NEW** — directly supported by the disruption phenotype (`Accumulation of unattached tails and full heads.`).
