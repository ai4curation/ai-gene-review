# mobA curation notes

## 2026-07-20 OpenScientist report assessment

The generated OpenScientist report is retained unchanged as provider output but is
assessed as `MISCITED` for target-level curation. Its one-MGD reaction agrees with
reviewed Q88HA3 UniProt, and it correctly states that no direct target-specific
experiment was found. However, it assigns `moaA` to PP_2123 (actually `moeA`) and
a `moeA`-family gene to PP_1294 (actually `moaE`). It also conflates the single
MobA guanylyltransferase reaction with bis-MGD assembly, delivery, and predicted
client-enzyme roles, while presenting unsaved alignment, motif, neighborhood,
MobB-absence, and client analyses as target evidence. Those claims are not
propagated.

The curated core function remains the optional downstream transfer of one GMP from
GTP to Mo-MPT to produce MGD. It is grounded in the reviewed target UniProt record
and the local PANTHER subfamily export; insertion, client-enzyme maturation, and
terminal cofactor assembly remain outside this review's direct-function claim.

## 2026-11-10 completion for the MoCo biosynthesis module

Aligned with the new ECOLI/mobA review:

- GO:0006777: ACCEPT -> MODIFY to GO:1902758. The draft accepted the broad term to avoid
  asserting bis-MGD assembly, but GO:1902758 is already accepted here (TreeGrafter batch-05
  verdict, unchanged), so the broad term is correct-but-general.
- GO:0019720: MARK_AS_OVER_ANNOTATED -> MODIFY to GO:1902758 (the draft's reason argued
  generality, which is a MODIFY).
- Added supported_by to GTP binding (FT BINDING, E. coli cocrystal PMID:10978347) and cytoplasm
  (HAMAP subcellular location); removed the reference entry that quoted the GOA table itself.
- PTHR19136 IBA of GO:0016779 (on E. coli MobA) is correct but general for MobA; the KT2440 row
  is an ARBA/TreeGrafter IEA and stays MODIFY to GO:0061603.
