
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

## 2026-08-13 — blinded OpenScientist run on GO:0005576, and its verification

Relaunched the run that had failed silently on a previous attempt (empty output dir, empty log,
no surviving process — neither of the two documented failure signatures). This time it completed
in ~31 min: `status=OK`, report and artifacts written to
`eno-hypotheses/function-hypothesis-go-0005576/`.

Blinding held. The only context passed was the term, the `IEA` code and `GO_REF:0000044`; the
review's `reason` — which names HAMAP `MF_00318` and the pathogen moonlighting story — was not
sent, and neither was `eno-bioinformatics/RESULTS.md`. The report's own Limitations section
confirms it: "local `*-bioinformatics` analyses were intentionally withheld".

**Scoring against the holdout:**

- *Verdict converged.* Both called GO:0005576 over-annotated for this organism, both traced it to
  a HAMAP rule propagation with no *P. putida* evidence behind it.
- *One computed result converged exactly.* From sequence alone the run found Q88MF9 ending
  `…RGRAEFRG` with no C-terminal lysine — the same `RAEFRG` the holdout found. Neither saw the
  other. That is the strongest form of agreement available here.
- *Complementary gap.* The run did not attempt the internal pneumococcal motif and says so; the
  holdout's `FYGKYNLSGE` vs `FYDKERKVYD` comparison is additional.
- *The novel argument was refuted.* Its headline claim — that the surface/secreted GO terms are
  **anti-correlated** with real biology, absent from enolases where surface display is proven —
  rests on a table in which only two of seven rows are correct. `P9WNV9` is DnaJ1, `Q8DR60` is an
  endo-alpha-N-acetylgalactosaminidase, `P0A4G2` is pneumococcal PsaA (and is labelled
  *S. aureus*); `P64075` is *Listeria* not *M. tuberculosis*, `P77972` is *Synechocystis* not
  *Bifidobacterium*. The three non-enolases are exactly the rows carrying "no CC term", which is
  what manufactured the pattern. Looked up properly, *S. pneumoniae* (Q97QS2) and *S. aureus*
  (P99088) enolases both carry GO:0005576 by the same rule.

Written up with a reproducible checker in `eno-bioinformatics/check_ortholog_go_audit.py`.

**Net effect on the review.** The verdict is unchanged and now better supported, but by
*uniformity* rather than anti-correlation: every enolase checked across six genera carries the
term as a rule-derived IEA with no organism-specific input — five of the six from
`GO_REF:0000044`, and *Listeria innocua* (P64075) from `GO_REF:0000120` — so it distinguishes
nothing and cannot be evidence about *P. putida*. (Earlier drafts of this note and of the review
`reason` said all six came from `GO_REF:0000044`; the committed audit output at
`eno-bioinformatics/RESULTS.md` shows otherwise. Corrected 2026-08-13. The argument is unaffected:
what matters is that both references are family-rule pipelines, not organism-specific evidence.)

One caution the run got backwards and worth keeping: it asserts no experimental GO:0005576 exists
on any enolase. *E. coli* enolase carries `GO:0005576 EXP PMID:15003462`, on
2-phosphoglycerate-dependent automodification and export [PMID:15003462 "As reported for other
bacteria, a significant fraction of E.coli enolase was found to be exported into the medium."].
That paper is now cached in `publications/` and declared in the review's `references`, so the
claim is wired rather than left as a lead. Non-classical enolase export is a live question, so the
argument here stays organism-specific and must not be generalised into "bacterial enolases are not
exported".

**Method lesson.** A generated table of accessions is a claim about identity, and identity is
cheap to check. The verdict survived verification; the evidence offered for it did not.
