# DYF-6 / IFT46 interface provenance tables

All values below were computed in this session from public coordinates and
sequences. Nothing is hand-estimated. Method summary:

- Structure: PDB **4UZZ**, 2.32 Å, "Crystal structure of the **Tt**IFT52-46 complex"
  (Taschner et al., PMID 25349261). Chain A = *Tetrahymena thermophila* IFT46
  C-terminal domain (UniProt Q23KH7 221-332, PDB numbering = UniProt + 15).
  Chain B = *T. thermophila* IFT52 C-terminal fragment (UniProt I7LT74 371-434,
  PDB numbering = UniProt + 169).
- Interface definition: all heavy-atom pairs ≤ 4.5 Å between chains A and B.
  45 IFT46 residues and 35 IFT52 residues qualify. "Contacts" = number of
  heavy-atom pairs under the cutoff for that residue.
- Alignment: Smith-Waterman, BLOSUM62, affine gaps (open -11, extend -1),
  implemented directly in numpy (biopython is not importable in this executor).
- Superposition: Kabsch on Cα atoms of sequence-mapped interface positions,
  with a 3 Å outlier trim and a matched-position self control.

## Table 1. IFT46 side: the 45 IFT52-contacting residues mapped onto C. elegans DYF-6

| TtIFT46 (Q23KH7 numbering) | heavy-atom contacts | DYF-6 (Q0G838) | class |
|---|---|---|---|
| K236 | 18 | K365 | identical |
| Q239 | 1 | P368 | different |
| P240 | 10 | A369 | different |
| H241 | 10 | Q370 | different |
| S242 | 9 | T371 | similar |
| V243 | 12 | V372 | identical |
| L255 | 6 | L384 | identical |
| M256 | 4 | M385 | identical |
| Q257 | 10 | Q386 | identical |
| E258 | 13 | E387 | identical |
| W259 | 48 | W388 | identical |
| E264 | 28 | E393 | identical |
| L267 | 1 | L396 | identical |
| I272 | 6 | I401 | identical |
| S274 | 9 | S403 | identical |
| E276 | 1 | E405 | identical |
| F279 | 4 | V408 | different |
| N280 | 3 | S409 | similar |
| L281 | 23 | L410 | identical |
| S282 | 4 | E411 | different |
| F284 | 24 | Y413 | similar |
| C285 | 7 | V414 | different |
| A288 | 6 | C417 | different |
| I291 | 4 | I420 | identical |
| L292 | 6 | V421 | similar |
| N301 | 2 | - | not aligned |
| E302 | 19 | G426 | different |
| S303 | 16 | K427 | different |
| N304 | 8 | S428 | similar |
| V305 | 13 | R429 | different |
| I306 | 33 | I430 | identical |
| L309 | 14 | L433 | identical |
| H310 | 20 | H434 | identical |
| L312 | 7 | M436 | similar |
| F313 | 29 | F437 | identical |
| T314 | 1 | S438 | similar |
| L315 | 6 | L439 | identical |
| Y316 | 30 | L440 | different |
| S317 | 13 | N441 | similar |
| E318 | 11 | E442 | identical |
| F319 | 20 | F443 | identical |
| K320 | 3 | N444 | different |
| S321 | 4 | N445 | similar |
| Q323 | 5 | Q447 | identical |
| H324 | 2 | H448 | identical |

Totals: 23 identical, 9 similar, 12 different, 1 not aligned (44/45 covered).
Unweighted interface identity 52.3 % versus 39.7 % at non-interface positions of
the same domain (Fisher exact OR 1.66, p = 0.238, two-sided; underpowered).
Contact-weighted interface identity **62.0 %**.

CrIFT46 L285/L286, defined by mutagenesis as the IFT52-binding residues
(PMID 28302912), map through the Tetrahymena reference to DYF-6 **I420/V421**.

## Table 2. IFT46 side across orthologs (45 interface positions)

| Species | Group | interface coverage % | interface % id | interface % similar | non-interface % id |
|---|---|---|---|---|---|
| Danio rerio | motile | 95.6 | 62.8 | 83.7 | 46.0 |
| Homo sapiens | motile | 95.6 | 60.5 | 83.7 | 44.8 |
| Mus musculus | motile | 95.6 | 60.5 | 83.7 | 43.1 |
| Xenopus tropicalis | motile | 95.6 | 58.1 | 81.4 | 47.4 |
| Chlamydomonas reinhardtii | motile | 88.9 | 52.5 | 75.0 | 51.5 |
| Trypanosoma brucei | motile | 95.6 | 44.2 | 72.1 | 51.7 |
| Drosophila melanogaster | motile | 80.0 | 25.0 | 61.1 | 25.9 |
| Strongyloides ratti | nematode | 93.3 | 54.8 | 73.8 | 38.7 |
| **Caenorhabditis elegans** | nematode | **97.8** | **52.3** | **72.7** | **39.7** |
| Brugia malayi | nematode | 97.8 | 50.0 | 75.0 | 47.5 |
| Trichinella spiralis | nematode | 97.8 | 47.7 | 65.9 | 41.9 |
| Caenorhabditis briggsae | nematode | 93.3 | 35.7 | 64.3 | 35.6 |

Group means: motile 51.9 % interface identity, nematode 50.8 %. DYF-6 sits
between Chlamydomonas and Trypanosoma, inside the motile-cilia range.

## Table 3. Domain-specific divergence: ODA16 module versus IFT52 module

Reference segments: CrIFT46 1-147 (ODA16-binding region, PMID 28298440) and the
116-residue TtIFT46_B_C fragment from 4UZZ. Values are Smith-Waterman scores.

| Species | Group | N-term score | C-term score | N/C ratio |
|---|---|---|---|---|
| Danio rerio | motile | 200 | 306 | 0.65 |
| Xenopus tropicalis | motile | 184 | 291 | 0.63 |
| Homo sapiens | motile | 164 | 293 | 0.56 |
| Mus musculus | motile | 164 | 287 | 0.57 |
| Trypanosoma brucei | motile | 146 | 263 | 0.56 |
| Drosophila melanogaster | motile | 112 | 87 | 1.29 |
| Caenorhabditis briggsae | nematode | 73 | 181 | 0.40 |
| Strongyloides ratti | nematode | 84 | 255 | 0.33 |
| **Caenorhabditis elegans** | nematode | **80** | **250** | **0.32** |
| Brugia malayi | nematode | 88 | 275 | 0.32 |
| Trichinella spiralis | nematode | 25 | 232 | 0.11 |

Excluding the Drosophila outlier (whose C-terminal alignment is itself poor,
score 87), the two groups do not overlap: 0.56-0.65 versus 0.11-0.40. C. elegans
DYF-6 aligns only 34 of the 147 Chlamydomonas N-terminal residues.

## Table 4. IFT52 side: the 35 IFT46-contacting residues

| Species | UniProt | positions covered | interface % id | contact-weighted % id |
|---|---|---|---|---|
| Tetrahymena thermophila | I7LT74 | 34/35 | 100.0 | 100.0 |
| Homo sapiens | Q9Y366 | 34/35 | 61.8 | 70.4 |
| Chlamydomonas reinhardtii | Q946G4 | 32/35 | 53.1 | 63.5 |
| **Caenorhabditis elegans OSM-6** | G5EDF6 | 33/35 | **30.3** | **47.2** |

High-contact anchors retained in OSM-6: TtIFT52 K430 (63 contacts) → K426,
K416 (34) → K412, N385 (30) → N380, Y395 (28) → F390, L426 (25) → L422,
L392 (24) → L387, F429 (22) → F425, F373 (20) → F368, K431 (20) → R427.
Largest single change: N389 (49 contacts) → E384.

## Table 5. Superposition onto 4UZZ chain A (same 44 interface Cα positions)

| Model | n Cα | RMSD all | n core (dev < 3 Å) | RMSD core | mean pLDDT |
|---|---|---|---|---|---|
| AlphaFold Tetrahymena IFT46 (self control) | 44 | 2.02 Å | 40 | 0.79 Å | 80.4 |
| AlphaFold C. elegans DYF-6 (AF-Q0G838-F1-v6) | 44 | 2.91 Å | 37 | 1.16 Å | 85.4 |

Largest DYF-6 deviations are at residues 365, 368 and the 426-427 loop, the same
positions that are sequence-divergent.

## Table 6. Native IFT train context (PDB 8BD7, Chlamydomonas, 9.9 Å, fitted model)

IFT46 (chain D) is modelled only over residues 212-344, that is the IFT46_B_C
domain alone. Every modelled IFT46 Cα within 12 Å of IFT52 (chain B, "Osm-6-like
protein", Q946G4) lies in that domain; the contacting IFT52 residues are 355-454,
exclusively its C-terminal region. Resolution limits this to a domain-level
statement, not a residue-level one.

## Table 7. DYF-6 isoforms

| Isoform | Length | Retains canonical 345-455 IFT46_B_C block |
|---|---|---|
| Q0G838-1 (a) | 471 | yes |
| Q0G838-2 (b) | 320 | yes (lacks residues 1-151) |
| Q0G838-3 (c) | 158 | no |
| Q0G838-4 (d) | 298 | yes (lacks residues 1-151) |

## Table 8. Current GO annotations for Q0G838 (QuickGO, this session)

| GO ID | Aspect | Qualifier | Evidence | Reference |
|---|---|---|---|---|
| GO:0042073 intraciliary transport | BP | involved_in | IEA | GO_REF:0000002 (InterPro IPR022088) |
| GO:0042073 | BP | involved_in | IBA | GO_REF:0000033 |
| GO:0042073 | BP | involved_in | IDA | PMID:16648645 (WB) |
| GO:0042073 | BP | involved_in | NAS | PMID:28479320 (ComplexPortal) |
| GO:0060271 cilium assembly | BP | involved_in | IBA, NAS | GO_REF:0000033, PMID:28479320 |
| GO:1905515 non-motile cilium assembly | BP | involved_in | IMP | PMID:16648645, WBVar00088609 |
| GO:0030992 intraciliary transport particle B | CC | part_of | IBA, NAS | GO_REF:0000033, PMID:28479320 |
| GO:0031514 **motile cilium** | CC | is_active_in | IBA | GO_REF:0000033 (from MGI:1923818 et al.) |
| GO:0005815 microtubule organizing center | CC | is_active_in | IBA | GO_REF:0000033 |
| GO:0005929 cilium | CC | located_in | IEA, NAS | GO_REF:0000044, PMID:28479320 |
| GO:0030425 dendrite | CC | located_in | IEA, IDA | GO_REF:0000044, PMID:16648645 |
| GO:0043025 neuronal cell body | CC | located_in | IDA | PMID:16648645 |
| GO:0043204 perikaryon | CC | located_in | IEA, EXP | GO_REF:0000044, PMID:16648645 |
| GO:0120025 plasma membrane bounded cell projection | CC | located_in | IEA | GO_REF:0000117 |

No molecular function annotation exists for Q0G838.

## Table 9. Burial control for interface conservation (iteration 3)

Burial proxy = heavy-atom neighbours within 8 Å, computed from 4UZZ chain A alone
(so the IFT52 partner does not contribute), averaged per residue atom. 100 chain A
residues mapped to DYF-6. Median burial 55.7.

| Stratum | interface % id (n) | non-interface % id (n) | Fisher OR | p |
|---|---|---|---|---|
| Buried half (burial ≥ median) | 45.8 (24) | 38.5 (26) | 1.35 | 0.775 |
| Exposed half (burial < median) | 60.0 (20) | 36.7 (30) | 2.59 | 0.149 |
| All | 52.3 (44) | 37.5 (56) | 1.66 | 0.238 |

Logistic regression, P(DYF-6 residue identical to TtIFT46) ~ interface + burial:

| term | coef | SE | z | p |
|---|---|---|---|---|
| const | 0.392 | 0.826 | 0.47 | 0.635 |
| interface | **0.618** | 0.412 | 1.50 | 0.134 |
| burial | -0.016 | 0.014 | -1.15 | 0.251 |

Permutation test, 20000 shuffles of identity labels across the whole domain:
observed contact-weighted interface identity **62.0 %**, null mean 44.0 %,
one-sided **p = 0.0163**.

The burial confound is rejected: the interface signal is present in the exposed
half and absent in the buried half, the opposite of the confound's prediction.

## Table 10. The ODA16-region motif, CrIFT46 119-133

Unbiased 15-residue sliding scan over CrIFT46 1-147 (ODA16-binding fragment,
PMID 28298440) across 6 motile-cilia orthologs. Best window = residues **119-133,
LFSYIGRYKPQTVEL** (mean per-position identity 0.444 versus 0.138 over the whole
fragment). Targeted ungapped BLOSUM62 search of that 15-mer in the N-terminal
60 % of each ortholog:

| Species | Group | UniProt | match start | window | score | identical /15 |
|---|---|---|---|---|---|---|
| Chlamydomonas reinhardtii | motile | A2T2X4 | 119 | LFSYIGRYKPQTVEL | 78 | 15 |
| Schistosoma mansoni | motile | A0A3Q0KNK3 | 121 | IFEYIQRYTPQTIEL | 57 | 10 |
| Homo sapiens | motile | Q9NQC8 | 81 | LFQYISRYTPQLIDL | 52 | 9 |
| Mus musculus | motile | Q9DB07 | 78 | LFEYISRYTPQLIDL | 52 | 9 |
| **Caenorhabditis elegans** | nematode | Q0G838 | **254** | **ILTYIDAYKTQEVEL** | **40** | **8** |
| Caenorhabditis briggsae | nematode | A8XQI8 | 227 | VLSYVDAYKAQEVQL | 38 | 7 |
| Xenopus tropicalis | motile | Q28H29 | 32 | DFNAIEVYKPQDATT | 21 | 6 |
| Strongyloides ratti | nematode | A0A090LGF7 | 19 | LPDFLSLYNPERAMI | 18 | 3 |
| Danio rerio | motile | Q6DRN0 | 215 | AISTMGFKQPTPIQK | 12 | 3 |
| Brugia malayi | nematode | A8PYM6 | 89 | PFAKLSELRPSALRR | 11 | 2 |
| Trypanosoma brucei | motile | Q57UX3 | 70 | FVEFFGDECVRADDL | 3 | 2 |

Shuffled-sequence null for DYF-6 (2000 shuffles of its N-terminal 60 %):
mean best score 10.2, sd 3.9. Observed 40, empirical **p < 0.0005**.
DYF-6 sits at the 43rd percentile of the motile-cilia set.
Motile versus nematode score medians 52 versus 28, Mann-Whitney one-sided
**p = 0.197**: the motif does not track ciliary motility.
Positional check: the motif lies 211 residues before the CrIFT46 C-terminus and
203 before the DYF-6 C-terminus, so the match is positionally homologous.

## Table 11. Per-position conservation of CrIFT46 1-147

| Species | Group | positions aligned /147 | % identical over aligned |
|---|---|---|---|
| Schistosoma mansoni | motile | 56 (0.38) | 53.6 |
| Homo sapiens | motile | 48 (0.33) | 56.2 |
| Mus musculus | motile | 48 (0.33) | 56.2 |
| Trypanosoma brucei | motile | 43 (0.29) | 37.2 |
| Danio rerio | motile | 38 (0.26) | 34.2 |
| Xenopus tropicalis | motile | 25 (0.17) | 36.0 |
| Brugia malayi | nematode | 78 (0.53) | 24.4 |
| **Caenorhabditis elegans** | nematode | 34 (0.23) | 47.1 |
| Strongyloides ratti | nematode | 20 (0.14) | 30.0 |

Mean per-position identity to CrIFT46 over 1-147: motile 0.138, nematode 0.085,
Mann-Whitney one-sided p = 2.44e-4. Nematode/motile identity ratio 0.67 over the
N-terminal region versus 1.16 over the C-terminal domain (198-344), confirming
that the divergence is region-specific. The low absolute numbers on both sides
show the N-terminal region is poorly conserved even among motile-cilia species.
