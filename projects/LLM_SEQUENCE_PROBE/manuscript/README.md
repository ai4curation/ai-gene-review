---
title: "LLM_SEQUENCE_PROBE / manuscript"
---

# LLM_SEQUENCE_PROBE / manuscript

Draft of a short preprint on the four sequence-only tests described on the
[project page](../../LLM_SEQUENCE_PROBE.md).

## Files

- `manuscript.tex`: the manuscript source. Start here.
- `references.bib`: bibliography. Entries with a DOI were checked against Europe PMC.
- `figures/make_figures.py`: draws both figures from the committed model outputs
  in `../pseudo/` and `../structure/`. Nothing in it is typed in by hand.
- `figures/*.pdf`: figures used by the manuscript. `figures/*.png` are copies for
  the project page.

## Build

```bash
uv run python figures/make_figures.py
pdflatex manuscript && bibtex manuscript && pdflatex manuscript && pdflatex manuscript
```

The PDF is not committed.

## Open before posting

- Author list, affiliations and funding (marked `TODO` in the source).
- Every question was asked once. Repeat runs would give intervals for tests 2 to 4.
- Opus 4.6 ran at low effort; a like-for-like comparison needs it at high effort.
- Function grading for the novel structures is one unblinded pass by the agent
  that ran the tests. A blinded second grader is needed.
- The two enzymes where both models disagree with the curated active-site
  position (Q08651, P64636) have not been adjudicated.
- Related work is thin: protein language model baselines on the same items, and
  prior tests of general language models on sequence, are not yet covered.
