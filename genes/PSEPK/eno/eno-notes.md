
## 2026-08-08 — OpenScientist blinded run on GO:0005576 (pre-registration)

```
scripts/gene_hypothesis_deep_research.py run PSEPK eno openscientist \
  --annotation-term-id GO:0005576 --as-function-hypothesis \
  --timeout-seconds 8100 -- --param max_iterations=3 --param timeout=7200
```

`--as-function-hypothesis` withholds this review's verdict; the dry-run confirms the prompt
carries only `term`, `evidence_type` and `original_reference_id`, with no `review:` block. The
hypothesis sent is the bare "eno has extracellular region (GO:0005576)." — no scoping context,
so OpenScientist picks its own decisive analysis.

**Why this hypothesis.** This is the flagship case of pattern C in the SL project
(`projects/SL.md`): HAMAP rule MF_00318 attaches `Secreted`/`Cell surface` to essentially every
bacterial enolase because the protein moonlights as a surface plasmin(ogen) receptor in
pathogens. Enolase is universal, so if the rule over-reaches it over-reaches at GOA scale. The
current verdict is `MARK_AS_OVER_ANNOTATED`, resting on an argument from absence.

**Held out.** `eno-bioinformatics/RESULTS.md` was written *immediately before this run*
specifically to be the holdout, and committed first (26fb1cf48). It tests whether the
plasminogen-binding determinants of pathogen enolases are present in *P. putida*, and finds
both absent: the internal pneumococcal motif (`FYDKERKVYD`, PMID:12828639) maps to `FYGKYNLSGE`
— 3/10 identical, 1 lysine vs 2, with the anchoring `FY` retained so it is the right structural
position — and the C-terminus is `RAEFRG`, no lysines at all, against `FYNLKK` in
*S. pneumoniae* and `FYNLDK` in *S. aureus*.

Note this holdout differs from the THI22 one in an important way: THI22's was written earlier
for a different question and only incidentally bore on the hypothesis, so it was a genuinely
independent artefact. This one was written *for* the comparison, by the same reviewer, on the
same day. That makes it a weaker form of independence — it tests whether OpenScientist
converges on the same mechanism, not whether two unrelated efforts agree.

**Prediction, recorded before the result.** Four outcomes are distinguishable:

1. *Converges on the same mechanism* — the run independently identifies the plasminogen-binding
   determinants as the thing to check and finds them absent. Strongest confirmation; wire the
   positive evidence into the review and escalate the MF_00318 rule-scoping request.
2. *Confirms by other means* — reaches the same verdict via secretome data, comparative
   genomics, or *Pseudomonas*-specific literature. Also useful, and a broader evidence base than
   the holdout has.
3. *Finds contrary evidence* — surface or secretome evidence for *P. putida* or a close
   relative. Then the verdict is wrong and the holdout is testing the wrong mechanism.
4. *Unresolved* — no organism-specific evidence either way, which would leave the sequence
   argument as the only positive finding and is itself informative about how thin the evidence
   base for the rule is.

Per project practice, conclusions resting on PMIDs not in `publications/` are recorded as leads
rather than wired as annotations.
