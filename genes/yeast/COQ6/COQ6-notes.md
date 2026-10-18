# COQ6 notes (P53318, YGR255C)

- FAD-dependent monooxygenase; mitochondrial import, peripheral matrix-side inner membrane [PMID:12721307 "Coq6p is a peripheral membrane protein that localizes to the matrix side of the inner mitochondrial membrane"].
- coq6 accumulates HHB [PMID:12721307; PMID:9266513].
- Exclusive C5-hydroxylase (HHB -> DHHB, EC 1.14.15.45), electrons from Yah1/Arh1; bypassed by vanillic acid / 3,4-diHB [PMID:21944752 "involved exclusively in the C5-hydroxylation reaction"].
- Also C4-deamination of pABA-derived HAB [PMID:26260787 "also deaminates position C4 in a reaction implicating molecular oxygen"].
- C1 decarboxylation + hydroxylation in eukaryotes is a single COQ4-dependent oxidative decarboxylation [PMID:38295803 "these two reactions occur in a single oxidative decarboxylation step catalyzed by COQ4"]. Hence UbiH-like C1 hydroxylase annotations to Coq6 (GO:0008681 ISA/RCA, GO:0120538 IEA via HAMAP MF_03193, YeastPathways EC 1.14.13.- reaction) are contradicted -> REMOVE.
- GO:0016712 (flavin donor) conflicts with GO:0106364 placement under GO:0016713 (iron-sulfur donor) -> MODIFY to GO:0106364.
- Review: 17 ACCEPT, 2 KEEP_AS_NON_CORE (FAD binding), 4 MODIFY, 5 REMOVE, 1 NEW (GO:0110142).
