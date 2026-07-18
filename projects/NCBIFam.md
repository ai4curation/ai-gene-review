---
title: "NCBIFAM / CDD → GO Contribution & Gap Project"
maturity: SCOPING
tags: [PIPELINE]
---

# NCBIFAM / CDD → GO Contribution & Gap Project

## The value question, answered first: yes — and here are the mappings

**Are there `ncbifam2go` mappings (existing NCBI-assigned, or new/refined here) that
would add high-value annotations we do *not* already get from the InterPro rollup?
Yes.** "Not from the rollup" has a precise meaning here, because NCBIFAM reaches GOA
*only* through `interpro2go`: an added annotation is genuinely **net-new** when an
entry already carries the NCBIFAM signature but the term never propagated — the
family is unintegrated into InterPro, or its InterPro entry has no `interpro2go` row.
That net-new count is exactly the closure-aware `gain` measured live by
[`ncbifam_go_gain.py`](NCBIFam/ncbifam_go_gain.py) (an entry counts as gaining the
term only if it lacks the term **and every descendant**). The highest-value cases,
straight from the [validated seed](NCBIFam/ncbifam2go.sssom.yaml):

| NCBIFAM family | Proposed GO (→ `ncbifam2go`) | Net-new (all) | reviewed† | Kind | Why it's unique / high-value |
|---|---|---:|---:|---|---|
| NF033545 IS630 transposase | GO:0004803 transposase activity | **18,874** | 2 ~ | adopt NCBI | Mobile elements — InterPro integration lags most here; single biggest gap |
| TIGR03542 LL-DAP aminotransferase | GO:0010285 LL-DAP transaminase | **1,185** | 2→**0** ✗ | **refine** | Large *bacterial* TrEMBL gap is real; but both reviewed "gaps" are plant ALD1 paralogs (see †) |
| NF041162 encapsulin shell protein | GO:0140737 encapsulin nanocompartment | **897** | 0 | adopt NCBI | CC term; new microbial-compartment biology, essentially no propagation |
| TIGR00417 spermidine synthase | GO:0004766 spermidine synthase | **575** | 1→**0** ✗ | **refine** | NCBI gave near-root GO:0003824 (gain ~0); specific term reveals 575; the 1 reviewed "gap" is tobacco PMT paralog (see †) |
| NF006559 dihydroorotase | GO:0004151 dihydroorotase activity | **491** | 0 | **refine** | NCBI gave broad GO:0016810; specific child (EC 3.5.2.3) unmasks 491 |
| NF002326 dGTPase | GO:0008832 dGTPase activity | **456** | 13 ⚠ | **refine** | NCBI gave broad GO:0016793; but all 13 reviewed are cautiously-named "dGTPase-*like*" (see †) |
| TIGR02791 VirB5 (T4SS) | GO:0043684 type IV secretion system complex | **298** | 4 ✅ | adopt (broad) | 0/298 carry it; **the one clean reviewed gap-fill** — all 4 are *Brucella* VirB5 |
| NF042963 anti-phage DUF1156 | GO:0051607 defense response to virus | **151** | 0 | adopt NCBI | Anti-phage family; BP term is coarse (see ‡) but mechanism now resolved to a DNA amino-MTase → gains a real MF (see ‡‡) |

**† Verification of the reviewed (Swiss-Prot) gains (2026-07-18).** The *reviewed*
column is the curation-relevant one, so each nonzero value was checked by pulling the
actual Swiss-Prot entries that lack the term (`ncbifam_go_gain.py` counts reproduced
live; entries inspected via the UniProtKB REST API). **The check materially changes
the reviewed story — only VirB5 survives as a clean gap-fill:**

| Row | reviewed gain (all UniProtKB) | …restricted to prokaryotes | What the entries actually are |
|---|---:|---:|---|
| VirB5 → GO:0043684 | 4 | 4 | ✅ Genuine — all 4 are *Brucella* VirB5, real T4SS subunits |
| dGTPase → GO:0008832 | 13 | 13 | ⚠️ All 13 are "dGTPase-**like** protein", **no EC assigned** — curators deliberately withheld the specific activity; propagating GO:0008832 asserts a substrate they declined (the FtsX over-annotation pattern, within Bacteria) |
| IS630 → GO:0004803 | 2 | 2 | ~ Both are "**uncharacterized**" IS630-element ORFs (Shigella, Sinorhizobium) — plausibly the transposase, but left uncharacterized; weak |
| LL-DAP → GO:0010285 | 2 | **0** | ✗ Both are **plant ALD1** (Arabidopsis Q9ZQI7, rice Q6VMN7); Q9ZQI7 carries *L-lysine α-aminotransferase* (GO:0062045, pipecolate/defense), **not** DapL — cross-kingdom paralog trap |
| spermidine synthase → GO:0004766 | 1 | **0** | ✗ Tobacco **PMT1** (Q42963), neofunctionalized to *putrescine N-methyltransferase* (GO:0030750) — paralog trap |

Two lessons fall out. **(1) Scope the gain to the model's lineage.** NCBI's PGAP
NF/TIGR models are only applied to prokaryotic genomes, yet UniProt runs the HMMs
cross-kingdom; querying all of UniProtKB inflates the *reviewed* gain with eukaryotic
paralogs PGAP would never touch. Restricting to Bacteria+Archaea collapses the LL-DAP
and spermidine reviewed gaps to **0** — the bacterial reviewed enzymes already carry
the term; only diverged plant paralogs were missing it. **(2) "-like" is a curator
caution flag.** Even in-scope, the dGTPase "gap" is a clade the curators declined to
give the specific activity. So the honest reviewed tally among these eight is: **1
clean (VirB5), 1 over-annotation-risk (dGTPase), 1 weak (IS630), 2 spurious (LL-DAP,
spermidine).** The **all-UniProtKB (bacterial TrEMBL) gains remain real** — this only
corrects the small *reviewed* number, which was the fragile part of the claim.

**‡ "defense response to virus" is coarse — and no better GO term exists yet.** The
user's instinct is right: NF042963 is *phage-specific*, and GO:0051607 (defense
response to virus) does not say so. But GO has **no** `defense response to
bacteriophage` term — the only `defense response to X` children are virus, bacterium,
symbiont, protozoan, insect, nematode, oomycetes, fungus, parasitic plant (QuickGO,
2026-07-18). So GO:0051607 is the least-wrong *existing* BP term (a phage is a virus),
and the right BP deliverable is a **`proposed_new_terms` entry** for a phage-specific
child (`defense response to bacteriophage`, is_a GO:0051607), not a confident
`ncbifam2go` exactMatch. This is a BP row whose value is entirely in bacterial TrEMBL
(0 reviewed), so it does not carry the "high-value reviewed" claim regardless.

**‡‡ The mechanism is no longer unknown — and it hands the family a real MF.** We
ran the DUF1156 family through **OpenScientist** as a blinded, structure-scoped
hypothesis job (representative A0A3B7MFS0, *Thermosynechococcus*, 1002 aa; prompt gave
only the Gao-2020 phage phenotype + sequence). Its structural analysis and our own
holdout **agree**: NF042963 is, at its core, an intact **site-specific SAM-dependent
DNA amino-methyltransferase** (Class I motif I FxGxG + catalytic **DPPY** motif IV,
converging in one Rossmann SAM pocket in the AlphaFold model), with **no nuclease**
anywhere in the chain; the DUF1156 module and C-terminal extension are **accessory**
(target-recognition / scaffolding). The defense mechanism is therefore **modification-
based self/non-self discrimination in the BREX/DISARM/restriction–modification mould**
— host DNA is self-marked by methylation, unmethylated phage DNA is excluded, and any
effector step is supplied *in trans*. This upgrades the row from "DUF of unknown
function" to a family with a concrete **molecular function**: `GO:0009008
DNA-methyltransferase activity` (safe parent; amino-MTase confirmed, m5C excluded).
The **specific target base is UNDECIDED** — OpenScientist confidently called
N4-cytosine (`GO:0015667`, EC 2.1.1.113) from Foldseek, but the fold cannot
distinguish amino-MTase subtypes, and the **family-wide annotation favors N6-adenine**
(`GO:0009007`, EC 2.1.1.72; 19/151 members named adenine-specific, 0 cytosine),
matching our holdout — so we hold the base open pending LC-MS/MS. This MF goes
**beyond** NCBI's BP-only `go_terms` for the family, so it is a *proposed enrichment*
(a `proposed_new_terms` MF), not part of the adopt/refine seed. Full write-up and
blinded comparison:
[`NF042963-hypotheses/duf1156_antiphage_mechanism/`](NCBIFam/NF042963-hypotheses/duf1156_antiphage_mechanism/COMPARISON.md).
It also illustrates an OpenScientist failure mode worth remembering: **a confident
single-representative Foldseek call (m4C) over-specified past what the fold can
resolve** — caught only by the family-wide sequence/annotation check.

**The honest caveat that frames all of the above:** the *bulk* of the gain is in
unreviewed **TrEMBL**, not Swiss-Prot — which is exactly what we should expect and is
fine. Over a 60-model `equivalog` sample the totals are **Σ 19 reviewed vs 26,578
all-UniProtKB** — the opposite emphasis from RHEA, because NCBIFAM is prokaryote-heavy
and Swiss-Prot's curated prokaryotic enzymes usually already carry the term. The value
is real and large, but it is mostly *automated-annotation depth*; the curation-ready
(reviewed) additions are a small, high-quality minority — and, as † shows, must be
inspected per-entry and taxonomically scoped before being trusted.

**Two things this table also demonstrates about *how* to build `ncbifam2go`:**

- **"Refine" > "adopt" for altitude.** Five of these top rows are cases where NCBI's
  own `go_terms` gave only a broad parent (up to the near-root GO:0003824); because
  the gain query is closure-aware, the broad term shows **~0 gain** and looks
  worthless, while the specific EC-bridged child we propose reveals hundreds of
  net-new annotations. *Proposing our own specific term is what converts these from
  invisible to high-value.*
- **High gain is a flag, not an instruction.** The mirror case, **FtsX (TIGR00439)**,
  is deliberately **excluded from the high-value list**: mapping to the most specific
  `GO:0043093 FtsZ-dependent cytokinesis` would show a 3,304 "gain", but curators
  apply it to only 2/7 reviewed FtsX, so blanket propagation is **over-annotation**.
  The seed maps FtsX to the safe consensus `GO:0051301 cell division` (gain 22). Every
  candidate needs this altitude check before it counts as value.

**Scale beyond the hand-picked eight.** The same EC-bridge standard, run over the
whole collection ([`ncbifam2go_candidates.py`](NCBIFam/ncbifam2go_candidates.py)),
yields **2,455 models (2,503 rows)** where NCBI's `go_terms` and GO's `ec2go`
independently agree — an automatable, ready-to-add `ncbifam2go` core (AMR-rich:
β-lactamases, trimethoprim-resistant DHFRs, aminoglycoside acetyltransferases), plus
**843 "refine"** models where `ec2go` supplies a specific term over NCBI's broad one.

**A second, different sense of "unique."** Separately, NCBIFAM is the **sole**
integrated signature behind **250** of this repo's existing `interpro2go`
annotations — including mainstream genes **GAPDH, RPS3, ATP6V1A, HMGCS2**. Those *do*
come through the rollup today, but they exist **only because** an NCBIFAM/TIGRFAM
model is the integrating signature; remove NCBIFAM and those GOA rows disappear. That
is an attribution/robustness argument (detailed [below](#un-masking-member-db-attribution-on-this-repos-annotations)),
distinct from the net-new gap-fills in the table above.

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
- **NCBIFAM/CDD are masked by InterPro in GOA — and the contribution is now
  measured.** A `GO_REF:0000002` row's `WITH/FROM` names the integrated
  `InterPro:IPRnnnnnn` entry, **never** the member signature (0 `TIGR…/NF…/cd…` ids
  in any `*-goa.tsv` `WITH/FROM`, vs 1,160 `DR NCBIfam` + 2,174 `DR CDD` in the
  proteins' UniProt records). Re-joining each annotation to its InterPro entry's
  member databases shows **NCBIFAM backs 705 (13%) and CDD 469 (8%)** of the repo's
  5,549 InterPro2GO rows, and is the **sole** integrated signature for **250 / 116**
  — invisible in GOA (the [attribution section](#un-masking-member-db-attribution-on-this-repos-annotations)).
  This is the NCBIFAM/CDD analog of RHEA being "masked by EC".
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

## Un-masking: member-DB attribution on this repo's annotations

The masking claim is now **measured**, not just asserted. Every `GO_REF:0000002`
annotation in this repo's `genes/**/*-goa.tsv` was re-joined to its InterPro entry's
`member_databases` via the InterPro API
([`interpro_member_attribution.py`](NCBIFam/interpro_member_attribution.py),
resumable). Across **5,549** resolved InterPro-citation rows (1,827 distinct entries):

| Member DB | distinct entries | annotation rows | sole signature |
|-----------|----------------:|----------------:|---------------:|
| pfam | 708 (39%) | 2,374 (43%) | — |
| panther | 459 (25%) | 1,082 (19%) | — |
| **ncbifam** | **272 (15%)** | **705 (13%)** | **250** |
| prints / profile / smart | ~190 each | ~820 each | — |
| **cdd** | **183 (10%)** | **469 (8%)** | **116** |
| hamap / pirsf / ssf / cathgene3d | 117–159 | 403–627 | — |

**NCBIFAM contributes a signature to 705 (13%) and CDD to 469 (8%)** of the repo's
InterPro2GO annotations — a contribution **entirely invisible in GOA**, which shows
only the `InterPro:IPR…` id. Stronger still, **NCBIFAM is the *sole* integrated
signature for 250 rows and CDD for 116** — annotations that exist *purely* because of
an NCBIFAM/CDD model, with no other member DB in the entry. And these are not exotic:
NCBIFAM-sole entries back annotations on **GAPDH** (`IPR006424`→`GO:0006006`), **RPS3**
(`IPR005703`→`GO:0006412`), **ATP6V1A** (`IPR005725`→`GO:0016887`), and **HMGCS2**
(`IPR010122`→`GO:0008299`) — mainstream genes whose InterPro2GO term traces solely to a
TIGRFAM/NCBIFAM signature. This is the quantitative form of the masking finding, and
the join the sibling [InterPro Mapping Review](INTERPRO.md) project needs to attribute
each interpro2go term to the member DB that earned it.

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
[`ncbifam2go.sssom.yaml`](NCBIFam/ncbifam2go.sssom.yaml) records the NCBIFAM-family →
GO mapping **we propose for ingestion** — *not* a transcription of NCBI's
`hmm_PGAP.tsv go_terms`. Each is backed by the model's `family_type`,
`product_name`, EC, and PMIDs, plus the live UniProtKB propagation gain. A
**28-mapping seed** spanning all three GO aspects (MF, BP, CC — NCBIFAM is a
whole-protein family resource, not enzyme-only) is in place, with predicate classes
parallel to RHEA:

- **`skos:exactMatch`** (26 rows) — the GO term *is* the family's function; a
  ready-to-add `ncbifam2go` row. The enzyme majority are **EC-bridge supported**
  (verified live: `ec2go(EC)` = this GO term, e.g. formamidase EC
  3.5.1.49→`GO:0004328`, β-lactamase EC 3.5.2.6→`GO:0008800`, uridine kinase EC
  2.7.1.48→`GO:0004849`). Spans AMR (two distinct β-lactamase families → one GO
  term, the family→GO many-to-one analog of RHEA's reactions→activity), central
  metabolism, phosphonate/arsenate/cobalamin pathways, plus the highest-gap case
  IS630 transposase → `GO:0004803` (18,874 entries missing it), an encapsulin-shell
  CC term, and an anti-phage defense BP term. **Five of these rows propose our own
  *specific* term to replace an NCBI value that was too broad** (see below).
- **`skos:broadMatch`** (1 row) — reserved for the case where **no more-specific GO
  term exists to adopt**: VirB5 → `type IV secretion system complex` (a subunit
  `part_of` the whole complex, no VirB5-specific CC term).

**We suggest our own term where NCBI's was too broad — and that unmasks the real
gain.** For five families NCBI's `go_terms` gave only a broad parent — twice the
ontology **near-root** `GO:0003824 catalytic activity` (enoyl-CoA hydratase NF005804,
spermidine synthase TIGR00417) — even though a precise, EC-bridged child already
exists. Rather than record the useless broad term, the seed proposes the specific
child as an `exactMatch` (dGTPase→`GO:0008832`, enoyl-CoA hydratase→`GO:0004300`,
dihydroorotase→`GO:0004151`, spermidine synthase→`GO:0004766`, LL-DAP
aminotransferase→`GO:0010285`). This is not cosmetic: the broad parent is
near-universal so its propagation gain looks **~0**, but the **specific term reveals
large gaps the parent masked** — spermidine synthase **575**, LL-DAP aminotransferase
**1,185**, dihydroorotase **491**, and dGTPase **456 (incl. 13 reviewed/Swiss-Prot)**
entries missing the precise activity. Proposing our own term is what turns these from
invisible into actionable gap-fills.

**…but more specific is not always right — the FtsX cell-division case.** The
mirror-image judgement is `TIGR00439` (permease-like cell division protein **FtsX**),
where chasing specificity would be **over-annotation**. NCBI assigned `GO:0000910
cytokinesis`; the ontology shows cytokinesis is `part_of` `GO:0051301 cell division`
(so NCBI's term is actually the *narrower* one — an earlier draft of this seed had
that backwards). Empirically, **all 7 reviewed FtsX proteins carry `GO:0051301 cell
division`** but only 2/7 carry cytokinesis or the most specific `GO:0043093
FtsZ-dependent cytokinesis`. FtsX/FtsEX *regulates* septal peptidoglycan hydrolysis
and divisome assembly, so curators annotate the safe participation term, not the
constriction act. The gain numbers make the trap explicit: mapping to `GO:0051301`
gains only **22** (it is already near-universal — a confirmatory mapping), whereas
mapping to `GO:0043093` would show a **3,304** apparent gap — but propagating
*FtsZ-dependent cytokinesis* to every FtsX would assert more than the family supports.
We therefore propose the curator-consensus `GO:0051301 cell division` as the
`exactMatch` and **decline** the higher-gain specific term. Specificity is the goal
only up to the altitude the evidence supports.

**Verification matters and catches real errors.** One scoping-sample NCBIFAM
`go_terms` value (`GO:0009448` on a GABA transaminase) is **obsolete**; a
diacylglycerol-kinase model (NF009874, EC 2.7.1.107) is tagged with the **wrong**
activity `GO:0003951 NAD+ kinase activity` (the correct `GO:0004143` exists); and
several assignments sit at near-root altitude. The obsolete and wrong ids were
**excluded**; the broad ones were **replaced by our own specific term** (above) — so
the seed drops obsolete/incorrect ids, prefers specific children, and
EC-bridge-confirms enzymes. Every GO id/label was checked non-obsolete
against QuickGO (2026-06-20); every family id/name/type/EC is from `hmm_PGAP.tsv`;
every EC→GO bridge against the live `ec2go`. Validate
with **`just validate-ncbifam-mappings`** — SSSOM structural validation plus GO
term/label validation (object bound to the **full** GO graph, MF+BP+CC; generated
nested view [`ncbifam2go.terms.yaml`](NCBIFam/ncbifam2go.terms.yaml)). The seed
**passes** validation.

A `cdd2go` set is **not** planned: per the [CDD section](#does-cdd-have-its-own-go-mappings-no-for-cdd-proper),
CDD-proper has no native GO, and the GO surfaced through CDD belongs to NCBIFAM
(captured here) or Pfam (InterPro-routed) — a `cdd2go` would be largely redundant.

## Scaling the seed to the whole collection (EC-bridge candidates)

The 28-row seed is hand-reviewed; the **EC bridge** lets us scale the *same evidence
standard* to the whole collection with no per-row human judgement, because the
agreement of two independent curated resources (NCBI's `go_terms` and GO's `ec2go`)
*is* the verification. [`ncbifam2go_candidates.py`](NCBIFam/ncbifam2go_candidates.py)
walks every NCBIFAM model and emits each `(model, GO)` where `ec2go(model's EC)`
confirms one of the model's own NCBI `go_terms`. The live funnel:

| Stage | Count |
|-------|------:|
| GO-bearing NCBIFAM models | 11,228 |
| …with both an EC and a GO term | 3,782 |
| …where `ec2go(EC)` **confirms** a model GO → **exactMatch candidates** | **2,455** (2,503 rows) |
| …where `ec2go(EC)` would **refine** NCBI's broader/absent GO (the spermidine-synthase pattern, at scale) | 843 |
| …candidates already in the reviewed seed (cross-check) | 17 |

The generated set is [`ncbifam2go.candidates.tsv`](NCBIFam/ncbifam2go.candidates.tsv)
(2,503 rows, clearly marked generated; `mapping_justification` would be
`semapv:CompositeMatching`). The **17** rows that coincide with the reviewed seed are
exactly the seed's EC-bridge enzyme rows — an automatic confirmation that the
generator agrees with manual curation where they overlap. These 2,455 are
AMR-rich (trimethoprim-resistant dihydrofolate reductases → `GO:0004146`,
β-lactamases → `GO:0008800`, aminoglycoside 6′-N-acetyltransferases → `GO:0047663`,
…) and are the natural ready-to-add core of a real `ncbifam2go`. The **843
"refine"** models are the scaled version of the five hand-fixed altitude rows: NCBIFAM
gave a broad/near-root term but `ec2go` supplies the specific child — a second,
also-automatable candidate class (propose `ec2go`'s term), pending the same
altitude/over-annotation check the FtsX case shows is still needed.

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
records. The **member-DB attribution** (which member DB backs each `GO_REF:0000002`
row in the repo) is computed live by
[`interpro_member_attribution.py`](NCBIFam/interpro_member_attribution.py) against the
InterPro API (resumable, cached). The forward closure-filtered cross-organism
contribution table reuses the [UniPathway](UNIPATHWAY.md)/[RHEA](RHEA.md) uniqueness
query and is **staged** pending the go-db DuckDBs (absent in the web container). Full
queries and caveats: [NCBIFAM-METHODOLOGY.md](NCBIFam/NCBIFAM-METHODOLOGY.md).

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
| ✅ GOA × InterPro member-integration re-join | **Done** ([attribution section](#un-masking-member-db-attribution-on-this-repos-annotations)): NCBIFAM backs 13% / CDD 8% of the repo's InterPro2GO rows (sole signature for 250 / 116). |
| Forward closure-filtered cross-organism scan | UniPathway-style uniqueness for member-attributed rows; needs go-db DuckDBs. Now seeded by the member-attribution join above. |
| Promote the 2,455 EC-bridge candidates | Altitude/obsolete-check [`ncbifam2go.candidates.tsv`](NCBIFam/ncbifam2go.candidates.tsv) and fold the clean rows into the reviewed SSSOM → a near-complete ingestible `ncbifam2go`. |
| Build the 843 "refine" class | Auto-propose `ec2go`'s specific term where NCBI's `go_terms` is broad/absent (the spermidine-synthase pattern), then altitude-review as FtsX shows is needed. |
| Non-EC families (defense/secretion/transport) | The high-gain non-enzyme equivalogs (transposases, anti-phage, T4SS, encapsulins) have no EC bridge → need a different verification (literature/SPARCLE), curated like the seed's CC/BP rows. |
| Full-collection gain run | Replace the 60-model gain sample with the complete equivalog set for a definitive reviewed-vs-TrEMBL gain figure. |
| Exemplar gene reviews | Pick 2–3 genes whose only MF/BP support is an NCBIFAM equivalog (e.g. an anti-phage or secretion family) and run the full review workflow. |

## Project Status

- **Started**: 2026-06-20
- **Maturity**: SCOPING — pipeline identified, masking demonstrated on the repo
  gene set, NCBIFAM GO/EC source and the integration coverage gap characterised
  live, CDD-own-GO question resolved, annotation gain measured, a **validated
  28-row `ncbifam2go` seed** in place, a **2,455-model EC-bridge candidate set**
  generated at collection scale, and the **member-DB attribution re-join done** on the
  repo's annotations.
- **Computed live** (via [`NCBIFam/ncbifam_cdd_probe.py`](NCBIFam/ncbifam_cdd_probe.py)
  and [`ncbifam_go_gain.py`](NCBIFam/ncbifam_go_gain.py)):
  `interpro2go` = 30,200 rows / 14,799 InterPro ids (GO `2026-04-28`); NCBIFAM PGAP
  = 34,351 models, 11,228 (33%) with GO, 6,417 (19%) with EC, 13,253 equivalogs;
  InterPro integration NCBIFAM 7,447/18,511 (40%), CDD 5,059/19,902 (25%); CDD-proper
  carries 0 native GO (FTP + Entrez); 60-model gain Σ = 19 reviewed / 26,578
  all-UniProtKB; member-DB attribution = NCBIFAM backs 705 (13%) / CDD 469 (8%) of
  5,549 repo InterPro2GO rows (sole signature 250 / 116); masking verified from this
  repo's `*-goa.tsv` / `*-uniprot.txt`.
- **Curated mappings**: [`NCBIFam/ncbifam2go.sssom.yaml`](NCBIFam/ncbifam2go.sssom.yaml)
  — 28 verified SSSOM rows (27 exactMatch ready-to-add, incl. 5 proposing our own
  specific term over NCBI's broad one and 1 — FtsX — declining a too-specific term;
  1 broadMatch, VirB5, where no specific term exists), spanning MF/BP/CC, each with
  live propagation gain; **passes** `just validate-ncbifam-mappings`.
- **Scaled candidates**: [`NCBIFam/ncbifam2go.candidates.tsv`](NCBIFam/ncbifam2go.candidates.tsv)
  — 2,503 generated EC-bridge-confirmed rows (2,455 models; `ncbifam2go_candidates.py`),
  AMR-rich; 17 coincide with the reviewed seed as a cross-check, plus 843 "refine" models
  where `ec2go` supplies a specific term over NCBI's broad one.
- **Current conclusion**: NCBIFAM/CDD reach GO only through InterPro, which
  **masks** their contribution in GOA and leaves the **majority of signatures
  unintegrated**. CDD-proper has **no native GO** (it is NCBIFAM, bundled inside
  CDD, that carries it). The highest-value work is (a) re-attributing
  `GO_REF:0000002` rows to the firing member DB, and (b) ingesting NCBIFAM's own
  curated `equivalog` GO via the `ncbifam2go` SSSOM mapping (seeded here) — the
  RHEA pattern applied to a family resource; the gain is large but TrEMBL-weighted,
  concentrated in mobile-element/defense/secretion biology.
