---
title: "GO:0034045 — corpus slice audit"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [human, mouse, yeast, SCHPO, worm, DICDI]
autolink_gene_symbols: false
---

# GO:0034045 — corpus slice audit

Supporting page for [Biomolecular Condensates](../CONDENSATES.md), and the first subproject of
[the SL project](../SL.md) (`SL-0221 Preautophagosomal structure membrane`). This is a per-assertion
re-adjudication of every `GO:0034045` and `GO:0097632` annotation held in this repository,
carried out against the analysis in GO issue
[#29437](https://github.com/geneontology/go-ontology/issues/29437). It is a small slice —
29 assertions across 13 gene folders, against ~2,151 direct annotations on GO:0034045 — but
it is a slice where every assertion has a written review attached, so it can say something
the annotation counts cannot.

## Headline: we reproduced the failure mode

**All 23 previously reviewed assertions were `ACCEPT`.** Not one had been questioned.
After re-review, 23 of the 29 have moved — 18 to `MODIFY` and 5 to
`MARK_AS_OVER_ANNOTATED` with the missing terms proposed.

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

**23 of the 29 assertions, across 14 genes, have moved off `ACCEPT`** — 18 to `MODIFY`,
5 to `MARK_AS_OVER_ANNOTATED` with new terms proposed. All files revalidate clean.

| species | gene | term | evidence | reference | n | destination |
|---|---|---|---|---|---|---|
| mouse | Rab7 | GO:0034045 | IDA | PMID:19956673 | 1 | GO:0061908 phagophore |
| human | RAB7A | GO:0034045 | IEA | GO_REF:0000107 | 1 | GO:0061908 phagophore |
| human | ATG5 | GO:0034045 | IBA, IDA, IEA, ISS | PMID:32960676 + refs | 4 | GO:0061908 phagophore |
| DICDI | atg1 | GO:0034045 | IBA, ISS, IEA | GO_REF:0000033/24/44 | 3 | GO:0000407 |
| SCHPO | atg101 | GO:0034045 | IEA | GO_REF:0000044 | 1 | GO:0000407 |
| SCHPO | atg2 | GO:0034045 | IEA | GO_REF:0000044 | 1 | GO:0000407 |
| SCHPO | atg5 | GO:0034045 | IBA, IEA | GO_REF:0000033/44 | 2 | GO:0000407 |
| SCHPO | atg16 | GO:0034045 | IEA | GO_REF:0000044 | 1 | GO:0000407 |
| SCHPO | atg38 | GO:0034045 | IEA | GO_REF:0000044 | 1 | GO:0000407 |
| yeast | ATG7 | GO:0097632 | IDA | PMID:10233148 | 1 | GO:0000407 |
| human | ATG14 | GO:0097632 | IBA, IDA | GO_REF:0000033, PMID:21518905 | 2 | GO:0000407 |

Two destinations, chosen by what the cited evidence actually shows:

- **`GO:0061908` phagophore** where the source paper says *phagophore*. For human ATG5 the
  supporting quote already read "RAB33B recruits the ATG16L1 complex to the phagophore", and
  the abstract adds that "RAB33B and ATG16L1 mutually determined the localization of each
  other on phagophores". The annotation said PAS membrane; the paper said phagophore. That is
  the `phagophore` RELATED synonym on GO:0034045 doing exactly the damage §2 predicts.
- **`GO:0000407`** where the evidence shows the punctum. Every *S. pombe* case is like this —
  the quotes already in those reviews are "recruitment of Atg5 and Atg16 to PAS",
  "PAS accumulation of Atg2, Atg18b, Atg24b, Atg5, Atg16, and Atg8", "Atg38 localizes to the
  PAS". The evidence says PAS; the term says PAS *membrane*. `GO:0000407` is also where
  `GO:0097632` already points via `part_of`, and neither destination pre-empts the
  `phagophore membrane` term proposed as R3.

Knock-on edits: ATG7's `core_functions.locations` carried `GO:0097632` and now carries
`GO:0000407`; ATG5's carried `GO:0034045` and now carries `GO:0061908`; atg1's carried both
`GO:0000407` and `GO:0034045`, and the duplicate was dropped. `propagation_review` blocks were
added to the four IBA annotations changed to `MODIFY`.

### The *S. pombe* set is the cleanest evidence in the audit

Five of the moved annotations are *S. pombe* IEAs whose sole source is `GO_REF:0000044` —
that is, SL-0221 with nothing else behind it. In every case a reviewer had written a
justification quoting experimental evidence about **PAS puncta**, then accepted a term naming
a **PAS membrane**, without noticing the substitution. The conflation is not buried in an
axiom file here; it is visible inside our own prose, one line apart.

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

## The missing-term cases: propose the term, don't hold the annotation

`ATG2A`, `ATG2B` and `worm atg-18` were initially left as `ACCEPT` on the grounds that there
was nowhere correct to move them. **That was wrong.** A review does not need an existing
destination to record a verdict — `proposed_new_terms` exists precisely for this, and holding
an annotation at `ACCEPT` because the ontology is incomplete records the opposite of what the
reviewer actually believes.

All five annotations now read `MARK_AS_OVER_ANNOTATED`, with the terms that ought to exist
authored on the gene reviews themselves:

| gene | annotations moved | `proposed_new_terms` authored |
|---|---|---|
| human ATG2A | 2 (IEA, EXP) | phagophore membrane; phagophore rim; endoplasmic reticulum-phagophore membrane contact site |
| human ATG2B | 2 (IEA, EXP) | phagophore membrane; endoplasmic reticulum-phagophore membrane contact site |
| worm atg-18 | 1 (IBA) | phagophore membrane |

`MARK_AS_OVER_ANNOTATED` rather than `MODIFY`, because `MODIFY` requires
`proposed_replacement_terms` carrying real identifiers and there are none to give — inventing
an id would be worse than the problem. The verdict, the reasoning, and the terms that would
resolve it are all recorded; only the identifier is missing, and that is GO's to mint.

Each proposal maps onto a recommendation in the issue: **phagophore membrane** is R3,
**phagophore rim** and **ER-phagophore membrane contact site** are R7. The `phagophore rim`
proposal records the alternative label "phagophore edge" and cites `GO:0097203 phagocytic cup
lip` as GO's existing precedent for the pattern; the `phagophore membrane` proposal takes the
collective sheet-plus-rim reading and flags explicitly that the sheet-versus-system question
of §4.2 is unresolved upstream, so an editor is not silently committed by the annotation.

Knock-on: ATG2A's `core_functions.locations` carried `GO:0034045` alongside `GO:0044232`
organelle membrane contact site and `GO:0005789` ER membrane, and ATG2B's carried it alongside
`GO:0061908` and `GO:0005789`. In both cases the defective term was the least informative of
the three and was dropped rather than replaced.

The *S. pombe* ATG8-conjugation genes were moved to `GO:0000407` rather than to a proposed
phagophore membrane because their cited evidence is punctum colocalization, which does not
distinguish the two — the sheet-versus-system decision does not arise on that evidence, so
there is nothing to propose.

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
