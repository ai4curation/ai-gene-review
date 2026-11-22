# SIRT2 — curation notes

UniProt Q8IXJ6. Human.

## Why GO:0051607 defense response to virus was withdrawn

The review previously proposed `GO:0051607` as `NEW`, hung off the
`GO:0140773` demyristoylase core function alongside `GO:0042742 defense response to
bacterium`. Both halves were treated as parallel consequences of the same
defatty-acylase activity. Only the bacterial half survives.

The two references originally attached to the viral row supported neither it nor each
other: `DOI:10.1038/s41467-022-32227-x` is the *Shigella* study, and
`DOI:10.1172/jci158978` reports that the allosteric SIRT2 inhibitor FLS-359 has
broad-spectrum antiviral activity — which makes SIRT2 a factor viruses need, the
opposite sign to a defense term. The same two references had been pasted onto both the
bacterial and the viral annotation, so each carried one about the wrong kind of
pathogen.

A blinded OpenScientist function-assignment run was commissioned to settle the
direction: prior review decision withheld, no references supplied, and the framing named
neither direction, only that published perturbation data point both ways. Report at
`SIRT2-hypotheses/virus-restriction-vs-dependency/openscientist.md`.

Its verdict, from 14 citations and without citing either paper that prompted the
question: the direction is **virus-specific and predominantly pro-viral**. The
asymmetry is methodological, which is what makes it persuasive —

- Both studies reading out **infectious progeny**, the metric that settles the sign, go
  pro-viral: dengue (PMID:34147476), where the inhibitor effect is *abolished by SIRT2
  knockdown*, an on-target genetic control; and HIV-1 (PMID:41883165), >1 log₁₀ in
  macrophages and humanized mice.
- Six HBV studies agree across overexpression and three independent inhibitors.
- HSV-1 has a mechanism: SIRT2 deacetylates G3BP1 to suppress cGAS-STING, so losing
  SIRT2 *raises* interferon (PMID:37870259).
- The antiviral side rests on SIRT2 **activation** (influenza, gain-of-function with a
  surrogate readout), an ISG-transcription signalling surrogate with no titre, and a
  **minor isoform 5** that opposes the dominant isoform 1.

All eight key PMIDs were checked against PubMed; every title matches the claim made for
it. SIRT2 carries no viral-defense annotation in GOA, so this was a proposal to add one,
not an existing annotation to defend.

Deleted rather than set to `REMOVE`: validation requires annotations absent from GOA to
carry `action: NEW`, so `REMOVE` on a not-in-GOA term fails.

## A paper that argues the other way, and why it did not change the call

`PMID:25516616` (Koyuncu et al. 2014, mBio, *Sirtuins are evolutionarily conserved viral
restriction factors*) reports that siRNA knockdown of each of the seven sirtuins
*increases* virus progeny — loss-of-function with a titre readout, which is exactly the
category the OpenScientist report calls missing on the antiviral side. It is cached here
deliberately.

It did not change the verdict because its SIRT2 evidence is one arm of a seven-sirtuin
screen: **SIRT2 is never discussed individually in its text** (two mentions, both the
same introductory sentence about subcellular localization). Its drug work is
SIRT1-specific. That is family-level evidence, and the report's own "paralog caution"
applies — pan-sirtuin tools and family claims should not carry over to SIRT2.

Note also that Thomas Shenk is senior author on both Koyuncu 2014 and the 2023 FLS-359
paper. The disagreement is a real one within a single lab's output, nine years apart,
not a citation error.

## Open question

The report suggests the pro-viral biology would be better captured by virus-qualified
`GO:0045070 positive regulation of viral genome replication` or `GO:0032480 negative
regulation of type I interferon production`. Not added: that is a new claim, and the
evidence for it has not been independently verified here. Recorded in
`suggested_questions` instead.
