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

## Status

- **Seed**: `cazy2go.sssom.yaml` — 5 exemplar GT-family rows, review-backed, GO ids QuickGO-verified.
- **Generated**: `cazy2go.generated.sssom.yaml` — 702 rows / 283 families, reproducible via
  `build_cazy2go.py` (UniProt CAZy↔EC × ec2go), SSSOM-structurally valid.
- **Next**: (1) `cazy2go` LinkML schema + `validate-cazy-mappings` recipe mirroring
  `validate-rhea-mappings` (incl. GO-label term validation of a generated terms file); (2) live
  cross-organism `ec2go`/`interpro2go` closure to quantify the marginal (non-redundant) contribution;
  (3) subfamily resolution for the 121 `narrowMatch` families from dbCAN-sub; (4) GlycoCoO→GO
  alignment SSSOM; (5) GlyGen-join confirmatory probe over the exemplars.
