# prc (PA3257, Q9HYY3) review notes

No deep-research provider was available. Sources: UniProt record (TrEMBL), cached
abstracts of PMID:24373018 (no PMC id; full text not available) and PMID:24082078.
PubMed and Europe PMC searches failed on 2026-11-05 (server errors), so the MucA
degradation papers could not be retrieved; the MucA role is taken from the Seo and Darwin
abstract.

## Function

- Prc is a periplasmic tail-specific (C-terminal processing) serine protease, peptidase S41A,
  with Sec signal peptide 1-23 and a PDZ domain (UniProt; Pfam PF03572, NCBIfam TIGR00225).
- Prc degrades mutant MucA anti-sigma factor to promote mucoidy
  [PMID:24082078 "Prc degrades mutant forms of the anti-sigma factor MucA to promote mucoidy in some cystic fibrosis lung isolates."].
- In cell-surface signalling (CSS), Prc removes the periplasmic anti-sigma domain before RseP
  cleavage, releasing an active ECF sigma factor
  [PMID:24373018 "Prc, which removes the periplasmic anti-sigma domain, and RseP, which subsequently removes the transmembrane domain and thereby generates the ECF active transcriptional form."];
  the Iut work is in P. putida, and the abstract extends the role to classical CSS systems
  [PMID:24373018 "We furthermore demonstrate the role of these proteases in the regulation of classical CSS systems"].
  The abstract does not name the organism of the classical-CSS experiments; the Llamas laboratory
  works on P. aeruginosa CSS, and PseudoCAP's IMP row implies a P. aeruginosa prc mutant was used.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001279639 | GO:0007165 signal transduction | 3 | 58 (32 taxa) | GO:0007165 signal transduction, IMP, PMID:24373018 (PseudoCAP) | SOUND | Prc performs the site-1 cleavage of the anti-sigma factor that transmits the cell-surface signal to the ECF sigma factor, so it does a step of the pathway, not merely a mutant phenotype. Organism of the classical-CSS experiments not stated in the abstract. | B. subtilis CtpB O35002 (sound); P. aeruginosa CtpA Q9HU50 (WRONG, S. aureus reference; see PA5134 notes) | The IBD stands for Prc and CtpB themselves, but the node-level placement is questionable: see the GO_CENTRAL defect recorded once on PA5134 (SUSPECTED, CHECK). |

Cross-reference: PA5134 (Q9HU50) seeds the same node term with a wrong reference; the
node-level GO_CENTRAL defect is recorded on PA5134.

Defects recorded on this gene: PSEUDOCAP 0; GO_CENTRAL 0 (node defect on PA5134).
