# fadD1 (PA3299, Q9HYU4) review notes

## Literature

- Kang et al. 2010 (full text read, PMC2958839). fadD1 and fadD2 are genetically linked; both complement an E. coli fadD/fadR mutant [PMID:21042406 "Upon introduction into an E. coli fadD(-)/fadR(-) double mutant, both P. aeruginosa fadDs functionally complemented the E. coli fadD(-)/fadR(-) mutant, allowing degradation of different chain-length FAs"].
- Purified FadD1 prefers long-chain fatty acids [PMID:21042406 "FadD1 of P. aeruginosa coupled CoASH to LCFA better than to SCFA or MCFA"]; the enzymes were purified from an E. coli fadD- strain [PMID:21042406 "purified to near homogeneity from an E. coli fadD"].
- Chromosomal mutants: [PMID:21042406 "Both fadD1 and fadD2 single mutants had various levels of defects when grown on all FAs"]; [PMID:21042406 "fadD1 was found to be important for the metabolism of all FAs, particularly the unsaturated LCFA oleate"]. The fadD1 mutant showed only increased swarming among virulence-related phenotypes; the mutants had reduced lung fitness in mice (not annotated; indirect).
- Location: no data for FadD1; the paper's pathway model follows E. coli, where FadD is peripheral to the inner membrane [PMID:21042406 "FA may be transported through the inner membrane via an unknown mechanism coupled to a single peripheral membrane FadD protein"].

Other seed: E. coli FadD (P69451) checked in QuickGO (live, 2026-11-05): GO:0006631 IMP (PMID:1649829), GO:0004467 IDA/EXP, GO:0009898 IDA.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001534887 | GO:0006631 fatty acid metabolic process | 2 | 20 (10 taxa) | GO:0006631, IDA, PMID:21042406 (also GO:0042758 IDA, same paper) | SOUND | Purified-enzyme kinetics plus complemented mutant growth defects on fatty acids; the gene performs the activation step. The generic node term suits a clade of FadD-type AMP-binding acyl-CoA synthetases (FadD, FadD1, FadD2, RpfB and others). | E. coli FadD (P69451; GO:0006631 IMP, PMID:1649829) | Yes |

No PSEUDOCAP or GO_CENTRAL defect.
