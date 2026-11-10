# Ttpa notes (rat, P41034)

## Session 2026-10-28
- Fetched with `just fetch-gene rat Ttpa`; accession P41034 confirmed (RGD:3915, GeneID 25571).
- 33 GOA rows. Cached extra papers: PMID:23599266 (Kono 2013 PIP-gated release), PMID:34563650
  (Arai & Kono 2021 review), PMID:9199513 (Hosomi 1997 ligand specificity). Only PMID:22147702 is
  full text; the rest are abstract-only.
- Core: alpha-tocopherol binding [PMID:1569384 "indicating the specificity of the binding"] and
  intermembrane transfer [PMID:8349655 "enhances its transfer between separate membranes"],
  released at PI(4,5)P2-containing target membranes [PMID:23599266 "PIPs in the target membrane
  promoted the intermembrane transfer of α-tocopherol by α-TTP"].
- Decisions:
  - vitamin binding (IDA) MODIFY to vitamin E binding.
  - PI bisphosphate binding IBA MODIFY to PI(4,5)P2 / PI(3,4)P2 binding.
  - cytoplasm MODIFY to cytosol; late endosome MODIFY to cytoplasmic side of late endosome membrane
    (GO:0098560), matching PMID:14531858 wording.
  - vitamin E metabolic process: transport is not metabolism, over-annotation (all three rows).
  - placenta, amyloid-beta clearance, BBB: downstream consequences of systemic vitamin E deficiency
    in KO mice; over-annotated.
  - intracellular pH reduction (IDA, PMID:22147702 full text): alpha-TTP prevents CQ accumulation
    and so preserves low pH; it does not reduce pH. MARK_AS_OVER_ANNOTATED + source_defects
    (WRONG_TERM, RGD, SUSPECTED, CHECK).
- No NEW process terms proposed (NEW bar).
