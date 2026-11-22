# PFD1 re-review notes

## 2026-09-28 IBA and cached-publication pass

- Reviewed `PFD1-ai-review.yaml`, `PFD1-uniprot.txt`, `PFD1-deep-research-falcon.md`, and the cached publications for the PMID-backed rows.
- Current PAINT in `interpro/panther/PTHR20903/PTHR20903-paint.tsv` places `GO:0005737`, `GO:0006457`, and `GO:0044183` at `PANTHER:PTN002325135`. Pfd1 (`P46988`) is in `PTHR20903:SF0`, so the cytoplasm, protein folding, and protein folding chaperone IBAs are sound core prefoldin transfers.
- The pinned GOA still contains a `GO:0051082` IBA, but the current PTHR20903 PAINT snapshot no longer has `GO:0051082` at `PTN002325135`. It already carries `GO:0044183` at the same node, matching the `UNFOLDED_PROTEIN_BINDING` project's `PFD1 | S. cerevisiae | P46988 | MODIFY -> GO:0044183` decision for prefoldin subunits.
- `GO:0005515` rows from the high-throughput interaction publications remain too generic to retain as separate molecular-function annotations. Removing these rows does not dispute the observed physical associations; prefoldin complex membership and `GO:0044183` capture the functional interaction context.

Cached publications checked:

- `PMID:9630229` is abstract-only locally. Its abstract identifies prefoldin as a heterohexameric chaperone that captures unfolded actin, binds cytosolic chaperonin, transfers targets to it, and produces actin/tubulin cytoskeleton phenotypes when a prefoldin subunit is deleted in yeast.
- `PMID:9463374` is abstract-only locally. Its abstract describes the yeast Gim proteins as a protein complex that promotes functional alpha- and gamma-tubulin formation.
- `PMID:9878052` is abstract-only locally. Its abstract says GimC accelerates actin folding on TRiC at least 5-fold and prevents premature release of non-native protein from TRiC.
- `PMID:16429126` and `PMID:16554755` are abstract-only large-scale yeast complex surveys.
- `PMID:19536198` has full text locally. It treats prefoldin/GimC as a stable chaperone complex in the yeast chaperone network and reports indirect TAP-tag interaction data.
- `PMID:24068951` is abstract-only locally. Its abstract supports the secondary role of prefoldin in transcription elongation and chromatin dynamics.
- `PMID:37968396` has full text locally. It is a 2023 yeast interactome resource and corroborates prefoldin co-complex interactions.

Newer literature search:

- PubMed query for `(Saccharomyces OR yeast) AND (PFD1 OR GIM6 OR YJL179W OR prefoldin)` in 2024-2026 found papers on Gim3/Pfd4 meiotic tubulin homeostasis, Gim3 fluconazole mutational robustness, HTD1265-induced GimC phenotypes, prefoldin-like Bud27/URI, a plant-prefoldin review, and non-PFD1 topics.
- Web searches for `Saccharomyces PFD1 Gim6 prefoldin 2024 2025 2026`, `YJL179W Pfd1 Gim6 yeast prefoldin 2024`, and exact titles for the 2026 GimC/Gim3 papers did not find a newer Pfd1-specific molecular-function paper or any evidence changing the canonical prefoldin interpretation.

## 2026-10-01 current GOA refresh

- `just fetch-gene yeast PFD1 --force` refreshed PFD1 to 13 live GOA rows. The
  live IBA set now has only `GO:0006457` protein folding, `GO:0005737`
  cytoplasm and `GO:0044183` protein folding chaperone from
  `PANTHER:PTN002325135`; all three remain `NO_FAILURE_CORE`.
- The historical `GO:0051082` unfolded protein binding rows and five generic
  `GO:0005515` protein binding IPI rows are absent from live GOA after the
  refresh and are retained as `retired: true` source assertions.
- The refresh added a ComplexPortal `PMID:9463374` IPI `GO:0016272` prefoldin
  complex row. The cached paper is abstract-only, but its abstract places Gim
  proteins in common cytoplasmic complexes and the later prefoldin discovery
  paper explicitly established prefoldin as a heterohexameric chaperone, so the
  new row was accepted.
- Searches through 2026 found the 2026 Gim3/Pfd4 meiotic-spindle paper
  [PMID:42647631 "Gim3 functions as part of the prefoldin complex, with tubulin
  as a key client"]. The paper is relevant complex-level context, but it assays
  a different beta-type prefoldin subunit and does not require new direct PFD1
  annotations.
