# PR 6164 review follow-up

Review 5809803940, checked against publication head 04e7322f4c2f032c8f88737ba78bf3197563f2ba.

1. Restored both verified wrong-PMID mappings as structured reference replacement metadata on the original references. Corrected references remain in use; annotation provenance is unchanged.
2. Refined the GroEL2 self-interaction row to GO:0042802. The crystal observation is supported by independent lower-oligomer evidence, without asserting that the asymmetric-unit dimer fixes physiological stoichiometry.
3. Marked the E. coli GroES metal-binding transfer as over-annotated. An indirect calcium-dependent hydrodynamic response does not establish a conserved binding site; high concentration alone does not prove the observation is an artifact. Positive donor evidence is retained.
4. Moved the ontology-only holdase limitation out of biological knowledge gaps into notes; biological client-transfer and occupancy uncertainties remain.
5. Restored mechanistic GroEL biology to the PSEPK description; evidence limitations remain in appropriate review fields and notes.
6. Set both holdase proposals under GO:0044183 protein folding chaperone, after checking its definition.
7. Added the supported PSEPK GroES complex relationship. BACSU and MYCTU already contain contributes_to GO:0140662, as do the other representatives; no change was needed there. ECOLI GroES already has the complete co-chaperonin representation.
8. Explicitly retained GroEL2's broader chaperone term for the documented non-ATP folding mode.
9. Retained the historical PR6121 merged-content proof: it supports a shared-ledger completion retained during main integration. Removing it would break that provenance or regress a verified completed row. No cytochrome scientific content was changed in this follow-up.

All 201 ordered original annotation payloads remain intact; two actions changed, with no added or retired rows. Focused gene, module, history, render, coverage and lint checks pass. Full follow-up validation is pending and the earlier full-run proof remains explicitly scoped to its recorded head.
