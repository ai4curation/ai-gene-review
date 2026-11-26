# TET2 notes

- `just fetch-gene human TET2` fetched 42 GOA rows and the seeding helper emitted 41 YAML entries because one exact duplicate OGT `GO:0005515` row collapsed; this review restores the duplicate so there is one `existing_annotations` entry per GOA row.
- `just fetch-gene-pmids human TET2` confirmed all 12 PMIDs in the seeded review were cached.
- `just paint-losses human TET2` reported no IRD or IKR losses on the `TET2` lineage.
- The review accepts TET2's nuclear/chromatin DNA 5-methylcytosine dioxygenase activity as core, keeps OGT recruitment and hematopoietic differentiation as non-core contexts, modifies the generic 2-oxoglutarate dioxygenase row to `DNA 5-methylcytosine dioxygenase activity`, and removes only bare protein-binding rows.
