# PA0148 (Q9I6Y4) notes

Adenine deaminase (cog1816 group 3, amidohydrolase superfamily), formerly misannotated as adenosine deaminase. No deep-research provider was available; literature search by hand (PubMed "Pa0148 adenine deaminase"; full text of PMID:21710971 in the cache).

## Literature

- Goble et al. 2011 (PMID:21710971; full text): purified PA0148 deaminates adenine ["All of these proteins will deaminate adenine to produce hypoxanthine with k(cat)/K(m) values that exceed 10(5) M(-1) s(-1)."]; no activity on adenosine ["Adenosine is not a substrate for any of these enzymes."]; zinc content ["Pa0148 and AAur1117 contained, on average, 0.5 and 0.9 equivalents of Zn2+ per monomer."]; structures with adenine, hypoxanthine, 6-chloropurine; zinc ligands His16, His18, His196, Asp277. The paper does not test the in vivo role (salvage vs catabolism).

## Review decisions

- ACCEPT: GO:0000034 IBA/IDA/IEA, GO:0006146 IBA/IEA, GO:0008270.
- GO:0019239 deaminase activity: TOO_GENERAL (GO:0000034 is_a it).
- GO:0043103 hypoxanthine salvage IBA/IEA: KEEP_AS_NON_CORE (fits the definition; in vivo role in P. aeruginosa untested).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000150991 | GO:0000034 adenine deaminase activity | 6 | 14 (12 taxa) | GO:0000034, IDA, PMID:21710971 (PseudoCAP) | SOUND | Full text read: purified-enzyme kinetics, product confirmed by mass spectrometry, co-crystal structures. Node term suits the clade. | S. cerevisiae AAH1 (SGD:S000005085), S. pombe SPBC1198.02, UniProt Q8X1T6, E9AF40, Q9RDE5 | Yes, on five other seeds |

No PSEUDOCAP or GO_CENTRAL defect.
