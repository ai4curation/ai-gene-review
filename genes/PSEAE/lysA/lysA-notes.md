# lysA (PA5277, P19572) review notes

Diaminopimelate decarboxylase (DAPDC, EC 4.1.1.20), the last step of the
diaminopimelate (DAP) pathway of L-lysine biosynthesis. 415 aa, PLP-dependent
fold-type III decarboxylase, Orn/Lys/Arg decarboxylase class-II family, LysA
subfamily (HAMAP MF_02120; NCBIfam TIGR01048; PANTHER PTHR43727).

## Literature (no deep-research provider available; own reading)

- Martin et al. 1986 (abstract only): the cloned P. aeruginosa lysA gene
  complemented a P. aeruginosa lys-12 mutant and an E. coli lysA mutant
  [PMID:3018430 "This gene complemented a lys mutation at the lys-12 locus of P.
  aeruginosa and a lysA defect in Escherichia coli."], and DAP-decarboxylase was
  made constitutively [PMID:3018430 "The P. aeruginosa DAP-decarboxylase was
  synthesized constitutively in P. aeruginosa as well as in E. coli"].
  Complementation of an E. coli lysA mutant by the cloned gene, plus DAPDC
  activity measured from the clone, directly supports the activity of this gene
  product.
- UniProt (HAMAP MF_02120): "Specifically catalyzes the decarboxylation of
  meso-diaminopimelate (meso-DAP) to L-lysine."
- No further P. aeruginosa-specific biochemistry found. PubMed MCP search
  returned API errors on 2026-11-05.

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000159906 | GO:0008836 diaminopimelate decarboxylase activity | 4 | 116 (80 taxa) | GO:0008836, IMP, PMID:3018430 (PseudoCAP) | SOUND | Abstract states the cloned gene encodes DAPDC and complements lysA mutants of P. aeruginosa and E. coli; HAMAP LysA subfamily agrees. | E. coli LysA P00861 (EXP/IDA), M. tuberculosis LysA P9WIU7 (IDA PMID:8440471), M. jannaschii LysA Q58497 (EXP PMID:12429091) | Yes; three independently characterised DAPDCs |

No PSEUDOCAP or GO_CENTRAL defect. The node is the LysA (PTHR43727) clade;
it is unrelated to the ODC node PTN000159726 for which a GO_CENTRAL AZIN1 defect
is recorded in genes/PSEAE/speC; that defect does not apply here.

The node also carries GO:0009085 L-lysine biosynthetic process (seed Mtb LysA
only); correct for the clade. The more specific GO:0009089 (via DAP) is now
obsolete, so GO:0009085 is the right level.
