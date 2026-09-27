---
title: "Succinate Dehydrogenase (Complex II) — gp2term Relation Review (`enables` → `contributes_to`)"
maturity: SCOPING
tags: [PIPELINE, FLAGSHIP]
species: [human, 9POAL]
genes: [SDHA, SDHB, SDHC, SDHD, NCGR_LOCUS67308]
sidecars:
  slide_figures:
    - SDH_GP2TERM_CONTRIBUTES_TO/slides/complex-ii-relations.svg
    - SDH_GP2TERM_CONTRIBUTES_TO/slides/qualifier-audit.svg
---

# Succinate Dehydrogenase (Complex II) — gp2term Relation Review (`enables` → `contributes_to`)

**Bottom line:** succinate dehydrogenase (respiratory complex II) is a
four-subunit enzyme, and no single subunit carries out the whole
succinate-to-quinone reaction (GO:0008177). GO has agreed
(go-annotation#6414) that each subunit should link to that activity with
`contributes_to` rather than `enables`. We audited the repo and found five
reviews carrying GO:0008177: human SDHA, SDHB, SDHC, SDHD and one plant
iron-sulfur-subunit ortholog (9POAL/NCGR_LOCUS67308). All five argue for
`contributes_to` in prose, but only SDHC and one SDHA row carry the
structured `qualifier: contributes_to` field, and in both cases that
qualifier comes from GOA itself, not from a curation edit. Scoped, not yet started: as of
2026-09-26 no review has been edited, and the SDHB (three rows) and SDHD
(one row) fixes are still open. PSEPK sdhA and sdhB reviews added later
also carry GO:0008177 rows with `enables` and are not yet in the table below
(PSEPK sdhC and sdhD mention GO:0008177 only under
`core_functions.contributes_to_molecular_function`, already modelled
correctly, so a plain grep returns nine files, not seven).

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

- Annotation tracker: [geneontology/go-annotation#6414](https://github.com/geneontology/go-annotation/issues/6414) — *Review gp2term relations for succinate dehydrogenase activity terms* (opened 2026-05-11, last updated 2026-05-18; labels: `annotation review`, `annotation relations`).
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

Five reviewed genes carry an existing annotation to **GO:0008177**.
Checked `genes/**/*-ai-review.yaml` for GO:0008177 / GO:0000104:

| Gene | File | Term(s) | Current handling | Action needed |
|---|---|---|---|---|
| **SDHC** (human, P56378) | `genes/human/SDHC/SDHC-ai-review.yaml` | GO:0008177 IEA | Structured **`qualifier: contributes_to`** present; `action: ACCEPT` | ✅ Already aligned with #6414 — exemplar pattern |
| **SDHA** (human, P31040) | `genes/human/SDHA/SDHA-ai-review.yaml` | GO:0008177 IBA | `action: MODIFY` → proposes GO:0000104; one `qualifier: contributes_to` present; prose discusses enables-vs-contributes | Re-check the SDHA/GO:0000104 nuance above; confirm GO:0008177 retains `contributes_to` |
| **SDHB** (human, P21912) | `genes/human/SDHB/SDHB-ai-review.yaml` | GO:0008177 IEA + 2 IMP | Prose says qualifier "should ideally be `contributes_to`"; `action: ACCEPT`; **no structured `qualifier:` field** on any of the three GO:0008177 rows | Add structured `qualifier: contributes_to` to all three GO:0008177 entries |
| **SDHD** (human, O14521) | `genes/human/SDHD/SDHD-ai-review.yaml` | GO:0008177 IEA (GOA qualifier `enables`) | Prose says qualifier "should be `contributes_to`"; `action: ACCEPT`; **no structured `qualifier:` field** | Add structured `qualifier: contributes_to` to the GO:0008177 entry |
| **NCGR_LOCUS67308** (9POAL plant SDH2 iron-sulfur ortholog) | `genes/9POAL/NCGR_LOCUS67308/NCGR_LOCUS67308-ai-review.yaml` | GO:0008177 IEA | `action: MODIFY` → GO:0009055; uses core-function `contributes_to_molecular_function`; prose says "contributes to" | Decide explicitly whether to retain MODIFY → GO:0009055 or instead keep GO:0008177 with `qualifier: contributes_to` |

> `genes/human/NDUFV1` also matched the GO:0008177 grep but only in
> *comparative prose* (NDUFV1 is a Complex I subunit) — **not** an
> SDH annotation, so it is out of scope here.

The substantive finding: the qualifier intent is discussed in prose
in all five reviews but the **structured `qualifier: contributes_to`
field is applied inconsistently** (present on SDHC and one SDHA
entry; missing on SDHB and SDHD). The follow-up is a small,
well-defined **consistency pass**, not new biology.

## Scope

- **Organisms in this repo**: human (SDHA/SDHB/SDHC/SDHD) plus one
  plant SDH2 ortholog (9POAL). Other MOD orthologs
  (CGD/TAIR/MGI/yeast SDH1–4/E. coli sdhCDAB) are handled by their
  respective groups upstream and are **not** reviewed in this repo.
- **GO branch**: MF only — GO:0008177 and its parent GO:0000104.
- **Type of fix**: gp2term relation/qualifier (`enables` →
  `contributes_to`). No term changes, no obsoletion.
- **Classification**: **Type B** (systematic, gene-family-wide
  relation correction).

## Candidate genes for follow-up review

All five are already in the repo — this is a refresh/consistency
pass, not new reviews. Re-pull only if upstream qualifier changes
have propagated to GOA: `just fetch-gene human SDHB` etc.

### Tier 1 — concrete consistency fixes (clear, low-judgement)

1. **SDHB** (human, P21912) — add structured `qualifier:
   contributes_to` to all three GO:0008177 existing-annotation entries
   (one IEA plus two IMP rows); the prose already justifies it.
2. **SDHD** (human, O14521) — same fix; GOA currently has `enables`,
   prose already argues for `contributes_to`.

Note: `qualifier` on an existing annotation mirrors the GOA row
(`SDHC-goa.tsv` itself ships `contributes_to`; `SDHB-goa.tsv` and
`SDHD-goa.tsv` ship `enables`), so a hand edit would be overwritten by
`just fetch-gene`. Until GOA reflects #6414, record the intended
`contributes_to` in each row's `review`, then re-fetch once GOA changes.

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

### Reference exemplar (no action)

5. **SDHC** (human, P56378) — already correctly uses `qualifier:
   contributes_to` with `action: ACCEPT`. Use as the template for
   the others.

## Proposed approach

1. **Hold as a tracking project.** Upstream #6414 is being worked
   group-by-group (CGD/TAIR/MGI done as of 2026-05-18); the GOA
   qualifier changes for human SDH subunits may not yet have
   propagated. Doing the consistency pass now risks re-pulling GOA
   that still shows `enables`.
2. When convenient (or when GOA reflects the upstream change),
   execute the **Tier 1** consistency fixes on SDHB and SDHD: add
   the structured `qualifier: contributes_to` to the GO:0008177
   entry, matching the existing SDHC pattern, and re-run
   `just validate human SDHB` / `just validate human SDHD`.
3. Do the **Tier 2** SDHA/9POAL checks, explicitly documenting the
   SDHA GO:0000104 half-reaction nuance.
4. Do **not** create reviews for non-repo MOD orthologs — those are
   owned by the upstream groups.

## Priority

**Low–Medium.** Small, well-bounded scope (4 genes needing a
structured-field consistency edit; 1 already correct). No new
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

## Slides

- [Slides](SDH_GP2TERM_CONTRIBUTES_TO/slides/SDH_GP2TERM_CONTRIBUTES_TO-slides.html) (Marp source: [SDH_GP2TERM_CONTRIBUTES_TO-slides.md](SDH_GP2TERM_CONTRIBUTES_TO/slides/SDH_GP2TERM_CONTRIBUTES_TO-slides.md)) — AI generated
