# phzS (PA4217, Q9HWG9) notes

## Identity

- 5-methylphenazine-1-carboxylate 1-monooxygenase, EC 1.14.13.218, 402 aa,
  FAD-dependent class A aromatic hydroxylase (Pfam FAD_binding_3, PANTHER
  PTHR13789:SF268). PE 1; crystal structures 2RGJ and 3C96.
- UniProt: [file:PSEAE/phzS/phzS-uniprot.txt "Catalyzes the oxidative decarboxylation of 5-methylphenazine-1-carboxylate (5-methyl-PCA) to pyocyanine"] (ECO:0000269, PMID:17253782); PCA is a poor alternative substrate, giving 1-hydroxyphenazine.
- Cofactor FAD (PMID:18416536 and structures); monomer in solution.

## Pathway

- PCA (made by phzA1-G1 / phzA2-G2) is converted to pyocyanin by PhzM (N5-methylation) then PhzS (hydroxylative decarboxylation).
- [PMID:11591691 "Expression of phzS alone in Escherichia coli or in enzymes, pyocyanin-nonproducing P. fluorescens resulted in conversion of PCA to 1-hydroxyphenazine. P. aeruginosa with insertionally inactivated phzM or phzS developed pyocyanin-deficient phenotypes."] (abstract only)
- [PMID:17253782 "1-HP was formed in an NADH dependant manner with an apparent k cat of 0.03s −1 in our assay."]
- [PMID:17253782 "Pyocyanin formation required PhzM, PhzS, PCA, SAM, oxygen, and NADH consistent with a methyl transfer reaction and a flavin-mediated hydroxylation."]
- [PMID:17253782 "Isolation of either PhzM or PhzS inside a dialysis membrane results in no pyocyanin formation suggesting that an at least transient physical interaction between PhzM and PhzS is required in order to activate production of pyocyanin."] No stable complex was seen by light scattering; PhzS is a monomer.
- [PMID:18416536 "The structure reveals that PhzS is a member of the family of aromatic hydroxylases characterized by p-hydroxybenzoate hydroxylase."] (abstract only)

## The PseudoCAP seed paper (PMID:17012792)

Full text cached. Gohain et al. 2006 is a crystallization communication:
cloning, His-tag purification, crystallization and X-ray data collection. It
calls PhzS an FAD-dependent monooxygenase on the basis of earlier genetics and
fold recognition ("Predictions from the fold-recognition program 3 DPSSM ...
indicate that it possesses significant fold similarity to FAD-dependent
oxidoreductases"), and notes the crystals are yellow from bound FAD. No
enzyme activity is measured. So the IDA "monooxygenase activity" row is not
supported by that paper; the claim itself is true on PMID:17253782 (direct
NADH-dependent hydroxylation by purified PhzS).

## GOA rows and decisions

- GO:0004497 monooxygenase activity, IBA (PTN002492679) and IDA (PMID:17012792): true but general; MODIFY to GO:0102169 (is_a descendant via GO:0016709). IDA row gets a PSEUDOCAP WRONG_REFERENCE defect.
- GO:0016709 IEA (ARBA): true but general; MODIFY to GO:0102169.
- GO:0102169 EXP (PMID:17253782) and IEA (RHEA/EC): ACCEPT, core.
- GO:0071949 FAD binding IEA: KEEP_AS_NON_CORE (cofactor; structurally confirmed).
- GO:0005515 protein binding IPI (PhzM): REMOVE per protein-binding policy; the PhzM-PhzS interaction is inferred from dialysis-separation assays and is transient, not a characterised binding function.
- NEW: GO:0106220 pyocyanine biosynthetic process. PhzS itself catalyses the last step (it does the work), PhzM already carries this term by IDA from the same paper, and UniProt's curated PATHWAY line says pyocyanine biosynthesis (ECO:0000269). Comparator: phzM (Q9HWH2) carries GO:0106220 IDA PMID:17253782; PhzS lacks it only because no curator added it.

## PseudoCAP IBA-seed assessment

Tree analysis: `phzS-bioinformatics/RESULTS.md`.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002492679 | GO:0004497 monooxygenase activity | 1 (sole seed) | 104 (19 taxa); 3507 GOA rows | GO:0004497 monooxygenase activity, IDA, PMID:17012792 (PseudoCAP); also GO:0102169 EXP PMID:17253782 (UniProt) | SOUND | The claim is true: purified PhzS hydroxylates PCA NADH-dependently and, with PhzM, makes pyocyanin (PMID:17253782); it is an FAD class A aromatic hydroxylase (PMID:18416536). The cited paper is only a crystallization note with no assay, so the PseudoCAP row should be re-keyed to PMID:17253782, but the UniProt EXP row (a descendant term) independently supports the node. The node is the LUCA root of PTHR13789 (fungal salicylate-hydroxylase-like, algal zeaxanthin-epoxidase-like and bacterial FAD monooxygenases), so the generic GO:0004497 is the right level; GO:0102169 would be wrong for the clade. One leaf, Synechocystis chlP (Q55087, geranylgeranyl reductase, now PTHR42685 in UniProt), receives the IBA and is a likely misplaced leaf. |

## Open questions

- Is the PhzM-PhzS interaction a stable complex under turnover conditions, or substrate channelling via a transient encounter?
- Should Synechocystis chlP (Q55087) be removed from PTHR13789 or given a NOT monooxygenase annotation?
