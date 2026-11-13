# sltB1 (PA4001, Q9HX24) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HX24 --alias sltB1`; accession matches the worklist. No
deep-research provider was used.

### Literature

- Blackburn & Clarke 2002 (PMID:11790124, abstract only): two P. aeruginosa family 3 LTs found by
  homology to E. coli MltB; the palmitoylated one was named MltB, the non-lipidated one SltB.
  [PMID:11790124 "Both enzymes produced the same three major soluble products which were identified as anhydromuropeptides based on ESI-MS analysis"];
  SltB more efficient (kcat/KM) than sMltB. PA4001 has a SignalP signal peptide and no lipobox, so it is
  the soluble enzyme (SltB, later SltB1).
- Legaree & Clarke 2008 (PMID:18708507, full text): [PMID:18708507 "One, MltB, is a lipoprotein, whereas three other homologues are produced in soluble form"];
  SltB1 binds PBP2 (affinity chromatography, SPR), through the N-terminal non-PB module of PBP2; sltB1 is
  clustered with PG-synthesis genes.
- Structure PDB 4ANR shows a Ca2+-binding EF-hand-like loop (UniProt FT BINDING 210-225).

### Annotation decisions

- GO:0008933 IBA and IDA: ACCEPT. GO:0009253 IBA: ACCEPT.
- GO:0005515 IPI (PBP2): REMOVE (protein-binding policy).
- Action counts: ACCEPT 3, REMOVE 1. No source defects.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002410022 | GO:0008933 peptidoglycan lytic transglycosylase activity | 4 | 34 (18 taxa) | GO:0008933, IDA, PMID:11790124 (PseudoCAP) | SOUND | Abstract states the purified soluble enzyme releases anhydromuropeptides from insoluble PG (decisive fact stated outright). Node term suits the GH103 MltB-like clade. | E. coli MltB P41052; P. aeruginosa MltB1 Q9HVX3 and SltB3 Q9HX28 (both also SOUND) | Yes |

The node's GO:0009253 IBD is seeded by E. coli MltB (P41052) alone and is not a PseudoCAP seed. Shared
node with mltB1 and PA3992: all three seeds SOUND, no node-level GO_CENTRAL defect.
