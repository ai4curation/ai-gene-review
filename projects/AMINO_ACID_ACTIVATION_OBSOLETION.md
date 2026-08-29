---
title: "Amino Acid Activation Terms — Obsoletion of 43 Substrate-Specific tRNA Aminoacylation BPs"
maturity: SCOPING
tags: [OBSOLETION]
species: [human, PSEPK, POPTR, DANRE, METTP]
---

# Amino Acid Activation Terms — Obsoletion of 43 Substrate-Specific tRNA Aminoacylation BPs

## Overview

A GO obsoletion proposal will obsolete **43 biological-process terms** that name a
specific amino acid being charged onto tRNA — the 20 cytosolic
`<aa>yl-tRNA aminoacylation` terms, their 20 mitochondrial counterparts, two
redundant compartment-qualified variants, and the transamidation route term.
Every one of them is replaced by a compartment-level parent:

- 23 terms → `GO:0006418 tRNA aminoacylation for protein translation`
- 20 terms → `GO:0070127 tRNA aminoacylation for mitochondrial protein translation`

The rationale is that **amino-acid specificity is a molecular-function
distinction, not a process one**. Each obsoleted BP has an exact 1:1 MF
counterpart that already exists (`GO:0006419 alanyl-tRNA aminoacylation` ↔
`GO:0004813 alanine-tRNA ligase activity`, and so on for all 20 amino acids), so
no new terms are required. Upstream states explicitly that the mitochondrial
terms map to the **same** MF as their cytosolic counterparts, because compartment
is likewise not a molecular-function distinction: a synthetase charging tRNA in
both compartments takes one MF annotation, not two.

This project tracks the impact on AI Gene Review. **Fifteen gene reviews in this
repo are affected**, eleven of them through author-supplied `core_functions` term
ids that are strictly validated and will need to change — so this is a concrete
re-review queue, not a documentation exercise. More importantly, four reviews
contain reasoning that the obsoletion will **invert** (see
[The four inverted judgments](#the-four-inverted-judgments)).

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6525](https://github.com/geneontology/go-annotation/issues/6525) (updated 2026-08-28)
- Ontology ticket: [geneontology/go-ontology#15375](https://github.com/geneontology/go-ontology/issues/15375) (opened 2018-03-10, **open**)
- Affected annotations spreadsheet: [Google Sheet](https://docs.google.com/spreadsheets/d/1OQWHL67xbqC47wRI1THT1MdN53HcSUnCBqamItzCW9U)
- Impacted groups (per upstream): UniProt 52, SGD 45, FlyBase 44, ComplexPortal 28,
  EcoCyc 25, GeneDB 11, MGI 7, CAFA 7, CGD 6, ZFIN 6, PINC 5, RGD 4, EcoliWiki 4,
  BHF-UCL 3, MTBBASE 2, HGNC 1, PomBase 1 — **251 total**

### Two structural changes have already landed

The surrounding hierarchy was repaired ahead of the obsoletion, in two PRs merged
against go-ontology#15375:

- **#32537** (merged 2026-08-26) severed `tRNA aminoacylation` from
  `amino acid metabolic process`. Charging a tRNA attaches an amino acid to
  something; it does not metabolize it. `GO:0043038 amino acid activation` was
  obsoleted in the same PR (it had zero annotations).
- **#32541** (merged 2026-08-27) renamed `GO:0043039` to **`tRNA charging`**,
  keeping `tRNA aminoacylation` as an exact synonym, and retained
  `is_a tRNA metabolic process`. A proposed `part_of GO:0160307 protein
  biosynthetic process` edge was **rejected** during review — correctly, since
  `GO:0043040 tRNA aminoacylation for nonribosomal peptide biosynthetic process`
  falsifies the universal claim.

**Release lag caveat:** as of 2026-08-29 neither OLS nor QuickGO reflects these
merges. Both still return `GO:0043038` as non-obsolete, and both still label
`GO:0043039` as "tRNA aminoacylation" (OLS does already carry `tRNA charging`
among its synonyms). Do not treat the live lookup services as evidence that the
merges have not happened; check the ontology repo instead.

### Count discrepancy worth confirming upstream

The ontology ticket's proposal says **"Obsoleted (42)"**; the annotation ticket
lists **43** terms. The difference is `GO:0070681 glutaminyl-tRNAGln biosynthesis
via transamidation`, which is the one entry that breaks the 1:1 pattern — it is
the *indirect* transamidation route (misacylated Glu-tRNA(Gln) formed by a
non-discriminating GluRS, then amidated by GatCAB), and its MF counterpart is
`GO:0050567 glutaminyl-tRNA synthase (glutamine-hydrolyzing) activity`, not a
glutamine-tRNA ligase. Whether it is genuinely in the same obsoletion batch
should be confirmed before any in-repo edits, because **five of this repo's
fifteen affected reviews hang on `GO:0070681` alone**, and it is also the source
term for a `concepts` node in `modules/bacterial_aminoacyl_trna_charging.yaml`.

## Obsoletion plan (per upstream)

All 43 terms confirmed **live** (non-obsolete) in QuickGO on 2026-08-29, as were
both replacements and a sampled MF counterpart (`GO:0004813`, `GO:0050567`).

Annotation counts below are from the QuickGO annotation API on 2026-08-29,
exact-term. `exp` counts `ECO:0000269` and descendants; `all` is all evidence.

### Block 1 → `GO:0006418 tRNA aminoacylation for protein translation`

| Obsoleted term | ID | 1:1 MF counterpart | exp | all |
|---|---|---|---|---|
| alanyl-tRNA aminoacylation | GO:0006419 | GO:0004813 alanine-tRNA ligase activity | 10 | 35,014 |
| arginyl-tRNA aminoacylation | GO:0006420 | GO:0004814 arginine-tRNA ligase activity | 5 | 40,567 |
| asparaginyl-tRNA aminoacylation | GO:0006421 | GO:0004816 asparagine-tRNA ligase activity | 9 | 18,878 |
| aspartyl-tRNA aminoacylation | GO:0006422 | GO:0004815 aspartate-tRNA ligase activity | 4 | 31,298 |
| cysteinyl-tRNA aminoacylation | GO:0006423 | GO:0004817 cysteine-tRNA ligase activity | 5 | 31,142 |
| glutamyl-tRNA aminoacylation | GO:0006424 | GO:0004818 glutamate-tRNA ligase activity | 7 | 46,903 |
| glutaminyl-tRNA aminoacylation | GO:0006425 | GO:0004819 glutamine-tRNA ligase activity | 6 | 13,762 |
| glycyl-tRNA aminoacylation | GO:0006426 | GO:0004820 glycine-tRNA ligase activity | 9 | 35,598 |
| histidyl-tRNA aminoacylation | GO:0006427 | GO:0004821 histidine-tRNA ligase activity | 5 | 34,734 |
| isoleucyl-tRNA aminoacylation | GO:0006428 | GO:0004822 isoleucine-tRNA ligase activity | 6 | 29,914 |
| leucyl-tRNA aminoacylation | GO:0006429 | GO:0004823 leucine-tRNA ligase activity | 8 | 29,621 |
| lysyl-tRNA aminoacylation | GO:0006430 | GO:0004824 lysine-tRNA ligase activity | 13 | 32,872 |
| methionyl-tRNA aminoacylation | GO:0006431 | GO:0004825 methionine-tRNA ligase activity | 9 | 30,699 |
| phenylalanyl-tRNA aminoacylation | GO:0006432 | GO:0004826 phenylalanine-tRNA ligase activity | 26 | 52,601 |
| prolyl-tRNA aminoacylation | GO:0006433 | GO:0004827 proline-tRNA ligase activity | 5 | 30,613 |
| seryl-tRNA aminoacylation | GO:0006434 | GO:0004828 serine-tRNA ligase activity | 11 | 28,880 |
| threonyl-tRNA aminoacylation | GO:0006435 | GO:0004829 threonine-tRNA ligase activity | 11 | 31,390 |
| tryptophanyl-tRNA aminoacylation | GO:0006436 | GO:0004830 tryptophan-tRNA ligase activity | 5 | 30,758 |
| tyrosyl-tRNA aminoacylation | GO:0006437 | GO:0004831 tyrosine-tRNA ligase activity | 8 | 28,429 |
| valyl-tRNA aminoacylation | GO:0006438 | GO:0004832 valine-tRNA ligase activity | 2 | 28,254 |
| cytosolic valyl-tRNA aminoacylation | GO:0061475 | GO:0004832 valine-tRNA ligase activity | 1 | **1** |
| cytoplasmic alanyl-tRNA aminoacylation | GO:1990762 | GO:0004813 alanine-tRNA ligase activity | 0 | **0** |
| glutaminyl-tRNAGln biosynthesis via transamidation | GO:0070681 | GO:0050567 glutaminyl-tRNA synthase (glutamine-hydrolyzing) activity | 14 | 56,741 |

### Block 2 → `GO:0070127 tRNA aminoacylation for mitochondrial protein translation`

All 20 mitochondrial terms map to the **same** MF as their cytosolic twin.

| Obsoleted term | ID | exp | all |
|---|---|---|---|
| mitochondrial alanyl-tRNA aminoacylation | GO:0070143 | 2 | 2,876 |
| mitochondrial arginyl-tRNA aminoacylation | GO:0070144 | 0 | 1 |
| mitochondrial asparaginyl-tRNA aminoacylation | GO:0070145 | 2 | 231 |
| mitochondrial aspartyl-tRNA aminoacylation | GO:0070146 | 2 | 160 |
| mitochondrial cysteinyl-tRNA aminoacylation | GO:0070147 | 0 | **0** |
| mitochondrial glutaminyl-tRNA aminoacylation | GO:0070148 | 0 | **0** |
| mitochondrial glutamyl-tRNA aminoacylation | GO:0070149 | 0 | 1 |
| mitochondrial glycyl-tRNA aminoacylation | GO:0070150 | 2 | 5,030 |
| mitochondrial histidyl-tRNA aminoacylation | GO:0070151 | 0 | **0** |
| mitochondrial isoleucyl-tRNA aminoacylation | GO:0070152 | 0 | **0** |
| mitochondrial leucyl-tRNA aminoacylation | GO:0070153 | 1 | **1** |
| mitochondrial lysyl-tRNA aminoacylation | GO:0070154 | 2 | 1,054 |
| mitochondrial methionyl-tRNA aminoacylation | GO:0070155 | 1 | **1** |
| mitochondrial phenylalanyl-tRNA aminoacylation | GO:0070156 | 1 | 17 |
| mitochondrial prolyl-tRNA aminoacylation | GO:0070157 | 0 | **0** |
| mitochondrial seryl-tRNA aminoacylation | GO:0070158 | 4 | 310 |
| mitochondrial threonyl-tRNA aminoacylation | GO:0070159 | 1 | 273 |
| mitochondrial tryptophanyl-tRNA aminoacylation | GO:0070183 | 2 | 3,113 |
| mitochondrial tyrosyl-tRNA aminoacylation | GO:0070184 | 4 | 296 |
| mitochondrial valyl-tRNA aminoacylation | GO:0070185 | 0 | **0** |

**Six of the twenty mitochondrial terms have zero annotations of any kind**
(`GO:0070147`, `GO:0070148`, `GO:0070151`, `GO:0070152`, `GO:0070157`,
`GO:0070185`), as does `GO:1990762`. The mitochondrial block carries 24 experimental annotations
across all 20 terms — fewer than `GO:0006432` alone. This is strong independent
support for the upstream position: the compartment-qualified terms were created
to mirror the cytosolic set, not because curators needed them.

### On the count gap

The QuickGO experimental totals come to **203** (179 in block 1, 24 in block 2)
against the upstream group tally of **251**. The gap is almost certainly a filter
difference rather than a real disagreement — the upstream spreadsheet's
ComplexPortal (28), CAFA (7) and PINC (5) contributions largely do not carry
`ECO:0000269`-descendant evidence codes. Reconcile against the spreadsheet before
quoting either number as authoritative.

## The four inverted judgments

This is the most consequential finding for this repo, and it is not a mechanical
id swap.

Four reviews here carry an explicit review action on `GO:0006418` — the term
everything is being merged **into** — arguing that it is too general and is
superseded by the amino-acid-specific child:

| Review | Action on GO:0006418 | Recorded reason |
|---|---|---|
| PSEPK/glnS | `MARK_AS_OVER_ANNOTATED` | "GO:0006425 already captures the direct substrate-specific process." |
| PSEPK/gltX | `MARK_AS_OVER_ANNOTATED` | "GO:0006424 already captures the defined glutamate and tRNA(Glu) substrates." |
| PSEPK/serS | `MODIFY` → GO:0006434 | "SerS has defined serine and tRNA substrates. GO:0006434 preserves its direct role in translational tRNA charging while recording the known amino-acid specificity." |
| human/AARS1 | `MODIFY` → GO:0006419 | "Use the alanine-specific aminoacylation process." |

The obsoletion asserts the **opposite**: the substrate-specific child is the wrong
place to record specificity, and `GO:0006418` is the correct BP. After the merge,
each of these four says "replace the surviving term with an obsolete one", and
two of them mark the surviving term as an over-annotation.

These reviews are not wrong about the biology — SerS really does charge serine —
they applied a general "prefer the most specific term" heuristic to an axis
(substrate identity) where GO has now decided specificity belongs on the MF. The
fix is to move the specificity claim to the MF slot (`GO:0004828 serine-tRNA
ligase activity` etc., which these reviews already carry) and let the BP sit at
`GO:0006418`. **This is a reusable lesson beyond tRNA charging**: "more specific
is better" is not unconditional, and cross-aspect redundancy is the signal that a
BP is encoding something that belongs in MF. It belongs in
[OVER_ANNOTATION_PATTERNS](OVER_ANNOTATION_PATTERNS.md).

A fifth, smaller inversion: **human/AARS2** has a `MODIFY` on `GO:0006419` whose
`proposed_replacement_terms` is `GO:0070143` — a term that is *itself* in the
obsoletion batch. That replacement target must be re-pointed to `GO:0070127`
regardless of how the rest of the review is handled.

## Impact on this repo

Fifteen reviews touch the obsoleted terms or their replacements. Per CLAUDE.md,
`existing_annotations[].term.id` is GOA-sourced and **not** hard-validated, so
those will not break validation — but `core_functions` ids **are** strictly
validated, and **eleven reviews use an obsoleted term inside
`core_functions.directly_involved_in`**.

### Reviews needing a `core_functions` change (11)

| Review | Accession | `core_functions` term | `existing_annotations` on obsoleted terms |
|---|---|---|---|
| human/AARS1 | P49588 | GO:0006419 | ×6 — IBA, IEA, IMP (PMID:33909043), IDA (PMID:28493438), IDA (PMID:27622773), TAS (PMID:7761427); all ACCEPT |
| human/AARS2 | Q5JTZ9 | GO:0070143 | GO:0070143 IBA + IMP (PMID:21549344) ACCEPT; GO:0006419 IEA MODIFY→GO:0070143 |
| POPTR/ALARS | B9HQZ6 | GO:0006419 | IBA + IEA, both ACCEPT |
| POPTR/GATC | B9INH0 | GO:0070681 | IBA + IEA, both ACCEPT |
| PSEPK/gatA | Q88PB9 | GO:0070681 | IEA ACCEPT |
| PSEPK/gatB | Q88PC0 | GO:0070681 | IEA ACCEPT |
| PSEPK/gatC | Q88PB8 | GO:0070681 | IEA ACCEPT |
| METTP/gatC | A0B5K3 | GO:0070681 | IEA ACCEPT |
| PSEPK/glnS | Q88IU5 | GO:0006425 | GO:0006425 IEA ACCEPT; GO:0006424 IEA REMOVE |
| PSEPK/gltX | Q88LF6 | GO:0006424 | IEA ACCEPT |
| PSEPK/serS | Q88FT2 | GO:0006434 | IEA ACCEPT |

### Reviews affected only in `existing_annotations` (2)

- **DANRE/gtpbp3** (Q501Z5) — six IMP annotations, all from PMID:30916346, to
  GO:0070143 / GO:0070153 / GO:0070154 / GO:0070155 / GO:0070183 / GO:0070184.
  All six are already `MARK_AS_OVER_ANNOTATED` here. See below.
- **human/AARSD1** (Q9BTE6) — GO:0006419 IEA (GO_REF:0000002), already `REMOVE`.
  AARSD1 is an editing-domain-only paralogue that does not charge tRNA, so the
  obsoletion is orthogonal: the annotation should go regardless of which BP term
  survives.

### Reviews carrying only the replacement terms (2, unaffected)

**human/AIMP1** (Q12904) and **human/AIMP2** (Q13155) each carry `GO:0006418`
(NAS, ACCEPT) and no obsoleted term. They gain company rather than losing scope.
Worth a re-check pass only.

### The gtpbp3 case is worth flagging upstream

`GO:0070153 mitochondrial leucyl-tRNA aminoacylation` and
`GO:0070155 mitochondrial methionyl-tRNA aminoacylation` have **exactly one
annotation each in all of GOA**, and in both cases it is zebrafish `gtpbp3`
(UniProtKB:Q501Z5, IMP, PMID:30916346, ZFIN) — verified via the QuickGO
annotation API on 2026-08-29. The entire existence of those two terms in the
annotation corpus rests on a single paper about a protein that is **not a
synthetase**: GTPBP3 is a tRNA-modifying GTPase that installs τm⁵U at the wobble
position.

This repo's existing gtpbp3 review already reached that conclusion independently,
noting that "gtpbp3KO zebrafish showed increased efficiencies of tRNA
aminoacylation", which is inconsistent with gtpbp3 acting as a direct ligase and
instead reflects an indirect consequence of altered tRNA modification.

The merge would silently roll all six of these into one `GO:0070127`, converting
a visible six-fold over-annotation into a single plausible-looking one. **These
six annotations should be withdrawn rather than migrated**, and that is worth
saying on go-annotation#6525 while the batch is still being assembled — it is
exactly the kind of case a bulk term-replacement will otherwise launder.

### Module impact

`modules/bacterial_aminoacyl_trna_charging.yaml` is affected twice:

- Its `indirect_gatabc_route` node carries `GO:0070681` as a `concepts` term.
- Its module-level `evidence.source_id` is `GO:0043039`, which has been **renamed
  to `tRNA charging`**. The id is stable and the old label survives as an exact
  synonym, so nothing breaks — but the recorded `title: tRNA aminoacylation`
  should be refreshed to match.

See also the
[PSEPK ppu00970 aminoacyl-tRNA biosynthesis batch](P_PUTIDA/batches/ppu00970_bacterial_aminoacyl_trna_charging.md),
which curated eight of the PSEPK reviews listed above.

## Mappings flagged for redirection

Upstream lists a large InterPro2GO / UniRule / HAMAP2GO / MetaCyc2GO block —
roughly 100 mappings across the 43 terms. These are the source of the ~30–50k
electronic annotations per term. Not independently verified here; see
go-annotation#6525 for the full list. Two observations:

- Every mapping is from a **family/domain signature for a specific synthetase**
  (e.g. `IPR002317 Serine-tRNA ligase, type1` → GO:0006434). Redirecting these to
  `GO:0006418` discards real information unless the corresponding **MF** mapping
  is also present. The MF mappings largely do exist, but this should be confirmed
  per-signature rather than assumed — a signature that maps only to the BP would
  silently lose its substrate specificity.
- `GO:0070681` has a `metacyc2go` mapping (`MetaCyc:PWY-5921`) that the other
  terms lack, consistent with it being a genuine pathway rather than a
  single-step process — another reason to confirm its inclusion in the batch.

## Scope

- **Organisms**: broad. In-repo: human (5), PSEPK (6), POPTR (2), DANRE (1),
  METTP (1). Upstream: SGD/FlyBase/EcoCyc-dominant, i.e. yeast, fly and *E. coli*.
- **GO branch**: BP only. **No MF term is obsoleted** — the 20 `<aa>-tRNA ligase
  activity` terms and `GO:0050567` all remain, and are where specificity now lives.
- **Type of fix**: structural, but with a genuine curation-philosophy component.
  Unlike a pure merge, this one **contradicts recorded reasoning in four reviews**
  and requires those to be re-argued, not just re-pointed.

## Candidate genes for initial review

Priority order.

1. **PSEPK/glnS, PSEPK/gltX, PSEPK/serS, human/AARS1** — highest priority. These
   four carry the inverted `GO:0006418` judgments. They need a re-argued review,
   not an id swap, and they are the ones that will look actively wrong once the
   merge lands.
2. **human/AARS2** (Q5JTZ9) — the `proposed_replacement_terms: GO:0070143` is
   already a dangling target. Also carries an IMP on PMID:21549344 that is a
   genuine upstream experimental annotation.
3. **DANRE/gtpbp3** (Q501Z5) — the six-annotation over-annotation cluster; the
   sole basis for two of the obsoleted terms. Should drive an upstream comment
   before the batch is finalised.
4. **The five GatCAB reviews** (POPTR/GATC, PSEPK/gatA, PSEPK/gatB, PSEPK/gatC,
   METTP/gatC) — all hinge on `GO:0070681`, whose inclusion in the
   batch is the open question above. Hold until that is settled.
5. **POPTR/ALARS** (B9HQZ6) — clean mechanical case; IBA + IEA, both ACCEPT, one
   `core_functions` entry.
6. **human/AARSD1** (Q9BTE6) — already `REMOVE`; confirm the removal survives the
   merge rather than being migrated to `GO:0006418`.
7. **Not yet in repo, worth adding**: *E. coli* `valS` (P07118) is the **sole**
   annotation to `GO:0061475`, and yeast `MSR1` (P38714) / `MSE1` (P48525) are
   the sole annotations to `GO:0070144` / `GO:0070149` (all verified via QuickGO,
   2026-08-29). Three single-annotation terms, three reviewable genes — a cheap
   way to cover the long tail of this batch.

## Proposed approach

1. **Do not edit gene reviews yet.** go-ontology#15375 is still open and the
   43-vs-42 question is unresolved. Editing `core_functions` now would desynchronise
   eleven reviews from GOA for no gain.
2. **Comment on go-annotation#6525** with the two findings this repo can
   contribute that are not in the upstream thread: (a) the gtpbp3 cluster should
   be withdrawn rather than migrated, with the single-annotation evidence above;
   (b) confirm whether `GO:0070681` is in the batch, since its MF counterpart and
   MetaCyc mapping make it structurally unlike the other 42.
3. **When the obsoletion lands**: re-point the eleven `core_functions` entries to
   `GO:0006418` / `GO:0070127`, re-run `just validate` per gene, and re-fetch GOA
   so `existing_annotations` pick up the replacements.
4. **Re-argue, don't re-point, the four inverted reviews.** Each needs its
   specificity claim relocated to the MF slot and its `reason` text rewritten.
   Record the general pattern in [OVER_ANNOTATION_PATTERNS](OVER_ANNOTATION_PATTERNS.md).
5. **Refresh the module**: update `modules/bacterial_aminoacyl_trna_charging.yaml`
   — the `GO:0043039` evidence title, and the `GO:0070681` concepts term if it is
   confirmed in the batch.

## Priority

**High** — the highest of the obsoletion projects currently in this repo. Fifteen
reviews are affected, eleven contain strictly-validated `core_functions` ids that
must change, and four contain reasoning the obsoletion directly contradicts. The
upstream ontology work is actively moving (two PRs merged in the last week), so
the window for contributing the gtpbp3 finding is now.

## Status

- **2026-08-29** — Project file created. Tracking go-annotation#6525 (updated
  2026-08-28) and go-ontology#15375 (open since 2018; PRs #32537 and #32541
  merged 2026-08-26/27). Obsoletion not yet applied. All 43 terms plus
  `GO:0006418`, `GO:0070127`, `GO:0004813` and `GO:0050567` confirmed live in
  QuickGO; per-term annotation counts, the six zero-annotation mitochondrial
  terms, and the single-annotation attributions for `GO:0061475`, `GO:0070144`,
  `GO:0070149`, `GO:0070153` and `GO:0070155` all verified via the QuickGO
  annotation API. In-repo impact enumerated by parsing all 15 affected review
  YAMLs. No upstream comment posted yet.
