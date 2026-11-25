# SMDT1 notes

- `just deep-research-falcon human SMDT1 --fallback perplexity-lite` was
  attempted after the fetch step, but the Falcon and Perplexity providers were
  unavailable. No provider-named deep-research file was written; this manual
  note records the literature and model checks used for the review instead.
- `uv run python -m ai_gene_review.validation.gene_paint_losses human SMDT1`
  reported `No IRD or IKR loss on this gene's lineage.`, so the PAINT IBA rows
  to calcium import, mitochondrial calcium homeostasis, and uniplex membership
  can be judged against the positive human and metazoan evidence rather than
  against an outstanding loss.
- The reviewed GO-CAM `gomodel:65d7e4ac00001363` is aligned with the SMDT1
  review: EMRE is a single-pass mitochondrial inner-membrane MCU pore auxiliary
  subunit whose transmembrane helix activates the pore and whose acidic
  intermembrane-space tail connects MCU to MICU gatekeepers [PMID:24231807,
  "EMRE was required for the interaction of MCU with MICU1 and MICU2";
  PMID:27099988, "EMRE supports Ca2+ transport by using its TMH to bind to MCU
  through its first TMH"].
- The same GO-CAM has the same upstream citation defect as the seeded GOA row:
  its SMDT1 activity cites PMID:22925203 for calcium import, but that paper is
  about mouse Pde8b behavior. The SMDT1 review records the UniProt GOA row as a
  `WRONG_REFERENCE` source defect and keeps the calcium-import claim on the
  direct EMRE literature.
- The related calcium-free model `gomodel:65d7e4ac00001584` places the SMDT1
  adaptor activity in `GO:0072732` cellular response to calcium ion starvation.
  PMID:32494073 supports a purified MCU-EMRE-MICU1-MICU2 holocomplex in
  inhibited and calcium-activated states, not a cellular starvation response, so
  the matching GOA row is marked `MARK_AS_OVER_ANNOTATED`.
