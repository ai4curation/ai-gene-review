# csc-1 review notes

## Session 1 (initial review)

- Fetched O45952 (CSC1_CAEEL; Y48E1B.12). 24 GOA rows: 23 from WormBase/ComplexPortal citing
  PMID:12707312, 4 protein-binding IPI from the PDZ Y2H screen PMID:21110867, 3 IEA SubCell.
- PMID:12707312 full text read. CSC-1 is a non-catalytic targeting subunit of the CPC
  (AIR-2/ICP-1/BIR-1/CSC-1). It binds BIR-1 directly; the CSC-1/BIR-1 dimer recruits ICP-1;
  AIR-2 joins via ICP-1. CSC-1 does not stimulate AIR-2 kinase activity [PMID:12707312
  "This activity is not stimulated by CSC-1/BIR-1, suggesting that these two subunits function
  as targeting subunits for AIR-2 kinase."].
- Molecular function choice: no existing MF row besides protein binding. In core_functions I
  use GO:0030674 protein-macromolecule adaptor activity, because CSC-1 is needed for stable
  BIR-1/ICP-1 and BIR-1/AIR-2 association (bridging). No NEW MF annotation row is proposed:
  this is an interpretation of the biochemistry, and whether CSC-1 contacts ICP-1 directly is
  not shown (binary ICP-1/CSC-1 binding was undetectable).
- Decisions kept consistent with the icp-1 review (same ComplexPortal NAS rows):
  - mitotic cell cycle -> MODIFY to mitotic sister chromatid segregation + mitotic cytokinesis.
  - mitotic chromosome movement towards spindle pole -> MODIFY to mitotic sister chromatid
    segregation (phenotype is failed segregation/congression, not anaphase A movement).
  - SAC and sister-chromatid-separation NAS -> MARK_AS_OVER_ANNOTATED (not tested for CSC-1).
  - spindle (IEA) and microtubule cytoskeleton (IDA) -> MODIFY to the meiotic/mitotic spindle
    midzone terms the gene already carries.
- Protein-binding rows: REMOVE under policy. Partners are PDZ proteins (LIN-10, MAGI-1, AFD-1,
  P90976); biological meaning unknown.
- No NEW process terms: the strict bar is not met by anything beyond what GOA already has.
- Literature is thin: PubMed finds no further CSC-1-specific papers under that name.
- Revised: comparator check on human CPC subunits in QuickGO (CDCA8/Borealin Q53HL2 has only
  GO:0005515 MF; BIRC5 and INCENP carry binding terms, not adaptor). Dropped the GO:0030674
  core_functions MF rather than assert an MF the GO convention does not use for Borealin;
  raised it as a suggested question instead.
