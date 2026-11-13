# BICD2 review notes

## 2026-09-27 (claude-code)

- Identity: human BICD2 (Q8TD16), BicD family coiled-coil dynein cargo adaptor.
- Activating adaptor: [PMID:24986880 "addition of dynactin together with the N-terminal region of the cargo adaptor BICD2 (BICD2N) gives rise to unidirectional dynein movement over remarkably long distances"]; [PMID:25814576 "The Bicaudal-D2 coiled coil runs between dynein and dynactin to stabilize the mutually dependent interactions between all three components."].
- Golgi/RAB6 route: [PMID:25962623 "BICD2 facilitates the binding of Rab6A to the Golgi by stabilizing its GTP-bound form"].
- Nuclear pore route (G2): [PMID:20386726 "the nuclear pore complex (NPC) component RanBP2 directly binds to BICD2 and recruits it to NPCs specifically in G2 phase of the cell cycle"]; activation by CDK1/PLK1 [PMID:37105961 "modified BICD2 preferentially interacts with the nucleoporin RanBP2 once RanBP2 has been phosphorylated by CDK1"]; INM in rat RGPs [PMID:24034252 "BicD2 RNAi caused specific inhibition of apical, but not basal nuclear migration"].
- LINC route (neurons): [PMID:32619477 "the motor proteins interact with Nesprin-2 through the dynein/kinesin \"adaptor\" BicD2, both in neurons and in non-mitotic fibroblasts"].
- Decisions: protein binding RanBP2 -> MODIFY GO:0008093; dynein IC/RAB6A -> MODIFY GO:0070840 + GO:0031267; Hem-1 proteomics and KIF1C (abstract lacks it) -> REMOVE. Nuclear pore part_of and annulate lamellae kept non-core (transient G2 recruitment, peripheral). GSK-3beta/BICD (PMID:17139249, abstract emphasizes BICD1) microtubule anchoring/regulation rows kept non-core, not removed.
- NEW: GO:0007097 nuclear migration (comparators HOOK3 GO:0022027, DYNC1H1/PAFAH1B1/SYNE2 GO:0007097 in human GOA); GO:0140660 cytoskeletal motor activator activity (PMID:24986880, verified via PubMed eutils).
- Deep research (falcon) consulted: consistent (activating adaptor; RAB6, RANBP2, nesprin-2 cargos; CDK1-PLK1 activation; SMALED2).
- Local oaklib GO cache labels GO:0008093 as "cytoskeletal anchor activity"; OLS/QuickGO current label is "cytoskeletal adaptor activity" (validator warning only).
- Module check: GO:0008093 at nuclear envelope for both routes agrees; consider adding GO:0140660 as a secondary function of the BICD2 annotons.

## 2026-11-13 ORGANELLES Golgi batch 1 (Golgi apparatus rows)

- Rows: GO:0005794 EXP PMID:23664116, EXP PMID:23664119, IBA (`is_active_in`), IDA GO_REF:0000052 (HPA), IEA GO_REF:0000120. All ACCEPT; Golgi is in core_functions.locations.
- Marker check: [PMID:23664116 "Immunostainings with BICD2 antibody and two different Golgi markers, p230 and MG160, revealed diffused BICD2 staining throughout the cytoplasm and an increased signal at the Golgi site in wild-type fibroblasts"] (endogenous protein, human fibroblasts). UniProt Golgi location is ECO:0000269 from PMID:23664116 and PMID:23664119.
- Function at the Golgi: [PMID:25962623 "BICD2 facilitates the binding of Rab6A to the Golgi by stabilizing its GTP-bound form"]. So the root stays core.
- IBA: PTN001261414 (PTHR31233) GO:0005794 IBD seeds MGI:1924145, UniProtKB:Q8TD16 (BICD2), UniProtKB:Q96G01 (BICD1). `is_active_in` defensible.
- Sub-compartment: none. BICD2 is a peripheral, RAB6-recruited adaptor; regulated Rab docking is not stable tethering (rule 7), and the p230 co-stain does not resolve a sub-compartment for a recruited protein.
- Outcome: all five rows stay ACCEPT; dated ORGANELLES sentence added to each reason, plus the marker quote on the PMID:23664116 row.
