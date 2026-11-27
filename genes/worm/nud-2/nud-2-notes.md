# nud-2 (C. elegans, O45717) review notes

## 2026-09-27 initial review (claude-code)

Context: sole worm NudE/NDEL family member; comparative for `modules/nucleokinesis.yaml` and `modules/linc_complex.yaml` (UNC-83 KASH recruits NUD-2).

Key evidence
- UNC-83 (KASH) binds NUD-2 C terminus and recruits it to the NE (HeLa co-expression; worm IF uninformative); nud-2(ok949) hyp7 nuclear migration defect (1.2%), enhanced with bicd-1 (14.2%); NUD-2/LIS-1 module parallel to BICD-1/EGAL-1/DLC-1 [PMID:20005871 "These data demonstrate that UNC-83 recruits NUD-2 to the nuclear envelope through a direct interaction in vivo."].
- P-cell nuclear migration through constrictions: dynein via UNC-83 central; nud-2;bicd-1 failed migrations and GABA neuron loss [PMID:27697906].
- Kinetochore: recruited by CENP-F-like HCP-1/2; sustains kinetochore dynein; delayed attachments, chromatin bridges; dispensable for centrosome separation, pronuclear migration, spindle positioning; synthetic with partial lis-1 RNAi [PMID:29192061].
- Spindle-region accumulation pre-NEBD via C-terminal helix; retention of dynein regulators [PMID:35817834].
- RNAi convulsion / GABA vesicle phenotypes [PMID:16996038, abstract only].
- Falcon deep research (nud-2-deep-research-falcon.md) consistent (kinetochore role, quantitative reductions); used as supporting text for NEW MF.

Decisions
- NEW MF GO:0140659 (IMP PMID:29192061). Core: NE-localized nuclear migration along MT; kinetochore dynein/chromosome segregation.
- MODIFY GO:0031022 nuclear migration along microfilament -> GO:0030473 (paper is about dynein/kinesin via UNC-83).
- Kinetochore and chromosome segregation IBAs ACCEPTED (worm-validated; note fungal NudE lacks this, worm has CENP-F-like HCP-1/2).
- Centrosome, centrosome localization, mitotic centrosome separation, MT nucleation IBAs over-annotated: worm null shows normal centrosome functions.
- Kinesin complex IBA removed; synapse IEA (process-inferred) removed; protein binding rows removed.
- GABAergic synaptic transmission IMP/IGI over-annotated (indirect; likely via P-cell migration/neuron loss or vesicle trafficking).
