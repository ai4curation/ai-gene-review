---
title: "RHEA → GO Contribution & Gap Project"
maturity: SCOPING
tags: [PIPELINE]
---

# RHEA → GO Contribution & Gap Project

## Overview

This project examines the **RHEA reaction database as a source of GO molecular-
function annotations**, in the same spirit as the [SPKW](SPKW.md) (UniProt
keywords) and [UniPathway](UNIPATHWAY.md) source-audit projects. RHEA reaches GO
through the public **`rhea2go`** mapping; in GOA these annotations appear as
`GO_REF:0000116`, `assigned_by=RHEA`, aspect `molecular_function`, evidence
`IEA`. `GO_REF:0000116` is the RHEA counterpart of SPKW's `GO_REF:0000043` and
EC2GO's `GO_REF:0000003`.

Unlike SPKW and UniPathway, RHEA is a **molecular-function** source (enzymatic
reactions), so the analysis runs in **two complementary directions**:

1. **Contribution (forward).** Where is `GO_REF:0000116` the *unique*
   (closure-filtered) source of an enzyme-activity annotation, and are those
   contributions useful or over-/mis-propagated? — the SPKW-style audit.
2. **Gaps (reverse).** Where does a UniProtKB entry carry a catalytic activity
   with a RHEA cross-reference, but the GO molecular-function term that
   `rhea2go` maps that reaction to **never propagates into GOA**? These are
   annotations that "fall through the cracks" — curation *gap-filling*
   opportunities rather than over-annotations.

See [RHEA-METHODOLOGY.md](RHEA/RHEA-METHODOLOGY.md) for the queries, the
reproducible probe script, and the all-important closure caveat. The deeper
**EC-masking and specificity** analysis lives in
[RHEA-EC-SPECIFICITY.md](RHEA/RHEA-EC-SPECIFICITY.md).

## Key Findings (scoping pass)

- **RHEA is largely masked by EC.** 84% of RHEA's GO terms are also reachable
  via EC2GO, and 88% of EC-carrying reactions map to the *same* GO term EC2GO
  already supplies — so most `GO_REF:0000116` volume is redundant and RHEA's
  unique value is a small set of pockets (see below). This is the concrete form
  of "contributions may be masked by EC".
- **`GO_REF:0000116` is the RHEA→GO pipeline reference.** Confirmed directly
  from GOA rows in this repo's gene set: every `GO_REF:0000116` row is
  `assigned_by=RHEA`, aspect `molecular_function`, evidence `IEA`. This is the
  handle for the forward (contribution) audit.
- **The `rhea2go` mapping is sizeable and many-to-one.** The current mapping
  (GO release `2026-05-19`) contains **7,746 RHEA→GO rows** covering **7,746
  distinct RHEA reactions** that collapse onto **4,744 distinct GO molecular-
  function terms** (~1.6 reactions per GO term). So multiple distinct reactions
  routinely share one generic activity term — which is exactly where the
  altitude/specificity problems live.
- **The reverse "gap" signal is real and large for some reactions.** A live
  exact-match probe of reviewed UniProtKB entries (see pilot table) finds
  reactions where a high fraction of entries carrying the RHEA do **not** carry
  the mapped GO term — up to ~99% for `RHEA:21248 → GO:0034062 (5'-3' RNA
  polymerase activity)` and ~40% for `RHEA:10596 → GO:0004713 (protein
  tyrosine kinase activity)`.
- **…but the gap headline must be closure-filtered.** Many "missing" entries
  carry a *more specific child* term instead of the generic mapped term (e.g.
  receptor-tyrosine-kinase children rather than the bare
  `protein tyrosine kinase activity`). The exact-match percentages are an
  **upper bound**; the true gap requires the same ontology-closure filtering the
  SPKW/UniPathway projects use. High-gap reactions are **candidates for
  closure-aware review**, not confirmed gaps.
- **Some reactions have no GO term at all** (e.g. `RHEA:46608` has no `rhea2go`
  line). These cannot propagate by construction and are candidates for
  `proposed_new_terms`.

## RHEA is mostly masked by EC

UniProt enzymes almost always carry **both** an EC number and a RHEA reaction,
and EC also reaches GO — via `ec2go` (`GO_REF:0000003`). So RHEA's `GO_REF:0000116`
contribution is only "real" where EC2GO did not already supply the same term.
Computed live from `rhea2go`, `ec2go`, and the RHEA REST API
([`rhea_ec_specificity.py`](RHEA/rhea_ec_specificity.py)):

- **84%** of RHEA's GO terms (3,972 / 4,744) are **also reachable via EC2GO**;
  only **772** GO terms are RHEA-only.
- At the reaction level, of the 4,904 reactions carrying both a `rhea2go` term
  and an EC, **88% (4,324) map to the exact same GO term EC2GO already gives** —
  fully masked; only **118** differ, and **462** have an EC with no `ec2go` term
  (RHEA as sole route).

So most `GO_REF:0000116` volume is redundant with EC2GO and would be dropped by
the closure-filtered uniqueness query. RHEA's genuine value is the **772
RHEA-only terms**, the **462 EC-without-ec2go** reactions, the **118
differing-term** reactions, and the reverse-propagation gap below.

## Specificity cuts both ways

- **EC → RHEA → GO:** one EC number spans many RHEA reactions. Of 435 ECs that
  map to >1 reaction, **323 (74%) collapse to a single GO term** (GO can't tell
  the reactions apart) but **112 (26%) spread across multiple GO terms** — RHEA
  here resolves a distinction the bare EC lumps. Cleanest case: **EC:1.1.1.256 →
  `GO:0004090 carbonyl reductase (NADPH)` + `GO:0004022 alcohol dehydrogenase
  (NAD+)`** — a cofactor split EC hides but RHEA→GO preserves.
- **RHEA → GO:** the more common direction is specificity *loss* — **679 GO terms
  absorb >1 reaction**, up to **67 distinct ADH reactions → one
  `alcohol dehydrogenase (NAD+) activity` term**, because GO lacks
  substrate-specific MF children. RHEA→GO is a specificity *bottleneck* that
  occasionally *rescues* a cofactor/substrate split.

Full tables and examples: [RHEA-EC-SPECIFICITY.md](RHEA/RHEA-EC-SPECIFICITY.md).

## Reverse-Gap Pilot (live, exact-match)

Reviewed-only UniProtKB entries carrying each reaction, and how many lack the
`rhea2go`-mapped GO molecular-function term. Generated with
[`rhea_go_gap_probe.py`](RHEA/rhea_go_gap_probe.py) (`--gap-sample`).
**`pct_missing` is an exact-match upper bound** — see the closure caveat below.

| RHEA | Mapped GO MF term | N reviewed | N missing (exact) | % missing | Note |
|------|-------------------|-----------:|------------------:|----------:|------|
| RHEA:21248 | GO:0034062 5'-3' RNA polymerase activity | ≥500 | 497 | ~99% | capped at 500; striking — generic parent rarely used directly |
| RHEA:10596 | GO:0004713 protein tyrosine kinase activity | ≥500 | 198 | ~40% | capped at 500; many entries carry specific RTK children |
| RHEA:13065 | GO:0016887 ATP hydrolysis activity | ≥500 | 33 | ~7% | capped at 500 |
| RHEA:15421 | GO:0004467 long-chain fatty acid-CoA ligase activity | 90 | 2 | ~2% | clean propagation |
| RHEA:16505 | GO:0008813 chorismate lyase activity | 148 | 0 | 0% | clean propagation |
| RHEA:11628 | GO:0004737 pyruvate decarboxylase activity | 33 | 0 | 0% | clean propagation |
| RHEA:22636 | GO:0047840 dCTP diphosphatase activity | 49 | 0 | 0% | clean propagation |
| RHEA:46608 | *(no rhea2go mapping)* | — | — | — | "no GO term" gap class → candidate new term |

**Reading the pilot.** The clean 0–2% reactions show the pipeline works well for
specific, single-product enzyme activities. The high-gap reactions
(`RHEA:21248`, `RHEA:10596`) are exactly the **generic-parent** reactions where
`rhea2go` points at a broad activity term that curated entries express via more
specific children — so most of that 40–99% is expected closure coverage, not a
genuine missing annotation. The job of the closure-filtered follow-up is to
separate the residual *true* gaps (entries with neither the parent nor any
child) from this expected altitude difference.

## Mapping Gaps Found

| # | Gap | Size | What it is |
|---|-----|------|-----------|
| G1 | EC-masking redundancy | 4,324 reactions (88%) | RHEA's GO term duplicates one EC2GO already supplies → low marginal value |
| G2 | RHEA-only GO terms | 772 terms | Reachable via `rhea2go` but not `ec2go` — RHEA's unique forward contribution |
| G3 | EC-without-`ec2go` | 462 reactions | EC has no `ec2go` line → RHEA is the only EC-adjacent GO route |
| G4 | No-`rhea2go` enzymatic reactions | **2,731 / 7,635 (36%)** | Genuine enzymatic reaction with no GO MF target (2,445 EC-level; 286 specific-reaction-only) |
| G5 | Specificity-collapse | 679 terms, up to 67:1 | GO lacks substrate-specific MF children → many reactions flatten to one term |
| G6 | Reverse-propagation gap | pilot below | UniProt RHEA annotations whose mapped GO term never reaches GOA |

**Worked case reviews** of this gap on real Swiss-Prot enzymes — where a RHEA
reaction has no `rhea2go` mapping and the GO molecular function is missing or
only a class root — are in [RHEA-GAP-CASES.md](RHEA/RHEA-GAP-CASES.md): **PHYKPL**
(MF = only `lyase activity`; propose new term), **B3GALNT2** (class-level
GalNAc-T; propose new term; dystroglycanopathy gene), **SAMD8/SMSr** (the
existing term `GO:0002950 ceramide phosphoethanolamine synthase activity` is
simply not applied — pure propagation gap), and **SULT6B1** (only
`sulfotransferase activity`; cautious fill given by-similarity evidence). Cases
selected reproducibly by [`rhea_gap_finder.py`](RHEA/rhea_gap_finder.py).

G1/G4 are mirror images: where EC and RHEA agree RHEA is redundant; where RHEA
has no GO term EC usually still carries the protein at coarser EC granularity —
so most gaps are **specificity** gaps (right activity, coarse GO representation),
not **coverage** gaps (no MF term at all). G2/G3/G6 are where RHEA genuinely adds
something EC does not. Detail and reproduction in
[RHEA-EC-SPECIFICITY.md](RHEA/RHEA-EC-SPECIFICITY.md).

## Curated new mappings (SSSOM)

Filling the gaps is a curation deliverable, not just an audit. The curated
RHEA→GO mappings — reactions absent from `rhea2go` but with (or needing) a GO MF
term — are recorded in [`rhea2go.sssom.yaml`](RHEA/rhea2go.sssom.yaml), the same
**SSSOM YAML** format used by the [ANTIMICROBIAL_RESISTANCE](ANTIMICROBIAL_RESISTANCE.md)
`aro2go` mapping set. **132 mappings** so far, each backed by a review of a reviewed
(Swiss-Prot) enzyme that carries the reaction
([RHEA-MAPPING-REVIEWS.md](RHEA/RHEA-MAPPING-REVIEWS.md)). The predicate encodes
the specificity finding:

- **`skos:exactMatch`** (111 rows) — the GO term *is* the reaction's activity;
  ready-to-add `rhea2go` entries. Most are **EC-bridge supported**: `ec2go` maps
  the reaction's EC to this exact GO term and `rhea2ec` maps the reaction to that
  EC. Backed by enzymes such as biotinidase (BTD, biotinidase deficiency), TPMT
  (thiopurine pharmacogenomics), VKORC1L1 (warfarin), PYCR1, phosphoserine
  aminotransferase (serC), mRNA-capping enzyme (RNGTT), and SAMD8/SMSr.
- **`skos:broadMatch`** (4 rows) — only a broader class term exists; the comment
  names the narrower GO term to request (PHYKPL→`lyase activity`; B3GALNT2→
  `acetylgalactosaminyltransferase activity`; SULT6B1→`aryl sulfotransferase
  activity`; DPEP2→`dipeptidase activity`).
- **`sssom:NoTermFound`** (17 rows) — **new GO term suggestions**: reactions where
  QuickGO returns no specific MF term at all (hppE fosfomycin epoxidase; a
  trimethylaminoethylphosphonate dioxygenase; cellobionic-acid phosphorylase;
  1,4-β-mannosyl-GlcNAc phosphorylase) — GO new-term-request candidates.

Every GO id/label is verified non-obsolete against QuickGO; every RHEA id +
equation comes from the UniProt catalytic-activity line; every backing enzyme is
reviewed (mostly PE1, with catalytic-activity PMIDs). Validate with
`just validate-rhea-mappings` — SSSOM structural validation plus GO term/label
validation (GO objects bound to the molecular-function branch; generated nested
view [`rhea2go.terms.yaml`](RHEA/rhea2go.terms.yaml)).

**Propagation gain.** If these mappings were added to `rhea2go`, they would
add **42 new GO molecular-function annotations to Swiss-Prot (reviewed)** entries — the
curation-relevant gain we track — filling real reviewed-entry gaps; the all-UniProtKB figure
(~25,842, mostly automated TrEMBL) is secondary because curated enzymes already carry the term,
because reviewed enzymes carrying the reaction already have the term (the
EC-masking result at the annotation level). See
[RHEA-ANNOTATION-GAIN.md](RHEA/RHEA-ANNOTATION-GAIN.md)
([`rhea_annotation_gain.py`](RHEA/rhea_annotation_gain.py)).

## Methods

`GO_REF:0000116` identification and the `rhea2go` mapping statistics were
computed live (GO release `2026-05-19`). The reverse-gap pilot was computed live
against the UniProtKB REST API (`rhea:<id>` query field, `reviewed:true`).

The **forward contribution** audit reuses the closure-filtered uniqueness query
from [UniPathway](UNIPATHWAY.md)/[SPKW](SPKW/SPKW-METHODOLOGY.md), swapping the
reference id to `GO_REF:0000116`. That cross-organism scan needs the local
`~/repos/go-db/db/*.ddb` DuckDBs, which are **not present in the web container**,
so the UNIPATHWAY-style contribution table is **staged, not yet populated** (see
Follow-Up Targets). The reverse-gap probe needs no go-db and runs anywhere with
network access.

Full queries, the probe script, and the mandatory closure caveat are in
[RHEA-METHODOLOGY.md](RHEA/RHEA-METHODOLOGY.md).

## How this differs from SPKW and UniPathway

| | SPKW (`GO_REF:0000043`) | UniPathway (`GO_REF:0000041`) | **RHEA (`GO_REF:0000116`)** |
|---|---|---|---|
| GO aspect | mostly BP (+ some MF/CC) | mostly BP (pathways) | **MF (enzyme activity)** |
| Dominant failure mode | process conflation / "expression ≠ function" | broad pathway-bucket propagation | **parent-vs-child altitude; wrong-substrate paralog** |
| Direction of interest | over-annotation (remove/modify) | mostly contribution audit | **both**: contribution *and* reverse gap-filling |
| Source status | retired by GOA (~Apr 2026) for cellular organisms | archived/legacy vocabulary | **active, curated, reaction-grounded** |

The RHEA source is *better* grounded than SPKW (a reaction is a precise
biochemical claim), so the expected verdict skew is toward `ACCEPT` /
`KEEP_AS_NON_CORE` on the forward side and toward **`NEW` / gap-filling** on the
reverse side — the opposite emphasis from the SPKW over-annotation hunt.

## Curation Recommendations (preliminary)

1. **Treat the gap direction as the high-value half.** Unlike SPKW, RHEA's main
   contribution is finding *correct enzyme activities that GO is missing*, not
   removing over-annotations. Prioritise reactions with a high closure-filtered
   gap.
2. **Always closure-filter before calling a gap.** Exact-match gap percentages
   are upper bounds; subtract entries carrying any descendant of the mapped term
   (the SPKW/UniPathway closure pattern) before proposing additions.
3. **Generic-parent reactions deserve altitude review.** Where `rhea2go` maps a
   reaction to a broad activity term (e.g. `protein tyrosine kinase activity`),
   prefer the specific child the curated entry already supports; the parent is
   often redundant.
4. **Reactions with no `rhea2go` line are `proposed_new_terms` candidates** — a
   real UniProt-annotated activity with no GO MF target to land on.
5. **Forward-unique RHEA rows are usually keepers.** A closure-unique
   `GO_REF:0000116` activity term is a precise biochemical assertion; the review
   risk is wrong-substrate/wrong-paralog specificity, not process conflation.

## Follow-Up Targets

| Target | Rationale |
|--------|-----------|
| Forward closure-filtered cross-organism scan (`GO_REF:0000116`) | The UNIPATHWAY-style contribution table; needs go-db DuckDBs. Quantifies where RHEA is the *unique* MF source. |
| Closure-aware reverse gap on the high-gap pilot reactions | Separate true gaps from expected parent/child altitude for `RHEA:21248`, `RHEA:10596`; promote real gaps to gene reviews. |
| "No `rhea2go` mapping" reaction set | Enumerate UniProt-used RHEA reactions with no GO MF target → batch `proposed_new_terms`. |
| RHEA directional-quartet join audit | Test whether master-vs-directional id mismatch causes systematic non-propagation. |
| Exemplar gene reviews | Pick 2–3 confirmed (closure-filtered) gap genes and run the full review workflow, mirroring the UniPathway exemplar pattern. |

## Project Status

- **Started**: 2026-06-20
- **Maturity**: SCOPING — pipeline identified, mapping characterised, reverse-gap
  probe working with live pilot results; forward cross-organism scan staged
  pending go-db access.
- **Computed live**: `GO_REF:0000116` identification (assigned_by=RHEA, MF, IEA);
  `rhea2go` = 7,746 reactions → 4,744 GO terms (GO release 2026-05-19);
  EC-masking + specificity (84% RHEA terms shared with EC2GO; 88% reaction-level
  masking; 772 RHEA-only terms; 36% no-GO enzymatic-reaction gap) via
  `rhea2go`/`ec2go`/RHEA REST; 8-reaction reverse-gap pilot via UniProt REST.
- **Reproducible scripts**: [`RHEA/rhea_go_gap_probe.py`](RHEA/rhea_go_gap_probe.py)
  (reverse gap), [`RHEA/rhea_ec_specificity.py`](RHEA/rhea_ec_specificity.py)
  (EC-masking, specificity, gaps), [`RHEA/rhea_gap_finder.py`](RHEA/rhea_gap_finder.py)
  (gap case selection)
- **Curated mappings**: [`RHEA/rhea2go.sssom.yaml`](RHEA/rhea2go.sssom.yaml) — 132
  SSSOM rows (111 exactMatch ready-to-add, 4 broadMatch, 17 new-term suggestions),
  each backed by a reviewed enzyme in
  [`RHEA/RHEA-MAPPING-REVIEWS.md`](RHEA/RHEA-MAPPING-REVIEWS.md);
  `just validate-rhea-mappings`
- **Current conclusion**: RHEA is an active, reaction-grounded MF source whose
  most valuable contribution to this project is the **reverse direction** —
  surfacing UniProt-annotated enzyme activities that never propagate to GO — once
  exact-match gaps are corrected by ontology-closure filtering.
