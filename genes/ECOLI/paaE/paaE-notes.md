# paaE (E. coli K-12) notes

## Deep research

`just deep-research ECOLI paaE --provider falcon` was attempted once (2026-10-23) and failed
("Exception: Failed to authenticate"); perplexity/openai keys are not configured. No
deep-research file exists; the review is built from cached primary literature.

## Key sources (all cached in publications/)

- PMID:21247899 (Grishin et al. 2011, E. coli K-12; full text): reconstitution, (PaaAC)2 structure,
  PaaE cofactors. [PMID:21247899 "In vitro reconstitution of the oxygenase subunits showed that each of the PaaA, B, C, and E subunits are necessary for catalysis, whereas PaaD is not essential."]
- PMID:20660314 (Teufel et al. 2010; full text): product is ring 1,2-epoxyphenylacetyl-CoA. Note the
  oxygenase biochemistry used Pseudomonas sp. Y2 PaaABC(D)E, not the E. coli proteins.
  [PMID:20660314 "PaaABC(D)E thus functions as a ring 1,2-phenylacetyl-CoA epoxidase."]
- PMID:16997993 (Fernandez et al. 2006, E. coli W; full text): per-gene deletions/complementation.
- PMID:9748275 (Ferrandez et al. 1998; abstract only): paa cluster; IMP rows deferred to curator.
- PMID:20823522 (Grishin et al. 2010): PaaAC crystallization (fetched in this session).

## Gene-specific

- Class IA reductase: N-terminal FAD/NAD(P) reductase, C-terminal plant-type [2Fe-2S] ferredoxin (PMID:16997993).
- [PMID:21247899 "The PaaE subunit is a reductase with a preference for NADPH and FAD, capable of reducing cytochrome c"]
- Oxidoreductase activity (IBA, IEA) MODIFIED to GO:0016651 oxidoreductase activity, acting on NAD(P)H.
- Iron-sulfur cluster binding MODIFIED to GO:0051537.
- GO:0062077 IPI accepted although PMID:21247899 found no stable PaaE-PaaABC complex in E. coli
  ("No evidence for the formation of a stable complex between PaaD or PaaE and other proteins");
  Y2 ortholog PaaE co-purifies with PaaABC (PMID:20660314). Possible evidence-code question for EcoCyc.
- NEW: contributes_to GO:0097266 (IDA, PMID:21247899).
