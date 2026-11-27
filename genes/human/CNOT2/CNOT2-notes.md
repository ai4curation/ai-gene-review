# CNOT2 review notes

## Scope

- Reviewed CNOT2 as the human PTHR23326:SF3 member of the Not2/Not3/Not5 noncatalytic CCR4-NOT family.
- Cross-checked CNOT3, the human PTHR23326:SF1 paralog, before writing `interpro/panther/PTHR23326/PTHR23326-review.yaml`.
- Treated CNOT2-CNOT3/CNOT1 complex assembly and noncatalytic participation in poly(A)-tail shortening as core, with Not-box-dependent transcriptional repression, P-body localization and ESC-maintenance rows retained as contextual.

## PAINT

The PTHR23326 PAINT slice has three root rows at `PANTHER:PTN000595684`: `GO:0000932` P-body, `GO:0030015` CCR4-NOT core complex and `GO:0000289` nuclear-transcribed mRNA poly(A) tail shortening. Separate stem-cell rows are asserted at `PANTHER:PTN000595688` for the CNOT2 branch and `PANTHER:PTN000595760` for the CNOT3 branch. `just paint-losses human CNOT2` and `just paint-losses human CNOT3` found no IRD or IKR loss rows to adjudicate.

## Module and GO-CAM fit

The production GO-CAM index has no CNOT2 or CNOT3 activity rows. `modules/mirna_biogenesis_and_silencing.yaml` already lists CNOT2 and CNOT3 as structural CCR4-NOT subunits in the miRNA-repression module and explicitly leaves a broader human CCR4-NOT module for future work, so this family PR does not add a module.
