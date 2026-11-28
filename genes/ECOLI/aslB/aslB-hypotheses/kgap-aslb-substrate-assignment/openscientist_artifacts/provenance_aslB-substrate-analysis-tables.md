# Computed provenance tables: AslB substrate assignment (P25550)

All values below were produced by code executed during this run against public
resources (UniProt REST, NCBI E-utilities, STRING v12 API, NCBI BLOSUM62 matrix).
No value is hand-entered from memory. Figures plot_1 to plot_5 in this directory
are the rendered versions of tables 1, 2, 3 and 4.

Resources that could not be used, stated plainly: EBI Clustal Omega and EBI EMBOSS
REST returned HTTP 400 "temporarily blocked", so the multiple alignment was replaced
by in-house Needleman-Wunsch pairwise alignment with BLOSUM62 (gap open -11, extend -1).
KEGG REST returns no KO assignment for b3800, b3801, b1497, b1498 or b3678, so KO-based
neighbourhood analysis was not possible. The PaxDb public API returned 404 for all
queries, so abundance values were not retrieved.

## Table 1. Formylglycine position of every type I sulfatase encoded in E. coli K-12

Set defined as UniProt taxonomy_id:83333 with Pfam PF00884 (12 proteins), intersected
with InterPro IPR024607 "sulfatase, conserved site" (3 proteins). The nine PF00884
proteins excluded are EptA (b4114), EptB (b3546), EptC (b3955), OpgB (b4359), OpgE
(b0815), PbgA (b2188) and YhbX (b3173), all alkaline-phosphatase-superfamily
phosphotransferases with no (C/S)XPXR in a sulfatase context.

| protein | uniprot | length | nucleophile | motif | context | type | status | all (C/S)XPXR hits |
|---|---|---|---|---|---|---|---|---|
| aslA / b3801 | P25549 | 551 | S136 | SSPTR | ILTSAYSQPS[S]SPTRATILTG | Ser-type | predicted from signature + alignment | 136:SSPTR; 315:SSPAR |
| ydeN / b1498 | P77318 | 560 | S132 | SGPSR | FTNGYVAHGV[S]GPSRAAIMTG | Ser-type | predicted from signature + alignment | 132:SGPSR |
| yidJ / b3678 | P31447 | 497 | C52 | CTPAR | FNSAYTCSPV[C]TPARAGLFTG | Cys-type | predicted from signature + alignment | 52:CTPAR |
| AtsA K. pneumoniae | Q9X759 | 577 | S72 | SAPAR | RMSQYYTSPM[S]APARSMLLTG | Ser-type | demonstrated, ECO:0000269 PubMed:9478923 | 72:SAPAR |
| AtsA P. aeruginosa | P51691 | 536 | C51 | CSPTR | RLTDFHTAST[C]SPTRSMLLTG | Cys-type | demonstrated, ECO:0000269 | 51:CSPTR |
| ARSA human | P15289 | 507 | C69 | CTPSR | FTDFYVPVSL[C]TPSRAALLTG | Cys-type | demonstrated, ECO:0000269 | 69:CTPSR |

Positional equivalence test (Needleman-Wunsch, BLOSUM62, gap -11/-1). Eight of nine
pairwise alignments place the predicted nucleophile exactly on the demonstrated
formylglycine of the reference:

| query | query residue | reference | reference FGly | aligns to | match | global % identity |
|---|---|---|---|---|---|---|
| AslA | S136 | AtsA K. pneumoniae | S72 | 72 | yes | 25.2 |
| AslA | S136 | AtsA P. aeruginosa | C51 | 51 | yes | 25.0 |
| AslA | S136 | ARSA human | C69 | 69 | yes | 29.0 |
| YdeN | S132 | AtsA K. pneumoniae | S72 | 72 | yes | 24.1 |
| YdeN | S132 | AtsA P. aeruginosa | C51 | 52 | off by one | 24.8 |
| YdeN | S132 | ARSA human | C69 | 69 | yes | 27.4 |
| YidJ | C52 | AtsA K. pneumoniae | S72 | 72 | yes | 24.5 |
| YidJ | C52 | AtsA P. aeruginosa | C51 | 51 | yes | 27.0 |
| YidJ | C52 | ARSA human | C69 | 69 | yes | 26.6 |

## Table 2. Genomic arrangement of maturase and sulfatase gene pairs

Coordinates read from the GenBank feature tables, not from secondary annotation.
For aslB and aslA the raw feature lines in U00096.3 region 3,982,000-3,987,000 are
`CDS 959..2194 /gene="aslB"` and `CDS complement(2353..4008) /gene="aslA"`.

| pair | source | gene A coords | gene B coords | same strand | arrangement | intergenic bp | operon possible |
|---|---|---|---|---|---|---|---|
| aslB - aslA (E. coli K-12) | U00096.3 | 3,982,958-3,984,193 (+) | 3,984,352-3,986,007 (-) | no | convergent, 3' ends facing | 158 | no |
| ydeN - ydeM (E. coli K-12) | U00096.3 | 1,580,842-1,582,524 (-) | 1,579,633-1,580,790 (-) | yes | co-oriented, ydeN then ydeM | 51 | yes |
| yidF - yidJ (E. coli K-12) | U00096.3 | 3,855,114-3,855,611 (-) | 3,856,911-3,858,404 (-) | yes | yidG, yidH and the opposite-strand yidI intervene | 1299 | no |
| atsB - atsA (K. pneumoniae) | AJ131525 | 623-1,810 (+) | 1,855-3,588 (+) | yes | co-oriented operon, atsB then atsA | 44 | yes |

## Table 3. STRING v12 evidence channels, species 511145, required_score 0

| pair | combined | neighbourhood | phylogenetic profile | coexpression | experiments | databases | textmining |
|---|---|---|---|---|---|---|---|
| aslB - aslA | 0.961 | 0.083 | 0.665 | 0.186 | 0.000 | 0.000 | 0.865 |
| ydeM - ydeN | 0.983 | 0.631 | 0.713 | 0.637 | 0.000 | 0.000 | 0.627 |
| yidF - yidJ | 0.565 | 0.083 | 0.539 | 0.055 | 0.000 | 0.000 | 0.000 |

Cross-pair phylogenetic profile scores, showing the channel does not discriminate:
yidF - aslB 0.772, ydeN - aslB 0.719, yidJ - aslB 0.652, ydeM - aslA 0.636,
yidF - aslA 0.656.

UniProt protein-existence and proteomics cross-references: AslB P25550 PE=3 (PaxDb only),
AslA P25549 PE=3 (PaxDb only), YdeN P77318 PE=3 (PaxDb, jPOST), YidJ P31447 PE=3
(PaxDb only). Control PbgA P0AD27 is PE=1 with a jPOST record.

## Table 4. Integrity of the type I sulfatase catalytic set

Reference positions are the human ARSA (P15289) catalytic and metal-binding residues
carrying ECO:0000269 and ECO:0007744 evidence: D29, D30, C69, K123, H125, S150, H229,
D281, N282, K302.

| protein | residues aligned to the ARSA set | identical | nucleophile | substitutions |
|---|---|---|---|---|
| AslA (E. coli) | D94, D95, S136, K188, H190, V213, H303, D356, N357, K375 | 8/10 | S136 | ARSA S150 to V213; Cys/Ser nucleophile swap |
| YdeN (E. coli) | D66, D67, S132, K183, H185, P195, H286, D345, N346, K364 | 8/10 | S132 | ARSA S150 to P195; Cys/Ser nucleophile swap |
| YidJ (E. coli) | D12, T13, C52, K100, H102, gap, H194, D284, H285, gap | 6/10 | C52 | D30 to T13, S150 gap, N282 to H285, K302 gap |
| AtsA (K. pneumoniae) | D34, D35, gap, K132, H134, S160, G244, D329, N330, K383 | 8/10 | S72 | H229 to G244; nucleophile column gapped in this pairwise alignment |
| AtsA (P. aeruginosa) | D13, D14, C51, K113, H115, gap, H211, D317, N318, R352 | 8/10 | C51 | S150 gap; K302 to R352 |

## Table 5. Export signals

| protein | signal peptide (UniProt) | evidence | twin-arginine motif in first 45 aa |
|---|---|---|---|
| AslA P25549 | 1-24 | ECO:0000255 (predicted) | none |
| YdeN P77318 | 1-29 | ECO:0000255 (predicted) | none |
| YidJ P31447 | none annotated | - | none |
| AtsA Q9X759 (precedent) | 1-20 | ECO:0000255 (predicted) | none |
| AslB P25550 | none annotated | - | none (cytoplasmic radical SAM enzyme) |

AslA and the characterised precedent AtsA both carry a predicted Sec-type signal
peptide, so export topology does not separate them.
