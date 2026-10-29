# NTE1 notes

## 2026-10-01 current GOA and PAINT refresh

- Forced a current GOA/UniProt refresh. GOA still carries the two core IBA rows,
  `GO:0004622` phosphatidylcholine lysophospholipase A1 activity and
  `GO:0005783` endoplasmic reticulum, on `PANTHER:PTN000369206`.
- Fetched the current `PTHR14226` PAINT slice. `PTN000369206` still asserts
  both NTE-family IBD rows, with `SGD:S000004524` among the descendant evidence;
  the target's self-donor is valid experimental grounding, not circular support.
- Reviewed seven new current GOA rows. The direct UniProt `GO:0005789`
  endoplasmic reticulum membrane and `GO:0102545` B-type glycerophospholipase
  activity rows are sound duplicates of already-accepted biology.
- Marked the new ARBA `GO:0004620` glycerophospholipase activity, `GO:0016020`
  membrane, and `GO:0052689` carboxylic ester hydrolase activity rows as
  over-annotations of more precise existing rows. The new InterPro
  `GO:0006629` lipid metabolic process row is likewise an over-broad duplicate.
- Removed both lipid-droplet rows. PMID:24868093 placed Nte1 in a reproducible
  lipid-droplet purification cluster, but the paper's microscopy check found
  that Nte1-GFP did not show LD localization and interpreted Nte1 as
  co-purifying with, rather than localizing to, lipid droplets.
- Searched PubMed/web for newer `NTE1`, `Nte1`, and `YML059C` papers through
  2026-10-01. No newer primary paper changed the 2023 interpretation that Nte1
  initiates PC-DRP by generating glycerophosphocholine, which Gpc1 and Ale1 then
  reacylate for ER membrane homeostasis.

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
