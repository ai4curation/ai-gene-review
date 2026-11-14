# nuoC notes

- PP_4121 is a fused NuoC/D polypeptide that satisfies two conserved
  quinone-site scaffold roles [file:PSEPK/nuoC/nuoC-uniprot.txt "RecName:
  Full=NADH-quinone oxidoreductase subunit C/D"].

- Quinone binding is retained, but NAD binding is removed because NAD(H) binds
  at the NuoF input site rather than this scaffold.

## 2026-10-23 re-review (complex I module promotion)

- Replaced all RecName and sidecar quotes with HAMAP MF_01359 CC text, family
  SIMILARITY lines, and E. coli/Thermus literature cited by orthology
  (PMID:20979355, 25545070, 34308841, 23417064). Deep-research providers are
  unavailable in this environment, so no new deep-research file was written.
- The GO:0008137 enables row is now ACCEPT, noted as contributes_to in
  core_functions; the old MODIFY proposed the identical id. GO:0016651 and
  GO:0016655 are MODIFY -> GO:0008137. GO:0030964 is MODIFY -> GO:0045271,
  which is added as a NEW (ISS) row.
- Quinone binding is confirmed as the core MF: the 49-kDa-family head-group
  ligands are Tyr/His.
- Removed the goa.tsv entry from references (GOA files are never cited).
- Validation: 0 warnings and 0 errors (with UV_NATIVE_TLS unset).
