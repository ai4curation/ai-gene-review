# PP_4452 curation notes

## Opine-dehydrogenase architecture

Q88EL0 carries the opine/lysopine dehydrogenase family assignments
`IPR051729`, `IPR003421`, and `PTHR38015:SF1`, including an Octopine_DH Pfam
domain. It lacks the PanE/ApbA family assignment that supports the canonical
ketopantoate reductase in this organism.
[file:PSEPK/PP_4452/PP_4452-uniprot.txt "DR   PANTHER; PTHR38015:SF1; OPINE
DEHYDROGENASE DOMAIN-CONTAINING PROTEIN; 1."]

The PANTHER family is grounded by reviewed opine, octopine, vitopine, and
tauropine dehydrogenases, whereas the current EC 1.1.1.169 and pantothenate
pathway assignments were propagated electronically. This is a family mismatch,
not merely a redundant paralog. The ketopantoate-reductase activity and
pantothenate-biosynthesis annotations should be removed. A broad oxidoreductase
term can be retained until the native opine-like substrate is identified.

KEGG independently assigns `ppu:PP_4452` to `K04940`, opine dehydrogenase
(EC 1.5.1.28), and gives the GenBank product as an NAD/NADP
octopine/nopaline-dehydrogenase-family protein.
[KEGG ppu:PP_4452](https://www.kegg.jp/entry/ppu:PP_4452)
The local whole-proteome metadata also places PP_4452 immediately before an
opine ABC-transporter neighborhood and the named opine-oxidase genes `ooxA`
(PP_4456) and `ooxB` (PP_4457).
[file:projects/P_PUTIDA/data/psepk_gene_list.tsv "ooxA PP_4456\tOpine oxidase subunit A"]

The family and neighborhood support an opine-related physiological role, but
they do not establish which opine PP_4452 uses or whether the relevant in vivo
direction is reductive condensation or oxidative cleavage. The first-pass gene
review therefore accepts only the existing broad oxidoreductase activity and
does not add the substrate-specific GO opine-dehydrogenase term.
