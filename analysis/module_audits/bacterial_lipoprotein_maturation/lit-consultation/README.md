# Lit consultation release

Verified single exemplar: BACCR/BC_1526, Q813T3, Bacillus cereus ATCC14579. Primary34253723 explicitly names this accession; discovery28320885 establishes the native locus/product phenotype. Enterococcus ATCC19433 WMC_RS08810 from32471867 could not be mapped to a current official accession, so no Enterococcus review was guessed or seeded.

The zero-row GOA seed is preserved. Three authored NEW proposals cover0016867 intramolecular acyltransferase activity,0042160 lipoprotein modification and0005886 plasma membrane. One core captures the exact sn-2 O-to-N relocation; no additional acyl chain is introduced. No PANTHER family or unsupported immune/copper activity is asserted. Source-specific mechanism boundaries and comparator limitations are in primary-scope.md.

Focused gene validation, generated history validation, rendering and parsed-HTML inspection pass. Ruff and source-preservation checks pass. Initial validation caught incorrectly shaped question objects; only that schema formatting was corrected before successful revalidation. PAINT cannot run lineage assessment without an official PANTHER family; this is not evidence of absence of losses. The configured Falcon provider failed authentication403; no research report was fabricated.

Reproduce with `just validate BACCR BC_1526`, `just render BACCR BC_1526`, and `uv run python analysis/module_audits/bacterial_lipoprotein_maturation/lit-consultation/check_preservation.py`. The latter checks62 protected files and explicit NEW accounting. Normal fetched new publications28320885 and34253723 are included in the handoff; pre-existing32471867 and all57 initial protected sources remain unchanged.

No module, family, project or previously released review was edited. No full-corpus validation, commit or push was performed. Ownership is released by handoff.yaml. Subsequent amendments require an additive versioned receipt.
