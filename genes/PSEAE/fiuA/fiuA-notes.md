# fiuA (PA0470, Q9I648) notes

## Literature (own research, 2026-11-05; no deep-research provider available)

- FiuA is the main outer-membrane receptor for ferric ferrichrome [PMID:20047910 "ferrichrome is transported across the outer membrane primarily (80%) by the FiuA receptor and to a lesser extent (20%) by a secondary transporter"]; energy from TonB1 [PMID:20047910 "the energy required for both pathways of ferrichrome uptake is provided by the inner membrane protein TonB1"].
- Substrate range: ferrichrome-type siderophores [PMID:39138320 "FiuA is the TBDT of the ferric forms of ferrichrome, ferricrocin, ferrichrysin and RHODO"].
- Regulation and signalling: produced only with ferrichrome; induced via the adjacent fiuI-fiuR ECF sigma/anti-sigma locus [PMID:16484199 "The involvement of this putative regulatory locus in the specific induction of the ferrioxamine B and ferrichrome receptors has been demonstrated"]. FiuA has an N-terminal STN signalling domain (SMART SM00965, residues 57-108), i.e. it is a TonB-dependent transducer [PMID:35138377 "TDPs may contain an additional signaling domain"].
- PMID:16484199 is abstract-only in the cache; the full text could not be retrieved in this session (PMC page access refused, Europe PMC returning 500). The earlier PA0472/foxI reviews read it and describe the regulatory experiments, not FiuA transport assays.
- UniProt name problem: the unreviewed entry carries the ARBA name "Metal-pseudopaline receptor CntO" and an ARBA pseudopaline FUNCTION text; both are wrong for FiuA (recorded as a UNIPROT source defect on the UniProt reference). FoxA (Q9I116) has the same wrong name.
- Consistency: PA0472 (FiuI) review describes FiuA as the ferrichrome receptor it regulates; consistent.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000793005 | GO:0033214 siderophore-iron import into cell | 3 | 68 (13 taxa) | GO:0042928 ferrichrome import into cell, IMP, PMID:20047910 | SOUND | Abstract states the fiuA mutant 55Fe-ferrichrome uptake result outright (80% FiuA-dependent). | E. coli Fiu P75780 (GO:0033214 IDA PMID:2139424, IMP PMID:31712312); E. coli FhuE P16869 (GO:0015687/GO:0044718 IMP PMID:31098021) | Yes; Fiu experimental rows alone support it |
| PTN000793005 | GO:0033214 siderophore-iron import into cell | 3 | 68 (13 taxa) | GO:0042928 ferrichrome import into cell, IMP, PMID:16484199 | UNVERIFIABLE | Abstract shows proteomics and regulation only; whether a fiuA mutant transport phenotype is in the full text could not be checked. Term correct for FiuA from PMID:20047910. | as above | Yes |

Other seeds were queried live in QuickGO (2026-11-05). The node is a clade of TonB-dependent siderophore receptors and the term suits it. No PseudoCAP or GO_CENTRAL defect. The same node's GO:0015344 IBD (seeded by FoxA) is assessed in genes/PSEAE/foxA/foxA-notes.md; verdicts are consistent.

## Action counts

ACCEPT 10, MODIFY 3, TOO_GENERAL 2.
