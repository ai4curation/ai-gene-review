# cysE (E. coli K-12, P0A9D4) curation notes

## 2026-11-03 review

- Deep research could not be generated: no provider API keys are available in
  this session. No `-deep-research-*.md` file was created; the review rests on
  the UniProt record and the cached publications below.
- Literature read (cached `publications/`):
  - PMID:3309158 (abstract): feedback-insensitive cysE mutant excretes cysteine;
    "A causal connection between this SAT sequence alteration, feedback
    insensitivity and L-cysteine excretion was demonstrated."
  - PMID:10993149 (abstract): free vs CysK-bound SAT kinetics; "The kinetics and
    kinetic constants for the wild-type SAT were not changed by the complex
    formation with OASS-A."
  - PMID:22179612 (abstract): three-stage CSC assembly; "SAT (a dimer of
    homotrimers) binds a maximum of two molecules of OASS (a dimer)".
  - PMID:10617639 (abstract, fetched for this review): "the serine
    acetyltransferase (SAT) of Escherichia coli is a hexamer."
  - PMID:2125278 (abstract, fetched): early purification and crystallisation.
  - PMID:18304323 (full text): cytosol proteomics; CysE only in supplementary data.
  - PMID:27718375 (abstract): Keio radiation screen listing cysE among hits.
  - PMID:5332668: no abstract in the cache; IDA accepted on corroborating papers.
- Decisions follow the module sibling-consistency policy: generic parents
  TOO_GENERAL, cytoplasm MODIFY to cytosol, bare protein binding REMOVE,
  cysteine synthase complex ACCEPT. Response to X-ray marked over-annotated
  (indirect knockout-screen phenotype).


## Comparative cysteine-route audit (2026-11-06)

All twelve original claims remain appropriately reviewed. The accepted cysteine synthase complex is an experimentally supported association of CysE and CysK, not proof of substrate channeling or of CysK catalysis while its active site is occupied. CysE activity is independently supported despite PMID5332668 having no accessible abstract. Cytosol fractionation rows are retained with the existing curator-deference limitation. The X-ray knockout phenotype does not establish a dedicated radiation-response mechanism; no response or virulence proposals are added.

Default Falcon research was attempted normally with --provider falcon and failed with HTTP403. No provider report was fabricated; this section records manual review.

Original GOA payloads, raw UniProt/GOA files and inherited authored proposals are preserved. Current GO checks distinguish the active cysteine synthase MF from obsolete route-specific BP terms GO:0006535 and GO:0019345. Focused gene and helper-history validations are recorded in the audit manifest.
