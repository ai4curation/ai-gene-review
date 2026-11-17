# eda (P0A955, b1850) notes

## Session 2026-11-13

Deep research was not generated: the falcon provider failed for the sister review
(BACSU gpmI) in this offline environment, so it was not retried here.

Literature checked (cached in `publications/`): PMID:4945194, PMID:1624451,
PMID:15659677, PMID:11274385, PMID:11342129, PMID:11094340, PMID:17962400,
PMID:1339418 (abstracts); PMID:17981470 (full text); PMID:1098660, PMID:4560498 and
PMID:7007372 (title only, no abstract in PubMed); proteomics PMID:15911532,
PMID:18304323 (full text), PMID:16858726, PMID:24561554 (full text).

### Identity

- UniProt P0A955 ALKH_ECOLI, eda (hga, kdgA), b1850/JW1839, 213 aa, E. coli K-12.
- PANTHER PTHR30246 (2-KETO-3-DEOXY-6-PHOSPHOGLUCONATE ALDOLASE), subfamily
  PTHR30246:SF1 (2-DEHYDRO-3-DEOXY-6-PHOSPHOGALACTONATE ALDOLASE-RELATED).
  Pfam PF01081 Aldolase; NCBIfam TIGR01182 eda; class I (Schiff base) aldolase,
  (alpha/beta)8 barrel, homotrimer.

### Function

- KDPG aldolase: KDPG <-> pyruvate + D-glyceraldehyde 3-phosphate. Lys133 Schiff base,
  Glu45 general base. [PMID:11274385 "KDPG aldolase catalyzes the reversible cleavage of
  KDPG to pyruvate and glyceraldehyde-3-phosphate."]
- Same protein as the classic "KHG aldolase". [PMID:1624451 "The data presented here
  provide proof that the two enzymes are identical."] KHG cleavage is S-stereoselective
  (UniProt CC FUNCTION, PubMed:1098660, PubMed:4560498).
- Oxaloacetate beta-decarboxylase activity in vitro (UniProt, PubMed:1339418,
  PubMed:4560498); no physiological role shown.
- eda mutants: complete loss of KDPG aldolase and no growth on gluconate, glucuronate or
  galacturonate. [PMID:4945194 "The inability to grow on the uronic acids was expected,
  because the aldolase is on the sole known pathway of their metabolism."]
- Regulation: three promoters (GntR/P1 gluconate, KdgR/P2 hexuronates, PhoB/P4 phosphate
  starvation). [PMID:15659677]

### Problem row

- GO:0008700 (R,S)-4-hydroxy-2-oxoglutarate aldolase activity, IDA, PMID:17981470
  (UniProt). The cached full text of PMID:17981470 is about KDPGal aldolase (DgoA) and
  KDPG aldolase stereoselectivity for KDPG vs KDPGal; it contains no 4-hydroxy-2-
  oxoglutarate assay. E. coli Eda is (4S)-specific, so the (R,S) term is also the wrong
  stereospecificity. MODIFY to GO:0106009 (lateral correction) and record a source defect.

### GO-CAM/BP gap

GOA has no biological-process row for eda. kdgK (the preceding step of hexuronate
catabolism) carries D-glucuronate and D-galacturonate catabolic process by IMP, and edd
carries Entner-Doudoroff pathway. Eda catalyses the last step of both routes, so NEW rows
for GO:0061678, GO:0042840 and GO:0019698 are proposed from PMID:4945194.
