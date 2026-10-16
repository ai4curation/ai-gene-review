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
