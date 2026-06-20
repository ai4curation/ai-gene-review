# OpenScientist hypothesis job — STAT3 GO:0030335

**Question:** Is *positive regulation of cell migration* (GO:0030335) a **core**
function of STAT3, or a **downstream / context-dependent** consequence of its core
signal-dependent DNA-binding transcription-factor activity?

**Why staged:** Surfaced by the ASSAY_TO_FUNCTION `CELL_MIGRATION_INVASION`
readout class (catalog extension). The two GO:0030335 annotations (IMP;
PMID:31638206, PMID:24846175) were set to **`UNDECIDED`** (was `ACCEPT`) and
deferred to expert review (**issue #1422**) rather than unilaterally demoted,
because STAT3 is high-profile and the call is genuinely contested (oncogenic
EMT/invasion driver vs downstream transcriptional consequence).

**Status:** prompt staged via
`projects/ASSAY_TO_FUNCTION/stage_hypotheses.py` (human-gated generator).
Result, when run, lands in `openscientist.md` (+ `openscientist.md.citations.md`).

## Reproduction

```bash
uv run deep-research-client research \
  --input-file genes/human/STAT3/STAT3-hypotheses/readout-go-0030335/prompt.md \
  --provider openscientist \
  --output genes/human/STAT3/STAT3-hypotheses/readout-go-0030335/openscientist.md \
  --separate-citations genes/human/STAT3/STAT3-hypotheses/readout-go-0030335/openscientist.md.citations.md
```

> Treat the output as **hypothesis-generating literature synthesis, not ground
> truth** — verify snippets against the cited PMIDs before using them in curation.
> The annotations remain `UNDECIDED` pending expert adjudication on issue #1422;
> fold only verified findings into `STAT3-ai-review.yaml` as a `file:` reference
> with an extracted `supporting_text` (the SCO1 review is the model).
