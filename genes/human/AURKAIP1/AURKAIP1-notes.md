# AURKAIP1 notes

## 2026-10-05 review (PAINT, affinage)

- AURKAIP1 = mitoribosome SSU protein mS38/MRPS38 [PMID:23908630 "Furthermore, we have demonstrated the essential roles of CHCHD1, AURKAIP1, and CRIF1in mitochondrial protein synthesis by siRNA knock-down studies, which had significant effects on the expression of mitochondrially encoded proteins."].
- Added NEW GO:0003735 structural constituent of ribosome (IDA); comparators MRPS34, MRPS2 and MRPS5 carry it.
- The Aurora-A degradation role (PMID:12244051, an overexpression study), the nuclear rows and positive regulation of proteolysis are kept as non-core. The AURKA IPI was changed to protein kinase binding.
- **Affinage symbol collision (not flagged by its gates):** the PKAc/NF-kappaB scaffold finding ("AKIP1") belongs to a different gene, AKIP1. It is not used.

## 2026-10-05 revision (reviewer round 1)

- Aurora-A axis: there are two 2007 mechanistic follow-ups [PMID:17125467 "In an attempt to investigate the mechanism of AURKAIP1-mediated Aurora-A degradation, we report here that AURKAIP1 targets Aurora-A for degradation in a proteasome-dependent but Ub (ubiquitin)-independent manner."] and the antizyme1 paper (PMID:17452972). Both use ectopic expression, so GO:0045862 stays non-core.
- Yeast mS38 is COX-selective [PMID:30968120 "Additionally, the absence of mS38 preferentially disturbs translation initiation of COX1, COX2, and COX3 mRNAs, without affecting the levels of mRNA-specific translational activators."]. The human knockdown is not [PMID:23908630 "However, we observed an overall reduction in the expression of all 13 mitochondrially encoded proteins in AURKAIP1 knock-down cell lines (Figure 4C), suggesting that this protein plays a general role in mitochondrial translation that is not limited to the synthesis of cytochrome oxidase."]. The knowledge gap is framed accordingly, and GO:0045182 is not asserted.
- Affinage collision: both PMID:21556136 and PMID:29677171 are AKIP1 (C11orf17, BCA3), not AURKAIP1.
- Current UniProt name: bS22m (formerly mS38); the family is also found in Actinomycetota ribosomes.
