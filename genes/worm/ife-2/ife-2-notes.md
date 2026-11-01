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

## 2026-10-28 correction (PR #5672 review)

The two positive regulation of translation (GO:0045727, IMP) rows are now ACCEPT, not MODIFY to
translational initiation, and their WRONG_TERM source defects are withdrawn. PMID:20530576 (full text)
shows IFE-2 is needed for the temperature-dependent polysome shift of msh-4/him-14, msh-5 and spo-11
mRNAs and the matching rise in MSH-5 protein at 25 C, while gpd-3 and zhp-3 mRNAs do not shift
[PMID:20530576 "These results indicate that efficient translation of spo-11, msh-4/him-14, msh-5 and zhp-3 mRNAs at 25°C depends on the presence of IFE-2."].
That mRNA-selective upregulation is what GO:0045727 describes, so the claim holds even though the two
rows' own papers report only reduced bulk synthesis. GO:0045727 is added to the third core function.
