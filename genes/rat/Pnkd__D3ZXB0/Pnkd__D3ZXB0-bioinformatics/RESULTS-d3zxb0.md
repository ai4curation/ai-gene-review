# D3ZXB0 (rat Pnkd canonical) vs reviewed mouse/human PNKD isoforms

Sequences fetched live from UniProt REST; Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5.

| Entry | Length | Identical residues | Identity over D3ZXB0 length |
|---|---|---|---|
| B4F7D2 | 369 | 338 | 0.797 |
| Q69ZP3 | 385 | 382 | 0.901 |
| Q69ZP3-2 | 142 | 131 | 0.309 |
| Q69ZP3-3 | 424 | 421 | 0.993 |
| Q69ZP3-4 | 360 | 320 | 0.755 |
| Q8N490 | 385 | 369 | 0.870 |
| Q8N490-2 | 142 | 121 | 0.285 |
| Q8N490-3 | 361 | 309 | 0.729 |
| Q8N490-4 | 325 | 299 | 0.705 |

## MR-1S-specific exon segment
Mouse Q69ZP3-2 residues 80-118: `AIGFPCGILFFVLTKQEVDKDRLKQMKARQNMRVSNTGE`
Exact substring of D3ZXB0: True; position in D3ZXB0: 80
D3ZXB0 residues 80-118: `AIGFPCGILFFVLTKQEVDKDRLKQMKARQNMRVSNTGE`
Human Q8N490-2 residues 80-118: `AIGFPCGILLFILTKREVDKDRVKQMKARQNMRLSNTGE` (identical to D3ZXB0 80-118 at 34/39 aligned positions)

## Human Q8N490 Zn(2+) ligand and PNKD disease positions mapped onto D3ZXB0

| Q8N490 position | Q8N490 residue | D3ZXB0 position | D3ZXB0 residue |
|---|---|---|---|
| 7 | A | 7 | A |
| 9 | A | 9 | A |
| 33 | A | 33 | A |
| 172 | H | 211 | H |
| 174 | H | 213 | H |
| 176 | D | 215 | D |
| 177 | H | 216 | H |
| 229 | H | 268 | H |
| 253 | D | 292 | D |
| 291 | H | 330 | H |

## Kyte-Doolittle 19-residue window, D3ZXB0 residues 56-140
Maximum mean hydropathy 2.18 for window starting at residue 74 (`AVGLAWAIGFPCGILFFVL`); values > 1.6 are conventionally taken as candidate transmembrane segments.

N-terminal 40 residues of D3ZXB0 (region containing the reported mitochondrial targeting sequence of MR-1L/MR-1S):
`MAAVVAATALKGRGARNARVLRGILSGATANKASQNRTRA`


## PAINT IBD rows in PTHR11935 for the terms under review
Source: interpro/panther/PTHR11935/PTHR11935-paint.tsv

| node | GO id | aspect | evidence | seeds | taxon |
|---|---|---|---|---|---|
| PTN000232795 | GO:0004416 | F | IBD | AGI_LocusCode:AT2G31350|AGI_LocusCode:AT2G43430|AGI_LocusCode:AT3G10850|MGI:MGI:95745|RGD:2779|SGD:S000002680|SGD:S000005566|UniProtKB:C0H490|UniProtKB:Q16775|UniProtKB:Q8I5Y8 | taxon:2759 |
| PTN000940186 | GO:0005739 | C | IBD | UniProtKB:Q8N490 | taxon:6072 |
| PTN002631193 | GO:0005739 | C | IBD | UniProtKB:Q16775 | taxon:117571 |
| PTN002631193 | GO:0006749 | P | IBD | RGD:2779|UniProtKB:Q16775 | taxon:117571 |
| PTN004322580 | GO:0016790 | F | IBD | AGI_LocusCode:AT2G31350|AGI_LocusCode:AT2G43430|AGI_LocusCode:AT3G10850|MGI:MGI:95745|RGD:2779|SGD:S000002680|SGD:S000005566|UniProtKB:C0H490|UniProtKB:Q16775|UniProtKB:Q8I5Y8 | taxon: |

PAINT nodes seeded by human PNKD Q8N490: PTN000940186

Interpretation is left to the review; alignment does not establish expression, localization or activity.
