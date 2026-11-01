# YAB3 review notes

## 2026-10-28 session

- Fetched with `just fetch-gene ARATH YAB3`; UniProt Q9XFB1 (YAB3_ARATH, TAIR AT4G00180,
  GeneID 827914) confirmed; 29 GOA rows.
- No deep-research API keys: literature synthesis written by hand in
  `YAB3-deep-research-manual.md`.
- Key paper PMID:23133401 (Gonzalez-Reig 2012) read in full: YAB3 is part of JAG/FIL
  activity in the ovary; yab3 single mutant raises BP transcripts in pistils by qRT-PCR
  [PMID:23133401 "including yab3"]; as1 yab3 fruits form ectopic valve margin. Supports
  fruit development (non-core) and the repressive role toward BP.
- PMID:23025792 read (full text): BD:YAB3 activates UAS::LUC in planta (1.8-fold) but not
  in yeast; YABs proposed to be bifunctional TFs.
- PMID:42860685 (2026, full text): YAB3-mCherry nuclear; SPL8-YAB3 BiFC and FRET-FLIM in
  nuclei; SPL8 directly activates YAB3. Used as direct evidence for nucleus.
- Paralog review genes/ARATH/YAB1 used for consistency of actions.

## Decisions

- Nine bare protein binding rows removed by policy (informative partners LUG/LUH, SPL/NZZ,
  SPL8 captured in description/core functions).
- cell fate commitment (IBA) MODIFY -> abaxial cell fate specification (GO:0010158). OAK:
  GO:0010158 is_a GO:0001708 cell fate specification, which is part_of GO:0045165, so the
  replacement is a part_of descendant, not an is_a descendant.
- SAM, leaf development and fruit development rows: KEEP_AS_NON_CORE (non-cell-autonomous
  or downstream developmental consequences, redundant with FIL).
- No NEW rows: nucleus already present from three sources; anther/vascular phenotypes do
  not meet the NEW process bar (SRDX chimera / mutant phenotype only).

## Open questions

- UniProt FUNCTION says YAB3 "Binds DNA without sequence specificity" citing PMID:10457020
  and PMID:12417699; the abstracts do not show this and the biochemical evidence is for FIL
  (PMID:11812777). Could not check full texts, so not recorded as a source defect.
