# glmR (PA5550, Q9HT24) review notes

DeoR-family transcriptional repressor, 257 aa: N-terminal HTH DeoR-type domain
(Pfam HTH_DeoR, residues 7-62) and C-terminal DeoR sensor domain (Pfam DeoRC,
NagB/RpiA-like fold, the effector-binding module of the family). PANTHER
PTHR30363 (SrlR-related). Unreviewed UniProt entry. Located between glmS
(PA5549) and glmU (PA5552).

## Literature (no deep-research provider available; own reading)

- Ramos-Aires et al. 2004 (abstract only; PMC353099 listed but the PubMed MCP
  returned no full text on 2026-11-05). A Tn501 insertion in PA5550 (mutant
  19A) gave broad antibiotic hypersusceptibility and a pleiotropic phenotype
  [PMID:14982774 "Light microscopy of the mutant strain revealed abnormal
  morphology characterized by large, filamentous cells."; "The drug
  supersusceptibility of 19A was accompanied by loss of motility, reduced
  resistance to osmotic and heat shock stress, and impaired growth at low
  temperatures."]. GlmR represses glmS [PMID:14982774 "We showed that GlmR
  represses the transcription of the adjacent glmS homologue (PA5549) in P.
  aeruginosa, possibly affecting the pool of precursors for peptidoglycan and
  LPS synthesis."].
- The repression of glmS is the only target-level finding. Effects on cell
  shape, motility and stress tolerance are consequences of a cell-envelope
  defect in a pleiotropic mutant, not demonstrated regulatory roles of GlmR.
- No other GlmR (PA5550) papers found; PubMed MCP search returned API errors.

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000769142 | GO:0006355 regulation of DNA-templated transcription | 8 | 104 (29 taxa) | GO:0045892, IMP, PMID:14982774 (PseudoCAP) | SOUND | Abstract states GlmR represses glmS transcription; DeoR-family HTH domain agrees. Descendant term supports the node term. | E. coli GlpR P0ACL0 (IDA), SrlR P15082 (IDA), DeoR P0ACK5 (IMP), AgaR P0ACK2 (IMP), YciT P76034 (IMP), CsqR P32144 (IEP), L. lactis LacR P0A0Q0 (IMP) | Yes; several E. coli IDA/IMP seeds |

No GO_CENTRAL defect.

### Other PseudoCAP rows from the same paper (not seeds)

| term | verdict | defect |
|---|---|---|
| GO:0045724 positive regulation of cilium assembly | WRONG | PSEUDOCAP WRONG_TERM, CONFIRMED: a cilium is by GO definition a eukaryotic organelle, so the term cannot apply to a bacterium. The underlying observation is loss of motility of a pleiotropic mutant. |
| GO:2000147 positive regulation of cell motility | INDIRECT-PHENOTYPE | PSEUDOCAP WRONG_TERM, PROBABLE: the abstract states loss of motility alongside filamentation and stress sensitivity, i.e. a general envelope defect; no flagellar target is reported. |
| GO:0032885 regulation of polysaccharide biosynthetic process | INDIRECT-PHENOTYPE | PSEUDOCAP WRONG_TERM, SUSPECTED (CHECK): the abstract only says glmS repression is "possibly affecting" precursor pools; the full text could contain measurements. |
