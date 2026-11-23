# bdhA curation notes

- Identity: Q88QE2 / PP_0552, EC 1.1.1.4. PpG2 Adh Q59696 is the exact 362-aa source-linked homolog from PMID:7813883.
- `PTHR43161:SF26` is named galactitol 1-phosphate 5-dehydrogenase and was rejected as a specificity selector for this module.
- All four QuickGO rows were reviewed. Broad oxidoreductase parents are over-annotations; zinc binding is credible non-core cofactor information.
- No completed gene-level OpenScientist artifact was present for bdhA. Research was not restarted.


## 2026-10-26 source-specific annotation audit

The earlier specificity uncertainty is superseded by full PMID:34513815. Methods explicitly amplify pp0552, express pETDuet-pp0552 and purify the protein. Figure 3 and Tables 1–3 establish R,R/meso oxidation with NAD+, reverse acetoin reduction, and R-acetoin-forming diacetyl reduction. Table 2 finds no detected NADP(H)-supported activity. Figure 4 shows deletion affects R,R/meso growth but not acetoin or pyruvate; S,S utilization is supplied by PedE/PedH. Thus GO:0000721 is accepted and both broad redox rows refined to supported substrate-specific reactions. The inherited acetoin-catabolism proposal is refined laterally to butanediol catabolism, not deleted as a duplicate. Zinc binding is integral, supported by RuleBase plus the zinc-ADH signature; inhibitory excess zinc is not evidence against bound catalytic zinc. No new annotation row was added. The old module-specific description and name-only support were replaced.

Acquisition and preservation: the complete original review payloads and raw UniProt/GOA hashes were captured before editing in the audit baseline. All rows, including inherited proposals and retirement flags, are preserved. Actual Falcon and perplexity-lite fallback attempts failed; no provider report was fabricated. Normal gene-publication acquisition succeeded, and actual FEBA/fitness attempts failed without generating usable data. Logs are in `.cache/module-audit-logs/acetoin-pseudomonas-fetch/`; this manual research note records the independent review. PMID:7813883 remains abstract-only after normal force, publisher-page and PDF recovery attempts; the publisher minimal page adds references but not full text. Full PMID:34513815/36482024/42046433 were read where relevant. Existing provider artifacts are discovery aids, not substitutes for source verification. The annotation-reviewer consultation agreed with separating component activity from isolated-subunit catalysis, native catabolism from engineering, and condition-limited negative assays from universal absence.

Historical-proposal bookkeeping: The inherited acetoin-process proposal is retained as a retired historical record with its lateral butanediol-process refinement; it is not a current GOA assertion. Parent authorized this explicit `retired: true` metadata addition. Original term, evidence, reference, qualifier and row order remain unchanged; the preservation report lists this metadata delta separately.

## 2026-11-02 — acetoin/butanediol module completion pass

- Deep research: no provider deep-research file exists for this gene, and none could be generated
  in this session (no deep-research provider API keys were configured). No deep-research file was
  written by hand. The review rests on the cached primary publications, the UniProt record and the
  PANTHER/PAINT family files cited in the review.
