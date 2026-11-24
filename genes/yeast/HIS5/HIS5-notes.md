# HIS5 (YIL116W, P07172) notes

Pathway context: YeastPathways HISTSYN-PWY, step 7 (EC 2.6.1.9). YeastPathways also lists HIS5 in PWY3O-4115 (phenylalanine degradation transamination) and ALL-CHORISMATE-PWY-1.

- Identity: [UniProt:P07172 "RecName: Full=Histidinol-phosphate aminotransferase {ECO:0000305};"], class II PLP aminotransferase, PLP cofactor.
- Genetics: [PMID:14190241 "Each of the histidine mutants of Saccharomyces cerevisiae has been correlated with a particular step in histidine biosynthesis"].
- Aromatic transamination in yeast is Aro8/Aro9: [PMID:9491082 "aro8 and aro9 double mutants which are auxotrophic for both phenylalanine and tyrosine"] -> HIS5 cannot substitute in vivo. No yeast experiment found showing His5 aromatic aminotransferase activity (WebSearch, Oct 2026). Bacterial HisC promiscuity is the likely basis of the pathway-database assignment.
- Decisions: aromatic-amino-acid transaminase RCA = MARK_AS_OVER_ANNOTATED; Phe catabolic process and chorismate metabolic process RCA = REMOVE; generic transferase/amino acid transaminase IEA -> MODIFY to GO:0004400.

- 2026-11-11 (PR #6250 review): GO places GO:0004400 L-histidinol-phosphate:2-oxoglutarate
  transaminase activity under GO:0140385 amino acid transaminase activity, although
  L-histidinol phosphate is not an amino acid. The ARBA GO:0140385 row is TOO_GENERAL in the review
  (true by GO's is_a and entailed by the accepted GO:0004400); the placement itself is a possible
  ontology question for GO rather than a curation issue for HIS5.
