# A0A0H2ZCT9 (PA14_27180 / LdtPae2) curation notes

## 2026-11-17 — PA14 OprI-anchoring enzyme (PTHR30582:SF24)

A0A0H2ZCT9 is *Pseudomonas aeruginosa* strain UCBPP-PA14 locus PA14_27180,
annotated erfK, a Sec-exported periplasmic YkuD-family L,D-transpeptidase
(PANTHER PTHR30582:SF24). In the PA14-based survey of the three P. aeruginosa
L,D-transpeptidases it is "LdtPae2", the enzyme that anchors OprI to
peptidoglycan [PMID:37255442, "We found that the three P. aeruginosa LDTs
catalyze peptidoglycan cross-linking (LdtPae1), the anchoring of lipoprotein OprI
to the peptidoglycan (LdtPae2), and the hydrolysis of the resulting
peptidoglycan-OprI amide bond (LdtPae3)."].

## Strain/locus identity check

- PA14_27180 (A0A0H2ZCT9) = **PA14** LdtPae2 (this entry).
- PA2854 (Q9HZZ0) = the orthologous **PAO1** locus, characterised by the in-vivo
  and in-vitro reconstitution study PMID:42100858.
These are orthologs of one anchoring enzyme across the two P. aeruginosa reference
strains; both are PTHR30582:SF24, with the *P. putida* KT2440 ortholog PP_2320
(Q88KH0). The locus→LdtPae mapping (PA14_27180 = LdtPae2, PA14_15840 = LdtPae3)
is used to connect the all-IEA UniProt entries to the functional assignments in
PMID:37255442; LdtPae3 (A0A0H2ZF55) is the paralogous hydrolase in the other
family (PTHR36699:SF1).

## Action notes

All nine existing annotations are IEA. The anchoring (GO:0071972 transpeptidase,
GO:0018104 cross-linking) rows are accepted and corroborated by the direct
experimental characterisation of LdtPae2. GO:0004180 carboxypeptidase is
TOO_GENERAL (GO:0071972 is a descendant of GO:0004180); GO:0016740 transferase is
MARK_AS_OVER_ANNOTATED (GO models the L,D-transpeptidase activity as a peptidase,
not a transferase, so the domain-mapping root term is uninformative rather than an
entailed ancestor).
