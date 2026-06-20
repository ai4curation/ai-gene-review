---
title: "NCBIFAM / CDD → GO Contribution & Gap Project"
maturity: SCOPING
tags: [PIPELINE]
---

# NCBIFAM / CDD → GO Contribution & Gap Project

## Overview

This project audits the **NCBI protein-family resources — NCBIFAM (the
PGAP/TIGRFAM HMM collection) and CDD (Conserved Domain Database) — as sources of
GO annotations**, in the same spirit as the [RHEA](RHEA.md), [SPKW](SPKW.md), and
[UniPathway](UNIPATHWAY.md) source-audit projects, and develops the missing
**`ncbifam2go` / `cdd2go` mappings** the way RHEA develops `rhea2go` gap-fills.

The structural fact that organises everything: **NCBIFAM and CDD are InterPro
*member databases*, so they reach GOA through exactly one pipeline** — InterPro
integration → `interpro2go` → `GO_REF:0000002` (evidence `IEA`,
`assigned_by=InterPro`). There is **no public `ncbifam2go` or `cdd2go`**
external2go file (verified: both 403 on `current.geneontology.org`; only
`interpro2go` is served). So like RHEA, the analysis runs in **two directions**:

1. **Contribution (forward).** Where is a `GO_REF:0000002` annotation actually
   carried by an *NCBIFAM/CDD* signature (versus Pfam, PROSITE, etc.), and is that
   contribution useful or over-/mis-propagated? — the SPKW-style audit, here
   complicated by InterPro **masking** the member DB.
2. **Gaps (reverse).** Where does NCBIFAM/CDD assert a function — an NCBI-curated
   GO/EC term, or a precise equivalog family name — that **never reaches GO**,
   either because the signature is *unintegrated* into InterPro or because the
   integrated InterPro entry has no `interpro2go` row? These are gap-filling
   opportunities, not over-annotations.

See [NCBIFAM-METHODOLOGY.md](NCBIFam/NCBIFAM-METHODOLOGY.md) for the queries, the
reproducible probe ([`ncbifam_cdd_probe.py`](NCBIFam/ncbifam_cdd_probe.py)), and
the masking/closure caveats.

## Key Findings (scoping pass)

- **One route in, and a dedicated mapping file is missing.** NCBIFAM/CDD GO
  reaches GOA *only* via `interpro2go` / `GO_REF:0000002`; there is no
  `ncbifam2go` or `cdd2go` (403). `interpro2go` is sizeable — **30,200 mapping
  rows over 14,799 distinct InterPro entries** (GO release `2026-04-28`) — but a
  member signature contributes GO only if it is *integrated* into one of those
  entries.
- **NCBIFAM/CDD are masked by InterPro in GOA.** A `GO_REF:0000002` row's
  `WITH/FROM` names the integrated `InterPro:IPRnnnnnn` entry, **never** the
  member signature. Verified on this repo's gene set: **0** `TIGR…/NF…/cd…`
  signatures appear in any `*-goa.tsv` `WITH/FROM`, yet the same proteins'
  UniProt records carry **1,160 `DR NCBIfam`** and **2,174 `DR CDD`** lines. This
  is the NCBIFAM/CDD analog of RHEA being "masked by EC".
- **NCBIFAM carries its own NCBI-curated GO/EC that GO does not ingest.** The PGAP
  HMM metadata (`hmm_PGAP.tsv`, **34,351 models**) assigns function directly:
  **11,228 models (33%) carry GO terms** (3,622 distinct GO ids) and **6,417
  (19%) carry EC numbers**. None of this propagates except where the model is
  integrated into InterPro — a large, curated, unused mapping source.
- **`equivalog` makes the gap-fill tractable.** **13,253 NCBIFAM models are typed
  `equivalog`** (all members share one function → safe GO/EC transfer), the direct
  analog of RHEA's reviewed enzymes backing each curated mapping. `domain` /
  `subfamily` models (10,974 / 4,564) need altitude care.
- **The coverage gap is large — most signatures are unintegrated.** Computed live
  from the InterPro API: **NCBIFAM 7,447 / 18,511 integrated (40%); CDD 5,059 /
  19,902 integrated (25%)**. The **11,064 unintegrated NCBIFAM** and **14,843
  unintegrated CDD** signatures contribute **zero** GO by construction — the
  NCBIFAM/CDD analog of RHEA's "no `rhea2go` line" reactions.

## NCBIFAM/CDD is mostly masked by InterPro

UniProt enzymes and families almost always carry **multiple** member signatures
(an NCBIFAM equivalog *and* a Pfam domain *and* a CDD model …), all collapsed into
one or a few InterPro entries. So an NCBIFAM/CDD signature's "real"
`GO_REF:0000002` contribution is only the slice where it is the integrating /
distinguishing signature for the InterPro entry, and where no other member DB
already supplies the same term. Two consequences:

- **Attribution requires re-joining GOA to InterPro member integration** (API
  `entry/integrated/{db}/`); GOA alone cannot tell you which member DB fired.
- The interesting NCBIFAM cases are the **equivalog**-grounded ones, where the
  member model is *more* specific/curated than the Pfam-style domain it shares an
  InterPro entry with — the place NCBIFAM resolves a function the broader members
  lump (mirroring RHEA resolving a cofactor split EC hides).

## Specificity and quality cut by family_type

NCBIFAM's `family_type` is a built-in altitude/quality signal absent from CDD:

| family_type | N | Function-transfer safety |
|-------------|---:|--------------------------|
| `equivalog` | 13,253 | **High** — all members one function; GO/EC transfer safe |
| `domain` | 10,974 | Low — domain, not whole-protein function |
| `subfamily` | 4,564 | Medium — clade-specific; check altitude |
| `PfamEq` / `PfamAutoEq` | 1,807 / 1,204 | Equivalent to a Pfam entry → likely already InterPro-covered |
| `exception` / `hypoth_equivalog` | 1,341 / 434 | Curated caveat / hypothetical — review individually |

CDD models, by contrast, are domain/architecture-oriented and lack this typing,
so CDD's forward contribution skews toward **broad domain** terms (the
`protein binding` / generic-domain altitude problem) and its reverse gap is
harder to curate than NCBIFAM's.

## Gaps Found (scoping)

| # | Gap | Size | What it is |
|---|-----|------|-----------|
| G1 | InterPro masking | all `GO_REF:0000002` rows | GOA hides which member DB fired → member contribution unattributable without re-join |
| G2 | NCBIFAM unintegrated | 11,064 / 18,511 (60%) | NCBIFAM signatures not in InterPro → contribute no GO |
| G3 | CDD unintegrated | 14,843 / 19,902 (75%) | CDD signatures not in InterPro → contribute no GO |
| G4 | NCBI-curated GO not ingested | 11,228 models w/ GO | NCBIFAM models carry NCBI GO that GO has no `ncbifam2go` to ingest |
| G5 | NCBI-curated EC not ingested | 6,417 models w/ EC | Could seed EC2GO-bridged GO mappings (the RHEA EC-bridge pattern) |
| G6 | Integrated-but-unmapped InterPro entries | staged | NCBIFAM/CDD integrated into an IPR entry that has no `interpro2go` row |

G4/G5 are the high-value half: an `equivalog` with a clean NCBI `go_terms` /
`ec_numbers` value is a ready-to-curate mapping; an `ec_numbers`-only equivalog
can be bridged through `ec2go` exactly as RHEA bridges reactions through
`rhea2ec`/`ec2go`.

## Curated new mappings (SSSOM) — planned

The curation deliverable mirrors RHEA's [`rhea2go.sssom.yaml`](RHEA/rhea2go.sssom.yaml):
an **`ncbifam2go.sssom.yaml`** (and, if warranted, `cdd2go`) recording
NCBIFAM-signature → GO mappings that are absent from the GOA route, each backed
by the NCBIFAM model's `family_type`, `product_name`, and NCBI `go_terms`/`pmids`.
Planned predicate classes parallel RHEA:

- **`skos:exactMatch`** — the NCBI-assigned GO term *is* the model's function
  (prioritise `equivalog`; EC-bridge supported where `ec2go(EC)` = the GO term).
- **`skos:broadMatch`** — only a broader class term exists; flag the narrower GO
  term to request.
- **`sssom:NoTermFound`** — equivalog with a precise function name but no GO MF/BP
  term at all → `proposed_new_terms` candidate.

Each GO id/label to be verified non-obsolete against QuickGO/OLS, every NCBIFAM id
+ name from `hmm_PGAP.tsv`, validated with a `just validate-ncbifam-mappings`
target analogous to `just validate-rhea-mappings`.

## Methods

The `interpro2go` characterisation, InterPro member-integration counts, and the
NCBIFAM PGAP GO/EC coverage are **computed live** by
[`ncbifam_cdd_probe.py`](NCBIFam/ncbifam_cdd_probe.py) (stdlib only; no go-db, no
auth). The masking evidence (0 member signatures in `WITH/FROM`; 1,160 NCBIfam +
2,174 CDD `DR` lines) is computed from this repo's `genes/**/*-goa.tsv` and
`*-uniprot.txt`. The forward closure-filtered cross-organism contribution table
reuses the [UniPathway](UNIPATHWAY.md)/[RHEA](RHEA.md) uniqueness query and is
**staged** pending the go-db DuckDBs (absent in the web container). Full queries
and caveats: [NCBIFAM-METHODOLOGY.md](NCBIFam/NCBIFAM-METHODOLOGY.md).

## How this differs from RHEA, SPKW, and UniPathway

| | SPKW (`GO_REF:0000043`) | RHEA (`GO_REF:0000116`) | **NCBIFAM/CDD (`GO_REF:0000002`)** |
|---|---|---|---|
| GO aspect | mostly BP | MF (enzyme activity) | **MF + BP + CC** (family/domain models) |
| Provenance in GOA | direct (keyword visible) | direct (`assigned_by=RHEA`) | **masked** — only the integrated `InterPro:IPR…` shows |
| Dedicated `*2go` file | yes | yes | **no** (`ncbifam2go`/`cdd2go` do not exist) |
| Dominant failure mode | process conflation | parent/child altitude; wrong substrate | **domain-altitude (CDD); unintegrated coverage gap** |
| Built-in quality signal | none | reaction precision | **NCBIFAM `family_type` (`equivalog`)** |
| Curation emphasis | over-annotation removal | gap-filling | **both, but attribution-first** then equivalog gap-fill |

NCBIFAM is unusual among these sources in carrying its **own curated GO/EC** that
GO does not ingest, so — like RHEA — the expected verdict skew is toward
**`NEW` / gap-filling** (for `equivalog` models) on the reverse side, with the
forward side dominated by the **attribution/masking** problem rather than outright
over-annotation.

## Curation Recommendations (preliminary)

1. **Attribute before auditing.** A `GO_REF:0000002` annotation cannot be praised
   or blamed on NCBIFAM/CDD until GOA is re-joined to InterPro member integration;
   build that join first.
2. **Mine NCBIFAM `equivalog` GO/EC as a mapping source.** The 13,253 equivalogs
   with NCBI `go_terms`/`ec_numbers` are the cleanest gap-fill substrate — start
   the `ncbifam2go.sssom.yaml` here.
3. **EC-bridge where only EC is given.** An equivalog with `ec_numbers` but no
   `go_terms` can be mapped through `ec2go`, the RHEA EC-bridge pattern.
4. **Treat CDD as domain-altitude-risky.** Without `family_type`, CDD's forward
   contribution skews broad; prefer the specific child the curated entry supports.
5. **Unintegrated signatures with a real function are `proposed_new_terms` /
   InterPro-integration requests**, not silent gaps.

## Follow-Up Targets

| Target | Rationale |
|--------|-----------|
| GOA × InterPro member-integration re-join | Attribute each `GO_REF:0000002` row to its firing member DB; quantify NCBIFAM/CDD's *actual* forward contribution. |
| Forward closure-filtered cross-organism scan | UniPathway-style uniqueness for member-attributed rows; needs go-db DuckDBs. |
| `ncbifam2go.sssom.yaml` seed | Curate exactMatch/broadMatch/NoTermFound mappings from equivalog GO/EC, backed by `family_type` + PMIDs. |
| Integrated-but-unmapped IPR set | NCBIFAM/CDD integrated into an InterPro entry lacking an `interpro2go` row → InterPro mapping requests. |
| Exemplar gene reviews | Pick 2–3 genes whose only MF/BP support is an NCBIFAM equivalog and run the full review workflow. |

## Project Status

- **Started**: 2026-06-20
- **Maturity**: SCOPING — pipeline identified, masking demonstrated on the repo
  gene set, NCBIFAM GO/EC source and the integration coverage gap characterised
  live; member-attribution re-join and the SSSOM mapping seed are staged.
- **Computed live** (via [`NCBIFam/ncbifam_cdd_probe.py`](NCBIFam/ncbifam_cdd_probe.py)):
  `interpro2go` = 30,200 rows / 14,799 InterPro ids (GO `2026-04-28`); NCBIFAM PGAP
  = 34,351 models, 11,228 (33%) with GO, 6,417 (19%) with EC, 13,253 equivalogs;
  InterPro integration NCBIFAM 7,447/18,511 (40%), CDD 5,059/19,902 (25%);
  masking verified from this repo's `*-goa.tsv` / `*-uniprot.txt`.
- **Current conclusion**: NCBIFAM/CDD reach GO only through InterPro, which
  **masks** their contribution in GOA and leaves the **majority of signatures
  unintegrated**. The highest-value work is (a) re-attributing `GO_REF:0000002`
  rows to the firing member DB, and (b) ingesting NCBIFAM's own curated
  `equivalog` GO/EC via a new `ncbifam2go` SSSOM mapping — the RHEA pattern
  applied to a family/domain source.
