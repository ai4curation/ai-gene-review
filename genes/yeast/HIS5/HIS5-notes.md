# HIS5 (YIL116W, P07172) notes

Pathway context: YeastPathways HISTSYN-PWY, step 7 (EC 2.6.1.9). YeastPathways also lists HIS5 in PWY3O-4115 (phenylalanine degradation transamination) and ALL-CHORISMATE-PWY-1.

- Identity: [UniProt:P07172 "RecName: Full=Histidinol-phosphate aminotransferase {ECO:0000305};"], class II PLP aminotransferase, PLP cofactor.
- Genetics: [PMID:14190241 "Each of the histidine mutants of Saccharomyces cerevisiae has been correlated with a particular step in histidine biosynthesis"].
- Aromatic transamination in yeast is Aro8/Aro9: [PMID:9491082 "aro8 and aro9 double mutants which are auxotrophic for both phenylalanine and tyrosine"] -> HIS5 cannot substitute in vivo. No yeast experiment found showing His5 aromatic aminotransferase activity (WebSearch, Oct 2026). Bacterial HisC promiscuity is the likely basis of the pathway-database assignment.
- Decisions: aromatic-amino-acid transaminase RCA = MARK_AS_OVER_ANNOTATED; Phe catabolic process and chorismate metabolic process RCA = REMOVE; generic transferase/amino acid transaminase IEA -> MODIFY to GO:0004400.
