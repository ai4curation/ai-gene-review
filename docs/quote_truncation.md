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
just quote-truncation-audit                     # whole corpus
just quote-truncation-audit --kind mid_word     # only the certain cases
just quote-truncation-audit modules/notch_signaling.yaml
```

It reports and exits 0. Repairing a quote edits curated prose, and the extension
sometimes changes what the quote supports, so this is not a gate.

## The two kinds, which are not equally strong

**`mid_word`** — the source continues with a word character, so a word was broken
in half. There is no reading on which the quote is complete. 22 of the corpus'
current 24 findings are this kind.

**`token_boundary`** — the source continues after a space, so the quote ends on a
real token: `remove glutathione from both (R)-` where the source reads
`both (R)- and (S)-isomers`. The quote is verbatim *and* ends where a token ends.
Whether it is *enough* is a judgement about the argument it supports — here, that
one enzyme handles both enantiomers, which the fragment does not convey — not a
mechanical defect.

A **suspended hyphen** — `in a CTP- and Mg2+-dependent manner`, `to Man3- and
Man4GlcNAc2-PP-Dol` — is this kind, decided by the following conjunction rather
than by whitespace. It has to be: the hyphen is correct English whatever the
source does at that point, and the corpus' two instances are the same
construction in two files that happen to wrap differently. Keying the class on
the line break alone classified them as two different things.

## What it does not find

The check finds the one case that leaves a syntactic trace. A quote truncated at
a comma, a word or a sentence boundary looks exactly like a short quote, and
nothing distinguishes them mechanically. **A clean result is not evidence that the
corpus' quotes are complete.**

In particular, do not read the finding count as a measure of the problem. A
hyphen at the end of a *physical line* in a YAML file is usually not the end of a
quote at all: a plain scalar wraps, so the hyphen sits mid-value. Grepping lines
reports well over a thousand such hyphens where there are two dozen truncated
quotes. Parse the YAML — which is what this check does — rather than grepping it.

## Wrap artifacts inside a quote are a different problem

A quote whose *middle* reads `similarly low activ- ity` came from a source that
wrapped inside the word, and the cached source still contains the break. Such a
quote matches its source, and "repairing" it to `activity` would make it stop
matching. The artifact is in the cached publication, not in the review, so these
are out of scope here and are not reported.

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
