---
title: "GO:0034045 — corpus slice audit"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [human, mouse, yeast, SCHPO, worm, DICDI]
autolink_gene_symbols: false
---

# GO:0034045 — corpus slice audit

Supporting page for [Biomolecular Condensates](../CONDENSATES.md). This is a per-assertion
re-adjudication of every `GO:0034045` and `GO:0097632` annotation held in this repository,
carried out against the analysis in GO issue
[#29437](https://github.com/geneontology/go-ontology/issues/29437). It is a small slice —
29 assertions across 13 gene folders, against ~2,151 direct annotations on GO:0034045 — but
it is a slice where every assertion has a written review attached, so it can say something
the annotation counts cannot.

## Headline: we reproduced the failure mode

**All 23 previously reviewed assertions were `ACCEPT`.** Not one had been questioned.

That is the strongest corroboration this corpus can offer for the mechanism described in
§2 of the issue analysis: a reviewer meeting this term sees a plausible label and a
definition that is *true as written* ("a membrane associated with the PAS" — there are
membranes at the PAS), while the false claim sits in a `bounding_layer_of` axiom that is
never surfaced. Our reviewers had the literature, wrote a justification for each one, and
still accepted every single assertion. Several of the justifications do not even address
localization:

| gene | term | prior `reason`, verbatim |
|---|---|---|
| ATG7 (yeast) | GO:0097632 | "Accepted because this annotation aligns with established ATG7 E1-like function and autophagy pathway roles." |
| Rab7 (mouse) | GO:0034045 | "Consistent with the Rab7 role in autophagy." |
| RAB7A (human) | GO:0034045 | "Consistent with RAB7A role in autophagy regulation." |

ATG7's cited supporting text was the paper's *title*. These are pathway-membership
arguments standing in for localization evidence — the same substitution that put the
annotations there originally.

## Changes made

Six annotations across six genes were re-adjudicated `ACCEPT` → `MODIFY`. All six files
revalidate clean.

| species | gene | term | evidence | reference | new action | destination |
|---|---|---|---|---|---|---|
| mouse | Rab7 | GO:0034045 | IDA | PMID:19956673 | MODIFY | GO:0061908 phagophore |
| human | RAB7A | GO:0034045 | IEA | GO_REF:0000107 | MODIFY | GO:0061908 phagophore |
| DICDI | atg1 | GO:0034045 | IBA, ISS, IEA | GO_REF:0000033/24/44 | MODIFY ×3 | GO:0000407 |
| SCHPO | atg101 | GO:0034045 | IEA | GO_REF:0000044 | MODIFY | GO:0000407 |
| yeast | ATG7 | GO:0097632 | IDA | PMID:10233148 | MODIFY | GO:0000407 |
| human | ATG14 | GO:0097632 | IBA, IDA | GO_REF:0000033, PMID:21518905 | MODIFY ×2 | GO:0000407 |

`GO:0000407` is used as the conservative destination wherever the supported claim is
"at the assembly site" — it is where `GO:0097632` already points via `part_of`, and it
does not pre-empt the `phagophore membrane` term proposed as R3. Two knock-on edits were
needed: ATG7's `core_functions.locations` carried `GO:0097632` and now carries
`GO:0000407`; atg1's carried both `GO:0000407` and `GO:0034045`, and the duplicate was
dropped.

## One correction to the §5.4 triage: Rab7

The triage table lists RAB7 under *"no evident support — review for removal"*, citing
PMID:19956673. Reading the full text, that is not quite right, and the difference matters
for how the migration is framed.

The paper **does** contain localization data for Rab7, in NIH3T3 and HeLa cells:

> Thus, a population of Rab7 is recruited to GFP-Atg5 positive membranes during the early
> phase of GcAV formation.

An Atg5-positive early sequestering membrane is a phagophore. So the assertion is not
unsupported — it is **mis-targeted**: the paper is about GAS-containing autophagosome-like
vacuoles, a xenophagy structure, and never examines the phagophore assembly site. The
abstract also states outright that Rab7 is

> an additional component, which is dispensable in canonical autophagosome formation

which is the opposite of a claim about the canonical PAS. The right disposition is
therefore a move to `GO:0061908`, not deletion.

This distinction is worth carrying into Stage 5. "No evident support" and "supported, but
for a different structure" need different handling: the first is a removal, the second is a
migration that must not be lost. An abstract-level triage cannot separate them — which is
the caveat §8 already makes, borne out on the first case checked.

Note also that this repository holds **both ends of the propagation chain**: human RAB7A
carries the same term as an IEA projected from mouse Rab7a via GO_REF:0000107
(`WITH UniProtKB:P51150`). Correcting the source should carry through, and both have been
changed together. This is a two-link instance of the amplification described in §5.1.

## Cases left alone, and why

`ATG2A`, `ATG2B`, and the *S. pombe* `atg2`, `atg5`, `atg16`, `atg38` annotations were left
as `ACCEPT`. Their reviews already describe the right biology — ATG2A's reads "at the
ER-phagophore edge", ATG2B's "membrane tethering/lipid-transfer during phagophore
expansion" — which is precisely the §5.4 hypothesis that these belong at a phagophore rim
or phagophore-ERES contact site. **There is nowhere correct to move them yet.** Changing
them now would substitute one wrong term for another. They are the argument for R3 and R7
being on the critical path, not for further per-gene action.

The `worm atg-18` IBA is in the same position, and *S. pombe* `atg5`/`atg16` are ATG8-
conjugation machinery whose destination depends on the sheet-versus-system decision in
§4.2.

## What this slice supports and does not

**Supports.** That the term is accepted uncritically even under review; that the failure
is compositional rather than evidential (reviewers substitute pathway membership for
localization); that the amplification chain is real and visible at small scale; and that
migration destinations for the Atg1-complex proteins (→ GO:0000407) are unambiguous while
those for the lipid-transfer and conjugation machinery are blocked on new terms.

**Does not support.** Anything about the ~2,120 assertions not in this corpus. This slice
is biased toward genes someone chose to review, and toward IEA/IBA (19 of 29 assertions);
it contains only four of the 110 manual annotations in §5.3. It is a demonstration that the
per-assertion method in Stage 5 works and produces corrections, not a sample from which the
full audit's outcome can be projected.

## Regenerating the inventory

The 29-assertion inventory comes from scanning `genes/*/*/*-goa.tsv` for the two terms and
joining against the `review.action` in the corresponding `*-ai-review.yaml`. The general
condensate-space scan in
[the GO and annotation audit](CONDENSATES-go-audit.md) uses the same approach over a wider
term list.
