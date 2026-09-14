---
title: "Lipoate Biosynthetic Process — Obsoletion & Merge into Protein Lipoylation"
maturity: IN_PROGRESS
tags: [OBSOLETION]
species: [BACSU, PSEPK, POPTR, METEA, human, mouse, yeast]
---

# Lipoate Biosynthetic Process — Obsoletion & Merge into Protein Lipoylation

## Overview

A GO obsoletion proposal will obsolete `GO:0009107 lipoate biosynthetic process`
and **merge** it into `GO:0009249 protein lipoylation`, with the latter's
definition broadened to cover both cofactor assembly and its attachment to
lipoyl-carrier proteins.

The upstream rationale is that the two terms are used inconsistently: enzymes
that perform the *biosynthetic* chemistry (octanoyl transfer, sulfur insertion)
are frequently annotated to `protein lipoylation` because the experimental
readout in the primary literature is almost always the **lipoylation status of
carrier proteins**, not free lipoate. Lipoate is essentially never made as a
free pool — the octanoyl group is installed on the lipoyl domain *first* and
sulfurated *in situ* — so "biosynthesis" and "protein lipoylation" describe the
same set of reactions from two angles. Consolidating them follows the precedent
set by `protein glycosylation`.

This project tracks the impact of that merge on AI Gene Review. Unlike most
obsoletion projects in this repo, **several affected genes are already reviewed
here** (see [Impact on this repo](#impact-on-this-repo)), so this is a concrete
re-review queue rather than a pure documentation exercise.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6505](https://github.com/geneontology/go-annotation/issues/6505) (opened 2026-08-14)
- Ontology ticket: [geneontology/go-ontology#32418](https://github.com/geneontology/go-ontology/issues/32418) (opened 2026-08-06, open)
- Affected annotations spreadsheet: [Google Sheet](https://docs.google.com/spreadsheets/d/1Cl-vmLcSU88aFtfCh4-Iy54fF7AcrRUfs2tITzf6IkM/edit?usp=sharing)
- Impacted groups (per upstream issue): EcoliWiki 2, FlyBase 2, MGI 1 (done),
  MTBBASE 1, SGD 1, TIGR 1, UniProt 6

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| lipoate biosynthetic process | GO:0009107 | GO:0009249 protein lipoylation (merge; definition to be broadened) |

**Update 2026-08-30: the obsoletion has landed.** Live QuickGO
(`/ontology/go/terms/GO:0009107/complete`, checked 2026-08-30 during the POPTR
re-review) returns `isObsolete: true` with `replaced_by GO:0009249`, the comment
"The reason for obsoletion is that the term usage has been inconsistent", and
ontology edits timestamped 2026-08-22. The paragraph below records the pre-obsoletion
state for history.

Term status verified via OLS on 2026-08-15 — both terms were then **live**:

- `GO:0009107` (`lipoate biosynthetic process`) — "The chemical reactions and
  pathways resulting in the formation of lipoate, 1,2-dithiolane-3-pentanoate,
  the anion derived from lipoic acid." 12 experimental annotations;
  **23,924 annotations total** (QuickGO, exact-term, all evidence, 2026-08-15)
  — the electronic bulk comes from the InterPro2GO/UniRule mappings below.
- `GO:0009249` (`protein lipoylation`) — current definition "The lipoylation of
  peptidyl-lysine to form peptidyl-N6-lipoyl-L-lysine." 76,753 annotations
  total (QuickGO, exact-term, 2026-08-15). Proposed new definition (edwong57,
  go-ontology#32418): "The chemical reactions and pathways resulting in the
  formation of lipoate ... and its attachment to lipoyl-carrier proteins."

### Ontology-structure note

`GO:0009107` currently has exactly one asserted child, and it is a **`part_of`
link from a molecular function**: `GO:0016992 lipoate synthase activity`
(QuickGO children endpoint, 2026-08-15). When the merge lands, that `part_of`
edge must be re-pointed at `GO:0009249`, or lipoate synthase loses its only
BP anchor. This is worth flagging on the ontology ticket — it is not mentioned
in either upstream issue.

A related caveat raised by Antonialock on go-ontology#32418: GCSH-type proteins
are not merely assembly scaffolds but are themselves lipoyl-dependent enzymes
whose lipoyl group acts as a swinging arm, so assembly and transfer are
genuinely intertwined. The merge is consistent with that view.

## Affected experimental annotations

Verified via the QuickGO annotation API on 2026-08-15 (exact term, experimental
evidence codes only) — 12 annotations, matching the "12 EXP" count in
go-ontology#32418.

| # | Gene product | Symbol | Taxon | Evidence | Reference | Assigned by | Qualifier |
|---|---|---|---|---|---|---|---|
| 1 | UniProtKB:A6NK58 | `LIPT2` | NCBITaxon:9606 (human) | IMP | PMID:28757203 | FlyBase | involved_in |
| 2 | UniProtKB:O32129 | `lipA` | NCBITaxon:224308 (*B. subtilis* 168) | IGI | PMID:19820084 | UniProt | involved_in |
| 3 | UniProtKB:O32174 | `gcvH` | NCBITaxon:224308 (*B. subtilis* 168) | IMP | PMID:21338421 | UniProt | involved_in |
| 4 | UniProtKB:P32463 | `ACP1` | NCBITaxon:559292 (*S. cerevisiae*) | IMP | PMID:9187370 | SGD | involved_in |
| 5 | UniProtKB:P39648 | `lipL` | NCBITaxon:224308 (*B. subtilis* 168) | IMP | PMID:21338420 | UniProt | involved_in |
| 6 | UniProtKB:P39648 | `lipL` | NCBITaxon:224308 (*B. subtilis* 168) | IDA | PMID:21338421 | UniProt | involved_in |
| 7 | UniProtKB:P54511 | `lipM` | NCBITaxon:224308 (*B. subtilis* 168) | IMP | PMID:21338420 | UniProt | involved_in |
| 8 | UniProtKB:P60716 | `lipA` | NCBITaxon:83333 (*E. coli* K-12) | IMP | PMID:8444795 | EcoliWiki | acts_upstream_of_or_within |
| 9 | UniProtKB:P60720 | `lipB` | NCBITaxon:83333 (*E. coli* K-12) | IMP | PMID:8444795 | EcoliWiki | acts_upstream_of_or_within |
| 10 | UniProtKB:P9WK83 | `lipB` | NCBITaxon:83332 (*M. tuberculosis* H37Rv) | IMP | PMID:16735476 | MTBBASE | involved_in |
| 11 | UniProtKB:Q7JQW6 | `Las` | NCBITaxon:7227 (*D. melanogaster*) | IMP | PMID:32648369 | FlyBase | involved_in |
| 12 | UniProtKB:Q99M04 | `Lias` | NCBITaxon:10090 (mouse) | IGI | PMID:11389890 | MGI | acts_upstream_of_or_within |

Notes on this list:

- The upstream group tally lists **TIGR 1**, but no TIGR-assigned annotation
  appears in the QuickGO snapshot above; conversely the human LIPT2 annotation
  (#1) is assigned by FlyBase. Both are bookkeeping discrepancies to confirm
  against the upstream spreadsheet rather than substantive issues.
- Five of the twelve are *B. subtilis* (`lipA`, `gcvH`, `lipL` ×2, `lipM`),
  reflecting the Cronan lab's dissection of the GcvH-relay route
  (PMID:21338420, PMID:21338421). That route is exactly the case the merge is
  meant to clarify: `LipM` octanoylates `GcvH`, `LipL` *transfers* the octanoyl
  group to other lipoyl domains, and `LipA` sulfurates — no free lipoate is ever made,
  so "biosynthetic process" is a misnomer for every step.
- The two EcoliWiki and one MGI annotation use `acts_upstream_of_or_within`,
  which will also want revisiting to `involved_in` when the terms are merged.

## Mappings flagged for redirection

All five InterPro entries verified via the InterPro REST API on 2026-08-15
(names match upstream exactly; protein counts show why the electronic impact is
large):

| Mapping file | Source | Name | Type | Proteins |
|---|---|---|---|---|
| interpro2go | InterPro:IPR003698 | Lipoyl synthase | family | 21,946 |
| interpro2go | InterPro:IPR024897 | Octanoyltransferase LipL | family | 1,008 |
| interpro2go | InterPro:IPR024898 | Octanoyltransferase LipM | family | 624 |
| interpro2go | InterPro:IPR027526 | Lipoyl synthase, chloroplastic | family | 512 |
| interpro2go | InterPro:IPR027527 | Lipoyl synthase, mitochondrial | family | 421 |

UniRule mappings listed upstream (not independently verified here):
`UR000080080`, `UR000112906`, `UR000159987`, `UR000375959`, `UR000376419`,
`UR000376665`.

All eleven mappings redirect cleanly to `GO:0009249 protein lipoylation` — every
one of these families is a lipoate *installation* enzyme, which is precisely
what the broadened `protein lipoylation` definition will cover. There is no
case here (unlike the ent-kaurene obsoletion) where the mapping would be better
served by an MF term instead, because the corresponding MFs
(`GO:0016992 lipoate synthase activity`, octanoyltransferase activities) are
already separately mapped.

## Impact on this repo

Five gene reviews carry `GO:0009107` and ten carry `GO:0009249`. Because
`existing_annotations[].term.id` values are GOA-sourced and deliberately **not**
hard-validated (see CLAUDE.md), the obsoletion does not break validation there —
but `core_functions` term ids **are** strictly validated. Four reviews used
`GO:0009107` inside `core_functions.directly_involved_in`; **as of 2026-08-30,
zero do** — the migration below was applied in the POPTR knowledge-base
re-review (PR #2784), exactly as prescribed by this tracker.

### Reviews containing `GO:0009107`

| Review | Where | Detail |
|---|---|---|
| POPTR/LIP1 | `existing_annotations` ×2 + `core_functions` | IBA (GO_REF:0000033, PANTHER:PTN000101947) and IEA (GO_REF:0000120, via IPR003698/IPR027527/UR000375959); both **MODIFY → GO:0009249** (were ACCEPT); `core_functions` entry dropped |
| POPTR/LIP1P-1 | `existing_annotations` ×2 + `core_functions` | same IBA + IEA pattern; both **MODIFY → GO:0009249**; `core_functions` entry dropped |
| POPTR/LIP1P-2 | `existing_annotations` ×2 + `core_functions` | same IBA + IEA pattern; both **MODIFY → GO:0009249**; `core_functions` entry dropped |
| BACSU/lipA | `existing_annotations` ×2 + `core_functions` | IEA (GO_REF:0000120, via IPR003698/UR000080080) **and the IGI on PMID:19820084 that is item #2 on the upstream experimental list**; both **MODIFY → GO:0009249**; `core_functions` entry dropped |
| PSEPK/lipA | `existing_annotations` ×1 | IEA (GO_REF:0000120, via IPR003698/UR000080080); **MODIFY → GO:0009249** (was ACCEPT) |

**The merge was a clean deletion in every one of the four `core_functions`
blocks**: each already listed `GO:0009249 protein lipoylation` alongside
`GO:0009107`, so the fix was to drop the `GO:0009107` entry rather than to
re-point it — applied 2026-08-30; `GO:0009249` is now the sole
`directly_involved_in` BP in all four. Example of the pre-migration state
(`genes/POPTR/LIP1/LIP1-ai-review.yaml`):

```yaml
  directly_involved_in:
  - id: GO:0009107          # <- removed 2026-08-30
    label: lipoate biosynthetic process
  - id: GO:0009249          # <- already present; now the sole BP
    label: protein lipoylation
```

The same paired-redundancy pattern holds in the GOA records themselves — every
in-repo gene with a `GO:0009107` IEA also has a `GO:0009249` IEA from the same
UniRule — which is direct evidence for the upstream claim that the two terms
are used interchangeably.

### Reviews containing `GO:0009249` (unaffected, but in scope for re-check)

`POPTR/LIP1`, `POPTR/LIP1P-1`, `POPTR/LIP1P-2`, `BACSU/lipA`, `PSEPK/lipA`,
`PSEPK/lipB`, `PSEPK/gcvH1`, `PSEPK/gcvH2`, `METEA/gcvH`, `human/GCSH`. These
gain scope (not lose it) when the definition broadens — `human/GCSH` already
argues in its review text that `GO:0009249` is the better description of its
role, which the broadened definition makes unambiguously correct.

### Related in-repo work

`modules/endogenous_protein_lipoylation.yaml` is grounded on `GO:0009249` as its
source term and models the direct `LipB`–`LipA` route plus the Bacillus `GcvH`-relay
and human variants. The broadened definition **strengthens** that module's
framing; no change is required, but the module is the natural place to record
the merge. See also
[PSEPK ppu00785 endogenous protein lipoylation batch](P_PUTIDA/batches/ppu00785_lipoate_installation.md).

## Scope

- **Organisms**: bacteria-dominant (*B. subtilis* 5 EXP annotations, *E. coli* 2,
  *M. tuberculosis* 1), plus human, mouse, *D. melanogaster*, and
  *S. cerevisiae*. In-repo affected reviews are POPTR (3), BACSU (1), PSEPK (1).
- **GO branch**: BP only. No MF term is obsoleted — `GO:0016992 lipoate synthase
  activity` and the octanoyltransferase MFs are unaffected (though the
  `part_of` edge noted above must be re-pointed).
- **Type of fix**: structural / curation hygiene. The biology is
  uncontroversial and no annotation needs to be rebutted on biological grounds;
  the change removes a redundant BP framing.

## Candidate genes for initial review

Listed in priority order.

1. **BACSU/lipA** (O32129) — highest priority. Already reviewed here **and**
   carries one of the twelve upstream experimental annotations (IGI,
   PMID:19820084). The review's `core_functions` block needs the redundant
   `GO:0009107` entry dropped.
2. **POPTR/LIP1, LIP1P-1, LIP1P-2** (B9H5L9 and paralogues) — already reviewed;
   mechanical `core_functions` edits plus a note on the two IBA/IEA
   `existing_annotations`. The IBA descends from `MGI:1934604` (mouse *Lias*),
   which is upstream item #12, so these move together.
3. **PSEPK/lipA** (Q88DM5) — already reviewed; `existing_annotations` only, no
   `core_functions` change needed.
4. **B. subtilis `lipM` (P54511), `lipL` (P39648), `gcvH` (O32174)** — not yet in the
   repo. Four of the twelve upstream experimental annotations sit on these three
   proteins, and together they define the GcvH-relay route that motivates the
   merge. Reviewing them would give this repo the clearest worked example of why
   `lipoate biosynthetic process` was the wrong framing.
5. **human LIPT2 (A6NK58)** — not yet in the repo. Human octanoyltransferase;
   PMID:28757203 is a disease-gene paper, and human LIPT1/LIPT2/LIAS are a
   coherent trio for a future human lipoylation review set.
6. **E. coli `lipA` (P60716) / `lipB` (P60720)** — not yet in the repo. The
   canonical two-step pathway; both annotations use
   `acts_upstream_of_or_within` and would benefit from a relation review at the
   same time.

## Proposed approach

1. ~~**Wait for the merge to land before editing gene reviews.**~~ **Done** —
   the obsoletion landed upstream on 2026-08-22 (verified via live QuickGO on
   2026-08-30), so the wait ended.
2. **Comment upstream on the `GO:0016992 part_of GO:0009107` edge**, which is
   the one structural detail neither issue mentions. Still open — `GO:0016992`
   remains live and is still the `core_functions` MF in POPTR/LIP1 and
   LIP1P-1, unaffected by the BP obsoletion.
3. ~~**When the merge lands**, drop the redundant `GO:0009107` entry from the
   four `core_functions` blocks and re-run `just validate`.~~ **Done
   2026-08-30** (PR #2784): all four `core_functions` entries dropped, the
   `existing_annotations` rows switched to MODIFY → `GO:0009249`, and the
   `cache/ontologies/go.tsv` row refreshed to the obsolete state; all five
   reviews validate with 0 errors and 0 warnings. **Remaining sub-step:**
   re-fetch GOA for the five affected genes once GOA itself catches up with the
   merge, so `existing_annotations` picks up the replacement term.
4. **Optionally extend coverage** to the *B. subtilis* GcvH-relay trio
   (`lipM`, `lipL`, `gcvH`), which is the most instructive untouched cluster on the
   upstream list. Still open.

## Priority

Medium. Higher than most obsoletion projects in this repo because five existing
reviews are directly affected and four contain author-supplied `core_functions`
ids that must change — but not urgent, since the ontology ticket is still open
and only MGI has marked its annotations done upstream.

## Status

- 2026-08-30 — **Obsoletion confirmed landed; in-repo migration applied**
  (PR #2784, POPTR knowledge-base re-review). Live QuickGO returns
  `isObsolete: true` and `replaced_by GO:0009249` for `GO:0009107`, with the
  comment "The reason for obsoletion is that the term usage has been
  inconsistent" and ontology edits timestamped 2026-08-22. All five affected
  reviews migrated: the redundant `GO:0009107` entries dropped from the four
  `core_functions` blocks (POPTR/LIP1, LIP1P-1, LIP1P-2, BACSU/lipA), and every
  `existing_annotations` row carrying the term (including the BACSU/lipA IGI,
  upstream experimental item #2) switched to MODIFY → `GO:0009249` with reasons
  recording the obsoletion; the `cache/ontologies/go.tsv` row refreshed to
  `obsolete lipoate biosynthetic process` / `True`. Remaining: the upstream
  `GO:0016992 part_of` edge comment (approach step 2), a GOA re-fetch for the
  five genes once GOA catches up, and the optional GcvH-relay trio reviews
  (step 4).
- 2026-08-15 — Project file created. Tracking go-annotation#6505 (opened
  2026-08-14) and go-ontology#32418 (opened 2026-08-06, open). Obsoletion not
  yet applied. `GO:0009107` and `GO:0009249` both confirmed live in OLS; the 12
  experimental annotations and the `GO:0016992` `part_of` child confirmed via
  QuickGO; all five InterPro entries confirmed via the InterPro REST API.
  Upstream, only MGI has marked its annotation done.
