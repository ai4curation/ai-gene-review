# unc80 (CG18437) review notes

UniProt Q9VB11 (Protein unc-80 homolog); unc-80 family (PTHR31781). No transmembrane domains in InterPro/Pfam architecture.

## Literature journal

- Complex with NA and UNC79 [PMID:24223770 "Immunoprecipitation experiments also confirm that UNC79 and UNC80 form a complex with NA in the Drosophila brain."]
- Mutant phenotype [PMID:24223770 "These mutants display severe defects in circadian locomotor rhythmicity that are indistinguishable from na mutant phenotypes."]
- Acts in pacemaker neurons [PMID:24223770 "Tissue-specific RNA interference and rescue analyses indicate that UNC79 and UNC80 likely function within pacemaker neurons, with similar anatomical requirements to NA."]
- Mutual stabilization and extra functions [PMID:24223770 "These data indicate functional requirements for UNC79 and UNC80 beyond promoting channel subunit expression."]

## Curation decisions

- Cation channel activity (IBA/ISS) -> sodium channel activity, to be expressed as contributes_to (accessory subunit, not pore).
- Complex rows -> sodium channel complex (already IBA). Cation homeostasis IBA/ISS marked over-annotated.

## Deep research

`unc80-deep-research-falcon.md` (falcon) arrived after the review was first committed (the recipe was reported as terminated, but the falcon job completed). It agrees with the review: UNC80 is a non-pore auxiliary assembly and regulatory component of the NA sodium leak channel complex, with a function that cannot be replaced by raising NA or UNC79. It also states that UNC80 associates with membrane preparations without being a transmembrane protein, which supports the plasma-membrane refinement of the generic membrane row. Human cryo-EM places UNC79/UNC80 as a cytoplasmic scaffold beneath NALCN. No annotation decision changed.

## PR #4480 revisions

- IBA/ISS enables cation channel activity rows changed to MARK_AS_OVER_ANNOTATED (wrong qualifier for a non-pore subunit); added a NEW row contributes_to GO:0005272 sodium channel activity (IC, PMID:24223770), matching the core function.
- Human channelosome structure [PMID:34929720 "NALCN requires FAM155A, UNC79 and UNC80 to function"].
