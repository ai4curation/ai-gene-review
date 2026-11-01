---
title: "Regulation Sign Errors: Activator vs Inhibitor"
maturity: SCOPING
tags: [EVALUATION]
species: [human, mouse, rat, yeast, DROME, ARATH, worm]
genes: [GNAI1, GNAI2, NTSR1, NLRP3, LRP5, CD47, CLYBL, CIB2, MCL1, ced-9, FLC, SVP, ADIPOQ, CFLAR, BAX, Cd48, Pck1]
---

# Regulation Sign Errors: Activator vs Inhibitor

**Bottom line:** a GO annotation can name the right process and the right gene and
still say the opposite of what happens: *positive* regulation where the gene
represses, an *adenylate cyclase-activating* pathway for a G protein that inhibits
the cyclase. Most over-annotation is a matter of degree (too broad, too indirect);
a sign error is a flat contradiction, and it propagates — through orthology
transfer, IBA and pathway models — with its sign intact. This project collects the
sign corrections already made during gene review, asks where they come from, and
looks for the ones not yet found.

A seed census of existing reviews finds **35 MODIFY rows on 25 genes** whose
replacement is the same term with the opposite sign
([census](REGULATION_SIGN/sign_flip_census.yaml), produced by
[sign_flip_census.py](REGULATION_SIGN/sign_flip_census.py)). Sign problems resolved by
REMOVE, UNDECIDED or a sign-neutral parent are not in that count; a keyword pass over
review reasons ([sign_reason_census.yaml](REGULATION_SIGN/sign_reason_census.yaml)) gives
152 candidate rows that still need screening by hand, since it also catches reasons
that merely discuss direction. A third, structured source is the
`REGULATORY_SIGN_INVERSION` failure mode reviewers already record in
`propagation_review`: **90 rows across 63 review files**, harvested below.

## Principle: sign is judged in vivo

GO annotates what a gene product does in the organism, not what it can be made to do
in an assay. A sign established only in vitro (a purified protein at non-physiological
concentration, an overexpression readout) does not outweigh the in vivo direction, and
is not a reason to hold a contradicted sign as UNDECIDED. When the in vivo role has the
opposite sign, the annotation is corrected (MODIFY to the opposite-sign term) or, if
the row also has no sound source, removed.

## Why this deserves its own project

The existing over-annotation work treats regulation terms mostly as a question of
*directness* — is the gene upstream, pleiotropic, or doing the work? Sign is a
separate axis with a separate failure mode:

- **It is a contradiction, not an imprecision.** A too-general term is still true; an
  inverted one is false, and a reader using GO for enrichment or causal modelling
  will draw the wrong conclusion.
- **It survives every refinement step.** IBA, ISS and Ensembl Compara (GO_REF:0000107)
  transfers copy the sign along with the term; GO-CAM `causally upstream of,
  positive effect` edges inherit it too.
- **It has characteristic origins**, which are testable (below).

## Working hypotheses for where sign errors come from

1. **Perturbation read the wrong way round (IMP).** Knockout raises X → the gene
   *negatively* regulates X. Recording the phenotype direction rather than the gene's
   effect inverts the sign. IMP is the largest evidence class in the census (15/35),
   e.g. NLRP3 `negative regulation of inflammatory response` (×3) and LRP5 osteoblast /
   fat cell differentiation, both corrected to the opposite sign.
2. **Context-dependent direction collapsed to one sign.** A gene that promotes X in one
   cell type and inhibits it in another gets whichever sign the first paper showed.
   NTSR1 locomotion (hypolocomotion in knockouts, hyperactivity with stimulants) was
   generalized to the sign-neutral `GO:0040012 regulation of locomotion`.
3. **Orthology transfer of a sign from a different assay or paralog.** In this PR's Gi
   reviews both GNAI2 `GO:0007189 adenylate cyclase-activating GPCR signaling` and two
   NTSR1 rows (`positive regulation of apoptotic process`, `negative regulation of
   release of sequestered calcium`) arrived by GO_REF:0000107. The GNAI2 source paper
   itself reports Gαi2 mediating cyclase *inhibition*.
4. **Wrong donor entirely.** GNAI1's `GO:0007189` ISS was transferred from an adenylyl
   cyclase (ADCY6), not a Gα ortholog — a sign error manufactured by a mis-matched
   similarity source. The merged #5582 review had held it UNDECIDED because
   high-concentration Gαi can stimulate type I/II cyclases in vitro (PMID:8119955);
   under the in vivo principle above it is now REMOVE, tagged
   `PROPAGATION_BAD` with failure modes `WRONG_ORTHOLOG_OR_PARALOG` and
   `REGULATORY_SIGN_INVERSION`. The episode is a pattern worth looking for elsewhere:
   an in vitro activity of the opposite sign can keep a physiologically wrong sign alive.
5. **Family-level sign defaults.** Gα proteins split into activating (Gs) and inhibiting
   (Gi/o) branches of the same pathway; a propagation that ignores the split imports
   the wrong half.
6. **Participant for an inhibitor.** An unsigned process term placed on a PAINT node
   whose family holds both effectors and inhibitors of the process lands on the
   inhibitors as if they took part (BCL2 family, CFLAR). The harvest below finds 28 such
   rows, 15 of them IBA.

## Harvest of `REGULATORY_SIGN_INVERSION` rows

[sign_inversion_harvest.py](REGULATION_SIGN/sign_inversion_harvest.py) collects every
`existing_annotations` row whose `propagation_review.failure_modes` includes
`REGULATORY_SIGN_INVERSION`, with its action, replacement, root cause and sources
([sign_inversion_harvest.yaml](REGULATION_SIGN/sign_inversion_harvest.yaml)). Because
the failure mode lives on `propagation_review`, every row is a propagated annotation:
ISO 40, IBA 23, IEA 16, ISS 10, plus one IGI.

The tagged rows have two structural shapes, distinguished by whether the original
term itself carries a direction:

| Shape | Rows | Dominant evidence | What went wrong |
|---|---|---|---|
| **Signed term, wrong sign** | 62 | ISO 29, IEA 15, ISS 9, IBA 8 | A `positive`/`negative`, activating/inhibiting or similar term transferred with the opposite direction to the target's own biology |
| **Participant for an inhibitor** | 28 | IBA 15, ISO 11 | An unsigned process or activity (`apoptotic process`, `mitochondrial fusion`, `transcytosis`, `heterochromatin formation`) given to a gene that *opposes* it |

The two shapes point to different mechanisms:

- **Signed rows lean on orthology transfers to rodents.** ISO is the largest evidence
  class among signed rows (29 of 62), and 40 of all 90 rows are rat or mouse ISO rows, transferred from a human (or other rodent) annotation; the sign
  error is inherited from, or created by, that single source. These are where tracing
  the donor annotation (next step below) will pay off, and where an upstream fix to
  one human row would correct several rodent rows.
- **Participant-for-inhibitor rows are mostly PAINT nodes over mixed families.**
  15 of the 28 are IBA, from families that contain both effectors and inhibitors of
  the same process: the BCL2 family (MCL1 `release of cytochrome c`, `intrinsic
  apoptotic signaling`, `channel activity`; BAX `mitochondrial fusion`), CFLAR
  (`apoptotic process`, `extrinsic apoptotic signaling`), LONRF2, plant EPF2 and
  SERK4, fly NijA, worm sta-1 and yeast RPD3. This is the case the enum describes
  ("family contains activators and inhibitors"), and it adds a sixth origin to the
  hypotheses above.

How reviewers resolved them:

| Correction | Rows |
|---|---|
| No replacement (REMOVE 19, MARK_AS_OVER_ANNOTATED 13, UNDECIDED 10, KEEP_AS_NON_CORE 2) | 44 |
| MODIFY to another kind of term (mostly participant → `negative regulation of` the process) | 24 |
| Opposite-sign sibling (15 MODIFY; one REMOVE, naked mole-rat Cgas, also names the flipped term) | 16 |
| MODIFY to the sign-neutral `regulation of` parent | 6 |

Root causes are split: `SOURCE_BAD` 34 (the donor annotation itself is wrong),
`TERM_SCOPING_PROBLEM` 25, `PROPAGATION_BAD` 16 (sound donor, wrong target),
`UNRESOLVED` 10. Every `SOURCE_BAD` and `PROPAGATION_BAD` row still in current GOA
now carries a `source_defects` entry (**50 of the 90 rows**), so `just
export-source-defects` routes them to the assigning group: GO Central (PAINT and the
rodent orthology pipeline) and Ensembl Compara take most of them. The rows without one
are term-scoping, unresolved or weak-source cases, where the source record is not
shown to be wrong. For family-tree (IBA) rows the requested change is `CHECK` rather
than a repoint, because PAINT fixes them at the node (an IRD or a narrower placement),
not on the gene's row. The most frequent co-occurring failure mode is
`ROLE_CONFLATION` (16), which tracks the participant-for-inhibitor shape.

Cases worth singling out:

- **Both signs from the same evidence.** Human ADIPOQ carries `positive` and `negative
  regulation of cold-induced thermogenesis` cited to the same two papers, a full 2×2
  cross-product that mouse Adipoq repeats; reviewers removed the unsupported pair.
- **Species divergence in direction.** Mouse and rat Cd48: CD48-2B4 activates human NK
  cells but inhibits rodent ones, so the human-seeded `natural killer cell activation`
  does not transfer.
- **GO-CAM causal chains.** Mouse Pck1 rows (`SREBP-SCAP complex retention in ER`,
  `positive regulation of cholesterol biosynthetic process`) derive from a human GO-CAM
  in which PCK1 *negatively* regulates INSIG; the derived process rows do not carry
  that negative edge. This makes the GO-CAM cross-check below concrete.
- **Neutral is sometimes the right answer.** S. pombe zds1, mouse Ptk7, yeast CDC55 and
  ROF1 went to the unsigned parent because the direction is context-dependent or
  untested in the target, not because the opposite sign is established.

## Seed cases

| Gene | Original → replacement | Evidence | Origin hypothesis (tentative) |
|---|---|---|---|
| human/GNAI2 | GO:0007189 AC-activating → GO:0007193 AC-inhibiting GPCR signaling | IEA (GO_REF:0000107) | 3, 5 |
| human/GNAI1 | GO:0007189 AC-activating → REMOVE | ISS (donor ADCY6) | 4 |
| human/NTSR1 | GO:0040017 positive regulation of locomotion → GO:0040012 | IEA (GO_REF:0000107) | 2 |
| human/NTSR1 | GO:0043065 positive regulation of apoptotic process → UNDECIDED | IEA (GO_REF:0000107) | 3 |
| human/NLRP3 | GO:0050728 negative → GO:0050729 positive regulation of inflammatory response (×3) | IMP | 1 |
| human/LRP5 | GO:0045668 negative → GO:0045669 positive regulation of osteoblast differentiation | IMP | 1 |
| human/CD47 | GO:0050766 positive → GO:0050765 negative regulation of phagocytosis | IBA, IEA | 3 |
| human/CLYBL | GO:0106121 positive → GO:0106122 negative regulation of cobalamin catabolism | IDA, IEA | — |
| human/MCL1 | GO:1903378 positive → GO:1903377 negative regulation of neuron apoptosis | IGI, IEA | — |
| worm/ced-9 | GO:0043065 positive → GO:0043066 negative regulation of apoptotic process | EXP | — |
| ARATH/FLC, ARATH/SVP | GO:0045944 positive → GO:0000122 negative regulation of transcription by RNA pol II | IEA | 3 |

The full list is in the census file. The CD47 case is notable: an IBA, so the sign
sits on a PAINT node and every descendant inherits it.

## Questions

- Does a sign error on a source row predict the same error on rows propagated from it?
  Trace each census row with IEA/IBA/ISS evidence back to its donor annotation.
- Are IMP sign errors concentrated in particular curation sources or eras?
- For GO-CAM: do the cached models (`gocams/`) carry any causal edge whose sign
  contradicts a reviewed annotation of the same gene?
- Which corrections should go upstream as GO tickets (the source annotation is wrong)
  versus stay as review-level judgments (the direction is genuinely context-dependent)?

---
# STATUS

2026-10-24

- [x] Seed census of sign-flip MODIFYs across all reviews (35 rows / 25 genes)
- [x] Keyword census of review reasons mentioning sign/direction (152 candidate rows, unscreened)
- [ ] Screen the keyword census by hand; classify each true sign issue by origin hypothesis
- [x] Harvest the `REGULATORY_SIGN_INVERSION` propagation_review rows (90 rows / 63 files)
- [x] Add `source_defects` to the `SOURCE_BAD` / `PROPAGATION_BAD` harvest rows (34 added; 50 of 90 rows now carry one)
- [ ] File the GO Central and Ensembl reports from `just export-source-defects`
- [ ] Look for other sign calls held UNDECIDED (or ACCEPTed) on in vitro evidence alone
- [ ] Extend the flip census to REMOVE/UNDECIDED rows and to MF activator/inhibitor pairs
- [ ] Trace propagated rows (IEA/IBA/ISS) to their donor annotations
- [ ] Cross-check GO-CAM causal-edge signs against reviews
- [ ] Draft upstream GO tickets for clear source-level errors

# NOTES

## 2026-10-24

Project started from the Gi/opioid signaling reviews (PR #5350), where GNAI2 and
GNAI1 both carried the adenylate cyclase-*activating* pathway term despite being the
canonical inhibitory Gα. The flip census matches term labels that differ only by a
sign word (positive/negative regulation, activating/inhibiting, activator/inhibitor,
agonist/antagonist, up/down-regulation, stimulation/inhibition), so it misses
corrections to a sign-neutral parent (NTSR1 locomotion) and sign problems resolved by
REMOVE or UNDECIDED (GNAI1); those are listed by hand above.

## 2026-10-31

Principle added: sign is judged on in vivo evidence. GNAI1 `GO:0007189` changed from
UNDECIDED to REMOVE on that basis. Found that `PropagationFailureModeEnum` already has
`REGULATORY_SIGN_INVERSION` ("Family contains activators and inhibitors, and a
positive/negative regulatory term leaks across members"), used on 88 rows.

## 2026-11-01

Harvested the `REGULATORY_SIGN_INVERSION` rows: 90 rows in 63 files (GNAI1 and one other
added since the earlier grep). Two shapes: 62 rows with a signed term carrying the wrong
direction, mostly rodent ISO transfers; 28 rows where an inhibitor was annotated as a
participant, mostly IBA over mixed families. Added that second shape as origin
hypothesis 6. Only 16 rows have a `source_defects` entry. The harvest's `original_signed`
flag is a regex over the term label, and its `correction` classes compare labels, so
both are aids to reading the table rather than curated judgements.

Later the same day: added `source_defects` to the 34 `SOURCE_BAD` / `PROPAGATION_BAD`
rows that lacked one (rat Prkaa2's row is no longer in GOA, so it was skipped). Resource
is the GOA assigned_by: GO_CENTRAL 19, OTHER 11 (Ensembl Compara, TreeGrafter,
YuBioLab, named in each explanation), and one each for ARUK_UCL, RGD, SGD and UNIPROT.
Requested changes: 18 CHECK, 9 DELETE_ROW, 7 REPOINT. REPOINT is used only where the
review gives a clear opposite-sign replacement for a row whose donor annotation it
shows to be wrong (GNAI2, ABCC8, ARG2, GOT1, RGS2 ×2, mouse Btk). Explanations reuse each review's own reasoning; no review action changed.
