# selA (P0A821) review notes

Deep research: no provider deep-research file was available for this gene in this
session; the review rests on cached publications (GOA references plus UniProt-cited
PMID:2007585, PMID:1474891 and PMID:9688279, fetched with `just fetch-pmid`) and the
reviewed UniProt record.

- Selenocysteine synthase: the whole Ser-tRNA(Sec) to Sec-tRNA(Sec) conversion
  occurs on SelA. [PMID:2007584 "Evidence is presented that the overall conversion of
  seryl-tRNA(Sec UCA) to selenocysteyl-tRNA(Sec UCA) occurs at the SELA protein"]
- PLP: 1 per subunit [PMID:2007584 "SELA contains 1 mol of bound pyridoxal
  5-phosphate/mol of 50-kDa subunit"]; Lys295 carries it [PMID:9688279 "proved that
  Lys295 was modified"].
- Mechanism: dehydration to aminoacrylyl-tRNA, then HSe- addition from SelD donor.
  [PMID:2007585 "involves the dehydration of L-serine esterified to tRNA in a first
  step formally followed by the 2,3-addition of HSe- which is provided by the SELD
  protein"]
- Decamer, one tRNA per dimer. [PMID:1474891 "consists of 10 monomers arranged in two
  rings"]
- Selectivity against sulfur from the selenophosphate phosphate. [PMID:9688279 "the
  phosphate moiety of selenophosphate provides selenocysteine synthase with the
  discrimination specificity against sulfur"]
- Ternary complex with SelD on tRNA(Sec). [PMID:26378233 "resulting in a 1.3-MDa
  ternary complex"] The GOA row is bare protein binding: REMOVE per policy.
- Decisions: selenocysteine incorporation IEA MODIFY to GO:0001717 (as in PSEPK selA);
  catalytic activity MODIFY to GO:0004125; cytoplasm MODIFY to cytosol; identical
  protein binding KEEP_AS_NON_CORE (decamer; no more specific MF term).
- PAINT: no IRD/IKR loss on the lineage.
