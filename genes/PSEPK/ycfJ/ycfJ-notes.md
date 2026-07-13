# ycfJ Notes

## 2026-07-09 PDT / 2026-07-10 UTC

First-pass motility-bucket curation. ycfJ has a regulator-of-flagellation
product name [file:PSEPK/ycfJ/ycfJ-uniprot.txt "DE   SubName: Full=Regulator of flagellation {ECO:0000313|EMBL:AAN66462.1};"],
but the concrete domain/location evidence supports an outer-membrane
lipoprotein/surface-antigen-family protein
[file:PSEPK/ycfJ/ycfJ-uniprot.txt "DR   InterPro; IPR051407; Bact_OM_lipoprot/Surf_antigen."]
[file:PSEPK/ycfJ/ycfJ-uniprot.txt "DR   GO; GO:0019867; C:outer membrane; IEA:InterPro."].

Decision: route ycfJ to `modules/transport_envelope_spillover_boundary.yaml`
and do not assert a process-level flagellar regulatory role in this pass.
