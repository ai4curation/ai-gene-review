---
title: "Sulfide Oxidation Children — Obsoletion & Replacement"
maturity: IN_PROGRESS
last_reviewed: 2026-10-05
tags: [OBSOLETION]
species: [human]
genes: [SQOR, TSTD1, SLC25A10]
manifest:
  slides:
    - href: SULFIDE_OXIDATION_OBSOLETION/slides/SULFIDE_OXIDATION_OBSOLETION-slides.html
---

# Sulfide Oxidation Children — Obsoletion & Replacement

**Bottom line:** Mitochondria detoxify hydrogen sulfide by oxidising it to
sulfite and sulfate, starting with sulfide:quinone oxidoreductase (SQOR).
GO has obsoleted three children of GO:0019418 *sulfide oxidation* that
named the enzyme used (GO:0070221 via SQOR, GO:0070222 via sulfide
dehydrogenase, GO:0070223 via sulfur dioxygenase), because they were
more specific than any known gene product and two had no annotations.
All three ontology PRs are merged, so annotations now belong on the
parent; Reactome, UniProt, InterPro, MGI, and RGD have all moved or
removed their affected assertions upstream. `human/SLC25A10` has since
been reviewed in another workstream; its GOA file now carries the
Reactome row on GO:0019418, and the review marks it
MARK_AS_OVER_ANNOTATED because the carrier exports sulfate but does not
oxidise sulfide. Human SQOR, the one direct experimentally supported
enzyme annotation on the list, and TAS-only TSTD1 are still unreviewed
here.

## Overview

A GO obsoletion has retired three molecular-mechanism-specific
children of GO:0019418 sulfide oxidation, because they were more
specific than any known gene product and 2 of the 3 had no
annotations. Affected annotations were migrated to the parent term
GO:0019418, with the appropriate substrate/specificity captured in
evidence rather than the term ID.

- **GO:0070221 sulfide oxidation, using sulfide:quinone oxidoreductase** (BP, obsolete)
- **GO:0070222 sulfide oxidation, using sulfide dehydrogenase** (BP, obsolete)
- **GO:0070223 sulfide oxidation, using sulfur dioxygenase** (BP, obsolete)

Replaced by:

- **GO:0019418 sulfide oxidation** (BP)

The textual definition of GO:0019418 was simultaneously updated to
"The chemical reactions and pathways resulting in the conversion of
sulfide to sulfite or sulfate." The MetaCyc cross-references on the
obsoleted children were redirected to GO:0019418
(MetaCyc:P222-PWY, MetaCyc:PWY-5274, MetaCyc:PWY-5285,
MetaCyc:PWY-7927).

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6388](https://github.com/geneontology/go-annotation/issues/6388) — **closed 2026-05-26**
- Ontology ticket: [geneontology/go-ontology#31842](https://github.com/geneontology/go-ontology/issues/31842) — **closed 2026-05-11**
- Ontology obsoletion PRs (all merged):
  - [geneontology/go-ontology#31949](https://github.com/geneontology/go-ontology/pull/31949) — obsoleted GO:0070222 and GO:0070223; moved MetaCyc xrefs and added synonyms (merged 2026-04-22)
  - [geneontology/go-ontology#32025](https://github.com/geneontology/go-ontology/pull/32025) — obsoleted GO:0070221 (merged 2026-05-04)
  - [geneontology/go-ontology#32068](https://github.com/geneontology/go-ontology/pull/32068) — changed textual definition for GO:0019418 (merged 2026-05-11)

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| sulfide oxidation, using sulfide:quinone oxidoreductase | GO:0070221 (obsolete) | GO:0019418 sulfide oxidation |
| sulfide oxidation, using sulfide dehydrogenase | GO:0070222 (obsolete) | GO:0019418 sulfide oxidation |
| sulfide oxidation, using sulfur dioxygenase | GO:0070223 (obsolete) | GO:0019418 sulfide oxidation |

### Affected experimental / direct annotations (GO:0070221 only)

GO:0070222 and GO:0070223 had **zero** direct annotations at
obsoletion time. All affected annotations were on GO:0070221.

| Group | Gene | Species | UniProt | Evidence | Reference / Source | Status |
|---|---|---|---|---|---|---|
| UniProt | **SQOR** | Homo sapiens (NCBITaxon:9606) | Q9Y6N5 | IDA (ECO:0000314) | UniProtKB | moved to GO:0019418; review absent here |
| Reactome | TSTD1 | Homo sapiens (NCBITaxon:9606) | Q8NFU3 | TAS (ECO:0000304) | Reactome | moved to GO:0019418; review absent here |
| Reactome | SLC25A10 | Homo sapiens (NCBITaxon:9606) | Q9UBX3 | TAS (ECO:0000304) | Reactome | moved to GO:0019418; reviewed here as MARK_AS_OVER_ANNOTATED |
| RGD | Sqor | Rattus norvegicus (NCBITaxon:10116) | — | ISO (ECO:0000266) | RGD | moved to GO:0019418 |
| MGI | Sqor | Mus musculus (NCBITaxon:10090) | — | ISS/ISO (ECO:0000250, ECO:0000266) | MGI | moved to GO:0019418 |

A larger pool of **IBA (ECO:0000318)** annotations propagated from
PANTHER will be remapped to GO:0019418 automatically once the next
PAINT/IBA pipeline run picks up the obsoletion. These span SQOR
orthologs across vertebrates (Bos taurus, Gallus gallus, Xenopus
tropicalis, Danio rerio, Anolis carolinensis, gorilla, chimp, etc.),
fungal/protist orthologs (Paramecium tetraurelia, Aspergillus
nidulans, Neurospora crassa, Cryptococcus deneoformans, S. pombe
hmt2, S. japonicus hmt2, Dictyostelium purpureum), bacterial homologs
(Pseudomonas aeruginosa PA2345, Staphylococcus aureus, Chloroflexus
aurantiacus), and a Monosiga brevicollis SQOR. These are
auto-migrated and do not need per-annotation work here.

### InterPro2GO / mapping cleanup (per upstream issue)

- **InterPro:IPR042457** Thiosulfate:glutathione sulfurtransferase,
  mammalian → GO:0070221 — mapping **removed** from InterPro
  (confirmed 2026-05-15 in go-annotation#6388 comments).
- Reactome has already migrated its 2 affected annotations
  (confirmed 2026-04-22 in upstream issue comments).
- UniProt has already migrated its affected annotations
  (confirmed 2026-05-22 in upstream issue comments).
- No ARBA / UniRule mappings to the obsoleted terms were listed.

## Impact on this repo

Only one of the three human genes from the direct-annotation set is
currently reviewed in this repo:

- `genes/human/SQOR/` — not yet present
- `genes/human/TSTD1/` — not yet present
- `genes/human/SLC25A10/` — present; the current GOA already has the
  Reactome TAS row on GO:0019418, and the review marks that row
  MARK_AS_OVER_ANNOTATED because DIC exports a sulfate product but does
  not perform a sulfide-oxidation step
- `genes/PSEAE/PA2345/` — does not exist
- `genes/SCHPO/hmt2/` — does not exist

So **no existing reviews still need refresh** for the obsoletion
itself. The remaining opportunity is that **SQOR is otherwise
unreviewed** in this repo despite being a well-characterized human
mitochondrial sulfide-oxidizing enzyme directly relevant to H2S
signaling, sulfide detoxification, and the inherited mitochondrial
disorder caused by SQOR deficiency (PMID:31108281). TSTD1 is a lower
priority follow-up because the migrated GO:0019418 row is TAS-only and
appears to come from pathway membership rather than direct SQOR-like
oxidoreductase activity.

## Scope

- **Organisms**: primary local candidates are the human direct-set genes. S.
  pombe `hmt2` and the bacterial homologs named below are PAINT/IBA follow-ups
  and can be deferred, while the rodent `Sqor` ISO/ISS rows were upstream-only
  and have already moved.
- **GO branches**: BP only — the obsoletion is a
  mechanism-specificity collapse to the broader parent term. No MF
  or CC changes.
- **Type of fix**: terminological — the biology (sulfide → sulfite/
  sulfate) is unchanged; reviews would evaluate whether GO:0019418
  is the correct BP for SQOR's core function while keeping the
  cognate MF, **GO:0070224 sulfide:quinone oxidoreductase activity**, as
  SQOR's molecular-function anchor.

## Candidate genes for initial review

Verify each missing gene with `just fetch-gene <organism> <gene>`
before starting and confirm UniProt accessions. `human/SLC25A10` is
already reviewed and remains here as a useful negative example: a
carrier can appear in the sulfide-oxidation pathway without itself
being a sulfide-oxidizing enzyme.

### Tier 1 — direct experimental annotation, well-characterized

- **SQOR / Q9Y6N5** (Homo sapiens) — mitochondrial sulfide:quinone
   oxidoreductase, the canonical human enzyme for sulfide oxidation
   in the first step of mitochondrial H2S detoxification. The IDA
   annotation that used to sit on GO:0070221 was the one EXP row that
   the upstream issue flagged for migration; it is now on GO:0019418.
   SQOR also carried a PAINT/IBA row on GO:0070221 that will follow the
   parent term automatically. A review here should anchor the BP on
   GO:0019418 (post-obsoletion) and confirm the MF anchor remains
   GO:0070224 sulfide:quinone oxidoreductase activity. Clinically relevant
   (SQOR deficiency causes Leigh-like mitochondrial encephalopathy).

### Tier 2 — TAS, less direct

- **TSTD1 / Q8NFU3** (Homo sapiens) — thiosulfate sulfurtransferase-
   like domain-containing 1; its migrated TAS annotation on GO:0019418
   comes from the same Reactome pathway as SLC25A10. Its primary
   characterized activity is rhodanese-type
   thiosulfate:glutathione sulfurtransferase (PMID:24107290), and
   InterPro has already removed the IPR042457 → GO:0070221 mapping per
   the upstream issue. A review would assess whether GO:0019418 or a
   different sulfurtransferase BP is the right placement.

### Already reviewed

- **SLC25A10 / Q9UBX3** (Homo sapiens) — mitochondrial
   dicarboxylate carrier; its TAS pathway row has moved to GO:0019418.
   The existing review marks this MARK_AS_OVER_ANNOTATED because DIC
   exchanges sulfate/thiosulfate for phosphate but does not catalyse
   sulfide oxidation.

### Tier 3 — opportunistic, non-human

- **hmt2 / SPBC2G5.06c** (Schizosaccharomyces pombe) — fission yeast
   ortholog in the former PAINT/IBA GO:0070221 set. Would extend SCHPO
   coverage but lower priority since IBA migration is automatic.

## Proposed approach

1. **Obsoletion has landed.** All three terms are obsolete in the
   ontology and the upstream ontology ticket is closed. The
   annotation-migration work in go-annotation#6388 also closed on
   2026-05-26, after Reactome, InterPro, and UniProt finished the
   affected upstream changes.
2. **Start with human SQOR.** Run `just fetch-gene human SQOR` and
   confirm the GOA pull now has GO:0019418 instead of obsolete
   GO:0070221. Review per the gene-review guidelines, paying attention
   to:
    - The cognate MF GO:0070224 sulfide:quinone oxidoreductase activity
      (intact) is the right MF anchor.
    - The BP anchor should be GO:0019418 sulfide oxidation
      (post-obsoletion).
    - SQOR also participates in CoQ/electron-transport context;
      check that any CC/BP claims about mitochondrial ETC
      integration are evidence-backed.
3. **Follow with TSTD1.** Its GO:0019418 row is TAS-only and the
   upstream InterPro2GO mapping (IPR042457 → GO:0070221) has already
   been removed, so review should evaluate whether the process row is
   even the right BP or whether the original TAS was on shaky ground.
4. **Keep SLC25A10 as the comparator.** The existing review already
   makes the same distinction this project needs to police: pathway
   transport of sulfate is not direct participation in sulfide
   oxidation.
5. **Defer S. pombe hmt2 and the bacterial homologs** unless they
   come up via other workstreams; the IBA propagations will be
   auto-migrated.
6. **Do not create reviews for the IBA-only orthologs** listed in
   the PANTHER/IBA paragraph — they will be remapped automatically.

## Priority

**Medium-low.** The direct non-IBA rows were limited and the upstream migration
is already in production. Locally, the remaining human follow-ups are SQOR and
TAS-only TSTD1; SLC25A10 has already been reviewed and rejected as an
over-annotation.

## Status

- 2026-05-15 — Project file created. Upstream annotation issue
  #6388 still open; latest activity was InterPro confirming
  removal of the IPR042457 → GO:0070221 mapping. All three ontology
  obsoletion PRs are merged (#31949, #32025, #32068) and the
  parent ontology ticket #31842 is closed. No gene reviews started
  in this repo for SQOR/TSTD1/SLC25A10.
- 2026-10-04 — Project file refreshed after go-annotation#6388 closed
  and SLC25A10 was reviewed elsewhere. SQOR and TSTD1 are still absent
  locally; `human/SLC25A10` now carries Reactome's GO:0019418 TAS row
  and marks it MARK_AS_OVER_ANNOTATED.
