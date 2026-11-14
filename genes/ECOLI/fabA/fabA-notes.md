# fabA (Escherichia coli K-12, P0A6Q3) curation notes

## 2026-11-13

- FabA is the bifunctional 3-hydroxydecanoyl-ACP dehydratase /
  trans-2-decenoyl-ACP isomerase of the oxygen-independent unsaturated fatty
  acid route. Both activities are core.
- Structure and mechanism: a hotdog-fold dimer with two shared active sites
  [PMID:8805534 "Dehydrase is a symmetric dimer with an unusual alpha+beta 'hot dog' fold. Each of the two independent active sites is located between the two subunits of the enzyme"];
  one His/Asp pair performs both reactions
  [PMID:8805534 "A two-base mechanism by which the histidine and aspartic acid together catalyze dehydration and isomerization reactions is consistent with the active-site structure."].
- Chain-length behaviour fixes where the double bond is introduced
  [PMID:8910376 "FabA was virtually inactive in the dehydration of long chain unsaturated beta-hydroxyacyl-ACP."];
  the trans-2 and cis-3 C10 products equilibrate on the enzyme
  [PMID:2195995 "Both E. coli acyl-ACP and recombinant acyl-ACP-I as cosubstrates with beta-OH 10:0, trans-2 10:1, or cis-3 10:1 yielded about equal amounts (37 mol%) of the two monoenes regardless of the initial substrate."].
- FabA also takes part in general elongation-cycle dehydration, so
  GO:0006633 is accepted alongside GO:0006636.
- PMID:4568811 (IMP, GO:0006633) is cached as title only; the row is accepted
  by deference to the curator, with independent support from PMID:8805534.
- Used as the FabA/FabB-route exemplar in
  `modules/bacterial_unsaturated_fatty_acid_biosynthesis.yaml`, beside the
  P. putida KT2440 ortholog Q88FC4.
