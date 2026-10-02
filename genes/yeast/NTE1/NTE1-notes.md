# NTE1 notes

## 2026-09-28 re-review

- Re-reviewed the two IBA rows in `NTE1-goa.tsv`. Both the
  `GO:0004622` lysophospholipase activity IBA and the `GO:0005783`
  endoplasmic-reticulum IBA trace to `PANTHER:PTN000369206`.
- The IBA `WITH/FROM` lists include `SGD:S000004524`, NTE1 itself. This is valid
  descendant experimental evidence used to place the PAINT node, not circular
  support.
- Re-read cached PMID:15044461 for the direct YML059c/Nte1 catalytic and ER
  evidence and PMID:19841481 for the downstream Opi1/phospholipid-biosynthetic
  transcription phenotype. These support the current ACCEPT and KEEP_AS_NON_CORE
  calls.
- Searched for newer NTE1 literature. A 2023 Gpc1/Ale1 PC
  deacylation/reacylation pathway study [PMID:37269946, "The acyltransferase
  Gpc1 is both a target and an effector of the unfolded protein response in
  Saccharomyces cerevisiae"] refined the downstream GPC reacylation arm, but
  did not change the interpretation of yeast NTE1 as the ER
  phosphatidylcholine-deacylating phospholipase B.
- Removed broad `GO:0006629` lipid metabolic process from `core_functions`;
  the reviewed annotations correctly mark that parent as too broad, while
  `GO:0034638` phosphatidylcholine catabolic process captures the direct process.
