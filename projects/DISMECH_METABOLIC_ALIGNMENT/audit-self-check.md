---
title: 'dismech metabolic alignment: audit self-check'
description: Two runs of the same audit reconciled flag by flag, as a check on the generator
species: [human]
---

# DISMECH metabolic alignment: audit self-check

[Back to the project page](../DISMECH_METABOLIC_ALIGNMENT.md)

This page reconciles two runs of the same audit over different trees. It is a check on the generator - that the flags which should not depend on which gene reviews exist do not - and not a finding about how dismech and ai-gene-review agree. It names individual rows and review statuses for that reason.

The second run records no answer for whether `align_audit.py` was modified when it ran, though git answered for the audited tree itself: clean. Both runs record the same script (`906bd065421d`), in which the two answers come from one command in one directory differing only in the pathspec that names the script - which is why `audit_revision` is unrecorded for that run as well. The primary run answers it: clean.

The audit also runs over a second tree, and comparing the two runs shows which flags
are artifacts of the missing slices rather than findings. That tree is this branch (claude/cool-edison-o9wvf0-alignment-project at 132532cf6) alone, before main was merged in, so the gene reviews and modules added by the ten themed slice PRs of #4690 are absent.
Both cover the same
183 gene rows. Flags that fall: `ALIGNED_NONCORE` 0 against 1, `ALIGNED_ON_SHARED_NODE_ONLY` 25 against 48, `NO_MODULE_MEMBERSHIP` 28 against 38, `PARTIAL_ALIGNMENT` 46 against 56. Flags that rise: `AIGR_NOT_COMPLETE` 85 against 8, `MODULE_NOT_COVERING` 7 against 4, `NO_AIGR_REVIEW` 61 against 5, `NO_CORE_FUNCTION_TERMS` 2 against 0.
That second run read a tree recorded at `132532cf6`, an ancestor of the branch tip, with **6416 of the audit's input files changed between the two**, so the figures below describe the recorded commit rather than the tip - e.g. `genes/AGKCO/fibrolase/fibrolase-ai-review.yaml`.

Every movement below is accounted for row by row rather than from the net counts: a flag's total can fall while rows arrive at it, and each row's cause is read from that row's own record on **both** trees, not from the flag's group. Where a flag moves in one direction only the net count is exact, and the line says so rather than implying the count was misleading.

- `ALIGNED_NONCORE` 0 against 1 moves in one direction only, so the net count is exact: 0 rows carry it on both trees, 1 left - 1 because the row has no review on the other tree (UCP2).

- `ALIGNED_ON_SHARED_NODE_ONLY` 25 against 48 moves in one direction only, so the net count is exact: 25 rows carry it on both trees, 23 left - 23 because the row has no review on the other tree (KCNJ11 (Congenital_Isolated_Hyperinsulinism), AGA, FUCA1, HNF1A, HNF4A (Hyperinsulinemic_Hypoglycemia), KCNJ11 (Hyperinsulinemic_Hypoglycemia), MT-ND1, MT-ND5, and 15 more).

- `NO_MODULE_MEMBERSHIP` 28 against 38 moves in both directions, so the net is not the movement: 14 rows carry it on both trees, 24 left - 24 because the row has no review on the other tree (LCT, DMP1, TRMT10C, HNF4A (Congenital_Isolated_Hyperinsulinism), SLC16A1 (Congenital_Isolated_Hyperinsulinism), CTNS, HNF1A, HNF4A (Hyperinsulinemic_Hypoglycemia), and 16 more); 14 arrived - 14 because the modules containing the gene differ (COX4I2, ABCD3, ABCC8 (Congenital_Isolated_Hyperinsulinism), ABHD5, APOB (Familial_Defective_Apolipoprotein_B-100), ABCC8 (Hyperinsulinemic_Hypoglycemia), APOB (Hypobetalipoproteinemia), APOB (MEND_Syndrome), and 6 more).

- `PARTIAL_ALIGNMENT` 46 against 56 moves in both directions, so the net is not the movement: 38 rows carry it on both trees, 18 left - 17 because the row has no review on the other tree (LCT, HNF4A (Congenital_Isolated_Hyperinsulinism), SLC16A1 (Congenital_Isolated_Hyperinsulinism), CTNS, AGA, FUCA1, HNF1A, HNF4A (Hyperinsulinemic_Hypoglycemia), and 9 more); 1 because the review on the other tree is a stub or has no core-function terms (PEX7); 8 arrived - 7 because the review on the flagged side is itself a stub, so the flag is an artifact of the thin review rather than a difference between the two reviews (ODC1, COX20, HSD17B4, GCK (Hyperinsulinemic_Hypoglycemia), EBP (MEND_Syndrome), COQ8B, EBP (X-linked_Chondrodysplasia_Punctata_2)); 1 because the row's own aligned terms differ, so the two reviews differ (DNAJC30).

The rises, on the same basis:

- `AIGR_NOT_COMPLETE` 85 against 8 moves in both directions, so the net is not the movement: 7 rows carry it on both trees, 1 left - 1 because the flag is itself a stub review, or the absence of core-function terms, on the tree carrying it (CTLA4); 78 arrived - 78 because the flag is itself a stub review, or the absence of core-function terms, on the tree carrying it (AHCY, ODC1, NSDHL, COQ2 (COQ2-Related_Primary_Coenzyme_Q10_Deficiency), COX18, COX20, ABCD3, ABCC8 (Congenital_Isolated_Hyperinsulinism), and 70 more).

- `MODULE_NOT_COVERING` 7 against 4 moves in both directions, so the net is not the movement: 3 rows carry it on both trees, 1 left - 1 because the modules containing the gene differ (APOB (Hypobetalipoproteinemia)); 4 arrived - 3 because the modules containing the gene differ (HADH (Congenital_Isolated_Hyperinsulinism), HADH (Hyperinsulinemic_Hypoglycemia), FGF23); 1 because the same modules carry different terms (TMEM70) - TMEM70: `mitochondrial_complex_v` covers `GO:0030674` here and nothing there.

- `NO_AIGR_REVIEW` 61 against 5 moves in one direction only, so the net count is exact: 5 rows carry it on both trees, 56 arrived - 56 because the flag is itself the absence of a review on the tree carrying it (LCT, PCSK9 (Autosomal_Dominant_Hypercholesterolemia_3), DMP1, SAR1B, MTFMT, TARS2, TRMT10C, HNF4A (Congenital_Isolated_Hyperinsulinism), and 48 more).

- `NO_CORE_FUNCTION_TERMS` 2 against 0 moves in one direction only, so the net count is exact: 0 rows carry it on both trees, 2 arrived - 2 because the flag is itself a stub review, or the absence of core-function terms, on the tree carrying it (PEX7, PEX5).

The groups below say where in the audit each flag is computed, which is why those causes are the ones available to it - not why any particular row moved.

- `NO_AIGR_REVIEW` counts rows with no review at all. This is the only risen flag the missing slices raise directly.

- `AIGR_NOT_COMPLETE`, `NO_CORE_FUNCTION_TERMS` fire where a review **was** found and is thin: a stub status, or no core-function terms to compare against. These count stub reviews present on the second tree, not reviews missing from it - a different claim, and the larger share of the movement.

- `MODULE_NOT_COVERING` cannot have either cause. All 3 module flags are computed only once a review has been found, so a missing review **removes** one rather than adding it. Which module fact moved each row is in the accounting above, per row, rather than asserted for the group here; what follows is only the shape of the two module sets: the second run reads 448 modules against 489 here, so fewer are available to cover a gene's aligned terms. The second set is a strict subset **by name**: 41 modules are here and not there (e.g. `arginine_catabolism_arginase_pathway`), and none the other way. provenance.modules records stems, so that says nothing about the contents of a module present in both - and the row accounting above attributes some arrivals to shared modules whose own terms differ, so the names are nested while the contents are not.

`ALIGNED_CONTRIBUTES_ONLY`, `PARTIAL_COVERAGE` are identical in **total** in both runs while depending on a review, so they appear in neither list above. An equal total is not an equal set of rows, and the difference matters here, so each is compared row by row below rather than read off the count.

`ALIGNED_CONTRIBUTES_ONLY` is identical row for row as well: the same rows, keyed by entry, gene and occurrence, carry the flag on each tree.
`ALIGNED_CONTRIBUTES_ONLY` is review-sourced, so a stable count there cannot be a property of the dismech side either. The reviews are not even the same: NDUFA1 is `COMPLETE` here and `INITIALIZED` on the second tree. What is stable is the contributes-to term the row aligns on, `GO:0008137` for NDUFA1, which both reports record identically - so the flag survives a change in the review around it.

`PARTIAL_COVERAGE` 14 against 14 moves in both directions, so the net is not the movement: 9 rows carry it on both trees, 5 left - 2 because the modules containing the gene differ (COX4I2, ABHD5); 2 because the row has no review on the other tree (MC4R, LIPA); 1 because the review on the other tree is a stub or has no core-function terms (PEX5); 5 arrived - 4 because the modules containing the gene differ (HADH (3-hydroxyacyl-CoA_Dehydrogenase_Deficiency), GLB1 (GM1_Gangliosidosis_Type_1), GLB1 (GM1_Gangliosidosis_Type_3), COQ8A); 1 because the same modules carry different terms (HAO1) - HAO1: `glyoxylate_oxalate_metabolism` covers `GO:0003973`, `GO:0046296` here and `GO:0003973` there. So the equal total is a coincidence of two populations, and nothing about stability follows from it.

The flags decided before any review is read are identical in both runs
(`GENE_ON_NO_NODE` 18, `NO_GO_ON_GENE_NODES` 19, `NO_ORIGIN` 3, `UNTYPED` 0), which is what separates
missing inputs from the script behaving differently - and that identity is enforced
rather than stated: the generator exits if one of those counts moves, or if the two runs
do not cover the same rows. So a second run tests that the audit works; the figures
on the project page come from the tree holding every reviewed gene, which with all
ten slices merged is this branch itself.

