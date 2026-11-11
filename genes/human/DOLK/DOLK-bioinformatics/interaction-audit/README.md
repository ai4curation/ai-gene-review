# DOLK interaction source audit

This analysis joins the complete saved QuickGO target response to exact IntAct MITAB records by target accession, partner accession and publication. It also recomputes participant ROGIDs from the saved official UniProt sequences and taxonomy. It does not infer a biological function or a full-length construct from the join.

Use Python 3.9 or newer; no third-party packages or network access are required. From this directory:

```sh
python3 replay.py --target Q9UPQ8 --output results --check
python3 replay.py --target Q92838 --all-incident --output secondary-results --check
```

Omit `--check` to write the outputs in the requested directory. `just check` and `just secondary` run the same saved-input checks. `pyproject.toml` records the standard-library-only dependency scope. The alternate EDA target verifies participant orientation using a different protein; it is not a complete EDA interactome query.

`source-manifest.json` records the original public URL, retrieval time and SHA-256 of every exact input. It can be used to retrieve current versions independently, but later live bytes may differ. The script authenticates all saved inputs before computing results. The MITAB response contains 112 incident DOLK records; selection is determined by all IPI partner/PMID contexts in the complete 45-row QuickGO response. Other incident records are not interpreted as negatives.

`results/contexts.json` preserves the current annotation IDs and partner-to-publication joins. `results/records.json` retains all 42 literal MITAB fields, the one-based physical line number, oriented roles, features, sequence-check fields and host. `results/summary.json` computes the totals and per-publication coverage. Coordinates in MITAB features remain source coordinates. In particular, sequence identity does not establish that the assay used the complete protein: the KCNA3 source records explicitly specify residues 53–575.

A ROGID is the base64 SHA-1 digest of the amino-acid sequence, with base64 padding removed and the taxon identifier appended. A match authenticates the reference sequence assigned to the record, not a historically unsequenced construct, a native interface or a physiological pathway. Two-hybrid validation and screening records can describe repeated stages of one experiment; they are not counted as independent physiological confirmations. AP-MS supports association rather than necessarily direct contact.
