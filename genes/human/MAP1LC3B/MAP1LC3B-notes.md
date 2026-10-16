# MAP1LC3B notes (human, Q9GZQ8)

Deep research: not run (falcon times out after 600 s in this environment and perplexity-lite is not
installed). Review based on cached publications and the UniProt record.

## Key findings
- Cleaved at Gly120 by ATG4B and conjugated to PE by ATG7/ATG3 [PMID:15355958 "These results indicate that the carboxyl terminus of MAP1LC3B is cleaved to expose Gly(120) for further ubiquitylation-like reactions."]. This corrects PMID:12740394, which reported no C-terminal cleavage.
- LC3 subfamily: phagophore elongation; GABARAPs: later maturation [PMID:20418806].
- Atg8 hexa-KO: autophagosomes still form (smaller, slower), fusion fails; GABARAPs dominate fusion and PINK1/Parkin mitophagy [PMID:27864321 "We show that Atg8s are dispensable for autophagosome formation and selective engulfment of mitochondria, but essential for autophagosome-lysosome fusion."].
- LIR receptor docking: PHB2 [PMID:28017329], AMBRA1 [PMID:25215947]; ceramide binding in lethal mitophagy [PMID:22922758]; JMY actin nucleation [PMID:30420355].

## Decisions
- 149 protein binding IPI rows: REMOVE (uninformative); there is no GO MF term for Atg8 LIR docking (raised as a suggested question).
- Core MF: phosphatidylethanolamine binding (repo convention for Atg8 lipidation, as in worm lgg-1).
- Mitochondrial locations, ceramide binding, ubiquitin ligase binding, starvation-response terms, cytoskeleton/axoneme/microtubule binding: non-core.
