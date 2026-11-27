# fabV (PA2950, Q9HZP8) notes

Triclosan-resistant enoyl-ACP reductase (TER/FabV family). No deep-research provider was
available; literature checked by hand (PMID:19933806 and PMID:27965638 full texts cached;
QuickGO for the V. cholerae and Y. pestis seeds). Consistent with the fabA, fabB and fabD
reviews (fatty acid biosynthetic process accepted as core for FAS II enzymes).

## Literature

- Zhu et al. 2010 (PMID:19933806): purified PaFabV reduces enoyl-ACP with NADH ["The addition of
  PaFabV, PaFabI, or EcFabI plus NADH to the reaction mixture yielded butyryl-ACP"]; also reduces
  crotonyl-CoA but with ~30-fold lower Vmax (UniProt kinetics); fabV deletion makes PAO1
  >2000-fold more triclosan-sensitive.
- Huang et al. 2016 (PMID:27965638, full text read): ENR activity in fabV-mutant extracts
  ["The ENR activity (in μmol/min per mg extract protein) in cell-free extract of PAO170 was
  0.175 ± 0.006, and was lower than that in the cell-free extract of wild-type strain PAO1 (0.478
  ± 0.032)."], partly restored by complementation; slower growth, less AHL, swarming and
  virulence factors (indirect phenotypes, not annotated).
- Seeds: V. cholerae FabV Q9KRA3 (IDA GO:0004318, PMID:18032386); Y. pestis FabV Q8Z9U1 (IDA
  GO:0004318, PMID:22244758).

## Review decisions

- GO:0004318 (IDA, IMP, IBA, IEA) and GO:0006633 (IDA, IBA, IEA): ACCEPT, core.
- GO:0050343 trans-2-enoyl-CoA reductase (all rows): KEEP_AS_NON_CORE (genuine secondary
  activity, much lower than on enoyl-ACP).
- GO:0051287 NAD binding (all rows): KEEP_AS_NON_CORE (cofactor).
- GO:0016491 oxidoreductase activity: TOO_GENERAL (entailed by GO:0004318).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002206122 | GO:0004318 enoyl-[acyl-carrier-protein] reductase (NADH) activity | 3 | 7 (6 taxa) | GO:0004318, IMP, PMID:27965638 (PseudoCAP) | SOUND | Full text read: ENR activity falls to ~37% in fabV-mutant extracts and rises on complementation. Lysate-activity evidence alone is weak, but the activity is FabV's own (purified-enzyme IDA, PMID:19933806); residual activity is FabI's. Node term suits the FabV clade. | V. cholerae FabV Q9KRA3 (IDA); Y. pestis FabV Q8Z9U1 (IDA); also FabV's own UniProt IDA | Yes, on the V. cholerae and Y. pestis seeds |

No PSEUDOCAP or GO_CENTRAL defect.
