# ICAM-3 Receptor Activity — Obsoletion & Replacement

## Overview

A GO obsoletion proposal will retire **GO:0030369 ICAM-3 receptor activity**
(MF) and move its annotations to the parent term
**GO:0004888 transmembrane signaling receptor activity**, with the ligand
specified via an annotation extension `has_input ICAM3` (UniProtKB:P32942) in
P2GO / GO-CAM rather than baked into a dedicated ligand-specific receptor
term.

The rationale, captured in the upstream go-ontology discussion
([geneontology/go-ontology#30560](https://github.com/geneontology/go-ontology/issues/30560)),
is that GO:0030369 is overly specific: ICAM3 is a ligand for at least three
distinct receptors (LFA-1 = ITGAL:ITGB2; the ITGAD:ITGB2 αD/β2 heterodimer;
and the C-type lectin CLEC4M / DC-SIGNR), so a single "ICAM-3 receptor
activity" MF term forces those biochemically and structurally distinct
receptors into one bucket. The proposed solution generalises to
GO:0004888 and uses the `has_input` annotation extension to record which
adhesion molecule each receptor actually binds. The same approach is
proposed for other singleton receptor-for-X terms under GO:0004888 that
have no further child terms.

This project tracks the impact on AI Gene Review and queues affected genes
for review, since none of the directly annotated genes are currently in this
repository.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6442](https://github.com/geneontology/go-annotation/issues/6442) (opened 2026-05-29)
- Ontology ticket: [geneontology/go-ontology#30560](https://github.com/geneontology/go-ontology/issues/30560) (OPEN — proposal stage as of 2026-05-30)

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| ICAM-3 receptor activity | GO:0030369 | GO:0004888 transmembrane signaling receptor activity (+ `has_input` ICAM3 / UniProtKB:P32942 extension) |

Term status verified in OLS on 2026-05-30: GO:0030369 is still live
(`isObsolete: false`); the obsoletion is at the proposal stage in the
upstream ontology ticket. GO:0004888 transmembrane signaling receptor
activity is the live parent and is the proposed replacement.

## Affected experimental / curated annotations

Pulled from QuickGO on 2026-05-30 (filter `assignedBy=UniProt`,
goId=GO:0030369). The upstream issue lists "UniProt 3" affected
annotations, all human:

| # | Group | Gene | Species | UniProt | Reference | Evidence | Status |
|---|---|---|---|---|---|---|---|
| 1 | UniProt | ITGAL | H. sapiens | P20701 | PMID:19029120 | IMP | move to GO:0004888 + `has_input` UniProtKB:P32942 |
| 2 | UniProt | ITGB2 | H. sapiens | P05107 | PMID:19029120 | IMP | move to GO:0004888 + `has_input` UniProtKB:P32942 |
| 3 | UniProt | CLEC4M | H. sapiens | Q9H2X3 | PMID:11257134 | NAS | move to GO:0004888 + `has_input` UniProtKB:P32942 |

ITGAL and ITGB2 are the LFA-1 αL/β2 heterodimer subunits; their joint IMP
annotation comes from a single publication (PMID:19029120). CLEC4M /
DC-SIGNR is the dendritic-cell C-type lectin; its annotation is NAS
(non-traceable author statement) and pre-dates current evidence-code
standards.

The remaining ~155 annotations to GO:0030369 in QuickGO are IEA from
Ensembl Compara orthology projection of these three human entries
(GO_REF:0000107, ECO:0000265), so they will follow the human entries
automatically once those are moved.

## Mappings flagged for redirection

Upstream states **None** for InterPro2GO, UniProt-Keywords, and UniRule
mappings to GO:0030369. No mapping redirects are required for this
obsoletion.

## Impact on this repo

No genes directly annotated to GO:0030369 are currently reviewed here.
Searches under `genes/` for `ITGAL`, `ITGB2`, `CLEC4M`, `CD209`, `ICAM3`
(and accessions P20701, P05107, Q9H2X3, P32942) returned no matches on
2026-05-30. This means **no existing reviews need refresh** for the
obsoletion itself; the project is a queueing exercise that lines up
leukocyte adhesion receptors for prospective review.

The repo currently has no other ICAM-family or β2-integrin reviews, so
this would be the entry point for that area of immunology.

## Scope

- **Organisms**: Human only for direct/manual annotations (3 entries).
  The ~155 Ensembl IEA projections cover orthologs across mammals and
  other vertebrates but follow automatically.
- **GO branches**: MF only. The replacement GO:0004888 sits in the same
  signaling-receptor sub-branch under GO:0038023 signaling receptor
  activity, so parent classifications upstream of GO:0030369 are
  preserved.
- **Type of fix**: terminological — annotated proteins genuinely are
  transmembrane signaling receptors that bind ICAM-3; the obsoletion just
  records the ligand via `has_input` rather than via a ligand-specific MF
  term. The biology of LFA-1 and DC-SIGNR is well established, so reviews
  can typically ACCEPT GO:0004888 (with the ICAM3 `has_input` extension)
  as a contributing MF term, while the core MF for LFA-1 is integrin /
  ICAM-binding adhesion (e.g. GO:0050839 cell adhesion molecule binding,
  GO:0007157 heterophilic cell-cell adhesion via plasma membrane cell
  adhesion molecules) and for DC-SIGNR is C-type lectin / mannose-binding
  (GO:0005537 D-mannose binding, GO:0038023 signaling receptor activity
  with `has_input` ICAM3 and other ligands).
- **Special case (CLEC4M NAS annotation)**: the CLEC4M GO:0030369 entry
  is NAS-evidence from PMID:11257134; a review here should evaluate
  whether PMID:11257134 (Bashirova et al. 2001) actually supports an
  ICAM-3-specific receptor function, given that DC-SIGNR is best
  characterised as a high-mannose-glycan-binding lectin whose
  ICAM3-binding role is glycan-dependent rather than peptide-specific.

## Candidate genes for initial review

Verify each with `just fetch-gene human <gene>` before starting. None are
currently in the repo.

### Tier 1 — directly annotated, experimental evidence

1. **ITGAL** (human, UniProt **P20701**) — αL integrin subunit, partners
   with ITGB2 to form LFA-1. The PMID:19029120 IMP annotation (Cox et al.
   2008 in PMC; ICAM-3-binding study) is the experimental basis for both
   subunits. LFA-1 is the textbook leukocyte adhesion / immune synapse
   integrin, so this review would seed broad leukocyte-adhesion coverage.
2. **ITGB2** (human, UniProt **P05107**) — β2 integrin subunit (CD18),
   common to LFA-1, Mac-1 (with ITGAM), p150,95 (with ITGAX), and αD/β2
   (with ITGAD). Loss-of-function causes leukocyte adhesion deficiency
   type I (LAD-I). The shared PMID:19029120 annotation pairs naturally
   with the ITGAL review.

### Tier 2 — directly annotated, NAS evidence

3. **CLEC4M / DC-SIGNR / L-SIGN** (human, UniProt **Q9H2X3**) — C-type
   lectin expressed on sinusoidal endothelial cells (liver, lymph node)
   and certain DCs. The GO:0030369 annotation is NAS from PMID:11257134
   and would benefit from re-evaluation against current understanding of
   DC-SIGNR as primarily a high-mannose-glycan / pathogen-recognition
   lectin (HIV, HCV, SARS-CoV-2 spike, Ebola GP) whose ICAM-3 binding is
   glycan-dependent. Core MF terms should likely centre on D-mannose
   binding (GO:0005537) and high-mannose glycan recognition, with
   ICAM3-binding captured via `has_input` on the signaling receptor
   activity.

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

## Proposed approach

1. **No urgent action needed.** The upstream ontology ticket #30560 is
   still in proposal stage (OPEN, no obsoletion PR yet) as of 2026-05-30,
   and the annotation tracker #6442 was opened the day before this
   project file. Reviews can proceed on the underlying biology now using
   the live GO:0004888 term and recording the proposed `has_input` ICAM3
   extension; the actual obsoletion of GO:0030369 will follow once
   discussion concludes upstream.
2. **Begin with paired ITGAL + ITGB2 review.** LFA-1 is the canonical
   leukocyte adhesion integrin with substantial biochemistry / structural
   biology and a well-defined disease association (LAD-I for ITGB2). The
   shared PMID:19029120 evidence makes the two reviews efficient to do
   together.
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
upstream obsoletion has not yet been implemented (proposal stage), and
no existing reviews in this repo are blocked by the obsoletion (no
ITGAL / ITGB2 / CLEC4M / CD209 reviews exist yet). This is opportunistic
— LFA-1 (ITGAL + ITGB2) is a major unreviewed leukocyte adhesion
receptor, so the obsoletion is a reasonable trigger to start that
coverage if interest develops. The CLEC4M NAS-evidence review is the
most diagnostically interesting piece because the underlying biology
may not match the literal "ICAM-3 receptor" framing.

## Status

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
