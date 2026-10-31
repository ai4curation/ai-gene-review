# GluRS zinc-site comparison

This analysis checks the actual ligand positions from PMID:7797500 rather than the previous incorrect four-cysteine description. See RESULTS.md for the bounded biological interpretation.

Requirements: repository Python environment (requests), MAFFT 7.x (`mafft --version` in the audit log), and just. `just all` retrieves two authoritative comparator FASTAs, extracts the target sequence from the immutable local UniProt record, aligns the proteins and maps explicit reference sites. `just align map` reuses the retained input files. The mapper is independently exercised on two reference proteins. Downloaded reference sequences are source inputs and are not hand edited.
