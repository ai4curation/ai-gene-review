# lon-2 (Q18530) review notes

- Deep research: falcon rerun (1500 s) succeeded: `lon-2-deep-research-falcon.md`.
- Q18530 is TrEMBL but is the only lon-2 entry; the module uses the same accession.
- Glypican HSPG and negative regulator of DBL-1 signaling [PMID:17240342 "LON-2 negatively regulates a BMP-like signaling pathway that controls body length"].
- Key revision: LON-2 binds human BMP2 in vitro [PMID:17240342], but no direct LON-2/DBL-1 interaction was detected. SMOC-1 bridges the two [PMID:37590248 "We did not detect any interaction between LON-2 and any form of DBL-1"].
  - The growth factor binding IPI is therefore kept as non-core and not used as the core MF.
  - The module uses GO:0019838 growth factor binding as the LON-2 MF; the curator should note this caveat.
- Two domains (N-terminal furin product; C-terminal HS-attachment region) can inhibit independently [PMID:22922164].
- IBA synapse and regulation of protein localization to membrane are marked over-annotated: these are vertebrate glypican functions.
