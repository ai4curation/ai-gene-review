# TNFRSF10B / DR5 notes

## Core role

- TNFRSF10B is DR5/TRAIL-R2, the second signaling receptor for TNFSF10/TRAIL.
  It is a type I plasma-membrane TNF receptor with extracellular cysteine-rich
  TRAIL-binding repeats and a cytoplasmic death domain.
- The structural DR5 paper provides the clearest ligand-level evidence:
  Apo2L/TRAIL and the DR5 ectodomain form a 3:3 complex, and receptor
  ligation triggers apoptosis by oligomerizing intracellular death domains
  [PMID:10549288].
- DR5 signaling is FADD dependent. The FADD-deficient MEF study showed that
  cells stably expressing human DR5 are resistant to TRAIL without FADD and
  regain sensitivity after FADD reconstitution [PMID:10862756]. Rows to
  generic apoptosis, regulation of apoptosis, death-domain-receptor apoptosis,
  and cell-surface signaling should therefore be tightened to
  `GO:0036462 TRAIL-activated apoptotic signaling pathway`.
- `GO:0036463 TRAIL receptor activity` is the best molecular-function term for
  DR5 because it captures both ligand recognition and receptor signaling.
  Generic `death receptor activity`, `signaling receptor activity`,
  `TRAIL binding`, and TNFSF10 `protein binding` rows should be folded into it.

## Contextual and indirect rows

- DR5 is frequently an induced effector in stress-sensitization papers.
  CHOP/ER stress can enhance DR5 expression, and DR5 knockdown blocks
  thapsigargin-induced apoptosis in some carcinoma cells [PMID:15322075].
  That supports an ER-stress-to-DR5 route, but the receptor itself is not an
  intrinsic ER-stress apoptotic effector, so the ER-stress rows are
  over-annotations.
- The PU.1 AML paper is similar: PU.1 supports TRAIL-mediated apoptosis partly
  by inducing DR5 expression [PMID:28362429]. The paper supports the
  TRAIL/DR5 axis but not the immune-process term
  `GO:0002357 defense response to tumor cell` on the tumor-cell receptor.
- The NF-kappaB rows are secondary. The 1997 DR5/DR4 paper supports
  contextual NF-kappaB activation [PMID:9430227], but the pancreatic
  adenocarcinoma paper is mixed CD95/TRAIL-receptor evidence [PMID:11464292],
  and the large-scale cDNA screen cache does not expose its TNFRSF10B-specific
  result [PMID:12761501]. Those latter two rows should remain unresolved from
  local evidence.
- The recurring mechanical-stimulus row has the same problem as in DR4. It
  derives from expression-pattern evidence in a BAD/prostate-cancer study
  [PMID:19593445]; altered DR5 expression during a stretch experiment does not
  make DR5 part of the mechanical-stimulus response.

## Interaction imports

- Direct TNFSF10 `GO:0005515 protein binding` rows from the Apo2L/TRAIL:DR5
  crystal structure and the Shilts et al. surface-protein screen should be
  narrowed to `GO:0036463 TRAIL receptor activity`.
- TNFSF10 imports from TRAIL sensitization studies with resveratrol,
  bortezomib, HDAC inhibition, or V-ATPase inhibition should be left
  `UNDECIDED` where the local cache is abstract-only and does not expose the
  exact TNFRSF10B-TNFSF10 interaction assayed.
- The DDX3X, GSK3B, BIRC2, and FADD/CASP8 rows from the anti-apoptotic
  death-receptor complex paper should also be left `UNDECIDED`. The cache only
  has title-level evidence for an anti-apoptotic complex at death receptors, so
  it cannot verify the individual DR5 IntAct edges.
- HuRI imports for MUC1, ASPH, and ZDHHC15 are useful interaction-screen leads
  but have no DR5-specific apoptotic mechanism in the cached article
  [PMID:32296183], so they should not remain as `GO:0005515` annotations.
- The Shilts et al. surface-protein screen recovered the extracellular
  TNFSF10-TNFRSF10B interaction and is aligned with TRAIL receptor activity
  [PMID:35922511].

## Reactome and GO-CAM exports

- The TRAIL/TRAILR2 GO-CAM places TNFRSF10B in
  `GO:0036462 TRAIL-activated apoptotic signaling pathway` at the plasma
  membrane. The HPV E6/MARCHF8 GO-CAM uses the newer
  `GO:0036463 TRAIL receptor activity` term for TNFRSF10B at the plasma
  membrane while modelling viral down-regulation of TRAIL-R1/R2.
- Unlike TNFRSF10A, the Reactome procaspase-8 dimerization event
  `R-HSA-141156` is directly DR5-specific: its summary places the event at a
  "TRAIL:TRAIL receptor-2:FADD" complex. It should therefore be accepted for
  TNFRSF10B.
- Reactome rows for TNFSF10 binding, receptor trimerization, FADD recruitment,
  procaspase-8/procaspase-10 recruitment, and DcR2 heteromerization are close
  enough to DR5 to keep as plasma-membrane assertions.
- Reactome exports from TP53 transcription of the TNFRSF10B gene and from
  downstream c-FLIP/CASP8 checkpoint events are too indirect for a
  TNFRSF10B component row, even though they are correctly inside broad TRAIL
  or death-receptor apoptosis models.
