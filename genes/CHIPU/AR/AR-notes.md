# CHIPU AR: comparative annotation review

## Provenance and scope

Normal `just fetch-gene` seeded every annotation; machine-sourced fields are preserved. Falcon deep research failed with HTTP 403 and its perplexity-lite fallback failed with HTTP 401. This is manual literature research, not a provider-generated report. Source caches were obtained through normal fetch commands and were not edited. Primary publications and curated UniProt statements were read; abstract-only evidence is not treated as proof of a wrong gene. No new biological-process annotations were proposed.

## Primary evidence

PMID:19819965 full text verifies the shark clone AB213019 (D0VX34), androgen-response-element reporter activity and ligand-dependent GFP-receptor nuclear localization. Teleost reporter experiments in that paper include western mosquitofish and must not all be attributed to medaka. The shark lacks a mammalian-like N/C-interaction motif but retains receptor function. Native organism knockout phenotypes were not established in this study.


## Selected source passages

[PMID:19819965] “the shark AR activates the target gene via androgen response element by classical androgens”

[file:CHIPU/AR/AR-uniprot.txt] “DR PROSITE; PS51030; NUCLEAR_REC_DBD_2; 1.”


## PR5554 member follow-up — 2026-10-26

Fetched the full primary 19819965 paper via the normal URL cache (PMC2795718), distinct from its abstract-only PMID cache. Figure 5 reports nuclear translocation of native shark AR in tagged COS-7 assays after DHT/11KT. Replaced the ARE boilerplate on localization and zinc-binding rows with the relevant localization and conserved zinc-finger passages. Ligand recognition remains functional inference from reporter activation and ligand-contact conservation, not a measured binding affinity.

All original annotation payloads were compared before/after and preserved; only reviewer assessments, source evidence, and the specified core-function location were changed.

## 2026-10-26 final PR evidence follow-up

Add a source-specific domain-classification finding for the declared UniProt record, without substituting a signature for experimental localization evidence.
