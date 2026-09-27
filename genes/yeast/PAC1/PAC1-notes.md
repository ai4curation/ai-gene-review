# PAC1 (S. cerevisiae, P39946) review notes

## 2026-09-27 initial review (claude-code)

Context: yeast LIS1 ortholog, comparative member of `modules/nucleokinesis.yaml` (human PAFAH1B1 reviewed).

Key evidence
- Pac1 in dynein/dynactin pathway; required for MT sliding along bud cortex and spindle movement; at MT plus ends; targets dynein to plus ends [PMID:12566428 "Our results suggest that Pac1 targets dynein to microtubule tips, which is necessary for sliding of microtubules along the bud cortex."]. Commentary [PMID:12566423].
- Ndl1 needed for efficient Pac1 plus-end targeting; Pac1-Ndl1 co-IP [PMID:15965467].
- Lis1 binds motor at AAA ring/stalk interface; "clutch" [PMID:22939623]; structure and yeast mutants [PMID:34994688 "In yeast, Lis1 is required for dynein’s localization to SPBs, microtubule plus ends, and the cell cortex"].
- Stabilizes uninhibited dynein [PMID:32341548]; Num1 relieves Pac1-mediated inhibition at cortex [PMID:26483554].
- Motor domain targets dynein to plus ends in Pac1-dependent manner [PMID:19185494].
- Falcon deep research (PAC1-deep-research-falcon.md) consistent: non-catalytic dimeric dynein regulator; used as supporting text for dynein complex binding and core function.

Decisions
- NEW GO:0140659 cytoskeletal motor regulator activity (IDA PMID:22939623), NEW GO:0035371 microtubule plus-end.
- Core BPs: nuclear migration along MT (IMP), spindle orientation (IEA accepted), microtubule sliding (IEA accepted; directly supported in yeast).
- Nucleus IDA (PMID:15965467) and IEA: KEEP_AS_NON_CORE - no explicit statement in cached text, but SGD and UniProt both extracted it from this paper (likely IF figures); no nuclear function known.
- Spindle pole IEA: UNDECIDED - Pac1 required for dynein SPB localization, Pac1 itself not shown at SPB in cached papers.
- Protein binding rows (Kel1, Nnf1, Rsc4; large-scale screens) removed as uninformative.
- Identical protein binding (dimerization) kept non-core.
- MT plus-end binding IDA kept non-core (localization evidence; partly Ndl1/Bik1-dependent).
