# mucB (PA0764, P38108) notes

## Identity

- Sigma factor AlgU regulatory protein MucB (AlgN), RseB family, 316 aa with a
  Sec signal peptide (1-21). Encoded in the algU-mucA-mucB-mucC-mucD operon.
  UniProt: "Negative regulator of the sigma factor AlgU." (Swiss-Prot, P38108).
- No deep-research provider was available; notes below are from cached
  publications and PubMed searches.

## Literature

- Genetics: chromosomal insertional inactivation of mucB in PAO makes the strain
  mucoid with strong algD activation
  [PMID:8412698 "Insertional inactivation of mucB on the chromosome of the standard genetic strain PAO resulted in mucoid phenotype, and in a strong transcriptional activation of algD."].
- PseudoCAP seed paper (Mathee et al. 1997; abstract only, full text PMC179169 not
  retrievable through the PMC tool): an algT clone kept PAO1 nonmucoid only while
  the coupled mucB was intact
  [PMID:9171421 "However, the bacterial cells remained nonmucoid if the transcriptionally coupled mucB on the clone remained intact."];
  MucB localised to the periplasm by Western blot and phoA fusions
  [PMID:9171421 "By Western blotting and phoA fusion analyses, the MucB antagonist of sigma22 was found to localize to the periplasm of the cell."].
- Mechanism: purified MucB binds the MucA periplasmic domain tightly and blocks
  its cleavage by the site-1 protease AlgW (DegS homolog)
  [PMID:19298369 "We demonstrate that tight binding of MucB to MucA strongly inhibits this cleavage."].
  MucB is the RseB homolog of E. coli
  [PMID:19298369 "RseB (a MucB homolog), which is a protein that inhibits DegS cleavage of RseA"].
- In vivo: MucB is part of the MucA sigma-sequestration complex
  [PMID:19226327 "Here we showed that MucB, encoded by the algT-mucABCD operon, interacts with MucA in the sigma-sequestration complex."].
- Structures (6IN8 MucB alone, 6IN9 MucA-peri/MucB)
  [PMID:31297938 "MucB binds MucA in the periplasm and inhibits proteolysis of MucA and subsequent release of AlgU."];
  a hydrophobic cavity senses lipids that trigger MucA-MucB dissociation
  [PMID:32747658 "These results provide evidence that the hydrophobic cavity of MucB is a primary site for sensing lipid molecules"].

## Interpretation

MucB is a periplasmic co-antagonist of the ECF sigma factor AlgU: it binds the
anti-sigma factor MucA (MF: antisigma factor binding, GO:0045152) and shields it
from regulated intramembrane proteolysis. Alginate (polysaccharide) overproduction
in mucB mutants is the AlgU-regulon output in P. aeruginosa; it is a true
regulatory role of this gene, but it is not the conserved family function. In
E. coli and other enterobacteria, RseB controls the sigmaE envelope-stress
response, not polysaccharide synthesis.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002215378 | GO:0032885 regulation of polysaccharide biosynthetic process | 1 (sole seed) | 7 (7 taxa) | GO:0032885 regulation of polysaccharide biosynthetic process, IMP, PMID:9171421 (PseudoCAP) | OVER-SPECIFIC | The seed is acceptable for MucB itself: mucB loss gives alginate overproduction because AlgU directly drives algD. But alginate control is a Pseudomonas-specific output of the AlgU regulon, not the RseB-family function. The node's other six leaves are enterobacterial/Vibrio/Shewanella/Haemophilus RseB orthologs (E. coli P0AFX9, Salmonella H9L461, Yersinia A0A2U2GWS2, Haemophilus P44792, Shewanella Q8EH85, Vibrio Q9KPA8) that regulate sigmaE, with no evidence of polysaccharide-synthesis control. The node term should not propagate; antisigma factor binding (already at this node, seeded by E. coli RseB) is the conserved claim. |

Node leaves were taken from the PAINT leaf GAF (`.cache/paint/leaf.gaf.gz`).

## Decisions summary

- MODIFY: protein binding IPI x2 -> antisigma factor binding (GO:0045152).
- ACCEPT: antisigma factor binding (IBA), outer membrane-bounded periplasmic space
  (IBA), periplasmic space (IEA).
- KEEP_AS_NON_CORE: regulation of polysaccharide biosynthetic process (IMP, IBA).
- GO_CENTRAL defect (PROBABLE): remove/restrict the GO:0032885 IBD at PTN002215378.
- No PSEUDOCAP defect.
