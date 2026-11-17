# PAINT node placement for the RecBCD module families

Generated 2026-11-09 by `paint_node_placement.py` (this folder) for the
`modules/bacterial_recbcd_end_resection.yaml` audit. The script downloads the
PANTHER 19 `treeinfo` tree for each family (the payload is not retained), and for
every PTN node in the committed `interpro/panther/<FAM>/<FAM>-paint.tsv` reports
whether the node is in that family's tree, its type, taxonomic range, leaf count
and the subfamilies beneath it. Reproduce with:

```
python -I paint_node_placement.py PTHR11070 PTHR30591 PTHR43788 \
  --targets P08394 Q88DZ5 P07648 Q88DZ4 P04993 Q88DZ6 P03018 P09980 Q9RT63 O34481 P23478 Q8NG08 P9WMQ1 P15038 F1ND48 \
  --show-sf PTHR11070:SF23 PTHR11070:SF48 PTHR11070:SF49 PTHR30591:SF1 PTHR43788:SF6
```

The P. putida KT2440 accessions (Q88DZ4-Q88DZ6) are not leaves of the PANTHER 19
trees, so no target line is printed for them; they inherit by classification.

## Raw output

## PTHR11070

- root node: PTN008960327 (taxonomic_range None); leaves: 248

| node | in tree | type | event | taxonomic range | leaves | subfamilies (leaf count) | terms |
|---|---|---|---|---|---|---|---|
| PTN000116141 | yes | INTERNAL | SPECIATION | LUCA | 245 | PTHR11070:SF2 (97); PTHR11070:SF61 (45); PTHR11070:SF30 (28); PTHR11070:SF23 (14); PTHR11070:SF64 (11); PTHR11070:SF45 (7); PTHR11070:SF3 (7); PTHR11070:SF17 (6); PTHR11070:SF63 (6); PTHR11070:SF48 (6); PTHR11070:SF46 (3); PTHR11070:SF67 (3); PTHR11070:SF66 (2); PTHR11070:SF69 (2); PTHR11070:SF59 (2); PTHR11070:SF55 (2); PTHR11070:SF49 (2); PTHR11070:SF50 (2) | GO:0043138,GO:0000725 |
| PTN000116143 | yes | INTERNAL | SPECIATION | Eukaryota | 117 | PTHR11070:SF61 (45); PTHR11070:SF2 (39); PTHR11070:SF30 (28); PTHR11070:SF46 (3); PTHR11070:SF66 (2) | GO:0005634 |
| PTN000116196 | yes | INTERNAL | SPECIATION | Eubacteria | 70 | PTHR11070:SF2 (54); PTHR11070:SF48 (6); PTHR11070:SF69 (2); PTHR11070:SF59 (2); PTHR11070:SF55 (2); PTHR11070:SF49 (2); PTHR11070:SF50 (2) | GO:0033202 |
| PTN000116249 | yes | INTERNAL | SPECIATION | Eubacteria | 14 | PTHR11070:SF23 (14) | GO:0009338 |
| PTN000116269 | yes | INTERNAL | SPECIATION | Opisthokonts | 28 | PTHR11070:SF30 (28) | GO:0000724,GO:0031297 |
| PTN000869814 | yes | INTERNAL | DUPLICATION | Eubacteria | 124 | PTHR11070:SF2 (54); PTHR11070:SF23 (14); PTHR11070:SF64 (11); PTHR11070:SF45 (7); PTHR11070:SF3 (7); PTHR11070:SF17 (6); PTHR11070:SF63 (6); PTHR11070:SF48 (6); PTHR11070:SF67 (3); PTHR11070:SF69 (2); PTHR11070:SF59 (2); PTHR11070:SF55 (2); PTHR11070:SF49 (2); PTHR11070:SF50 (2) | GO:0005829 |

- target P08394 (recB, Escherichia coli, PTHR11070:SF23): annotated ancestors PTN000116141, PTN000869814, PTN000116249
- target P03018 (uvrD, Escherichia coli, PTHR11070:SF2): annotated ancestors PTN000116141, PTN000869814, PTN000116196
- target P09980 (rep, Escherichia coli, PTHR11070:SF64): annotated ancestors PTN000116141, PTN000869814
- target P23478 (addA, Bacillus subtilis, PTHR11070:SF48): annotated ancestors PTN000116141, PTN000869814, PTN000116196
- target P9WMQ1 (uvrD1, Mycobacterium tuberculosis, PTHR11070:SF2): annotated ancestors PTN000116141, PTN000869814, PTN000116196
- target P15038 (helD, Escherichia coli, PTHR11070:SF63): annotated ancestors PTN000116141, PTN000869814
- target F1ND48 (FBH1, Gallus gallus, PTHR11070:SF30): annotated ancestors PTN000116141, PTN000116143, PTN000116269

- leaves of PTHR11070:SF23: P9WMQ3 recB (Mycobacterium tuberculosis); Q8F7H9 LA_0966 (Leptospira interrogans); O84645 recB (Chlamydia trachomatis); Q9K037 recB (Neisseria meningitidis serogroup b); Q74CY7 recB (Geobacter sulfurreducens); Q89BR0 blr8088 (Bradyrhizobium diazoefficiens); P45157 recB (Haemophilus influenzae); Q8EF45 recB (Shewanella oneidensis); Q9KPP6 recB (Vibrio cholerae); Q8P379 recB (Xanthomonas campestris); Q9HWB6 recB (Pseudomonas aeruginosa); Q8ZMB6 recB (Salmonella typhimurium); A0A3N4BT68 recB (Yersinia pestis); P08394 recB (Escherichia coli)
- leaves of PTHR11070:SF48: A5HYY0 addA (Clostridium botulinum); Q8DPR6 addA (Streptococcus pneumoniae); Q2FZT5 addA (Staphylococcus aureus); Q8Y511 addA (Listeria monocytogenes); P23478 addA (Bacillus subtilis); Q81GP9 addA (Bacillus cereus)
- leaves of PTHR11070:SF49: Q2FZT6 addB (Staphylococcus aureus); Q8Y510 addB (Listeria monocytogenes)

## PTHR30591

- root node: PTN001255136 (taxonomic_range Eubacteria); leaves: 17

| node | in tree | type | event | taxonomic range | leaves | subfamilies (leaf count) | terms |
|---|---|---|---|---|---|---|---|
| PTN000116141 | no | | | | | | GO:0043138,GO:0000725 |
| PTN000116196 | no | | | | | | GO:0033202 |
| PTN000869814 | no | | | | | | GO:0005829 |
| PTN001255136 | yes | ROOT | SPECIATION | Eubacteria | 17 | PTHR30591:SF1 (17) | GO:0006310 |

- target P07648 (recC, Escherichia coli, PTHR30591:SF1): annotated ancestors PTN001255136

- leaves of PTHR30591:SF1: P9WIQ5 recC (Mycobacterium tuberculosis); A5HYX0 addB (Clostridium botulinum); Q8DPR7 rexB (Streptococcus pneumoniae); P23477 addB (Bacillus subtilis); Q81GQ0 addB (Bacillus cereus); Q8F7I0 LA_0965 (Leptospira interrogans); O84646 recC (Chlamydia trachomatis); Q9JY62 recC (Neisseria meningitidis serogroup b); Q74CY8 recC (Geobacter sulfurreducens); P44945 recC (Haemophilus influenzae); Q8EF44 recC (Shewanella oneidensis); Q9KPP4 recC (Vibrio cholerae); Q8P378 recC (Xanthomonas campestris); Q9HWB5 recC (Pseudomonas aeruginosa); Q8ZMB4 recC (Salmonella typhimurium); A0A3N4B3Y5 recC (Yersinia pestis); P07648 recC (Escherichia coli)

## PTHR43788

- root node: PTN002465241 (taxonomic_range LUCA); leaves: 271

| node | in tree | type | event | taxonomic range | leaves | subfamilies (leaf count) | terms |
|---|---|---|---|---|---|---|---|
| PTN000094675 | no | | | | | | GO:0005737,GO:0017108,GO:0071932 |
| PTN000094957 | no | | | | | | GO:0005829,GO:0043186,GO:0035194 |
| PTN000095131 | yes | INTERNAL | SPECIATION | Bilateria | 27 | PTHR43788:SF8 (27) | GO:0005634,GO:0005737 |
| PTN000095219 | yes | INTERNAL | SPECIATION | Eubacteria | 26 | PTHR43788:SF6 (26) | GO:0009338,GO:0006310 |
| PTN002248233 | no | | | | | | GO:0001147,GO:0006369 |
| PTN002465241 | yes | ROOT | DUPLICATION | LUCA | 271 | PTHR43788:SF8 (118); PTHR43788:SF6 (51); PTHR43788:SF3 (43); PTHR43788:SF16 (41); PTHR43788:SF17 (9); PTHR43788:SF9 (3); PTHR43788:SF10 (2); PTHR43788:SF13 (2); PTHR43788:SF18 (2) | GO:0043139,GO:0006974 |
| PTN008452915 | yes | INTERNAL | SPECIATION | LUCA | 51 | PTHR43788:SF6 (51) | GO:0017116,GO:0006261,GO:1903775,GO:2000042 |
| PTN008507816 | no | | | | | | GO:0003723 |

- target P04993 (recD, Escherichia coli, PTHR43788:SF6): annotated ancestors PTN002465241, PTN008452915, PTN000095219
- target Q9RT63 (recD2, Deinococcus radiodurans, PTHR43788:SF6): annotated ancestors PTN002465241, PTN008452915, PTN000095219
- target O34481 (yrrC, Bacillus subtilis, PTHR43788:SF6): annotated ancestors PTN002465241, PTN008452915, PTN000095219
- target Q8NG08 (HELB, Homo sapiens, PTHR43788:SF6): annotated ancestors PTN002465241, PTN008452915

- leaves of PTHR43788:SF6: Q8NG08 HELB (Homo sapiens); A0A2J8K075 HELB (Pan troglodytes); G3RJF6 HELB (Gorilla gorilla gorilla); F6TPE9 HELB (Macaca mulatta); Q6NVF4 Helb (Mus musculus); G3MYV2 HELB (Bos taurus); A0A287AAH7 HELB (Sus scrofa); F7BTU9 HELB (Equus caballus); A0A2I2UTW7 HELB (Felis catus); A0A8I3NCM6 HELB (Canis lupus familiaris); F6PRP3 HELB (Ornithorhynchus anatinus); A0A8V0YG75 HELB (Gallus gallus); H9G7R3 HELB (Anolis carolinensis); A0A1L8GYH3 helb.L (Xenopus laevis); F6WN51 helb (Xenopus tropicalis); B0UYS3 helb (Danio rerio); W5NH11 None (lepisosteus oculatus); A0A9J7LP36 LOC118422829 (Branchiostoma floridae); A0A7M7NZW1 None (Strongylocentrotus purpuratus); A0A7M7TH98 None (Strongylocentrotus purpuratus); A0A7M7PFJ1 None (Strongylocentrotus purpuratus); A9VCH2 MONBRDRAFT_34547 (Monosiga brevicollis); B9TCW0 RCOM_1823800 (Ricinus communis); A0A1Y1HUL8 KFL_001080010 (Klebsormidium nitens); Q58914 MJ1519 (Methanocaldococcus jannaschii); A9WGW5 recD2 (Chloroflexus aurantiacus); Q9AD96 SCO1671 (Streptomyces coelicolor); Q9RDI9 recD2 (Streptomyces coelicolor); P9WHJ1 recD (Mycobacterium tuberculosis); A5HY63 recD2 (Clostridium botulinum); Q8DR28 recD (Streptococcus pneumoniae); Q2FXV8 recD2 (Staphylococcus aureus); Q8Y717 recD2 (Listeria monocytogenes); O34481 yrrC (Bacillus subtilis); Q817Y5 recD2 (Bacillus cereus); Q9RT63 recD2 (Deinococcus radiodurans); Q7NMY6 recD2 (Gloeobacter violaceus); Q6ZE92 sll7106 (Synechocystis); Q8F7H8 LA_0967 (Leptospira interrogans); O84658 recD_2 (Chlamydia trachomatis); O84036 recD_1 (Chlamydia trachomatis); Q9JZ93 recD (Neisseria meningitidis serogroup b); Q74CY6 recD (Geobacter sulfurreducens); Q89MC7 bll4266 (Bradyrhizobium diazoefficiens); Q8EF46 recD (Shewanella oneidensis); Q9KPP7 recD (Vibrio cholerae); Q8P380 recD (Xanthomonas campestris); Q9HWB7 recD (Pseudomonas aeruginosa); Q8ZMB7 recD (Salmonella typhimurium); A0A2U2H3L4 recD (Yersinia pestis); P04993 recD (Escherichia coli)


## Interpretation

1. PTHR30591 PAINT slice contains three nodes from another tree. PTN000116141,
   PTN000116196 and PTN000869814 are not in the PTHR30591 tree. They are nodes of
   the PTHR11070 tree, where the Staphylococcus aureus and Listeria monocytogenes
   AddB leaves (Q2FZT6, Q8Y510) sit in PTHR11070:SF49. Current classification puts
   those same accessions in PTHR30591:SF1, so the per-family slice picks up their
   PTHR11070 ancestors. These rows are a classification artefact of the slice, not
   annotations placed in the RecC/AddB tree.
2. The only node inside the PTHR30591 tree is its root, PTN001255136 (Eubacteria),
   whose 17 leaves mix RecC proteins with AddB/RexB proteins in the single
   subfamily PTHR30591:SF1. PTHR30591:SF1 is therefore not a RecC-specific selector.
3. In PTHR11070, PTN000116249 (exodeoxyribonuclease V complex) covers exactly the
   14 RecB leaves of PTHR11070:SF23, and E. coli RecB descends from PTN000116141,
   PTN000869814 and PTN000116249 only.
4. In PTHR43788, PTN008452915 is a LUCA speciation node holding only
   PTHR43788:SF6 (51 leaves): bacterial RecD, standalone RecD2, archaeal and
   eukaryotic HELB proteins. E. coli RecD, D. radiodurans RecD2 and B. subtilis
   YrrC/RecD2 all descend from PTN000095219, the Eubacteria node carrying
   exodeoxyribonuclease V complex, so that complex term also reaches standalone
   RecD2 proteins that are not RecBCD subunits.
5. Human HELB (Q8NG08) descends from PTN002465241 and PTN008452915 but not from
   PTN000095219.
