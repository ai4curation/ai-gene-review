# slaB (D5E1S7, Priestia megaterium QM B1551 / DSM 1804) notes

## 2026-11-10 session

- Deep research: `just deep-research PRIM1 slaB --provider perplexity` failed in this
  environment (the deep-research client dependency could not be resolved offline and no
  provider key is configured). No provider file was written; the review rests on the
  UniProt record and cached literature below.
- Function: NAD+-dependent 3-sulfolactaldehyde (SLA) dehydrogenase of the sulfo-TAL
  (sulfo-SFT) pathway. UniProt (Swiss-Prot, ECO:0000269 PubMed:33036753): "Catalyzes the
  oxidation of 3-sulfolactaldehyde (SLA) to sulfolactate (SL)"; reaction RHEA:47932, EC 1.2.1.97.
- PMID:33036753 (Liu et al. 2020 BBRC, B. megaterium DSM 1804) is abstract-only in the cache;
  the abstract names only the transaldolase SqvA [PMID:33036753 "in which sulfosugar cleavage is
  catalyzed by the transaldolase SqvA"]. The SlaB assay is therefore taken from the curated
  UniProt statement.
- Review PMID:41676062: [PMID:41676062 "it can be oxidized to SL by sulfolactaldehyde
  dehydrogenase SlaB in aerobic Bacillus strains"].
- Ortholog SftD of B. aryabhattai (PMID:32919372) also oxidizes GAP and E4P
  [PMID:32919372 "SftD oxidized also GAP and E4P as substrates but showed no activity with SL and
  DHPS"]; not tested for SlaB as far as the accessible text shows.
- GO: no SLA-specific MF term (OLS 2026-11-10); GO:0004029 aldehyde dehydrogenase (NAD+) is
  used as the core MF and a new term is proposed. The TreeGrafter GO:0008911 lactaldehyde
  dehydrogenase row descends from a PAINT IBD (PTN008677383) seeded only by M. jannaschii
  MJ1411 (Q58806); corrected laterally to GO:0004029.
- PANTHER PTHR42991:SF1 is functionally mixed (GapN, lactaldehyde DH, SafD sulfoacetaldehyde DH,
  PhnY, aspartate-semialdehyde DH, SLA DH); see the PTHR42991 family review.
- BP: added GO:1902777 (6-sulfoquinovose(1-) catabolic process); GO:0061722 sulphoglycolysis is
  defined by DHAP/pyruvate products and does not fit the F6P-forming sulfo-TAL route.
