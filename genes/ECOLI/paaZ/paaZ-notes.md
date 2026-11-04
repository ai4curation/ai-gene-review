# paaZ (P77455) notes — E. coli K-12 bifunctional oxepin-CoA hydrolase / 3-oxo-5,6-dehydrosuberyl-CoA semialdehyde dehydrogenase

## Deep research
- 2026-10-23: `just deep-research-falcon ECOLI paaZ` failed ("Exception: Failed to authenticate"). No deep-research file.

## Function
- Fusion protein: N-terminal NADP+-dependent ALDH domain + C-terminal MaoC-like (R)-specific hydratase (hotdog) domain.
  The hydratase domain hydrolytically opens the oxepin-CoA ring to a reactive semialdehyde; the ALDH domain oxidizes it
  to 3-oxo-5,6-dehydrosuberyl-CoA [PMID:21296885 abstract; PMID:20660314 "PaaZ thus functioned as an oxepin-CoA hydrolase/ 3-oxo-5,6-dehydrosuberyl-CoA semialdehyde dehydrogenase"].
- Without ALDH activity (mutant or no NADP+), the semialdehyde cyclizes to a dead-end product, so the intermediate is
  channelled [PMID:31511507].
- CryoEM (PDB 6JQL-6JQO): three domain-swapped dimers forming a trilobed hexamer; CoA electrostatic pivoting
  proposed for intermediate transfer [PMID:31511507].
- MaoC (= PaaZ; old name) shows enoyl-CoA hydratase activity on crotonyl-CoA in vitro and supports PHA synthesis in
  engineered fadB strains [PMID:12949091]; side activity, not the physiological role.
- Disruption converts phenylacetate to 2-hydroxyphenylacetate [PMID:9748275 via UniProt]; deletion mutant cannot grow on PA [PMID:12846838].

## GOA review summary
- Ring cleavage is hydrolysis of an enol-ether C-O bond (EC 3.3.2.12, ether hydrolases): GO:0016803 ACCEPT (core).
- GO:0016823 (C-C bond hydrolase in ketonic substances): no C-C bond is hydrolysed -> MODIFY to GO:0016803.
- GO:0016726 (acting on CH/CH2) wrong sub-branch for an aldehyde oxidation (EC 1.2.1.91) -> MODIFY to GO:0033721.
- GO:0016491 IBA/IEA -> MODIFY to GO:0033721.
- GO:0004300 (crotonyl-CoA, in vitro) KEEP_AS_NON_CORE; GO:0042802 KEEP_AS_NON_CORE; GO:0010124 x3 ACCEPT.
