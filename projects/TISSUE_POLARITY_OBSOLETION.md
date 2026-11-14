---
title: "Establishment of Tissue Polarity — Obsoletion (GO:0007164) and the PCP Restructuring"
maturity: SCOPING
tags: [OBSOLETION]
species: [DROME, rat, mouse, ARATH, DANRE, CHICK, human]
genes:
  - pk
  - ft
  - Hnf4a
  - PIP5K4
  - ccdc57
  - Grg4
# "Hnf4a" on this page means the rat gene, which has no review here; the only
# HNF4A review is the human paralog, so do not autolink the symbol.
autolink_exclude: [HNF4A]
---

# Establishment of Tissue Polarity — Obsoletion (GO:0007164) and the PCP Restructuring

**Bottom line:** GO proposes to obsolete **GO:0007164 *establishment of tissue
polarity*** because its only child is GO:0001736 *establishment of planar
polarity* and no other kind of tissue polarity is known — apical/basal and other
cell-level polarity terms live under *cell polarity*. The upstream annotation
ticket lists 5 direct experimental annotations to review and reports two of them
(FlyBase *ft*, ZFIN *ccdc57*) as already handled. A QuickGO check run for this
page on 2026-10-31 found **28 live annotations to GO:0007164**, including **two
things the upstream table does not list**: a sixth experimental annotation
(chicken *Grg4*, AgBase IMP, PMID:10772799 — a midbrain-tectum paper that looks
like a wrong-term call, not a planar-polarity one) and an **ARBA machine-learning
rule, ARBA00029049, that still produces GO:0007164** even though the ticket
states no mappings exist. Both are worth reporting upstream. GO:0007164 is **not
yet obsolete in OLS** (checked 2026-10-31), so nothing in this repo is broken
today; no review in `genes/` uses GO:0007164 at all. The larger exposure is the
parent ontology ticket, which also obsoletes the whole Wnt/PCP signalling branch
and thirteen compound planar-polarity terms — **15 reviews in this repo use
terms slated for obsoletion or redefinition**. Scoped, not started: no gene
review has been written or edited for this project.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6638](https://github.com/geneontology/go-annotation/issues/6638)
  (open; last updated 2026-10-30)
- Ontology ticket: [geneontology/go-ontology#32697](https://github.com/geneontology/go-ontology/issues/32697)
  — "Review of planar cell polarity GO terms and ontology" (open), the parent
  proposal that motivates the obsoletion

The ontology ticket records that the restructuring was agreed with PCP experts
(fly and mouse) and reorganises the branch into a morphogenesis arm under
GO:0001736 plus new "PCP module" terms under GO:0007154 *cell communication*.
Issue #6638 is, as of 2026-10-31, the **only** annotation-side ticket opened for
that restructuring: a search of the go-annotation tracker for the ontology issue
number and for "planar polarity" in titles returns nothing else.

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| establishment of tissue polarity | GO:0007164 | no single replacement; per-annotation re-terming (below) |

Term labels and status below were checked against OLS on 2026-10-31.

| Term | ID | OLS status |
|---|---|---|
| establishment of tissue polarity | GO:0007164 | live (obsoletion proposed) |
| establishment of planar polarity | GO:0001736 | live (definition/parentage being updated) |
| establishment of epithelial cell apical/basal polarity | GO:0045198 | live |
| tight junction assembly | GO:0120192 | live |
| maintenance of cell polarity | GO:0030011 | live |
| pollen tube growth | GO:0009860 | live |

The upstream table also suggests two **new** PCP module terms, written there as
`GO:7770140 core planar cell polarity` and `GO:7770141 Fat/Dachsous planar cell
polarity`. Neither id resolves in OLS as of 2026-10-31, so they are recorded
here as upstream-proposed ids only and **must be re-checked before use** — the
ontology ticket shows the three new module terms (*planar cell polarity*, *core
planar cell polarity*, *Fat/Dachsous planar cell polarity*, reference
PMID:27576155) as created, so the ids are plausible but unverified. The parent
*planar cell polarity* term is marked "not for direct annotation".

### Affected upstream groups (from the issue body)

| Group | Annotations | Status per upstream |
|---|---:|---|
| TAIR | 1 | pending |
| UniProt | 1 | pending |
| RGD | 1 | pending |
| FlyBase | 1 | DONE (comment by rozaru) |
| ZFIN | 1 | DONE (comment by sramachand) |
| AgBase | 1 | **not listed upstream** (found here) |

### Mappings to be reviewed

The issue body states: "There are no InterPro2GO, UniProt-Keyword, UniRule or EC
mappings to this term." That enumeration omits ARBA, and **an ARBA rule is
live**: QuickGO shows `UniProtKB:A0A8S0VMH2` (*Olea europaea* subsp. *europaea*,
OLEA9_A111867) annotated IEA to GO:0007164 under GO_REF:0000117 ("Electronic Gene
Ontology annotations created by ARBA machine learning models") with
`with/from ARBA:ARBA00029049`. The rule is already in this repo's rules export
(`rules/rules-export-go-summary.csv:2584`) and in the ARBA redundancy table
(`projects/ARBA_REVIEW/rule_redundancy.tsv:2508`), where it is recorded as
covered by GO:0001736 — i.e. the rule's condition sets are already served by the
surviving term. Retiring or re-pointing ARBA00029049 to GO:0001736 should be
part of the obsoletion, and is the one mapping action the ticket is missing.
See [ARBA_REVIEW](ARBA_REVIEW.md).

## Live annotation set (QuickGO, exact term, 2026-10-31)

28 annotations total. Grouped by what they are:

### Experimental, direct (6 — upstream lists 5)

| Gene | UniProt | Organism | Ev | Reference | Group | Upstream recommendation |
|---|---|---|---|---|---|---|
| pk (prickle) | A1Z6W3 | *D. melanogaster* | IMP | PMID:12015986 | UniProt | **Remove** — same paper already gives GO:0001736; consider the new core-PCP term |
| ft (fat) | P33450 | *D. melanogaster* | IMP | PMID:16735478 | FlyBase | Replace with GO:0001736 (or Fat/Dachsous PCP) — reported DONE, still live in QuickGO |
| ccdc57 | A0A8M1NYX9, E7EY31 | *D. rerio* | IMP | PMID:36862758 | ZFIN | Replace with GO:0001736 — reported DONE, still live in QuickGO (2 rows) |
| Hnf4a | P22449 | *R. norvegicus* | IDA | PMID:12749857 | RGD | Replace with GO:0045198 and/or GO:0120192 |
| PIP5K4 | Q9M1K2 | *A. thaliana* | IMP | PMID:19033528 | TAIR | Replace with GO:0030011, or remove (paper already gives GO:0009860) |
| **Grg4** | **Q8JIM6** | *G. gallus* | IMP | PMID:10772799 | **AgBase** | **none — missing from the upstream table** |

PMIDs above were resolved against PubMed on 2026-10-31; the titles match the
claims made in the upstream table.

The ZFIN and FlyBase rows being "DONE" upstream while still present in QuickGO is
expected release lag, not a contradiction — but it means the counts should be
re-pulled before anyone acts on this page.

### Propagated from the rows above (8)

| Gene | UniProt | Organism | Ev | Source |
|---|---|---|---|---|
| Hnf4a | P49698 | *M. musculus* | ISO | GO_REF:0000096, mouse–rat transfer from the RGD row |
| pk | Q174I2 | *Aedes aegypti* | ISS | GO_REF:0000024, `with` UniProtKB:A1Z6W3 |
| pk | Q292U2 | *D. pseudoobscura pseudoobscura* | ISS | GO_REF:0000024, `with` UniProtKB:A1Z6W3 |
| pk | Q7QJT4 | *Anopheles gambiae* | ISS | GO_REF:0000024, `with` UniProtKB:A1Z6W3 |

(plus 13 EnsemblMetazoa IEA rows across *Drosophila* species under
GO_REF:0000107, Ensembl Compara ortholog transfer.)

These matter because they are **downstream of annotations the ticket wants
removed**, not re-termed: if the fly *pk* IMP is removed rather than replaced,
the three UniProt ISS rows and the Compara IEA rows lose their seed and should
follow it, and the mouse *Hnf4a* ISO follows whatever RGD does to the rat row.
The upstream table does not mention this cascade.

### Electronic, rule-derived (1)

`A0A8S0VMH2` (*Olea europaea*), IEA, GO_REF:0000117, ARBA00029049 — see
**Mappings** above.

## Impact on this repo

**Direct impact of the GO:0007164 obsoletion: none.** No file under `genes/`
cites GO:0007164, and none of the six experimentally annotated genes is reviewed
here (`genes/human/HNF4A` exists but is the human paralog, and its review does
not touch polarity or tight-junction terms; `genes/ARATH/FT` is *FLOWERING LOCUS
T*, unrelated to fly *ft*). `genes/CHICK/` exists but has no *Grg4*.

**Indirect impact of the parent PCP restructuring: 15 reviews.** Counts from
`grep -rl` over `genes/**/*-ai-review.yaml` on 2026-10-31:

| Term | ID | Upstream plan | Reviews here |
|---|---|---|---:|
| Wnt signaling pathway, planar cell polarity pathway | GO:0060071 | obsolete | 7 |
| establishment of planar polarity | GO:0001736 | redefine, re-parent | 8 |
| regulation of Wnt signaling pathway, PCP pathway | GO:2000095 | obsolete | 1 |
| positive regulation of Wnt signaling pathway, PCP pathway | GO:2000096 | obsolete | 1 |
| establishment of ommatidial planar polarity | GO:0042067 | obsolete | 1 |
| microtubule cytoskeleton organization involved in establishment of planar polarity | GO:0090176 | obsolete | 2 |
| protein localization involved in establishment of planar polarity | GO:0090251 | obsolete | 1 |
| establishment of planar polarity of embryonic epithelium | GO:0042249 | obsolete | 1 |

The affected reviews (some appear twice):

- **GO:0060071** — `human/ADGRA3`, `human/ANKRD6`, `human/ARHGEF19` (ACCEPT),
  `human/CDC42` (UNDECIDED), `human/FZD7` (KEEP_AS_NON_CORE), `human/LRP6`
  (ACCEPT, IDA), `rat/Rac1` (KEEP_AS_NON_CORE)
- **GO:0001736** — `ARATH/AUX1`, `ARATH/EIN2`, `human/ANKRD6`, `human/INTU`,
  `human/WDPCP`, `mouse/Ptk7`, `mouse/Wdpcp`, `rat/Ptk7`
- **GO:2000095** — `human/ADGRA3`; **GO:2000096** — `human/ANKRD6`
- **GO:0042067** — `DROME/hbs`; **GO:0090176** — `human/BRSK2`,
  `human/PAFAH1B1`; **GO:0090251** — `worm/nphp-1`; **GO:0042249** —
  `human/PAFAH1B1`

The reviews that **ACCEPT** a GO:0060071 row (`human/ARHGEF19`, `human/LRP6`)
are the ones that will need real re-reasoning: upstream's position is that
"Wnt/PCP signaling does not exist as a separate signaling process", so an
accepted row becomes an assertion about a retired class. `human/ANKRD6` appears
in three of the eight lists and is the densest single case.

## Scope

- **Organisms**: *D. melanogaster* (2 direct), *D. rerio*, *R. norvegicus*,
  *A. thaliana*, *G. gallus* for the obsoletion itself; plus *M. musculus*,
  three other insects and 13 *Drosophila* species via propagation. The wider
  PCP restructuring is fly- and mouse-heavy.
- **GO branches**: BP only. The obsoletion sits in the morphogenesis arm; the
  parent ticket also moves material into *cell communication* via the new
  PCP-module terms.
- **Size of the wider batch** (QuickGO exact counts, all evidence, 2026-10-31,
  for context — these are *not* this project's workload): GO:0001736 6331,
  GO:0060071 1960, GO:2000095 973, GO:2000096 836, GO:0042067 599,
  GO:0001737 528, GO:0141113 9. The ontology ticket's own EXP counts are much
  smaller (122 and 97 for the two biggest), which is the number that matters for
  manual review.
- **Type of fix**: mostly terminological, but two of the six direct cases are
  substantive. The rat *Hnf4a* row is a genuine aspect error (apical/basal
  polarity annotated as tissue polarity), and the chicken *Grg4* row looks like
  a different error again — PMID:10772799 is about antagonising tectum-organising
  activity, i.e. midbrain anteroposterior patterning, which is not planar
  polarity in any sense; that row probably wants removal, not re-terming.

## Candidate genes for initial review

Verify each with `just fetch-gene <organism> <gene>` before starting, and
re-pull QuickGO first — the ZFIN and FlyBase rows may have cleared by then.
Accessions below were confirmed against the UniProt REST API on 2026-10-31.

1. **DROME pk** (*prickle*, FB:FBgn0003090, UniProt A1Z6W3, PRIC1_DROME) — the
   highest-value target. It is a **core PCP module** gene (the ontology ticket
   names Pk among the six fly core components), it is the one pending UniProt
   row, and it seeds the three ISS rows. PMID:12015986 ("Prickle mediates
   feedback amplification to generate asymmetric planar cell polarity
   signaling") is the paper behind both its GO:0007164 and its GO:0001736
   annotation, so the review can decide between removal-as-redundant and the new
   core-PCP term on the actual evidence. Doing *pk* also gives this repo a
   reference review for the new module terms.

2. **rat Hnf4a** (RGD:2810, UniProt P22449, HNF4A_RAT) — the clearest wrong-term
   case: PMID:12749857 reports HNF-4alpha triggering tight junction formation and
   polarised epithelial morphology in F9 cells, which is GO:0045198 and/or
   GO:0120192, not tissue polarity. Review should also address the mouse ISO row
   (P49698) that follows it, and can be cross-read against the existing
   `genes/human/HNF4A` review, which currently says nothing about polarity.

3. **CHICK Grg4** (UniProt Q8JIM6, Groucho-related gene 4, TrEMBL) — the
   annotation upstream missed. PMID:10772799 is a tectum-organiser paper; the
   IMP to GO:0007164 should most likely be removed outright. Low cost, and the
   finding is useful upstream whether or not a full review is written. A
   `review.source_defects` entry (resource AgBase) is the right way to record it
   if a review is written.

4. **ARATH PIP5K4** (AT3G56960, UniProt Q9M1K2, PI5K4_ARATH) — PMID:19033528
   concerns polarity *within* single pollen tube cells, so the question is
   GO:0030011 versus simply dropping the row in favour of the GO:0009860 the same
   paper already supports. `genes/ARATH/` is well populated here, so this fits
   existing coverage.

5. **DANRE ccdc57** (ZDB-GENE-090603-1, UniProt A0A8M1NYX9 / E7EY31) and
   **DROME ft** (FB:FBgn0001075, UniProt P33450, FAT_DROME) — reported DONE
   upstream. Do not re-curate the obsoleted row; they are listed only so the
   QuickGO lag is not mistaken for outstanding work. *ft* is independently
   interesting as a **Fat/Dachsous module** anchor if this repo later takes on
   the new module terms.

6. **Repo-side refresh**, once the Wnt/PCP obsoletions land: `human/ANKRD6`
   first (three affected terms), then `human/LRP6` and `human/ARHGEF19` (both
   ACCEPT a term headed for obsoletion), then the rest of the GO:0060071 and
   GO:0001736 lists above.

## Proposed approach and priority

1. **Report the two gaps upstream on #6638** — the AgBase chicken *Grg4* IMP
   missing from the table, and ARBA00029049 still emitting GO:0007164 despite
   the "no mappings" statement. Both are cheap, verifiable, and useful to the
   curators regardless of what this repo reviews. Note also the propagation
   cascade (3 UniProt ISS + 13 Compara IEA behind fly *pk*; mouse ISO behind rat
   *Hnf4a*), which the table does not cover.
2. **Wait for the new module term ids** before writing any review that would use
   them. `GO:7770140` / `GO:7770141` do not resolve in OLS yet; per CLAUDE.md a
   core function with no live term goes in `proposed_new_terms` with
   `proposed_molecular_function`, not an unresolvable id. For BP rows the honest
   interim action on a *pk*-style case is GO:0001736.
3. **Anchor on fly pk.** It is the one pending row whose biology this repo would
   genuinely add value to, and it doubles as the reference review for core PCP.
4. **Do Hnf4a and Grg4 as the two error cases**, with `source_defects` entries
   (RGD and AgBase respectively) so `just export-source-defects` carries them
   upstream.
5. **Hold the repo-side refresh** until the Wnt/PCP obsoletions are actually
   merged. Re-terming 15 reviews against a proposal that is still open would
   churn them twice.

## Priority

**Low for the obsoletion itself, medium for the restructuring.** GO:0007164 has
6 direct experimental annotations, two already handled, and none of the six genes
is reviewed here — so there is no breakage to fix and little curation value
beyond the *pk* review and the two upstream reports. The parent PCP
restructuring is the real exposure: it retires a term that 7 of our reviews
accept or keep, and redefines one that 8 more use. That is worth watching
closely and acting on promptly once merged.

## Status

- 2026-10-31 — Project file created from an automated scan of the go-annotation
  tracker. Verified upstream issue #6638 and ontology issue #32697; confirmed
  GO:0007164, GO:0001736, GO:0045198, GO:0120192, GO:0030011 and GO:0009860
  against OLS (all live; GO:0007164 not yet obsolete); pulled the 28 live
  GO:0007164 annotations from QuickGO; resolved the six PMIDs against PubMed and
  the eight accessions against UniProt; found the unlisted AgBase *Grg4*
  annotation and the live ARBA00029049 mapping; measured repo impact. No gene
  review started, nothing reported upstream yet.
