# mucD (PA0766, G3XD20) notes

## Identity

- MucD (AlgY), HtrA/DegP-like serine protease (peptidase S1C, MEROPS S01.453), 474
  aa-class protein with a SignalP signal peptide (1-25), trypsin-like protease
  domain with charge-relay residues 114/144/217 (PIRSR) and two PDZ domains.
  Unreviewed TrEMBL entry; last gene of the algU-mucA-mucB-mucC-mucD operon.
- No deep-research provider was available; notes are from cached publications
  and PubMed searches.

## Literature

- Discovery: mucD encodes an HtrA homolog; inactivation causes mucoidy and
  heat/H2O2 sensitivity
  [PMID:8550474 "Inactivation of mucD on the PAO1 chromosome resulted in conversion to the mucoid phenotype."].
- PseudoCAP localisation seed (Hay et al. 2012, abstract only)
  [PMID:21713511 "Experimental evidence was provided for a periplasmic multiprotein complex composed of AlgX, AlgK, and the regulatory protein MucD."].
  A 2026 paper describes this evidence as affinity pull-downs
  [PMID:42766672 "Affinity pull-down studies further suggested that MucD could form a periplasmic complex with the terminal acetyltransferase AlgX and tetratricopeptide repeat (TPR)-rich scaffold protein AlgK [14]."].
- AlgX-MucD complex purified from detergent-solubilised membranes
  [PMID:16376476 "This data suggested a protein-protein interaction between AlgX and MucD (AlgY) with a 1:1 stoichiometry."].
  This paper has no protease assay, so it is a weak reference for the ISS
  serine-type endopeptidase row (the ISS itself rests on E. coli DegP).
- Regulated intramembrane proteolysis: in a mucD mutant MucA is degraded through
  MucP even without AlgW
  [PMID:21036998 "When mucD is inactivated, a high level of algU promoter activity was noted (Fig. 3A ), suggesting that the RIP activities are negatively regulated by MucD."].
  This is a genetic (mutant + reporter + Western) paper, so IMP rather than IDA,
  and it shows negative regulation of the AlgW/MucP signalling cascade, not a
  part of it.
- Direct biochemistry and structure (Jiang et al. 2026, full text): purified MucD
  degrades AlgK and AlgX; S217A is inactive; cryo-EM of the 12-mer and
  24-mer; resting 12-mer/active trimer equilibrium
  [PMID:42766672 "In contrast, isolated AlgK and AlgX were completely degraded by MucD within 2 h of incubation (Figs 1B and S1C–S1E)."];
  [PMID:42766672 "Collectively, these results suggest that MucD can alternatively regulate alginate production by directly degrading alginate biosynthetic proteins."];
  P1 preference for small hydrophobic residues
  [PMID:42766672 "In particular, short side-chain nonpolar residues, such as alanine, valine, and leucine, were enriched at P1 position and accounted for more than 50% of P1 residues in both AlgK and AlgX degradation products (Fig 2C)."].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002342204 | GO:0042597 periplasmic space | 1 (sole seed) | 5 (5 taxa) | GO:0042597 periplasmic space, IDA, PMID:21713511 (PseudoCAP) | SOUND | The abstract reports MucD in a periplasmic complex with AlgK and AlgX (affinity pull-downs). The paper is abstract-only here, so the exact fractionation could not be checked, but periplasmic location is independently supported by the SignalP signal peptide, the HtrA/DegP family, and the 2026 biochemical study, which treats MucD as periplasmic. The leaves (P. aeruginosa MucD, Neisseria HtrA Q4W577, Geobacter DegP Q74GB5, Bradyrhizobium Q89G41, Xanthomonas MucD Q8PB56) are all DegP-like proteases, for which periplasm is the standard location. The node term suits the clade. |

## Other PseudoCAP rows

- GO:0007165 signal transduction IDA PMID:21036998: the paper is genetic and shows
  that MucD negatively regulates MucA proteolysis. MODIFY to GO:0009968 negative
  regulation of signal transduction; PSEUDOCAP defect (term and evidence code).
- GO:0004252 ISS PMID:16376476 (with E. coli DegP): claim is correct (now
  directly shown in PMID:42766672), but the cited paper shows only an AlgX-MucD
  complex.

## Decisions summary

- ACCEPT: periplasmic space (IBA, IEA, IDA), serine-type endopeptidase activity
  (IEA, ISS), proteolysis (IEA).
- MODIFY: signal transduction (IDA) -> negative regulation of signal transduction.
- PSEUDOCAP defect (PROBABLE) on the signal transduction row.
