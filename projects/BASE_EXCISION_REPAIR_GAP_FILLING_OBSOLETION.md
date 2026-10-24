---
title: "Base-Excision Repair, Gap-Filling (GO:0006287) — Obsoletion & Patch-Length Split"
maturity: SCOPING
tags: [OBSOLETION]
species:
  - human
  - mouse
  - rat
  - worm
  - yeast
  - ARATH
# Gene products holding GO:0006287, i.e. the scope of the remap --
# not a coverage claim: only APEX1, FEN1 and ADPRS have reviews here.
genes:
  - APEX1
  - FEN1
  - ADPRS
  - POLB
  - LIG1
  - LIG3
  - PARG
  - NEIL1
  - PNKP
  - POLD1
  - POLE
  - POLG
  - POLL
  - PCNA
---

# Base-Excision Repair, Gap-Filling (GO:0006287) — Obsoletion & Patch-Length Split

**Bottom line:** GO is obsoleting `GO:0006287 base-excision repair, gap-filling`
as an unnecessary grouping term — every base-excision repair ends in gap
filling, and the real branch point in the pathway is patch length. Two
replacement children of `GO:0006284 base-excision repair` were created on
2026-10-16 and merged: `GO:7770137 short-patch base-excision repair` and
`GO:7770138 long-patch base-excision repair`. Because the obsoleted term is
patch-length-agnostic while both replacements are patch-length-specific, there
is **no mechanical `replaced_by`**: every annotation has to be sorted into a
branch or dropped back to the parent. We inventoried all 9,941 current
annotations from QuickGO, and the useful result is that they collapse into a
handful of decisions rather than ten thousand: 97% descend from two PAINT nodes
seeded by human POLD1 and POLE (both long-patch), and the 12 Reactome TAS rows
come from exactly four pathway-to-GO mappings whose Reactome names already
state their patch length. Three reviews here carry the term (APEX1, FEN1,
ADPRS), and for all three the obsoletion is a precision gain. Status: scoped,
not started.

## Overview

`GO:0006287` was created to capture the repair-synthesis end of base-excision
repair (BER). The upstream objection is that this is not a distinguishing
feature: *all* BER includes gap filling, so the term groups nothing. What does
distinguish BER sub-pathways is the length of the repair tract, and that split
is mechanistically real:

- **Short-patch (single-nucleotide) BER** — one nucleotide is inserted into the
  one-nucleotide gap at the incised abasic site, the 5'-deoxyribose-5-phosphate
  residue is removed by dRP **lyase** activity, and the nick is ligated.
- **Long-patch BER** — strand-displacement synthesis adds two or more
  nucleotides, generating a 5' flap that carries the abasic sugar-phosphate;
  the flap is removed by a 5'-**flap endonuclease** and the nick is ligated.
  This route is PCNA-dependent and is used when the 5'-terminal sugar is
  refractory to dRP lyase (for example an oxidised or reduced abasic residue).

The two branches share the glycosylase and AP-incision steps and diverge at
repair synthesis. So the obsoletion is not a redundancy cleanup with a clean
`replaced_by` target — it is a **re-sorting**: each existing annotation moves
to `GO:7770137`, to `GO:7770138`, or (where the evidence does not resolve
patch length) up to the parent `GO:0006284`.

### The replacement is also a change of scope, not just of granularity

This is easy to miss and it changes several of the per-row judgments below.
`GO:0006287` named a **step** — its definition is the combined action of an AP
endonuclease and a polymerase synthesising a patch. Both replacements name a
**sub-pathway**: each is `is_a GO:0006284`, each definition runs from the
incised abasic site through ligation, and their shared `comment` states that
the two branches "share the initial glycosylase and abasic-site incision steps
and diverge at repair DNA synthesis". Incision is therefore *inside* both new
terms, where it was the upstream boundary of the old one.

Consequently, "this gene product does not perform the gap-filling step" is an
argument against the **old** term that does not automatically transfer to the
new ones. Anywhere that reasoning appears in an existing review — and it
appears in two of the three reviews affected here — it has to be re-derived
against the sub-pathway definition rather than carried across.

This project tracks the impact on AI Gene Review, proposes per-mapping
destinations for the Reactome rows, and queues the gap-filling polymerases and
ligases for review, since almost none of them are reviewed here yet.

## Upstream tickets

- Annotation tracker:
  [geneontology/go-annotation#6627](https://github.com/geneontology/go-annotation/issues/6627)
- Obsoletion request:
  [geneontology/go-ontology#32760](https://github.com/geneontology/go-ontology/issues/32760)
  (open)
- New-term request for the two replacements:
  [geneontology/go-ontology#32759](https://github.com/geneontology/go-ontology/issues/32759)
  (closed), implemented in
  [PR #32765](https://github.com/geneontology/go-ontology/pull/32765) (merged)
- Affected-annotation spreadsheet (upstream-curated):
  https://docs.google.com/spreadsheets/d/1IHa0Tn96BuvYzwDR3yUQc54mJD_qRqJv3F8gVauYqYA/edit

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| base-excision repair, gap-filling (BP) | `GO:0006287` | `GO:7770137 short-patch base-excision repair` **or** `GO:7770138 long-patch base-excision repair`, falling back to `GO:0006284 base-excision repair` where the evidence does not distinguish the branches |

Term metadata, verified 2026-10-17:

- `GO:0006287` (`base-excision repair, gap-filling`) — still **live and
  non-obsolete** in OLS (`is_obsolete: false`, no children). The obsoletion
  request is open; the annotation re-sorting is expected to precede it.
- `GO:7770137` (`short-patch base-excision repair`) — created 2026-10-16,
  `is_a GO:0006284`, definition cites PMID:19153658. Exact synonyms include
  "base-excision repair, short-patch", "short-patch BER", "single-nucleotide
  BER", "SN-BER", "SP-BER". Verified from the merged `go-edit.obo` diff in
  go-ontology PR #32765 rather than from OLS, which has not yet picked up the
  release.
- `GO:7770138` (`long-patch base-excision repair`) — created 2026-10-16,
  `is_a GO:0006284`, definition cites PMID:19153658. Exact synonyms include
  "base-excision repair, long-patch", "long-patch BER", "LP-BER",
  "multinucleotide BER". Same source.
- `GO:0006284` (`base-excision repair`) — live, has children; the fallback
  parent.

Note that the **labels differ from the request**: go-ontology#32759 asked for
"base-excision repair, short-patch" / "base-excision repair, long-patch", and
the terms were created as "short-patch base-excision repair" /
"long-patch base-excision repair", with the requested forms kept as exact
synonyms. Use the created labels in annotations here.

## Annotation inventory (verified via QuickGO, 2026-10-17)

`goId=GO:0006287`, `goUsage=exact` (the term has no children, so this is the
complete set): **9,941 annotations**, all biological_process.

| Evidence | ECO | Rows | Source |
|---|---|---|---|
| IEA | ECO:0007826 | 9,437 | TreeGrafter (GO_REF:0000118) |
| IBA | ECO:0000318 | 214 | GO_Central PAINT (GO_REF:0000033) |
| IEA | ECO:0000265 | 132 | Ensembl Compara (GO_REF:0000107) |
| IEA | ECO:0000501 | 120 | UniProt combined multi-method IEA (GO_REF:0000120) |
| TAS | ECO:0000304 | 14 | Reactome (12) + MGI (2) |
| ISO | ECO:0000266 | 10 | RGD (7, GO_REF:0000121) + GO_Central (3, GO_REF:0000119) |
| IDA | ECO:0000314 | 7 | UniProt, MGI, TAIR |
| ISS | ECO:0000250 | 3 | UniProt (GO_REF:0000024) |
| IMP | ECO:0000315 | 3 | MGI, CACAO |
| ISA | ECO:0000247 | 1 | MGI |

By assigning group: TreeGrafter 9,437; GO_Central 217; UniProt 127; Ensembl
114; EnsemblPlants 17; Reactome 12; MGI 7; RGD 7; CACAO 1; EnsemblMetazoa 1;
TAIR 1 — 9,941 in total.

**The experimental count matches upstream exactly** (10 = MGI 4 + UniProt 4 +
TAIR 1 + CACAO 1), as does the Reactome tally (12 TAS from 4 pathway mappings).

**One discrepancy to confirm with upstream.** The tracker states "All 85 IEA
annotations are phylogenetic projections: Ensembl Compara (GO_REF:0000107, 34)
and TreeGrafter (GO_REF:0000118, 51)". QuickGO today returns 9,689 IEA rows
(9,437 TreeGrafter + 132 Compara + 120 `GO_REF:0000120`), i.e. two orders of
magnitude more, and adds a third reference the tracker does not name. The
upstream figure was presumably taken from a filtered or
reference-proteome-restricted snapshot. The *shape* of the upstream conclusion
holds for this term's rows — see the `GO_REF:0000120` check below — but the
volume matters for whoever executes the mechanical remap, so the snapshot basis
is worth pinning down.

**`GO_REF:0000120` is not itself a projection pipeline, but these 120 rows are
projections.** The reference is UniProt's *combined* automated annotation from
multiple IEA methods, so membership does not by itself say the row came from an
ortholog; this repo's own classifier only counts such a row as electronic
orthology when its `WITH/FROM` names an Ensembl protein or a PANTHER node
(the `ensembl|PANTHER` gate in `classify()`, `src/ai_gene_review/export/propagation_rows.py`). Checked rather than
assumed: all 120 rows are UniProt-assigned and **every one** carries all three
— a UniProtKB donor, an `ensembl` protein id, and a `PANTHER` node — and the
donors are only two accessions, `Q07864` (human POLE, 64 rows) and `P28340`
(human POLD1, 56 rows). So these rows do follow the POLD1/POLE decisions, by
the same logic as the IBA and TreeGrafter tails, though the PANTHER nodes they
cite are per-protein grafted nodes rather than the two IBD nodes below.

### The whole IEA/IBA tail reduces to two PAINT nodes

The 214 IBA rows — all of them, across both result pages — come from exactly
**two** PAINT ancestral nodes, read from their `WITH/FROM` fields:

| PAINT node | Seeded from | IBA rows |
|---|---|---|
| `PANTHER:PTN000035478` | `MGI:97741` (mouse Pold1) + `UniProtKB:P28340` (human POLD1) | 121 |
| `PANTHER:PTN000072300` | `UniProtKB:Q07864` (human POLE) | 93 |

Both seeds are **long-patch** polymerases, and the TreeGrafter tail tracks the
same families: in a 800-row sample across four pages of the 9,437 IEA rows,
every recognisable gene symbol was a DNA polymerase δ or ε catalytic subunit
ortholog (POLD1, POLE, *S. cerevisiae* POL3/POL2, POLD, DNAPOL-DELTA), the rest
being unnamed locus identifiers. So the 9,651 propagated rows are not 9,651
separate judgments: they are two IBD node placements, and **both should move to
`GO:7770138 long-patch base-excision repair`** unless the PAINT curator wants
to argue that the ancestral function was patch-length-agnostic, in which case
`GO:0006284` is the right node annotation and the branch terms stay
experimental-only.

## Reactome: four pathway mappings, three of them already patch-specific

This is where this repo can contribute something upstream does not list. All 12
Reactome TAS rows are pathway-to-GO exports, and each source pathway's own
Reactome name states its patch length — so the destination term follows
directly, with no need to read the member reactions:

| Reactome pathway | Name | Rows | Proposed destination |
|---|---|---|---|
| `R-HSA-110381` | Resolution of AP sites via the **single-nucleotide** replacement pathway | 2 (POLB, LIG3) | `GO:7770137` short-patch |
| `R-HSA-5649702` | APEX1-Independent Resolution of AP Sites via the **Single Nucleotide** Replacement Pathway | 4 (POLB, LIG3, NEIL1, PNKP) | `GO:7770137` short-patch |
| `R-HSA-110373` | Resolution of AP sites via the **multiple-nucleotide patch** replacement pathway | 5 (POLB, LIG1, FEN1, PARG, ADPRS) | `GO:7770138` long-patch |
| `R-HSA-73933` | Resolution of Abasic Sites (AP sites) | 1 (APEX1) | `GO:0006284` base-excision repair |

`R-HSA-73933` is the parent pathway containing both branches, so it cannot take
either branch term; the parent BER term is the only correct export for it. Each
mapping was read from the pathway's own `goBiologicalProcess` field via the
Reactome ContentService on 2026-10-17, and all four currently point at
`GO:0006287`.

Two rows in this set are PAR-turnover enzymes rather than gap-filling
machinery, `ADPRS` and `PARG`, and they need **different** treatment — the
scope shift described above separates them.

- **ADPRS: drop, do not remap.** The argument that survives the scope shift is
  the compartment one, worked out in detail in the ADPRS review: Reactome nests
  a mitochondrial-matrix PAR hydrolase reaction inside a nucleoplasmic
  long-patch BER pathway, so the *export route* is invalid regardless of how
  the destination term is scoped. "Drop" here means do not mint a replacement
  row; it is not a recommendation to change that review's action, which
  deliberately chose `MARK_AS_OVER_ANNOTATED` over `REMOVE` on the reasoned
  ground that the route is invalid while the biology is not false.
  `GO:0006281 DNA repair` (IMP, human experimental) already carries ADPRS's
  real involvement at the right granularity.
- **PARG: needs review; fall back to `GO:0006284` meanwhile.** There is no
  compartment argument here — PARG is nucleoplasmic — and the only argument
  against the row was that PARG performs no gap-filling step, which is exactly
  the reasoning the scope shift invalidates. `R-HSA-110373`'s own summary puts
  PAR metabolism inside the sub-pathway: long-patch BER "can be completed by
  continued POLB-mediated DNA strand displacement synthesis in the presence of
  PARP1 or PARP2, FEN1 and DNA ligase I". That names the PAR *writers* rather
  than PARG the eraser, so it does not settle the question — but it does mean
  the sub-pathway term cannot be ruled out a priori, and the honest
  recommendation is the parent term pending a review of PARG itself
  (candidate 8 below).

So do not send a blanket "drop both" to upstream.

The two MGI TAS rows (mouse Polb, PMID:10197627 and PMID:10655502) are
knockout-phenotype papers on alkylation sensitivity and immunoglobulin
mutation; neither title speaks to patch length, so they need the full text or a
fallback to `GO:0006284`.

## Affected experimental annotations (10)

All 10 experimental rows, retrieved from QuickGO 2026-10-17, with the branch
assignment the cited paper's title supports. Where the title does not resolve
patch length we say so rather than guessing — these are the rows that need a
curator to read the paper.

| # | Group | Accession | Symbol | Organism | Evidence | Reference | Paper title (PubMed) | Proposed destination |
|---|---|---|---|---|---|---|---|---|
| 1 | UniProt | UniProtKB:P28340 | POLD1 | Human | IDA | PMID:10559260 | *Long patch base excision repair with purified human proteins. DNA ligase I as patch size mediator for DNA polymerases delta and epsilon* | `GO:7770138` long-patch — stated in the title |
| 2 | UniProt | UniProtKB:Q07864 | POLE | Human | IDA | PMID:10559260 | as above | `GO:7770138` long-patch |
| 3 | UniProt | UniProtKB:P28340 | POLD1 | Human | IDA | PMID:10559261 | *Reconstitution of proliferating cell nuclear antigen-dependent repair of apurinic/apyrimidinic sites with purified human proteins* | `GO:7770138` long-patch — PCNA-dependent AP-site repair is the long-patch route by definition |
| 4 | CACAO | UniProtKB:A0FLQ6 | polq-1 | *C. elegans* | IMP | PMID:21917855 | *Single-nucleotide base excision repair DNA polymerase activity in C. elegans in the absence of DNA polymerase β* | `GO:7770137` short-patch — stated in the title |
| 5 | MGI | UniProtKB:P17918 | Pcna | Mouse | IDA | PMID:15177179 | *Aphidicolin-resistant and -sensitive base excision repair in wild-type and DNA polymerase beta-defective mouse cells* | needs full text; the aphidicolin-sensitive activity is the pol δ/ε route, so `GO:7770138` is likely, but the paper probes both branches |
| 6 | MGI | UniProtKB:P52431 | Pold1 | Mouse | IMP | PMID:15177179 | as above | needs full text; same reasoning as #5 |
| 7 | MGI | UniProtKB:Q8K409 | Polb | Mouse | IMP | PMID:15177179 | as above | needs full text; pol β is the short-patch polymerase but also initiates long-patch synthesis |
| 8 | MGI | UniProtKB:P54098 | POLG | Human (!) | IDA | PMID:15177179 | as above | see the accession query below before remapping |
| 9 | UniProt | UniProtKB:Q9UGP5 | POLL | Human | IDA | PMID:19806195 | *Characterization of a natural mutator variant of human DNA polymerase lambda which promotes chromosomal instability by compromising NHEJ* | needs full text; the title is about non-homologous end joining, so the BER claim is in the body |
| 10 | TAIR | UniProtKB:Q9FNY4 | POLL | *A. thaliana* | IDA | PMID:38217735 | *The enzymatic properties of Arabidopsis thaliana DNA polymerase λ suggest a role in base excision repair* | needs full text; the title asserts BER generally, so `GO:0006284` unless the body resolves patch length |

Rows 5–8 are all the same reference and the same assay series; a single reading
of PMID:15177179 settles four annotations at once, which makes it the highest-value
paper in the set.

### Two data queries for MGI

Both come out of row 8 and are worth resolving *before* the remap, since
remapping propagates whatever is already wrong.

1. **`P54098` is the human accession.** `P54098` is `DPOG1_HUMAN` (human POLG);
   mouse Polg is `P54099` (`DPOG1_MOUSE`). QuickGO reports row 8 as
   `assignedBy: MGI`, `taxonId: 9606` — an MGI-assigned IDA sitting on a human
   protein, sourced from a paper in mouse cells, with the correct mouse
   accession one digit away. A single-digit transposition is the obvious
   explanation, but we have not confirmed it with MGI, so it is raised as a
   question rather than asserted.
2. **The `Poll` ISA infers pol λ from pol γ.** Row 11 of the non-experimental
   set (mouse `Q9QXE2` Poll, ISA, PMID:15177179, assigned by MGI) carries
   `WITH/FROM: UniProtKB:P54098` — an inference from sequence alignment to
   *that same* human POLG accession. Pol λ (X family) and pol γ (A family) are
   not in the same polymerase family, so an alignment-based transfer between
   them needs an explanation. If query 1 resolves as a typo, this `WITH/FROM`
   inherits the correction.

## Impact on this repo

Three gene reviews carry `GO:0006287` rows; all three come from Reactome TAS,
and in all three cases the obsoletion improves the annotation.

| Gene | Row source | Current review action | Recommended on obsoletion |
|---|---|---|---|
| FEN1 | `Reactome:R-HSA-110373` | `ACCEPT` | `MODIFY` with `proposed_replacement_terms: [GO:7770138 long-patch base-excision repair]` — the row's own GOA-sourced id is not rewritten (see *Proposed approach*). A clean precision gain: the review's own reason already says "the standard GO term for participants in the long-patch BER sub-pathway". **Also fix `core_functions`** — the 5'-flap endonuclease activity entry lists *both* `GO:0006287` and `GO:0006284` under `directly_involved_in`, so swapping the id in place would leave a term and its own parent side by side. Replace the pair with `GO:7770138` alone. |
| APEX1 | `Reactome:R-HSA-73933` | `ACCEPT` | `MODIFY` with `proposed_replacement_terms: [GO:0006284 base-excision repair]` — a generalisation rather than a refinement, and a term APEX1 already carries twice (IBA `GO_REF:0000033`, IDA PMID:8932386), which CLAUDE.md asks be stated in the reason. Both the row's `summary` ("participates in BER gap-filling by coordinating with DNA polymerase beta") and its `reason` ("APEX1's role in the downstream steps of BER where the gap is filled") need rewriting while we are in the file — but **not** to "APEX1 does not fill the gap", which under the new sub-pathway terms would argue against `GO:0006284` too, a term APEX1 holds by IDA. The correct reason is that `R-HSA-73933` is the branch-agnostic parent pathway, so this evidence does not resolve patch length; APEX1 in fact incises in both branches, which is an independent argument for the parent. |
| ADPRS | `Reactome:R-HSA-110373` | `MARK_AS_OVER_ANNOTATED` | **Propose no replacement**, and keep the action as it stands. When GOA drops the row, set `retired: true` and keep the row and its review rather than deleting either. The review traced this row to a compartment mismatch in Reactome's pathway nesting, which is the one argument here that is unaffected by the scope shift; `GO:0006281 DNA repair` (IMP, human experimental) carries ADPRS's real involvement at the right granularity. That review considered and declined `REMOVE` on reasoned grounds, and retirement is not a `REMOVE`. |

Of the gene products named above, only these three are reviewed here (the
term's full 9,941 rows span thousands of orthologs). RAD27 is reviewed and is named in
go-ontology#32759 as a gene product to annotate with long-patch BER; it
currently carries `GO:0006284` (IEA) and no `GO:0006287`, so it is a candidate
for a `NEW` long-patch row rather than a remap — subject to the usual
participation test, which it passes on the face of it, since flap cleavage is
one of the defining steps of the long-patch branch.

## Candidate genes for initial review

Ordered by how much a review would contribute to the remap rather than by
prominence. The first three are gap-filling core machinery whose branch
assignment is the whole question; none has a review here.

1. **POLB** (human, `P06746`) — the short-patch polymerase and the only gene
   product appearing in three of the four Reactome mappings (both
   single-nucleotide pathways and the multiple-nucleotide one). Its review has
   to split short- from long-patch participation explicitly, so it is the
   natural exemplar for this project.
2. **POLD1** (human, `P28340`) — long-patch polymerase and the seed of PAINT
   node `PTN000035478`, hence of 121 IBA rows and the bulk of the 9,437
   TreeGrafter projections. Reviewing it grounds the single largest remap
   decision.
3. **POLE** (human, `Q07864`) — long-patch polymerase and seed of
   `PTN000072300` (93 IBA rows). Same argument as POLD1.
4. **LIG3** (human, `P49916`) — ligase for both single-nucleotide pathways,
   including the APEX1-independent one; pairs with POLB.
5. **LIG1** (human, `P18858`) — the long-patch ligase, and PMID:10559260 casts
   it as the patch-size mediator, which makes it the most interesting gene in
   the set for the short/long distinction itself.
6. **POLL** (human, `Q9UGP5`) — two of the ten experimental rows are pol λ
   (human and Arabidopsis) and both need the full text; a review would resolve
   them together.
7. **PNKP** (human, `Q96T60`) and **NEIL1** (human, `Q96FI4`) — the
   APEX1-independent short-patch route; worth reviewing as a pair because that
   pathway's whole point is bypassing AP endonuclease.
8. **PARG** (human, `Q86W56`) — the Reactome row we deliberately leave
   unresolved, recommending the parent term pending review. The question is
   whether PAR erasure is inside the long-patch sub-pathway; the method already
   applied to ADPRS would settle it, without the compartment shortcut that
   case had.
9. **RAD27** (yeast) — already reviewed; revisit to consider a `NEW`
   `GO:7770138` row, as go-ontology#32759 proposes.
10. **POL4** (yeast) — named upstream as the short-patch example
    (`SGD:S000000607`); no review here and no `GO:0006287` row, so this is a
    gap-filling candidate rather than a remap.

## Proposed approach

**A GOA-sourced term id is never rewritten, so the in-repo work splits into
three phases with different gates.** The previous version of this page said to
"change the row id" once the new terms were in a GO release. Both halves of that
were wrong. CLAUDE.md is explicit — "do not rewrite an existing-annotation id
just to satisfy validation" — because those ids are GOA provenance, not
curator-chosen values; the obsoletion-specific form is stated in
[Entner-Doudoroff](ENTNER_DOUDOROFF_OBSOLETION.md), where "the change is carried
in `action` plus `proposed_replacement_terms` instead", and `genes/PSEPK/edd`
still carries the obsolete `GO:0009255` as its row id with `action: MODIFY` and
`proposed_replacement_terms: [GO:0061678]`. The row's own term only ever changes
when GOA changes, which for a Reactome TAS row means Reactome remapping its
pathway export and a fresh `just fetch-gene` — at which point the old row is
**retired**, not deleted (`docs/goa_source_refresh.md`: set `retired: true`,
"retain its original source and review", "do not delete the historical record";
`GOAValidator` skips retired rows, so an orphaned retired row is not an error).

| Phase | Edit | Gate |
|---|---|---|
| 1 | `action: MODIFY` + `proposed_replacement_terms` on the FEN1 and APEX1 rows | **none** — doable now |
| 2 | FEN1 `core_functions` `directly_involved_in` → `GO:7770138` | a GO release `linkml-term-validator` resolves (author-supplied ids are hard validated) |
| 3 | the rows' own terms | Reactome remap + `just fetch-gene`, then `retired: true` on the old rows and review of the reseeded `PENDING` ones |

Phase 1 was verified locally rather than assumed: adding `action: MODIFY` with
`proposed_replacement_terms: [{id: GO:7770138, label: long-patch base-excision
repair}]` to the FEN1 row leaves `just validate human FEN1` passing (`✓ Valid`),
even though `GO:7770138` is not yet in our ontology cache —
`proposed_replacement_terms` has a plain `Term` range and is not enum-bound. It
adds exactly one new warning, and usefully so: *"Process term GO:0006287 ... is
not reflected in existing_annotations"*, pointing at the `core_functions` entry
that still names the old term. That is phase 2's job, so the two phases are
coupled: expect that warning to stand between them.

1. **Send upstream the Reactome mapping table.** The four pathway-to-GO
   mappings are the highest-leverage fix in this obsoletion (12 TAS rows, three
   of them already self-describing as single- or multiple-nucleotide), and
   go-annotation#6627 lists them as needing review without proposing
   destinations. Carry over the ADPRS drop recommendation, but send PARG as
   "parent term pending review" rather than as a second drop. This is also what
   unblocks phase 3.
2. **Raise the two MGI data queries** (the `P54098`/`P54099` accession and the
   pol λ–from–pol γ `WITH/FROM`) before the remap runs.
3. **Work the three phases above.** Per gene:
   - **FEN1** — phase 1 `MODIFY` → `GO:7770138`; phase 2 collapse the
     `core_functions` `directly_involved_in` pair (it holds `GO:0006287` *and*
     `GO:0006284`) to `GO:7770138` alone, which also clears the warning phase 1
     introduces.
   - **APEX1** — phase 1 `MODIFY` → `GO:0006284`, a term APEX1 already holds by
     IBA and IDA, so say so in the reason as CLAUDE.md asks. Rewrite both the
     `summary` and the `reason` against the sub-pathway definition, per the
     table above. No phase 2 work: `GO:0006284` is already in the ontology.
   - **ADPRS** — no `proposed_replacement_terms`, because the recommendation is
     that no replacement be minted; keep `MARK_AS_OVER_ANNOTATED` and note the
     obsoletion in the reason. At phase 3, set `retired: true` and **keep the
     row and its review** — the compartment analysis is the record of why this
     export route was wrong, and retirement records disappearance from the
     current snapshot rather than a biological `REMOVE`. Explain the retirement
     in `ADPRS-notes.md` as `docs/goa_source_refresh.md` directs.

   `grep` each file rather than editing the tabled line alone — FEN1 names
   `GO:0006287` in a third place (inside the `reason` of its `GO:0006281 DNA
   repair` row) and ADPRS has a dozen occurrences. Most of the ADPRS prose is
   *about* the historical Reactome mapping, so the id should stay there; mark it
   as obsoleted wherever the prose reads as a live term.
4. **Read PMID:15177179 once** and settle rows 5–8 together; then
   PMID:19806195 and PMID:38217735 for the two pol λ rows. **None of the ten
   experimental PMIDs is cached** in `publications/` — only PMID:17983848, a
   synonym source for the new terms, is — so cache them first. The branch
   assignments in the table above come from PubMed titles, which is enough to
   call the two rows whose titles say "long patch" and "single-nucleotide"
   outright and is not enough for the rest.
5. **Review POLB, POLD1, POLE** as the exemplar trio: short-patch, long-patch,
   long-patch. Their reviews determine both PAINT node placements and
   therefore the destination of ~97% of all rows.
6. **Confirm the IEA snapshot basis** with upstream so the mechanical remap is
   sized correctly (85 rows vs the 9,689 QuickGO returns today).

## Priority

**Medium-high.** The in-repo work is small — three files, none of them a large
edit, and the first phase (`MODIFY` plus `proposed_replacement_terms`) needs no
upstream change at all — but the upstream leverage is unusually good: a handful of
Reactome mapping decisions and two PAINT node decisions determine where 9,941
annotations land, and the obsoletion ticket is open right now with those
decisions unmade. The gap-filling polymerases and ligases are also a coherent,
well-characterised gene set that this repo has no coverage of at all, which
makes the exemplar reviews worth doing on their own terms.

## Status

Scoped on 2026-10-17 from go-annotation#6627. No reviews started. The in-repo
work is phased rather than wholly blocked — see the table under *Proposed
approach*: the `MODIFY` plus `proposed_replacement_terms` edits can be made now,
FEN1's `core_functions` entry waits on a GO release that
`linkml-term-validator` resolves (author-supplied ids are hard validated), and
only the rows' own terms wait on Reactome remapping its exports and a fresh
`just fetch-gene`. While waiting,
confirm the `GO:77701xx` allocation with the ontology editors: the ids here are
reported verbatim from the merged `go-edit.obo` patch, but the range is
unusual for GO, and it is cheap insurance before writing them into a
hard-validated slot.

## Related obsoletions

Other obsoletion projects that split a grouping term into mechanistically
distinct children, rather than merging a redundant one away, so the
"no clean `replaced_by`" problem recurs:

- [Amino Acid Activation](AMINO_ACID_ACTIVATION_OBSOLETION.md) — 43
  substrate-specific tRNA aminoacylation BPs
- [Neural Crest Formation](NEURAL_CREST_FORMATION_OBSOLETION.md) — per-row
  remapping with notes split by mechanism
