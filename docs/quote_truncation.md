# Truncated quotes

A `supporting_text` quote copied out of a line-wrapped source is easy to stop at
the hyphen the wrap left behind:

```yaml
supporting_text: "FUNCTION: Catalyzes the NADPH-dependent reduction of 7-cyano-7-"
```

The substrate is 7-cyano-7-deazaguanine. Cut at the hyphen, the quote names no
substrate at all — and it was cited to support exactly that substrate's
reduction.

`just validate-quotes` cannot see this. That check collapses whitespace before
matching (`supporting_text.py`), so the quote genuinely *is* a verbatim substring
of its source; it is just not a complete one.

## Running it

```bash
just quote-truncation-audit                     # every file in scope (see below)
just quote-truncation-audit --kind mid_word     # only the certain cases
just quote-truncation-audit modules/notch_signaling.yaml
```

### Scope

With no arguments the audit scans `quote_check`'s default globs **plus**
`genes/*/*/*-ai-review.yaml`.

Gene reviews are deliberately outside `quote_check.DEFAULT_GLOBS`, on the grounds
that `validator.py` already checks their quotes. That rationale does not carry over
here: `validator.py` checks whether a gene-review quote *matches* its source, and
nothing checks whether it was *cut*. Inheriting the narrower scope silently excluded
the largest holder of `supporting_text` in the repository — and the first version of
this check did exactly that while reporting its count as "the corpus". The same
UniProt sentence was reported from `interpro/panther/PTHR43160` and missed in
`genes/yeast/ACO1`, because one was in scope and the other was not.

It reports and exits 0. Repairing a quote edits curated prose, and the extension
sometimes changes what the quote supports, so this is not a gate.

## The two kinds, which are not equally strong

**`mid_word`** — the source continues with a word character, so a word was broken
in half. There is no reading on which the quote is complete, and this is the great
majority of what the audit finds. No count is quoted here on purpose: run the audit.
A number written into prose goes stale silently, which is the same failure this
check exists to catch.

**`token_boundary`** — the source continues after a space, so the quote ends on a
real token: `remove glutathione from both (R)-` where the source reads
`both (R)- and (S)-isomers`. The quote is verbatim *and* ends where a token ends.
Whether it is *enough* is a judgement about the argument it supports — here, that
one enzyme handles both enantiomers, which the fragment does not convey — not a
mechanical defect.

A **suspended hyphen** — `in a CTP- and Mg2+-dependent manner`, `to Man3- and
Man4GlcNAc2-PP-Dol` — is this kind, decided by what follows rather than by
whitespace. It has to be: the hyphen is correct English whatever the source does at
that point, and two instances of the same construction in two files that wrap
differently were being classified as two different things.

The conjunction alone is **not** enough. `comm-` followed by `and` is the word
"command" split across lines, and reading that as punctuation is the mirror of
letting `andro-` read as `and`. So the test requires positive evidence of the
construction: a coordinating conjunction *and* a following word carrying its own
internal hyphen (`Mg2+-dependent`, `Man4GlcNAc2-PP-Dol`). Note the hyphen there is
preceded by `+`, not by a letter, which is why the test matches a word-internal
hyphen rather than a tokenised word.

## What it does not find

The check finds the one case that leaves a syntactic trace. A quote truncated at
a comma, a word or a sentence boundary looks exactly like a short quote, and
nothing distinguishes them mechanically. **A clean result is not evidence that the
corpus' quotes are complete.**

It also shares `source_renderings` with `validate-quotes` but not its matcher. A
quote written with an explicit `...` elision is matched there part by part and is
**not located here**, so such a quote is silently absent from this report rather
than reported as unchecked.

In particular, do not read the finding count as a measure of the problem, and be
careful which way round the error runs.

A hyphen at the end of a *physical line* in a YAML file is sometimes not the end of
a quote at all: a plain or quoted scalar can wrap, leaving the hyphen mid-value. That
is why this check parses the YAML instead of grepping lines, and the module file for
aspartate-to-threonine biosynthesis is the clear case — twelve lines begin with the
same sentence and only four end a scalar, so a line-based repair there would have
corrupted eight complete quotes to make four fixes.

But that observation was then used here to dismiss a grep's magnitude, and the
dismissal was wrong. An earlier version of these docs said grepping "reports well
over a thousand such hyphens where there are two dozen truncated quotes". The two
dozen came from a parse whose scope excluded `genes/*/*/*-ai-review.yaml`; with gene
reviews in scope the parsed count is in the same order as the grep's. The grep was
approximately right and the parse was too narrow. **A more rigorous instrument
pointed at less of the data is not more trustworthy than a crude one pointed at all
of it** — check what your scope covers before using it to overrule a cruder count.

## Wrap artifacts inside a quote are a different problem

A quote whose *middle* reads `similarly low activ- ity` came from a source that
wrapped inside the word, and the cached source still contains the break. Such a
quote matches its source, and "repairing" it to `activity` would make it stop
matching. The artifact is in the cached publication, not in the review, so these
are out of scope here and are not reported.

This class is real but it is **not** an explanation for a large grep count; do not
reach for it as one, which is the mistake corrected above. Mid-value wrap artifacts
and value-final truncations are separate populations, and only measuring each
separately tells you how big either is.

## Fixing one

`Truncation.completed` extends the quote by a single token, which is enough to
make the word whole and rarely enough to make the sentence so. Treat it as a
proposal:

1. Read the surrounding sentence in the source and take as much of it as the
   claim needs.
2. Check whether the completed quote still supports the row. Occasionally it does
   the opposite — a cut can hide a qualifier.
3. Re-run `just validate-quotes` on the edited file, and on anything that quotes
   it.
