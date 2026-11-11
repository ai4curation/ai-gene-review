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
