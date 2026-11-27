# rfth-1 review notes

## 2026-10-28 - initial review

- `just fetch-gene worm rfth-1` resolved UniProt Q23444 (RFT1_CAEEL, ZK180.3); 9 GOA rows, all
  IBA/ISS/IEA. No C. elegans primary literature on ZK180.3/rfth-1 found in PubMed.
- PMID:23483992 was requested as a key paper but it characterizes rft-1 (Y47D7A.16) and rft-2
  (Y47D7A.14), riboflavin transporters (SLC52 family), not rfth-1 [PMID:23483992 "we assign them the
  names rft-1 (for Y47D7A.16) and rft-2 (for Y47D7A.14)"]. Recorded in references with relevance NONE
  so the name collision is visible; not used as evidence.
- IBA rows come from PTN000319164 (eukaryote root, taxon:2759), seeded by yeast Rft1, human RFT1 and
  T. brucei Rft1 (ER membrane only). RFTH-1 sits inside that clade (PTHR13117:SF5).
- Pairwise identity: ~31% to human RFT1, ~25% to yeast Rft1 [file:worm/rfth-1/rfth-1-bioinformatics/RESULTS.md].
- Decisions follow genes/human/RFT1: ER membrane accept; dolichol-linked oligosaccharide biosynthesis and
  N-glycosylation accept; glycolipid translocation accept (family biochemical activity, process term is
  mechanism-neutral); membrane -> MODIFY to ER membrane; NEW MF GO:0140303 intramembrane lipid carrier
  activity by ISS (the human review re-termed the ATP-dependent floppase IDA to this term).
- Caveat carried throughout: whether M5-DLO scrambling is the essential in-vivo role is disputed
  [PMID:42417535 "scrambling activity is dispensable"].
