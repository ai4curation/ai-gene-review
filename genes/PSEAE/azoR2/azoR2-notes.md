# azoR2 (PA1962, Q9I2E2) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I2E2 --alias azoR2`; accession matches the
worklist. Reviewed Swiss-Prot entry. No deep-research provider was used. Papers
come from the UniProt citations (PMID:24915188 full text; PMID:20417637 abstract
only); see `genes/PSEAE/azoR1/azoR1-notes.md` for the shared literature on the
three P. aeruginosa azoreductases. The PubMed MCP search returned API errors.

### Literature

- Purified paAzoR2 reduces quinones with NADH as donor
  [PMID:24915188 "Rates of quinone reduction were obtained by monitoring the absorbance at 340 nm for oxidation of either NADPH (paAzoR1) or NADH (paAzoR2 and paAzoR3)."]
  and has broad quinone specificity
  [PMID:24915188 "paAzoR2 reduces both benzoquinones and naphthoquinones efficiently"].
- Distinct azo substrate profile among the three paralogs
  [PMID:20417637 "The pure recombinant proteins each have a distinct substrate specificity profile against a range of azo substrates."].
- No structure of paAzoR2 itself; FMN binding rests on HAMAP MF_01216 and the
  homology model in PMID:20417637. No mutant phenotype reported.
- Unlike azoR1 and azoR3, azoR2 carries no GO:0006979 IBA from PTN000811013, so it
  probably sits outside that subnode.

### Decisions

- NEW: GO:0003955 NAD(P)H dehydrogenase (quinone) activity, IDA PMID:24915188 (core).
- TOO_GENERAL: catalytic activity (IEA); GO:0016655 (IBA, PseudoCAP IDA, IEA).
- ACCEPT: FMN binding (IEA).
- MARK_AS_OVER_ANNOTATED: electron transfer activity (IEA).
- REMOVE: GO:0016652 (UniRule mapping wrong; the UNIPROT defect is recorded once on
  azoR1, not duplicated here).
- Counts: NEW 1, TOO_GENERAL 4, ACCEPT 1, MARK_AS_OVER_ANNOTATED 1, REMOVE 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000024600 | GO:0016655 oxidoreductase activity, acting on NAD(P)H, quinone or similar compound as acceptor | 4 | 38 (25 taxa) | GO:0016655, IDA, PMID:24915188 (PseudoCAP) | SOUND | Full text read: purified paAzoR2 assayed with a quinone panel (NADH oxidation at 340 nm). Term correct; GO:0003955 added as NEW. | E. coli AzoR (P41407; EcoCyc IDA GO:0016655, PMID:19666717); azoR1 (Q9I5F3), azoR3 (Q9HZ17) | Yes; E. coli AzoR alone carries independent experimental evidence |

No PSEUDOCAP and no GO_CENTRAL defect; node-level assessment shared with azoR1
(`genes/PSEAE/azoR1/azoR1-notes.md`), which also holds the UniRule GO:0016652
defect.
