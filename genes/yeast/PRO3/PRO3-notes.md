# PRO3 (YER023W, P32263) notes

- Delta1-pyrroline-5-carboxylate reductase (EC 1.5.1.2), final step of proline biosynthesis; uses NADH or NADPH; homo-oligomer [UniProt:P32263 "Catalyzes the reduction of 1-pyrroline-5-carboxylate (PCA) to"].
- Gene-enzyme identification; overexpression raises P5CR 20-fold [PMID:2824433 "caused a 20-fold overproduction of delta 1-pyrroline-5-carboxylate reductase"].
- ORE2 = PRO3: ts cdc mutants rescued by proline [PMID:1508147 "were found to be capable of growing at the non-permissive temperature on a synthetic medium supplemented with proline"]; G1 arrest phenotype is a consequence of proline starvation.
- Cytoplasmic; compartmentalized away from mitochondrial P5C dehydrogenase (PUT2) to avoid futile cycling [PMID:7009582 "converts pyrroline-5-carboxylate to proline and is located in the cytoplasm"]; GFP cytosolic [PMID:25112878].
- Arginine catabolism: ornithine-derived P5C made in the cytosol (CAR2) is reduced by Pro3 to proline, which is then degraded in mitochondria; pro1/pro2 mutants grow without proline because of this route [PMID:25112878 "consistent with arginine catabolism supplying P5C for PRO3 in pro1 and pro2 cells"]. So arginine catabolism annotation is a genuine (non-core) participation.
- Self-interaction in three HTP interactome screens (IPI identical protein binding), consistent with homo-oligomer.


## 2026-10-26 systematic arginase-pathway audit

Reviewed every one of the 22 original annotations and all core functions using the review and annotation-reviewer workflows. Machine payloads, row order, evidence codes, qualifiers, source identifiers and WITH/FROM values were preserved. No NEW rows were added.

PRO3 activity is supported by genetic complementation and overproduction (PMID:2824433), proline rescue of ore2/pro3 mutants (PMID:1508147), and the enzyme-expression study PMID:1592829. Direct GFP and fractionation evidence establishes cytosol (PMID:25112878/7009582). The existing self-binding annotations are retained as core biochemical assembly, with tetramer stoichiometry attributed to curated UniProt rather than inferred from binary screens. Arginine-to-proline conversion remains a secondary physiological route (PMID:6997271). The ER-stress study establishes context-dependent consequences of proline depletion, not new direct chaperone activity of Pro3; no new annotation was proposed.

Normal publication caching passed. Genuine Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota errors prevented a report. Manual source review is recorded here, with no fabricated provider-named research file. Abstract-only and bibliographic-only access are distinguished from full text; unknown target supplementary details are not treated as a contradiction. Logs are under `.cache/module-audit-logs/arginase-yeast-PRO3-*`.

The initial focused validation passed. Record sections are backfilled, and final schema/term/reference validation, rendering and helper-history checks are recorded in the same log directory. Actions: ACCEPT 19, KEEP_AS_NON_CORE 2, MODIFY 1.

Final synthesis check: the historical compartmentation interpretation (PMID:7009582) does not establish absence of all proline/P5C cycling. PMID:32978391 measures mitochondrial proline uptake and P5C efflux in the regulatory context, so the description now states spatial separation without an absolute no-cycling claim.
