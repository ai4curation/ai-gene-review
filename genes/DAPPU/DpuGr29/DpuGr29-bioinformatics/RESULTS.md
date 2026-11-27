# DpuGr29 report motif verification

On 2026-09-20, `scan_motif.py` independently scanned the unchanged UniProt flat-file sequence using the report's explicit `TY.{5}QF` pattern. E9FXF3 contains 379 residues and one match: TYLVILYQF at residues 364-372 inclusive. This reproduces the provider's sequence claim. The unrelated 192-residue human AKIRIN1 input has no match; it tests that the program consumes its input rather than returning a target-specific constant.

The target's predicted final helix is 354-372 in the UniProt record. PMID:38573859 experimentally relates the corresponding BmGr9 family-signature region to pore/gating structure. A sequence motif match is compatible with the GR fold but does not establish DpuGr29 conductance, cation selectivity, ligand or oligomerization. No structural alignment, pore geometry or target functional assay was performed. Consequently this check does not reinstate the withdrawn GO:0099094 NEW annotation.

Provenance: adjacent target UniProt record; unrelated input `genes/human/AKIRIN1/AKIRIN1-uniprot.txt`. Exact SHA256 hashes and pattern/coordinate output are in `target-motif.json` and `control-motif.json`. Python 3.12.9, standard library only; local uv lock and justfile make the execution reproducible.

- [x] Script input paths and motif are arguments; results are computed without hardcoded target coordinates or matches.
- [x] Tested on a second, unrelated input.
- [x] Both analyses completed successfully.
- [x] Raw output and input hashes are preserved.
- [x] Conclusions are restricted to sequence-pattern presence; functional uncertainty is explicit.
