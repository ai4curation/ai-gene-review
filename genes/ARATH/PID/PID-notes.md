# PID (PINOID; At2g34650; UniProt O64682) notes

Deep research: falcon failed (Edison API 429, 2026-10-05); review from cached publications.

## Activity
- Ser/Thr AGCVIII kinase; autophosphorylation needed for substrate phosphorylation; activated by PDK1 [PMID:16601102 "We demonstrate that intramolecular PID autophosphorylation is required for the ability of PID to phosphorylate an exogenous substrate."].
- Phosphorylates PIN loop and controls apical-basal PIN polarity [PMID:20040538 "The Ser/Thr protein kinase PINOID (PID) catalyzes PIN phosphorylation and crucially contributes to the regulation of apical-basal PIN polarity."].
- Binary switch [PMID:15514156 "Overexpression of the PINOID protein kinase induces a basal-to-apical shift in PIN localization"].
- Activates PIN efflux directly (oocytes) [PMID:24948515 "PIN-mediated auxin transport is directly activated by D6 PROTEIN KINASE (D6PK) and PINOID (PID)/WAG kinases"].

## Localization
- Cell periphery via insertion domain [PMID:16973627 "We present evidence that PID insertion domain sequences are sufficient to direct the observed peripheral localization."]; apical PM [PMID:33705718].

## Reinterpretation
- Christensen 2000 proposed negative regulation of auxin signaling [PMID:10693763]; later work (Benjamins 2001 PMID:11641228; Lee & Cho 2006 PMID:16731587) shows PID positively regulates auxin efflux/polar transport. GO:0009734 IMP marked over-annotated.
- Root hair IMP rows are from PID overexpression in root hair cells (gain-of-function) -> over-annotated.

## NEW
- GO:1901703 protein localization involved in auxin polar transport (IDA PMID:15514156) and GO:2000012 regulation of auxin polar transport (IDA PMID:24948515). PID catalyses the step (PIN phosphorylation), so it does work in the process (CLAUDE.md NEW bar).


## Polar auxin transport source audit — 2026-10-26

This dated audit supersedes conflicting earlier shorthand. All 43 original annotation payloads, including qualifiers and inherited NEW rows, were retained exactly. Every row was reconsidered against the target biology and cited sources. Actual Falcon and fallback provider attempts failed; the orchestration logs are preserved in `.cache/module-audit-logs/auxin-polar-fetch/provider-publication-results.json`. Existing provider reports, where present, served only as discovery aids. Manual primary-source inspection and normally fetched caches support the decisions below. No provider report was fabricated.

The core MF is protein serine/threonine kinase activity, refining broad kinase terms; ATP binding is integral and retained core. PIN phosphorylation influences polarity and activity in source-specific tissues/constructs. PID is not universally apical: PMID:33705718 describes apolar PID/WAG membrane distribution. An apical membrane pool does not mean exclusive apical enrichment. Direct kinase-activated PIN transport assays (PMID:24948515) must not be generalized to every possible kinase/carrier pair.

The root-hair initiation/elongation claims are overannotated for endogenous PID function because PMID:16731587 uses ectopic ATEXPA7-driven PID in the tested hair cells. The phenotype and catalytic sufficiency are real; they do not demonstrate an endogenous PID-specific hair-development role. Existing polar-transport and localization-regulation terms are assessed by their biological claim, not made artificially non-core by relation qualifiers. Both inherited NEW rows are preserved unchanged as payloads.

Nucleus IBA/ISM remain UNDECIDED. The original PTN000682243 and seed list are preserved, but a target-resolved IBD/tree placement was not recovered for the current family. Predominant PM imaging does not exclude a nuclear population. No guessed ancestral placement, donor-count argument or unobserved divergence is asserted. Bare protein-binding removals do not deny the actual regulator/substrate interactions; they apply only to the uninformative generic MF.

Final actions: 13 ACCEPT, 9 KEEP_AS_NON_CORE, 3 MARK_AS_OVER_ANNOTATED, 5 MODIFY, 2 NEW, 9 REMOVE, 2 UNDECIDED. This panel contains no negated source rows; there are no manufactured NOT assertions. Exact-row payload proof and focused validation are recorded in `.cache/module-audit-logs/auxin-polar-six-*`. Reciprocal scientific consultation with the parallel annotation reviewer confirmed source-specific localization, integral binding and substrate-assay distinctions.


## Bounded source follow-up — 2026-10-26

Narrowed GO0009734 overannotation rationale to the evidence actually established: PIN transport regulation versus inferred participation in an auxin-perception signaling cascade. Removed the categorical claim that PID cannot participate in any auxin-activated signaling and avoided equating all such pathways with TIR1/AFB. Action and original payload unchanged.
