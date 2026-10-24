---
title: Additional pombe prediction availability check
autolink_gene_symbols: false
---
# Additional pombe prediction availability check

Joining the original 28,553-record XML export against current UniProt pombe primary **and secondary** accession identifiers recovers the same 28 entries, with no additional matches. The [summary](summary.json) records the full source hashes and matched identifiers. The [compressed accession-line extract](uniprot-accession-lines.txt.gz) retains the unmodified ID/AC lines of the source flat file, sufficient to reconstruct its accession groups without keeping an additional full proteome download.

The [96 additional API probes](extra-api-probes.json) all returned HTTP 404. They are the first 96 primary accessions in lexicographic order outside the known 28 in the frozen 5,228-record taxonomy index. This is a sample of additional candidates, not proof that no other pombe predictions exist anywhere in the current API.

The 20 GO/function-bearing pombe genes are therefore the complete set identified by this export-based search. The next 20-gene function review cohort uses [Neurospora](../../neurospora.md), which has 16 GO/function-bearing records plus four selected localization cases.
