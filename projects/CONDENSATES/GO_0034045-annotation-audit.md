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
re-adjudication of every `GO:0034045`, `GO:0097632` and `GO:0097629` annotation held in this
repository, carried out against the analysis in GO issue
[#29437](https://github.com/geneontology/go-ontology/issues/29437). It is a small slice —
59 assertions across 21 gene folders, against ~2,151 direct annotations on GO:0034045 — but
it is a slice where every assertion has a written review attached, so it can say something
the annotation counts cannot. (`GO:0097629` was added to the scope late; see the R4 gap below.)

## Headline: we reproduced the failure mode

The audit ran in two passes. The **first pass** reached genes through the term itself:
**all 23 previously reviewed assertions were `ACCEPT`.** Not one had been questioned. After
re-review, **all 31 have moved** — 26 to `MODIFY` and 5 to `MARK_AS_OVER_ANNOTATED` with the
missing terms proposed. Nothing is left at `ACCEPT`. The **second pass**, described below,
reached seven more genes through the issue's §5.4 triage table and reviewed each in full,
adding 28 assertions on the same footing.

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

**All 31 first-pass assertions, across 14 genes, have moved off `ACCEPT`** — 26 to `MODIFY`,
5 to `MARK_AS_OVER_ANNOTATED` with new terms proposed. All files revalidate clean. The
second-pass genes are tabulated separately further down.

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
| human | ATG14 | GO:0034045 | EXP ×3, IDA, IEA, TAS | PMID:18843052 + refs | 6 | GO:0061908 phagophore |
| human | ATG14 | GO:0097629 | IBA, IDA | GO_REF:0000033, PMID:21518905 | 2 | GO:1990462 omegasome |

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

## A gap in recommendation R4: GO:0097629 has the same defect

R4 proposes obsoleting `GO:0097632` extrinsic component of phagophore assembly site membrane,
noting that issue #23424 obsoleted its intrinsic and integral siblings and the parallel
autophagosome set, and that GO:0097632 "was missed". **A second term was missed in the same
pass.**

| set | intrinsic | integral | extrinsic |
|---|---|---|---|
| autophagosome membrane | GO:0097636 obsolete | GO:0097637 obsolete | GO:0097635 **obsolete** |
| omegasome membrane | GO:0097630 obsolete | GO:0097631 obsolete | GO:0097629 **live** |
| phagophore assembly site membrane | GO:0097633 obsolete | GO:0097634 obsolete | GO:0097632 **live** |

For the autophagosome all three went. For the omegasome and the phagophore assembly site, only
intrinsic and integral went and the extrinsic term survived in both. `GO:0097629` carries the
identical protein-topology defect as `GO:0097632` and should be obsoleted with it, so R4 should
name both.

**ATG14 is the demonstration.** It carries `GO:0097629` and `GO:0097632` as IDAs from *the same
paper and the same experiment* — PMID:21518905, showing the BATS domain binding curved
PtdIns(3)P-rich autophagic membrane, with puncta overlapping ATG16, LC3 and partially DFCP1.
One observation, split across two topology terms because the membrane it was observed on has
two names in GO. Both are now `MODIFY`: the omegasome pair to `GO:1990462`, the
phagophore-assembly-site pair to `GO:0000407`.

ATG14 is the only gene in this corpus carrying `GO:0097629`, so this slice says nothing about
how many annotations the term holds at GOA scale — only that the term should not have survived
#23424.

## ATG14 completes the audit

ATG14's six `GO:0034045` annotations were the last ones sitting at `ACCEPT`, held over from the
first pass. They moved to `GO:0061908` phagophore rather than `GO:0000407`, because the
evidence is about the isolation membrane — "Atg14 is present on autophagic isolation membranes"
(PMID:18843052) — and *isolation membrane* is a related synonym of `GO:0061908`, not of the
assembly site. Generalizing to `GO:0000407` would also have been redundant: ATG14 already
carries it from an IDA (PMID:20713597).

`phagophore membrane` is additionally proposed on the ATG14 review, because the BATS-domain
result is specifically a membrane-binding observation and `GO:0061908` can record it only as
the structure. Knock-on: ATG14's `core_functions.locations` carried both defective terms and
now carries `GO:1990462` and `GO:0061908`.

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

## Second pass: seven §5.4 genes reviewed in full

The genes above were reached through the term. The seven below were reached through the
issue's §5.4 triage table and reviewed **in full** — every annotation on each gene, not only
the `GO:0034045` ones — which is a different and more demanding exercise: 496 annotations
across seven genes, of which 28 are `GO:0034045`.

| gene | annotations | GO:0034045 | destination |
|---|---|---|---|
| human ULK1 | 139 | 4 | GO:0061908 phagophore |
| human RAB1B | 75 | 2 | **GO:0000407** — see below |
| human ATG16L1 | 71 | 4 | GO:0061908 phagophore |
| human ATG9A | 68 | 5 | GO:0061908 phagophore |
| human ATG12 | 55 | 4 | GO:0061908 phagophore |
| human WIPI2 | 45 | 7 | GO:0061908 phagophore |
| human STBD1 | 43 | 2 | *none* — `MARK_AS_OVER_ANNOTATED` |

That brings the audit to **59 assertions across 21 gene folders**, none at `ACCEPT`.
`phagophore membrane` is proposed on ATG9A, WIPI2, ATG16L1 and ATG12, joining ATG14, ATG2A,
ATG2B and worm atg-18.

WIPI2 alone carries seven assertions from four evidence routes — EXP ×4, IDA, IBA, and an IEA
carrying `UniProtKB-SubCell:SL-0221` — which makes it the heaviest single-gene load in the
audit and a good illustration of how the ambiguity compounds without anyone re-deciding it.

### Two genes that do not fit the pattern

**RAB1B** is the one gene whose assertions do *not* go to `GO:0061908`. ATG9A, WIPI2, ATG16L1
and ATG12 are phagophore-membrane proteins. RAB1B is a secretory-pathway GTPase, and
PMID:20545908 locates its requirement upstream — at ER exit sites, with "the autophagic and
secretory pathways intersect at a level preceding the brefeldin A blockage". A membrane term
of any kind overstates that; the site-level `GO:0000407` is the right destination, and the
functional claim is already carried by `GO:2000785`. This matters for the migration plan: a
blanket rewrite of `GO:0034045` → phagophore membrane would put RAB1B on a bilayer it was
never shown to be on.

**STBD1** confirms the triage table's *"no evident support — review for removal"* reading,
which is the opposite outcome to the Rab7 correction above. The primary text places STBD1 at
"enlarged perinuclear structures, co-localized with glycogen, the late endosomal/lysosomal
marker LAMP1 and the autophagy protein GABARAPL1" (PMID:20810658) — and `GO:0048471` and
`GO:0005789` already carry that. There is nothing left for a phagophore term to record, so
both assertions are `MARK_AS_OVER_ANNOTATED` with **no replacement proposed**. Not every
defective annotation needs a destination.

**ULK1** is the strongest case in the whole audit for the condensate reading over the membrane
one, and it is worth stating separately because it cuts against the R3 proposal. ULK1 has no
membrane-binding domain; it is a soluble kinase whose concentration at the site is part of what
*defines* the site; and it already carries `GO:0000407` for the structure and `GO:1903349`
omegasome membrane — the more precise membrane term — from the same study that supplies one of
its `GO:0034045` assertions. For soluble PAS residents of this kind, the site term may simply be
correct and no membrane term needed.

### An unremarked feature of the PAINT records: self-referential WITH/FROM

Five of the seven genes have at least one IBA whose `WITH/FROM` column lists **the annotation
target itself**: WIPI2 (`UniProtKB:Q9Y4P8` on GO:0034045), ATG16L1 (`UniProtKB:Q676U5` on
GO:0034045), ATG12 (`UniProtKB:O94817` on GO:0034045), ULK1 (`UniProtKB:O75385` on GO:0034045
and on GO:0005737), and STBD1 (`UniProtKB:O95210` on GO:0016020). This was not looked for; it
turned up once and then kept turning up.

It is not a GO:0034045 problem — it is a property of how these PAINT records list node
members — but it inflates the apparent evidence for exactly the annotations this audit is
questioning. A reader counting donor genes to judge how well-supported a propagated
annotation is will count the target among its own sources. Worth a separate check across the
IBA corpus; the `propagation_review` blocks on these five reviews record it as
`CIRCULAR_OR_REDUNDANT` so the cases are findable.

### Three further missing-term cases, from full review rather than from the term

Reviewing whole genes rather than single terms surfaced three more instances of the same
underlying pattern — a curator reaching for the nearest wrong term because the right one does
not exist. None of them involve `GO:0034045`.

| gene | annotation | what the evidence shows | term proposed |
|---|---|---|---|
| ATG16L1 | `GO:0120095` vacuole-isolation membrane contact site (IDA, PMID:28890335) | ER–isolation membrane contacts in mammalian and *C. elegans* cells; mammals have no vacuole | endoplasmic reticulum-phagophore membrane contact site |
| ATG16L1 | `GO:0016237` microautophagy (IDA ×2) | ATG8 conjugation to single endolysosomal membranes (CASM); no invagination, no cargo uptake | protein lipidation at single membranes |
| RAB1B | `GO:0090557` establishment of endothelial **intestinal** barrier (IMP NOT) | intestinal **epithelial** tight junctions | establishment of intestinal epithelial barrier |

The ATG16L1 contact-site case is the same gap already proposed on ATG2A and ATG2B and modelled
in `modules/phagophore_organelle_contact_site.yaml`, now reached from a third direction:
`GO:0120095` is the ontology's *only* isolation-membrane contact site term, and it is the yeast
VICS. The organelle membrane contact site branch has ER–vacuole, ER–endosome, ER–lysosome,
ER–plasma membrane, ER–*trans*-Golgi and ER–lipid droplet children, and no ER–phagophore child.

Two adjacent findings that are *not* missing-term cases, recorded here because they came from
the same sweep:

- **ULK1 `GO:0035032`** asserts `part_of` the class III PI3-kinase complex. PMID:40442316 shows
  the ULK1C:PI3KC3-C1 *supercomplex*, assembled through contacts between the FIP200 scaffold and
  the VPS15, ATG14 and BECN1 subunits. ULK1 is not at the interface and is not a subunit. GO has
  no way to say two named complexes coassemble, so the observation was expressed as membership —
  which corrupts `GO:0035032`'s subunit list. A supercomplex term is proposed on that review.
- **ATG16L1 `GO:0019787`** ubiquitin-like protein transferase activity, from Reactome, where
  `GO:0019776` Atg8-family ligase activity exists and its definition already covers both the
  phosphatidylethanolamine and the phosphatidylserine routes. Not a missing term; a
  not-yet-used one.

### Qualifier inconsistency across the conjugation complex

ATG12 annotates `GO:0019776` with `contributes_to`. ATG5 and ATG16L1 use `enables` for the same
complex-level reaction. All three are subunits of an E3-like conjugate that none of them
performs alone, so `contributes_to` is right and the other two should follow — and ATG12 has the
best claim of the three to a specific contribution, since the high-affinity ATG3-binding surface
is exclusive to it. Recorded as a question on the ATG12 review rather than acted on, since it is
a consortium-wide convention rather than a gene-level call.

## What this slice supports and does not

**Supports.** That the term is accepted uncritically even under review; that the failure is
compositional rather than evidential (reviewers substitute pathway membership for
localization); that the amplification chain is real and visible at small scale; that every
assertion in the slice turned out to have a destination, either an existing term or one worth
proposing; and — from the `GO:0097629` finding — that the #23424 sweep was incomplete in a way
that is checkable from the ontology alone.

**Does not support.** Anything about the ~2,090 assertions not in this corpus. This slice is
biased toward genes someone chose to review or that the issue itself named. It is a
demonstration that the per-assertion method in Stage 5 works and produces corrections, not a
sample from which the full audit's outcome can be projected.

The two passes differ in a way that bears on that caveat. The first pass was 19 IEA/IBA out of
31, and a single gene (ATG14) supplied 10 of them. The second pass is 15 experimental out of
28 — 10 `EXP` and 5 `IDA` — spread across seven genes, none supplying more than seven.
Combined, the audit is **27 experimental assertions out of 59**. The objection that this
failure mode is confined to automatic pipelines does not survive that: most of the
second-pass assertions were made by curators reading papers.

## Regenerating the inventory

The 59-assertion inventory comes from scanning `genes/*/*/*-goa.tsv` for the three terms and
joining against the `review.action` in the corresponding `*-ai-review.yaml`. The general
condensate-space scan in
[the GO and annotation audit](CONDENSATES-go-audit.md) uses the same approach over a wider
term list.
