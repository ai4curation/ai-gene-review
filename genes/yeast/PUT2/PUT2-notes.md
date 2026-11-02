# PUT2 (P07275, YHR037W) notes

- P5C dehydrogenase, second step of proline utilization [PMID:3025596 "the second enzyme in the proline utilization (Put) pathway of Saccharomyces cerevisiae and the product of the PUT2 gene"]
- Reaction EC 1.2.1.88 [UniProt:P07275 "Reaction=L-glutamate 5-semialdehyde + NAD(+) + H2O = L-glutamate + NADH"]
- Matrix by fractionation/latency [PMID:3025596 "was localized to the matrix compartment by a mitochondrial fractionation procedure"]; UniProt says inner membrane (PMID:11502169, not cached) -> inner membrane kept non-core.
- put2 mutants lack P5C DH, cannot use proline as N source [PMID:387737 "Mutants in put1 are deficient in proline oxidase, and those in put2 lack P5C dehydrogenase"]
- Arginine degradation converges at P5C [PMID:387737 "The arginine-degradative pathway intersects the proline-degradative pathway at P5C"]

## YeastPathways / GO-CAM
- BioPAX summary: RXN-14116 has no gene in PROUT-PWY or ARGDEG-YEAST-PWY, but the YeastPathways GO-CAMs (gocams/index.tsv) DO attach PUT2 to RXN-14116 and GOA has RCA rows; both put PUT2 in cytosol (wrong, removed).
- Protein binding with Ssa2 (HT) removed.


## 2026-10-26 systematic arginase-pathway audit

Reviewed every one of the 23 original annotations and all core functions using the review and annotation-reviewer workflows. Machine payloads, row order, evidence codes, qualifiers, source identifiers and WITH/FROM values were preserved. No NEW rows were added.

Native matrix localization is directly supported by fractionation and activity latency (PMID:3025596), so broad mitochondrion is refined. The separate inner-membrane claim comes from publication-linked UniProt citing PMID:11502169: normal retrieval is abstract-only, publisher access returned 403, and PubMed indexes Put2 although its abstract omits the protein. That omission is not misattribution evidence. Matrix activity and peripheral membrane association can coexist; exact membrane association remains UNDECIDED pending the full target data. Bare Ssa2-binding rows are removed as uninformative without assuming precursor engagement or contamination. PMID:4145181 is bibliographic-only; its title is replaced as support by independent native enzyme evidence. The IBA donor list is corrected: P09546 is E. coli PutA, P10503 Salmonella PutA and Q9I5F6 Pseudomonas PutA, not human ALDH4A1. PMID:32978391 supports the regulatory/metabolic context, not a proven dedicated Put1-Put2 channeling complex.

Normal publication caching passed. Genuine Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota errors prevented a report. Manual source review is recorded here, with no fabricated provider-named research file. Abstract-only and bibliographic-only access are distinguished from full text; unknown target supplementary details are not treated as a contradiction. Logs are under `.cache/module-audit-logs/arginase-yeast-PUT2-*`.

The initial focused validation passed. Record sections are backfilled, and final schema/term/reference validation, rendering and helper-history checks are recorded in the same log directory. Actions: ACCEPT 12, KEEP_AS_NON_CORE 2, MODIFY 4, REMOVE 4, UNDECIDED 1.

The local ontology cache may warn on the older GO:0003842 label without NAD+. Live QuickGO was checked and confirms the preserved current NAD+-specific label; raw annotation IDs/labels were not rewritten to silence the stale cache.

## 2026-10-26 PR #5566 root-organelle follow-up

The mitochondrial proteome observation is independently corroborated by Put2 fractionation and activity-latency analysis in PMID:3025596. Retain the informative mitochondrial organelle claim alongside the separately supported matrix assignment. The original proteome assay need not resolve the submitochondrial compartment. Existing matrix annotations and core functions are preserved.

The current policy retains informative organelle terms; the earlier blanket MODIFY-to-matrix rationale was incorrect. Original machine annotation payloads are preserved.
