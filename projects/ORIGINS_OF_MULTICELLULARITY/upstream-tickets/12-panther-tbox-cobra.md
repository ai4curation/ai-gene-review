# PANTHER / TreeGrafter, PTHR11267: Capsaspora Brachyury classification and an animal developmental term

**Destination:** PANTHER team (pantherdb.org feedback), copied to PAINT curators.

**Summary.**
1. **Subfamily.** PANTHER classifies *Capsaspora* Brachyury (CoBra,
   A0A0D2VUC6, CAOG_005512) in **PTHR11267:SF181 "OPTOMOTOR-BLIND PROTEIN"**,
   a Tbx2-class name. Sebe-Pedros et al. 2013 (PMID:24043797) place CoBra at
   the base of the Brachyury class. CoBra also has the Brachyury-specific
   arginine at the position of Xenopus Brachyury K149
   (`projects/ORIGINS_OF_MULTICELLULARITY/capsaspora-tbox/RESULTS.md`).
2. **Graft-node term.** TreeGrafter grafts CoBra onto node PTN000137774. In
   the PANTHER tree API this is a duplication node whose leaves come from 34
   organisms, all animals (from *Trichoplax* and *Nematostella* to human). It
   carries `GO:0001708` cell fate specification. In QuickGO that term reaches
   5 *Capsaspora* T-box proteins and 3 ichthyosporean proteins.

**Evidence.**
- No experiment links any unicellular T-box protein to cell fate.
- In *Xenopus*, CoBra activates mesendodermal genes without the target
  selectivity of animal Brachyury (PMID:24043797).

**Requested change.**
- Revisit the SF181 assignment of A0A0D2VUC6.
- Keep animal developmental IBDs off unicellular grafts (see
  [ticket 10](10-treegrafter-qc-rule.md)).

**Repo references.** `genes/CAPO3/CoBra/CoBra-ai-review.yaml` (REMOVE).
