# PA3992 (SltB3, Q9HX28) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HX28 --alias PA3992`; accession matches the worklist. No gene
name in UniProt; folder and symbol use the locus tag. PMID:27035839 cached with `just fetch-pmid`
(full text, PMC5436585). No deep-research provider was used.

### Literature

- Lee et al. 2016 (PMID:27035839, full text): [PMID:27035839 "We describe here the properties of SltB3 (also referred to as SltH; the gene for which is annotated as PA3992), a soluble LT of P."]
  SltB3 is exolytic: [PMID:27035839 "The ultimate product of the reaction is N-acetylglucosamine-1,6-anhydro-N-acetylmuramic acid."]
  Kinetics on a synthetic tetrasaccharide-pentapeptide substrate: [PMID:27035839 "The purified recombinant SltB3 turned over 1 (Figure 2B), with the following kinetics parameters: kcat = 19."]
  It also processes a 20-sugar peptidoglycan strand; X-ray structures (5ANZ, 5AO7, 5AO8) show four
  domains in an annulus through which the glycan strand threads.
- UniProt predicts a lipobox (PRU00303, Cys31), but the paper calls SltB3 a soluble LT and
  Legaree & Clarke 2008 (PMID:18708507) list SltB3 among the soluble paralogs; no CC annotation is under
  review, so this is noted only.

### Annotation decisions

- GO:0008933 IBA and IDA: ACCEPT. GO:0009253 IBA: ACCEPT. GO:0009254 peptidoglycan turnover IDA: ACCEPT
  (the enzyme performs the breakdown step of turnover; the paper frames it as turnover in recycling).
- Action counts: ACCEPT 4. No source defects.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002410022 | GO:0008933 peptidoglycan lytic transglycosylase activity | 4 | 34 (18 taxa) | GO:0008933, IDA, PMID:27035839 (PseudoCAP) | SOUND | Full text read: purified SltB3 turns over PG substrates to GlcNAc-1,6-anhydroMurNAc with measured kinetics. GO:0008933 explicitly includes exolytic activity. Node term suits the GH103 clade. | E. coli MltB P41052; P. aeruginosa SltB1 Q9HX24 and MltB1 Q9HVX3 (both SOUND) | Yes |

Shared node with sltB1 and mltB1 (see `genes/PSEAE/sltB1/sltB1-notes.md`): all seeds SOUND, no
GO_CENTRAL defect.
