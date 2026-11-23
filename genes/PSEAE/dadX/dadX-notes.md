# dadX (PA5302, Q9HTQ2) notes

Sources read on 2026-11-05: UniProt Q9HTQ2 (ALR2_PSEAE), the GOA file, the cached
abstract of PMID:10977898 (no full text in cache). PubMed MCP searches for further
dadX papers ("dadX Pseudomonas aeruginosa alanine", "alanine catabolism Pseudomonas
aeruginosa dadA dadX") returned no hits or an API error. No deep-research provider
file was generated (no keys).

## Biology

- P. aeruginosa PAO1 has two alanine racemases, Alr (PA4930) and DadX (PA5302). Both
  were cloned, overexpressed, purified and characterised biochemically, and both
  complement E. coli D-alanine auxotrophs
  [PMID:10977898 "The dadX(PA) and alr(PA) genes have been sequenced, overexpressed, and their activity was demonstrated by complementing d-alanine auxotrophs of Escherichia coli."];
  [PMID:10977898 "Both gene products were purified to electrophoretic homogeneity, the enzymes were characterized biochemically"].
- UniProt (curated, ECO:0000269 PubMed:10977898): DadX racemises L-alanine to
  D-alanine, which DadA oxidises to pyruvate; Km 1.4 mM for each enantiomer,
  Vmax 134-155 umol/min/mg [file:PSEAE/dadX/dadX-uniprot.txt "Isomerizes L-alanine to D-alanine which is then oxidized to"].
  The dadX name and the dadA partnership place it in the catabolic (L-alanine
  utilisation) route, while Alr is the constitutive biosynthetic racemase.
- Crystal structure (PMID:14674749, not cached): homodimer, PLP Schiff base at Lys33,
  carbamylated Lys122 (UniProt CC COFACTOR / SUBUNIT, ECO:0000269).
- Family: HAMAP MF_01201, TIGR00492, PANTHER PTHR30511:SF0 (catabolic-related
  subfamily).

## Annotation judgements

- GO:0008784 alanine racemase activity: core, IDA on purified enzyme.
- GO:0030170 PLP binding: supported by the crystal structure (UniProt FT, ECO:0000269).
- GO:0030632 D-alanine biosynthetic process (IBA from PTN001253738, seeded by E. coli
  and M. tuberculosis Alr; IEA): DadX does make D-alanine and can supply it to an E.
  coli auxotroph, but its physiological role is L-alanine catabolism. Kept as non-core.
- Proposed NEW GO:0042853 L-alanine catabolic process (IC, from the curated UniProt
  function statement): DadX performs the racemisation step of the DadX-DadA route.

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000775508 | GO:0008784 alanine racemase activity | 8 | 51 (33 taxa) | GO:0008784, IDA, PMID:10977898 (PseudoCAP) | SOUND | The abstract states both P. aeruginosa racemases were purified and characterised biochemically and complement D-alanine auxotrophs; UniProt records kinetics for DadX from this paper. | E. coli Alr P0A6B4 (EcoCyc IDA PMID:18434499), E. coli DadX P29012 (EcoCyc IDA PMID:1527514), M. tuberculosis Alr P9WQA9 (IDA PMID:11267762), P. aeruginosa Alr Q9HUN4 (PseudoCAP; reviewed in parallel), V. cholerae Q9KUY6 and Q9KSE5, S. pombe SPCC965.08c | Yes; several independent IDA seeds |

The node term is the defining activity of the alanine racemase family and suits the
clade. No PSEUDOCAP defect on the dadX seed row and no GO_CENTRAL defect on
PTN000775508. Alr (Q9HUN4) shares this node and is being reviewed in parallel; any
node-level defect belongs on alr, and none is warranted from the dadX side.
