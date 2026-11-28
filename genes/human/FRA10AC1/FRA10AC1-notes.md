# FRA10AC1 notes

## Manual literature review

- Deep research could not be generated for this family because the configured `falcon` and `perplexity` providers were unavailable in the local runner (`agentapi not found`; fallback providers unavailable). I reviewed the fetched UniProt, GOA, PANTHER/PAINT, and cached PMID records manually.
- FRA10AC1 is the catalytic-loss branch inside PTHR11567. PAINT already records an IRD at `PANTHER:PTN000170711`, so the broad root phosphatase IBD no longer reaches the human FRA10AC1 leaf.
- PMID:34694367 supports nuclear localization, ESS2/spliceosomal C-complex association, and a role in pre-mRNA splicing. The remaining protein-binding rows are generic interactome or spliceosome-complex contacts and were removed under the bare protein-binding policy.
