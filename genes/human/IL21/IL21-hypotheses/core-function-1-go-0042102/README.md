# OpenScientist hypothesis job — IL21 GO:0042102

**Status:** ✅ completed 2026-06-06 (28.5 min, 28 PMID citations). Result in
`openscientist.md` (+ `openscientist.md.citations.md`).

**Verdict:** *OVER-ANNOTATED as core function → recommend `KEEP_AS_NON_CORE`* for
GO:0042102 — the T-cell-proliferation effect is real but costimulation-dependent,
bidirectional across T-cell subsets, not a defining feature of IL-21R deficiency,
and subordinate to IL-21's B-cell/Tfh signature. Same call for NK cytotoxicity
(GO:0045954). Notable leads: GO:0045954 actually has IDA support (PMID:18005035),
and IL-21's true core functions have only ISS/IEA (so IDA ≠ core).

> This is the autonomous agent's analysis — **hypothesis-generating literature
> synthesis to verify against the cited PMIDs, not ground truth.** The
> annotations remain `UNDECIDED` pending expert adjudication on
> [issue #1418](https://github.com/ai4curation/ai-gene-review/issues/1418); this
> brief is a complement, not the decision.

---

## Reproduction

```bash
export OPENSCIENTIST_API_KEY="name:secret"   # your key
uv run deep-research-client research \
  --input-file genes/human/IL21/IL21-hypotheses/core-function-1-go-0042102/prompt.md \
  --provider openscientist \
  --output genes/human/IL21/IL21-hypotheses/core-function-1-go-0042102/openscientist.md \
  --separate-citations
```

Jobs run ~10–15 min. The result lands as `openscientist.md` (+ a
`openscientist.md.citations.md`). After review, fold any verified findings into
`genes/human/IL21/IL21-ai-review.yaml` as a `file:` reference with an extracted
`supporting_text` statement (the SCO1 review is the model), and report the
verdict back on issue #1418.

> Treat the output as hypothesis-generating literature synthesis, not ground
> truth — verify snippets against the cited PMIDs before using them in curation.
