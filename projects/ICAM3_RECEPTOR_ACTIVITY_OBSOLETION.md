---
title: "ICAM-3 Receptor Activity — Obsoletion & Replacement"
maturity: SCOPING
last_reviewed: 2026-10-04
tags: [OBSOLETION]
species: [human]
manifest:
  slides:
    - href: ICAM3_RECEPTOR_ACTIVITY_OBSOLETION/slides/ICAM3_RECEPTOR_ACTIVITY_OBSOLETION-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/4Uucr6PiddSxk9TztWyqsp
      title: Project brief
---

# ICAM-3 Receptor Activity — Obsoletion & Replacement

**Bottom line:** GO has obsoleted the molecular function term GO:0030369
*ICAM-3 receptor activity*, because ICAM3 is a ligand for several unrelated
receptors (the integrins ITGAL:ITGB2 and ITGAD:ITGB2, and C-type lectins
such as CLEC4M and CD209), and one ligand-named term fits none of them
precisely: it lumps biochemically distinct receptors together and names the
ligand rather than the activity. The replacement is the parent GO:0004888
*transmembrane signaling receptor activity*, with the ligand recorded as a
`has_input` ICAM3 (UniProtKB:P32942) extension. We checked the affected
annotations: three human rows assigned by UniProt (ITGAL and ITGB2, IMP from
PMID:19029120; CLEC4M, NAS from PMID:11257134), plus about 155 Ensembl
Compara IEA projections that followed them in the 2026-05-30 QuickGO pull.
No review in this repo uses the obsolete term, and none of ITGAL, ITGB2,
CLEC4M, CD209, ITGAD or ICAM3 has been fetched here yet. Scoped, not yet
started: the obsoletion has landed, the annotation tracker remains open, and
the CLEC4M NAS row is the one that most needs a curator's eye because its
ICAM3 binding depends on glycans.

## Overview

GO obsoleted **GO:0030369 ICAM-3 receptor activity** (MF) and recorded
**GO:0004888 transmembrane signaling receptor activity** as its replacement;
geneontology/go-annotation#6442 tracks review and migration of the affected
UniProt rows. The ligand should be specified via an annotation extension
`has_input ICAM3` (UniProtKB:P32942) in P2GO / GO-CAM rather than baked into a
dedicated ligand-specific receptor term.

The rationale, captured in the upstream go-ontology discussion
([geneontology/go-ontology#30560](https://github.com/geneontology/go-ontology/issues/30560)),
is that GO:0030369 is overly specific: ICAM3 is a ligand for at least three
distinct receptors (LFA-1 = ITGAL:ITGB2; the ITGAD:ITGB2 αD/β2 heterodimer;
and the C-type lectin CLEC4M / DC-SIGNR), so a single "ICAM-3 receptor
activity" MF term forces those biochemically and structurally distinct
receptors into one bucket. The solution generalises to GO:0004888 and uses
the `has_input` annotation extension to record which
adhesion molecule each receptor actually binds. The same approach is
proposed for other singleton receptor-for-X terms under GO:0004888 that
have no further child terms.

This project tracks the impact on AI Gene Review and queues affected genes
for review, since none of the directly annotated genes are currently in this
repository.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6442](https://github.com/geneontology/go-annotation/issues/6442) (opened 2026-05-29)
- Ontology ticket: [geneontology/go-ontology#30560](https://github.com/geneontology/go-ontology/issues/30560) (closed 2026-06-12; term now obsolete)

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| ICAM-3 receptor activity | GO:0030369 | GO:0004888 transmembrane signaling receptor activity (+ `has_input` ICAM3 / UniProtKB:P32942 extension) |

Term status rechecked in QuickGO / AmiGO on 2026-10-04: GO:0030369 is now
**obsolete**. The obsoletion comment says the term was retired because it is
more specific than any known gene product specificity, and AmiGO records
`GO:0004888` as the replacement.

## Affected experimental / curated annotations

Pulled from QuickGO on 2026-05-30 (filter `assignedBy=UniProt`,
goId=GO:0030369). The upstream issue lists "UniProt 3" affected
annotations, all human:

| # | Group | Gene | Species | UniProt | Reference | Evidence | Status |
|---|---|---|---|---|---|---|---|
| 1 | UniProt | ITGAL | H. sapiens | P20701 | PMID:19029120 | IMP | move to GO:0004888 + `has_input` UniProtKB:P32942 |
| 2 | UniProt | ITGB2 | H. sapiens | P05107 | PMID:19029120 | IMP | move to GO:0004888 + `has_input` UniProtKB:P32942 |
| 3 | UniProt | CLEC4M | H. sapiens | Q9H2X3 | PMID:11257134 | NAS | move to GO:0004888 + `has_input` UniProtKB:P32942 |

ITGAL and ITGB2 are the LFA-1 αL/β2 heterodimer subunits; the upstream tracker
lists the same IMP support, PMID:19029120, for both rows. The CLEC4M /
DC-SIGNR row is NAS (non-traceable author statement) from the upstream-listed
PMID:11257134 and pre-dates current evidence-code standards.

In the 2026-05-30 QuickGO pull, the remaining ~155 annotations to GO:0030369
were Ensembl Compara IEA projections from those three human entries
(GO_REF:0000107, ECO:0000265), so they were expected to follow when the human
entries moved.

## Mappings flagged for redirection

Upstream states **None** for InterPro2GO, UniProt-Keywords, and UniRule
mappings to GO:0030369. No mapping redirects are required for this
obsoletion.

## Impact on this repo

No genes directly annotated to GO:0030369 are currently reviewed here.
Searches under `genes/` for the directly affected accessions and target
directories (`ITGAL`, `ITGB2`, `CLEC4M`, `CD209`, `ICAM3`, `ITGAD`) still
found no fetched review, UniProt, or GOA files on 2026-10-04. This means
**no existing reviews need refresh** for the obsoletion itself; the project
is a queueing exercise that lines up leukocyte adhesion receptors for
prospective review.

The repo currently has no other ICAM-family or β2-integrin reviews, so
this would be the entry point for that area of immunology.

## Scope

- **Organisms**: Human only for direct/manual annotations (3 entries).
  The 2026-05-30 Ensembl IEA projection set covered orthologs across mammals
  and other vertebrates and was expected to follow the human-row migration.
- **GO branches**: MF only. The replacement GO:0004888 sits in the same
  signaling-receptor sub-branch under GO:0038023 signaling receptor
  activity, so parent classifications upstream of GO:0030369 are
  preserved.
- **Type of fix**: terminological upstream — the obsoletion records the
  ligand via `has_input` rather than via a ligand-specific MF term. Whether
  GO:0004888 *transmembrane signaling receptor activity* fits each
  annotated protein is left to the gene reviews. It is debatable for the
  LFA-1 heterodimer (ITGAL:ITGB2), whose ICAM engagement is chiefly
  adhesive; the ITGAL/ITGB2 reviews should weigh it against an adhesion MF
  (e.g. GO:0050839 cell adhesion molecule binding) rather than accept it
  by default. For DC-SIGNR, the review should weigh C-type lectin /
  mannose-binding activity, including GO:0005537 D-mannose binding, against
  retaining GO:0004888 transmembrane signaling receptor activity with
  `has_input` ICAM3 rather than assuming a straight transfer.
- **Special case (CLEC4M NAS annotation)**: the CLEC4M GO:0030369 entry
  is NAS-evidence from upstream-listed PMID:11257134; after
  `just fetch-gene human CLEC4M` caches the source paper, the review should
  evaluate whether the citation supports an ICAM-3-specific receptor
  function or a glycan-dependent binding role.

## Candidate genes for initial review

Verify each with `just fetch-gene human <gene>` before starting. None are
currently in the repo.

### Tier 1 — directly annotated, experimental evidence

1. **ITGAL** (human, UniProt **P20701**) — αL integrin subunit, partners
   with ITGB2 to form LFA-1. The upstream tracker lists PMID:19029120 as
   IMP support for both subunits. LFA-1 is the canonical leukocyte adhesion /
   immune synapse integrin, so this review would seed broad
   leukocyte-adhesion coverage.
2. **ITGB2** (human, UniProt **P05107**) — β2 integrin subunit (CD18),
   common to LFA-1, Mac-1 (with ITGAM), p150,95 (with ITGAX), and αD/β2
   (with ITGAD). Loss-of-function causes leukocyte adhesion deficiency
   type I (LAD-I). The upstream-listed PMID:19029120 support pairs
   naturally with the ITGAL review.

### Tier 2 — directly annotated, NAS evidence

3. **CLEC4M / DC-SIGNR / L-SIGN** (human, UniProt **Q9H2X3**) — C-type
   lectin expressed on sinusoidal endothelial cells (liver, lymph node)
   and certain DCs. The GO:0030369 annotation is NAS from upstream-listed
   PMID:11257134 and would benefit from re-evaluation against the current
   picture of DC-SIGNR as a glycan-binding lectin whose ICAM-3 binding is
   glycan-dependent. The review should weigh D-mannose binding (GO:0005537)
   and high-mannose glycan recognition against retaining GO:0004888 with an
   ICAM3 `has_input` extension.

### Tier 3 — related but not on the upstream list

4. **CD209 / DC-SIGN** (human, UniProt **Q9NNX6**) — DC-SIGNR's closer
   paralog, expressed on dendritic cells. Listed by the upstream
   curator as one of the canonical ICAM-3 receptors but does not appear
   in the QuickGO list of direct GO:0030369 annotations as of 2026-05-30.
   A CD209 review would naturally complement CLEC4M and provide a
   cleaner template for handling glycan-dependent ICAM3 binding.
5. **ITGAD** (human, UniProt **Q13349**) — αD integrin subunit, the
   third β2-partnered α subunit alongside ITGAL and ITGAM. Also
   mentioned upstream as forming an ICAM3-binding heterodimer with
   ITGB2. Lower priority because no direct GO:0030369 annotation, but
   inclusion would round out the β2-integrin family.

### Related ligand

6. **ICAM3** (human, UniProt **P32942**) — the ligand itself, not on
   the upstream list. Its annotation profile (cell adhesion molecule
   binding, leukocyte adhesion, signaling-ligand role) is the
   complementary view of the same biology and would be a natural addition
   if leukocyte adhesion receptor coverage is built out here.

## Review approach

1. **No urgent local refresh needed.** The ontology ticket #30560 has
   landed and GO:0030369 is obsolete, but the local repository still has no
   affected ITGAL, ITGB2 or CLEC4M reviews. Reviews can proceed on the
   underlying biology using the live GO:0004888 term and recording the
   `has_input` ICAM3 extension where a receptor really binds ICAM3.
2. **Begin with paired ITGAL + ITGB2 review.** LFA-1 is the canonical
   leukocyte adhesion integrin with substantial biochemistry / structural
   biology and a well-defined disease association (LAD-I for ITGB2). The
   upstream-listed PMID:19029120 evidence makes the two reviews efficient to
   do together.
3. **Follow with CLEC4M.** This is the more diagnostic review because the
   GO:0030369 annotation is NAS and the underlying biology (high-mannose
   glycan recognition, ICAM3 binding as a glycan-mediated interaction)
   may warrant `MARK_AS_OVER_ANNOTATED` or `MODIFY` to GO:0005537 +
   GO:0004888 (with `has_input` extension) rather than a straight
   transfer.
4. **Add CD209 if leukocyte adhesion / pathogen recognition coverage is
   built out** — it provides the cleaner template (well-characterised
   C-type lectin with multiple pathogen ligands) and complements CLEC4M.
5. **Defer ITGAD and ICAM3 itself** unless interest develops; the Tier 1
   pair covers the bulk of the LFA-1 biology and the upstream obsoletion.
6. **Cross-reference with leukocyte adhesion / immune synapse work** if
   such projects are added later. No related obsoletion projects in this
   repo overlap directly with the leukocyte adhesion receptor area.

## Priority

**Low-medium.** The biology is canonical and well-established, the
upstream obsoletion has landed, and no existing reviews in this repo are
blocked by the term change because no ITGAL / ITGB2 / CLEC4M / CD209 /
ITGAD / ICAM3 review has been fetched here yet. This is opportunistic —
LFA-1 (ITGAL + ITGB2) is a major unreviewed leukocyte adhesion
receptor, so the obsoletion is a reasonable trigger to start that
coverage if interest develops. The CLEC4M NAS-evidence review is the
most diagnostically interesting piece because the underlying biology
may not match the literal "ICAM-3 receptor" framing.

## Status

- 2026-10-04 — Rechecked upstream and local status. QuickGO reports
  GO:0030369 as obsolete, AmiGO lists `GO:0004888` as the replacement,
  geneontology/go-ontology#30560 is closed, and go-annotation#6442 remains
  open. None of ITGAL, ITGB2, CLEC4M, CD209, ICAM3 or ITGAD has been
  fetched under `genes/`, so the local work remains prospective.
- 2026-05-30 — Project file created. Tracking upstream issue #6442
  (opened 2026-05-29). Upstream ontology ticket #30560 is OPEN at the
  proposal stage with no obsoletion PR yet. Verified GO:0030369 still
  live in OLS on 2026-05-30 (isObsolete: false). Verified the 3
  UniProt-assigned direct annotations via QuickGO REST on 2026-05-30
  (ITGAL P20701 IMP, ITGB2 P05107 IMP, CLEC4M Q9H2X3 NAS). No
  InterPro2GO / UniProt-Keywords / UniRule mappings flagged upstream.
  No gene reviews started yet in this repo; none of the affected genes
  (ITGAL, ITGB2, CLEC4M, CD209, ICAM3, ITGAD) are present under
  `genes/`.
