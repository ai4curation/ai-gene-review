# PET100 curation notes

## IBA / PAINT

- The pinned GOA snapshot has three `GO_REF:0000033` rows, all with
  `PANTHER:PTN002143768|SGD:S000002486` in `WITH/FROM`.
- Current local PAINT for `PTHR33968` places four IBDs on `PTN002143768`:
  `GO:0005743` mitochondrial inner membrane, `GO:0044183` protein folding
  chaperone, `GO:0033617` mitochondrial respiratory chain complex IV assembly,
  and `GO:0051131` chaperone-mediated protein complex assembly.
- The `GO:0005743` and `GO:0033617` IBAs are retained as `NO_FAILURE_CORE`.
  They are placed at the PET100-family PTN and match direct yeast evidence.
- The pinned `GO:0051082` unfolded protein binding IBA is stale relative to
  current PAINT, which now uses `GO:0044183` at the same node. The human PET100
  review marks that replacement MF as over-annotated because PET100 family
  proteins are COX-specific assembly factors, not demonstrated general
  foldases. The unfolded-protein-binding project likewise lists yeast PET100 as
  an over-annotated COX assembly factor. The same reasoning applies here: keep
  the stale row as over-annotated rather than rewriting it to another generic
  chaperone MF.
- `GO:0051131` chaperone-mediated protein complex assembly is now an IBD at the
  same PAINT node, seeded by yeast Pet100p, and should appear as an IBA after a
  GOA refresh. I left it out of `proposed_new_terms` because the retained
  `GO:0033617` IBA already captures the specific respiratory-chain complex IV
  assembly process.
- The direct `GO:0051082` row is over-annotated for the same biological reason.

## Cached literature

- The three older PMID caches used by the review are abstract-only. PMID:38612624
  is a full-text review used only as recent background.
- PMID:11498004 reports Pet100 topology in the inner mitochondrial membrane and
  describes the C-terminal domain as essential for its function as a COX-specific
  assembly facilitator.
- PMID:15507444 places Pet100 in an inner-membrane subassembly with Cox7, Cox8
  and Cox9, absent from mature holoenzyme, supporting a late complex-IV assembly
  role instead of a generic unfolded-client binding activity.
- PMID:16823961 is high-throughput mitochondrial proteomics support for a broad
  mitochondrion location only.

## 2024-2026 literature check

- PubMed searches for recent `PET100`/`Pet100` papers found no new yeast primary
  studies that change the annotation. The 2024 yeast-to-human COX-deficiency
  review keeps PET100 in late complex IV biogenesis: [PMID:38612624 "PET100 was
  first identified in yeast [74] as being required for COX assembly. PET100 was
  found to be associated with two different subassembly complexes"].
