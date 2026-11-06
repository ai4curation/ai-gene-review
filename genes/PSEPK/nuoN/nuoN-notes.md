# nuoN notes

- NuoN is an antiporter-like membrane-arm subunit contributing to vectorial
  proton translocation [file:PSEPK/nuoN/nuoN-uniprot.txt "RecName:
  Full=NADH-quinone oxidoreductase subunit N"].

- Generic membrane is removed only because plasma membrane is already present.
  GO:0050136 is removed because its non-electrogenic definition conflicts with
  NDH-1 proton pumping.

## 2026-10-23 rework (Claude Code)

Deep-research providers are unavailable (no API keys); reviewed manually from the
HAMAP-annotated UniProt record and cached E. coli literature.
- Evidence now quotes HAMAP MF_00445 statements [file:PSEPK/nuoN/nuoN-uniprot.txt
  "Couples the redox reaction to proton translocation (for every two electrons
  transferred, four hydrogen ions are translocated across the cytoplasmic membrane),
  and thus conserves the redox energy in a proton gradient."] and E. coli NuoN
  mutagenesis [PMID:23864658 "Our mutation study on NLys(395) suggests that this
  residue participates in the proton translocation."].
- GO:0016020 KEEP_AS_NON_CORE -> MODIFY to GO:0005886; GO:1902600 ACCEPT -> MODIFY to
  GO:0015990 (descendant); GO:0008137 MODIFY-to-same-id -> ACCEPT; GO:0050136 REMOVE
  retained [PMID:3122832 NDH-2 is the non-electrogenic enzyme].
- Added NEW part_of GO:0045271. PANTHER: UniProt DR line gives PTHR22773 with no
  subfamily. `just validate PSEPK nuoN`: zero warnings/errors; status COMPLETE.
