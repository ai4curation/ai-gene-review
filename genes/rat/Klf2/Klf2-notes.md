# Klf2 (rat) review notes

## Accession
`just fetch-gene rat Klf2` resolved Q9ET58 (Swiss-Prot KLF2_RAT; RGD:1359220; GeneID 306330), as
requested. GOA file is keyed to Q9ET58 (57 rows).

## Literature
See Klf2-deep-research-manual.md (manual synthesis; no deep-research provider available).
Full text read: PMID:18406357 (Cullingford 2008), PMID:15540987 (Wick 2005), PMID:15136591.
Abstract only: PMID:16466697, PMID:9367982, PMID:16855590, PMID:12176889, PMID:15947087,
PMID:10409672, PMID:26299712, PMID:22482507. PMID:19192484 cache has title/bibliographic
data only (no abstract text).

## Decisions
- Core MF: GO:0000981 (RNAPII-specific DNA-binding TF activity) and GO:0000978 (RNAPII
  cis-regulatory sequence-specific DNA binding) [PMID:15540987 "LKLF bound to a GC-rich region
  of the cPLA2 promoter"]. Generic DNA binding / GO:0003700 / GO:1990837 rows -> MODIFY to these
  (ancestry checked with OAK: GO:0000978 is_a GO:1990837 is_a GO:0003677; GO:0000981 is_a GO:0003700).
- Core BP: GO:0045944. GO:0045893 rows (incl. the rat IMP on the cPLA2 promoter) -> MODIFY to
  GO:0045944 (OAK: GO:0045944 is_a GO:0045893). GO:0006357 IBA -> MODIFY to GO:0045944 and
  GO:0000122 (both descendants).
- Negative regulation (GO:0000122): human IDA on VEGFA promoter repression [PMID:26299712];
  kept as non-core.
- Shear-stress rows: GO:0071499 accepted (non-core but characteristic); GO:0071498 and IEP
  GO:0034616 refined to GO:0071499 (OAK: GO:0071499 is_a both).
- IEP rows (endothelin, H2O2, IL-1, TNF) from PMID:18406357 are expression responses: kept as
  non-core, consistent with GO's IEP convention.
- Developmental MGI ISO rows (acts_upstream_of_or_within) kept as non-core phenotypes;
  epigenetic regulation of gene expression (Prdm14-Klf2 reprogramming), positive regulation of
  protein metabolic process (KLF4 paper, IGI) and cellular stress response to acid chemical
  (uric acid study) marked over-annotated.
- No NEW process terms proposed (developmental phenotypes are necessity evidence only).
