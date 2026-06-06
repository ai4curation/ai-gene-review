# Staged OpenScientist hypothesis job — IL21 GO:0042102

**Status:** staged, **not yet submitted** (requires `OPENSCIENTIST_API_KEY`).

This is a pilot of the openscientist.io hypothesis-job pattern (as used in
`monarch-initiative/dismech` and already exemplified here by
`genes/human/SCO1/SCO1-hypotheses/`), pointed at a candidate produced by the
ASSAY_TO_FUNCTION analysis.

- **Hypothesis:** is `positive regulation of T cell proliferation` (GO:0042102)
  a *core* function of IL21, or a downstream/context-dependent consequence of
  cytokine signaling?
- **Why staged:** IL21 GO:0042102 was set to `UNDECIDED` and removed from
  `core_functions` pending expert review — see
  [issue #1418](https://github.com/ai4curation/ai-gene-review/issues/1418). A
  cited OpenScientist brief is intended to *complement* (not replace) that human
  review.
- `prompt.md` is the rendered, submittable prompt
  (`templates/gene_hypothesis_deep_research.md` filled for this hypothesis).

## How to submit (with an API key)

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
