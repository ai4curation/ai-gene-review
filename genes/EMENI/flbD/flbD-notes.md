# flbD (Aspergillus nidulans) — curation notes

UniProt G5EAY5 (FLBD_EMENI). Myb-like transcription factor; upstream developmental
activator. Upstream-activation tier of the module.

- Myb-like DNA-binding protein coordinating conidiophore-development initiation.
  [PMID:7883170 "flbD encodes a Myb-like DNA-binding protein that coordinates initiation of Aspergillus nidulans conidiophore development"].
- Uniquely required for BOTH asexual and sexual differentiation.
  [PMID:22798393 "FlbD, a Myb transcription factor of Aspergillus nidulans, is uniquely involved in both asexual and sexual differentiation"].
- **Notable over-propagation:** a large ARBA/InterPro2GO (GO_REF:0000117) IEA block
  propagates plant/animal Myb terms. REMOVED as taxon-inappropriate:
  regulation of stomatal complex patterning (GO:2000037), multicellular water
  homeostasis (GO:0050891), salt-stress (GO:1901002) and water-deprivation
  (GO:1902584) response regulation. MARK_AS_OVER_ANNOTATED: post-embryonic/tissue/
  system development, endoreduplication & G1/S cell-cycle regulation, response to
  lipid/alcohol, mitotic cell cycle (IBA).

## Re-review 2026-10-01 (GOA refresh)

- Retired (no longer in the current GOA snapshot): the ARBA (GO_REF:0000117) IEA rows
  GO:0009888 tissue development and GO:0030154 cell differentiation. Their reviews
  (MARK_AS_OVER_ANNOTATED and KEEP_AS_NON_CORE) are kept as history; retirement records
  disappearance from GOA, not a biological judgment.
- New ARBA row GO:0048869 cellular developmental process (IEA, GO_REF:0000117) reviewed:
  KEEP_AS_NON_CORE - a broad, correct-but-uninformative parent of conidium formation and
  peridium differentiation; the specific conidiation/cleistothecium terms carry the core.
- Added a propagation_review to the IBA GO:0000278 mitotic cell cycle row
  (MARK_AS_OVER_ANNOTATED; PTN000067791 carries metazoan Myb cell-cycle roles not shown
  for the fungal FlbD lineage), and a supporting quote for the nitrogen-starvation row.
