# ptsP (E. coli K-12, P37177) notes

## Provenance

- Deep research could not be generated for this review: no deep-research provider
  API key (Perplexity, OpenAI, FutureHouse/Falcon) is configured in this session, so
  `just deep-research ECOLI ptsP` was not run. The review is based on the UniProt
  record, the GOA table, and the cached publications listed below. No
  `-deep-research-*.md` file was written.
- Publications read: PMID:10473571 (abstract), PMID:23517463 (full text),
  PMID:19400808 (abstract), PMID:18296519 (full text, P. putida ortholog context).

## Findings

- EI(Ntr) is the GAF-domain paralogue of enzyme I. Purified EI(Ntr) phosphorylates
  NPr from PEP and does not phosphorylate HPr [PMID:10473571 "EI(Ntr) phosphorylated
  NPr but not HPr, whereas Enzyme I exhibited a strong preference for HPr."].
- Glutamine and 2-oxoglutarate act on EI(Ntr) autophosphorylation through the GAF
  domain [PMID:23517463 "glutamine and α-ketoglutarate, the canonical signals of
  nitrogen availability, reciprocally regulate the phosphorylation state of the
  PTS(Ntr) by direct effects on enzyme I(Ntr) autophosphorylation"].
- The EI(Ntr)-NPr-IIA(Ntr) chain works in parallel to the sugar transport PTS
  [PMID:19400808 "Proteins EI(Ntr), NPr and IIA(Ntr) form a phosphoryl group transfer
  chain (Ntr-PTS) working in parallel to the phosphoenolpyruvate:carbohydrate
  phosphotransferase system (transport-PTS) in Escherichia coli."].

## Curation decisions

- The sugar PTS (GO:0009401) InterPro2GO row and the N-acetylglucosamine transport
  IBA are removed: EI(Ntr) does not feed sugar transport, and the NAG term was placed
  on the root PAINT node from a single P. aeruginosa multiphosphoryl transfer protein
  seed (PA3760, Q9HXN5).
- The broad phosphorus-group transferase row is refined to GO:0008965.
