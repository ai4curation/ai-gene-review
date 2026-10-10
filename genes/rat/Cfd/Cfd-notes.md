# Cfd (rat, P32038) notes

## Re-review 2026-10-04

**GOA changes (refresh in commit a3cf70b6d):**
- Four new rows, all duplicates of already-reviewed terms with a different evidence code or donor:
  - GO:0005576 extracellular region IBA (is_active_in, PTN008611740)
  - GO:0005576 ISO located_in from mouse Cfd (MGI:87931)
  - GO:0005576 ISO located_in from human CFD (P00746)
  - GO:0006957 complement activation, alternative pathway ISO involved_in from human CFD (P00746)
- No rows retired. GOA lists the human-donor ISS GO:0004252 row twice; the review carries it once.
- UniProt FUNCTION text was expanded in the refresh, so the old FUNCTION quote was no longer verbatim. All 16 occurrences were replaced with the current sentence [UniProtKB:P32038 "Activated CFD cleaves factor B (CFB) when the latter is complexed with complement C3b, activating the C3 convertase of the alternative pathway."].

**PENDING resolved:** the three extracellular region rows -> KEEP_AS_NON_CORE; GO:0006957 ISO from human -> ACCEPT. Each has its own propagation_review naming the donor.

**Actions changed:**
- GO:0009617 response to bacterium (ISO, mouse Cfd): ACCEPT -> KEEP_AS_NON_CORE. QuickGO shows the mouse source is an IEP from an intestinal transcriptome during Listeria infection [PMID:23012479 "A whole genome intestinal transcriptomic analysis revealed that each Lactobacillus changes expression of a specific subset of genes during infection"]. An expression change is context, not core, and the antibacterial role is already captured by GO:0006957.

**Reasons corrected (actions unchanged):**
- GO:0035886 vascular smooth muscle cell differentiation and GO:0060041 retina development (ISO, mouse Cfd): REMOVE kept. The donor was traced to IGI PMID:28057640 (now cached) [PMID:28057640 "Genetic deficiency of complement C3 and factor D prevented both the systemic thrombophilia and renal TMA phenotypes."]. The retinal phenotype is ischemic retinopathy, a disease phenotype rather than development. A companion Cfd-/- study reports no change in retinal morphology [PMID:27564415 "Overall the retinal morphology and retinal vasculature did not appear different across the various genotypes."].
- GO:0051604 protein maturation (IBA) and GO:0031638 zymogen activation (ISS/ISO): KEEP_AS_NON_CORE kept. The old support cited Cfd's own maturation by MASP-3, which is Cfd as a substrate and fails the participation test. It now cites factor D's cleavage of factor B into Ba/Bb, which is the step factor D itself performs.
- GO:0006957 ISO (mouse Cfd): ACCEPT kept; donor IMP PMID:27564415 (now cached) cited.
- GO:0007219 Notch signaling pathway (IMP, PMID:12949072): REMOVE kept. The cached abstract states explicitly that adipsin is a differentially expressed readout of gamma-secretase inhibition, repressed by the Notch target Hes-1. That makes Cfd a target of the pathway, not a participant.

**Description:** removed the curation commentary ("The review accepts ...") and rewrote it as standalone biology.

**Open questions:**
- Should the Notch IMP be re-expressed by the curator as a regulation-of-expression or response annotation rather than involvement?
