# clec-67 review notes

## 2026-10-28 initial review

- Fetched with `just fetch-gene worm clec-67` (after UniProt rate-limit retries). UniProt id
  Q8ITX4 confirmed; 4 GOA rows.
- No deep-research provider keys; manual literature work in `clec-67-deep-research-manual.md`.
- Bioinformatics: `clec-67-bioinformatics/ctld_motifs.py` - CTLD has 3 Cys, no EPN/QPD/WND.

### Decisions
- GO:0044183 protein folding chaperone (IC, WB, with GO:0036498): the inference chain
  "induced in the UPR -> chaperone" does not hold for a secreted CTLD protein with no chaperone
  domain. REMOVE, with a source_defect (WRONG_TERM, PROBABLE) to WormBase.
- GO:0006457 protein folding (IEA GO_REF:0000108): mechanically derived from the chaperone IC row;
  REMOVE together with it.
- GO:0036499 PERK-mediated UPR (HEP): being a pek-1-dependent transcriptional target is not
  participation in the signalling pathway; MARK_AS_OVER_ANNOTATED (consistent with nsf-1, snap-1
  handling of the same paper). Supplementary Table S2 not cached, so the target status itself is
  deferred to the WormBase curator.
- GO:0030246 carbohydrate binding (IEA UniRule): CTLD present but non-canonical (UniProt CAUTION;
  our motif scan). MARK_AS_OVER_ANNOTATED; carbohydrate binding untested.
- Not proposed as NEW: defense response to Gram-negative bacterium / innate immune response.
  Evidence is induction (expression) plus one survival phenotype of a deletion mutant
  [PMID:30177956 "clec-67 mutants had one of the highest hazards in response to JCMS"]; this
  does not show that CLEC-67 itself performs a step of defense, so the NEW bar is not met.
  Raised as a suggested question/experiment.
