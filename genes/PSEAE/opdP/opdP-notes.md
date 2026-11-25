# opdP (OccD3, Q9HVS0) review notes

No deep-research provider was available. Literature: Europe PMC search "OpdP AND aeruginosa"
(2026-11-05); full text of PMID:25338022 and PMID:22272184; fetched PMID:28440622 (abstract).

## Function

- OccD-subfamily channel [PMID:28440622 "OccD3 (OpdP or PA4501) is an OprD-like arginine"].
- Single-channel and uptake data [PMID:22272184 "Remarkably, the conductance of the dominant state of OccD3 is the largest of all channels analyzed";
  "The efficient arginine uptake mediated by OccD3 is noteworthy since this protein was shown, like OccD1, to mediate arginine uptake in P. aeruginosa in vivo"].
- Operon partner of dppA4 [PMID:25338022 "co-transcribed in an operon with PA14_58410 encoding the porin OpdP"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002160747 | GO:0015288 porin activity | 3 | 24 (6 taxa) | GO:0015288, IDA, PMID:25338022 (PseudoCAP) | WRONG (reference) | Full text read: the Dpp paper has no OpdP experiment and cites earlier work for OpdP transport. The term is correct (Eren 2012 single-channel and arginine uptake; PMID:28440622). PSEUDOCAP WRONG_REFERENCE, REPOINT to PMID:22272184, CONFIRMED. | OprD (P32722), OprE (G3XDA5) | Yes; stands on OprD (see oprD notes). No GO_CENTRAL defect. |
