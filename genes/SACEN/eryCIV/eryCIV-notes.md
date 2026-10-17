# eryCIV curation notes

## 2026-10-15 re-review after OpenScientist TreeGrafter control batch

- Blinded run [file:SACEN/eryCIV/eryCIV-hypotheses/function-hypothesis-go-0008483/openscientist.md,
  "EryCIV has Lys, not His"]: verdict partially supported / too general.
- Reproduced locally (Biopython global NW/BLOSUM62, gap -10/-0.5): EryCIV vs DesI Q9ZGH0
  60.9%, ArnB P77690 36.1%, EryC1 P14290 38.0%, ColD G4WJD4 26.9%. EryCIV K200 aligns to Lys
  in DesI/ArnB/EryC1 and to His in ColD.
- Abstracts of PMID:17630700 (DesI structure with product dTDP-4-amino-4,6-dideoxyglucose),
  PMID:9353926 (eryCIV named for AscC 3,4-dehydratase similarity) and PMID:9563840 (eryCIV
  deletion gives eryC phenotype) read via E-utilities; not cached in publications/.
- GO already has GO:0019179 (EC:2.6.1.33, RHEA:19085, verified via Rhea and ExPASy), so no new
  term was proposed.
- Decision: GO:0008483 UNDECIDED -> MODIFY to GO:0019179; core function MF updated.
