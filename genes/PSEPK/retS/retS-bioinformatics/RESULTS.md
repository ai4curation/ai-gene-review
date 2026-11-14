# RetS (PP_4824, Q88DK1) HATPase motif check

Question: P. aeruginosa RetS is reported to be kinase-dead because its HATPase
domain lacks the conserved G-boxes (PMID:29880803). Does KT2440 RetS share this?

Method: `uv run --no-project --script hatpase_motifs.py > results.txt`.
The script fetches the four sequences and their UniProt "Histidine kinase"
DOMAIN span from UniProt REST, scans the N-terminal half of that span for the
HisKA H-box (`H[ED]..[TN]`) and the C-terminal (HATPase) half for the G1
(`D.G.G`) and G2 (`G.G.G`) ATP-lid boxes, and reports BLOSUM62 global
pairwise identities. An N-box regex (`N..[NHT]A` in the first 60 aa of the
HATPase half) was also scanned; it matched in none of the four proteins,
including the two active GacS kinases, so it is uninformative and is not used.

## Result (from results.txt)

| protein | accession | HK domain | H-box | G1-box | G2-box |
|---|---|---|---|---|---|
| RetS KT2440 | Q88DK1 | 404-624 | 407 HEIRT | none | none |
| RetS PAO1 | Q9HUV7 | 421-641 | 424 HEIRT | none | none |
| GacS KT2440 | Q88MC3 | 292-513 | 295 HEIRT | 444 DTGIG | 474 GTGLG |
| GacS PAO1 | G3XD98 | 290-511 | 293 HEIRT | 442 DTGIG | 472 GTGLG |

Pairwise identity: RetS KT2440 vs RetS PAO1 0.615 (912 aligned columns);
GacS KT2440 vs GacS PAO1 0.684 (900); RetS KT2440 vs GacS KT2440 0.352 (767).

## Interpretation

KT2440 RetS lacks both G1 and G2 ATP-binding boxes in its HATPase region,
exactly like the kinase-dead PAO1 RetS, while both GacS proteins carry them
(DTGIG, GTGLG). KT2440 RetS retains the HExxT H-box, the motif needed for
transmitter phosphatase activity. KT2440 RetS is the clear ortholog of PAO1
RetS (61.5% identity over the full length). By orthology and motif
conservation, KT2440 RetS is therefore predicted to be unable to
autophosphorylate and to act on GacS by phosphoryl-group capture and
transmitter phosphatase activity rather than as a kinase. This is a sequence
inference; no biochemistry on KT2440 RetS exists.

## What the motif calls rest on

The scan region is the C-terminal half of the UniProt "Histidine kinase"
DOMAIN span, not Pfam HATPase_c bounds, and the regexes are loose. The G-box
calls are therefore trusted because of the controls, not because of regex
sensitivity: the two active GacS kinases (positive controls) score DTGIG and
GTGLG, and PAO1 RetS, which is biochemically kinase-dead (PMID:29880803),
scores none, exactly like KT2440 RetS.

## Residue-level mapping (gbox_alignment.py)

Method: `uv run --no-project --script gbox_alignment.py > gbox_alignment.txt`.
Each protein is aligned (BLOSUM62, global) to KT2440 GacS and the residues
aligned to the GacS G1 box (D444, G446, G448) and G2 box (G474, G476, G478)
are reported. All four UniProt sequences are at sequence version 1.

| protein | G1 box (D, G, G) | G2 box (G, G, G) |
|---|---|---|
| GacS KT2440 Q88MC3 | D444 G446 G448 | G474 G476 G478 |
| GacS PAO1 G3XD98 | D442 G444 G446 | G472 G474 G476 |
| RetS KT2440 Q88DK1 | D555 G557 P559 | G585 H587 G589 |
| RetS PAO1 Q9HUV7 | D572 G574 P576 | G602 H604 G606 |

The RetS G-boxes are degenerate rather than absent: both RetS proteins carry
proline at the third G1 glycine and histidine at the central G2 glycine.
These two positions are the residue sites hatpase_g1_box and hatpase_g2_box
in interpro/panther/PTHR45339/PTHR45339-review.yaml, with the GacS proteins
as positive and the RetS proteins as negative controls.

## PANTHER 19 tree extract (panther_tree_check.py)

Method: `uv run --no-project --script genes/PSEPK/retS/retS-bioinformatics/panther_tree_check.py`
(from the repository root). Writes panther_tree_check.yaml: tree size, which
PTHR45339 PAINT nodes are present, and the ancestors and leaves of
PTN009177399 (the WITH node of the RetS TreeGrafter GO:0071474 row) and
PTN000703787. Result: 76 leaves; only PTN000703787 of the eight PAINT nodes is
in the tree; PTN009177399 is the single Nematostella vectensis leaf A7T7B3,
under PTN000703787 (Unikonts) and PTN005207482 (Eukaryota).
