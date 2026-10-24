# LYS9 (YNR050C, P38999) notes

## 2026-10-24

Re-reviewed S. cerevisiae `LYS9` after the `PTHR11133` LYS1/lys3 branch. The
fungal `PANTHER:PTN000875327` IBA is the correct LYS9/lys9 sister placement to
the `PTN000875292` LYS1/lys3 branch. The broad `PANTHER:PTN000123605`
`GO:0004753 saccharopine dehydrogenase activity` placement is true at the mixed
family node but over-generic for `P38999`, which sits in `PTHR11133:SF22` and
has direct NADP(+), L-glutamate-forming saccharopine reductase evidence.

Deep research: `just deep-research-falcon yeast LYS9` could not run because the
deep-research provider API keys are unavailable in this environment. Manual
searches for `Saccharomyces LYS9`, `P38999`, and saccharopine reductase found
newer pathway and fungal-evolution papers that discuss yeast LYS9 as the
canonical saccharopine reductase step, but no newer paper changed the PTHR11133
placement, the exact EC 1.5.1.10/GO:0004755 activity, or the cytosolic
L-lysine-biosynthesis role.

Pathway context: LYSINE-AMINOAD-PWY-2, saccharopine reductase (EC 1.5.1.10).

- Activity: [PMID:18416559 "Kinetic studies were carried out for histidine-tagged saccharopine reductase from Saccharomyces cerevisiae at pH 7.0"], ordered NADPH-first mechanism (same paper).
- Genetics: [PMID:6429126 "The lys14 strains, like lys9 mutants, accumulated alpha-aminoadipate-semialdehyde and lacked significant amounts of saccharopine reductase activity."] (LYS14 is the pathway activator [PMID:10103047 "transcriptional activator Lys14p"]).
- Location: cytoplasm (Kumar 2002, Huh 2003 HDA). Cell periphery from SWAT screen scored by eye without markers -> marked over-annotated. Interacts with Trm112 [UniProt:P38999] (not in GOA).
- All exact MF/BP rows were accepted; the generic `GO:0004753` parent was
  marked `TOO_GENERAL` because it is true but subsumed by the accepted exact
  `GO:0004755` activity.
