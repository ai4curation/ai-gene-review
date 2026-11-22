# mud review notes

- Fetched with `just fetch-gene DROME mud`; UniProt M9NEG4 confirmed (FlyBase FBgn0002873,
  GeneID 44839). 22 GOA rows.
- Full text read: PMID:21074723, 21855794, 22024168, 26886796, 26893348. Abstract only:
  10884435, 16510791, 17726110, 18594510, 19619498, 21920316, 8790424, plus the three 2006
  Mud/Pins papers I added (16740476, 16648843, 16648846).
- Core: Mud is the NuMA/LIN-5 counterpart: a cortical Pins(TPR)-binding, microtubule-binding
  coiled-coil protein that couples cortical polarity cues (Gαi/Pins, Dsh, TCJs/Gliotactin) to
  dynein-mediated astral microtubule pulling for spindle orientation [PMID:16740476 "Like
  NuMA, Mud can bind to microtubules and enhance microtubule polymerization."]
- DNA binding (IDA, PMID:21855794): full text has no DNA assay; the experiment is
  Pins-TPR binding a fluorescent Mud peptide. Recorded as a FlyBase WRONG_TERM source
  defect; REMOVE.
- Spindle midzone (IDA, PMID:16510791): the abstract places Mud on the central spindle pole
  body between the tandem MII spindles - a pole structure, so MODIFY to meiotic spindle pole.
- Basal cortex (IDA, PMID:17726110): abstract only, apical localization is the norm; UNDECIDED.
- Thermosensory behaviour (PMID:18594510): screen; abstract does not name mud; over-annotation.
- Tricellular tight junction: GO term is defined by tight-junction sealing strands;
  Drosophila TCJ is a tricellular septate junction. Raised as a suggested question.
- Added NEW microtubule binding (IDA, PMID:16740476).
