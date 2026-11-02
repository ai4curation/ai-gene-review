# Alpl (rat) review notes

## Session 1 (initial review)

- `just fetch-gene rat Alpl` resolved P08289 (PPBT_RAT, RGD:2100, GeneID 25586); 99 GOA rows.
- No deep-research provider available; manual synthesis in `Alpl-deep-research-manual.md`.
- Most rat rows are ISO/ISS/IEA transfers from mouse Alpl (MGI:87983) and human ALPL
  (P05186); the rat-specific experimental rows are IDA for ALP activity [PMID:3472490],
  TAS [PMID:3422431], extracellular region [PMID:19697513], extracellular
  membrane-bounded organelle [PMID:32710882], and IEP/IDA expression-response rows.
- PMID:20048161 (read in full) used human recombinant TNAP, not rat
  ["The 2.5-kb human TNAP cDNA was cloned into pCMV-Script vector"]. Treated as ortholog
  evidence for PPi, PLP, ATP/ADP/AMP hydrolysis.
- Decisions mirror the mouse (`genes/mouse/Alpl`) and human (`genes/human/ALPL`) reviews:
  - Core MFs: inorganic diphosphate phosphatase (mineralization), pyridoxal phosphatase
    (B6), phosphoamidase / phosphocreatine (futile creatine cycle).
  - `GO:0016462` pyrophosphatase activity MODIFY -> `GO:0004427` (plus ATP/ADP hydrolysis).
  - `GO:0016791` phosphatase activity (InterPro2GO) MODIFY -> specific phosphatase terms.
  - `GO:0140928` inhibition of non-skeletal tissue mineralization REMOVE: inverted sign;
    TNAP promotes ectopic calcification ["Overexpression of TNAP increased calcification
    of cultured aortas." PMID:21490328]. Recorded as a source defect against the mouse
    MGI row from which the ISO/IEA descend.
  - `GO:0046677` response to antibiotic: UNDECIDED, as in the mouse review.
  - Response-to-stimulus rows: KEEP_AS_NON_CORE, except M-CSF, whose own abstract
    calls the effect secondary ["osteoblast abnormalities in tl rats are an effect of the
    osteopetrotic condition rather than the cause of the disease." PMID:7669437]:
    MARK_AS_OVER_ANNOTATED.
- No NEW terms proposed.
