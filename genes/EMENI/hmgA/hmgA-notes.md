# EMENI hmgA (Q00667) notes

## Deep research

No provider deep-research file exists and no deep-research API keys are available
in this session, so none was generated (no `-deep-research-<provider>.md` file
was written). Notes below are from the cached publications (all abstract-only),
the UniProt record and the PAINT file for PTHR11056.

## Identity

- UniProt Q00667 (HGD_EMENI), gene hmgA, ORF AN1897, 448 aa; strain FGSC A4.
- Clustered with maiA (AN1895) and fahA (AN1896) [PMID:9417084 "maiA is clustered
  with fahA and hmgA, the genes encoding the two other enzymes of the common part of
  the Phe/phenylacetate pathways."].
- PANTHER PTHR11056:SF0; Pfam HgmA_N/HgmA_C; NCBIfam TIGR01015. Fe-binding residues
  340/346/377 by similarity (ECO:0000250).

## Function

- First homogentisate dioxygenase gene characterized; recombinant GST-HmgA is active
  [PMID:7673153 "the affinity-purified protein has homogentisate dioxygenase activity"].
- Disruption: homogentisate accumulation on Phe [PMID:7673153 "disruption of the gene
  results in accumulation of homogentisate in broths containing phenylalanine"].
- Loss of HGD suppresses fahA Phe toxicity [PMID:7568087 "loss of homogentisate
  dioxygenase (leading to alkaptonuria in humans) prevents the effects of a Fah
  deficiency"].
- Used to identify human HGD (alkaptonuria gene) [PMID:7673153].

## Curation decisions

- All GO:0004411 and GO:0006559 rows ACCEPT; IBA PTN000114776 is seeded by Q00667's
  own experimental data (expected, not circular).
- ARBA broad process terms (GO:0009063, GO:0009074): TOO_GENERAL.
- NEW: GO:1902000 homogentisate catabolic process (IMP, PMID:7673153). HmgA is the
  enzyme acting on homogentisate. Comparator: FahA (Q00770) and human FAH carry it,
  human HGD does not; judged an omission since HGD/HmgA catalyses the step on the
  named compound (not a substrate-of-process case).
- Not added: L-tyrosine catabolic process (no fungal hmgA data on Tyr in the cached
  abstracts) and a location term (no data).

## 2026-11-01 review follow-up (PR 5356)

- GO:1902000 homogentisate catabolic process is now asserted uniformly for all nine
  homogentisate-pathway exemplars (KT2440 hmgA/hmgC/hmgB, human HGD/GSTZ1/FAH,
  A. nidulans hmgA/maiA/fahA), as NEW where GOA lacks it: each enzyme performs one of
  the three catalytic steps of homogentisate breakdown.
