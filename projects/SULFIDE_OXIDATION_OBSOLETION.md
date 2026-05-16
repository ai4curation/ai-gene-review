# Sulfide Oxidation Children — Obsoletion & Replacement

## Overview

A GO obsoletion has retired three molecular-mechanism-specific
children of GO:0019418 sulfide oxidation, because they were more
specific than any known gene product and 2 of the 3 had no
annotations. All affected annotations should be migrated to the
parent term GO:0019418 (with the appropriate substrate/specificity
captured in evidence rather than the term ID).

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

- Annotation tracker: [geneontology/go-annotation#6388](https://github.com/geneontology/go-annotation/issues/6388)
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
obsoletion time. All affected annotations are on GO:0070221.

| Group | Gene | Species | UniProt | Evidence | Reference / Source | Status |
|---|---|---|---|---|---|---|
| UniProt | **SQOR** | Homo sapiens (NCBITaxon:9606) | Q9Y6N5 | IDA (ECO:0000314) | UniProtKB | pending move to GO:0019418 |
| UniProt | TSTD1 | Homo sapiens (NCBITaxon:9606) | Q8NFU3 | TAS (ECO:0000304) | UniProtKB | pending move to GO:0019418 |
| UniProt | SLC25A10 | Homo sapiens (NCBITaxon:9606) | Q9UBX3 | TAS (ECO:0000304) | UniProtKB | pending move to GO:0019418 |
| RGD | Sqor | Rattus norvegicus (NCBITaxon:10116) | — | ISO (ECO:0000266) | RGD | pending move |
| MGI | Sqor | Mus musculus (NCBITaxon:10090) | — | ISS/ISO (ECO:0000250, ECO:0000266) | MGI | pending move |

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
  mammalian → GO:0070221 — mapping **removed** from InterPro (will
  appear in InterPro release 109.0; confirmed 2026-05-15 in
  go-annotation#6388 comments).
- Reactome has already migrated its 2 affected annotations
  (confirmed 2026-04-22 in upstream issue comments).
- No ARBA / UniRule mappings to the obsoleted terms were listed.

## Impact on this repo

No genes annotated to GO:0070221/222/223 are currently reviewed in
this repo:

- `genes/human/SQOR/` — does not exist
- `genes/human/TSTD1/` — does not exist
- `genes/human/SLC25A10/` — does not exist
- `genes/PSEAE/PA2345/` — does not exist
- `genes/SCHPO/hmt2/` — does not exist

So **no existing reviews need refresh** for the obsoletion itself.
The opportunity here is that **SQOR is otherwise unreviewed** in
this repo despite being a well-characterized human mitochondrial
sulfide-oxidizing enzyme directly relevant to H2S signaling, sulfide
detoxification, and the inherited mitochondrial disorder caused by
SQOR deficiency (PMID:31108281; affects 1 of the 3 known annotations
queued for migration).

## Scope

- **Organisms**: primary candidates are human (existing `genes/human/`)
  and S. pombe (existing `genes/SCHPO/`). All other affected genes
  are IBA propagations and will migrate automatically.
- **GO branches**: BP only — the obsoletion is a
  mechanism-specificity collapse to the broader parent term. No MF
  or CC changes.
- **Type of fix**: terminological — the biology (sulfide → sulfite/
  sulfate) is unchanged; reviews would evaluate whether GO:0019418
  is the correct BP for SQOR's core function or whether more
  appropriate descendants (e.g. **GO:0070221** is gone, but the
  cognate MF **GO:0047804 sulfide:quinone reductase activity** is
  intact) better capture SQOR's mechanism.

## Candidate genes for initial review

Verify each with `just fetch-gene <organism> <gene>` before starting
and confirm UniProt accessions. None are currently in the repo.

### Tier 1 — direct experimental annotation, well-characterized

1. **SQOR / Q9Y6N5** (Homo sapiens) — mitochondrial sulfide:quinone
   oxidoreductase, the canonical human enzyme for sulfide oxidation
   in the first step of mitochondrial H2S detoxification. The IDA
   annotation on GO:0070221 is the 1 EXP that the upstream issue
   flags for migration. SQOR also carries an IBA on GO:0070221. A
   review here should anchor the BP on GO:0019418 (post-obsoletion)
   and confirm the MF anchor remains GO:0047804 sulfide:quinone
   reductase activity. Clinically relevant (SQOR deficiency causes
   Leigh-like mitochondrial encephalopathy).

### Tier 2 — TAS, less direct

2. **TSTD1 / Q8NFU3** (Homo sapiens) — thiosulfate sulfurtransferase-
   like domain-containing 1; carries a TAS annotation on GO:0070221
   plus an IEA. Its primary characterized activity is rhodanese-type
   thiosulfate:glutathione sulfurtransferase (PMID:24107290), and
   InterPro has already removed the IPR042457 → GO:0070221 mapping
   per the upstream issue. A review would assess whether GO:0019418
   (the obsoletion replacement) or a different sulfurtransferase BP
   is the right placement.
3. **SLC25A10 / Q9UBX3** (Homo sapiens) — mitochondrial
   dicarboxylate carrier; TAS on GO:0070221. The annotation is on a
   pathway role rather than direct enzymatic activity; review would
   determine whether GO:0019418 is appropriate or whether this
   annotation should be retracted in favor of transport-centric BPs.

### Tier 3 — opportunistic, non-human

4. **hmt2 / SPBC2G5.06c** (Schizosaccharomyces pombe) — fission yeast
   ortholog carrying an IBA on GO:0070221. Would extend SCHPO
   coverage but lower priority since IBA migration is automatic.

## Proposed approach

1. **Obsoletion has landed.** All three terms are obsolete in the
   ontology and the upstream ontology ticket is closed. The
   annotation-migration work in go-annotation#6388 is the only
   remaining loose end upstream (still open as of 2026-05-15, with
   the InterPro mapping removed the same day).
2. **Start with human SQOR.** Run `just fetch-gene human SQOR` and
   confirm the GOA pull picks up the obsoletion: GO:0070221 should
   appear as an obsolete term (or already have been remapped to
   GO:0019418). Review per CLAUDE.md, paying attention to:
   - The cognate MF GO:0047804 sulfide:quinone reductase activity
     (intact) is the right MF anchor.
   - The BP anchor should be GO:0019418 sulfide oxidation
     (post-obsoletion).
   - SQOR also participates in CoQ/electron-transport context;
     check that any CC/BP claims about mitochondrial ETC
     integration are evidence-backed.
3. **Follow with TSTD1 then SLC25A10.** Both are TAS-only on the
   obsoleted term and the upstream mapping (IPR042457 → GO:0070221)
   has already been removed; review should evaluate whether
   GO:0019418 is even the right BP or whether the original TAS was
   on shaky ground.
4. **Defer S. pombe hmt2 and the bacterial homologs** unless they
   come up via other workstreams; the IBA propagations will be
   auto-migrated.
5. **Do not create reviews for the IBA-only orthologs** listed in
   the impact table — they will be remapped automatically.

## Priority

**Medium-low.** Only 3 direct (non-IBA) annotations are affected
and the ontology change is already in production. The migration
upstream is small. However, human SQOR is a clinically and
biologically important gene with no review yet in this repo, so
this obsoletion is a reasonable trigger to add it. The other two
human entries (TSTD1, SLC25A10) are TAS-only and lower value.

## Status

- 2026-05-15 — Project file created. Upstream annotation issue
  #6388 still open; latest activity was InterPro confirming
  removal of the IPR042457 → GO:0070221 mapping. All three ontology
  obsoletion PRs are merged (#31949, #32025, #32068) and the
  parent ontology ticket #31842 is closed. No gene reviews started
  in this repo for SQOR/TSTD1/SLC25A10.
