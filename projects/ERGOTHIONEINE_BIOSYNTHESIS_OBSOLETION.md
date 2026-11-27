---
title: "Ergothioneine Biosynthesis Variant-Pathway Terms — Obsoletion"
maturity: SCOPING
last_reviewed: 2026-10-04
tags: [OBSOLETION]
species: [MYCS2]
manifest:
  slides:
    - href: ERGOTHIONEINE_BIOSYNTHESIS_OBSOLETION/slides/ERGOTHIONEINE_BIOSYNTHESIS_OBSOLETION-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/UgnTdyckzfeHaC4cu2CbXT
      title: Project brief
---

# Ergothioneine Biosynthesis Variant-Pathway Terms — Obsoletion

**Bottom line:** GO has retired the two route-specific children of
GO:0052699 *ergothioneine biosynthetic process*: the bacterial route
GO:0052704 (via gamma-glutamyl-hercynylcysteine sulfoxide) and the fungal
route GO:0140479. Which intermediates a pathway passes through is detail
GO now leaves to MetaCyc and GO-CAMs, so all annotations move to the
parent. The May 2026 migration snapshot had four UniProt IDA rows, one per
enzyme of the *Mycolicibacterium smegmatis* *egtBCDE* operon, all from
PMID:20420449, plus about 2,247 IEA rows to regenerate automatically.
GO:0052704 is now obsolete as well as GO:0140479, and both upstream tickets
are closed. As of 2026-10-04, no gene review in this repo uses GO:0052704,
GO:0140479 or GO:0052699, and none of the *egt* genes is reviewed. Scoped,
not yet started: the four-enzyme operon is a compact batch to add if the
repo wants mycobacterial pathway coverage.

## Overview

A GO obsoletion retires the two variant-pathway children of
GO:0052699 ergothioneine biosynthetic process. These children encode
*how* ergothioneine is made (bacterial vs fungal route), which is a
level of pathway-variant detail that upstream curators have decided is
beyond GO scope (better captured by MetaCyc pathways or GO-CAMs). All
affected annotations move to the parent term.

- **GO:0052704 ergothioneine biosynthesis from histidine via gamma-glutamyl-hercynylcysteine sulfoxide** (BP, bacterial route, obsolete)
- **GO:0140479 ergothioneine biosynthesis from histidine via hercynylcysteine sulfoxide synthase** (BP, fungal route, obsolete)

Both replaced by:

- **GO:0052699 ergothioneine biosynthetic process** (BP, active)

Per the upstream ontology decision, the two MetaCyc variant pathways
(`MetaCyc:PWY-7255` ergothioneine biosynthesis I (bacteria) and
`MetaCyc:PWY-7550` ergothioneine biosynthesis II (fungi)) are added as
`narrowMatch` cross-references on GO:0052699 rather than being
preserved as distinct GO classes.

This project tracks the impact on AI Gene Review. No genes in scope are
currently reviewed here.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6402](https://github.com/geneontology/go-annotation/issues/6402) — **closed 2026-05-26**; UniProt marked done
- Ontology ticket: [geneontology/go-ontology#32018](https://github.com/geneontology/go-ontology/issues/32018) — **closed 2026-05-11**
- Earlier note on the same problem: [geneontology/go-ontology#11163](https://github.com/geneontology/go-ontology/issues/11163)
- Affected annotations spreadsheet: [Google Sheet](https://docs.google.com/spreadsheets/d/1-DrrK_JPPMuU9Bzlp9jyG9b6bg2LpcDs5N06u2bPF-0/edit?gid=0#gid=0)
- Impacted groups (per upstream issue): UniProt — 4 annotations to GO:0052704, now done

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Status | Replacement |
|---|---|---|---|
| ergothioneine biosynthesis ... via gamma-glutamyl-hercynylcysteine sulfoxide | GO:0052704 | obsolete | GO:0052699 ergothioneine biosynthetic process |
| ergothioneine biosynthesis ... via hercynylcysteine sulfoxide synthase | GO:0140479 | obsolete | GO:0052699 ergothioneine biosynthetic process |

The fungal-route term GO:0140479 carried **zero** direct experimental
annotations, so it was obsoleted directly. The bacterial-route term
GO:0052704 stayed active until four UniProt experimental annotations
and a large IEA pool could be migrated to GO:0052699; UniProt marked
that migration done and go-annotation#6402 closed on 2026-05-26.
The current GO release marks both route-specific terms `is_obsolete:
true` with `replaced_by: GO:0052699`.

## Affected experimental annotations (May 2026 migration snapshot)

Before GO:0052704 was obsoleted, all four direct experimental
annotations were on genes of the *Mycolicibacterium smegmatis* mc(2)155
*egt* operon, all IDA (ECO:0000314), all from the same study
(PMID:20420449, the in vitro reconstitution of the mycobacterial
ergothioneine pathway), all assigned by UniProt, qualifier
`involved_in`.

| Gene | UniProt | Locus | Protein name | Taxon |
|---|---|---|---|---|
| egtB | A0R5N0 | MSMEG_6249 | Hercynine oxygenase (sulfoxide synthase) | NCBITaxon:246196 |
| egtC | A0R5M9 | MSMEG_6248 | Gamma-glutamyl-hercynylcysteine sulfoxide hydrolase | NCBITaxon:246196 |
| egtD | A0R5M8 | MSMEG_6247 | Histidine N-alpha-methyltransferase | NCBITaxon:246196 |
| egtE | A0R5M7 | MSMEG_6246 | Hercynylcysteine sulfoxide lyase | NCBITaxon:246196 |

NCBITaxon:246196 = *Mycolicibacterium smegmatis* (strain ATCC 700084 /
mc(2)155); UniProt mnemonic suffix `MYCS2`.

Each annotation simply moves to **GO:0052699 ergothioneine
biosynthetic process** — the obsoletion is terminological, not a change
of biology. The four enzymes catalyze consecutive steps of the same
pathway, so the parent BP term is the correct shared placement.

### IEA pool (auto-migrated)

The pre-obsoletion GO:0052704 snapshot also carried roughly **2,247
IEA annotations** (mostly `egtB` orthologs across bacteria) assigned via
`GO_REF:0000108` (automatic logical inference). These regenerate against
GO:0052699 through the automatic inference pipeline — no per-annotation
work is needed here.

### Parent-term annotations (unaffected)

GO:0052699 already carries 2 direct experimental annotations —
*Schizosaccharomyces pombe* `egt1` (O94632) and `egt2` (O94431), both
IMP from PMID:24828577. These are on the surviving parent term and are
**not** affected by the obsoletion. The repo also has the production
GO-CAM for the parent pathway under `gocams/68b0f0d000008187/`, with
PomBase `egt1` and `egt2` activity nodes, but not matching gene reviews.

## Impact on this repo

No genes from the GO:0052704 / GO:0140479 migration snapshot are
currently reviewed in this repo:

- `genes/MYCS2/` — does not exist; no *M. smegmatis* mc(2)155 genes are
  reviewed. The only *M. smegmatis* review is `genes/MYCSM/arr/` (O67972,
  generic taxon 1772), which is unrelated to ergothioneine.
- `genes/SCHPO/egt1/`, `genes/SCHPO/egt2/` — do not exist

So **no existing review needs a refresh** for the obsoletion itself.
The opportunity is that the *M. smegmatis* *egt* operon is a compact,
well-characterized four-enzyme biosynthetic pathway with no coverage in
this repo, and the obsoletion is a natural trigger to add it.

## Scope

- **Organisms**: the four directly affected genes are all
  *M. smegmatis* mc(2)155. The fungal route (S. pombe egt1/egt2) is on
  the surviving parent term and is opportunistic, not required.
- **GO branches**: BP only — a variant-pathway-specificity collapse to
  the broader parent term. No MF or CC changes.
- **Type of fix**: terminological — the chemistry (histidine →
  ergothioneine) is unchanged. Reviews would confirm GO:0052699 is the
  right BP anchor and that each enzyme also has a precise cognate MF.

## Candidate genes for initial review

Verify each with `just fetch-gene MYCS2 <gene>` before starting and
confirm UniProt accessions. **Species folder:** use `MYCS2`, not the
existing `MYCSM`. The four accessions are strain mc(2)155 entries
(e.g. EGTB_MYCS2, A0R5N0, taxon 246196), and the repo already files
strain-specific UniProt mnemonics beside generic ones (`PSEAE` beside
`PSEAI`, `ECOLI` beside `ECOLX`). `MYCSM` is the generic taxon-1772 code
used by the `arr` review. None are currently in the repo. The four
genes form one operon and are best reviewed together as a small batch.

### Tier 1 — direct experimental annotation, well-characterized

1. **egtD / A0R5M8** (MSMEG_6247) — histidine N-alpha-methyltransferase;
   catalyzes the first committed step, SAM-dependent triple methylation
   of L-histidine to hercynine. The cognate MF (a histidine
   N-methyltransferase activity) should anchor the review; BP anchors on
   GO:0052699 post-obsoletion.
2. **egtB / A0R5N0** (MSMEG_6249) — hercynine oxygenase / sulfoxide
   synthase; the signature non-heme-iron enzyme that forms the C–S bond
   between hercynine and cysteine (or gamma-glutamylcysteine). Most
   mechanistically studied step of the pathway.
3. **egtC / A0R5M9** (MSMEG_6248) — gamma-glutamyl-hercynylcysteine
   sulfoxide hydrolase; a glutamine-amidotransferase-class enzyme that
   removes the gamma-glutamyl group.
4. **egtE / A0R5M7** (MSMEG_6246) — hercynylcysteine sulfoxide lyase;
   PLP-dependent C–S lyase that produces ergothioneine in the final
   step.

All four are characterized in PMID:20420449 (Seebeck FP, 2010, *J Am
Chem Soc* — in vitro reconstitution of mycobacterial ergothioneine
biosynthesis), which is the single reference behind every affected
annotation.

### Tier 2 — opportunistic, fungal route

5. **egt1 / O94632** and **egt2 / O94431** (*S. pombe*) — already
   annotated to the surviving parent GO:0052699; not affected by the
   obsoletion. Reviewing them would extend SCHPO coverage but is not
   required by this ticket.

## Proposed approach

1. **Both obsoletions have landed**: GO:0052704 and GO:0140479 now
   resolve as obsolete and are replaced by the parent GO:0052699.
   Reviews for any newly added *egt* genes can simply anchor BP on
   GO:0052699.
2. **Review the four *M. smegmatis* *egt* genes as one batch.** Run
   `just fetch-gene MYCS2 egtD` (and egtB/egtC/egtE), then `/review`
   per CLAUDE.md. Because the four enzymes share one pathway and one
   reference (PMID:20420449), the literature work is largely shared.
3. **For each gene, anchor on the cognate molecular function** — the
   pathway membership (GO:0052699) is the BP; the per-enzyme catalytic
   activity (methyltransferase, oxygenase/sulfoxide synthase,
   amidotransferase/hydrolase, C–S lyase) is the more informative MF
   and should drive `core_functions`. Look up precise MF terms via the
   OLS MCP rather than guessing IDs.
4. **Do not create reviews for the ~2,247 IEA `egtB` orthologs** — they
   are auto-migrated by the logical-inference pipeline.
5. **Defer the S. pombe egt1/egt2 pair** unless SCHPO ergothioneine
   coverage is wanted independently; they are on the surviving parent
   term and unaffected.

## Priority

**Low-medium.** Only four direct experimental annotations are affected
and the upstream migration was mechanical (variant-pathway term
collapsed to its parent). No existing review in this repo is blocked.
The opportunity — not the urgency — is that the *M. smegmatis* *egt*
operon is a clean, fully reconstituted four-enzyme pathway with a
single well-cited reference and no coverage here, making it an
efficient small batch if the repo wants to extend *Mycolicibacterium*
coverage.

## Status

- 2026-10-04 — Confirmed GO:0052704 is now obsolete with replacement
  GO:0052699, and the upstream go-annotation#6402 tracker closed on
  2026-05-26 after UniProt marked its four annotations done. Local
  repo status is unchanged: no `genes/MYCS2/` directory and no SCHPO
  `egt1`/`egt2` reviews exist; the cached PomBase GO-CAM for
  GO:0052699 is present but does not create gene-review coverage.
- 2026-05-21 — Project file created. Upstream annotation issue #6402
  open; ontology ticket #32018 closed. GO:0140479 (fungal route)
  already obsolete; GO:0052704 (bacterial route) still active pending
  migration of 4 UniProt experimental annotations + ~2,247 IEA to the
  parent GO:0052699. No gene reviews started in this repo for the
  *M. smegmatis* egtB/egtC/egtD/egtE operon.
