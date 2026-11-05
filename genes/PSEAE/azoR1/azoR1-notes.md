# azoR1 (PA0785, Q9I5F3) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I5F3 --alias azoR1`; accession matches the
worklist. Reviewed Swiss-Prot entry. No deep-research provider was used; literature
was gathered from the UniProt record's citations and fetched with `just fetch-pmid`.
PMID:24915188 and PMID:22355582 have full text in the cache; PMID:17904577,
PMID:20057057, PMID:20417637 and PMID:19666717 are abstract-only. The PubMed MCP
search returned API errors during this session.

### Literature

- PA0785, annotated as acpD, is an FMN azoreductase
  [PMID:17904577 "The purified recombinant enzyme exhibits activity corresponding to that of azoreductase but not acpD."],
  with one FMN per subunit
  [PMID:17904577 "Each recombinant protein molecule has an estimated molecular mass of 23,050 Da and one non-covalently bound FMN as co-factor."].
- Quinone reductase activity of the purified enzyme, NADPH as donor
  [PMID:24915188 "Rates of quinone reduction were obtained by monitoring the absorbance at 340 nm for oxidation of either NADPH (paAzoR1) or NADH (paAzoR2 and paAzoR3)."];
  quinones are far better substrates than azo compounds
  [PMID:24915188 "Rates of quinone reduction in all cases were up to two orders of magnitude higher than were observed for reduction of azo substrates"].
  The paper frames the family as two-electron reducers
  [PMID:24915188 "Two electron reduction reactions of quinones are carried out by a group of enzymes known as NAD(P)H quinone oxidoreductases."]
  but did not determine the product.
- Nitrofurazone reduction
  [PMID:22355582 "azoreductases have a wider role in drug metabolism than previously thought as they can also reduce and hence activate nitrofurazone"].
- E. coli ortholog AzoR protects against electrophilic quinones
  [PMID:19666717 "These data indicated that AzoR is a quinone reductase providing resistance to thiol-specific stress caused by electrophilic quinones."].
  No P. aeruginosa mutant phenotype is reported for any of the three azoR genes.

### Decisions

- NEW: GO:0003955 NAD(P)H dehydrogenase (quinone) activity, IDA PMID:24915188 (core).
- TOO_GENERAL: catalytic activity (IEA); GO:0016655 (IBA, PseudoCAP IDA, IEA).
- MODIFY: GO:0003960 quinone reductase (NADPH) activity (EXP, IEA Rhea) to
  GO:0003955, because GO:0003960 is the semiquinone-forming reaction (UNIPROT
  WRONG_TERM, SUSPECTED).
- ACCEPT: FMN binding (IEA).
- KEEP_AS_NON_CORE: response to oxidative stress (IBA PTN000811013, E. coli seed).
- MARK_AS_OVER_ANNOTATED: electron transfer activity (IEA), consistent with PA0949.
- REMOVE: GO:0016652 (NAD(P)+ as acceptor; UniRule mapping wrong; UNIPROT
  WRONG_TERM, CONFIRMED by the GO definition). This defect is recorded once, here;
  the same UniRule row on azoR2 and azoR3 cross-references it.
- Counts: NEW 1, TOO_GENERAL 4, MODIFY 2, ACCEPT 1, KEEP_AS_NON_CORE 1,
  MARK_AS_OVER_ANNOTATED 1, REMOVE 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000024600 | GO:0016655 oxidoreductase activity, acting on NAD(P)H, quinone or similar compound as acceptor | 4 | 38 (25 taxa) | GO:0016655, IDA, PMID:24915188 (PseudoCAP) | SOUND | Full text read: purified paAzoR1 assayed with a quinone panel (NADPH oxidation at 340 nm). The term is correct; GO:0003955 is the specific child, added as NEW. | E. coli AzoR (P41407; EcoCyc IDA GO:0016655, PMID:19666717); paralogs azoR2 (Q9I2E2) and azoR3 (Q9HZ17), same paper | Yes; E. coli AzoR alone carries independent experimental evidence |

No PSEUDOCAP and no GO_CENTRAL defect. The node term is the general quinone-acceptor
term, which suits a 38-leaf, 25-taxon clade of azoreductase type 1 proteins
(HAMAP MF_01216) in which quinone reduction has been shown in both E. coli and
P. aeruginosa. The three P. aeruginosa paralogs are seeds of the same node from
the same paper; their seed verdicts (SOUND) and actions are kept consistent in the
azoR2 and azoR3 reviews.

Other defects (not node-level): UNIPROT WRONG_TERM on the GO:0003960 EXP row
(SUSPECTED); UNIPROT WRONG_TERM on the UniRule UR000101231 GO:0016652 mapping
(CONFIRMED), recorded here only.
