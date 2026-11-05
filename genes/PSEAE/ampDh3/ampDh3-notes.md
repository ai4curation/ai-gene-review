# ampDh3 (PA0807, Q9I5D1) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I5D1 --alias ampDh3`; accession matches the worklist.
Unreviewed entry. No deep-research provider was used; literature from the cached seed paper,
PubMed MCP and web searches ("AmpDh3 Pseudomonas", "AmpDh3 PA0807 type VI secretion"). Reviewed
together with ampD and ampDh2 (shared PAINT nodes).

### Literature

- Seed paper PMID:23510438 (full text read): kinetics with six substrates; sacculus digestion
  [PMID:23510438 "The reaction with AmpDh3 also produced products (20), but its quantity was
  three times less than that with AmpDh2."]. Location not assayed [PMID:23510438 "the cellular
  location of AmpDh3 is currently unknown"]; a periplasmic role is proposed from substrate
  preference. No beta-lactamase assay.
- PMID:23931161 (full text): tetramer, processive on polymeric sacculus [PMID:23931161 "This
  enzyme is soluble, it has higher specific activity and it does not leave behind partially
  hydrolyzed peptidoglycan."]; the abstract calls it "a periplasmic zinc protease".
- PMID:36577706 (Colautti et al. 2023, abstract): found no export of AmpDh3, did not reproduce
  the proposed T6SS effector-immunity pair with PA0808, and calls AmpDh3 a cytosolic enzyme
  [PMID:36577706 "we found no evidence that AmpDh3 is exported from cells"].
- UniProt Q9I5D1 has no signal peptide feature; the N-terminus (MLTIDYNSYR...) is not a
  Sec signal. Structures 4BXD, 4BXE, 4BXJ with Zn ligands.

### Annotation decisions

- GO:0008745 (IBA, IDA, IEA): ACCEPT, core MF.
- GO:0009253 (IEA), GO:0009254 (IBA): ACCEPT.
- GO:0009276 cell wall (IBA, IDA): UNDECIDED. Location disputed and never assayed; PSEUDOCAP
  WRONG_EVIDENCE_CODE on the IDA (CONFIRMED: the paper says the location is unknown).
- GO:0033252 (IDA): REMOVE; PSEUDOCAP WRONG_TERM, CONFIRMED.
- Action counts: ACCEPT 5, UNDECIDED 2, REMOVE 1.

## PseudoCAP IBA-seed assessment

Node assessments are recorded once in `genes/PSEAE/ampD/ampD-notes.md`; summary below.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001252273 | GO:0008745 N-acetylmuramoyl-L-alanine amidase activity | 5 | 37 (19 taxa) | GO:0008745, IDA, PMID:23510438 | SOUND | Kinetics with purified enzyme and sacculus digestion (full text). | E. coli AmpD P13016, AmiD P75820, ampD, ampDh2 | Yes |
| PTN002019137 | GO:0009276 Gram-negative-bacterium-type cell wall | 3 | 18 (11 taxa) | GO:0009276, IDA, PMID:23510438 | INDIRECT-PHENOTYPE | Location inferred from in vitro substrate preference; the paper states the location is unknown, and later work disagrees on it. | ampD (WRONG), ampDh2 (SOUND) | No: the node term does not suit the clade. GO_CENTRAL defect recorded once, on the ampD review |
