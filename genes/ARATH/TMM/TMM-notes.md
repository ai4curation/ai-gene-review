# TMM (At1g80080, Q9SSD1) curation notes

Session 2026-10-06 (stomatal_lineage_development module). Falcon deep research failed (HTTP 402); notes from cached literature.

## Identity
- UniProt Q9SSD1 TMM_ARATH (RLP17), 496 aa LRR receptor-like protein, single TM, no kinase domain [PMID:22241782 "Unlike ERECTA family RKs, TMM lacks a cytoplasmic effector domain"].

## Key findings
- tmm randomizes orientation of spacing divisions and allows divisions next to stomata -> clusters [PMID:11090210]; organ-specific: excess stomata in leaves, none in stems [PMID:11536724; PMID:9684356].
- TMM associates with ERECTA and ERL1 in vivo, not with itself [PMID:22241782 "TMM-YFP and ERECTA-Flag as well as TMM-YFP and ERL1-Flag associate with each other in vivo"].
- TMM-ERf constitutive complexes are the EPF1/EPF2 receptors; TMM creates the ligand pocket and excludes EPFL4/6 [PMID:28536146 "TMM interaction with ERL1 creates a binding pocket for recognition of EPF1 and EPF2..."].
- EPF2 and stomagen bind ER and TMM [PMID:26083750]; SERKs associate with TMM ligand-independently [PMID:26320950].
- Secondary: ABA sensitivity phenotypes [PMID:18434605; PMID:24553751], antifungal immunity with ERf [PMID:27446127], trichome overexpression phenotype [PMID:24553751].

## Curation decisions
- Core MF: coreceptor activity GO:0015026 (added NEW, IDA PMID:28536146); IBA signaling receptor activity accepted as the correct parent.
- Core BP: stomatal complex patterning GO:0010375 (IMP, accepted).
- Generic protein binding: 14-3-3 TAP row REMOVED; stomagen row MODIFIED to peptide binding.
- No GO-CAM models contain TMM.
