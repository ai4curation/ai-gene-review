# Hand (Drosophila melanogaster, Q9VL05) - curation notes

Automated deep research failed for this run (falcon 402, OpenAI 401); notes below are from cached
publications fetched with `just fetch-pmid`.

## Identity and expression
- Single fly member of the Hand bHLH family (HAND1/HAND2 ortholog); PANTHER PTHR23349 (Twist family).
- Expressed in all cardioblasts and pericardial cells, circular visceral muscle progenitors, lymph gland,
  garland cells and a few CNS cells [PMID:12424518 "We found hand to be expressed in the entire heart, including all cardioblasts and pericardial cells, in the progenitors of the circular visceral muscles, the lymph gland and garland cells, and in a few cells in the CNS"].

## Upstream regulation
- Direct target of Tinman/Pannier in heart and Serpent in lymph gland [PMID:15975941 "Hand is activated by Tinman and Pannier in cardioblasts and pericardial nephrocytes, and by Serpent in hematopoietic progenitors in the lymph gland"].
- Direct target of Biniou in visceral mesoderm; dispensable for initial visceral mesoderm differentiation [PMID:17511863 "we provide evidence that Hand is dispensable for the initial differentiation of the embryonic visceral mesoderm"].

## Molecular function
- Transcriptional activator [PMID:16467358 "Here we show that Drosophila Hand functions as a potent transcriptional activator, and converting it into a repressor blocks heart and lymph gland formation"].
- Targets include muscle genes [PMID:26252215 "Drosophila Hand regulates the expression of numerous genes of diverse physiological relevancy, including distinct factors required for proper muscle development and function such as Zasp52 or Msp-300"].
- Candidate dimer partners [PMID:23747982 "we identified Daughterless and Nautilus as potential dimerization partners of Hand in wing hearts"].
- No direct DNA-binding assay for fly Hand found in cached literature.

## Phenotypes - conflicting embryonic heart data
- Han et al. 2006: [PMID:16467358 "Disruption of Hand function by homologous recombination also results in profound cardiac defects that include hypoplastic myocardium and a deficiency of pericardial and lymph gland hematopoietic cells, accompanied by cardiac apoptosis"].
- Lo et al. 2007: [PMID:17904115 "The dorsal vessel and midgut musculature are unaffected in null mutant embryos, but in a large fraction the lymph glands are missing"]; main requirement is pupal [PMID:17904115 "Hand participates in the proper hormone-dependent remodeling of the larval aorta into the adult heart"].
- Lymph gland/hematopoiesis requirement is reproducible across both studies.
- Wing hearts require Hand (PMID:23747982).

## Review decisions
- MODIFY GO:0032968 (elongation) and GO:0006355 -> GO:0045944.
- Embryonic heart tube development kept as non-core because of the allele conflict.
- NEW GO:0007512 adult heart development (Lo et al. 2007).
- Module annoton (GO:0000981, heart development) is consistent with this review.
