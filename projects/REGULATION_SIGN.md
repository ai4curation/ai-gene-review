---
title: "Regulation Sign Errors: Activator vs Inhibitor"
maturity: SCOPING
tags: [EVALUATION]
species: [human, DROME, ARATH, worm]
genes: [GNAI1, GNAI2, NTSR1, NLRP3, LRP5, CD47, CLYBL, CIB2, MCL1, ced-9, FLC, SVP]
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
that merely discuss direction.

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
   similarity source (REMOVE rather than MODIFY).
5. **Family-level sign defaults.** Gα proteins split into activating (Gs) and inhibiting
   (Gi/o) branches of the same pathway; a propagation that ignores the split imports
   the wrong half.

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
REMOVE (GNAI1); those are listed by hand above.
