# PANTHER family assignment review

A pass over all 279 module YAMLs examining every PANTHER family assignment, the
PAINT evolutionary evidence cited for it, and the extant proteins named as its
representatives. Generated against PANTHER 19.0.

## Scope

| | count |
|---|---|
| module files | 279 |
| family/subfamily descriptors with an id and a representative member | 1,001 |
| declared at family level | 900 |
| declared at subfamily level | 101 |
| family descriptors asserting no id | 163 (across 50 modules) |
| PAINT nodes resolved | 369 |
| prose PANTHER claims checked | 168 / 168 |
| cited accessions resolved to a PANTHER family | 1,450 / 1,485 |

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

**The substantive remaining issue is precision, not correctness.** 814 of the
900 family-level assignments have every representative member sitting in a
single subfamily — the subfamily is the sharper claim. This matters most where
the family is heterogeneous: 205 of those sit in families split into 20+
subfamilies.

The harm is concrete. **332 distinct proteins are grounded on 136 family ids
that cannot distinguish between them**, and **136 distinct molecular-function
assertions rest on 61 families that cannot support them all**. The worst cases:

| family | name | distinct proteins | modules | subfamilies |
|---|---|---:|---:|---:|
| PTHR24416 | TYROSINE-PROTEIN KINASE RECEPTOR | 13 | 9 | 96 |
| PTHR24418 | TYROSINE-PROTEIN KINASE | 6 | 5 | 76 |
| PTHR11157 | FATTY ACID ACYL TRANSFERASE-RELATED | 6 | 1 | 58 |
| PTHR11848 | TGF-BETA FAMILY | 4 | 7 | 71 |
| PTHR22603 | CHOLINE/ETHANOALAMINE KINASE | 4 | 1 | 20 |

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

**Evidence depth.** 82 of 369 resolved nodes are reconstructed from ≤3 seed
proteins; only 3 have no seed at all, and none of those three is the stated
evidence for a molecular-function claim. Reconstructions that thin are weak
support for propagating a specific function and are worth a second look.

Counting seeds requires care: PAINT records them as model-organism identifiers
(MGI 4,514, RGD 2,807, FB 1,801, WB 1,067, SGD 511, ZFIN 479, ...) at least as
often as UniProtKB (7,912). Counting only `UniProtKB:` seeds inflates the
"shallow" figure to 180. The pre-existing seed-overlap warning had the same
blind spot — 3 of its 9 firings were vacuous, comparing a representative against
a node whose seeds carry no UniProt accession at all — and now says so instead.

**Claim support.** 100 nodes exactly support the module's assertion. Of the 33
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
