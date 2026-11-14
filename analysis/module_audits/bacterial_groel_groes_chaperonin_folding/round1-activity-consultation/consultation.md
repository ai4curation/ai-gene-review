# PR6164 activity consultation receipt

Assessed review5809803940 important items2/3 and suggestion8 independently. Baseline is published HEAD04e7322f4c2f032c8f88737ba78bf3197563f2ba. Scope is MYCTU/groEL2 and ECOLI/groS only.

Two action changes: GroEL2 GO0005515/PMID12198306 REMOVE→MODIFY with replacement GO0042802, grounded in self-partner/dimer evidence plus independent solution oligomers; E. coli GroES GO0046872 KEEP_AS_NON_CORE→MARK_AS_OVER_ANNOTATED, because ion-dependent DLS assembly and proposed coordination do not sufficiently establish target metal binding. The valid Mtb source and PAINT node are preserved, with propagation mechanism explicitly unresolved. No claim that high calcium alone proves artifact or that an absent affinity measurement automatically invalidates every IBA is made. GroEL2 GO0044183 stays ACCEPT with an explicit explanation that its non-ATP activity adds coverage beyond GO0140662.

Suggestion7: the E. coli GroES core already has GO0051087, contributes_to GO0140662 and in_complex GO1990220, with folding-process/cytosol context and direct complex evidence. No core change was warranted.

Both reviews remain COMPLETE. All64 annotation payloads and row order remain identical; no NEW, deletion or retirement occurred. Forty-six protected raw/provider/publication files remain byte-identical. Action totals are29 ACCEPT,18 MODIFY,12 KEEP_AS_NON_CORE,2 REMOVE,2 UNDECIDED,1 MARK_AS_OVER_ANNOTATED. The three edited review objects and reasons are ledgered in preservation.json.

Primary Methods/Results/Table2 of PMID12837792 and accessible original abstracts/curated source statements were inspected; no inaccessible full-text details were invented. No source cache or previous source-analysis note was edited. Existing notes now record the new assessment as superseding the earlier endorsement. No new provider research was required for this focused source adjudication.

Both focused validations, both renders and both generated history validations passed. File-scoped Ruff, preservation and diff-check passed. A formatting cleanup after validation preserved the complete parsed documents exactly and reduced the diff to edited blocks; validation.json records that comparison. No module/project/family/other gene edits, full validation, commit or push were performed. Root owns integration and any coverage checker expectations affected by the two action changes.
