# UBE2F (Q969M7) evolutionary grounding

Script: `panther_placement.py` (raw output in `results.txt`). Run on 2026-10-20.

## PANTHER subfamily placement (live PANTHER geneinfo API)

| Protein | Accession | Family | Subfamily | Subfamily name |
|---|---|---|---|---|
| human UBE2F | Q969M7 | PTHR24068 | PTHR24068:SF129 | NEDD8-CONJUGATING ENZYME UBE2F |
| mouse Ube2f | Q9CY34 | PTHR24068 | PTHR24068:SF129 | NEDD8-CONJUGATING ENZYME UBE2F |
| human UBE2M | P61081 | PTHR24068 | PTHR24068:SF132 | NEDD8-CONJUGATING ENZYME UBC12 |
| mouse Ube2m | P61082 | PTHR24068 | PTHR24068:SF132 | NEDD8-CONJUGATING ENZYME UBC12 |
| yeast UBC12 | P52491 | PTHR24068 | PTHR24068:SF132 | NEDD8-CONJUGATING ENZYME UBC12 |

The live PANTHER release numbers the E2 family PTHR24068; the UniProt record and the
local PAINT cache use PTHR24067 (an older release). UBE2F and its mouse ortholog form
their own subfamily (SF129), separate from the UBE2M/UBC12 subfamily (SF132) that
contains the yeast and fly NEDD8 E2s. Yeast has no UBE2F-subfamily member.

## PAINT node PTN000630367 (local PTHR24067 PAINT cache)

| GO term | Aspect | Evidence | Negated | Seeds |
|---|---|---|---|---|
| GO:0019788 NEDD8 transferase activity | F | IBD | false | FB:FBgn0035853, MGI:1915171, SGD:S000004297, UniProtKB:P61081, UniProtKB:Q969M7 |
| GO:0045116 protein neddylation | P | IBD | false | same five seeds |
| GO:0005829 cytosol | C | IBD | false | UniProtKB:Q57TW2 |
| GO:0061631 ubiquitin conjugating enzyme activity | F | IRD | true | PANTHER:PTN002514495 |
| GO:0000209 protein polyubiquitination | P | IRD | true | PANTHER:PTN002514495 |

The node is seeded by both the UBE2M/UBC12 subfamily (yeast, fly, mouse, human) and by
human UBE2F, so it sits above both subfamilies. NEDD8 transfer is therefore an
ancestral property of the clade that includes UBE2F. PAINT curators also placed
deliberate negative (IRD, NOT) assertions on ubiquitin-conjugating activity and protein
polyubiquitination at this node. The UBE2F-specific features (pairing with RBX2,
selectivity for CUL5) rest on direct experiments on human UBE2F, not on transfer from
UBE2M.

## Sequence checks (UniProt Q969M7 canonical isoform)

- Length 185 aa; residue 1 is Met (the N-acetylated Met recognised by DCNL co-E3s).
- Residue 116 is Cys in context `ETGEICLSLLR`, the UBC active-site cysteine that forms
  the NEDD8 thioester.
