# Reusing glycoscience resources for GO curation — strategy

Decision record for the [Glycobiology project](../GLYCOBIOLOGY.md): how to reuse the external
glycoscience resources catalogued in [GLYCOBIOLOGY-resources.md](GLYCOBIOLOGY-resources.md) as
inputs to GO curation, rather than just describing them.

## Framing

Most glycoscience resources reach GO only **indirectly** today (via UniProt / EC / InterPro /
Reactome). There is no official `cazy2go` or `glyconnect2go`. So "reuse via mappings" means **the
mapping is the deliverable** — but the repo already has the exact machinery for this: curated
**SSSOM** mapping sets validated with `linkml-term-validator`, exactly as for
[RHEA](../RHEA.md) (`rhea2go`), [InterPro](../INTERPRO.md) (`interpro2go`), and NCBIFam.

## Modes of reuse — decisions

| Mode | Decision | Notes |
|------|----------|-------|
| **Forward propagation — `cazy2go` family→GO MF** | **DO** | Same EC-masking situation as RHEA. The "risk" of producing over-general terms is **not a risk** — redundant rows are trivially **closure-filtered** against `ec2go`/`interpro2go` (drop terms those already supply); what remains is the genuine contribution. |
| **Ontology alignment — GlycoCoO / GlycoEnzOnto → GO (SSSOM)** | **DO (cheap one-shot)** | [GlycoEnzOnto](https://academic.oup.com/bioinformatics/article/38/24/5413/6772808) appears **abandoned**, but that doesn't matter: a one-shot SSSOM alignment salvages its glyco-enzyme MF terms into GO space at low cost. |
| **Confirmatory cross-check (GlyGen join)** | **DO** | UniProt → CAZy family + GlyConnect enzyme record → compare to the gene's GO MF. Read-only QC; catches the wrong-paralog / over-general errors the 7 exemplar reviews fixed. |
| **GO-CAM / pathway modelling** | **PUNT (for now)** | Glycan biosynthesis is a natural causal/multi-enzyme model, but deferred — not in current scope. |

## `cazy2go`: the forward-propagation source

A CAZy **family** → GO **molecular-function** mapping, the glyco analogue of `interpro2go`. Seeded in
[`cazy2go.sssom.yaml`](cazy2go.sssom.yaml) from the project's five exemplar GT families, each row
backed by a completed gene review:

| CAZy family | GO MF | Predicate | Why |
|-------------|-------|-----------|-----|
| GT13 (GnT-I) | GO:0003827 | exactMatch | mono-specific family (EC 2.4.1.101) |
| GT65 (POFUT1) | GO:0046922 | exactMatch | animal GT65 = POFUT1 (EC 2.4.1.221) |
| GT29 (sialyl-Ts) | GO:0008373 | exactMatch | family scope == the `sialyltransferase activity` class |
| GT7 (β4Gal/GalNAc-Ts) | GO:0003831 | narrowMatch | term fits B4GALT-type members only → needs subfamily |
| GT31 (β3Gal/GalNAc/Fringe) | GO:0008376 | narrowMatch | highly heterogeneous family → needs subfamily |

**Predicate semantics** (mirrors `interpro2go.sssom.yaml`): `exactMatch` = holds for ~all (animal)
family members → ready to propagate; `narrowMatch` = the GO term describes a **subfamily** only, so
the family is too coarse and subfamily/EC resolution is required first.

### The trivial redundancy filter

For each row, the family's EC(s) usually already reach the same GO term via `ec2go`
(`GO_REF:0000003`) or an InterPro entry reaches it via `interpro2go` (`GO_REF:0000002`). Those rows
are **redundant** (no marginal annotation) and are dropped by a closure filter — the same
EC-masking computation [RHEA](../RHEA.md) already runs (`ec2go` is fetchable from
`current.geneontology.org/ontology/external2go/ec2go`). The genuine `cazy2go` contribution is the
**non-redundant remainder**: families with no EC, no `ec2go` row, or no InterPro coverage. Redundancy
status is noted per row in the seed; computing it live across all families is the scale-up step.

### Beyond the seed — the generated full mapping

The 5-family hand-curated seed is now extended to **all CAZy enzyme families derivable from public
data**, reproducibly, by [`build_cazy2go.py`](build_cazy2go.py) →
[`cazy2go.generated.sssom.yaml`](cazy2go.generated.sssom.yaml). No row is hand-typed: each is the
live join

```
CAZy family --(reviewed Swiss-Prot CAZy↔EC xref, UniProt REST)--> EC --(ec2go)--> GO MF
```

Current build (2026-06): **3,183 reviewed UniProtKB CAZy+EC entries → 302 families → 702 mapping
rows over 283 families** (19 families carry an EC with no `ec2go` term — gap candidates). The same
exact/narrow logic as the seed is applied automatically:

| | families | meaning |
|--|---------:|---------|
| `exactMatch` | **162** | family's ECs resolve to a single GO MF → mono-specific, ready to propagate |
| `narrowMatch` | **121** | poly-specific family; GO term applies to a subfamily → resolve subfamily/EC first |

The **trivial redundancy filter** is built in: 80 generic-parent rows (`glycosyltransferase
activity`, `hexosyltransferase activity`, `hydrolase acting on glycosyl bonds`, …) were dropped where
the family also resolved to a specific child — so the output already prefers the specific term. The
generated rows are cross-consistent with the hand-curated seed (e.g. GT13→GO:0003827,
GT65→GO:0046922 both resolve to the same `exactMatch` the seed asserts).

**Caveat** (the redundancy property): because every row is derived *through* an EC that already
reaches GO via `ec2go`, the rows are EC-reachable by construction. Their value is the same as
`interpro2go`'s — annotating a protein from CAZy family membership when it lacks an EC/`ec2go`
annotation — but the marginal-vs-`ec2go` contribution still needs closure-filtering across organisms
(the [RHEA](../RHEA.md) EC-masking method). Finer subfamily resolution (for the `narrowMatch`
families) is the next refinement, seedable from the **dbCAN-sub subfamily → EC** table
([dbCAN3](https://pubmed.ncbi.nlm.nih.gov/37125649/)).

### Did it yield anything new, or just confirm?

At the **GO-term level it is confirmatory by construction** — derived through `ec2go`, it cannot mint
a term `ec2go` lacks. But the join surfaced genuinely new, actionable signal:

- **19 GO-coverage-gap families** — curated EC(s) but no `ec2go` term at all. Notably a whole class:
  the **auxiliary-activity / LPMO redox CAZymes** (AA9, 28 reviewed members; AA10–AA14; CBM104) on
  EC 1.14.99.54/56, plus **GH130** (β-mannoside phosphorylases) and **GT81**. Systematic GO-MF gaps,
  not confirmation. (Some are partial ECs / `ec2go` lag; AA9 & GH130 carry full ECs — real candidates.)
- **Independent rediscovery of the B3GALNT2 gap**: `EC 2.4.1.313` is absent from `ec2go` and is
  carried by **GT31** — the same gap our hand B3GALNT2 review raised as a `proposed_new_term`, found
  here with zero manual input. Validates the gap-finding (not just echoing known annotations).
- **A coarseness map**: GT1 → 33 GO MF terms (214 members), GH13 → 27, GH1 → 25, GT4 → 21 — quantifies
  exactly which families are too heterogeneous to propagate from (the `narrowMatch` set) and should be
  prioritised for dbCAN-sub subfamily resolution.

**`cazy2go` vs `interpro2go` (computed)** — the marginal-knowledge test, via
[`compare_cazy_interpro.py`](compare_cazy_interpro.py) (UniProt CAZy+EC+InterPro × `ec2go` ×
`interpro2go`). **This is the opposite of the RHEA result**: where RHEA was ~84% masked by EC2GO,
`cazy2go` is only **20% masked** by `interpro2go` —

- **283** families have a `cazy2go` GO MF term; **56 (20%)** are fully masked by `interpro2go`, but
  **227 (80%)** reach ≥1 GO MF term InterPro does **not** supply (**544** marginal (family,GO) pairs,
  exact-match upper bound).
- **Why the inverse of RHEA:** `interpro2go` is deliberately *conservative* — a signature maps to GO
  only when the term holds for **all** matching proteins, so for heterogeneous enzyme families it
  withholds the specific catalytic term (or gives only a generic parent). `cazy2go` (via EC) supplies
  the **reaction-level specificity** InterPro withholds. The two routes are **complementary by
  altitude**, not redundant.
- **The safe, actionable win = 110 mono-specific (`exactMatch`) families** with a marginal term →
  safe to propagate at family level. Headliners: **GT27** (polypeptide-GalNAc-T, mucin-type
  O-glycosylation initiators, 46 members), **GT66** (OST glycotransferase, N-glycosylation), **GT39**
  (dolichyl-P-mannose-protein mannosyltransferase), **GT13** (GnT-I), **GT21** (ceramide
  glucosyltransferase), **GH109** (α-N-acetylgalactosaminidase). (A handful only reach a generic
  `hexosyltransferase activity` and are weaker.)
- **The other 117 marginal families are poly-specific** (`narrowMatch`) — real specificity gain but
  **unsafe at family level**; route via subfamily/EC (dbCAN-sub).
**Closure-filtered result** ([`closure_cazy_interpro.py`](closure_cazy_interpro.py), GO `is_a`
closure via oaklib / cached `sqlite:obo:go`). I expected closure to *shrink* the 544 headline; **it
barely does (544 → 529)** — instead it shows what kind of contribution it is. Partitioning the 544
marginal pairs:

| class | pairs | meaning |
|-------|------:|---------|
| **DESCENDANT_MASKED** (drop) | **15 (3%)** | InterPro already gives G or a *more specific* child → no gain |
| **ALTITUDE_GAIN** | **405 (74%)** | InterPro gives only a generic *ancestor*; `cazy2go` adds the specific reaction-level MF |
| **TRUE_GAP** | **124 (23%)** | InterPro is *silent* on G's branch for this family → genuinely new coverage |

So only **3%** of the marginal is closure-masked; **97% is real** (529 pairs = altitude + gap). The
TRUE_GAP set spans **98 families** and includes biologically central activities InterPro2GO does not
supply for the family at all: **GT27/CBM13 → polypeptide-GalNAc-T** (mucin O-glyco initiators),
**GH19 → lysozyme**, **GH14 → α-amylase**, **GH33 → sialidase**, **PL1 → pectin lyase**,
**GT43 → β-1,4-xylan synthase**, **GH32 → fructan fructosyltransferase**. (A few are still generic,
e.g. GH72 → `hexosyltransferase activity`, or noisy multi-activity families like GH23 → peptidase.)

**Caveat:** `is_a`-only closure; an ALTITUDE_GAIN whose only InterPro ancestor is near the
`molecular_function` root is a weak gain. And the partition is per (family, term): a TRUE_GAP in a
**poly-specific** family (e.g. GH1 90 members → one plant glucosyltransferase) is real coverage but
still **unsafe to propagate at family level** — route via subfamily.

**Bottom line:** `cazy2go` is **not** mostly redundant with `interpro2go` and closure does **not**
explain it away — 97% of the exact-match marginal survives closure as genuine altitude (74%) or
coverage (23%) gain. It adds reaction-level MF specificity for ~110 mono-specific families safely
(family-level) and more via subfamilies; **124 pairs across 98 families are activities InterPro2GO is
silent on entirely**.

## Status

- **Seed**: `cazy2go.sssom.yaml` — 5 exemplar GT-family rows, review-backed, GO ids QuickGO-verified.
- **Generated**: `cazy2go.generated.sssom.yaml` — 702 rows / 283 families, reproducible via
  `build_cazy2go.py` (UniProt CAZy↔EC × ec2go), SSSOM-structurally valid.
- **Marginal-vs-interpro2go**: computed (`compare_cazy_interpro.py`) — only 20% masked; and
  **closure-filtered** (`closure_cazy_interpro.py`) — 97% of the marginal survives closure (74%
  altitude, 23% true-gap; only 3% descendant-masked).
- **Next**: (1) `cazy2go` LinkML schema + `validate-cazy-mappings` recipe mirroring
  `validate-rhea-mappings` (incl. GO-label term validation of a generated terms file); (2) subfamily
  resolution for the poly-specific families from dbCAN-sub (so TRUE_GAP/altitude terms can be
  attributed safely); (3) curate the ~110 mono-specific safe wins + the 98 TRUE_GAP families into
  the `cazy2go.sssom.yaml` proper; (4) GlycoCoO→GO alignment SSSOM; (5) GlyGen-join confirmatory
  probe over the exemplars.
