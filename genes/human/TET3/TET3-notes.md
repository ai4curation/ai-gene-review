# TET3 notes

- `just fetch-gene human TET3` fetched 36 GOA rows and the seeding helper emitted 32 YAML entries because two exact duplicate OGT `GO:0005515` rows and duplicate mouse-supported ISS rows collapsed; this review restores the duplicates so there is one `existing_annotations` entry per GOA row.
- `just fetch-gene-pmids human TET3` confirmed all 5 PMIDs in the seeded review were cached.
- `just paint-losses human TET3` reported no IRD or IKR losses on the `TET3` lineage.
- The review accepts TET3's DNA 5-methylcytosine dioxygenase activity, nucleus/chromosome/male-pronucleus localization, and zygotic epigenetic-programming rows, modifies CXXC-domain methyl-CpG rows to `unmethylated CpG binding`, keeps cytoplasm and OGT-linked glycosylation as non-core, and removes only bare protein-binding rows.
