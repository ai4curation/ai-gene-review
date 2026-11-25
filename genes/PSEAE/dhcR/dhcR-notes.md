# dhcR (PA1998, Q9I2B1) review notes

## What the gene is

DhcR is a LysR-family transcriptional regulator that turns on part of the carnitine catabolic
pathway. The evidence is a transposon screen plus transcript measurements:

- [PMID:19406895 "The PA5389 and PA1998 transcription factors are required for growth on
  carnitine."]
- [PMID:19406895 "the PA1999-PA2000 transcripts are induced in a PA1998-dependent manner and
  induction appears to depend on a carnitine catabolite, possibly 3-dhc"]

So the regulator is required for induction of its target operon, which makes it a positive
regulator, and the inducing signal is probably a downstream metabolite rather than carnitine
itself. The target, PA1999-PA2000, encodes [PMID:19406895 "the alpha and beta subunits of a
predicted 3-ketoacid CoA-transferase"].

The record adds family placement and nothing else usable: `IPR000847 LysR_HTH_N`,
`IPR005119 LysR_subst-bd`, `PF00126 HTH_1`, `PF03466 LysR_substrate`, and a `CC SIMILARITY` line
whose only evidence is ARBA, which this project does not accept as support. `PE 3`. The name
`DhcR, transcriptional regulator` is a submitter `SubName` (`ECO:0000313|EMBL`), so it is not
support either.

## The GO:0006351 row asserts that a regulator transcribes

`GO:0006351` DNA-templated transcription is annotated **involved_in** from `UniRule:UR000400807`.
That term is the synthesis of RNA from a DNA template — what RNA polymerase does. A transcription
factor is not doing that work; it governs whether the polymerase does it. This is the
participation test from the project's own guidance: being required for a process, or acting on the
machinery that performs it, is not performing it.

Checked rather than assumed, in two directions:

1. **The two terms are not parent and child.** OLS confirms `GO:0006355` regulation of
   DNA-templated transcription is **not** a descendant of `GO:0006351`. Regulation terms do not sit
   under the processes they regulate, so this is a distinct claim and a wrong one, not a general
   version of a right one. That is why `TOO_GENERAL` is not the action: that action never means the
   claim is false.
2. **The corpus has a dominant handling, and it is not removal.** Across 168 `GO:0006351` rows in
   this repository the actions are MODIFY 62, ACCEPT 49, MARK_AS_OVER_ANNOTATED 25,
   KEEP_AS_NON_CORE 23, REMOVE 6. Of the MODIFYs, the replacements are regulation terms —
   `GO:0006357` 16, `GO:0045944` 10, `GO:0006355` 10, `GO:0045892` 6, `GO:0045893` 5. So the
   established reading of this legacy keyword-derived row is that its intent was "acts on
   transcription" and the fix is to say which way.

Following that, the row is `MODIFY`. The replacement is the **unsigned** `GO:0006355` rather than
`GO:0045893`, even though this gene is demonstrably a positive regulator, because the row's own
evidence is a LysR-family UniRule: a rule that recognises the family supports "regulator" but says
nothing about the sign. The sign is established by the paper, which sits on different rows.

## No term for what it actually regulates

`GO:0009896` positive regulation of catabolic process is coarse — it covers the positive regulation
of any catabolism whatever — and the gene's real role is narrower: positive regulation of carnitine
catabolism. `GO:0042413 carnitine catabolic process` exists, but a search of GO finds **no**
regulation-of-carnitine-catabolism term; the only carnitine regulation terms are for transmembrane
transport (`GO:1902272`, `GO:1902273`, `GO:1902274`).

So `GO:0009896` is kept as the most informative available term, not marked over-annotated or
general, since nothing more specific is asserted anywhere for it to be entailed by. A new term is
deliberately **not** proposed: GO does not mint a regulation term for every pathway, and the gap
here is ordinary coarseness rather than a missing concept for a characterised activity. Recorded as
an observation instead.
