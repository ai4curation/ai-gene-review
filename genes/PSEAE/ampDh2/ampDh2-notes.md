# ampDh2 (PA5485, Q9HT86) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HT86 --alias ampDh2`; accession matches the worklist.
Unreviewed entry. No deep-research provider was used; literature from the cached seed paper,
PubMed MCP and web searches ("AmpDh2", "AmpDh3 Pseudomonas"). Reviewed together with ampD and
ampDh3 (shared PAINT nodes).

### Literature

- Seed paper PMID:23510438 (Zhang et al. 2013), full text cached and read. Kinetics with six
  synthetic substrates and sacculus digestion [PMID:23510438 "Overnight incubation of the
  polymeric sacculus with AmpDh2 produced products with oligomeric cell-wall sugars without the
  peptide stem."]. No localization experiment: [PMID:23510438 "AmpDh2 has a signal peptide that
  targets it to the periplasm and an anchor that is believed to insert it into the outer
  membrane."]. No beta-lactamase assay; the AmpC link is interpretive [PMID:23510438
  "the marginal activity in turnover of metabolite 1 with AmpDh2 and AmpDh3 explains the
  stepwise effect observed in augmenting derepression of AmpC β-lactamase"].
- PMID:23931161 (Lee et al. 2013, full text): [PMID:23931161 "AmpDh2 is a dimeric protein that
  inserts itself into the inner leaflet of the outer membrane, where it interacts and
  hydrolyzes the amide bond between the stem peptide and the NAM moiety of the sacculus."]
- UniProt Q9HT86: SignalP signal peptide 1-16 and PROSITE PS51257 lipoprotein site; PG_binding_1
  domain; crystal structures 4BJ4, 4BOL.

### Annotation decisions

- GO:0008745 (IBA, IDA, IEA): ACCEPT, core MF.
- GO:0009253 (IEA), GO:0009254 (IBA): ACCEPT.
- GO:0009276 cell wall (IBA, IDA): ACCEPT; true for this lipoprotein acting on the sacculus.
  The IDA code overstates the evidence (PSEUDOCAP WRONG_EVIDENCE_CODE, CONFIRMED).
- GO:0033252 regulation of beta-lactamase activity (IDA): REMOVE; PSEUDOCAP WRONG_TERM,
  CONFIRMED (full text read).
- NEW GO:0009279 cell outer membrane (IC): signal peptide plus lipobox, and the laboratory's
  structural work.
- Action counts: ACCEPT 7, REMOVE 1, NEW 1.

## PseudoCAP IBA-seed assessment

Node assessments are recorded once in `genes/PSEAE/ampD/ampD-notes.md`; summary below.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001252273 | GO:0008745 N-acetylmuramoyl-L-alanine amidase activity | 5 | 37 (19 taxa) | GO:0008745, IDA, PMID:23510438 | SOUND | Kinetics with purified enzyme and sacculus digestion (full text). | E. coli AmpD P13016, AmiD P75820, ampD, ampDh3 | Yes |
| PTN002019137 | GO:0009276 Gram-negative-bacterium-type cell wall | 3 | 18 (11 taxa) | GO:0009276, IDA, PMID:23510438 | SOUND | Location correct (outer-membrane lipoprotein acting on the sacculus), but not assayed in the paper; evidence code is IDA where TAS/IC fits. | ampD (WRONG), ampDh3 (location unsettled) | No: the node term does not suit the clade, which includes the cytoplasmic AmpD lineage. GO_CENTRAL defect recorded once, on the ampD review |
