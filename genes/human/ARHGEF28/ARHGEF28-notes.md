# ARHGEF28 (RGNEF / p190RhoGEF) notes

## Biology
- GEF for RhoA but not Rac1 or Cdc42 [PMID:11058585]; RhoB and RhoC were not tested there, and the abstract does not state the species:
  - The DH/PH module activates RhoA, not Rac1 or Cdc42; the full-length protein is autoinhibited in vitro.
  - Localized to cytosol, microtubules and plasma membrane.
- Rgnef knockout fibroblasts: lose integrin-stimulated RhoA activation, focal adhesions and migration [PMID:22649559].
- GEF-independent FAK scaffolding at early adhesions [PMID:24006257].
- Active RhoA and Rac1 bind the PH domain and stimulate exchange [PMID:29196061].
- From the affinage record, not used for annotation: NEFL mRNA binding, ALS, TDP-43.

## GOA calls
- **ACCEPT:** GEF activity (EXP/IBA/IEA/TAS); regulation of Rho signal transduction (IBA); cytosol; plasma membrane.
- **Non-core:** small GTPase-mediated signal transduction (IBA), regulation of small GTPase signalling (TAS) and cytoplasm, all general parents.
- **Ephrin receptor signaling (Reactome TAS) → UNDECIDED:** no study reviewed here links RGNEF to ephrin receptors.
- **IBA node PTN002677784** (Lbc family). A sibling node, PTN002677811, carries a NOT GEF activity (IRD).
- Review round (PR #4164):
  - The cached Reactome entries were read:
    - R-HSA-3928598: p190RhoGEF binds phospho-FAK in the EphB/FAK spine-morphogenesis branch. The ephrin row is therefore KEEP_AS_NON_CORE (indirect, via FAK).
    - R-HSA-9013023 and R-HSA-9013109 list ARHGEF28 as a GEF for RHOB and RHOC (Jaiswal 2011/2013); those GEF rows now cite them.
  - NEW focal adhesion assembly (IMP) and protein kinase binding (FAK; IPI), forming a second core function for the GEF-independent FAK scaffold. Comparator: talin carries GO:0048041.
  - GO:0005085 is the only GEF term because GO:0005089 was merged into it. The core function lists RHOA as substrate.
- Lesson: the repo caches Reactome entries in reactome/R-HSA-*.md. Read them before calling a Reactome TAS row unverifiable.
