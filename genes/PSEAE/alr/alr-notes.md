# alr (PA4930, Q9HUN4) review notes

No deep-research API was available. Manual research on 2026-11-05: cached
abstracts (PMID:20971724, PMID:10977898, PMID:29964014, PMID:14674749), a Europe
PMC title search for "alanine racemase" AND "Pseudomonas aeruginosa" (PubMed MCP
and NCBI E-utilities returned server errors), UniProt (reviewed), and QuickGO for
other seeds.

## Biology

- P. aeruginosa has two alanine racemases, biosynthetic Alr (PA4930) and
  catabolic DadX (PA5302). Both were cloned, shown to complement E. coli
  D-alanine auxotrophs, purified and characterised [PMID:10977898 "The dadX(PA)
  and alr(PA) genes have been sequenced, overexpressed, and their activity was
  demonstrated by complementing d-alanine auxotrophs of Escherichia coli."].
  UniProt records Km 1.1 mM for both enantiomers and Vmax 40-44 umol/min/mg from
  this paper.
- Crystal structure of Alr (PDB 6A2F): conserved homodimer, guest D-lysine in the
  active site [PMID:29964014 "Here we report the crystal structure of
  biosynthetic alanine racemase (Alr) from a pathogenic bacteria Pseudomonas
  aeruginosa PAO1."]. (PMID:14674749 is the DadX structure, not Alr.)
- Monomer-dimer equilibrium and Vmax were compared for seven bacterial alanine
  racemases including P. aeruginosa enzymes [PMID:20971724 "In both biosynthetic
  and catabolic alanine racemases, association constants for dimerization were
  high for the enzymes with high V(max) values."].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000775508 | GO:0008784 alanine racemase activity | 8 | 51 (33 taxa) | GO:0008784, IDA, PMID:20971724 (PseudoCAP) | SOUND | Abstract reports Vmax for the P. aeruginosa racemases studied; independently, purified Alr was characterised (PMID:10977898) and UniProt has ECO:0000269 kinetics. | P. aeruginosa DadX Q9HTQ2, E. coli Alr P0A6B4 and DadX P29012, M. tuberculosis Alr P9WQA9, V. cholerae Q9KUY6 and BsrV Q9KSE5, S. pombe SPCC965.08c | Yes |

Shared node with dadX (PA5302, reviewed in parallel): no node-level defect is
needed. The alanine racemase term suits the clade (BsrV is a broad-specificity
racemase that still racemises alanine). The PseudoCAP seed is sound, so no
PSEUDOCAP or GO_CENTRAL defect is recorded here, and there is none for dadX to
cross-reference. The dadX review (genes/PSEAE/dadX) reached the same verdict:
its seed (IDA, PMID:10977898) is SOUND with no node defect.

## Action summary

ACCEPT: GO:0008784 (IBA, IDA, IEA), GO:0030632 (IBA, IEA).
KEEP_AS_NON_CORE: GO:0005829 (IBA), GO:0030170 (IBA, IEA), GO:0009252 (IEA).
TOO_GENERAL: GO:0003824 (IEA).
