# ycgR Notes

## 2026-07-09 PDT / 2026-07-10 UTC

First-pass motility-bucket curation. ycgR encodes a PilZ-domain c-di-GMP-binding
flagellar brake [file:PSEPK/ycgR/ycgR-uniprot.txt "DE   RecName: Full=Flagellar brake protein YcgR;"]
[file:PSEPK/ycgR/ycgR-uniprot.txt "DE   AltName: Full=Cyclic di-GMP binding protein YcgR;"].
UniProt describes c-di-GMP-dependent regulation of swimming and swarming
[file:PSEPK/ycgR/ycgR-uniprot.txt "CC   -!- FUNCTION: Acts as a flagellar brake, regulating swimming and swarming"]
and records basal-body localization [file:PSEPK/ycgR/ycgR-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Bacterial flagellum basal body {ECO:0000250}."].

Decision: route ycgR to `modules/flagellar_motor_switch_stator_boundary.yaml`
as a c-di-GMP-dependent motor-brake node, not to c-di-GMP turnover.
