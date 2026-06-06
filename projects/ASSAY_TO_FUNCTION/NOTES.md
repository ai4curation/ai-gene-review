# ASSAY_TO_FUNCTION — working notes

Journal of decisions and findings. Append, don't rewrite.

## 2026-06-06 — project kickoff, first mining pass

- Named the project ASSAY_TO_FUNCTION (branch: gene-readout-reliability).
- Core thesis: `R → P` reliability = f(proximity, convergence); phenotypic +
  high-convergence "hub" readouts (ROS, caspase, UPR, Ca²⁺, pH, ΔΨm) are the
  over-annotation traps. GO evidence codes don't capture this axis.
- Decision: start by mining the corpus (per user) rather than writing the rubric
  first.

### What I built
- `readout_catalog.yaml` — editable, regex-based catalog of readout classes,
  each tagged proximity/convergence + GO terms it's commonly over-mapped to.
- `mine_readouts.py` — scans all `*-ai-review.yaml`, joins readout class to
  reviewer action, writes matches + crosstab + QC string-count table.

### Findings
- 1,971 files / 75,931 annotations; 1,736 matches.
- Phenotypic hubs with usable N: caspase/apoptosis 49% any-downgrade, ΔΨm 42%
  vs molecular controls (in-vitro 24%, binding 18%). Directional but weak; most
  hub classes are N<10.
- **Key negative result**: probe brand names (CellROX, DCFDA, MitoSOX, pHrodo,
  FeRhoNox) are essentially absent from curator *prose*. The review summaries
  are synthesis, not methods. So review-text mining under-captures the very
  readouts we care about.

### Bugs caught in QC (don't repeat)
- `HyPer` → matched "hyper-activation" (case + hyphen). Fix: `(?-i:HyPer)`.
- `ERSE` → matched "diverse/reverse/adverse". Fix: `\bERSE\b`. (Had inflated
  UPR 29→609.)
- `MTS` → matched "MTs" (microtubules) + mito-targeting-sequence. Fix: require
  "MTS assay/reagent/reduction".
- Lesson: always read `matched_string_counts.tsv` before believing a total.

### Next
1. Pivot to publications corpus: PMID → cached `publications/PMID_*.md` →
   detect assay in the *paper* → join to annotation action. Richer signal.
2. Add GO aspect (from `*-goa.tsv`) to test "hubs shouldn't drive MF" directly.
3. Expand catalog; build the per-readout licensing rubric with worked examples.
