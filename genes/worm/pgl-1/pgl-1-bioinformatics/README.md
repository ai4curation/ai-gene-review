# PGL-1 focused motif audit

This small analysis checks the explicit sequence-pattern claims in the focused
OpenScientist report. It is not a phylogenetic reconstruction or an activity assay.

Run `just` in this directory to reproduce `motif-results.json` from the saved inputs.
Run `just fetch` only to obtain new live UniProt/InterPro snapshots; this overwrites
these analysis inputs, so retain the versioned inputs to reproduce the present result.
The canonical gene-level UniProt and GOA snapshots are untouched.

`scan_motifs.py` accepts arbitrary UniProt JSON files and an external JSON pattern
mapping. `fetch_records.py` accepts accession arguments, checks UniProt accession
identity, follows InterPro pagination, and records exact URLs, UTC retrieval times,
and SHA-256 hashes in `source-provenance.json`. InterPro pages are saved separately
without editing their contents. Neither script embeds biological conclusions.

Python 3.12.9 was used through uv; only the Python standard library is required.
`pyproject.toml` and `uv.lock` record the environment. The regular expressions in
`patterns.json` are explicit audit parameters. Coordinates are one-based and inclusive.
No score threshold or random procedure is used in the short-pattern scan.

Read RESULTS.md for the interpretation and the limitations of negative motif scans.
