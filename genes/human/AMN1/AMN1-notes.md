# AMN1 (Q8IY45) review notes

## 2026-10-04: PAINT/affinage review

**Affinage symbol collision (real).** The affinage record for AMN1 describes only budding-yeast Amn1: Tem1/MEN antagonist, Ace2 degradation, the AMEN pathway. A blocking trust gate fired; I quarantined the output with --out and read it. It is not about the human protein, so it was not written to the gene folder and is not used.

Human-specific checks:
- **No human literature.** A Europe PMC search for human AMN1, excluding yeast, returns only expression-list and circRNA hits.
- **No F-box.** See `AMN1-bioinformatics/RESULTS.md`: no F-box is annotated or detected (InterPro, Pfam and SMART find only LRRs), and only the N-terminal 2-28 aligns weakly to the FBXL15 F-box.
- **No membrane features:** neither human AMN1 nor mouse Amn1 has an annotated transmembrane segment or signal peptide in UniProt.
- **Mouse microvillus source:** the IEA rests on an MGI IDA for mouse Amn1 from PMID:14321840, a 1965 study of vitamin B12-binding substances. The paper's other mouse annotations are to Cubn and Cblif, the cubilin-intrinsic factor system whose membrane partner is amnionless (symbol Amn), not Amn1.

Decisions:
- **SCF complex and SCF-dependent catabolism (IBA, node PTN002547163, F-box-containing FBXL donors): MARK_AS_OVER_ANNOTATED**, with propagation_review. These are a sequence inference, not a negative experiment.
- **Microvillus membrane (IEA from mouse): REMOVE.** The source is a homonym mix-up, confirmed in round 1 by MGI's own GO-CAM (see below). This is recorded as propagation_review SOURCE_BAD and raised as a question for MGI.
- **Gene recorded as WHOLLY_DARK.**

## Round 1 (PR #4034 review)

- **GO-CAM confirms the source-side mix-up.** `gocams/index.tsv` lists MGI:MGI:2442933 "Amn1 Mmus" in model 62900b6400002552, "Cobalamin transport, into enterocytes (Mouse)", as cargo receptor activity in the microvillus membrane, citing PMID:14321840 alongside Cubn and Cblif and with no Amn. That cargo-receptor role is amnionless's, the cubilin partner.
- **All IBA donors verified as F-box proteins (UniProt F-box DOMAIN features):**
  - FBXL5, FBXL7 and FBXL15 (human)
  - Fbxl7 and Fbxl2 (mouse)
  - Fbxl7 (fly)
  - fbxl14a and fbxl14b (zebrafish)
  - SKP2A, FBL17, FBL3 and EBF2 (Arabidopsis)
  - D3 (rice)
  - YDR306C and YLR352W (yeast; neither is yeast AMN1, P38285)
