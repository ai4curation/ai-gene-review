# Observed comparator data

The complete live combined query returned 97 records; the LMAN2 query returned 17. Each response is byte-for-byte identical to its corresponding original snapshot. In particular, the combined response SHA256 is `a7b92a379413a4a6a44b5322f22c9a1893154d2b7f0d03348dce0790053b4ef2` (45,011 bytes), and it contains both disputed IDs `UniProtKB:P27824!357439916` and `UniProtKB:P49257!357460020`. The latter literally carries IDA, assignedBy WB and PMID:10559958. These observations establish what the endpoint returned, not whether its biological attribution is correct.

The independent repository TSV comparison finds 46 versus 45 CANX CC records, 41 versus 41 LMAN1 and 17 versus 17 LMAN2. Across the nine explicitly compared fields, the API-only/TSV-only multiset differences are 9/8, 11/11 and 5/5 respectively. These include metadata changes such as dates; equal counts do not imply identical records. The exact projections are in the YAML report. No cause for these differences has been established.

The second input selects only LMAN2 and lowers the page size to five. All four pages were retrieved, their unique record count equals 17, and the complete record objects match the original one-page snapshot. Raw page hashes naturally differ for this differently paginated representation. Offline replay reproduces the comparison from the downloaded pages; hash-corruption and incomplete-page controls fail rather than silently accepting partial or modified input. These controls are verification of the comparison, not biological experiments.

- [x] Script inputs are parameterized; no biological outcome or expected comparison result is hardcoded.
- [x] A distinct LMAN2-only input exercises four-page retrieval.
- [x] Both complete queries, the pagination control and offline replay completed.
- [x] Raw responses, manifests, HTTP receipts and structured results are included here.
- [x] Tampered-hash and incomplete-page controls are rejected.
- [x] Provenance and limitations are explicit; no annotation action is inferred by the code.

CLN6's unchanged membrane refinement is supported by its topology and GO membrane guidance. This comparison is corroborating provenance about other annotation records, not an independent CLN6 experiment.
