# gtl-1 review notes

## Session 1 (2026-10-28)

- `just fetch-gene worm gtl-1` resolved G5ECM4 (WormBase C05C12.3 / WBGene00001795, GeneID 178031),
  as expected. GOA has 7 rows: 4 IBA from PTN001013045 (TRPM node), 1 IEA membrane, 2 defecation
  (IMP, IGI with gon-2 = WBGene00001651) from PMID:18299395.
- Literature was reviewed manually (see `gtl-1-deep-research-manual.md`); no deep-research API.
  Full texts read: PMID:18299395 (Xing 2008), PMID:20221407 (Teramoto 2010), PMID:32009965
  (Cohen 2020, HEK293 expression), plus PMID:22483941, PMID:21549603, PMID:18495023.
  Abstract only: PMID:16054081, PMID:19923421, PMID:17233618, PMID:38373693, PMID:32148064.
- Key facts:
  - I(GTL-1) (current left in gon-2 mutant intestinal cells) is >60-fold Ca2+ over Na+ selective and
    Mg2+-permeable [PMID:18299395 "GON-2, GTL-1, and the ORCa channels exhibit a >60-fold selectivity
    for Ca2+ over Na+"].
  - GTL-1 alone forms a Ca2+-activated channel in HEK293 excised patches [PMID:32009965 "using excised
    patches we show that GTL-1 can be activated by internal calcium"].
  - gtl-1 single mutants have ~0.4x whole-body Mg2+ [PMID:20221407].
- Decisions:
  - IBA monoatomic cation channel activity -> MODIFY to calcium channel activity + calcium-activated
    cation channel activity (both descendants of GO:0005261; GTL-1's own data).
  - IBA metal ion transport / monoatomic cation transmembrane transport -> MODIFY to calcium ion and
    magnesium ion transmembrane transport (consistent with the gon-2 review).
  - IEA membrane -> MODIFY to plasma membrane; IBA plasma membrane ACCEPT.
  - Defecation IMP/IGI -> KEEP_AS_NON_CORE (consistent with gon-2 review).
  - No NEW process terms: nociception/cold response and Mg2+ homeostasis rest on phenotypes; Mg2+
    transport is captured by the transport term in core_functions.
- Curation gaps (not knowledge gaps): no GOA annotation yet from PMID:32009965 (HEK293 calcium-activated
  channel), from PMID:16054081 (Mg2+/Ni2+ uptake), or from PMID:22483941/PMID:32009965 (PVD sensory
  roles).

## 2026-10-28 PR review fixes

Extended the truncated deep-research-manual quote 'Plasma-membrane activity follows from' through the patch-clamp evidence.
