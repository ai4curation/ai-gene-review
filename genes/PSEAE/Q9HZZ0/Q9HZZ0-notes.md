# Q9HZZ0 (PA2854) curation notes

## 2026-11-17 — experimentally characterised OprI-anchoring enzyme (PTHR30582:SF24)

Q9HZZ0 is the *Pseudomonas aeruginosa* PAO1 gene PA2854, a Sec-exported
periplasmic YkuD-family L,D-transpeptidase (PANTHER PTHR30582:SF24). It is the
anchoring (tether-forming) exemplar of the module. Its activity is directly
demonstrated: PA2854 attaches the outer-membrane lipoprotein OprI to the
peptidoglycan sacculus in live cells [PMID:42100858, "We document that the gene
product of PA2854 is the catalyst that performs this transformation between the
cell wall and the outer-membrane lipoprotein OprI in live Pseudomonas
aeruginosa."], and the reaction was reconstituted in vitro with purified
components, pinning the acceptor residue [PMID:42100858, "Furthermore, we
reconstitute this reaction in vitro with the use of purified recombinant PA2854,
OprI, and synthetic samples of the cell-wall peptidoglycan, in each case
documenting the attachment of the side-chain ε-amino group of Lys83 of OprI to
the peptide stem of the peptidoglycan."]. The broader P. aeruginosa LDT survey
assigns the same OprI-anchoring role to this enzyme (LdtPae2) [PMID:37255442, "We
found that the three P. aeruginosa LDTs catalyze peptidoglycan cross-linking
(LdtPae1), the anchoring of lipoprotein OprI to the peptidoglycan (LdtPae2), and
the hydrolysis of the resulting peptidoglycan-OprI amide bond (LdtPae3)."].

## Strain identity: PAO1 PA2854 vs PA14 LdtPae2

Two strains are involved and must not be conflated. **PA2854 (Q9HZZ0) is the PAO1
locus**, the entry characterised by the in-vivo + in-vitro reconstitution study
(PMID:42100858). The **PA14** ortholog of the same anchoring enzyme is locus
**PA14_27180 (A0A0H2ZCT9)**, "LdtPae2" in the PA14-based survey (PMID:37255442).
They are orthologs of one enzyme across the two reference strains and both sit in
PTHR30582:SF24, alongside the *P. putida* KT2440 ortholog PP_2320 (Q88KH0).

## Action notes

- GO:0004180 carboxypeptidase (IEA): GO classifies the specific activity
  GO:0071972 (L,D-transpeptidase) under carboxypeptidase/peptidase, so the broad
  carboxypeptidase term is an entailed, uninformative ancestor → TOO_GENERAL.
- GO:0016740 transferase (IEA, from the IPR005490 domain signature): GO does NOT
  place GO:0071972 under transferase (it is modelled as a hydrolase/peptidase), so
  this is not an entailed ancestor; it is an uninformative domain-mapping
  over-annotation → MARK_AS_OVER_ANNOTATED (not TOO_GENERAL).
