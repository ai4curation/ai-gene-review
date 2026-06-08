# cdc2 (Cdk1, p34cdc2) — S. pombe — review notes

UniProt: P04551 (CDK1_SCHPO). PomBase SPBC11B10.09. EC 2.7.11.22.

## Core identity
Cdc2 is the founding cyclin-dependent serine/threonine protein kinase (CDK1), the master regulator of the
fission-yeast mitotic and meiotic cell cycle (Nurse, Nobel Prize 2001). It drives both the G1/S and G2/M
transitions. It is catalytically inert as a monomer and is activated by binding a B-type cyclin (mitotic
cyclin Cdc13; G1/S cyclins Cig1/Cig2/Puc1), CAK-mediated activating phosphorylation of Thr167, and removal
of inhibitory Tyr15 phosphorylation by Cdc25; it is inhibited by Wee1/Mik1 phosphorylation of Tyr15 and by
the CDK inhibitor Rum1 in G1.

## Key supporting evidence (verbatim)
- Founding genetic identification of dual G1/G2 roles: [PMID:7254352 "Gene required in G1 for commitment to cell cycle and in G2 for control of mitosis in fission yeast."]
- Tyr15 phospho-regulation of mitotic entry: [PMID:2682257 "The single detectable site of tyrosine phosphorylation in pp34 has been mapped to Tyr 15, a residue within the presumptive ATP-binding domain. Substitution of this tyrosine by phenylalanine advances cells prematurely into mitosis, establishing that tyrosine phosphorylation/dephosphorylation directly regulates pp34 function."]
- Thr167 activating phosphorylation / cyclin association: [PMID:1655416 "we establish that Thr167 phosphorylation is required for p34cdc2 kinase activity at mitosis and is involved in the association of p34cdc2 with cyclin B."]
- Master regulator + ORC2/Orp2 substrate, anti-rereplication: [PMID:11486016 "Cdc2 kinase is a master regulator of cell cycle progression in the fission yeast Schizosaccharomyces pombe. Our data indicate that Cdc2 phosphorylates replication factor Orp2, a subunit of the origin recognition complex (ORC)."]
- suc1/Cks1 is a component of the holoenzyme: [PMID:3322810 "p13suc1 was found in yeast lysates in a complex with the cdc2+ gene product."]
- Meiosis: [PMID:7498766 "The cdc2 gene, which is required for the initiation of both mitotic S-phase and M-phase, is essential for premeiotic DNA synthesis and meiosis II."]
- Single CDK can run the whole cell cycle; activity thresholds order substrate phosphorylation: [PMID:27984725 "a single genetically engineered cyclin-CDK chimera between the mitotic B-type cyclin Cdc13 and the CDK Cdc2 (Cdc13-L-Cdc2) can substitute for the four cyclin-CDK complexes acting during the mitotic cell cycle and the six cyclin-CDK complexes acting during the meiotic cell cycle"] and [PMID:27984725 "a single rising CDK activity orders substrate phosphorylation via the sequential passage through substrate-specific activity thresholds"]. >200 substrates identified.
- Substrate dis1 (chromosome segregation): [PMID:16920624 "Cdc2 thus directly phosphorylates Dis1, and this phosphorylation regulates Dis1 localization in both metaphase and anaphase and ensures high-fidelity segregation."]
- G1 inhibition by pheromone via G1 cyclin B-CDK: [PMID:9034336 "Pheromone inhibits the p34cdc2 kinase associated with both the G1-specific B-type cyclin p45cig2 and the B-type cyclin p56cdc13"]

## Annotation review strategy
- MF kinase terms (GO:0004693 cyclin-dependent protein serine/threonine kinase activity; GO:0097472 CDK activity;
  GO:0004674 protein serine/threonine kinase activity; GO:0004672 protein kinase activity; GO:0106310 protein
  serine kinase activity) — all describe the CORE catalytic activity. GO:0004693 is the most informative; ACCEPT
  it as core. The many duplicate GO:0004693 / GO:0004674 entries (esp. ~70 from PMID:27984725, which are
  individual substrate-phosphorylation observations) are all valid IDA/EXP support for the same core MF; ACCEPT
  (one representative is the core; the rest are redundant duplicates of the same MF, also ACCEPT). GO:0004672 and
  GO:0004674 are less specific parents → MODIFY/ACCEPT-as-supporting; GO:0106310 protein serine kinase activity is
  a partial/over-narrow Rhea/ISS import (CDK is Ser/Thr) → KEEP_AS_NON_CORE/ACCEPT but not core.
- BP core: G1/S transition (GO:0000082), G2/M transition (GO:0000086), positive regulation of G1/S (GO:1900087),
  premeiotic DNA replication initiation (GO:1904514), positive regulation of meiotic cell cycle (GO:0051446) —
  ACCEPT as core cell-cycle driving functions.
- Numerous specific downstream/substrate-process BP terms (kinetochore assembly, sister chromatid biorientation,
  spindle elongation, chromosome condensation, contractile ring/cytokinesis inhibition, septum biogenesis, NHEJ
  restraint, telomere tethering, APC regulation, protein catabolism, mitotic exit, etc.) are genuine experimentally
  supported phosphorylation-substrate roles but are peripheral consequences of the single master kinase acting on
  many substrates → KEEP_AS_NON_CORE (real but not the core function). Mark clearly over-reaching/very narrow ones
  appropriately.
- CC: cyclin-dependent protein kinase holoenzyme complex (GO:0000307) is core. nucleus/cytoplasm/SPB/spindle/
  kinetochore/chromatin localizations are valid IDA active-site locations → ACCEPT/KEEP_AS_NON_CORE. IEA nucleus
  (ARBA) and IEA cytoplasm duplicate the experimental CC; ACCEPT/redundant.
- protein binding (GO:0005515, bare) — uninformative; MARK_AS_OVER_ANNOTATED, partners (orc2, pch1, rum1, cig2,
  cdc13, suc1, wos2) better captured by holoenzyme complex and specific BP terms.
- NOT nuclear pore complex assembly (GO:0051292, negated, PMID:35354597) — ACCEPT the negation.
- IEA GO:0004693 from EC/ARBA and InterPro GO:0004672 — redundant electronic versions of experimentally proven
  activity; ACCEPT (correct) but redundant.
