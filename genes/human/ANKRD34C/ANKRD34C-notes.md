# ANKRD34C notes

- Uncharacterized ANKRD34-family protein; brain-enhanced (HPA). The only GOA row is the pi-body IBA from the stale PTN001192751 / Asz1 (MGI:1921318) node, which is REMOVE, as for ANKRD34A (#4117) and ANKRD34B (#4119). Mouse Ankrd34c carries the same IBA plus ND roots (QuickGO).
- The current PTHR24156 PAINT node (cytosol, seeded by ANKRD34A/B) should reach ANKRD34C when GOA refreshes. No NEW is added here; the ANKRD34C-specific data are nil.
- Literature: one RARA::ANKRD34C fusion in an APL case [PMID:38294534, abstract]. It has an erratum (PMID:38532123) whose content is not in PubMed, so correctness is left unset. Affinage calls the fusion "recurrent"; it is a single case.
- knowledge_gaps: WHOLLY_DARK.

## Round 2 (reviewer on ANKRD34A, PR #4117; applied to all three ANKRD34 reviews)

- The pi-body propagation_review root_cause changes from SOURCE_STALE_OR_MISSING to PROPAGATION_BAD. Asz1's own pi-body localization is sound; the node propagated it to the wrong subfamily. failure_modes are [WRONG_ORTHOLOG_OR_PARALOG, CONTEXT_OR_TISSUE_MISMATCH].
- The reason now gives the domain-architecture argument. PTHR24157 is the ankyrin repeat, SAM and bZIP family, and mouse Asz1 has 6 ANK repeats plus a SAM domain; ANKRD34 proteins have 4 ANK repeats plus a disordered tail. PANTHER keeps a PTHR24157:SF0 "ANKYRIN REPEAT DOMAIN-CONTAINING PROTEIN 34A-RELATED" subfamily, which is probably how the stale node once spanned both.
