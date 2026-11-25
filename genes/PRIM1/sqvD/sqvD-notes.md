# sqvD (D5E1S9, Priestia megaterium QM B1551 / DSM 1804) notes

## 2026-11-10 session

- Deep research: the perplexity provider failed in this environment when tried for the sibling
  gene slaB (client dependency unresolvable offline, no key); not retried, no provider file.
- Function: SQ isomerase, RHEA:40439, EC 5.3.1.31. UniProt (Swiss-Prot, ECO:0000269
  PubMed:33036753): "Catalyzes the isomerization of sulfoquinovose (SQ) to
  6-deoxy-6-sulfo-D-fructose (SF)". PMID:33036753 is abstract-only in the cache and the abstract
  names only SqvA; the EXP row is accepted on the curated record (curators saw the full text).
- Review: [PMID:41676062 "wherein SQ is isomerized by SqvD to 6-deoxy-6-sulfo fructose (SF), with a
  concomitant contribution of the mutarotase SqvB."] SqvD orthologs are also used by the sulfo-TK
  and sulfo-EMP2 routes [PMID:41676062 "SQ is also initially converted to SF via SqvD"].
- Fold: L-fucose isomerase-like (Pfam PF31143 Fuc_iso_N, PF02952 Fucose_iso_C; InterPro
  IPR015888/IPR009015); PANTHER PTHR36120:SF1; NCBIfam NF048012 SlpQosIsomSftI. Not related to
  E. coli YihS (PTHR15108). InterPro2GO therefore gives fucose isomerase/fucose metabolism rows:
  L-fucose isomerase marked over-annotated (untested; ortholog SftI is promiscuous with F6P),
  fucose metabolic process removed, monosaccharide metabolism and aldose-ketose isomerase rows
  modified to GO:1902777 and GO:0061593.
- Added NEW GO:1902777 (comparator: E. coli YihS carries it).
