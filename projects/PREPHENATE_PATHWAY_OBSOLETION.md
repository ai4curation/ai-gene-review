# Aromatic Amino Acid Biosynthetic Process, Prephenate Pathway — Obsoletion

## Overview

A GO obsoletion proposal will obsolete `GO:0009095 aromatic amino acid family
biosynthetic process, prephenate pathway`. The term is a pre-composed
representation of two distinct downstream pathways (L-phenylalanine biosynthesis
and L-tyrosine biosynthesis) and corresponds to the combined MetaCyc
superpathway `PWY-3481 superpathway of L-phenylalanine and L-tyrosine
biosynthesis`. The two component pathways are already represented separately as
`GO:0009094 L-phenylalanine biosynthetic process` (xref MetaCyc:PWY-3462) and
`GO:0006571 L-tyrosine biosynthetic process` (xref MetaCyc:PWY-3461), so the
combined parent term is redundant.

The four experimental annotations on the upstream list are spread across three
genes/proteins in three organisms (Arabidopsis, Petunia, Mycobacterium
tuberculosis). The upstream issue was opened by Raymond Lee (WormBase), who
inspected each publication and proposed concrete actions — for the most part,
removal rather than relabeling, because none of the cited papers actually
establish a BP role in either component pathway. The annotation review ticket
itself (geneontology/go-annotation#6395) is assigned to Antonia Lock for
coordination of the per-group cleanup.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6395](https://github.com/geneontology/go-annotation/issues/6395)
- Ontology ticket: [geneontology/go-ontology#32005](https://github.com/geneontology/go-ontology/issues/32005)

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Suggested replacements |
|---|---|---|
| aromatic amino acid family biosynthetic process, prephenate pathway | GO:0009095 | GO:0009094 L-phenylalanine biosynthetic process and/or GO:0006571 L-tyrosine biosynthetic process |

Term labels and live status verified in OLS on 2026-05-14:
- `GO:0009095` — `aromatic amino acid family biosynthetic process, prephenate
  pathway` (still live; obsoletion proposed but not yet applied)
- `GO:0009094` — `L-phenylalanine biosynthetic process` (live)
- `GO:0006571` — `L-tyrosine biosynthetic process` (live)

The replacements are downstream subprocesses, not synonyms — moving an
annotation to a replacement is only valid if the supporting paper actually
establishes a role in phenylalanine or tyrosine biosynthesis specifically. The
reviewer's analysis suggests that for three of the four annotations, the
underlying papers do **not** support either replacement and the cleanest action
is removal.

## Affected experimental annotations (upstream list)

| # | Source | Accession | Symbol | Taxon | PMID | Evidence | Reviewer's proposed action |
|---|---|---|---|---|---|---|---|
| 1 | UniProt | UniProtKB:Q9SIE1 | PAT | NCBITaxon:3702 (Arabidopsis thaliana) | PMID:21102469 | EXP | Remove — paper does not show a BP role for Arabidopsis PAT |
| 2 | UniProt | UniProtKB:E9L7A5 | PPA-AT | NCBITaxon:4102 (Petunia hybrida) | PMID:21102469 | EXP | Reannotate to GO:0009094 L-phenylalanine biosynthetic process — Fig 1 shows PPA-AT RNAi affects L-Phe biosynthesis |
| 3 | TAIR | UniProtKB:Q9SIE1 (AGI: AT2G22250; Arabidopsis PAT) | PAT | NCBITaxon:3702 | PMID:20883697 | EXP | Remove — biochemical paper, no BP information |
| 4 | MTBBASE | UniProtKB:P9WIC1 | Rv0948c (intracellular chorismate mutase) | NCBITaxon:83332 (Mycobacterium tuberculosis H37Rv) | PMID:18727669 | EXP | Remove — biochemical/structural paper, no BP information |

Group impact tally (from upstream): UniProt 2, TAIR 1, MTBBASE 1.

UniProt protein names verified via UniProtKB REST on 2026-05-14:
- Q9SIE1 (Arabidopsis PAT): "Bifunctional aspartate aminotransferase and
  glutamate/aspartate-prephenate aminotransferase"
- E9L7A5 (Petunia PPA-AT): "Bifunctional aspartate aminotransferase and
  glutamate/aspartate-prephenate aminotransferase"
- P9WIC1 (M. tuberculosis Rv0948c): "Intracellular chorismate mutase"

## Mappings flagged for redirection

None. The upstream issue states there are no InterPro2GO, UniProt-Keywords, or
UniRule mappings to GO:0009095 (only the MetaCyc:PWY-3481 xref on the term
itself). The obsoletion is therefore a pure annotation/ontology cleanup with no
mapping fan-out.

## Impact on this repo

None of the three affected genes currently have an `*-ai-review.yaml` in this
repo (verified on 2026-05-14 via `find genes -iname '*PAT*' -path '*ARATH*'`,
`find genes -iname '*PPA*'`, and `find genes -iname '*Rv0948*'`). There is also
no existing project covering aromatic amino acid biosynthesis or chorismate
metabolism. This project is therefore a queueing exercise; no live reviews need
to be updated.

## Scope

- Organisms: Arabidopsis thaliana (1 gene, 2 annotations), Petunia hybrida
  (1 gene, 1 annotation), Mycobacterium tuberculosis H37Rv (1 gene, 1
  annotation).
- GO branch: biological process — aromatic amino acid biosynthesis.
- Type of fix: scientific. The obsoletion is not a rename — the parent term
  collapses two distinct downstream pathways. Three of the four cited papers
  are biochemical/structural and do not actually show a BP role, so the
  outcome for those is removal rather than remapping. Only the Petunia PPA-AT
  RNAi data in PMID:21102469 supports a replacement with `GO:0009094
  L-phenylalanine biosynthetic process`.

## Candidate genes for initial review

Listed in priority order. Each should be set up with
`just fetch-gene <organism> <gene>` before review begins.

1. **PPA-AT (Petunia hybrida, E9L7A5)** — Highest-value review on this list:
   the upstream proposal is to reannotate (not remove) this entry to
   `GO:0009094 L-phenylalanine biosynthetic process` based on Fig 1 RNAi
   evidence in PMID:21102469. The AI review should confirm the figure
   actually supports L-phenylalanine specifically (vs. tyrosine or both) and
   record the reannotation as MODIFY with the proposed replacement term.
2. **PAT (Arabidopsis thaliana, Q9SIE1)** — Carries two of the four affected
   annotations (PMID:21102469 + PMID:20883697). Both proposed actions are
   removal. Review should confirm that neither paper establishes a BP role and
   record REMOVE for each entry. PMID:20883697 in particular is a pure
   biochemical characterisation, so the BP annotation is best characterised as
   over-annotation.
3. **Rv0948c (Mycobacterium tuberculosis, P9WIC1)** — Intracellular chorismate
   mutase. PMID:18727669 is a biochemical/structural paper. Proposed action is
   removal. This is also a useful test case for cross-organism aromatic
   amino acid biosynthesis annotation patterns; chorismate mutase activity
   itself sits upstream of both phenylalanine and tyrosine biosynthesis but is
   not specific to either, so even a remap to `GO:0009094` or `GO:0006571`
   would not be defensible without in-vivo data.

## Proposed approach

1. **Wait for the obsoletion to land before bulk action.** GO ontology ticket
   #32005 is closed (Steven Marygold proposed it) but the annotation review
   ticket #6395 is still open with reviewer assigned (Antonia Lock). Per-gene
   AI reviews can proceed independently — the action codes (REMOVE vs MODIFY)
   are what matter and are stable regardless of obsoletion timing.
2. **Start with Petunia PPA-AT.** It is the only annotation on the list with a
   proposed positive replacement (MODIFY → GO:0009094). The PMID:21102469
   Fig 1 RNAi check is concrete and fast.
3. **Do the two Arabidopsis PAT annotations together.** Same gene, same
   organism — the two reviews share the gene-fetch and notes work, and the
   evidence base for both is biochemical-only. Likely outcome: REMOVE on both.
4. **M. tuberculosis Rv0948c last.** Mycobacterium chorismate mutase is a
   smaller scientific lift but is also the most clearly correct REMOVE on
   the list (biochemical/structural paper, no BP claim), so it is the
   lowest-priority confirmation review.
5. **No upstream mapping fan-out.** Unlike obsoletions that involve InterPro2GO
   or UniRule mappings, GO:0009095 has no such mappings — there is no
   additional flag-to-upstream task here.

## Priority

Low–Medium. The biology is mostly settled (the reviewer has already done the
hard work), and the affected gene set is small (3 genes, 4 annotations). The
Petunia PPA-AT review is the most interesting case because it converts a
generic prephenate-pathway annotation into a substrate-specific
phenylalanine-biosynthesis annotation; the rest are cleanup.

## Status

- 2026-05-14 — Project file created. Tracking upstream annotation issue #6395
  (opened 2026-05-13) and ontology issue #32005 (closed). Obsoletion not yet
  applied. No reviews started; none of the three affected genes are in this
  repo.
