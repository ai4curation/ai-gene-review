# D14 (AtD14, At3g03990, UniProt Q9SQR3) curation notes

Context: reviewed as part of the `strigolactone_signaling_shoot_branching` module (D14 receptor ->
SCF(MAX2) -> SMXL6/7/8 degradation -> BRC1). Falcon deep research was attempted but all providers
failed, so these notes are built from cached publications.

## Identity
- UniProt Q9SQR3 (D14_ARATH, 267 aa), alpha/beta hydrolase, catalytic triad S97/D218/H247.
- Arabidopsis ortholog of rice D14; paralog KAI2 mediates karrikin responses
  [PMID:22357928 "AtD14, is also necessary for normal strigolactone responses in seedlings and adult plants"].

## Receptor function
- SL induces open-to-closed transition and D14-D3/MAX2-ASK1 complex
  [PMID:27479325 "Here we report the crystal structure of the strigolactone-induced AtD14-D3-ASK1 complex"].
- Catalytically dead AtD14 D218A still complements atd14 -> intact SL binding may suffice
  [PMID:30643123 "we show that an AtD14D218A catalytic mutant that lacks enzymatic activity is still able to complement the atd14 mutant phenotype in an SL-dependent manner"].
- GR24-enhanced interaction with SMXL6/7 (Y2H, co-IP) [PMID:26546446 "In response to rac -GR24 treatment, SMXL6 and SMXL7 directly interacted with D14 in yeast cells in a concentration-dependent manner"].
- Nuclear D14 binds SMXL7 and MAX2 SL-dependently [PMID:27317673 "nucleus-localized D14 can physically interact with both SMXL7 and the MAX2 F-box protein in a SL-dependent manner"].

## Hydrolase
- Hydrolyses GR24 butenolide; very slow turnover [PMID:23381136 "only the D14 proteins were able to hydrolyze GR24, demonstrating hormone substrate specificity for this class of signaling hydrolases"].
- Hydrolysis deactivates SL after signalling [PMID:30643123 "We also demonstrate that D14 can deactivate SLs by hydrolytic degradation after signal transmission."].

## Localisation / feedback
- Nucleus + cytoplasm, overlapping MAX2; local action; SL-induced MAX2-dependent degradation [PMID:24610723].

## Curation decisions
- GO:1901601 strigolactone biosynthetic process: IBA REMOVE (receptor clade, d14 is SL-insensitive);
  IMP (PMID:22422982) also REMOVE on the same biology. Full text is not open access (Europe PMC: no PMC
  copy; science.org returns 403), so the assay could not be read; the same paper's IMP secondary shoot
  formation row suggests it was a branching phenotype, which reflects SL insensitivity, not biosynthesis.
  D14 does none of the work of SL formation (D27/CCD7/CCD8/MAX1 do), so the term is contradicted
  regardless of evidence code. (Changed from MARK_AS_OVER_ANNOTATED after PR #4383 review.)
- GO:0010223 secondary shoot formation -> MODIFY to GO:2000032 regulation of secondary shoot formation.
- protein binding to SMXLs/MAX2 -> MODIFY to GO:0038023 signaling receptor activity; HT HIPP26 -> REMOVE.
- NEW: GO:0038023 signaling receptor activity; GO:0052689 carboxylic ester hydrolase activity.
- Proposed term: strigolactone receptor activity (child of GO:0038023, analogous to GO:0038198 auxin receptor activity).
