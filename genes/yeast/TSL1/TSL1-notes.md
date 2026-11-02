# TSL1 (YML100W) notes

UniProt P38427; module `trehalose_metabolism` (TSL1/TPS3-type regulatory subunit annoton, GO:0030234).

## Evidence journal
- 123-kDa subunit of trehalose synthase; N-terminus regulates Tps1 [PMID:8404905 "Specific proteolytic degradation of the 123-kDa polypeptide from the N-terminus greatly influences the Tre6P synthase activity, decreasing its inhibition by phosphate and activatability by fructose 6-phosphate"].
- Two-hybrid with Tps1 and Tps2; shared role with Tps3 [PMID:9194697 "both TsI1 and Tps3 can interact with Tps1 and Tps2"].
- Complex composition and redundancy [PMID:9837904 "Deletion of TPS2, TSL1, or TPS3 and, in particular, of TSL1 plus TPS3 destabilized the trehalose synthase complex"]; [PMID:9837904 "We conclude that Tps3 is a fourth subunit of the complex with functions partially redundant to those of Tsl1"].
- No catalytic activity: [PMID:9194697 "Tps1 and Tps2 carry the catalytic activities of trehalose synthesis"].
- Cytoplasmic, glucose-repressed [UniProt:P38427].

## Curation decisions
- GO:0003824 catalytic activity (InterPro GT-20) marked over-annotated: regulatory paralog.
- All protein-binding IPI rows REMOVE (captured by GO:0005946 / GO:0030234).
- YeastCyc TRESYN-PWY lists only TPS1 and TPS2 on reactions; its comment text has a typo ("TSL1 and TSL3" for TSL1 and TPS3).
