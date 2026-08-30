---
title: "propagation_review Corpus Audit"
species: [human, yeast, worm, DICDI, SCHPO, ANOGA, ARATH, DROME]
autolink_gene_symbols: true
---

# `propagation_review` corpus audit (2026-08-26)

A re-review of every `review.propagation_review` block now in the gene reviews. The
question was not "is each biological call right" — that is the per-gene reviews' job —
but **is the structured taxonomy being applied consistently, and does it agree with the
prose next to it.**

Extraction and the mechanical checks: `scripts/` equivalent is inlined in the audit
run; the corpus snapshot is 1843 blocks across 366 gene review files.

## What the corpus looks like

| | |
|---|---|
| blocks | 1843 across 366 files |
| actions | ACCEPT 629 · KEEP_AS_NON_CORE 399 · MARK_AS_OVER_ANNOTATED 357 · MODIFY 237 · REMOVE 171 · NEW 28 · UNDECIDED 22 |
| root causes | NO_FAILURE_CORE 673 · NO_FAILURE_NON_CORE 389 · PROPAGATION_BAD 337 · TERM_SCOPING_PROBLEM 311 · SOURCE_BAD 40 · SOURCE_WEAK_OR_INFERRED 39 · EVIDENCE_CIRCULAR_OR_REDUNDANT 32 · UNRESOLVED 22 |
| evidence | IEA 763 · **IBA 749** · ISS 233 · ISO 41 · other 57 |

**Coverage note.** Only 41% of blocks are on IBA rows. The taxonomy has become a
general propagation-review vocabulary covering IEA, ISS and ISO as well — which the
schema allows ("propagated or inferred annotation") but which the project page still
frames as IBA-specific. Worth reconciling in the prose.

Every value used is a legal enum member; there are no schema violations.

## Finding 1 — the target's own accession marked `CIRCULAR_OR_REDUNDANT` (27 rows, 16 genes)

This is the one substantive defect, and it contradicts an explicitly documented rule.
`CLAUDE.md` and [IBA_REVIEW.md](../IBA_REVIEW.md#what-an-iba-actually-asserts-and-two-ways-to-misread-the-withfrom)
both state that a target appearing in its own `WITH/FROM` is **correct and expected** —
the target's own experimental annotation is one of the descendant evidences the PAINT
curator used to place the IBD — and that such a source must **never** be marked
`CIRCULAR_OR_REDUNDANT`.

27 rows do exactly that. The prose sometimes states the inverted reading outright, e.g.
AAK1: *"The IBA includes the human target itself among its sources, so that item is
self-supporting and adds no independent propagation evidence."*

The data refutes the inverted reading in **26 of 27** cases: the target does carry its
own experimental annotation for the same term, which is precisely why it seeded the IBD.

| Grounding on the target | rows |
|---|---|
| own experimental annotation at the **same** term (IDA/IMP/EXP/TAS) | 20 |
| own experimental annotation at a **descendant** term | 6 |
| no experimental annotation found in the cached set | 1 (LNX1, GO:0005737) |

The six descendant cases: LMTK2 `GO:0004672` → IDA `GO:0004674`; LMTK3 `GO:0004672` →
EXP `GO:0106310`; AFF1 `GO:0006355` → IMP `GO:0032968`; LPGAT1 `GO:0005783` → IMP
`GO:0005789`, `GO:0016746` → IDA `GO:0071617`, `GO:0012505` → the same ER evidence.

Affected genes (all human): A4GNT, AADAC, AAK1, AASDHPPT, ADAMTSL5, AFF1, LMTK2,
LMTK3, LNX1, LPAR6, LPCAT4, LPGAT1, LPIN2, LRBA, LRCH1, LRCH3.

**The corpus already contains the correct handling**, which makes this a consistency
fix rather than a judgement call — ADPRS marks its self-source `SUPPORTS_TRANSFER` with
the comment *"self-reference: the target is its own IBD seed."* That is the model.

## Finding 2 — the structured fields drift from the prose

Recurring pattern: `review.reason` is careful and correct while the enums beside it say
something weaker or different. Three confirmed instances, plus two systematic classes.

- **ADPRS `GO:0071451`** — `root_cause: SOURCE_BAD`, yet all three `source_entities` are
  `SUPPORTS_TRANSFER`. The prose says the problem is that the *term* names the wrong
  reactive oxygen species (superoxide vs the hydrogen peroxide actually assayed), which
  is `TERM_SCOPING_PROBLEM`. Its `failure_modes: [GRANULARITY_MISMATCH]` is contradicted
  by its own sentence *"neither contains the other"* — siblings are not a granularity
  mismatch.
- **LPA `GO:0004252`** — `failure_modes: [PSEUDO_OR_SUBACTIVITY_LOSS]`, but the same
  review states apo(a) "retains the catalytic His-Asp-Ser triad" and argues from the
  zymogen activation junction instead. Independently confirmed: the triad is intact
  (see [msa/RESULTS.md](msa/RESULTS.md#3-six-further-pseudo-enzyme-claims-2026-08-26-pass)).
  Nothing was lost from the active site.
- **8 `MODIFY` rows carry a `NO_FAILURE_*` root cause** (AFF1 ×2, LNX1 ×3, SERINC1/3/5).
  Proposing a replacement term *is* a term-scoping problem by definition.
- **34 `NO_FAILURE_*` rows carry `failure_modes`**, including 4 `WRONG_ORTHOLOG_OR_PARALOG`
  (ACAP3 ×2, ACTG2, ACTL7B) and 1 `REGULATORY_SIGN_INVERSION` (AEBP2) — naming a
  failure while declaring no failure.
- **26 `MARK_AS_OVER_ANNOTATED` rows pair with `NO_FAILURE_NON_CORE`** (SLC25A1, CYP51A1,
  NUBPL, SHMT1, NADSYN1 …). Milder: arguably these should be `KEEP_AS_NON_CORE`, or the
  root cause should be `TERM_SCOPING_PROBLEM`.

The consistent direction — prose better than enums — means the enums should be treated
as a **derived index over the prose**, not as independent evidence. Downstream tooling
that aggregates `failure_modes` without reading `reason` will over-count
`PSEUDO_OR_SUBACTIVITY_LOSS` and under-count `TERM_SCOPING_PROBLEM`.

## Checks that fired but were wrong (recorded so they are not re-raised)

Applying the project's own discipline to the audit itself:

- **`root_cause` claiming failure while all sources `SUPPORTS_TRANSFER` (93 rows)** — 92
  are `TERM_SCOPING_PROBLEM`, where this is *coherent, not contradictory*: the source
  genuinely supports transferring the biology and the fault is in the GO term chosen.
  Separating those two axes is the point of the taxonomy. Only the ADPRS row above is a
  real contradiction.
- **`ACCEPT` with a failure root cause (LMTK2 `GO:0070853`, LRCH4 `GO:0034123`)** — this
  is the taxonomy working as designed: accept the annotation, flag the `WITH/FROM`
  citation as bad. LMTK2's catch is excellent and verified against UniProt: the source
  `UniProtKB:P13533` is **MYH6**, whose recommended name is "Myosin-6" (cardiac myosin
  heavy chain), *not* the unconventional **myosin VI / MYO6** (`Q9UM54`) actually
  assayed — a real homonym trap that the review caught and documented.

## Suggested actions (none applied)

> Finding 1 is tracked as
> [issue #2761](https://github.com/ai4curation/ai-gene-review/issues/2761).

1. Retype the 27 self-source rows to `SUPPORTS_TRANSFER` with an ADPRS-style comment,
   and fix the AAK1-style prose that states the inverted reading. This is mechanical and
   safe: the rule is explicit and the evidence check above confirms it case by case.
2. Retype ADPRS `GO:0071451` to `TERM_SCOPING_PROBLEM` and drop `GRANULARITY_MISMATCH`.
3. Retype LPA `GO:0004252`'s failure mode away from `PSEUDO_OR_SUBACTIVITY_LOSS`.
4. Reconcile the 8 `MODIFY` + `NO_FAILURE_*` rows.
5. Decide whether the project page should describe the taxonomy as covering all
   propagated evidence (IEA/ISS/ISO), which is what the corpus now does.
