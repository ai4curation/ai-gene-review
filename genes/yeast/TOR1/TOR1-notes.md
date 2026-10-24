# TOR1 notes

## 2026-09-29 IBA re-review

- TOR1 is in PANTHER family `PTHR11139`, subfamily `PTHR11139:SF9`
  (`SERINE_THREONINE-PROTEIN KINASE MTOR` in the UniProt/PANTHER record).
- The six TOR1 IBA rows in the GOA snapshot are all still present in the
  current local PAINT export:
  - `PTN000124197`: `GO:0004674 protein serine/threonine kinase activity` and
    `GO:0005634 nucleus`
  - `PTN000124327`: `GO:0005737 cytoplasm`, `GO:0038201 TOR complex`, and
    `GO:0016242 negative regulation of macroautophagy`
  - `PTN000124328`: `GO:0038202 TORC1 signaling`
- Current PAINT also places `GO:0031929 TOR signaling` at `PTN000124327` and
  `GO:0038203 TORC2 signaling` at `PTN000124328`, but the GOA snapshot does not
  propagate either assertion to TOR1 as IBA. TOR1 already carries direct and
  electronic `GO:0031929` rows, and the TORC2 term is not appropriate for TOR1.
- The six legacy `GO:0005515 protein binding` IPI review actions were migrated
  from `MARK_AS_OVER_ANNOTATED` to `REMOVE`. The reported IntAct interactions
  are not challenged; the GO term is simply too generic to describe TOR1's
  kinase or complex function.

## 2025-2026 literature refresh

Recent papers continue to refine upstream nutrient sensing and regulatory-state
control of yeast TORC1, especially through Gtr1/Gtr2, Pib2, Ait1, Gcn2, and
SEAC/EGOC, but do not change the reviewed core model of TOR1 as a TORC1
serine/threonine kinase catalytic subunit that coordinates growth with
macroautophagy inhibition.

- Gtr1/2 and Pib2 drive multiple TORC1 signaling states in budding yeast
  [PMID:40622848 "Here, we report that this dual regulator system pushes TORC1
  into at least three distinct signaling states"].
- Ait1, Gcn2, and SEAC/GATOR cooperate to regulate TORC1 during nitrogen
  limitation and starvation [PMID:41318596 "SEAC, Ait1, and Gcn2 cooperate to
  drive TORC1 into a fully inhibited state"].
- Cryo-EM and functional analysis refined the yeast amino-acid-sensing
  SEAC-EGOC supercomplex [PMID:41680390 "Here we determined the cryo-electron
  microscopy structure of the SEAC bound to its substrate, the EGOC
  (Ragulator-Rag), and studied its function in TORC1 amino acid signaling"].
- Tor1 A2357T confers growth-promoting TORC1 activity independent of Gtr1/2 and
  Pib2 [PMID:41513735 "identified a novel, dominant TOR1 mutation introducing
  an A2357T substitution into the Tor1 kinase domain"].
