# acnA (Q8ZP52, Salmonella Typhimurium LT2) - curation notes

## Session log (2026-10-23)

- Provider deep research (`just deep-research SALTY acnA --provider ...`) could not be run
  in this session because provider API credentials were unavailable. No
  `*-deep-research-*.md` file was created; these notes and the review rely on the cached
  primary paper, the UniProt entry, and cached E. coli orthologue papers.
- Primary paper PMID:11294638 is abstract-only in the cache (`full_text_available: false`).

## Key findings

- Aconitase activity of the purified Salmonella enzyme:
  [PMID:11294638 "Homogeneous AcnA protein of S. enterica had strong aconitase activity and catalyzed the hydration of the 2-methyl-cis-aconitate to yield 2-methylisocitrate."]
- PrpD does not do the hydration step, so an aconitase is needed:
  [PMID:11294638 "did not catalyze the hydration of 2-methyl-cis-aconitate to 2-methylisocitrate"]
- In vitro reconstitution of the 2-methylcitric acid cycle:
  [PMID:11294638 "The purification of this enzyme allows the complete reconstitution of the 2-methylcitric acid cycle in vitro using homogeneous preparations of the PrpE, PrpC, PrpD, AcnA, and PrpB enzymes."]
- Redundancy with AcnB:
  [PMID:11294638 "inactivation of the acnA gene did not block growth of S. enterica on propionate as carbon and energy source"];
  [PMID:11294638 "an acnA and acnB double mutant was constructed, and this mutant strain cannot grow on propionate even when supplemented with glutamate"]
- UniProt (reviewed) curates both reactions (RHEA:10336, EC 4.2.1.3; RHEA:17941, EC 4.2.1.99)
  with ECO:0000269 from PMID:11294638; [4Fe-4S] cofactor and apo-form RNA binding are
  by similarity to E. coli/mammalian aconitases
  [file:SALTY/acnA/acnA-uniprot.txt "The apo form of AcnA functions as a RNA-binding regulatory protein"].
- E. coli orthologue (P25516) apo-AcnA binds acnA/acnB 3'UTRs
  [PMID:10589714 "the AcnA and AcnB apo-proteins each interact with the 3' untranslated regions (3'UTRs) of acnA and acnB mRNA"].

## Curation decisions

- Activities GO:0003994 and GO:0047456 (IDA + IBA/IEA): ACCEPT, core.
- TCA cycle GO:0006099 and propionate catabolic process GO:0019543: ACCEPT; the enzyme
  catalyses a step in each (participation, not just necessity). Specific 2-methylcitrate
  cycle GO process terms are obsolete (see genes/SHEON/prpF review), so GO:0019543 is the
  most precise term.
- mRNA binding (ISS) and IRE binding (IBA): MODIFY to mRNA 3'-UTR binding GO:0003730,
  which is kept as non-core (untested in Salmonella), following genes/ECOLI/acnA.
- Cellular respiration (ARBA IEA): MODIFY to TCA cycle.
- Cytosol (IBA) and [4Fe-4S] binding (IBA, ISS): ACCEPT.
