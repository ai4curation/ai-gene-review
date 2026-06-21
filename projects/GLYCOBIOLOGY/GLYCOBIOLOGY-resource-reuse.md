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

### Scaling beyond the seed

The seed covers 5 families. The full ~190 GT/GH/PL/CE families can be seeded from the **dbCAN-sub
subfamily → EC → glycan-substrate** table ([dbCAN3](https://pubmed.ncbi.nlm.nih.gov/37125649/)),
which is specific enough to avoid the family-level coarseness (it is precisely the subfamily
resolution the `narrowMatch` rows ask for), then EC → `ec2go` for the GO target and the redundancy
filter for the marginal set.

## Status

- **Seeded**: `cazy2go.sssom.yaml` (5 exemplar GT-family rows; GO ids QuickGO-verified, activities
  review-backed).
- **Next**: (1) build the `cazy2go` LinkML schema + `validate-cazy-mappings` recipe mirroring
  `validate-rhea-mappings`; (2) compute live `ec2go`/`interpro2go` redundancy; (3) seed GlycoCoO→GO
  alignment SSSOM; (4) write the GlyGen-join confirmatory probe over the exemplars.
