# PP_4329 Notes

## 2026-07-09 PDT / 2026-07-10 UTC

First-pass motility-bucket curation. PP_4329 is a short FlhB-family/type-III
substrate exporter candidate, distinct from canonical `flhB`/PP_4352
[file:PSEPK/PP_4329/PP_4329-uniprot.txt "DE   RecName: Full=Flagellar biosynthetic protein FlhB {ECO:0000256|ARBA:ARBA00021622};"]
[file:PSEPK/PP_4329/PP_4329-uniprot.txt "DR   InterPro; IPR006135; T3SS_substrate_exporter."].
UniProt states that it is required for flagellar rod/basal-body formation and
may constitute the flagellin export apparatus [file:PSEPK/PP_4329/PP_4329-uniprot.txt "CC   -!- FUNCTION: Required for formation of the rod structure in the basal body"].

Decision: modify generic protein secretion toward flagellar type-III-like
export/assembly and route PP_4329 to
`modules/flagellar_export_assembly_boundary.yaml`.
