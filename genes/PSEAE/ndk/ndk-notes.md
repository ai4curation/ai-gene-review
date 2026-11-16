# ndk (PA3807, Q59636) review notes

## Literature

Search (Europe PMC REST, 2026-11-05: `TITLE:"nucleoside diphosphate kinase" AND
aeruginosa`, 30 hits read as titles). Papers used (all abstract only):

1. Kavanaugh-Black et al. 1994 [PMID:8016083]: Ndk purified from P. aeruginosa; activity
   also associated with succinyl-CoA synthetase.
2. Shankar et al. 1996 [PMID:8606147]: a 16-kDa cytoplasmic form and a protease-derived
   12-kDa membrane-associated form; both autophosphorylate; the membrane form prefers GTP
   synthesis [PMID:8606147 "In the membrane-associated state, the 12-kDa form of Ndk was
   found to synthesize GTP in preference to other nucleoside triphosphates."].
3. Sundin et al. 1996 [PMID:8809750]: cloning of ndk; NDK activity in cytosolic and
   membrane fractions; cytosolic Ndk transfers the ATP gamma-phosphate to other NDPs
   non-specifically [PMID:8809750 "The cytosolic Ndk was non-specific in its transfer
   activity of the terminal phosphate from ATP to other nucleoside diphosphates."]. ndk
   hyperexpression in an algR2 mutant restored alginate to ~60% of wild type
   [PMID:8809750 "Hyperexpression of ndk from pGWS95 in the P. aeruginosa algR2 mutant
   also restored alginate production to levels that were approximately 60% of wild
   type."]. The authors link this to GTP supply for GDP-mannose.

UniProt Q59636 (reviewed): HAMAP MF_00451, active-site His117 (phosphohistidine).

Alginate: AlgA (GDP-mannose pyrophosphorylase) uses GTP; Ndk supplies GTP, a co-substrate,
and performs no step of alginate synthesis. The algR2 (AlgQ) mutant is a regulatory
mutant affecting many genes, and the rescue is partial. This is a necessity/precursor
supply phenotype, not participation.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000887110 | GO:0004550 nucleoside diphosphate kinase activity | 21 | 412 (137 taxa) | GO:0004550, IDA, PMID:8809750 (PseudoCAP) | SOUND | Abstract reports NDK activity assays in cytosolic and membrane fractions and the substrate range of the cytosolic enzyme; HAMAP NDK with active-site His. | E. coli Ndk (P0A763), human NME1-4 (P15531, P22392, Q13232, O00746), mouse/rat Nme, yeast YNK1, S. pombe ndk1, Arabidopsis NDPK1/2, Drosophila awd, Dictyostelium, zebrafish, Plasmodium, maize | Yes; NDK is among the best characterised enzymes and the node is richly seeded. No GO_CENTRAL defect. |

## Annotation decisions

- GO:0004550 (IBA, IDA, IEA): ACCEPT; core.
- GO:0005524 ATP binding IEA: KEEP_AS_NON_CORE (phosphate donor substrate).
- GO:0005737 (EXP, IBA, IEA): ACCEPT.
- GO:0006183/0006228/0006241 GTP/UTP/CTP biosynthesis IEA: ACCEPT.
- GO:0006163, GO:0006220 IDA and GO:0009142 IBA: TOO_GENERAL (entailed by the accepted
  GTP/UTP/CTP biosynthetic terms).
- GO:0042121 alginic acid biosynthetic process IDA: REMOVE, PSEUDOCAP WRONG_TERM defect,
  PROBABLE (not a seed).
