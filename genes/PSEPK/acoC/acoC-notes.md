# acoC curation notes

- Identity: Q88QE1 / PP_0553, E2 of the acetoin-cleaving system. Reviewed PpG2 Q59695 and protein-level Cupriavidus P27747 were verified in UniProt.
- The OpenScientist report was integrated conservatively. Its locus and E2/lipoyl-domain conclusions agree with primary sources. Predicted catalytic-triad, AlphaFold, cytoplasmic-localization, and strain-specific regulation claims were not converted into GO annotations.
- `PTHR43194:SF2` is unrelated by name and was rejected as a functional selector.
- The sole QuickGO row was reviewed; a process row was added by orthology.


## 2026-10-26 source-specific annotation audit

The E2 reaction is retained as a strong homolog/locus inference: PpG2 Q59695 has a reviewed catalytic reaction, and the reproducible comparison finds 351 identities across 370 alignment columns (two gaps). Native KT2440 operon studies corroborate pathway placement. The old DR GO quote and submitted protein-name support are replaced with the actual curated donor reaction and primary locus evidence. The lipoyl-domain/alpha-beta-hydrolase architecture is supported, but the existing OpenScientist model-derived Ser/His/Asp mechanism is not upgraded into an experimental catalytic-residue claim. The Asta report is genuine retrieval output but largely irrelevant; both reports remain unchanged. Native E3 identity and isolated AcoC kinetics remain open.

Acquisition and preservation: the complete original review payloads and raw UniProt/GOA hashes were captured before editing in the audit baseline. All rows, including inherited proposals and retirement flags, are preserved. Actual Falcon and perplexity-lite fallback attempts failed; no provider report was fabricated. Normal gene-publication acquisition succeeded, and actual FEBA/fitness attempts failed without generating usable data. Logs are in `.cache/module-audit-logs/acetoin-pseudomonas-fetch/`; this manual research note records the independent review. PMID:7813883 remains abstract-only after normal force, publisher-page and PDF recovery attempts; the publisher minimal page adds references but not full text. Full PMID:34513815/36482024/42046433 were read where relevant. Existing provider artifacts are discovery aids, not substitutes for source verification. The annotation-reviewer consultation agreed with separating component activity from isolated-subunit catalysis, native catabolism from engineering, and condition-limited negative assays from universal absence.
