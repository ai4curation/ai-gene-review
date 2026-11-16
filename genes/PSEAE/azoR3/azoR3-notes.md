# azoR3 (PA3223, Q9HZ17) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HZ17 --alias azoR3`; accession matches the
worklist. Reviewed Swiss-Prot entry. No deep-research provider was used. Papers
come from the UniProt citations (PMID:24915188 full text; PMID:20417637 abstract
only); see `genes/PSEAE/azoR1/azoR1-notes.md` for the shared literature on the
three P. aeruginosa azoreductases. The PubMed MCP search returned API errors.

### Literature

- Purified paAzoR3 reduces quinones with NADH as donor
  [PMID:24915188 "Rates of quinone reduction were obtained by monitoring the absorbance at 340 nm for oxidation of either NADPH (paAzoR1) or NADH (paAzoR2 and paAzoR3)."],
  preferring naphthoquinones
  [PMID:24915188 "In contrast paAzoR3 prefers naphthoquinones"],
  and is the most active of the three (16.8 mM/s/mg with plumbagin)
  [PMID:24915188 "These maximum rates were as follows: paAzoR1 and paAzoR2 reducing Bzq 0.57 mM.s−1.mg of enzyme−1 and 7.78 mM.s−1.mg of enzyme−1 respectively and paAzoR3 reducing Plu 16.8 mM.s−1.mg of enzyme−1."].
- Distinct azo substrate profile among the paralogs
  [PMID:20417637 "The pure recombinant proteins each have a distinct substrate specificity profile against a range of azo substrates."].
- No structure of paAzoR3 itself; FMN binding rests on HAMAP MF_01216 and the
  homology model in PMID:20417637. No mutant phenotype reported.

### Decisions

- NEW: GO:0003955 NAD(P)H dehydrogenase (quinone) activity, IDA PMID:24915188 (core).
- TOO_GENERAL: catalytic activity (IEA); GO:0016655 (IBA, PseudoCAP IDA, IEA).
- ACCEPT: FMN binding (IEA).
- KEEP_AS_NON_CORE: response to oxidative stress (IBA PTN000811013), as for azoR1.
- MARK_AS_OVER_ANNOTATED: electron transfer activity (IEA).
- REMOVE: GO:0016652 (UniRule mapping wrong; the UNIPROT defect is recorded once on
  azoR1).
- Counts: NEW 1, TOO_GENERAL 4, ACCEPT 1, KEEP_AS_NON_CORE 1,
  MARK_AS_OVER_ANNOTATED 1, REMOVE 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000024600 | GO:0016655 oxidoreductase activity, acting on NAD(P)H, quinone or similar compound as acceptor | 4 | 38 (25 taxa) | GO:0016655, IDA, PMID:24915188 (PseudoCAP) | SOUND | Full text read: purified paAzoR3 assayed with a quinone panel (NADH oxidation at 340 nm); highest rates of the three paralogs. Term correct; GO:0003955 added as NEW. | E. coli AzoR (P41407; EcoCyc IDA GO:0016655, PMID:19666717); azoR1 (Q9I5F3), azoR2 (Q9I2E2) | Yes; E. coli AzoR alone carries independent experimental evidence |

No PSEUDOCAP and no GO_CENTRAL defect; node-level assessment shared with azoR1
(`genes/PSEAE/azoR1/azoR1-notes.md`), which also holds the UniRule GO:0016652
defect.
