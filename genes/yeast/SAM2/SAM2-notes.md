# SAM2 (YDR502C) notes

## Identity
- S-adenosylmethionine synthase 2 (AdoMet synthase 2, MAT2), EC 2.5.1.6; synonym ETH2; paralog of SAM1 (P10659) [UniProt:P19358].
- Catalytic activity: L-methionine + ATP + H2O = S-adenosyl-L-methionine + phosphate + diphosphate (RHEA:21080) [UniProt:P19358 "FUNCTION: Catalyzes the formation of S-adenosylmethionine from"].
- Mg2+ and K+ cofactors by similarity to E. coli MetK [UniProt:P19358].
- Family: AdoMet synthase family (PANTHER PTHR11964; Pfam PF00438/PF02772/PF02773) [UniProt:P19358].
- Subunit: heterotetramer; IntAct records 5 experiments for Sam1-Sam2 interaction [UniProt:P19358 "P19358; P10659: SAM1; NbExp=5; IntAct=EBI-10795, EBI-10789;"].

## Enzyme activity evidence
- Recombinant SAM2 expressed in Pichia is active [PMID:18078345 "The specific activity of the purified synthetase was 23.84 U/mg."].
- sam1 sam2 double mutant cannot make SAM from methionine [PMID:17426150 "sam1(-) sam2(-) mutants, in which the conversion of methionine to S-adenosylmethionine is blocked"].

## Complexes / regulation
- Sam1 and Sam2 are components of the SESAME complex with Pyk1, Ser33, Shm2 and Acs1; SAM made by SESAME is used by Set1 H3K4 methylation [PMID:26527276 "SESAME interacts with the Set1 H3K4 methyltransferase complex, which requires SAM synthesized from SESAME"].
- Sam1/Sam2 heteromerization is one of many paralog heteromers in yeast [PMID:31454312 "heteromerization is frequent among duplicated homomers and correlates with functional similarity between paralogs"].
- Found in stress granule core proteome by HDA (PMID:26777405); SAM2 not named in the cached text, so this rests on supplementary data.

## Pathway context
- YeastPathways places SAM2 in SAM biosynthesis (SAM-PWY), SAM cycle (PWY-5041), and superpathways of sulfur amino acid biosynthesis (PWY-821-1) and methionine salvage (PWY3O-351). SAM synthesis is not an amino acid biosynthetic step and SAM2 does not regenerate methionine; the latter two BP assignments are superpathway inheritance.
- GO:0006556 S-adenosylmethionine biosynthetic process is NOT a descendant of GO:0000097 sulfur amino acid biosynthetic process (checked with runoak ancestors).
