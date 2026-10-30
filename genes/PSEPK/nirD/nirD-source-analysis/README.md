# NirD ligand-sequence check

Q88M68 contains cysteines at positions 18 and 95 and a single histidine at position 87.

Run `uv run python genes/PSEPK/nirD/nirD-source-analysis/check_ligands.py` from the repository root. It parses the immutable UniProt sequence with Biopython, reports the residue positions and input hash, and asserts the counts. The 120-residue target cannot provide the canonical Rieske two-cysteine/two-histidine ligand set. This alone is not a direct metal-content measurement or a universal exclusion of every noncanonical cofactor.

The target has NirD-specific NCBIfam TIGR02378, InterPro IPR017881, and PROSITE PS51300 membership. PMID:22965870 explicitly reports that Mycobacterium tuberculosis NirD has a Rieske-related fold but lacks an Fe-S cluster or other electron-transfer cofactor. Its cached abstract was read; full publisher access was blocked. This is comparative structural support, not a KT2440 structure. Together with the target sequence and family specificity, it supports rejecting the electronic canonical Rieske-cluster mapping.

`retired-proposals.yaml` preserves the exact inherited authored GO:0008942 NEW row, including its original ordinal. The original machine row is accepted as a complex contribution; the redundant authored row is retired without changing any machine payload or raw source.
