# cif (PA2934, Q9HZR3) — research notes

## Identity

- UniProt Q9HZR3 (unreviewed), 319 aa, gene `cif`, ordered locus `PA2934`,
  *P. aeruginosa* PAO1 (NCBITaxon:208964). Matches the worklist entry (rank 29).
- SubName "CFTR inhibitory factor, Cif"; no curated FUNCTION or CATALYTIC
  ACTIVITY block in the UniProt entry, protein existence level 4 (Predicted).
- Architecture: SignalP signal peptide 1-24 with mature chain 25-319, one
  AB hydrolase-1 domain (Pfam PF12697, 57-305), alpha/beta hydrolase fold
  (Gene3D 3.40.50.1820, SSF53474), ESTHER entry `pseae-PA2934`
  (CFTR-inhibitory-factor_Cif), PANTHER PTHR43329 "EPOXIDE HYDROLASE".
- The signal peptide and the ESTHER/secretion data fit a secreted protein; Cif
  is found in outer-membrane vesicles
  [PMID:17502391, "is a secreted protein and is found associated with outer membrane-derived"].

## Function

### Epoxide hydrolase (direct, purified protein)

Cif was named from its effect on host CFTR, but it is an enzyme in its own
right, and the enzymology is direct and on purified protein:

- Catalytic triad: [PMID:20118260, "Cif has a catalytic triad consisting of residues Asp129, His297, and Glu153"],
  with [PMID:20118260, "Asp129 serves as the nucleophile responsible for the initial attack on a carbon of the substrate epoxide ring"].
- Activity confirmed against two classical epoxide substrates:
  [PMID:20118260, "detailed enzymatic analysis confirms that Cif catalyzes the hydrolysis of epoxide compounds, with specific activity against both epibromohydrin and cis"],
  with [PMID:20118260, "We measured a specific activity of EBH hydrolysis of 0.25 U/mg (1 U = 1 μmol substrate hydrolyzed per minute) for Cif-WT."].
- Specificity is narrow and *not* that of the neighbouring alpha/beta hydrolase
  classes: [PMID:20118260, "Cif does not exhibit activity as either a haloacetate dehalogenase or a haloalkane dehalogenase"].
  This is a tested negative, so the epoxide-hydrolase assignment within the
  Asp-nucleophile alpha/beta hydrolases is not a default.
- Earlier work had already seen the activity and shown it is required for the
  host effect: [PMID:17502391, "epoxide hydrolase activity in vitro and requires a highly conserved histidine"].
- Cif is a homodimer in solution (gel filtration Mr ~60 kDa vs 34 kDa monomer).

### Host CFTR / chloride secretion

- Cif is the secreted factor responsible for the filtrate activity on CFTR, and
  purified Cif is sufficient:
  [PMID:17502391, "sufficient to mediate the reduction in apical membrane expression of CFTR and a"] and
  [PMID:17502391, "concomitant reduction in CFTR-mediated Cl(-) ion secretion. Cif demonstrates"].
- Mechanism: [PMID:21455491, "Cif redirected endocytosed CFTR from recycling endosomes to lysosomes by"]
  [PMID:21455491, "stabilizing an inhibitory effect of G3BP1 on the deubiquitinating enzyme (DUB),"]
  [PMID:21455491, "USP10, thereby reducing USP10-mediated deubiquitination of CFTR and increasing"]
  [PMID:21455491, "the degradation of CFTR in lysosomes. This is the first example of a bacterial"].
- The catalytic histidine is needed for the host effect, and the structure paper
  concludes the host effect needs turnover of a real substrate:
  [PMID:20118260, "Cif's effect on host-cell CFTR expression requires the hydrolysis of an extended endogenous epoxide substrate"].
  The physiological epoxide is still unidentified.

### Note on the reference behind the GOA chloride-transport row

The PseudoCAP `negative regulation of chloride transport` row cites
PMID:16236828 (Swiatecka-Urban et al. 2006). That paper precedes the
identification of Cif and works with unfractionated secretions:
[PMID:16236828, "report herein that a cell-free filtrate of P. aeruginosa reduced CFTR-mediated"]
(the abstract names no protein). The claim is nevertheless correct for this gene,
established with purified Cif two years later [PMID:17502391]. Recorded as a
`PSEUDOCAP` `WRONG_REFERENCE` / `CHECK` defect, not as a reason to drop the row.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002458043 | GO:0004301 epoxide hydrolase activity | 1 (sole seed) | 38 (15 taxa) | GO:0004301 \| IDA \| PMID:20118260 \| PseudoCAP | SOUND | The seed is direct enzymology on purified recombinant Cif: a 1.8 Å structure showing the complete EH catalytic triad, measured turnover of two standard epoxide substrates (0.25 U/mg on epibromohydrin; cis-stilbene oxide), and tested absence of the two competing alpha/beta hydrolase activities (haloacetate and haloalkane dehalogenase). The activity is independently reproduced in [PMID:17502391]. It is a molecular-function claim about the protein itself, not a mutant phenotype, and it is exactly the term the assay supports. A 38-leaf, 15-taxon node of Cif-like bacterial epoxide hydrolases is an appropriate scope for it. |
| PTN000863140 | GO:0016787 hydrolase activity | 13 | 791 (88 taxa) | GO:0004301 \| IDA \| PMID:20118260 \| PseudoCAP | SOUND | Here the PseudoCAP row is one of 13 seeds, alongside characterised mammalian epoxide hydrolases (human EPHX2 P34913, mouse and rat entries, zebrafish, *M. tuberculosis* P9WMR9 and others). An epoxide hydrolase is a hydrolase, so the seed entails the node term; the question the protocol asks is whether the term suits the clade. It does, and deliberately so: PTHR43329-type alpha/beta hydrolases with an Asp nucleophile include epoxide hydrolases, haloacetate dehalogenases and haloalkane dehalogenases, and Cif itself shows that family membership does not predict which — it has EH activity and demonstrably lacks both dehalogenase activities. Across 791 leaves in 88 taxa the generic parent is the cautious, defensible choice; propagating `epoxide hydrolase activity` at this depth would be the error. No defect. |

## Open questions

- What is the endogenous epoxide substrate whose hydrolysis mediates the CFTR
  effect? The structure paper infers an "extended" lipid-like epoxide but does
  not identify it.
- Does Cif have a function in *P. aeruginosa*'s own physiology (detoxification
  of host- or environment-derived epoxides), independent of the host CFTR
  effect, and is that the selected function in environmental isolates?
