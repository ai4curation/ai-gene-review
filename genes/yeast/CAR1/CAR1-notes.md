# CAR1 (YPL111W, P00812) notes

Evidence journal (no paid deep research run; built from UniProt and cached publications).

- Arginase, EC 3.5.3.1, homotrimer, arginase family; hydrolyses L-arginine to urea + L-ornithine [UniProt:P00812].
- Purified yeast enzyme: "The purified enzyme has a specific activity of 885 mumol urea min-1 mg-1 and a Km for arginine of 15.7 mM" and "The native trimeric enzyme has a sedimentation coefficient of 5.95 S" [PMID:2404017].
- Metals: "there is a weakly associated Mn2+ that binds to the trimeric enzyme" and "the loosely associated catalytic Mn2+ ion and the more tightly associated structural Zn2+ ion confer stability to the enzyme" [PMID:1939179].
- Induction: CAR1 mRNA "was markedly increased, however, in wild-type cells grown in the presence of inducer" and "arginase production is probably controlled at the level of gene expression" [PMID:14582193]. UniProt: induced by arginine or homoarginine [UniProt:P00812].
- Location: soluble fraction with OTCase and the other ornithine-to-arginine enzymes [PMID:205532 "the two first catabolic enzymes, arginase and ornithine aminotransferase, were in the"].
- Epiarginase regulation (moonlighting): "In this complex, arginase acts as a negative allosteric effector for ornithine transcarbamoylase" [PMID:2404017]; "OTCase and arginase form a one-to-one enzyme complex in which the activity of OTCase is inhibited whereas arginase remains catalytically active" and "In arginase, two cysteines at the C terminus of the protein are crucial for its epiarginase function but not for its catalytic activity and trimeric structure" [PMID:12679340].

## Curation decisions
- Core MF 1: GO:0004053 arginase activity; BP GO:0006527 L-arginine catabolic process; CC cytosol.
- Core MF 2: GO:0090369 ornithine carbamoyltransferase inhibitor activity, in GO:1903269 complex with ARG3 (prevents futile cycling of arginine synthesis/degradation).
- Urea cycle (IBA/IEA/IDA/IMP): yeast is not ureotelic; arginase is the first step of arginine catabolism to use arginine as nitrogen source (urea is further hydrolysed by DUR1,2). Experimental rows MODIFY -> L-arginine catabolic process; IBA MARK_AS_OVER_ANNOTATED (consistent with ARG1 review).
- protein binding (ARG3) REMOVE: superseded by complex/inhibitor annotations (consistent with ARG3 review).


## 2026-10-26 systematic arginase-pathway audit

Reviewed every one of the 33 original annotations and all core functions using the review and annotation-reviewer workflows. Machine payloads, row order, evidence codes, qualifiers, source identifiers and WITH/FROM values were preserved. No NEW rows were added.

The urea-cycle rows are retained as contextual participation rather than rejected by an invalid ureotelic restriction. GO:0000050 describes ornithine-to-arginine synthesis and hydrolysis back to ornithine plus urea. The CAR1-ARG3 inhibitory complex (PMID:12679340) constrains simultaneous flux but does not erase the reaction topology. Generic protein binding is refined to the directly established OTC-inhibitor activity. PMID:1939179 measures about one weak catalytic Mn per subunit and a tighter site predominantly occupied by Zn (sometimes Mn), with metal-dependent stability of the trimer; structural Zn binding is a core property, not peripheral simply because it is structural. The full PMID:19053807 text explicitly names Car1 among the screen hits, supporting a contextual shmoo-tip location without adding a mating function. Nuclear localization is retained as the curated observation, without invented passive-diffusion explanation.

Normal publication caching passed. Genuine Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota errors prevented a report. Manual source review is recorded here, with no fabricated provider-named research file. Abstract-only and bibliographic-only access are distinguished from full text; unknown target supplementary details are not treated as a contradiction. Logs are under `.cache/module-audit-logs/arginase-yeast-CAR1-*`.

The initial focused validation passed. Record sections are backfilled, and final schema/term/reference validation, rendering and helper-history checks are recorded in the same log directory. Actions: ACCEPT 20, KEEP_AS_NON_CORE 6, MODIFY 7.


## PR #5563 narrow synchronization, 2026-10-26


Copied the four GO:0000050 row reviews exactly from the completed PR #5566 arginase audit. The term does not require ureotelic excretion. Native arginase supplies the urea/ornithine-generating reaction; the CAR1-ARG3 inhibitory interaction constrains simultaneous cycling and does not establish steady-state full-cycle flux. These rows are contextual non-core, consistent with the other fungal cycle enzymes. All original row payloads and unrelated CAR1 review decisions are preserved.


## 2026-10-26 integration provenance

Preserved the approved arginase audit and the published arginine follow-up notes together. This is a journal union; no CAR1 annotation, action, core function or source record changed.
