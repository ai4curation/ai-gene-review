# ANKRD55 notes

- MS and autoimmune GWAS risk gene; the risk allele raises transcript levels [PMID:27183579]. GOA held only 22 HuRI IPIs, all REMOVE; none of the later functional partners (CCT subunits) is among them.
- Function (two independent 2025 mouse knockout studies, full text):
  - PMID:41090353: ANKRD55 binds CCT subunits and promotes CCT assembly, supporting immune-synapse microtubules and TCR signaling. Th1 and Th17 differentiation are impaired, and EAE is milder.
  - PMID:40932625: ANKRD55 is mitochondria-associated (IF and fractionation), supports respiration and restrains LKB1. TH17 IL-17 production is impaired; colitis protection.
- NEW terms:
  - GO:0005634 nucleus (IDA, human cells, PMID:27183579).
  - GO:0005739 mitochondrion (IDA, PMID:40932625; corrected from ISO in round 4, because the imaging was done on endogenous human ANKRD55 in human TH17 cells).
  - GO:2000321 positive regulation of Th17 differentiation (ISO, PMID:41090353).
  - The localization discrepancy (2016 nuclear report vs endogenous human ANKRD55 at the centrosome in Jurkat and at mitochondria in human TH17 cells) is stated in the rows and raised as a question; see the rounds below for the reframing.
- OpenCell has no ANKRD55 line. PAN-GO 0; PTHR24198:SF188 has no node reaching ANKRD55.

## Round 2 (reviewer, PR #4141): under-annotation

- Added NEW rows from the human Jurkat evidence in PMID:41090353:
  - GO:0051087 protein-folding chaperone binding (IPI; endogenous TCP1 co-IP); now the core MF.
  - GO:0005813 centrosome (IDA; colocalizes with TCP1 at the centrosome).
  - GO:0031334 positive regulation of protein-containing complex assembly (IMP; knockdown disrupts CCT assembly).
  - GO:0001771 immunological synapse formation (IMP; knockdown inhibits synapse formation).
  - GO:0050862 positive regulation of TCR signaling (IMP; overexpression enhances it).
- Also added GO:0045627 Th1 differentiation (ISO, same experiments as Th17) and GO:0032740 positive regulation of IL-17 production (ISO, PMID:40932625, effector output).
- The localization conflict is now framed as tagged construct (2016 nuclear) vs endogenous protein (centrosome, Jurkat), not species. The 2019 fractionation found nuclear plus organelle plus cytosol.
- PMID:31620119's tables include CCT4 and several mitochondrial proteins, corroborating both links. PMID:27183579 has an erratum of unknown content, so correctness is left unset.
