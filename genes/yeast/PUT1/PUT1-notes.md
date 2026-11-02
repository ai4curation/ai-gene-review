# PUT1 (YLR142W, P09368) notes

- Mitochondrial FAD-dependent proline dehydrogenase (proline oxidase, EC 1.5.5.2), first step of proline degradation to glutamate (with PUT2) [UniProt:P09368 "Converts proline to delta-1-pyrroline-5-carboxylate."].
- put1 mutants lack proline oxidase and cannot use proline as N source; induced by proline [PMID:387737 "Mutants in put1 are deficient in proline oxidase"].
- Mitochondrial import signal; lacZ fusions mitochondrial [PMID:3125423 "two PUT1-lacZ gene fusions were constructed that produced mitochondrially localized beta-galactosidase in vivo"]. Mitochondrial proteomes [PMID:14576278; PMID:16823961].
- Purified recombinant Put1p: bound flavin, Km 36 mM proline, uses CoQ1 as acceptor [PMID:20450881 "Put1p also exhibited high activity using ubiquinone-1 (CoQ(1)) as an electron acceptor"]. Electrons pass to the respiratory quinone pool; ETF not required [PMID:20450881 "demonstrating that ETF is not required for proline utilization in yeast"].
- UniProt places it in the matrix; given quinone use it is presumably at the matrix face of the inner membrane (not experimentally resolved in cached literature).
- YeastPathways RCA rows put Put1 "is_active_in cytosol" for PROUT-PWY and ARGDEG-YEAST-PWY: contradicted by mitochondrial localization; flagged for removal.
- Arginine catabolism: in yeast arginine nitrogen is released via ornithine -> P5C -> proline -> (Put1) P5C -> (Put2) glutamate [PMID:387737 "The arginine-degradative pathway intersects the proline-degradative pathway at P5C"].


## 2026-10-26 systematic arginase-pathway audit

Reviewed every one of the 20 original annotations and all core functions using the review and annotation-reviewer workflows. Machine payloads, row order, evidence codes, qualifiers, source identifiers and WITH/FROM values were preserved. No NEW rows were added.

Purified-protein PMID:20450881 demonstrates FAD-associated proline dehydrogenase and strong CoQ1 electron acceptance; low oxidase turnover does not make oxygen the obligatory immediate acceptor. ETF knockout growth tests support dispensability of ETF for the tested yeast proline use. PMID:3125423 demonstrates mitochondrial targeting and explicitly shows high expression in respiratory-deficient cells; the old assertion that expression requires a functional respiratory chain is corrected. Oxygen-regulated transcription is distinct from respiratory coupling of proline utilization. Matrix assignment remains curated/comparative; membrane topology is not newly measured here. PMID:32978391 measures mitochondrial proline uptake and metabolite flux in Put6/Put7 mutants but does not identify those factors as the carrier. No transport activity is assigned to Put1.

Normal publication caching passed. Genuine Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota errors prevented a report. Manual source review is recorded here, with no fabricated provider-named research file. Abstract-only and bibliographic-only access are distinguished from full text; unknown target supplementary details are not treated as a contradiction. Logs are under `.cache/module-audit-logs/arginase-yeast-PUT1-*`.

The initial focused validation passed. Record sections are backfilled, and final schema/term/reference validation, rendering and helper-history checks are recorded in the same log directory. Actions: ACCEPT 17, KEEP_AS_NON_CORE 1, REMOVE 2.
