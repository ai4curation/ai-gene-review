# CTLA4 curation notes

## 2026-09-04 (PAINT no-IBA project finishing pass)

Reviewed the full `CTLA4-ai-review.yaml` draft (all actions pre-assigned). CTLA4 is
the inhibitory checkpoint counterpart to CD28, competing for CD80/CD86 with higher
avidity. Core MF `receptor decoy activity` (GO:0140319) and the NEW `signaling
receptor inhibitor activity` (GO:0030547) are well grounded in the two crystal
structures [PMID:11279501; PMID:11279502 "Signalling through CD28 augments the T-cell
response, whereas CTLA-4 signalling attenuates it"].

Changes made this pass:
1. `DNA damage response` (GO:0006974, IMP, PMID:17875758): changed action
   REMOVE -> UNDECIDED. This is an experimental annotation and the cached publication
   is abstract-only (full text unavailable). The paper's title foregrounds ATM (a
   DNA-damage gene), so removing on the basis that "DNA damage belongs to ATM" is
   exactly the move the project guidance forbids for experimental annotations whose
   full text we cannot read. Reason text updated to flag it as a likely theme-transfer
   over-annotation while deferring to the curator's unseen full-text evidence.
2. Added structured `propagation_review` to the `B cell receptor signaling pathway`
   IBA (GO:0050853, node PTN000160996, MARK_AS_OVER_ANNOTATED). root_cause
   SOURCE_WEAK_OR_INFERRED; the IBD node is seeded by CTLA4's own weak IMP for the
   same term (the same correlative B-CLL expression study, PMID:17875758), and CTLA4
   acts in the TCR/CD28 axis, so BCR signaling does not transfer confidently
   [PMID:17875758 "the overexpression of CTLA4 and MNDA was associated with good
   outcome"].
3. Added a deep-research supporting citation to the LRBA trafficking annotation
   (PMID:26206937) to satisfy the "no annotations reference deep research" warning
   [file:human/CTLA4/CTLA4-deep-research-falcon.md "recycling to the surface (e.g.,
   after TCR stimulation) is regulated by LRBA and Rab11 pathways"].

Confirmed sound: the whole PMID:17875758 cluster (BCR signaling, neg reg B-cell
proliferation, pos reg apoptosis) as MARK_AS_OVER_ANNOTATED — all from one CLL
differential-expression paper, correlative rather than mechanistic. Trafficking/
localization annotations (Golgi, clathrin-coated vesicle, perinuclear region, external
side of PM) accepted, consistent with CTLA4's constitutive endocytosis biology.

Both warnings cleared; validates clean with no PENDING. Status IN_PROGRESS -> COMPLETE.

Action tally: 31 ACCEPT, 19 MARK_AS_OVER_ANNOTATED, 1 NEW, 1 UNDECIDED.
