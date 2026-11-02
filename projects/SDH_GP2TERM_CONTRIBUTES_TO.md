---
title: "Succinate Dehydrogenase (Complex II) — gp2term Relation Review (`enables` → `contributes_to`)"
maturity: IN_PROGRESS
last_reviewed: 2026-10-05
tags: [PIPELINE, FLAGSHIP]
species: [human, 9POAL, PSEPK]
genes: [SDHA, SDHB, SDHC, SDHD, NCGR_LOCUS67308, sdhA, sdhB, sdhC, sdhD]
sidecars:
  slide_figures:
    - SDH_GP2TERM_CONTRIBUTES_TO/slides/complex-ii-relations.svg
    - SDH_GP2TERM_CONTRIBUTES_TO/slides/qualifier-audit.svg
manifest:
  slides:
    - href: SDH_GP2TERM_CONTRIBUTES_TO/slides/SDH_GP2TERM_CONTRIBUTES_TO-slides.html
      description: AI generated
---

# Succinate Dehydrogenase (Complex II) — gp2term Relation Review (`enables` → `contributes_to`)

**Bottom line:** succinate dehydrogenase (respiratory complex II) is a
four-subunit enzyme, and no single subunit carries out the whole
succinate-to-quinone reaction (GO:0008177). GO has agreed
(go-annotation#6414) that each subunit should link to that activity with
`contributes_to` rather than `enables`. The first repo audit found five
reviews carrying GO:0008177: human SDHA, SDHB, SDHC, SDHD and one 9POAL
plant iron-sulfur-subunit ortholog, NCGR_LOCUS67308. Those five all argue for
`contributes_to` in prose. At that 2026-09-26 audit, only SDHC and one SDHA row
carried the structured `qualifier: contributes_to` field, and in both cases
that qualifier comes from GOA itself, not from a curation edit.
[PR #3223](https://github.com/ai4curation/ai-gene-review/pull/3223) (merged
2026-09-27) fixed SDHB and SDHD by marking the GOA `enables` GO:0008177 rows
`MODIFY` and pairing them with one `NEW` GO:0008177
`qualifier: contributes_to` row per gene, the relation-only pattern the
validator accepts. Still open in
[#582](https://github.com/ai4curation/ai-gene-review/issues/582): the SDHA
GO:0000104 half-reaction decision, the plant SDH2 ortholog
(NCGR_LOCUS67308), and PSEPK `sdhA`/`sdhB`, which were added later and still
carry GOA `enables` rows on GO:0008177.

The fix matters because a qualifier that lives only in prose is invisible to
any tool that reads the YAML, and SDHA needs a real judgement: its
flavoprotein subunit can run the succinate half-reaction alone, so `enables`
on the parent GO:0000104 may be correct for it.

## Overview

As part of the GO-CAM protein-complex annotation policy, the GO
consortium has agreed that the individual subunits of **respiratory
chain complex II (succinate dehydrogenase)** should all be annotated
to the molecular-function term **GO:0008177 succinate dehydrogenase
(quinone) activity** (and to its parent **GO:0000104 succinate
dehydrogenase activity**) using the **`contributes_to`** qualifier
rather than **`enables`**. No individual subunit carries out the full
succinate → quinone reaction on its own, so `enables` (which asserts
the gene product has the activity independently) is the wrong
gene-product-to-term relation; `contributes_to` (gene product
contributes to a complex-level activity) is correct.

The biology is unchanged — this is a **gp2term relation
(qualifier) correction**, not a term change.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6414](https://github.com/geneontology/go-annotation/issues/6414) — *Review gp2term relations for succinate dehydrogenase activity terms* (opened 2026-05-11; still open as of 2026-10-05).
- Repo tracker: [ai4curation/ai-gene-review#582](https://github.com/ai4curation/ai-gene-review/issues/582) — tracks the repo-side Complex II qualifier cleanup.
- Curator-maintained review spreadsheet: `https://docs.google.com/spreadsheets/d/1h0_fUrGRlDKUyy9o1S3gMuN8XiVJW_3vHwIe5aaP250`
- Upstream progress (issue comments): **CGD done** (@jlewsmith), **TAIR done** (@lreiser), **MGI done** (@LiNiMGI).

## The two MF terms (verified via OLS, 2026-05-19)

| Term | Label | Definition | Notes |
|---|---|---|---|
| GO:0008177 | succinate dehydrogenase (quinone) activity | "the overall reaction of the entire SDH complex": a quinone + succinate = a quinol + fumarate | Leaf term (no children). The whole-complex activity. **Always `contributes_to` for any single subunit.** |
| GO:0000104 | succinate dehydrogenase activity | succinate + acceptor = fumarate + reduced acceptor | Parent of GO:0008177 (generic acceptor; has children). |

Both terms are **active** (not obsolete) in the GO API / OLS as of
2026-05-19. This is purely a qualifier/relation fix; no obsoletion is
involved.

## Complex II subunits

Respiratory chain complex II has four subunits:

| Subunit (human) | Role | Independent activity? |
|---|---|---|
| **SDHA** (flavoprotein, Fp) | FAD-linked catalytic subunit; harbours the succinate → fumarate active site | Can catalyse the succinate → fumarate **half-reaction** alone, but **not** the quinone-coupled GO:0008177 reaction |
| **SDHB** (iron-sulfur, Ip) | [3Fe-4S]/[2Fe-2S]/[4Fe-4S] electron relay | No |
| **SDHC** (cybL, large membrane anchor) | Q-binding site, heme b | No |
| **SDHD** (cybS, small membrane anchor) | Q-binding site, membrane anchor | No |

**Nuance for SDHA:** the upstream blanket "`contributes_to` for
GO:0008177 *and* GO:0000104" applies cleanly to SDHB/SDHC/SDHD. For
**SDHA**, the *complex-level* GO:0008177 (quinone) is unambiguously
`contributes_to`, but the **parent GO:0000104** (succinate +
generic acceptor → fumarate) describes the half-reaction that the Fp
subunit *can* catalyse via its FAD with an artificial acceptor — so
`enables` on GO:0000104 for SDHA specifically is defensible. Reviews
touching SDHA should flag this rather than blindly applying
`contributes_to` to GO:0000104. (This is exactly the kind of
relation judgement this repo is designed to surface.)

## Impact on this repo

Seven review files carry an existing annotation to **GO:0008177**.
Checked `genes/**/*-ai-review.yaml` for GO:0008177 / GO:0000104:

| Gene | File | Term(s) | Current handling | Action needed |
|---|---|---|---|---|
| **SDHC** (human, Q99643) | `genes/human/SDHC/SDHC-ai-review.yaml` | GO:0008177 IEA | Structured **`qualifier: contributes_to`** present; `action: ACCEPT` | ✅ Already aligned with #6414 — exemplar pattern |
| **SDHA** (human, P31040) | `genes/human/SDHA/SDHA-ai-review.yaml` | GO:0008177 IBA | `action: MODIFY` → proposes GO:0000104; one `qualifier: contributes_to` present; prose discusses enables-vs-contributes | Re-check the SDHA/GO:0000104 nuance above; confirm GO:0008177 retains `contributes_to` |
| **SDHB** (human, P21912) | `genes/human/SDHB/SDHB-ai-review.yaml` | GO:0008177 IEA + 2 IMP | At audit: prose-only, `action: ACCEPT`, no structured qualifier. Since [PR #3223](https://github.com/ai4curation/ai-gene-review/pull/3223): the three GOA `enables` rows are `MODIFY`, plus a paired `NEW` row with `qualifier: contributes_to` (IDA, PMID:37098072) | ✅ Done in #3223 (merged 2026-09-27); re-fetch once GOA reflects #6414 |
| **SDHD** (human, O14521) | `genes/human/SDHD/SDHD-ai-review.yaml` | GO:0008177 IEA (GOA qualifier `enables`) | At audit: prose-only, `action: ACCEPT`, no structured qualifier. Since [PR #3223](https://github.com/ai4curation/ai-gene-review/pull/3223): the GOA `enables` row is `MODIFY`, plus a paired `NEW` row with `qualifier: contributes_to` (IDA, PMID:37098072) | ✅ Done in #3223 (merged 2026-09-27); re-fetch once GOA reflects #6414 |
| **NCGR_LOCUS67308** (9POAL plant SDH2 iron-sulfur ortholog) | `genes/9POAL/NCGR_LOCUS67308/NCGR_LOCUS67308-ai-review.yaml` | GO:0008177 IEA | `action: MODIFY` → GO:0009055; uses core-function `contributes_to_molecular_function`; prose says "contributes to" | Decide explicitly whether to retain MODIFY → GO:0009055 or instead keep GO:0008177 with `qualifier: contributes_to` |
| **sdhA** (PSEPK, Q88FA7) | `genes/PSEPK/sdhA/sdhA-ai-review.yaml` | GO:0008177 IEA | GOA row still has `qualifier: enables`; `action: MARK_AS_OVER_ANNOTATED`; core function uses GO:0000104 plus `contributes_to_molecular_function: GO:0008177` | Bring into #6414 pattern; decide whether the GOA row should become `MODIFY` + paired `NEW` `contributes_to`, as in SDHB/SDHD |
| **sdhB** (PSEPK, Q88FA8) | `genes/PSEPK/sdhB/sdhB-ai-review.yaml` | GO:0008177 IEA | GOA row still has `qualifier: enables`; `action: ACCEPT`; core function uses electron transfer activity plus `contributes_to_molecular_function: GO:0008177` | Bring into #6414 pattern; likely same relation-only correction as human SDHB |

> `genes/PSEPK/sdhC` and `genes/PSEPK/sdhD` mention GO:0008177 only under
> `core_functions.contributes_to_molecular_function`, not as existing GOA rows;
> they are already modelled correctly for this issue. `genes/DESVH/Q72DT2`
> matches GO:0000104 because TreeGrafter propagated succinate dehydrogenase
> activity to the wrong `SdhA`/FrdA-family protein, but that row is already
> `REMOVE`; it is a false positive, not an unresolved SDH qualifier case.

The substantive finding: the qualifier intent was discussed in prose
in the original five human and 9POAL reviews but the **structured
`qualifier: contributes_to` field was applied inconsistently** (present
on SDHC and one SDHA entry; missing on SDHB and SDHD until #3223).
The follow-up is a small, well-defined **consistency pass**, not new
biology.

## Scope

- **Organisms in this repo**: human (SDHA/SDHB/SDHC/SDHD) plus one
  plant SDH2 ortholog (9POAL) and the *Pseudomonas putida* KT2440
  SdhABCD reviews that now exist under `genes/PSEPK/`. Other MOD
  orthologs (CGD/TAIR/MGI/yeast SDH1–4/E. coli sdhCDAB) are handled
  by their respective groups upstream and are **not** reviewed in
  this repo.
- **GO branch**: MF only — GO:0008177 and its parent GO:0000104.
- **Type of fix**: gp2term relation/qualifier (`enables` →
  `contributes_to`). No term changes, no obsoletion.
- **Classification**: **Type B** (systematic, gene-family-wide
  relation correction).

## Candidate genes for follow-up review

All scoped genes are already in the repo — this is a refresh/consistency
pass, not new reviews. Re-pull only if upstream qualifier changes
have propagated to GOA: `just fetch-gene human SDHB` etc.

### Tier 1 — concrete consistency fixes (clear, low-judgement)

1. **SDHB** (human, P21912) — ✅ done in [PR #3223](https://github.com/ai4curation/ai-gene-review/pull/3223) (merged 2026-09-27): the three GOA
   `enables` GO:0008177 rows (one IEA, two IMP) are `MODIFY` with
   GO:0008177 as the proposed replacement, and a `NEW` GO:0008177 row
   carries `qualifier: contributes_to` (IDA, PMID:37098072).
2. **SDHD** (human, O14521) — ✅ done in #3223, same pattern for its
   one IEA row.

Note: `qualifier` on an existing annotation mirrors the GOA row
(`SDHC-goa.tsv` itself ships `contributes_to`; `SDHB-goa.tsv` and
`SDHD-goa.tsv` ship `enables`), so on the SDHB/SDHD GOA rows the
qualifier is written to match GOA (`enables`), not overridden;
an override would be overwritten by `just fetch-gene`. The intended
relation is recorded as a `MODIFY` on each `enables` row plus a paired
`NEW` `contributes_to` row, which is the combination the validator
accepts. Once GOA reflects #6414, re-fetch and the paired rows collapse
into the GOA rows.

### Tier 2 — verify / nuance

3. **SDHA** (human, P31040) — re-examine the GO:0000104-vs-GO:0008177
   split per the SDHA nuance above. Confirm GO:0008177 is
   `contributes_to`; decide explicitly whether GO:0000104 (FAD
   half-reaction) is `enables` for the Fp subunit and document the
   reasoning.
4. **NCGR_LOCUS67308** (9POAL SDH2) — decide between two curation
   strategies: keep the current MODIFY → GO:0009055 electron transfer
   activity replacement, or revise the existing-annotation review to
   retain GO:0008177 with structured `qualifier: contributes_to`. Do
   not simply add a qualifier if the MODIFY-to-GO:0009055 strategy
   remains the intended review outcome.
5. **PSEPK `sdhA` and `sdhB`** — update the GOA `enables`
   GO:0008177 rows to the #6414 relation-only pattern. `sdhC` and
   `sdhD` do not have GOA GO:0008177 rows and already capture their
   Complex II contribution in `core_functions`.

### Reference exemplar (no action)

6. **SDHC** (human, Q99643) — already correctly uses `qualifier:
   contributes_to` with `action: ACCEPT`. Use as the template for
   the others.

## Proposed approach

1. **Hold as a tracking project.** Upstream #6414 is being worked
   group-by-group (CGD/TAIR/MGI done as of 2026-05-18); the GOA
   qualifier changes for human SDH subunits may not yet have
   propagated. Doing the consistency pass now risks re-pulling GOA
   that still shows `enables`.
2. **Tier 1** on SDHB and SDHD is done (#3223, `MODIFY` + paired
   `NEW` `contributes_to` rows). When GOA reflects the upstream change,
   re-fetch both and re-run `just validate human SDHB` /
   `just validate human SDHD`.
3. Do the **Tier 2** SDHA/9POAL/PSEPK checks, explicitly documenting
   the SDHA GO:0000104 half-reaction nuance and applying the paired
   `MODIFY` + `NEW` pattern to PSEPK `sdhA` and `sdhB`.
4. Do **not** create reviews for non-repo MOD orthologs — those are
   owned by the upstream groups.

## Priority

**Low–Medium.** Small, well-bounded scope (6 genes needing a
structured-field consistency edit or explicit relation decision, of
which SDHB and SDHD are done in #3223; SDHC is already correct). No new
biology and no obsoletion — the substantive value is making the
repo's gp2term qualifiers internally consistent and aligned with the
upstream Complex II policy decision. Good low-risk follow-up once the
upstream qualifier change propagates.

## Status

- 2026-05-19 — Project file created. Upstream go-annotation#6414
  open (last updated 2026-05-18; CGD/TAIR/MGI done upstream).
  GO:0008177 and GO:0000104 both verified active (not obsolete) via
  OLS. Five repo genes carry GO:0008177; structured `contributes_to`
  qualifier present on SDHC (and one SDHA entry) but missing on
  SDHB/SDHD — held as a tracking project with a defined Tier 1/Tier 2
  consistency pass. No gene reviews edited yet.
- 2026-09-27 — SDHB and SDHD edited in
  [PR #3223](https://github.com/ai4curation/ai-gene-review/pull/3223)
  (merged 2026-09-27): GOA `enables` GO:0008177 rows → `MODIFY`, each gene gains a paired
  `NEW` GO:0008177 `contributes_to` row (IDA, PMID:37098072). Open:
  SDHA GO:0000104, 9POAL NCGR_LOCUS67308, PSEPK `sdhA`/`sdhB`.
- 2026-10-05 — Re-checked all current GO:0008177 / GO:0000104 review
  hits. Confirmed PSEPK `sdhA` and `sdhB` are unresolved GOA-row cases,
  while PSEPK `sdhC`/`sdhD` only mention GO:0008177 in core functions
  and DESVH `aprA` is a false-positive GO:0000104 propagation that the
  review already removes.
