# PP_4328 Notes

## 2026-07-09 PDT / 2026-07-10 UTC

First-pass motility-bucket curation. PP_4328 has no GOA rows, but UniProt and
Asta support a FliK-like hook-control C-terminal-domain candidate
[file:PSEPK/PP_4328/PP_4328-uniprot.txt "DE   RecName: Full=Flagellar hook-length control protein-like C-terminal domain-containing protein {ECO:0000259|Pfam:PF02120};"]
[file:PSEPK/PP_4328/PP_4328-uniprot.txt "DR   InterPro; IPR021136; Flagellar_hook_control-like_C."]
[file:PSEPK/PP_4328/PP_4328-deep-research-asta.md "Key Domains:** Flagellar_hook_control-like_C. (IPR021136); FliK-like_C_sf. (IPR038610); Flg_hook (PF02120)"].

Decision: add a conservative `bacterial-type flagellum assembly` NEW row and
route PP_4328 to `modules/flagellar_export_assembly_boundary.yaml` as a
hook-length/accessory spillover.
