# TARDBP notes

## 2026-11-03 ORGANELLES batch 4 (mitochondrion rows)

- Rows: GO:0005739 IEA (GO_REF:0000044, SL-0173). No sub-compartment rows. Action stays KEEP_AS_NON_CORE; reason extended and supported_by added.
- UniProt: Mitochondrion {ECO:0000269|PubMed:28794432, PubMed:33031745}; [file:human/TARDBP/TARDBP-uniprot.txt "A small subset localizes in mitochondria (PubMed:28794432)"]. Mapping sound. Both papers fetched 2026-11-03 (full text).
- Protease protection: [PMID:28794432 "we treated a mitochondrial fraction with proteinase K and detected both endogenous and exogenous TDP-43; TDP-43 was not detected, however, if the mitochondrial membrane was permeabilised with Triton X-100 prior to proteinase K treatment"], plus immuno-EM inside mitochondria. UV-CLIP binds mt-tRNAs (Asn, Gln, Pro) and processing intermediates, a matrix-side function.
- Import: depends on the TIM22 carrier pathway and AGK [PMID:33031745 "TIM22 normally functions to import multi-pass transmembrane proteins, which TDP-43 is not"]; that paper cites earlier work [PMID:33031745 "it has been reported that TDP-43 gains access to the mitochondrial matrix via the mitochondrial import inner membrane translocase TIM22"].
- Outcome: root only. The internal pool is real (minor), but the lines disagree on matrix vs inner membrane, the protease assay cannot separate matrix from IMS or inner membrane, and there is no presequence, so neither GO:0005759 nor GO:0005743 is added. Candidate for a sub-mitochondrial fractionation (alkaline carbonate, digitonin titration) to decide.
