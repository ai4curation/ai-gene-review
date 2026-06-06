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

## 2026-06-06 (cont.) — publications-corpus pass (mine_papers.py)

Coverage: 36,449 of 36,660 PMID-backed annotations resolved to cached papers.
16,682 paper-level matches; 722 thematically aligned (high-precision subset).

### Perf war story (don't repeat)
- v1: 80 regex/annotation over full text → killed at 280s.
- v2 memoize per pmid + 1 alternation/class → still ~10min (IGNORECASE scan of
  ~MB papers is ~0.15s each, ×12 classes ×many large papers).
- v3 combined single regex w/ named groups → SLOWER (0.2s/MB ×, alternation
  tries every branch per char). Reverted.
- v4 WINNER: two-stage filter. Cheap literal substring screen (necessary
  superset per class, `SCREEN` dict) gates the precise regex. Validated 0 lost
  matches vs regex-only on 350 papers (incl 50 largest). Full run ~4 min.
- Keep text original-case so case-sensitive `(?-i:HyPer)` works; screen on a
  lowercased copy.

### Findings (the good stuff)
- **Aspect constraint CONFIRMED**: aligned hub readouts license BP (or CC for
  ΔΨm = mito localization), essentially never MF. Caspase BP68/MF0, ROS BP10/MF0,
  viability BP87, autophagy BP109. Only exception: transcriptional reporters
  MF71 — but those are real TF-activity terms on real TFs, mostly ACCEPT. Not
  over-annotation.
- **Real failure mode = non-core demotion, not error.** Hard removal (rm/OA) of
  hub-readout annotations is ~comparable to molecular evidence (~27%). The
  difference: viability (58/90) and apoptosis (34/63) aligned annotations get
  KEEP_AS_NON_CORE. So hubs inflate the annotation set with correct-but-
  peripheral BP terms rather than producing wrong calls.
- ΔΨm is the one hub with elevated *hard* downgrade (21%), often via MODIFY —
  refined to more proximal terms.
- Caveat: any-downgrade is 40-60% for ALL classes incl molecular (dominated by
  NON_CORE/MODIFY refinements). Don't headline that number; headline aspect +
  non-core breakdown.

### Next
- Build the licensing rubric (per readout: aspect allowed, default core/non-core).
- Tighten paper→annotation link (title/abstract or methods-section only).

## 2026-06-06 (cont.) — rubric built

- RUBRIC.md (narrative + decision procedure + quick-ref table + worked
  contrasts) and rubric.yaml (machine-readable) written.
- Core rule: phenotypic hub readout -> BP/CC "response to/regulation of P",
  never MF, default non-core; promote to core only if gene is in P's recognized
  machinery/sensor set. MF exception: transcriptional reporter for a real TF.
- Every per-class rule anchored to ACCEPT-vs-downgrade corpus contrasts (BCL2 vs
  Akt1; CDK1 vs ACTB; TP53 vs PEX10/13; ATF4 vs HSPA1A + IRE1 MF over-call;
  AMBRA1 vs ABI2; ATF2/ASCL1 vs AIP). All examples verified against
  paper_readout_matches.tsv.
- Next: operationalize as a flagger (hub-readout + MF aspect, or core-call on a
  non-machinery gene = re-review candidate).

## 2026-06-06 (cont.) — flagger built

- flag_candidates.py consumes paper_readout_matches.tsv, applies rubric, writes
  reports/flagged_candidates.tsv. Flags only standing + hub-aligned annotations.
- Tier 1 (MF from hub): 7. Exactly the predicted pattern — reporter-driven
  coactivator/corepressor MF for non-TF coregulators (CTNNB1, NOTCH1, SIRT1,
  HMGB1) + Ca2+-binding MF (Calm2, HRC) that needs EF-hand evidence not imaging.
  TF DNA-binding-activity MF excluded via TF_LEGIT_MF regex.
- Tier 2 (core hub-aligned BP/CC): 291. Triage queue: MITO 85 (mostly generic
  mitochondrion), TRANSCRIPTIONAL 72, AUTOPHAGY 70, APOPTOSIS 24, VIABILITY 18.
- Dedup per (organism, gene, go_id). Framed as re-review candidates, not errors.
