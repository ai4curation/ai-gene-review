# TET1 notes

- `just fetch-gene human TET1` seeded 48 GOA rows and fetched the shared PANTHER family `PTHR23358`.
- `just fetch-gene-pmids human TET1` confirmed all 11 PMIDs in the seeded review were cached.
- `just deep-research-falcon human TET1 --fallback perplexity-lite` could not complete because both configured providers were unavailable in this runtime, so the review used cached publications, UniProt, InterPro/PANTHER, PAINT loss output, and manual synthesis in `TET1-deep-research-manual.md`.
- `just paint-losses human TET1` reported no IRD or IKR losses on the `TET1` lineage.
- The review accepts the conserved nuclear DNA 5-methylcytosine dioxygenase activity as core, keeps CpG-DNA binding and stress/SIN3A-linked regulatory annotations where directly supported, modifies the generic 2-oxoglutarate dioxygenase row to `DNA 5-methylcytosine dioxygenase activity`, and removes only bare protein-binding rows.
