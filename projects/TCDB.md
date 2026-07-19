---
title: "TCDB → GO Transporter-Activity Mapping & Gap Project"
maturity: SCOPING
tags: [PIPELINE]
species: [ARATH, human]
---

# TCDB → GO Transporter-Activity Mapping & Gap Project

## Overview

This project examines the **Transporter Classification Database (TCDB) as a
source of GO molecular-function annotations for membrane transport proteins**, in
the same spirit as the [RHEA](RHEA.md) (reactions), [EC](RHEA.md)/`ec2go`, and
[CAZy](GLYCOBIOLOGY.md) source-audit projects. TCDB is the **only transporter
classification adopted by the IUBMB**, organising transport systems into a
five-level **TC number** (`class.subclass.family.subfamily.system`, e.g.
`2.A.69.1.1`) that is the transport analogue of an EC number.

The defining fact of this project — and what makes it different from RHEA and EC
— is a **coverage gap at the pipeline level**:

> **There is no `tc2go` external2go mapping.** TCDB is *absent* from GO's
> `external2go` directory (which ships `ec2go`, `rhea2go`, `interpro2go`,
> `pfam2go`, `uniprotkb_kw2go`, … but no `tc2go`). Unlike EC (`GO_REF:0000003`)
> and RHEA (`GO_REF:0000116`), a TCDB classification does **not** propagate into
> GOA through a curated pipeline. Confirmed live against
> `http://current.geneontology.org/ontology/external2go/` (GO release
> `2026-05-19`).

So, like RHEA, the analysis runs in **two directions**, but with a heavier
emphasis on the reverse (gap) direction because the forward pipeline does not
exist:

1. **Forward (what TCDB *does* offer).** TCDB publishes its own per-protein GO
   associations at `https://tcdb.org/cgi-bin/projectv/public/go.py`. Is that dump
   usable as a `tc2go` seed, and at what quality and specificity?
2. **Reverse (gap).** Where does a UniProtKB entry carry a TCDB cross-reference
   (`DR TCDB;`) but **no GO transmembrane-transporter-activity term at all**?
   With no pipeline, this "falls through the cracks" gap is *structural*, not
   incidental.

See [TCDB-METHODOLOGY.md](TCDB/TCDB-METHODOLOGY.md) for queries, the reproducible
probe script, and the closure caveat.

## Key Findings (scoping pass)

- **No `tc2go` pipeline exists.** TCDB is not in GO's `external2go` directory —
  the single most important structural finding. EC and RHEA reach GO through
  curated external2go mappings; TCDB does not.
- **TCDB *does* publish a raw GO dump, but it is noisy and multi-aspect.** The
  `go.py` file has **34,497 rows** mapping **4,943 distinct TC systems**
  (5-level) across **589 TC families** (3-level) to **3,518 distinct GO terms** —
  but only **13% of rows (4,557) and 12% of GO terms (424) are actually
  transmembrane-transporter-*activity* (molecular function)**. The dump is
  dominated by cellular-component and biological-process terms
  (`GO:0016021 integral component of membrane` ×3,876;
  `GO:0005886 plasma membrane` ×2,300; `GO:0055085 transmembrane transport`
  ×1,422; `GO:0006810 transport` ×882) plus outright noise
  (`GO:0005515 protein binding` ×452; `GO:0005488 binding` ×145;
  `GO:0003824 catalytic activity` ×56 — on transporters). It is an **aggregation
  of member-protein annotations, not a curated mapping**, so it cannot be
  adopted as `tc2go` wholesale.
- **The reverse gap is large and structural.** Of **8,758 reviewed (Swiss-Prot)
  entries** carrying a TCDB cross-reference, **4,431 (50.6%) carry no GO
  transporter-activity term at all** (`GO:0005215` closure). This is the
  headline: *half of all reviewed transporters with an IUBMB TC classification
  have no transport MF term propagated from it.* (Exact-match upper bound on the
  gap; see caveat.) Across all of UniProtKB the TCDB cross-reference count is
  **16,344**.
- **The gap is a specificity problem, mirroring RHEA.** A TC *family*
  (3-level) is frequently poly-specific: the MFS superfamily `2.A.1` alone spreads
  across **49 distinct substrate-specific MF terms** in `go.py`
  (D-glucose, fructose, nitrate, heme, biotin, spermine, …); the APC family
  `2.A.3` across 11. The right GO target lives at the **subfamily** level, not
  the family — exactly the parent-vs-child specificity lesson RHEA and CAZy already
  learned. Some families *are* cleanly mono-specific (e.g. `2.A.69` auxin efflux
  carrier → `GO:0010329`).
- **This repo already contains the exemplars.** **353 gene folders** carry a
  `DR TCDB;` cross-reference (e.g. PIN1, AUX1, SOS1, HKT1, CHL1/NRT1.1, AQP1),
  several with *experimental* transport-activity GO terms — ready-made backing for
  a curated `tc2go` seed and for closure-filtered gap review.

## TCDB's own `go.py` dump: usable seed, but only after filtering

| Slice | Count | % of dump |
|---|---:|---:|
| Rows (GO ↔ TC-system) | 34,497 | 100% |
| Distinct TC systems (5-level) | 4,943 | — |
| Distinct TC families (3-level) | 589 | — |
| Distinct GO terms | 3,518 | — |
| **Rows whose GO term is a transporter-activity MF** | **4,557** | **13%** |
| Distinct transporter-activity MF terms | 424 | 12% of GO terms |
| TC systems with ≥1 transporter-activity MF term | 2,866 | 58% |
| TC families with ≥1 transporter-activity MF term | 222 / 589 | 37% |

Rows by TC class: `1` channels/pores 7,984 · `2` electrochemical-potential-driven
11,959 · `3` primary active 10,290 · `4` group translocators 890 · `5`
transmembrane electron carriers 693 · `8` accessory 1,092 · `9` incompletely
characterised 1,589. Computed live by
[`tcdb_go_probe.py`](TCDB/tcdb_go_probe.py) (`--tcdb-go`); the transporter-activity
MF closure (1,042 terms, `is_a GO:0022857 ∪ GO:0005215`) comes from QuickGO.

The take-home: **the clean, adoptable slice of `go.py` is the 13% that is
transporter-activity MF.** [`build_tc2go.py`](TCDB/build_tc2go.py) distils exactly
that slice into an SSSOM candidate set (below).

## Reverse gap: half of reviewed transporters lack a transport MF term

| Reviewed Swiss-Prot entries with a `DR TCDB;` xref | Count | % |
|---|---:|---:|
| Total | 8,758 | 100% |
| …with `GO:0022857` transmembrane transporter activity (closure) | 4,208 | 48% |
| …with `GO:0005215` transporter activity (closure) | 4,327 | 49% |
| **…with NO transporter-activity term (gap upper bound)** | **4,431** | **50.6%** |

Computed live against the UniProtKB REST API (`database:tcdb AND reviewed:true`,
GO-closure-expanded on the GO side) by [`tcdb_go_probe.py`](TCDB/tcdb_go_probe.py)
(`--gap`). Because there is no `tc2go`, the only routes by which these transporters
*could* get a transport MF term are EC/`ec2go` (many transporters have no EC),
InterPro/`interpro2go`, or manual curation — so a structural half-coverage is
unsurprising, and is precisely the gap a `tc2go` pipeline would close.

**Closure caveat (mandatory).** The 50.6% is an **exact-match upper bound**: some
entries carry a transport-related term *outside* the `GO:0005215` MF branch (a
transport *process* BP term, or a channel-complex CC term) that a closure-aware,
cross-branch audit would credit. As in RHEA/CAZy, high gap = **candidate for
closure-filtered review**, not a confirmed missing annotation.

## Specificity: the TC family is usually too general

- **TC → GO is a specificity bottleneck.** Poly-specific superfamilies collapse
  many substrates onto one family id: `2.A.1` (MFS) touches 49 distinct
  transporter-activity MF terms, `2.A.3` (APC) 11, `2.A.55` (NRAMP) 11. A single
  family→GO row is therefore usually a `narrowMatch` (the GO term is really a
  *subfamily* property), not an `exactMatch`.
- **…but some families are clean.** `2.A.69` (auxin efflux carrier) →
  `GO:0010329 auxin efflux transmembrane transporter activity` and `1.A.8` (MIP)
  → `GO:0015250 water channel activity` are mono-specific — one GO term fits the whole family —
  ready-to-add `exactMatch` rows.

The curated seed encodes this distinction directly (below).

## Curated mappings (SSSOM)

Filling the gap is a curation deliverable, not just an audit. Two SSSOM files,
same format as [RHEA](RHEA/rhea2go.sssom.yaml) and
[CAZy](GLYCOBIOLOGY.md):

- **[`tc2go.sssom.yaml`](TCDB/tc2go.sssom.yaml)** — a **hand-curated seed** of TC
  family → GO transporter-activity mappings, each backed by a **reviewed
  Swiss-Prot transporter** (five of the six are reviewed *in this repo* with
  experimental evidence):
  - `exactMatch` (mono-specific, ready-to-add): `2.A.69` AEC → `GO:0010329`
    (backing PIN1 Q9C6B8, IDA/IMP); `1.A.8` MIP → `GO:0015250` (backing AQP1
    P29972).
  - `narrowMatch` (GO term is a subfamily property of a poly-specific family):
    `2.A.17` POT/PTR → `GO:0015112 nitrate transmembrane transporter activity`
    (backing CHL1/NRT1.1 Q05085, IMP — a classic too-general-family case: a *peptide*
    transporter family whose plant NPF subfamily moves nitrate); `2.A.18` AAAP →
    `GO:0010328` (AUX1 Q96247, IDA); `2.A.36` CPA1 → `GO:0015385` (SOS1 Q9LKW9);
    `2.A.38` Trk → `GO:0015079` (HKT1 Q84TI7).
- **[`tc2go.generated.sssom.yaml`](TCDB/tc2go.generated.sssom.yaml)** — a
  **machine-derived candidate set** (154 families, 477 rows: 82 `exactMatch`, 395
  `narrowMatch`) distilled by [`build_tc2go.py`](TCDB/build_tc2go.py): the live
  join of TCDB's `go.py` with QuickGO, keeping only non-obsolete
  transporter-activity MF terms, aggregated to the TC family (min 2 supporting
  members). No row is hand-typed; this is TCDB's own assertion filtered for aspect
  + obsolescence, and must be reviewed before adoption.

Every GO id/label is validated non-obsolete and molecular-function; the GO object
is bound to the MF branch. Validate with `just validate-tcdb-mappings` (SSSOM
structural validation + GO term/label validation; generated nested views
[`tc2go.terms.yaml`](TCDB/tc2go.terms.yaml),
[`tc2go.generated.terms.yaml`](TCDB/tc2go.generated.terms.yaml)).

## How this differs from EC, RHEA, and CAZy

| | EC (`ec2go`) | RHEA (`GO_REF:0000116`) | CAZy | **TCDB** |
|---|---|---|---|---|
| GO aspect | MF (enzyme activity) | MF (enzyme activity) | MF (glycoenzyme) | **MF (transporter activity)** |
| external2go pipeline | **yes** | **yes** | no (built here from EC) | **no — none at all** |
| Source GO material | curated mapping | curated mapping | via EC bridge | **noisy multi-aspect `go.py` dump** |
| Dominant failure mode | too-general term | parent-vs-child specificity | poly-specific family | **no pipeline + over-general family + aspect noise** |
| Emphasis | over-annotation audit | both | gap-filling | **gap-filling (structural half-coverage)** |

TCDB is the most **under-connected** of these sources: its classification is
IUBMB-endorsed and reaction-grounded, yet it has no route into GO. The expected
verdict skew is heavily toward **`NEW` / gap-filling**, tempered by the family
over-generality problem (prefer the subfamily-specific child term).

## Curation Recommendations (preliminary)

1. **Treat TCDB as a gap source, not an over-annotation source.** With no
   pipeline, the value is finding correct transport activities GO is missing —
   half of reviewed TC-classified transporters lack a transport MF term.
2. **Curate at the subfamily, not the family.** A TC family is usually
   poly-specific; map the substrate-specific GO child (`narrowMatch`) using the
   4- or 5-level TC id, reserving `exactMatch` for genuinely mono-specific
   families (AEC, MIP-water).
3. **Filter `go.py` to transporter-activity MF before use.** 87% of the dump is
   CC/BP/generic/noise; only the 13% MF-activity slice is adoptable, and even
   that needs specificity review.
4. **Always closure-filter (cross-branch) before calling a gap.** The 50.6% is an
   upper bound; subtract entries carrying any transport-related descendant/BP/CC
   term first.
5. **Prefer EC-bridge support where it exists.** Some transporters (e.g. primary
   active `3.A` ATPases) carry an EC and reach GO via `ec2go`; use that as
   corroboration and to avoid duplicating an existing route.

## Follow-Up Targets

| Target | Rationale |
|--------|-----------|
| Closure-aware (cross-branch) reverse gap | Separate true gaps from transport-BP/channel-CC coverage in the 4,431 reviewed no-MF entries; promote real gaps to gene reviews. |
| Subfamily-level `tc2go` from `go.py` | Rebuild the generated set at 4/5-level TC ids so poly-specific families resolve to substrate-specific MF children. |
| Exemplar gene reviews | Run the full review workflow on 2–3 confirmed-gap transporters already in this repo (353 candidates), mirroring the RHEA/UniPathway exemplar pattern. |
| "No transporter-activity MF at all" family set | The 367 TC families with no MF-activity term in `go.py` → candidates for `proposed_new_terms` or accessory (class 8/9) exclusion. |
| Propose `tc2go` to GO | The strategic deliverable: a curated, specificity-correct `tc2go` external2go mapping seeded by this project. |

## Project Status

- **Started**: 2026-07-18
- **Maturity**: SCOPING — the absence of a `tc2go` pipeline confirmed; TCDB's
  `go.py` dump characterised and filtered; the structural reverse gap quantified;
  curated seed + machine-generated candidate SSSOM built and validated.
- **Computed live** (2026-07-18): no `tc2go` in `external2go` (GO release
  `2026-05-19`); `go.py` = 34,497 rows → 4,943 TC systems / 589 families / 3,518
  GO terms, of which 13% rows / 12% terms are transporter-activity MF; reverse gap
  4,431 / 8,758 (50.6%) reviewed TCDB entries with no transport MF term
  (16,344 all-UniProtKB TCDB xrefs); 353 local gene folders carry a TCDB xref.
- **Reproducible scripts**: [`TCDB/tcdb_go_probe.py`](TCDB/tcdb_go_probe.py)
  (dump characterisation + reverse gap),
  [`TCDB/build_tc2go.py`](TCDB/build_tc2go.py) (generated SSSOM).
- **Curated mappings**: [`TCDB/tc2go.sssom.yaml`](TCDB/tc2go.sssom.yaml) — 6
  review-backed seed rows; [`TCDB/tc2go.generated.sssom.yaml`](TCDB/tc2go.generated.sssom.yaml)
  — 477 machine-derived candidate rows; `just validate-tcdb-mappings`.
- **Current conclusion**: TCDB is a high-quality, IUBMB-endorsed transporter
  classification that is **structurally disconnected from GO** — no external2go
  mapping, a noisy self-published `go.py` dump, and half of reviewed TC-classified
  transporters carrying no transport MF term. The high-value deliverable is a
  curated, specificity-correct `tc2go` mapping.
