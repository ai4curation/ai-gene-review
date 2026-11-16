# nfxB (PA4600, P32265) review notes

## Literature

- NfxB represses the divergent mexC-mexD-oprJ operon and its own gene: the cloned gene reverses OprJ overproduction in the nfxB mutant K385 and represses mexC-lacZ and nfxB-lacZ fusions in E. coli [PMID:8878035 "the cloned nfxB gene repressed synthesis of a mexC-lacZ fusion in Escherichia coli"].
- Purified NfxB binds upstream of nfxB [PMID:7592337 "NfxB specifically binds upstream of the nfxB coding region as demonstrated by gel retardation and DNase I footprinting"].
- The 199-residue form is the functional repressor; it binds a region with two inverted repeats upstream of mexCD-oprJ and is a tetramer [PMID:23924707 "NfxB binds upstream of the mexCD-oprJ transcription initiation site to a region containing two inverted repeats, both of which are required for binding"; "Size exclusion column chromatography demonstrated that wild-type NfxB forms tetramers in solution"].
- Most nfxB mutant phenotypes are indirect, via pump overexpression [PMID:20373734 "suggesting that inappropriate overexpression of a functional MexCD-OprJ efflux pump causes pleiotropic changes"].
- Original cloning: nfxB affects quinolone permeability [PMID:1330820 "The gene nfxB is one of the genes which affect the cell membrane permeability of quinolones in Pseudomonas aeruginosa PAO"].

Search: PubMed metadata/abstracts for all GOA-cited PMIDs (PubMed MCP, 2026-11-05); all cached abstracts read. No deep-research provider available.

## PseudoCAP IBA-seed assessment

Node-level record for the shared PTN004738546 group (nfxB, nalC, PA3678, atuR, nalD here; PA4596, psrA, mexZ reviewed in parallel).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004738546 | GO:0000976 transcription cis-regulatory region binding | 7 | 411 (33 taxa) | GO:0000976, IDA, PMID:23924707 (also CollecTF IPI PMID:7592337) | SOUND | Abstract reports EMSA of purified NfxB on the mexCD-oprJ upstream region with two required inverted repeats. Under-specific only (GO:0000987 fits). | P0ACS9 AcrR (E. coli; IDA GO:0000976 PMID:17644067, PMID:37787551), Q9KR96 VC_1746 (CollecTF), G3XCU9 mexZ, Q9HXS0 nalC, Q9HXW2 PA3678/mexL, Q9HY46 nalD | Yes |
| PTN004738546 | GO:0006355 regulation of DNA-templated transcription | 19 | 411 (33 taxa) | GO:0045892, IMP, PMID:8878035 (PseudoCAP and UniProt) | SOUND | Complementation and lacZ-fusion repression stated in the abstract. | E. coli AcrR, RutR (P0ACU2, IDA), UidR, CecR, BetI, BdcR, ComR; M. tuberculosis KstR, KstR2, Mce3R, EthR (IMP/IDA); P. aeruginosa mexZ, psrA, PA4596, nalC, nalD, atuR, PA3678 | Yes |
| PTN004738546 | GO:0003700 DNA-binding transcription factor activity | 7 | 411 | (no PseudoCAP seed from nfxB in the worklist) | n/a | AcrR IDA (PMID:8821940, PMID:36416552), RutR IDA, Mce3R IMP | P0ACS9, P0ACU2, P95251, Q9KR96, G3XCU9, Q9HXW2 | Yes |

Node verdict: the three IBDs on PTN004738546 stand on many independent experimentally characterised TetR regulators (checked live in QuickGO, 2026-11-05, experimental evidence codes for P0ACS9, P0ACT6, P0ACU0, P0ACU2, P17446, P39334, P75952, P95251, P96856, P9WMB9, P9WMC1, Q9KR96). Generic transcription-regulator and cis-regulatory-binding terms suit a TetR clade of 411 leaves in 33 taxa. All five PseudoCAP seeds from this batch are SOUND. **No GO_CENTRAL defect is recorded for this node**; the leaf IBAs are refined (MODIFY to GO:0000987 / GO:0001217 / GO:0045892) only for gene-level granularity, with `root_cause: NO_FAILURE_CORE`.

Non-seed PseudoCAP defects on this gene: GO:0032410 negative regulation of transporter activity (PMID:8878035 and PMID:20373734), DELETE_ROW, PROBABLE (NfxB represses pump transcription, not pump activity). The same defect is recorded on nalC, nalD and (by the parallel agent) mexZ.
