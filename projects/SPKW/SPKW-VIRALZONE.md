---
title: "SPKW ViralZone Upstream-Source Subproject"
autolink_gene_symbols: false
---

# SPKW ViralZone Upstream-Source Subproject

**Parent project:** [SPKW.md](../SPKW.md) · **Sibling:** [SPKW-VIRUS.md](SPKW-VIRUS.md)

## Overview

Every other SPKW subproject audits a *downstream* product: annotations that a
keyword-to-GO mapping produced on particular proteins. This one audits the
*upstream* source those verdicts quietly depend on.

[SPKW-VIRUS.md](SPKW-VIRUS.md) established `VZ-primary` as a confidence flag: a
Swiss-Prot keyword that is the primary keyword of a ViralZone page is much less
likely to be one of the generic keyword artifacts driving the virus-wide SPKW
burden, so the flag raises the prior on the annotation. That is a claim about
ViralZone's editorial quality — and nobody had checked it.

Checking it turns out to matter more than expected, because ViralZone does not
feed GO once. It feeds GO twice, by two routes that meet again downstream:

1. **Definition route.** GO cites ViralZone pages as definition cross-references
   under the prefix `VZ` — `GO:0039713 viral factory` carries `VZ:1951`. Where the
   citation marks real textual reuse, the ViralZone page is effectively the term's
   authored definition.
2. **Annotation route.** A ViralZone page may declare one primary UniProt keyword
   in its header. That keyword maps to a GO term and generates the SPKW
   (`GO_REF:0000043`) IEA annotations the parent project reviews.

So a single paragraph of ViralZone prose can determine both **what a GO term
means** and **which proteins are annotated to it**. When both routes run from the
same page, an error upstream is not caught by cross-checking the annotation
against the term definition — because the definition came from the same place.
That compounding is the object of this subproject.

## Scope and Method

All figures on this page are produced by
[`viralzone/build_viralzone_audit.py`](viralzone/build_viralzone_audit.py), which
enumerates ViralZone from its public `sitemap.xml`, fetches each page, reads GO's
`VZ:` cross-references from the local OAK GO build, and writes three tables:

| Table | Contents |
|-------|----------|
| [`vz-go-xrefs.tsv`](viralzone/vz-go-xrefs.tsv) | every GO term citing ViralZone, with a text-reuse score |
| [`vz-dead-xrefs.tsv`](viralzone/vz-dead-xrefs.tsv) | GO terms citing a page absent from the live sitemap |
| [`vz-dual-path.tsv`](viralzone/vz-dual-path.tsv) | pages on both routes (GO definition xref **and** primary keyword) |

**Reuse scoring.** For each sentence of a GO definition, the best-matching window
of the cited page's prose is scored with `difflib.SequenceMatcher` on normalized
text; the term's score is its best sentence. Two cautions are load-bearing:

- `autojunk` must be disabled. On strings over 200 characters the default
  heuristic treats frequent characters as noise; with it on, `GO:0039713` against
  `VZ:1951` scores **0.006** instead of **0.82**. Any similar audit that reports
  near-zero reuse everywhere has probably hit this.
- A high score means textual reuse, **not** that the definition is wrong. A low
  score means GO wrote its own text, **not** that ViralZone was ignored. The score
  selects what to audit; it is not itself a verdict.

Page prose is cut at the first navigation/UniProt-table marker: ViralZone appends
the full list of matching UniProt entries to keyword pages (`VZ:982` is 161 KB of
HTML for ~450 characters of definition), which would otherwise swamp the text.

**Cross-check on the keyword extraction.** This script reads the primary keyword
from the `(kw:KW-####)` string rendered in the page header and finds **147**
pages carrying one. The 2026-05-21 audit behind [SPKW-VIRUS.md](SPKW-VIRUS.md)
read the same field from the header's `data-about` attribute and also found 147.
Two independent readings agreeing is the reason to trust either.

## Results

### Propagation footprint

| Measure | Count |
|---------|------:|
| ViralZone pages in the live sitemap | 1,170 |
| ...with prose successfully fetched | 1,158 |
| ...declaring a primary UniProt keyword (annotation route) | 147 |
| GO terms carrying a `VZ:` dbxref (definition route) | 152 |
| ...scorable (cited page still live) | 148 |
| ...by aspect | 126 BP / 22 CC |
| ViralZone pages cited by GO | 144 |
| **Pages on both routes** | **107** |
| ...keyword only | 40 |
| ...definition xref only | 37 |

There is no molecular-function term in the set: ViralZone's influence on GO is
entirely on process and component.

### Text reuse is the exception, not the rule

| Reuse band | Best-sentence similarity | Terms | Share |
|------------|-------------------------:|------:|------:|
| `VERBATIM_ISH` | ≥ 0.85 | 10 | 7% |
| `CLOSE_PARAPHRASE` | 0.70–0.85 | 12 | 8% |
| `REWORDED` | 0.55–0.70 | 24 | 16% |
| `INDEPENDENT` | < 0.55 | 102 | **69%** |

This is the subproject's first substantive finding, and it is reassuring: in
roughly seven cases out of ten, GO curators used ViralZone as a *reference* and
wrote their own definition. The naive worry — that GO's viral vocabulary is a
transcription of ViralZone — is wrong as a general claim.

It is right for a minority, and that minority is where the two routes overlap
most:

| | keyword present | keyword absent |
|---|---:|---:|
| `VERBATIM_ISH` | 9 | 1 |
| `CLOSE_PARAPHRASE` | 8 | 4 |
| `REWORDED` | 21 | 3 |
| `INDEPENDENT` | 75 | 27 |

**17 of the 22 high-reuse terms also sit on the annotation route.** For those, the
GO definition and the SPKW annotations trace to one unreferenced paragraph, and a
`VZ-primary` flag on the annotation adds no independent confirmation of the term
it is annotated to. This is the concrete form of the compounding risk, and it is a
sharpening of SPKW-VIRUS's working rule rather than a contradiction of it.

### Highest-reuse definitions (audit queue)

All 22 are live (non-obsolete) terms. `kw` marks the annotation route.

| GO term | Label | Page | best | mean | kw |
|---------|-------|------|-----:|-----:|----|
| GO:0099045 | viral extrusion | VZ:3951 | 0.99 | 0.81 | KW-1249 |
| GO:0075520 | actin-dependent intracellular transport of virus | VZ:991 | 0.99 | 0.73 | KW-1178 |
| GO:0099009 | viral genome circularization | VZ:3968 | 0.91 | 0.75 | KW-1253 |
| GO:0099000 | symbiont genome ejection through host cell envelope | VZ:3950 | 0.90 | 0.63 | KW-1242 |
| GO:0060141 | symbiont-mediated induction of syncytium formation | VZ:5957 | 0.88 | 0.62 | KW-1180 |
| GO:0099001 | symbiont genome ejection through host cell envelope | VZ:3952 | 0.87 | 0.64 | KW-1243 |
| GO:0075525 | viral translational termination-reinitiation | VZ:858 | 0.86 | 0.66 | KW-1158 |
| GO:0039592 | symbiont-mediated arrest of host cell cycle | VZ:876 | 0.85 | 0.67 | KW-1079 |
| GO:0039690 | positive stranded viral RNA replication | VZ:1116 | 0.85 | 0.67 | — |
| GO:0075526 | cap snatching | VZ:839 | 0.85 | 0.81 | KW-1157 |
| GO:0099018 | symbiont-mediated evasion of host restriction-modification system | VZ:3966 | 0.85 | 0.64 | KW-1258 |
| GO:0039698 | polyadenylation of viral mRNA by polymerase stuttering | VZ:1916 | 0.84 | 0.72 | — |
| GO:0039704 | viral translational shunt | VZ:608 | 0.84 | 0.84 | — |
| GO:0039708 | nuclear capsid assembly | VZ:1516 | 0.83 | 0.69 | — |
| GO:0098931 | virion attachment to host cell flagellum | VZ:3949 | 0.83 | 0.71 | KW-1240 |
| GO:0099002 | symbiont genome ejection through host cell envelope | VZ:3954 | 0.83 | 0.67 | KW-1244 |
| GO:0039713 | viral factory | VZ:1951 | 0.82 | 0.74 | — |
| GO:0098669 | superinfection exclusion | VZ:3971 | 0.79 | 0.59 | KW-1260 |
| GO:0046755 | viral budding | VZ:1947 | 0.78 | 0.75 | KW-1198 |
| GO:0039666 | virion attachment to host cell pilus | VZ:981 | 0.78 | 0.54 | KW-1175 |
| GO:0039587 | symbiont-mediated-mediated suppression of host tetherin activity | VZ:665 | 0.77 | 0.57 | KW-1084 |
| GO:0098671 | adhesion receptor-mediated virion attachment to host cell | VZ:3943 | 0.76 | 0.60 | KW-1233 |

Two rows connect directly to an existing verdict. `GO:0099018` (R-M evasion) and
`GO:0099000` (contractile-tail genome ejection) are both named in
[SPKW-BPT4.md](SPKW-BPT4.md) as the *good* phage-specific replacement targets;
`GO:0099000` carries an explicit **ACCEPT** there for T4 `18/P13332`, `19/P13333`
and `20/P13334`, reasoned from the tail-contraction mechanism. Those calls still
look right — the sheath/tube/portal argument stands on UniProt's own description,
not on ViralZone. But the definitions of both terms score in the high-reuse band,
so "the GO definition supports this" and "ViralZone supports this" are one
argument, not two, and the ACCEPT should rest on the mechanism rather than on
their agreement.

### Worked case: the viral-factory branch

`GO:0039713 viral factory` scores 0.82/0.74 against `VZ:1951`, and the branch
beneath it — spherule, double-membrane vesicle, tube viral factory, virogenic
stroma, peristromal region — is drawn from the same page's sections, though only
the parent carries the dbxref. Sizes ("50-400nm diameter membrane invagination",
"200-300nm... derived from the endoplasmic reticulum or Golgi") and family lists
travel verbatim into the definitions.

GO's curator did filter: `VZ:1951` states that viroplasms are produced by
"ssRNA(-) viruses like filoviridae", and `GO:0039716 viroplasm viral factory`
drops that clause. So the definition route is not a blind copy even at its most
derivative. What is not known is whether *other* ViralZone claims were filtered as
carefully — which is what the audit queue is for.

This is recorded as scope note (5) in [`modules/viral_factory.yaml`](../../modules/viral_factory.yaml),
so a reader of that module does not mistake its GO groundings and ViralZone for
independent support.

### Maintenance defects found in passing

Neither of these needs a biology judgement; both are filable now.

**Four dead cross-references.** GO cites pages absent from the live sitemap:

| GO term | Label | Page |
|---------|-------|------|
| GO:0039525 | symbiont-mediated perturbation of host chromatin organization | VZ:899 |
| GO:0039628 | T=169 icosahedral viral capsid | VZ:10117 |
| GO:0052150 | symbiont-mediated perturbation of host apoptosis | VZ:1518 |
| GO:0039659 | *(obsolete)* suppression by virus of host TBK1-IKBKE-DDX3 complex activity | VZ:719 |

The first three are live terms whose stated provenance no longer resolves.

**A doubled-word label.** `GO:0039587` reads
"symbiont-mediated**-mediated** suppression of host tetherin activity" — a
straightforward GO label typo, surfaced by reading 152 labels in one pass.

**Nine obsolete terms** still carry `VZ:` cross-references (`GO:0019048`,
`GO:0019051`, `GO:0039511`, `GO:0039526`, `GO:0039553`, `GO:0039586`,
`GO:0039589`, `GO:0039655`, `GO:0039667`). Harmless, and useful as provenance for
why the terms were once created; noted so the audit queue can skip them.

## Source-Quality Assessment

Read as an evidence source rather than a vocabulary, ViralZone has one
disqualifying property and several minor ones.

**No inline references, anywhere.** `VZ:695` asserts that "Vaccinia K1 inhibits
NF-kappa-B by preventing I-kappa-B degradation" and that "A238L from African swine
fever virus interacts with free NF-kappa-B to prevent its nuclear translocation"
with no PMID attached to either. Every ViralZone claim is therefore tertiary and
untraceable without independent lookup. This is why ViralZone is registered in
[`conf/oak_config.yaml`](../../conf/oak_config.yaml) as `VZ: null` — an explicitly
unvalidated prefix — and why a ViralZone quote should never be the sole support
for a curation action in this repository.

**Copy quality is below journal standard.** "Attachement", "neo-synthetized",
"NF-kBdependent", "occulsion", "african swine virus" for African swine fever
virus, and a page titled "Poylprotein splitting". None of this is disqualifying on
its own; it is a signal about editorial process, and it is a reason to read a
quoted sentence rather than trust it.

**Prose is short and useful.** Median ~1,300 characters after the UniProt table is
stripped. The process pages read like GO definitions already; the family pages are
structured mini-records (VIRION / GENOME / GENE EXPRESSION / ENZYMES /
REPLICATION). The whole audit queue is 24,824 characters of prose — a day's close
reading, not a programme.

**The useful content is largely already harvested.** GO has absorbed the
definitional material into terms with taxon constraints and a hierarchy.
ViralZone's remaining value to this repository is breadth on families GO has not
termed, plus provenance for why terms say what they say — not rigour GO lacks.

## Working Rules (refines SPKW-VIRUS)

1. **`VZ-primary` remains a positive prior, with one subtraction.** Where the
   annotated term is also a high-reuse term (the 17 in the crosstab above), the
   flag and the term definition are the same evidence. Do not count them twice.
2. **Never cite ViralZone as sole support.** Use it to locate a claim, then cite
   the primary literature that establishes it.
3. **Cite pages as `VZ:<id>`,** GO's own dbxref spelling and the numbering used
   throughout this project — not the bioregistry `viralzone` prefix.
4. **A `VZ:` citation carries no verified quote.** The repository's
   supporting-text validator resolves `PMID:`/`DOI:` only, so a `supporting_text`
   on a `VZ:` source passes unchecked. Prefer `statement` over `supporting_text`
   for ViralZone evidence items.

## Work Queue

| # | Task | Scope | Status |
|---|------|-------|--------|
| 1 | File the four dead `VZ:` cross-references with GO | 4 terms | TODO |
| 2 | File the `GO:0039587` doubled-word label typo | 1 term | TODO |
| 3 | Audit the 22 high-reuse definitions against primary literature | 24,824 chars | TODO |
| 4 | For each, record divergences **both ways**: a ViralZone error that propagated into GO, and a ViralZone correction GO missed | 22 terms | TODO |
| 5 | Grade the 107 dual-path pages, so SPKW inherits a per-page confidence rather than a flat `VZ-primary` boolean | 107 pages | TODO |
| 6 | Decide whether `VZ:` should become quote-checkable (needs a page cache; see the `PMCID`/Reactome gap in the same validator) | infra | OPEN QUESTION |

Task 3 is the only one requiring literature work, and the filovirus/viroplasm case
is the model: establish what the page claims, what GO carried over, and whether the
difference was a judgement or an accident.

## Status

- **Started**: 2026-09-27
- **Terms measured**: 152 (148 scorable)
- **Terms audited against literature**: 0 of 22 queued
- **Defects filed**: 0 of 5 found
