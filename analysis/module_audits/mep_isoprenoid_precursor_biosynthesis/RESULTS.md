# PAINT node placement for the MEP isoprenoid precursor module families

Generated 2026-11-13 by `paint_node_placement.py` (this folder, copied from the
RecBCD module audit) for the `modules/mep_isoprenoid_precursor_biosynthesis.yaml`
audit. The script downloads the PANTHER 19 `treeinfo` tree for each family (the
payload is not retained) and, for every PTN node in the committed
`interpro/panther/<FAM>/<FAM>-paint.tsv`, reports whether the node is in that
family's tree, its type, taxonomic range, leaf count and the subfamilies beneath
it, plus the annotated ancestors of selected target proteins. Reproduce with:

```
python -I paint_node_placement.py PTHR43322 PTHR30525 PTHR32125 PTHR43527 PTHR43181 PTHR30454 PTHR30426 \
  --targets P77488 P45568 Q46893 P62615 P62617 P62620 P62623 F4K0E8 Q38854 Q9XFS9 P69834 O81014 Q9CAK8 P54482 Q9XDM4 P54523 Q88QG7 \
  --show-sf PTHR43322:SF4 PTHR32125:SF8 PTHR43527:SF1
```

The P. putida KT2440 accessions are not leaves of the PANTHER 19 trees, so no
target line is printed for them; they inherit by classification.

PTHR37850 (the DRL family) is not part of this run: it has no reviewed UniProt
members, so `just fetch-panther-family` writes no member list and
`just fetch-panther-paint` cannot slice it, and the GOA file for its exemplar
(Brucella abortus BAB2_0264, Q2YIM3) carries no IBA rows.

## Raw output

## PTHR43322

- root node: PTN000179225 (taxonomic_range LUCA); leaves: 207

| node | in tree | type | event | taxonomic range | leaves | subfamilies (leaf count) | terms |
|---|---|---|---|---|---|---|---|
| PTN000179225 | yes | ROOT | SPECIATION | LUCA | 207 | PTHR43322:SF5 (91); PTHR43322:SF4 (46); PTHR43322:SF3 (34); PTHR43322:SF6 (23); PTHR43322:SF7 (4); PTHR43322:SF8 (4); PTHR43322:SF9 (3); PTHR43322:SF1 (2) | GO:0016744 |
| PTN000179234 | yes | INTERNAL | SPECIATION | Magnoliophyta | 55 | PTHR43322:SF5 (48); PTHR43322:SF8 (4); PTHR43322:SF9 (3) | GO:0009507,GO:0015995 |
| PTN000179250 | yes | INTERNAL | DUPLICATION | Eubacteria | 33 | PTHR43322:SF5 (31); PTHR43322:SF1 (2) | GO:0005829,GO:0008661,GO:0019288 |

- target P77488 (dxs, Escherichia coli, PTHR43322:SF5): annotated ancestors PTN000179225, PTN000179250
- target Q38854 (DXS, Arabidopsis thaliana, PTHR43322:SF5): annotated ancestors PTN000179225, PTN000179234
- target P54523 (dxs, Bacillus subtilis, PTHR43322:SF5): annotated ancestors PTN000179225, PTN000179250

- leaves of PTHR43322:SF4: W1PBG9 AMTR_s00019p00192810 (Amborella trichopoda); U5CWM1 AMTR_s00033p00220630 (Amborella trichopoda); A0A804J4K1 None (Musa acuminata subsp. malaccensis); A0A804IR08 None (Musa acuminata subsp. malaccensis); A0A804J906 103986006 (Musa acuminata subsp. malaccensis); K3ZR37 101761672 (Setaria italica); A0A1W0W2N7 SORBI_3002G064700 (Sorghum bicolor); C5XBX3 SORBI_3002G064500 (Sorghum bicolor); A0A1D6HUR1 606430 (Zea mays); Q6YU51 Os07g0190000 (Oryza sativa); I1H2X1 100821434 (Brachypodium distachyon); A0A287GK35 None (Hordeum vulgare subsp. vulgare); A0A3B5Z542 CFC21_008837 (Triticum aestivum); A0A3B6A0I1 CFC21_013658 (Triticum aestivum); A0A3B5Y5R6 None (Triticum aestivum); A0A9R0J1M7 LOC110798177 (Spinacia oleracea); A0A251T274 DXS2 (Helianthus annuus); A0A9R1W0I7 LSAT_V11C300126150 (Lactuca sativa); A0A022QQE8 MIMGU_mgv1a002082mg (Erythranthe guttata); A0A2G2Y552 T459_29300 (Capsicum annuum); M1BBK8 102598525 (Solanum tuberosum); A0A3Q7IS63 101251053 (Solanum lycopersicum); A0A1S3Y7Y6 LOC107773391 (Nicotiana tabacum); D7UDN7 VIT_00s0218g00110 (Vitis vinifera); A0A059ALI3 EUGRSUZ_I00566 (Eucalyptus grandis); A0A1U8NAH5 LOC107945427 (Gossypium hirsutum); A0A1U8PTU0 LOC107962064 (Gossypium hirsutum); A0A061DHE8 TCM_000965 (Theobroma cacao); A0A061DJ11 TCM_000964 (Theobroma cacao); A0A067EZF3 CISIN_1g003948mg (Citrus sinensis); A0A2K1ZPY4 POPTR_007G058500 (Populus trichocarpa); A0A2C9UQB5 MANES_13G101600 (Manihot esculenta); A0A2C9UW20 MANES_12G124300 (Manihot esculenta); B9T2B5 RCOM_0410350 (Ricinus communis); I1KX60 100798930 (Glycine max); I1N1T9 100814637 (Glycine max); A0A0R0IAU8 100799481 (Glycine max); K7L9B1 100799983 (Glycine max); A7DY38 dxs2-2 (Medicago truncatula); Q8L692 dxs2 (Medicago truncatula); A0A2I4DSD7 LOC108983005 (Juglans regia); A0A0A0L869 Csa_3G114510 (Cucumis sativus); A0A251NT99 PRUPE_6G204700 (Prunus persica); D8T0X7 SELMODRAFT_427859 (Selaginella moellendorffii); D8R481 DXS (Selaginella moellendorffii); A0A2R6WNW2 MARPO_0070s0009 (Marchantia polymorpha)

## PTHR30525

- root node: PTN000776155 (taxonomic_range LUCA); leaves: 102

| node | in tree | type | event | taxonomic range | leaves | subfamilies (leaf count) | terms |
|---|---|---|---|---|---|---|---|
| PTN000776155 | yes | ROOT | SPECIATION | LUCA | 102 | PTHR30525:SF0 (98); PTHR30525:SF7 (2); PTHR30525:SF6 (2) | GO:0030604 |
| PTN000776172 | yes | INTERNAL | SPECIATION | Proteobacteria | 12 | PTHR30525:SF0 (12) | GO:1990065 |

- target P45568 (dxr, Escherichia coli, PTHR30525:SF0): annotated ancestors PTN000776155, PTN000776172
- target Q9XFS9 (DXR, Arabidopsis thaliana, PTHR30525:SF0): annotated ancestors PTN000776155


## PTHR32125

- root node: PTN000781812 (taxonomic_range LUCA); leaves: 84

| node | in tree | type | event | taxonomic range | leaves | subfamilies (leaf count) | terms |
|---|---|---|---|---|---|---|---|
| PTN000440569 | no | | | | | | GO:0005829,GO:0070567 |
| PTN000781812 | yes | ROOT | SPECIATION | LUCA | 84 | PTHR32125:SF4 (80); PTHR32125:SF8 (4) | GO:0050518 |

- target Q46893 (ispD, Escherichia coli, PTHR32125:SF4): annotated ancestors PTN000781812
- target P69834 (ISPD, Arabidopsis thaliana, PTHR32125:SF4): annotated ancestors PTN000781812

- leaves of PTHR32125:SF8: Q8DPI2 tarI (Streptococcus pneumoniae); Q2G1C0 tarI (Staphylococcus aureus); Q2G2C4 tarI' (Staphylococcus aureus); Q8Y832 tarI (Listeria monocytogenes)

## PTHR43527

- root node: PTN000466527 (taxonomic_range LUCA); leaves: 88

| node | in tree | type | event | taxonomic range | leaves | subfamilies (leaf count) | terms |
|---|---|---|---|---|---|---|---|
| PTN000466527 | yes | ROOT | SPECIATION | LUCA | 88 | PTHR43527:SF2 (84); PTHR43527:SF1 (4) | GO:0050515 |
| PTN002882405 | yes | INTERNAL | SPECIATION | Firmicutes | 3 | PTHR43527:SF1 (3) | GO:0050515 |

- target P62615 (ispE, Escherichia coli, PTHR43527:SF2): annotated ancestors PTN000466527
- target O81014 (ISPE, Arabidopsis thaliana, PTHR43527:SF2): annotated ancestors PTN000466527
- target Q9XDM4 (pduX, Salmonella typhimurium, PTHR43527:SF1): annotated ancestors PTN000466527, PTN002882405

- leaves of PTHR43527:SF1: Q9EX47 SCO0991 (Streptomyces coelicolor); A5I0E6 pduX (Clostridium botulinum); Q9XDM4 pduX (Salmonella typhimurium); Q8Y7U9 lmo1170 (Listeria monocytogenes)

## PTHR43181

- root node: PTN000781796 (taxonomic_range LUCA); leaves: 83

| node | in tree | type | event | taxonomic range | leaves | subfamilies (leaf count) | terms |
|---|---|---|---|---|---|---|---|
| PTN000781796 | yes | ROOT | SPECIATION | LUCA | 83 | PTHR43181:SF1 (79); PTHR43181:SF3 (4) | GO:0008685,GO:0016114 |
| PTN001281128 | yes | INTERNAL | SPECIATION | Viridiplantae | 50 | PTHR43181:SF1 (46); PTHR43181:SF3 (4) | GO:0015995,GO:0016117 |

- target P62617 (ispF, Escherichia coli, PTHR43181:SF1): annotated ancestors PTN000781796
- target Q9CAK8 (ISPF, Arabidopsis thaliana, PTHR43181:SF1): annotated ancestors PTN000781796, PTN001281128


## PTHR30454

- root node: PTN000765215 (taxonomic_range Eubacteria); leaves: 86

| node | in tree | type | event | taxonomic range | leaves | subfamilies (leaf count) | terms |
|---|---|---|---|---|---|---|---|
| PTN000765210 | yes | INTERNAL | SPECIATION | Viridiplantae | 53 | PTHR30454:SF0 (53) | GO:0009507 |
| PTN000765215 | yes | ROOT | SPECIATION | Eubacteria | 86 | PTHR30454:SF0 (86) | GO:0046429,GO:0019288 |
| PTN000765227 | yes | INTERNAL | SPECIATION | Proteobacteria | 12 | PTHR30454:SF0 (12) | GO:0005829 |

- target P62620 (ispG, Escherichia coli, PTHR30454:SF0): annotated ancestors PTN000765215, PTN000765227
- target F4K0E8 (ISPG, Arabidopsis thaliana, PTHR30454:SF0): annotated ancestors PTN000765215, PTN000765210
- target P54482 (ispG, Bacillus subtilis, PTHR30454:SF0): annotated ancestors PTN000765215


## PTHR30426

- root node: PTN000764787 (taxonomic_range LUCA); leaves: 31

| node | in tree | type | event | taxonomic range | leaves | subfamilies (leaf count) | terms |
|---|---|---|---|---|---|---|---|
| PTN000764789 | yes | INTERNAL | SPECIATION | Eubacteria | 29 | PTHR30426:SF0 (29) | GO:0005829,GO:0051745,GO:0019288 |

- target P62623 (ispH, Escherichia coli, PTHR30426:SF0): annotated ancestors PTN000764789
