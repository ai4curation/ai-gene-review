# pchA (PA4231, Q51508) notes

Isochorismate synthase, first and rate-limiting enzyme of salicylate/pyochelin biosynthesis; last gene of the pchDCBA operon. No deep-research provider was available; literature search by hand (cached abstracts of PMID:12624097 and PMID:7500944; QuickGO for E. coli EntC).

## Literature

- Gaille, Reimmann & Haas 2003 (PMID:12624097; abstract only): PchA purified to homogeneity from P. aeruginosa ["The PchA protein was purified to apparent electrophoretic homogeneity from a PchA-overexpressing P. aeruginosa strain."]; Mg2+-dependent 52-kDa monomer; ["a K(m) = 4.5 microm and a k(cat) = 43.1 min(-1) were determined for chorismate"]; PchA level limits salicylate formation and its overexpression raises pyochelin.
- Serino et al. 1995 (PMID:7500944; abstract only): pchBA necessary for salicylate formation; complementation of an E. coli entC mutant needs pchBA; ["a pathway leading from chorismate to isochorismate and then to salicylate plus pyruvate, catalyzed consecutively by the iron-repressible PchA and PchB proteins"].
- QuickGO (2026-11-05): E. coli EntC P0AEJ2 has GO:0008909 by IDA (PMID:2139795, 2684979) and EXP (PMID:17243787, 20079748).

## Review decisions

All six rows ACCEPT (activity IBA/IDA/IEA; salicylic acid biosynthetic process IDA/IEA; pyochelin biosynthetic process IDA). PchA catalyses a step of both processes, so involved_in is participation, not necessity.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000132907 | GO:0008909 isochorismate synthase activity | 2 | 17 (13 taxa) | GO:0008909, IDA, PMID:12624097 (PseudoCAP) | SOUND | Abstract reports purified-enzyme kinetics with chorismate for PchA itself. Node term suits an isochorismate synthase clade. | E. coli EntC P0AEJ2 (IDA/EXP) | Yes, on EntC |

No PSEUDOCAP or GO_CENTRAL defect.
