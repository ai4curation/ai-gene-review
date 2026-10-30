# AQP5-AS1 (MIAC) notes

- AQP5-AS1 encodes MIAC, a 51-aa micropeptide (UniProt A0A7L8Y648, PE1).
- **No affinage record exists** for AQP5-AS1 (the script returned no content, 2026-10-04).
- Evidence comes from two papers from one group:
  - HNSCC [PMID:32176498]: abstract-only; MIAC-AQP2 binding, F-actin loss via SEPT2/ITGB4.
  - RCC [PMID:36117171]: full text; binding by co-IP, Y2H, MST, SPR and mutant pulldowns; lowers EREG/EGFR expression.
- **GOA calls:**
  - AQP2 IPI rows → REMOVE: there is no informative MF term, though the interaction is well supported.
  - Actin filament organization (IMP) → MODIFY to regulation of actin filament organization (GO:0110053).
  - Regulation of EGFR signaling (IMP) → MODIFY to negative regulation (GO:0042059).
  - Both changed from over-annotated in the review round: 'regulation of' terms accommodate expression-mediated effects (repo precedent).
- MF_DARK knowledge gap.
- Review round (PR #4162):
  - The RCC abstract sentence saying MIAC 'activates' PI3K/AKT contradicts the paper's own Results and Discussion (inhibits). The Results quotes are used instead.
  - UniProt FUNCTION says SEPTIN4 where the primary paper says SEPT2; likely a UniProt mis-transcription.
  - AQP2 is a collecting-duct water channel, so an AQP2 mechanism in head and neck carcinoma is unexpected on expression grounds.
