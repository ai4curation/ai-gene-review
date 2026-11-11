# TGFBR3 re-review: site mapping and juxtamembrane segment check

Human Q03167 (851 aa) vs donkey A0A8C4M6Z6 (836 aa); global alignment, BLOSUM62, gap open -10, extend -0.5.

## Human point/region features mapped to donkey

- TOPO_DOM Extracellular: human [21, 787] -> donkey [21, 772]; 667/767 identical, 752 paired
- TOPO_DOM Cytoplasmic: human [810, 851] -> donkey [795, 836]; 42/42 identical, 42 paired
- REGION Interaction with TGF-beta ligand: human [737, 751] -> donkey [736, 750]; 14/15 identical, 15 paired
- MOD_RES Phosphothreonine: human T840 -> donkey T825
- CARBOHYD N-linked (GlcNAc...) asparagine: human N141 -> donkey N141
- CARBOHYD N-linked (GlcNAc...) asparagine: human N492 -> donkey N491
- CARBOHYD O-linked (Xyl...) (glycosaminoglycan) serine: human S534 -> donkey S533
- CARBOHYD O-linked (Xyl...) (glycosaminoglycan) serine: human S545 -> donkey S544
- CARBOHYD N-linked (GlcNAc...) asparagine: human N571 -> donkey N570
- CARBOHYD N-linked (GlcNAc...) asparagine: human N590 -> donkey N589
- CARBOHYD N-linked (GlcNAc...) asparagine: human N697 -> donkey N696

## Human 755-790 window in each sequence (aligned to human)

- human Q03167: IHHEAESKEKGPSMKEPNPISPPIFHGLDTLTVMGI
- donkey A0A8C4M6Z6 (836 aa): IHHQVESK--------------AIFHGLDTLTVMGI; human residues without partner: 15 (first 359, last 776)
- sp|O88393|TGBR3_MOUSE (850 aa): V-LQVDYKENVPNMKESSPVPPPIFHGLDTLTVMGI; human residues without partner: 5 (first 359, last 756)
- sp|P26342|TGBR3_RAT (853 aa): V-LQVDYKENVPSTKDSSPIPPPIFHGLDTLTVMGI; human residues without partner: 4 (first 359, last 756)
- sp|P35054|TGBR3_PIG (848 aa): IHHEVQF--KGPSTKESNPISPPIFHGLDTLTVMGI; human residues without partner: 3 (first 359, last 763)
- tr|F7E1V2|F7E1V2_HORSE (809 aa): IHHQVES--KGPSIKEPSPISPPIFHGLDTLTVMGI; human residues without partner: 45 (first 2, last 763)
- tr|A0A8I3NZI6|A0A8I3NZI6_CANLF (851 aa): IHQEAEGKETGPSFKEPNPISPPVFHGLDTLTVMGI; human residues without partner: 0
- tr|Q90998|Q90998_CHICK (841 aa): TH---EGKPEDSSLPKSNVRQPSVFYGLDTLTVVGI; human residues without partner: 21 (first 357, last 759)

## C-terminal cytoplasmic tail (last 15 residues)

- human: IGSTQSTPCSSSSTA
- donkey: IGSTQSTPCSSSSTA
- sp|O88393|TGBR3_MOUSE: IGSTQSTPCSSSSTA
- sp|P26342|TGBR3_RAT: IGSTQSTPCSSSSTA
- sp|P35054|TGBR3_PIG: LGSTQSTPCSSSSAA
- tr|F7E1V2|F7E1V2_HORSE: IGSTQSTPCSSSSTA
- tr|A0A8I3NZI6|A0A8I3NZI6_CANLF: IGSTQSTPCSSSSAA
- tr|Q90998|Q90998_CHICK: IGSTQSTPCSSSSAT

Interpretation is left to the review; pairwise alignment does not by itself establish orthology
(orthology here rests on PANTHER subfamily PTHR14002:SF7 membership).
