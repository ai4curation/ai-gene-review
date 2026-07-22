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
— is a **missing annotation pipeline, not a missing mapping**:

> **GO already curates TCDB cross-references on its terms, but there is no
> `tc2go` external2go *annotation pipeline*.** GO curators have attached TC
> references to **170 non-obsolete molecular-function terms** (via `xref: TC:`
> clauses and definition dbxrefs) — a real, high-quality *partial* TC→GO mapping
> that lives inside the ontology. What is missing is the propagation half: TCDB
> is *absent* from GO's `external2go` directory (which ships `ec2go`, `rhea2go`,
> `interpro2go`, … but no `tc2go`), so unlike EC (`GO_REF:0000003`) and RHEA
> (`GO_REF:0000116`) a protein's TCDB classification is **not** turned into a GAF
> annotation. The correspondence exists on the *terms*; it just isn't applied to
> *proteins*. Both facts confirmed live (GO release `2026-05-19`; `go-basic.obo`).

So the analysis runs in **two directions**:

1. **Forward (candidate sources).** GO's 170 TC xrefs are the best starting leads,
   but neglected and unreviewed. TCDB *also* publishes a per-protein GO dump
   (`https://tcdb.org/cgi-bin/projectv/public/go.py`), noisier but wider. Both are
   candidate pools; neither is safe to propagate without per-entry curation.
2. **Reverse (gap).** Where does a UniProtKB entry carry a TCDB cross-reference
   (`DR TCDB;`) but **no GO transmembrane-transporter-activity term at all**?
   Because GO's xrefs sit on terms and are never propagated to proteins, this
   "falls through the cracks" gap is *structural*, not incidental.

See [TCDB-METHODOLOGY.md](TCDB/TCDB-METHODOLOGY.md) for queries, the reproducible
probe script, and the closure caveat.

## Key Findings (scoping pass)

- **GO carries TC cross-references, but as neglected *sources* (the correction to
  the headline).** GO terms hold curator TC references: **202 references on 170
  non-obsolete molecular-function terms**, spanning **63 TC families / 185 TC
  systems** (extracted live from `go-basic.obo` by
  [`extract_go_tc_xrefs.py`](TCDB/extract_go_tc_xrefs.py)). These are real leads,
  but they are largely neglected and are *not* a ready mapping: an xref does not
  by itself justify **propagating** the GO term to every protein with that TC id.
  That propagation judgment is curated by hand, per entry (see below).
- **What is actually missing is the annotation pipeline.** TCDB is not in GO's
  `external2go` directory, so those curated term-xrefs are **never propagated to
  the proteins** that carry the TC number. EC and RHEA turn a classification into
  a GAF annotation (`GO_REF`); TCDB does not. That, not the absence of a mapping,
  is the structural gap.
- **TCDB *also* publishes a raw GO dump, but it is noisy and multi-aspect.** The
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

## GO's TCDB cross-references: neglected sources, not a ready mapping

GO carries TC references on molecular-function terms. Extracted live from
`go-basic.obo` ([`extract_go_tc_xrefs.py`](TCDB/extract_go_tc_xrefs.py), obsolete
terms excluded):

| | Count |
|---|---:|
| TC xref references on GO terms | 202 (61 `xref: TC:` + 141 definition dbxref) |
| Distinct TC→GO source pairs (deduped) | 194 |
| Distinct GO terms (all molecular function) | 170 |
| Distinct TC systems (5-level) | 185 |
| Distinct TC families (3-level) | 63 |

**These are leads, not an asserted mapping.** GO's TC xrefs are largely
neglected, and the term-`xref:` vs definition-dbxref distinction carries no
reliable signal, so they are treated alike. Crucially, an xref says *"a curator
once linked this TC entry and this GO term"* — **not** *"every protein with this
TC number has this function"*. Whether a lead is safe to **propagate** (a protein
inheriting the GO term from its TC id) is a separate judgment that must be
**curated by hand, per entry** — see the propagation verdicts below.

They are shipped, inverted to TC→GO, as
[`tc2go.from_go.sssom.yaml`](TCDB/tc2go.from_go.sssom.yaml) — every row
`skos:relatedMatch` + `semapv:UnspecifiedMatching` (i.e. explicitly *unreviewed
source*). Many are keyed at the specific TC system (e.g. `GO:0005335 ←
TC:2.A.22.1.1`, SERT), where propagation is usually safe; others sit on a whole
family, where it usually is not. They cover only **63 of TCDB's 2,235 families
(3%)** and, being ontology annotations rather than an `external2go` mapping, are
**not propagated to proteins** — so they do not close the reverse gap below.

## Propagation curation: every GO-xref lead scored by evidence

Whether a lead is safe to **propagate** — can a protein carrying the TC id inherit
the GO term? — is answered for all 194 source pairs with **UniProt member
evidence**, not assertion. For each pair, [`curate_propagation.py`](TCDB/curate_propagation.py)
fetches the reviewed Swiss-Prot proteins carrying that TC id (level-aware: a
5-level system matched exactly, a coarser id by dot-bounded prefix) and measures
what fraction also carry the GO term (ontology-closure expanded, so a member with
a more specific child still counts). The fraction is the propagation signal:

| Verdict (SSSOM predicate) | Rule | Count |
|---|---|---:|
| **JUSTIFIED** (`exactMatch`) | ≥2 members, ≥70% carry the term (or 1/1) | **80** |
| **NOT JUSTIFIED at this TC level** (`narrowMatch`) | ≥3 members, <50% carry it | **23** |
| **GAP_CANDIDATE** (`relatedMatch`) | specific system (≥4-level), member(s) exist but 0 carry it | **62** |
| **CLASS_LEVEL** (`broadMatch`) | whole TC class/subclass (≤2-level); broad by construction | **12** |
| **NO_REVIEWED_MEMBER** (`relatedMatch`) | no reviewed protein xref'd to the TC id | **10** |
| **UNCERTAIN** (`relatedMatch`) | ambiguous small-n middle | **7** |

Shipped as [`tc2go.propagation.sssom.yaml`](TCDB/tc2go.propagation.sssom.yaml)
with the per-pair evidence (`k/n`) in every comment; the full table is
[`data/propagation_evidence.tsv`](TCDB/data/propagation_evidence.tsv). Findings:

- **Propagation is safe at the system level.** 70 of the 80 JUSTIFIED pairs are
  5-level TC systems (e.g. `3.A.2.1.1 → GO:0046933 proton-motive-force-driven ATP
  synthase activity`, 8/8; `TC:2.A.19.2.- → GO:0015369 calcium:proton antiporter`,
  8/8) — the evidence backs the "curate at the system, not the family" rule.
- **`narrowMatch` is where an xref would over-propagate.** e.g. the MFS
  sugar-porter subfamily `2.A.1.1 → GO:0005351 carbohydrate:proton symporter
  activity` (only 35/88 members, 40%), or `1.A.9 → GO:0160039 serotonin-gated
  chloride channel activity` (1/59): correct for a few members, wrong for the rest.
- **`GAP_CANDIDATE` is a reverse-gap harvest.** 62 leads are specific systems where
  GO curates a precise term but the reviewed member is annotated only to a
  *parent/sibling* — e.g. `2.A.1.1.10 → GO:0005364 maltose:proton symporter` whose
  member P15685 carries the general `carbohydrate:proton symporter activity` but not
  the maltose-specific child. These are refinement leads for the gene-review
  workflow, not propagation bases.
- **`CLASS_LEVEL` (12) and `NO_REVIEWED_MEMBER` (10) are honestly out of scope** —
  class/subclass xrefs (`TC:1 → channel activity`) are broad by construction; the
  no-member cases have only TrEMBL entries or a reviewed protein that lacks the
  `DR TCDB` line (a UniProt xref gap, e.g. MelB). Neither is silently included.
- **Several `k<n` JUSTIFIED cases are also gap finds** — e.g. `3.A.3.1.1 →
  GO:0005391` (4/5): the activity is shared, so the 5th member is a missing
  annotation.

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
(`--gap`). GO's curated term-xrefs do **not** help here — they sit on GO terms,
not on the proteins — so the only routes by which these transporters *could* get a
transport MF term are EC/`ec2go` (many transporters have no EC),
InterPro/`interpro2go`, or manual curation. A structural half-coverage is
therefore unsurprising, and is precisely the gap a `tc2go` propagation pipeline
would close.

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

Filling the gap is a curation deliverable, not just an audit. Four SSSOM files,
same format as [RHEA](RHEA/rhea2go.sssom.yaml) and
[CAZy](GLYCOBIOLOGY.md):

- **[`tc2go.from_go.sssom.yaml`](TCDB/tc2go.from_go.sssom.yaml)** — GO's TC xrefs
  as **unreviewed sources/leads** (194 TC→GO pairs, 170 MF terms, 63 families;
  all `relatedMatch` + `UnspecifiedMatching`). The candidate pool to curate *from*
  — not a mapping to adopt as-is.
- **[`tc2go.propagation.sssom.yaml`](TCDB/tc2go.propagation.sssom.yaml)** — those
  same 194 leads **scored for propagation by UniProt member evidence** (80
  JUSTIFIED `exactMatch`, 23 `narrowMatch`, 62 GAP_CANDIDATE, 12 CLASS_LEVEL, 17 other;
  see above). Evidence-
  derived (`semapv:CompositeMatching`), the systematic first pass over every lead.
- **[`tc2go.generated.sssom.yaml`](TCDB/tc2go.generated.sssom.yaml)** — a second,
  noisier candidate pool: **machine-derived coverage extension** (154 families,
  477 rows) from TCDB's `go.py` × QuickGO (see below). **110 of its 154 families
  are *not* in GO's xrefs** — the genuine coverage it adds — but it is
  family-level and needs review.
- **[`tc2go.sssom.yaml`](TCDB/tc2go.sssom.yaml)** — the **hand-curated exemplar
  layer**: 8 mappings, each with an explicit *propagation verdict* and backed by a
  **reviewed Swiss-Prot transporter** read individually (deeper than the automated
  scoring). This is where a source becomes a fully-backed mapping:
  - `exactMatch` — **propagation justified** (member set is mono-specific at the
    cited TC level): the 5-level systems `2.A.22.1.1` SERT → `GO:0005335` (backing
    SERT/SLC6A4 P31645) and `3.A.3.1.1` Na⁺/K⁺-ATPase → `GO:0005391` (ATP1A1
    P05023) — both curated *up* from GO sources — plus the mono-specific family
    `2.A.69` AEC → `GO:0010329` (PIN1 Q9C6B8, IDA/IMP).
  - `narrowMatch` — **propagation NOT justified at that TC level** (the GO term is
    a subfamily property): `1.A.8` MIP → water (aquaglyceroporins move glycerol,
    not water); `2.A.17` POT/PTR → nitrate (CHL1/NRT1.1 Q05085); `2.A.18` AAAP →
    auxin influx (AUX1 Q96247); `2.A.36` CPA1 → Na⁺/H⁺ (SOS1 Q9LKW9); `2.A.38` Trk
    → K⁺ (HKT1 Q84TI7). Six of the eight fall in a family GO already xrefs
    (independent corroboration).
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
is bound to the MF branch. Validate all three with `just validate-tcdb-mappings`
(SSSOM structural validation + GO term/label validation; generated nested views
[`tc2go.terms.yaml`](TCDB/tc2go.terms.yaml),
[`tc2go.generated.terms.yaml`](TCDB/tc2go.generated.terms.yaml),
[`tc2go.from_go.terms.yaml`](TCDB/tc2go.from_go.terms.yaml)).

Across all three sources, **173 of TCDB's 2,235 families (8%)** have at least one
candidate GO transporter-activity mapping.

## How this differs from EC, RHEA, and CAZy

| | EC (`ec2go`) | RHEA (`GO_REF:0000116`) | CAZy | **TCDB** |
|---|---|---|---|---|
| GO aspect | MF (enzyme activity) | MF (enzyme activity) | MF (glycoenzyme) | **MF (transporter activity)** |
| external2go **annotation** pipeline | **yes** | **yes** | no (built here from EC) | **no** |
| TC/ID references in the ontology (term xrefs) | some | some | some | **yes but neglected — 170 MF terms / 63 families, unreviewed** |
| Source GO material | curated mapping | curated mapping | via EC bridge | **GO's neglected term xrefs + noisy `go.py` dump (both = leads)** |
| Dominant failure mode | too-general term | parent-vs-child specificity | poly-specific family | **no propagation pipeline + over-general family + go.py aspect noise** |
| Emphasis | over-annotation audit | both | gap-filling | **gap-filling (structural half-coverage)** |

TCDB is the most **under-connected** of these sources: it has a real, curated
term-level correspondence to GO, but no pipeline to propagate it to proteins, so
half of TC-classified transporters still lack a transport MF term. The expected
verdict skew is heavily toward **`NEW` / gap-filling**, tempered by the family
over-generality problem (prefer the subfamily-specific child term).

## Curation Recommendations (preliminary)

1. **Treat GO's TC xrefs (and `go.py`) as sources, then curate propagation
   per entry.** An xref is a lead, not a licence to annotate: decide explicitly
   whether every protein at that TC level truly has the GO function before
   propagating. Record the verdict (`exactMatch` = propagate, `narrowMatch` =
   subfamily-only) as in [`tc2go.sssom.yaml`](TCDB/tc2go.sssom.yaml).
2. **Propagation is safe at the level that is mono-specific.** A 5-level TC system
   is usually mono-specific (`2.A.22.1.1` SERT → `GO:0005335`) → propagate; a
   3-level family is usually poly-specific (`1.A.8` MIP mixes water channels and
   glycerol-permeable aquaglyceroporins; `2.A.22` NSS mixes serotonin/dopamine/GABA)
   → do **not** propagate the substrate-specific term to the whole family.
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
| Propose a `tc2go` **propagation pipeline** to GO | The strategic deliverable: the 80 evidence-JUSTIFIED leads (mostly 5-level systems) are a ready `external2go` starter set; package them (plus reviewed extensions) so a protein's TC number yields a GAF annotation. |
| Promote the 62 GAP_CANDIDATE leads | Specific systems whose reviewed member carries only a parent term — run them through the gene-review workflow to add the specific GO term. |
| Chase the 10 NO_REVIEWED_MEMBER cases | Reviewed protein exists but lacks the `DR TCDB` xref (e.g. MelB) — a UniProt cross-reference gap to report upstream. |
| Extend GO's 63 xref'd families | Promote the 110 novel `go.py`-generated families (and the 16 GO-xref families `go.py` misses) toward curated term-xrefs. |

## Project Status

- **Started**: 2026-07-18
- **Maturity**: SCOPING — GO's neglected TC term-xrefs extracted (194 leads) and
  **every one scored for propagation against UniProt evidence** (80 JUSTIFIED / 23
  narrow / 62 gap-candidate / 12 class-level / 17 other); the missing piece identified as the *annotation
  pipeline*, not the mapping; TCDB's `go.py` dump characterised as a noisy second
  candidate pool; the structural reverse gap quantified; four SSSOM sets built and
  validated.
- **Computed live** (2026-07-18): GO curates **202 TC references on 170
  non-obsolete MF terms / 63 families** (`go-basic.obo`); no `tc2go` in
  `external2go` (GO release `2026-05-19`); `go.py` = 34,497 rows → 4,943 TC
  systems / 589 families / 3,518 GO terms, of which 13% rows / 12% terms are
  transporter-activity MF; reverse gap 4,431 / 8,758 (50.6%) reviewed TCDB entries
  with no transport MF term (16,344 all-UniProtKB TCDB xrefs); 353 local gene
  folders carry a TCDB xref; **173 / 2,235 TCDB families (8%) mapped across all
  three sources**.
- **Reproducible scripts**: [`TCDB/extract_go_tc_xrefs.py`](TCDB/extract_go_tc_xrefs.py)
  (GO's own TC xrefs → SSSOM), [`TCDB/curate_propagation.py`](TCDB/curate_propagation.py)
  (propagation verdicts from UniProt evidence),
  [`TCDB/tcdb_go_probe.py`](TCDB/tcdb_go_probe.py) (dump characterisation + reverse
  gap), [`TCDB/build_tc2go.py`](TCDB/build_tc2go.py) (generated SSSOM).
- **Mapping sets** (all pass `just validate-tcdb-mappings`):
  [`tc2go.from_go.sssom.yaml`](TCDB/tc2go.from_go.sssom.yaml) — 194 GO-xref source
  leads; [`tc2go.propagation.sssom.yaml`](TCDB/tc2go.propagation.sssom.yaml) — the
  same 194 scored for propagation (80 JUSTIFIED / 23 narrow / 62 gap-candidate / 12
  class-level / 17 other);
  [`tc2go.generated.sssom.yaml`](TCDB/tc2go.generated.sssom.yaml) — 477
  machine-derived candidate rows; [`tc2go.sssom.yaml`](TCDB/tc2go.sssom.yaml) — 8
  hand-backed exemplars.
- **Current conclusion**: GO *does* reference TCDB — 170 molecular-function terms
  carry TC xrefs — but these are neglected, unreviewed *sources*: they cover only
  3% of TCDB families and, lacking an `external2go` pipeline, are never propagated
  to proteins, leaving half of reviewed TC-classified transporters with no
  transport MF term. The high-value deliverable is a **`tc2go` pipeline built on
  per-entry propagation curation** (which TC level safely inherits which GO term),
  seeded by GO's xrefs plus reviewed extensions.
