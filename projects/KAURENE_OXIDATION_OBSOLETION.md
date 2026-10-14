---
title: "Ent-Kaurene Oxidation to Kaurenoic Acid — Obsoletion & Replacement"
maturity: SCOPING
last_reviewed: "2026-10-04"
tags: [OBSOLETION, FLAGSHIP]
species: [ARATH, ORYSJ]
sidecars:
  slide_assets:
    - KAURENE_OXIDATION_OBSOLETION/slides/ko-reaction.svg
    - KAURENE_OXIDATION_OBSOLETION/slides/term-map.svg
manifest:
  slides:
    - href: KAURENE_OXIDATION_OBSOLETION/slides/KAURENE_OXIDATION_OBSOLETION-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/5BmmH5Vkxba1QVEiczUKnU
      title: Project brief
---

# Ent-Kaurene Oxidation to Kaurenoic Acid — Obsoletion & Replacement

**Bottom line:** GO has obsoleted the process term GO:0010241 *ent-kaurene
oxidation to kaurenoic acid*, which restated the three oxidations carried out
by one enzyme, ent-kaurene oxidase. Its process content maps to GO:0009686
*gibberellin biosynthetic process*, and its catalytic content already has the
function term GO:0052615 *ent-kaurene oxidase activity*. The two experimental
rows and the one InterPro2GO mapping the obsoletion touched have now been
handled upstream: QuickGO no longer returns GO:0010241 for Arabidopsis KO or
rice CYP701A6, and the current InterPro2GO release maps IPR044225 to
GO:0052615 and GO:0009686 instead. Neither gene has a review in this repo, so
there is no local GO:0010241 row to migrate; reviewing Arabidopsis KO remains
an optional positive-control exercise for the GO:0009686 / GO:0052615 pairing.

## Overview

GO obsoleted `GO:0010241 ent-kaurene oxidation to kaurenoic acid`, a BP
describing three successive oxidations of the 4-methyl group of ent-kaurene.
The upstream rationale is that the experimental data behind the term is
adequately captured by the broader BP
`GO:0009686 gibberellin biosynthetic process`, and that any catalytic-activity
content already has a dedicated MF — `GO:0052615 ent-kaurene oxidase activity`
— which is unaffected by this obsoletion.

This project tracks the two experimental annotations called out on the
upstream list and the one InterPro2GO mapping from IPR044225. UniProt and TAIR
are marked `DONE` on the go-annotation issue, InterPro reported that it had
removed the obsolete mapping in August 2026, and the live GOA / InterPro feeds
now reflect those changes. The go-annotation tracker itself remains open, so
this page is primarily a status record for the AI Gene Review obsoletion log.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6433](https://github.com/geneontology/go-annotation/issues/6433)
- Ontology ticket: [geneontology/go-ontology#32078](https://github.com/geneontology/go-ontology/issues/32078)

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| ent-kaurene oxidation to kaurenoic acid | GO:0010241 | GO:0009686 gibberellin biosynthetic process (BP); MF content moves to GO:0052615 ent-kaurene oxidase activity |

Term status rechecked in QuickGO on 2026-10-04:
- `GO:0010241` (`obsolete ent-kaurene oxidation to kaurenoic acid`) — obsolete; its obsoletion comment points to `GO:0009686`.
- `GO:0009686` (`gibberellin biosynthetic process`) — live BP replacement.
- `GO:0052615` (`ent-kaurene oxidase activity`) — live MF (EC 1.14.14.86); not part of the obsoletion. SJM's comment on the upstream issue effectively treats `GO:0010241` as a redundant restatement of MF + BP.

SJM's initial triage on the two experimental annotations (paraphrased from
go-annotation#6433) was:

- PMID:22487175 (CYP701A6, Q5Z5R4) — only shows enzyme activity assays. No BP
  evidence in the paper. SJM suggests "just removed" rather than remapped.
- PMID:9671797 (KO, Q93ZB2) — ga3-1 mutant deficient in ent-kaurene oxidase
  activity, framed in the abstract as "the first cytochrome P450-mediated
  step in the gibberellin biosynthetic pathway". SJM suggests remapping to
  GO:0009686.

After obsoletion, the live GOA feed landed slightly differently: the rice
PMID:22487175 IDA row was automatically replaced onto `GO:0009686`, and the
Arabidopsis PMID:9671797 row is now on `GO:0052615`. In both cases,
`GO:0010241` is gone from QuickGO for the affected accession.

## Affected experimental annotations (upstream list)

| # | Source | Accession | Symbol | Taxon | PMID | Evidence | Notes |
|---|---|---|---|---|---|---|---|
| 1 | UniProt | UniProtKB:Q5Z5R4 | CYP701A6 | NCBITaxon:39947 (Oryza sativa Japonica Group) | PMID:22487175 | IDA | Rice ent-kaurene oxidase 2 (EC 1.14.14.86). The paper is an enzyme assay; the obsolete GO:0010241 row is gone from QuickGO and UniProt accepted the automatic replacement onto GO:0009686, preserving the PMID:22487175 IDA row. |
| 2 | TAIR | UniProtKB:Q93ZB2 / AT5G25900 | KO (GA3, CYP701A3, KO1) | NCBITaxon:3702 (Arabidopsis thaliana) | PMID:9671797 | IMP | Arabidopsis ent-kaurene oxidase, chloroplastic (EC 1.14.14.86). The ga3-1 mutant phenotype supports KO's role in gibberellin biosynthesis; the obsolete GO:0010241 row is gone from QuickGO and PMID:9671797 now supports GO:0052615 there. |

Group impact tally (from upstream): UniProt 1 (DONE), TAIR 1 (DONE).

## Mappings flagged for redirection

The current `interpro2go` file maps `InterPro:IPR044225` (Ent-kaurene oxidase,
chloroplastic — plant KO family, including AtKO1) to `GO:0052615 ent-kaurene
oxidase activity` and `GO:0009686 gibberellin biosynthetic process`, plus the
generic cytochrome-P450 MF terms `GO:0005506 iron ion binding` and
`GO:0020037 heme binding`. It no longer points at obsolete `GO:0010241`,
matching InterPro's 2026-08-12 comment that the old term had been removed from
IPR044225.

No UniRule, HAMAP, or UniProt-Keywords mappings to `GO:0010241` were listed by
upstream.

## Impact on this repo

Neither affected gene currently has an `*-ai-review.yaml` in this repo
(rechecked via gene/accession search on 2026-10-04). This project is therefore
a queueing exercise rather than a re-review of existing files. Both
experimental rows are already actioned in the live GOA feed, and IPR044225 is
redirected in the current InterPro2GO release, so the value of pulling these
into AI Gene Review is low relative to open obsoletion projects. The genes
themselves remain scientifically clean examples of plant gibberellin
biosynthesis enzymes and would be useful as optional positive controls for
GO:0009686 / GO:0052615 annotation.

## Scope

- Organism: Arabidopsis thaliana (KO, Q93ZB2) and Oryza sativa Japonica Group
  (CYP701A6, Q5Z5R4). Plant gibberellin biosynthesis — both proteins are
  CYP701-family cytochromes P450 catalysing the three sequential oxidations of
  ent-kaurene to kaurenoic acid.
- GO branch: BP (gibberellin biosynthetic process). The MF side
  (`GO:0052615 ent-kaurene oxidase activity`) is the natural home for the
  catalytic content formerly described by `GO:0010241`.
- Type of fix: structural / curation hygiene. The biology is uncontroversial;
  the obsoletion is about removing a hybrid term whose BP framing actually
  conflated three successive catalytic steps. No annotations need to be
  rebutted on biological grounds; the question is just which of MF
  (`GO:0052615`) and BP (`GO:0009686`) is the right home for each evidence
  record.

## Candidate genes for initial review

Listed in priority order. Both are optional given the upstream DONE markers and
the now-completed InterPro2GO redirect.

1. **KO / GA3 (Arabidopsis, Q93ZB2)** — Higher-value review candidate of the
   two. The PMID:9671797 paper is foundational for the gibberellin biosynthesis
   pathway in plants and the gene already carries `GO:0009686 IDA` from TAIR.
   A review would mostly serve as a positive-control example for the
   `GO:0009686` + `GO:0052615` pairing.
2. **CYP701A6 (Oryza sativa, Q5Z5R4)** — Rice ent-kaurene oxidase 2. Less
   pressing because the live GOA feed already has `GO:0052615` from
   PMID:22487175, the same enzyme-assay paper that originally supported the
   obsolete process row.

## Proposed approach

1. **No local GO:0010241 migration is needed.** QuickGO no longer returns the
   obsolete term for Q93ZB2 or Q5Z5R4, and neither gene has a local review row.
2. **Treat the IPR044225 InterPro2GO mapping as handled.** The current mapping
   points to `GO:0052615 ent-kaurene oxidase activity` and `GO:0009686
   gibberellin biosynthetic process`, not to obsolete `GO:0010241`.
3. **If plant positive-control reviews are queued**, start with Arabidopsis KO
   (Q93ZB2). The biology is canonical and well-supported; the review can serve
   as a positive-control example for ent-kaurene-oxidase-family annotations
   after the obsoletion.

## Priority

Very low — both impacted curation groups are marked DONE upstream, live GOA no
longer serves the obsolete term for either accession, and the InterPro2GO
mapping redirect has landed.

## Status

- 2026-05-27 — Project file created. Tracking go-annotation#6433 (opened
  2026-05-26) and go-ontology#32078. Obsoletion not yet applied. UniProt and
  TAIR marked DONE for the two affected experimental annotations. No
  AI Gene Review files exist for either gene. OLS confirms GO:0010241,
  GO:0009686, and GO:0052615 are all currently live; InterPro IPR044225
  confirmed via REST.
- 2026-09-26 — OLS now returns GO:0010241 as obsolete, with the reason
  pointing to GO:0009686. Still no AI Gene Review files for either gene.
- 2026-10-04 — QuickGO no longer returns GO:0010241 for KO/Q93ZB2 or
  CYP701A6/Q5Z5R4. The current InterPro2GO release maps IPR044225 to
  GO:0052615 and GO:0009686 instead of GO:0010241.
