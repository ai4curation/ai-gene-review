# PANTHER family assignment review

A pass over all 281 module YAMLs examining every PANTHER family assignment, the
PAINT evolutionary evidence cited for it, and the extant proteins named as its
representatives. Generated against PANTHER 19.0.

## Scope

| | count |
|---|---|
| module files | 281 |
| family/subfamily descriptors with an id and a representative member | 1,008 |
| declared at family level | 907 |
| declared at subfamily level | 101 |
| family descriptors asserting no id | 163 (across 50 modules) |
| PAINT node citations | 372 (of 195 distinct nodes) |
| PAINT annotations resting on <=3 seeds | 295 / 570 distinct (node, term) = 468 / 1159 citation-weighted |
| family-level groundings with all members in one subfamily | 806 / 892 checkable (of 907 declared) |
| ...in families split into 20+ subfamilies (the advisory) | 197 |
| ...why the other 101 family-level ones are not | 82 members spread, 11 grounding inconsistent, 4 some members unplaced, 4 no subfamily recorded |
| family ids covering more than one distinct protein | 213 (over 528 proteins) |
| prose PANTHER claims checked | 168 / 168 |
| cited accessions resolved to a PANTHER family | 1,457 / 1,492 |

Every row above is emitted by `just panther-report-stats` — paste its output
over the table after a merge. These counts drift whenever main merges a module
and went stale four times in this branch's history; the first attempt at a fix
named two commands that between them covered three of the then eight rows, so
the four that actually kept drifting stayed hand-maintained. The last three rows
were narrative figures in §1 until they were found to have drifted too, and were
moved here for the same reason.

Counts are post-removal: 21 descriptors that named a family provably excluding
their own representative member now assert no id (see §1); the other 142
pre-date this work. The figure comes from the sweep's own `ℹ️` counter (carried
on `ModuleValidationResult`), so report and tool cannot drift apart: it counts
family descriptors that name UniProt representative members and carry no id in
either `term` or `family_terms[]`.

The 35 accessions for which no PANTHER family exists in either PANTHER's
classifications or UniProt are listed in `panther-members.tsv` itself, so the
resolution rate above is over a stated denominator rather than over successes
only — the file cannot be read as claiming 100% coverage of a set it never
enumerated.

## 1. Family assignments

**Identifier correctness is now clean.** No fabricated ids remain. The 21
groundings where the declared family provably excluded its own representative
member have had that `term` removed: 15 were invented ids (the authored label
named a different protein), and 6 were real families whose *name* fit a protein
PANTHER classifies elsewhere -- the class label checking cannot see at all.

Those descriptors keep `preferred_term` and `representative_members` and simply
assert no PANTHER id. A replacement was not guessed: re-pointing a family is a
judgement about evolutionary placement, and doing it mechanically broke 9 real
PAINT links on the first attempt. An omitted id states "not established"; a
wrong id states something false in a field other tooling believes.

**Prose is a separate surface, and it was not clean.** Validation reads
`term.id`/`label` pairs, so a PANTHER id written into a `notes` or `description`
field is invisible to it. The same wrong id therefore survived in three places
per descriptor, and removing it from the two checked slots left the third
asserting what had just been disproved -- in the field a curator is most likely
to consult when re-grounding. Nine such claims across seven files were corrected
(the scan below reports 168 claims, all checked, 0 contradictions).
Several prose claims are genuinely true and were deliberately left alone
(CYP11A1/B1/B2 share PTHR24279; ACOX1/ACOX3 share PTHR10909; the ELOVLs share
PTHR11157), so a blanket edit would have destroyed correct content. That check now exists as
`src/ai_gene_review/validation/prose_panther_scan.py`
(`just scan-prose-panther`). Two constraints were
learned by getting them wrong: ids must be matched exactly (a truncating window
produced four false positives), and an id belongs to the accession it
*immediately* follows -- proximity alone pairs one protein's accession with the
next protein's id across a clause boundary. Measured against the nine errors it
was built from, it catches seven; the two misses are a symbol-phrased claim and
the first-named member of a shared claim, both documented rather than papered
over.

**The substantive remaining issue is precision, not correctness.** Most
family-level assignments have every representative member sitting in a single
subfamily — the subfamily is the sharper claim — and a quarter of those sit in
families split into 20+ subfamilies, where the family says least about any one
member. Both counts are scope-table rows, and the second *is* the
subfamily-precision advisory `just validate-modules` prints, computed from the
same `subfamily_precision_case` predicate rather than a second implementation
of it.

That shared predicate is new, and it is why these numbers changed. The report
previously claimed 817 of 907 and 206, asserting the advisory "tracks the same
population" while never printing the two together; the sweep was warning 199.
Both figures were recomputed independently here and had drifted — precisely the
failure the §2 rule below describes, left in place in the section that states
it. Deriving them from the validator's own predicate is what makes the
"same population" claim checkable instead of merely asserted.

The denominator is the descriptors where narrowing had a real answer, and its
complement is those where the answer is no — the family is the level that
covers every member, either because they span subfamilies or because one has
none to narrow to. The whole partition is a scope-table row, so the breakdown
is checkable rather than quoted.

Getting there meant letting the predicate report *which* outcome it reached
instead of collapsing them to a yes/no, and two attempts got it wrong in
opposite directions. The first counted family-level-with-a-resolvable-member,
sweeping in grounding-inconsistent descriptors (a correctness finding the sweep
reports separately, including the `PTHR23037` case below) and members PANTHER
assigns no subfamily at all. The second discarded a member the index places in no
subfamily and reported the remainder as a clean finding — so the advisory told a
curator that *every* representative member sits in one subfamily while naming a
member it places nowhere, and the narrowing it recommended would have dropped a
module's own *P. putida* exemplar. Two such advisories were inside the published
count, which is why it is now 197. A third error, caught in testing, compared
distinct subfamilies against member count and so misread every descriptor whose
members legitimately share a subfamily as partially unplaced, cutting the
finding count by 79.

A missing subfamily is worth stating precisely, because the whole judgement
rests on it. The index records what the consulted source returned, so a
bare-family row means no subfamily was *recorded* — not that PANTHER assigns
none. Which of the two resolution paths produced any given row is not recoverable
from the artifact, and both admit bare rows: `parse_sequence_classification`
keeps them deliberately, and the UniProt cross-reference fallback emits one when
a record carries no `:SF`. Nor does the organism account for it — 346 of the 360
*P. putida* accessions in the index do carry a subfamily. So if a particular
blank is a gap rather than a verdict, `histidine_catabolism` is a genuine finding
after all. Declining to recommend a narrowing that would drop a member you cannot
place is right under either reading, which is why these outcomes are named for
the record rather than for a verdict PANTHER has not given.

An earlier revision of this paragraph asserted the fallback as the sole
mechanism and invoked organisms PANTHER does not publish. Both were wrong, and
checkably so from this repo — the same overreach the rename had just removed one
field over.

The harm is concrete: **many more distinct proteins are grounded on family ids
that cannot distinguish between them than there are such ids** (scope table).
A member counts toward the family the committed index places it in; where the
index places it outside every family the descriptor declares, the declared
grounding stands. Both halves of that rule matter. Attributing a member to
every declared family credited each with the others' proteins, so the two
descriptors whose own prose says PANTHER splits these paralogs across families
— and names which member is in which — were counted as evidence that ids cannot
distinguish between proteins. Dropping those members instead understated it,
discarding the UniProt/PAINT disagreements (P08887 classified in PTHR23036
against a PAINT node in the declared PTHR23037) where the module's grounding is
the only claim available. The first correction here made exactly that second
error, and its cost was five family ids. The worst cases, among
families PANTHER splits into 20+ subfamilies, by distinct proteins then
subfamily count:

| family | name | distinct proteins | modules | subfamilies |
|---|---|---:|---:|---:|
| PTHR24416 | TYROSINE-PROTEIN KINASE RECEPTOR | 13 | 9 | 96 |
| PTHR24418 | TYROSINE-PROTEIN KINASE | 6 | 5 | 76 |
| PTHR11157 | FATTY ACID ACYL TRANSFERASE-RELATED | 6 | 1 | 58 |
| PTHR11848 | TGF-BETA FAMILY | 4 | 7 | 71 |
| PTHR43591 | METHYLTRANSFERASE | 4 | 3 | 29 |

An earlier revision of this table listed `PTHR22603` in the last row. It ties
on distinct proteins, so the row was an undeclared tie-break rather than an
error; the sort criterion is now stated.

A fifth claim once stood here — that 136 distinct molecular-function assertions
rest on 61 families that cannot support them all. It has been withdrawn rather
than restated. `FamilyMemberUse` does not carry the enclosing annoton's
molecular function, so the figure cannot be rederived from the code that
produced the others, and its original predicate is no longer recoverable. Per
the rule this report applies elsewhere, an unverifiable number is worse than a
missing one. Recovering it needs the descriptor walk to thread the annoton, and
the underlying point — that a shared id cannot support divergent MF claims —
survives in the paragraph below without it.

`PTHR24416` alone grounds EGFR, ERBB2, ERBB3, EPHA2, EPHB4, FGFR1, TRKA, TRKB,
VEGFR1, VEGFR2, MET, PDGFRB and INSR across nine modules. As a functional
grounding it asserts no more than "a receptor tyrosine kinase".

Not every case is a defect — `PTHR22912` collapses three dihydrolipoyl
dehydrogenase subfamilies that do share the function. The discriminator is
whether the module asserts *different* molecular functions on the shared id;
`validate_family_members` now emits a precision advisory for the heterogeneous
cases (threshold: 20 subfamilies).

## 2. Evolutionary history (PAINT)

**One hard contradiction found and fixed.** `erbb2_signaling.yaml` asserted
`GO:0004714` transmembrane receptor protein tyrosine kinase activity for ERBB3
while citing node `PTN002814617` — where PAINT records **IRD `GO:0004714`**,
i.e. that this activity was *lost* on this lineage. ERBB3 is the canonical
pseudokinase; it signals by heterodimerising with ERBB2. Corrected to
`GO:0038131` neuregulin receptor activity, which the same node retains as a
positive IBD row. `validate_paint_ptns` now blocks this class outright.

**Three other loss-bearing nodes are cited correctly** — the modules' claims are
consistent with what PAINT struck out:

| module | node | lost (IRD) | retained, and used |
|---|---|---|---|
| hedgehog_signaling | PTN000885245 | Wnt binding/receptor activity, canonical + non-canonical Wnt signaling | smoothened signaling, cilium, patched binding |
| nitric_oxide_cgmp_signaling | PTN001066032 | NADPH-hemoprotein reductase activity | nitric oxide synthase activity |
| nlr_signaling | PTN004670420 | molecular function inhibitor activity | pattern recognition receptor activity, response to muramyl dipeptide |

Smoothened losing its ancestral Wnt functions while retaining Hh signalling is
exactly the evolutionary story the node encodes, and the module reflects it.

**Evidence depth.** The unit is the *annotation*, not the node. Each PAINT
row's with/from is the seed set backing that one term, and "weak support for
propagating a specific function" is a claim about a term. Aggregating to the
node first forces a quantifier choice — is a node thin when *every* annotation
on it is thin, or when *any* is? — that moves the answer by more than half
again, and either way credits or blames a term with evidence that does not
back it. Those two node-level figures are deliberately not quoted here: they
are emitted by nothing, so they would drift exactly as the table did.

The scope-table row above gives both aggregations of that measure rather than
picking one: **a slim majority of distinct (node, term) annotations rest on ≤3
seed proteins**, and weighted by how often modules actually cite them, two
fifths. The first describes the evidence base, the second how much of
the propagation in use rests on it. No node has zero seeds. Reconstructions
this thin are weak support for propagating a specific function and are worth a
second look. The counts are not repeated here — the table is the one place
they are written, and it is regenerated by `just panther-report-stats`, so the
definition travels with the number.

Earlier revisions of this paragraph reported 22%/33% by pooling each node's
seeds across its rows, then 27%/39% by requiring *every* annotation on a node
to be thin — neither choice was stated, and both were made in the paragraph
warning against mixing populations. `PTN000329346` is the case that separates
them: two IBD rows of 3 seeds each sharing `UniProtKB:Q9Y5Y5`, so 5 pooled —
well-supported under pooling, while neither of its two annotations rests on
more than 3.

**Claim support.** 103 nodes exactly support the module's assertion. Of the 33
that appeared not to, 12 were GO ancestry artifacts (the node is annotated to a
child or parent term) — the check is now ancestry-aware. Of the 21 genuinely
disjoint, most share one shape: the node attests the *pathway role* (`P:`) while
the module asserts a *molecular function* (`F:`) the node says nothing about.
That is not a contradiction, but the MF claim rests on other evidence and the
advisory now says so explicitly.

## 3. Extant proteins

**Taxonomic plausibility is clean.** Resolving each descriptor's *nearest
enclosing* taxon scope, all 47 Bacteria-scoped family assignments use families
that genuinely occur in bacterial proteomes — zero taxon-constraint violations.

An earlier run that attributed any taxon in a file to every descriptor flagged
three eukaryote-only families in `selenocysteine_biosynthesis_incorporation.yaml`
(PSTK, SEPSECS, SECISBP2). That was an artifact of the crude scoping: the module
correctly splits a Bacteria-scoped SelA route from a Eukaryota-scoped
PSTK–SepSecS route via `variant_sets`. Taxon scope must be read from the nearest
enclosing context, not the file.

## Checks added by this pass

- **Loss contradiction** (error): a module may not assert a GO term that a cited
  ancestral node records as IRD/IKR.
- **Ancestry- and aspect-aware node support** (advisory): distinguishes "node is
  silent in this GO aspect" from "node supports an unrelated term".
- **Subfamily precision** (advisory): flags a family-level grounding whose
  members all sit in one subfamily of a 20+-subfamily family.
