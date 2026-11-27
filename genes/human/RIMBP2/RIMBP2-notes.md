# RIMBP2 evidence notes

## 2026-09-20 — propagated annotation re-review

All six existing annotation rows were inspected with the cached UniProt record,
the existing Falcon/OpenAI research, and primary papers fetched into the
publication cache. The broad plasma-membrane location is supported; a
presynaptic active-zone location does not imply that the broader location is
wrong or dispensable.

The neuromuscular transmission objection confused function at other synapse
types with exclusion from neuromuscular junctions. The mammalian studies do
not establish that exclusion. Grauel et al. explicitly describe conserved
short-term-plasticity roles between flies and mammals
([PMID:27671655](https://pubmed.ncbi.nlm.nih.gov/27671655/)). Nevertheless, the
specific human neuromuscular context remains unresolved. The historical
PTN002306629 node does not appear in the PTHR14234 PAINT slice, including after
`just fetch-panther-paint PTHR14234`; no claim about loss of function can be
made from that snapshot difference.

A neutral OpenScientist hypothesis, with no previous reviewer action supplied,
was launched for GO:0007274 after checking the gene folder and provider cache
(the cache held general OpenAI/Falcon research, but no OpenScientist RIMBP2
report). The current action is UNDECIDED pending evaluation of that report.

Scaffold and priming evidence is positive: the mouse imaging and complex study
states, "RIM-BP2 is part of the presynaptic AZ scaffold"
([PMID:27671655](https://pubmed.ncbi.nlm.nih.gov/27671655/)); the mossy-fiber study
links RIMBP2 to "stabilization of Munc13-1 at the active zone"
([PMID:31535974](https://pubmed.ncbi.nlm.nih.gov/31535974/)). These support the
existing proposed annotations through mammalian orthology. Supporting excerpts
in the review now quote the cached primary texts rather than paraphrases marked
as inaccessible DOI quotes. The Cell Reports study
([PMID:32755572](https://pubmed.ncbi.nlm.nih.gov/32755572/)) is abstract-only in
the cache; it was not treated as full-text verification.

The requested synapse-type comparison is with neuronal RIMBP1/TSPOAP1. The
previous RIMBP3 wording concerned a different, predominantly spermiogenic
branch and was unsuitable for that comparison.

### Completed OpenScientist adjudication

Report job `3be64e87-d5a4-4134-946b-8933a9946030` completed and was incorporated with exact excerpts. It documents conserved active-zone mechanisms and the absence of an identified vertebrate NMJ experiment, explicitly distinguishing untested from refuted. Its stronger recommendation against any phylogenetic transfer on that basis is not adopted. The report's skeletal-muscle-expression comparison also misses that a presynaptic protein is made by motor neurons.

Independent QuickGO queries confirm six current human O15034 annotations, none GO:0007274, with current IBA presynaptic terms; the historical source row is preserved. The exact human/mouse term query returned 59 rows with no RIM-BP symbol; the report's different aggregate counts are not used. Query parameters/results and term definition are recorded in `projects/IBA_REVIEW/rereview-2026-09-20/rimbp2-quickgo-crosscheck.json`. The historical inference remains UNDECIDED. A PAINT curator's explanation of the context-specific node change is the remaining useful second opinion; no repeat OpenScientist run is needed.
