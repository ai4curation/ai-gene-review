# tesA (PA2856, Q9HZY8) notes

SGNH/GDSL-family periplasmic esterase/lysophospholipase, close relative of E. coli TesA/TAP
(P0ADA1). No deep-research provider was available; literature was checked by hand (cached
PMID:23874889 full text; PMID:20931591 abstract only; QuickGO for the E. coli seed).

## Literature

- Leščić Ašler et al. 2010 (PMID:20931591, abstract only): of 34 substrates, TesA acts mainly as
  an esterase ["TesA, EstA and EstP were shown to function as esterases with different
  affinities and catalytic efficacies towards p-nitrophenyl butyrate."].
- Kovačić et al. 2013 (PMID:23874889, full text read): purified TesA hydrolyses 1-acyl
  glycerophosphocholines (C6, C12, C16) with kcat/Km 10^5-10^6 per M per s, far above
  p-nitrophenyl butyrate (1.2 x 10^4), ["strongly suggest that lysophospholipase A activity may
  represent at least one of the physiological functions of TesA"]; fractionation in PAO1 ["These
  results indicate that TesA is primarily localized in the periplasm."]; crystal structure,
  SGNH fold.
- E. coli TesA (P0ADA1): IDA GO:0004622 (PMID:1864840, EcoCyc), IDA GO:0030288 (QuickGO).

## Review decisions

- GO:0004622 (IDA, IBA, IEA): ACCEPT, core.
- GO:0004064 arylesterase and GO:0106435 carboxylesterase (all rows): KEEP_AS_NON_CORE (genuine
  activity on artificial esters, secondary to lysoPL A1 activity).
- GO:0016042 lipid catabolic process IBA: KEEP_AS_NON_CORE.
- GO:0030288 IBA: ACCEPT. GO:0005576 extracellular region IEA: TOO_GENERAL (periplasm is
  part_of extracellular region in GO; UniProt "Secreted" by similarity is contradicted by the
  fractionation, which places TesA in the periplasm).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000769562 | GO:0004622 phosphatidylcholine lysophospholipase A1 activity | 2 | 12 (10 taxa) | GO:0004622, IDA, PMID:23874889 (PseudoCAP) | SOUND | Full text read: Michaelis-Menten kinetics of purified TesA on 1-acyl-sn-glycero-3-phosphocholines, the exact substrate of the term; catalytic efficiency well above that on artificial esters. Node term suits a small TesA/TAP clade. | E. coli TesA P0ADA1 (IDA GO:0004622, PMID:1864840) | Yes, on E. coli TesA |

No PSEUDOCAP or GO_CENTRAL defect. (The other TesA IBA node, PTN002018599 GO:0106435, is
seeded by a UniProt IDA, not PseudoCAP, and is experimentally grounded.)
