# PTEN review notes


## 2026-09-20 focused nuclear/cell-cycle report incorporation

The complete nuclear-localization-and-cell-cycle OpenScientist report was read, including its evidence matrix, proposed sequence analysis, limits and artifacts. Its recommendation is disputed. GO:0051726 is an existing source IBA and is present at PTN000959472 in the PAINT slice, contrary to the report's claim that it is absent. Cytokinesis is part of cell-cycle progression; a lack of a nuclear checkpoint phenotype does not refute a broader inherited regulatory role. PTEN contributes cortical phosphoinositide regulation and AprA-dependent proliferation control (PMID:38940195). The cell-cycle row remains KEEP_AS_NON_CORE.

The report additionally misstates PMID:15809030 as PTEN loss with intact PI3K: the accessible primary abstract says “Cell lines lacking both of these enzymatic activities fail to modulate PI(3,4,5)P3 levels”. This does not negate the independently documented target cytokinesis function, but limits the claimed genotype-specific discriminator. The report also repeats the membrane-positive-imaging/nuclear-negative inference despite acknowledging no dedicated nuclear assay. The nucleus IBD includes worm as well as mammalian experimental descendants, so mammal-only evidence is an inaccurate premise.

Its new potentially useful lead is claimed divergence at human PTEN K289, but its own caveat says “the exact single-residue call is low-confidence”. Only final-report HTML/PDF artifacts were delivered, without code, actual alignment or numerical output to reproduce the claimed 45% identity or K289-to-E assignment. Those values are not adopted as verified analysis. More importantly, the primary human import paper PMID:17218261 says the mutation-induced shuttling defect “can be overcome by forced mono-ubiquitination”. A human sequence substitution phenotype is not automatically equivalent to the same aligned residue in an independently evolved ortholog. Nuclear localization remains UNDECIDED, with human follow-up for a reproducible structural/MSA comparison and endogenous nuclear imaging/fractionation under defined conditions. Do not add a NOT or launch a duplicate report.


## Recovery PR evidence refinement (2026-09-22)

Restore direct Dictyostelium cytokinesis evidence to the cell-cycle row and remove a report error from positive support. Source GOA assertions are unchanged.
