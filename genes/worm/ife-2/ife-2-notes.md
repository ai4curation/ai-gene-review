# ife-2 review notes

- Fetched Q21693 (Swiss-Prot IF4E2_CAEEL, WBGene00002060, GeneID 180393): matches requested.
- Literature compiled in ife-2-deep-research-manual.md (no deep-research API).
- Key decisions:
  - Core MF: m7G cap binding + TMG cap binding [PMID:9553113 "binding of IFE-1 and IFE-2
    to m7GTP-Sepharose was inhibited by m32,2,7GTP"]; translation initiation factor activity;
    BP translational initiation; CC cytoplasm, eIF4F complex (IBA).
  - RNA binding (IEA InterPro) -> MODIFY to the two cap-binding terms (is_a RNA cap binding
    is_a RNA binding, checked with OAK).
  - positive regulation of translation (IMP x2): the evidence is reduced global protein
    synthesis on loss of a core cap-binding factor; this is participation in translation
    initiation, not regulation. MODIFY to translational initiation, with source_defects
    (WRONG_TERM, SUSPECTED, CHECK).
  - lifespan / embryo development: KEEP_AS_NON_CORE (downstream phenotypes of a translation
    factor).
  - negative regulation of response to oxidative stress: MARK_AS_OVER_ANNOTATED; resistance
    phenotype of a loss-of-function in a general translation factor does not show IFE-2
    regulates the stress response (abstract-only paper).
  - stress granule: KEEP_AS_NON_CORE (stress-conditional).
  - No NEW terms: meiotic crossover (PMID:20530576) and TORC1 postembryonic growth
    (PMID:23705068) evidence is mutant phenotype only; the work is done by MSH-4/5 and TORC1.
  - Conflict: PMID:30282029 (P bodies) vs PMID:25061667 (SG, not PBs) - suggested question.
