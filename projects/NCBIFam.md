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
- **CDD-proper has *no* native GO of its own; NCBIFAM does.** Checked directly
  (see [CDD section](#does-cdd-have-its-own-go-mappings-no-for-cdd-proper)): the
  NCBI-curated `cd…` models — what InterPro calls the "cdd" member DB — carry **no
  GO** in any bulk file (`cddannot*.dat`, `cddid_all.tbl` → 0 GO) or in the NCBI
  Entrez `cdd` record (no GO field). Where the broad CDD *search* database appears
  to "have GO", that GO is **borrowed** from the non-`cd` models CDD bundles —
  chiefly the **13,669 NCBIFAM models (PRK 7,039 + TIGR 4,488 + NF 2,142)** inside
  CDD, plus Pfam/COG — not CDD-curated. So the GO-bearing source is **NCBIFAM**;
  CDD-proper reaches GO **only** via InterPro.
- **Ingesting NCBIFAM GO would gain mostly TrEMBL, modestly Swiss-Prot.** A live
  UniProtKB propagation probe (closure-aware; see
  [NCBIFAM-ANNOTATION-GAIN.md](NCBIFam/NCBIFAM-ANNOTATION-GAIN.md)) over a 60-model
  `equivalog` sample finds **Σ gain = 19 reviewed (Swiss-Prot) vs 26,578
  all-UniProtKB** — the opposite emphasis from RHEA (whose gain was reviewed-heavy),
  because NCBIFAM is prokaryote-heavy and curated entries already carry the term.
  The gap concentrates in **mobile elements (IS630 transposase: 18,874 entries
  missing the term), conjugation/secretion (VirB5 T4SS, conjugative ATPases),
  CRISPR/anti-phage defense, sporulation, encapsulins, and cell division (FtsX)** —
  the newer microbial biology where InterPro integration lags.

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

## Does CDD have its own GO mappings? No — for CDD-proper

It is worth pinning down, because the CDD *search* database superficially looks
like it carries GO. The answer separates two things CDD conflates:

- **CDD-proper (the NCBI-curated `cd…` models)** — the 21,955 `cd` models, which
  is exactly what InterPro ingests as its "cdd" member database — **has no native
  GO.** Verified three ways: (1) the NCBI bulk annotation files carry only residue
  features, not GO — `cddannot.dat` / `cddannot_generic.dat` contain **0** `GO:`
  lines, and `cddid_all.tbl` has none; (2) the NCBI Entrez `cdd` record for a `cd`
  model (e.g. `cd00009 AAA`) exposes an abstract, PSSM, and site descriptions but
  **no GO field**; (3) GO serves **no `cdd2go`** file (`HTTP 403`). So CDD-proper
  reaches GO **only** through InterPro integration → `interpro2go`.
- **The CDD *search* database is a superset** of **74,122** models drawn from many
  sources (`cd` 21,955 · `pfam` 19,637 · `PRK` 7,039 · `COG` 5,137 · `KOG` 4,825 ·
  `TIGR` 4,488 · `NF` 2,142 · …). Where a CDD hit *does* come with GO, that GO is
  **borrowed from the source resource** — overwhelmingly the **13,669 NCBIFAM
  models (PRK + TIGR + NF) bundled inside CDD**, whose GO is the
  `hmm_PGAP.tsv go_terms` we mine here, plus Pfam/COG (themselves InterPro-routed).

**Conclusion:** the GO-bearing NCBI family resource is **NCBIFAM**, not CDD. CDD
"has GO" only as a search aggregator surfacing NCBIFAM/Pfam GO under `cd`/`PRK`/
`TIGR` accessions. This is why the curated mapping deliverable targets
**`ncbifam2go`**, and a `cdd2go` would be largely redundant with it (and with
Pfam→InterPro). Reproduce with `ncbifam_cdd_probe.py` and the FTP/Entrez checks in
[NCBIFAM-METHODOLOGY.md](NCBIFam/NCBIFAM-METHODOLOGY.md).

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

## Curated new mappings (SSSOM)

The curation deliverable mirrors RHEA's [`rhea2go.sssom.yaml`](RHEA/rhea2go.sssom.yaml):
[`ncbifam2go.sssom.yaml`](NCBIFam/ncbifam2go.sssom.yaml) records NCBIFAM-family →
GO mappings adopting NCBI's own `hmm_PGAP.tsv go_terms` **after independent
verification**, each backed by the model's `family_type`, `product_name`, EC, and
PMIDs, plus the live UniProtKB propagation gain. A **10-mapping seed** spanning all
three GO aspects (MF, BP, CC — NCBIFAM is a whole-protein family resource, not
enzyme-only) is in place, with predicate classes parallel to RHEA:

- **`skos:exactMatch`** (7 rows) — the NCBI-assigned GO term *is* the family's
  function; ready-to-add `ncbifam2go` rows. Enzyme rows are **EC-bridge supported**
  (verified: `ec2go(EC)` = this GO term for formamidase EC 3.5.1.49→`GO:0004328`,
  AHL lactonase EC 3.1.1.81→`GO:0102007`, lipoprotein lipase EC 3.1.1.34→`GO:0004465`).
  Includes the highest-gap case, IS630 transposase → `GO:0004803` (18,874 entries
  missing it), an encapsulin shell CC term, and an anti-phage defense BP term.
- **`skos:broadMatch`** (3 rows) — NCBI assigned a broader parent; the comment
  names the narrower term to use/request (dGTPase NF002326 → `GO:0016793`, use
  `GO:0008832 dGTPase activity`; VirB5 → the whole `type IV secretion system
  complex`; FtsX → broad `cytokinesis`, prefer a bacterial cell-division child).

**Verification matters:** one scoping-sample NCBIFAM `go_terms` value
(`GO:0009448` on a GABA transaminase) is **obsolete**, and several are
altitude-broad — so the seed drops obsolete ids, prefers specific children, and
EC-bridge-confirms enzymes. Every GO id/label was checked non-obsolete against
QuickGO (2026-06-20); every family id/name/type/EC is from `hmm_PGAP.tsv`. Validate
with **`just validate-ncbifam-mappings`** — SSSOM structural validation plus GO
term/label validation (object bound to the **full** GO graph, MF+BP+CC; generated
nested view [`ncbifam2go.terms.yaml`](NCBIFam/ncbifam2go.terms.yaml)). The seed
**passes** validation.

A `cdd2go` set is **not** planned: per the [CDD section](#does-cdd-have-its-own-go-mappings-no-for-cdd-proper),
CDD-proper has no native GO, and the GO surfaced through CDD belongs to NCBIFAM
(captured here) or Pfam (InterPro-routed) — a `cdd2go` would be largely redundant.

## Methods

The `interpro2go` characterisation, InterPro member-integration counts, and the
NCBIFAM PGAP GO/EC coverage are **computed live** by
[`ncbifam_cdd_probe.py`](NCBIFam/ncbifam_cdd_probe.py) (stdlib only; no go-db, no
auth). The masking evidence (0 member signatures in `WITH/FROM`; 1,160 NCBIfam +
2,174 CDD `DR` lines) is computed from this repo's `genes/**/*-goa.tsv` and
`*-uniprot.txt`. The **annotation-gain** numbers are computed live against the
UniProtKB REST API by [`ncbifam_go_gain.py`](NCBIFam/ncbifam_go_gain.py)
(closure-aware `go:` query; see
[NCBIFAM-ANNOTATION-GAIN.md](NCBIFam/NCBIFAM-ANNOTATION-GAIN.md)). The CDD-own-GO
check uses the NCBI CDD FTP (`cddannot*.dat`, `cddid_all.tbl`) and Entrez `cdd`
records. The forward closure-filtered cross-organism contribution table reuses the
[UniPathway](UNIPATHWAY.md)/[RHEA](RHEA.md) uniqueness query and is **staged**
pending the go-db DuckDBs (absent in the web container). Full queries and caveats:
[NCBIFAM-METHODOLOGY.md](NCBIFam/NCBIFAM-METHODOLOGY.md).

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
| Scale up `ncbifam2go.sssom.yaml` | Extend the 10-row verified seed across the 13,253 equivalogs (obsolete-filter, child-prefer, EC-bridge) → a full ingestible mapping. |
| Full-collection gain run | Replace the 60-model gain sample with the complete equivalog set for a definitive reviewed-vs-TrEMBL gain figure. |
| Integrated-but-unmapped IPR set | NCBIFAM/CDD integrated into an InterPro entry lacking an `interpro2go` row → InterPro mapping requests. |
| Exemplar gene reviews | Pick 2–3 genes whose only MF/BP support is an NCBIFAM equivalog (e.g. an anti-phage or secretion family) and run the full review workflow. |

## Project Status

- **Started**: 2026-06-20
- **Maturity**: SCOPING — pipeline identified, masking demonstrated on the repo
  gene set, NCBIFAM GO/EC source and the integration coverage gap characterised
  live, CDD-own-GO question resolved, annotation gain measured, and a **validated
  10-row `ncbifam2go` seed** in place; member-attribution re-join and full-scale
  mapping are staged.
- **Computed live** (via [`NCBIFam/ncbifam_cdd_probe.py`](NCBIFam/ncbifam_cdd_probe.py)
  and [`ncbifam_go_gain.py`](NCBIFam/ncbifam_go_gain.py)):
  `interpro2go` = 30,200 rows / 14,799 InterPro ids (GO `2026-04-28`); NCBIFAM PGAP
  = 34,351 models, 11,228 (33%) with GO, 6,417 (19%) with EC, 13,253 equivalogs;
  InterPro integration NCBIFAM 7,447/18,511 (40%), CDD 5,059/19,902 (25%); CDD-proper
  carries 0 native GO (FTP + Entrez); 60-model gain Σ = 19 reviewed / 26,578
  all-UniProtKB; masking verified from this repo's `*-goa.tsv` / `*-uniprot.txt`.
- **Curated mappings**: [`NCBIFam/ncbifam2go.sssom.yaml`](NCBIFam/ncbifam2go.sssom.yaml)
  — 10 verified SSSOM rows (7 exactMatch ready-to-add, 3 broadMatch), spanning MF/BP/CC,
  each with live propagation gain; **passes** `just validate-ncbifam-mappings`.
- **Current conclusion**: NCBIFAM/CDD reach GO only through InterPro, which
  **masks** their contribution in GOA and leaves the **majority of signatures
  unintegrated**. CDD-proper has **no native GO** (it is NCBIFAM, bundled inside
  CDD, that carries it). The highest-value work is (a) re-attributing
  `GO_REF:0000002` rows to the firing member DB, and (b) ingesting NCBIFAM's own
  curated `equivalog` GO via the `ncbifam2go` SSSOM mapping (seeded here) — the
  RHEA pattern applied to a family resource; the gain is large but TrEMBL-weighted,
  concentrated in mobile-element/defense/secretion biology.
