# NirD ligand-sequence check

Q88M68 contains cysteines at positions 18 and 95 and a single histidine at position 87.

Run `uv run python genes/PSEPK/nirD/nirD-source-analysis/check_ligands.py --input genes/PSEPK/nirD/nirD-uniprot.txt --output genes/PSEPK/nirD/nirD-source-analysis/ligands.json` from the repository root. It parses the immutable UniProt sequence with Biopython, reports the residue positions and input hash, and calculates the counts. The 120-residue target cannot provide the canonical Rieske two-cysteine/two-histidine ligand set. This alone is not a direct metal-content measurement or a universal exclusion of every noncanonical cofactor.

The target has NirD-specific NCBIfam TIGR02378, InterPro IPR017881, and PROSITE PS51300 membership. PMID:22965870 explicitly reports that Mycobacterium tuberculosis NirD has a Rieske-related fold but lacks an Fe-S cluster or other electron-transfer cofactor. Its cached abstract was read; full publisher access was blocked. This is comparative structural support, not a KT2440 structure. Together with the target sequence and family specificity, it supports rejecting the electronic canonical Rieske-cluster mapping.

`retired-proposals.yaml` preserves the exact inherited authored GO:0008942 NEW row, including its original ordinal. The original machine row is accepted as a complex contribution; the redundant authored row is retired without changing any machine payload or raw source.

## 2026-10-30 three-target extension

The parameterized script was run on the existing raw UniProt files for Q88M68, P0A9I8 and A0QPK3 without editing or refreshing them. `panel-ligands.json` contains calculated positions and input hashes.

| Target | Length | Cysteine positions | Histidine positions |
|---|---:|---|---|
| PSEPK NirD Q88M68 | 120 | 18, 95 | 87 |
| ECOLI NirD P0A9I8 | 108 | 8, 20, 84 | 35, 62, 94 |
| MYCS2 MSMEG_0428 A0QPK3 | 122 | 22, 79, 98 | 15, 54 |

The **same count-based exclusion cannot be applied to all three proteins**. Only Q88M68 has fewer than two histidines. The other two have enough cysteines and histidines in total for a two-Cys/two-His set, although totals do not establish the correct geometry, motif, actual ligation or any bound cofactor. The comparative cofactor-free M. tuberculosis NirD structure and NirD-specific family identity remain relevant to all three, but these counts do not provide the additional target-specific impossibility argument used for PSEPK.

Consequently this extension does not warrant changing both other proteins to REMOVE on the same ligand-count rationale. Their existing MARK_AS_OVER_ANNOTATED decisions can retain a different evidential threshold unless a separate site/structure analysis supplies a stronger target-specific exclusion. No E. coli or M. smegmatis review was edited. Even the PSEPK count excludes the canonical Rieske ligand set rather than proving the absence of every possible noncanonical cluster-binding mode.

Reproduce with `just --justfile genes/PSEPK/nirD/nirD-source-analysis/justfile panel`; `single` reproduces the pre-existing one-target JSON format. See `RESULTS.md` for checks.
