---
title: "Reactome-GO Alignment Project"
maturity: SCOPING
tags: [PIPELINE]
---

# Reactome-GO Alignment Project

**Bottom line:** Reactome enters AI Gene Review at two granularities, and both
need to line up with GO. At the fine-grained level, individual `Reactome:R-*`
events appear in GOA as TAS evidence for molecular-function and biological-
process assertions; each one needs to be checked against the gene product that
actually executes the reaction, the activity term used in GO, and any complex
membership that could be over-exporting an MF to accessory subunits. At the
pathway level, whole Reactome pathways can be compared to GO-CAMs and to the
local module YAMLs: catalyst, reaction order, input/output molecules,
compartments, causal edges, and missing "black box" transport or catalytic
events. The project is currently in its scoping phase. Existing work gives two
anchors: the [FAO module vs Reactome](FATTY_ACID_BETA_OXIDATION/reactome-comparison.md)
comparison, which found agreement through most of mitochondrial beta-oxidation
but a thiolase granularity difference, and the narrower
[Reactome Black Box Event Gap-Filling](REACTOME_GAP_FILLING.md) project, which
uses gene reviews to identify catalysts or transporters absent from Reactome
events.

## Overview

Reactome is both an evidence source for existing GO annotations and an
independent pathway model. This project audits the interface in two directions:

| Track | Reactome object | GO object | Alignment question |
|-------|-----------------|-----------|--------------------|
| Individual MF alignment | Reaction-like `Reactome:R-*` events attached to GOA rows | Gene-level MF annotations in `*-ai-review.yaml` | Does the Reactome event support this MF term on this gene product, or should it be refined, demoted, or flagged as a complex/pathway over-export? |
| Pathway/GO-CAM alignment | Reactome pathways and reaction networks cached under `reactome/` | GO-CAM production models in `gocams/` and local module YAMLs in `modules/` | Do the pathway steps have the same executors, MFs, compartments, inputs/outputs, and ordering? |

The tracks are complementary. A single Reactome event can be the right support
for a GO MF row while the surrounding pathway still differs from GO-CAM in
reaction granularity or causal order. Conversely, a Reactome pathway can capture
the right biological process while one exported MF row lands on a scaffold,
accessory member, or assembly factor that does not perform the activity.

## Track 1: Individual MF Alignment

The reaction-level audit starts from Reactome-backed rows in gene reviews:

1. Inventory `existing_annotations` whose `original_reference_id` is
   `Reactome:R-*`, split by aspect and GO term.
2. Join each row to its cached `reactome/<stable_id>.md` entry when present, and
   record whether the cached event is a reaction, transport event, pathway
   container, complex assembly event, or black-box placeholder.
3. Compare the GO term to the event statement:
   - exact or intentionally broader MF
   - too broad or too narrow relative to the reaction chemistry
   - pathway/BP row that is mechanistically justified
   - pathway/BP row that only reflects downstream necessity
   - MF exported to a non-executor subunit through complex membership
   - event missing an assigned gene product in Reactome
   See the [Reactome MF verdict vocabulary](REACTOME/verdict-vocabulary.md)
   for the first reusable set of row-level labels.
4. Materialize curation in the affected gene reviews: `ACCEPT` clean rows,
   `MODIFY` rows whose chemistry is sound but term specificity is wrong,
   `MARK_AS_OVER_ANNOTATED` or `REMOVE` rows where pathway or complex membership
   has been flattened onto the wrong gene product, and `UNDECIDED` rows whose
   Reactome evidence cannot be checked from local sources.

Important guardrail: Reactome pathway membership is not by itself evidence that
the gene product is `involved_in` every named pathway container. The entity has
to perform a molecular step, recruit a substrate, contribute a structural or
cofactor activity, or otherwise do work in the process being asserted.

## Track 2: Pathways and GO-CAMs

The pathway-level audit compares Reactome pathways to two local pathway
representations:

- production GO-CAM models cached in `gocams/<MODEL>/<MODEL>-src.yaml` and
  indexed by `gocams/index.tsv`
- local curation modules in `modules/*.yaml`, many of which already cite
  Reactome stable IDs at the module and reaction level

For each pilot pathway, the comparison should record:

| Dimension | Check |
|-----------|-------|
| Activity inventory | Are there steps in Reactome with no GO-CAM/local-module counterpart, or vice versa? |
| Gene product executor | Does each reaction assign the same catalyst, transporter, receptor, adaptor, or complex subunit set? |
| Molecular function | Does the GO MF match the reaction chemistry at the right specificity? |
| Inputs and outputs | Do substrates, products, and reaction direction match, including cofactors and transported species? |
| Cellular context | Do compartments agree, and do membrane transport events cross the same boundary? |
| Causal order | Does the upstream/downstream ordering in GO-CAM match Reactome's event graph? |
| Complex attribution | Does the model distinguish active members from accessory, regulatory, or assembly members? |
| Black boxes | Does Reactome intentionally leave a catalyst or transporter absent that local gene reviews can now propose? |

The output of a pathway audit should be a project sub-page under
`projects/REACTOME/` when it is Reactome-centric, or a section in an existing
biology-domain project when Reactome is only one cross-check. The
mitochondrial beta-oxidation comparison in
`projects/FATTY_ACID_BETA_OXIDATION/reactome-comparison.md` is the current
template for a concise pathway-level reconciliation.

## Relation To Neighboring Projects

- [REACTOME_GAP_FILLING](REACTOME_GAP_FILLING.md) is the black-box-event arm:
  reactions that Reactome already knows should occur but has not yet assigned to
  a catalyst or transporter.
- [Protein Complex Functions](PROTEIN_COMPLEX_FUNCTIONS.md) supplies the
  attribution policy for Reactome and GO-CAM complex events, especially the
  distinction between active members and accessory or structural members.
- [RHEA](RHEA.md) covers reaction-to-GO MF mapping for RHEA. Reactome should use
  those findings when a Reactome reaction is enzymatic and already has a RHEA
  equivalent.
- [TCDB](TCDB.md) and [GLYCOBIOLOGY](GLYCOBIOLOGY.md) provide source-audit
  patterns for external databases whose entities need careful term-specific
  propagation into GO.

## Pilot Areas

| Area | Existing anchor | Next Reactome-specific question |
|------|-----------------|---------------------------------|
| Mitochondrial fatty acid beta-oxidation | `fatty_acid_beta_oxidation` module and the FAO Reactome comparison | Convert the hand comparison into a reusable reaction-inventory report and capture the step 4 thiolase divergence as a structured finding. |
| Bile acid synthesis and transport | ABCD3 in `REACTOME_GAP_FILLING`; local bile-acid modules with Reactome evidence | Distinguish assigned transport events from true black boxes across mitochondrial import/export and peroxisomal import/export. |
| OXPHOS complexes | Complex II and Complex IV modules plus the Protein Complex Functions project | Check whether Reactome catalysts map to active subunits, whole complexes, or accessory/assembly factors before MF export. |
| Purine nucleotide interconversion | `purine_nucleotide_interconversion` module with Reactome reaction evidence | [First pilot](REACTOME/purine-nucleotide-interconversion.md) found reaction-level agreement for ADSS, IMPDH, GMPS, and AMPD; the cached human GO-CAM index has no rows for these executors yet. |

## Status

- [x] 2026-09-30: Create the umbrella Reactome-GO alignment project page.
- [x] 2026-09-30: Inventory Reactome-backed `existing_annotations` in completed
  gene reviews and stratify them by aspect, evidence code, action, and stable
  ID. See [Reactome inventory results](REACTOME/RESULTS.md).
- [x] 2026-09-30: Inventory module-level `Reactome:R-*` citations in
  `modules/*.yaml` and group them by pathway domain.
- [x] 2026-09-30: Inventory human GO-CAM activities and flag rows whose
  `UniProtKB` gene product appears in a Reactome-citing local module.
- [x] 2026-10-01: Create a reaction-by-reaction Reactome/module/GO-CAM pilot for
  [purine nucleotide interconversion](REACTOME/purine-nucleotide-interconversion.md).
- [x] 2026-10-01: Write a
  [verdict vocabulary](REACTOME/verdict-vocabulary.md) for individual Reactome
  MF rows so repeated failure modes, especially complex over-export and
  pathway-container over-annotation, can be counted across reviews.
- [x] 2026-10-01: Apply the verdict vocabulary to a
  [first MF-focused inventory slice](REACTOME/MF_VERDICT_SLICE.md) and count
  accepted matches, term-refinement candidates, mixed over-annotations, and
  removed or undecided MF rows.
- [x] 2026-10-01: Manually resolve the first pass's blank MF verdicts,
  especially `REMOVE` and `MARK_AS_OVER_ANNOTATED` rows whose failure modes
  distinguish wrong executor, wrong branch, contradicted family event, and
  pathway/container overreach.
- [x] 2026-10-03: Audit
  [repeated multi-gene Reactome MF stable IDs](REACTOME/REPEATED_MF_EVENTS.md),
  starting with the mixed RHOA GAP, LPCAT/LPGAT, and ABCC-family events that
  already have both accepted and non-accepted gene-review outcomes.
- [x] 2026-10-05: Add a YAML-first Reactome pathway ingester seeded by
  [`reactome_pathways.yaml`](REACTOME/reactome_pathways.yaml), normalize the
  first urea-cycle, purine-interconversion, and bile-acid ring-modification
  subtrees, and emit
  [module-alignment reports](REACTOME/pathway-alignments/urea_cycle.md).
- [x] 2026-10-09: Seed the GPI anchor core-glycan and glycosphingolipid
  lysosomal degradation slices in `reactome_pathways.yaml`, add structured
  comparator verdicts for exact cited events and same-participant fuzzy gaps,
  and regenerate the existing alignment YAML/reports without introducing new
  TSV interchange files.
- [x] 2026-10-09: Add a repeatable `--pathway` selector to the Reactome
  ingester and make network/HTTP fetch failures skip only the affected slice,
  so the two newly seeded pathways can be live-fetched without refreshing the
  three already materialized imports.
- [ ] Resolve the four high-priority repeated MF events by deciding whether the
  Reactome family grouping is over-broad, the GO MF mapping is too general, or
  one paralog-specific gene review needs curation follow-up.
- [ ] Re-run
  `python3 projects/REACTOME/ingest_reactome_pathways.py --pathway gpi_anchor_core_glycan_assembly --pathway glycosphingolipid_lysosomal_degradation`
  once `reactome.org` DNS resolution is available, then inspect the materialized
  PSAP and PIGX rows for exact-event/missing-executor verdicts.

## Notes

### 2026-10-21

Resolved PR #5246 review follow-up in the pathway and inventory tooling. The
Reactome pathway comparator now distinguishes exact
`EntityWithAccessionedSequence` catalysts from overlapping `Complex`,
`DefinedSet`, and `CandidateSet` members, so set- or complex-mediated
overlaps are held at `same_reaction_executor_unconfirmed` instead of being
promoted to `reaction_id_exact`.

Recorded the bile-acid `R-HSA-192033` AKR1D1 event as a `wrong_go_branch`
case: the event evidence supports delta4-3-oxosteroid 5beta-reductase
chemistry, but the Reactome GO activity sits on the alcohol-dehydrogenase
NADP+ branch. Corrected the 2026-10-05 exact-count framing at the same time:
the regenerated purine slice has one exact single-executor match plus ADSS,
IMPDH, and AMPD `DefinedSet` rows, and the bile-acid slice has one exact
single-executor match, one CYP7B1 `CandidateSet`, one AKR1D1 wrong-branch
event, and one HSD3B7 parent/child MF mismatch.

Converted the hand-curated MF verdict overrides from
`mf_manual_verdicts.tsv` to `mf_manual_verdicts.yaml` and joined them by stable
`organism`/`gene`/`reactome_id`/`term_id` keys rather than by
`existing_annotations` position.

### 2026-10-09

Extended the YAML-first pathway-ingest seed with two additional curated slices:
`gpi_anchor_core_glycan_assembly`, rooted at Reactome `R-HSA-162710` with five
local core-glycan reaction events, and
`glycosphingolipid_lysosomal_degradation`, rooted at `R-HSA-1660661` with the
five unique catalytic events cited by the local module. The existing Reactome
Markdown cache already has titles for these IDs, but the normalized YAML
imports still need a live ContentService fetch because the Markdown cache does
not preserve catalyst, input/output, and physical-entity structure.

Promoted the comparator from set subtraction to structured verdicts. Exact
`source_id: Reactome:*` matches are now classified as full
`reaction_id_exact` rows when the imported catalyst and GO MF both match the
local activity, or as `same_reaction_mf_unconfirmed` /
`same_reaction_missing_executor` when the stable ID is shared but the imported
Reactome event lacks one of those checks. Reactome-only and module-only gaps now
record verdict-bearing YAML objects and cross-link same-participant candidates
when a local selector overlaps an imported reaction under a different stable
ID. Offline regeneration from the existing imports found one such fuzzy link:
the current Reactome `R-HSA-70635` urea-cycle subtree contains mitochondrial
ARG2 arginase activity, while the local urea-cycle module includes ARG2 as a
representative of the ARG1/ARG2 arginase family but cites only the cytosolic
ARG1 reaction.

Added a repeatable `--pathway` selector for `ingest_reactome_pathways.py` and
made live-fetch network failures local to each requested slice. A targeted
materialization run for `gpi_anchor_core_glycan_assembly` and
`glycosphingolipid_lysosomal_degradation` could not resolve `reactome.org`, so
the normalized imports for those two slices remain absent. The local Markdown
cache has all selected Reactome IDs, but only as display names and prose
summaries; it does not contain enough catalyst, input/output, or
physical-entity cross-reference structure to stand in for the ContentService
payloads without circularly restating the local modules.

### 2026-10-05

Added `ingest_reactome_pathways.py`, a YAML-first Reactome subtree ingester that
keeps graph-shaped pathway data out of TSV source files. The hand-authored
`reactome_pathways.yaml` seed starts with three module comparisons: the full
Reactome `R-HSA-70635` urea-cycle subtree, a four-reaction curated slice of
`R-HSA-73817` for purine nucleotide interconversion, and a four-reaction curated
slice of `R-HSA-192105` for bile-acid ring modification. Generated imports live
under `imports/*.reactome.yaml`, computed exact-ID comparison verdicts under
`alignments/*.yaml`, and curator-facing reports under `pathway-alignments/*.md`.
The first live ingest used Reactome release 97, found 4/4 exact activity matches
for both curated slices, and found 7 exact urea-cycle matches plus one local-only
citrin transport event and ten current Reactome-only reaction-like events.

### 2026-10-03

Added a repeated-event rollup for Reactome-backed molecular-function rows. The
new `data/repeated_mf_events.tsv` table groups the 905-row MF slice by
Reactome stable ID and identifies 49 stable IDs reused across multiple genes,
covering 119 rows. Thirty-five repeated events are uniform exact matches, ten
have mixed refinement or undecided outcomes, and four carry manual failure
modes: the RHOA GAP event, the ABCC organic-anion transport family event, and
two LPCAT/LPGAT events where an accepted family reaction is contradicted or
overly broad for at least one paralog.

### 2026-10-01

Added the first compact pathway pilot under `projects/REACTOME/`, centered on
the `purine_nucleotide_interconversion` module. The Reactome reaction IDs
`R-HSA-111524`, `R-HSA-73794`, `R-HSA-73792`, and `R-HSA-76590` match the
module's ADSS, IMPDH, GMPS, and AMPD molecular functions respectively, while
`R-HSA-73817` is a pathway-level purine ribonucleoside monophosphate
biosynthesis container that should be excluded from one-to-one MF matching. No
cached human GO-CAM activity rows currently mention the module's seven
`UniProtKB` executors, so this pilot records a Reactome/module alignment and a
GO-CAM absence rather than a full three-way pathway reconciliation.

Added an initial row-level verdict vocabulary for Reactome MF review work. The
codes separate exact reaction-to-MF matches from term refinements,
location/pathway context rows, complex active-member versus complex over-export
cases, pathway-container overreach, passive input/product roles, black-box
gaps, boundary mismatches, and events that need richer Reactome graph detail
before they can be judged.

Extended the reproducible inventory with a Reactome-backed MF slice. The first
pass extracts 905 molecular-function rows from the 16,334 Reactome-backed
gene-review annotations, assigns conservative candidate verdicts from completed
review actions, and writes `data/mf_verdict_slice.tsv` plus a Markdown summary.
The slice has 781 accepted exact-or-non-core candidates, 80 term-refinement
candidates, 25 mixed over-annotation rows, 12 removed rows, 7 undecided rows,
119 rows whose Reactome stable ID is reused across multiple genes, and 73 rows
whose stable ID also appears as local module MF evidence.

Added `mf_manual_verdicts.yaml` and fed it back into the inventory so the 37
`MARK_AS_OVER_ANNOTATED` and `REMOVE` MF rows now have explicit verdicts rather
than a blank "needs manual bucket" placeholder. The largest manual bucket is 19
broad-parent or duplicate mappings that collapse to `reaction_mf_refine`; the
rest split into five paralog/legacy activity contradictions, three contested
direct activities, three regulator-not-executor cases, two wrong executors, two
wrong GO branches, and single nonphysiological-side-activity,
obsolete-term, and vesicle-versus-transmembrane transport cases.

### 2026-09-30

Created the top-level project after finding three local Reactome integration
points: cached `reactome/R-*.md` entries, Reactome stable IDs embedded in
module YAML evidence blocks, and `Reactome:R-*` references in completed human
and mouse gene reviews. The project is deliberately broader than
`REACTOME_GAP_FILLING`: black-box event resolution is one class of
pathway-level divergence, while this page also covers ordinary reaction-to-MF
adjudication and alignment between complete Reactome pathways, GO-CAMs, and
local modules.

Added a reproducible local inventory in `projects/REACTOME/`. The first pass
extracts 16,334 Reactome-backed existing annotations from gene reviews, 325
Reactome source citations from module YAMLs, and 5,604 human GO-CAM activities
with 92 of those GO-CAM rows overlapping a `UniProtKB` representative member
from a Reactome-citing local module. The script joins gene-review rows back to
their `*-goa.tsv` records to recover the GO aspect for older reviews that lack
an explicit qualifier, and enriches both gene and module rows with any matching
cached `reactome/R-*.md` frontmatter.
