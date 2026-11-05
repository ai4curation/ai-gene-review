# KhtT curation notes

## 2026-11-04

Normally fetched O07535/BACSU; all five original rows and raw sources pinned before review. Falcon was attempted and failed with HTTP 403 authentication; research here is manual.

PMID:33790011 directly compares KhtTU with KhtU alone in everted vesicles. KhtU is active without KhtT; apo-KhtT is a brake and c-di-AMP weakens that restraint. This updates the older UniProt wording “Required for activity” derived from PMID:14987767 and PMID:17679694. The assay demonstrates pH-dependent activation of the complex and direct binding to KhtT, not c-di-AMP binding to KhtU. No independent antiporter function or obligatory-complex contribution is assigned to KhtT.

GO:0141108 (transporter regulator activity), GO:0043266 and GO:0180001 were verified in QuickGO on 2026-11-04. Transport annotations are corrected to the executed regulatory role, not removed as duplicates. The two plasma-membrane annotations are consistent with peripheral association on the cytosolic face. PAINT donor count is not used to judge support. The initial version omitted new annotation rows; the PR review follow-up below supersedes that choice. The core functions support the KhtT receptor branch of MODULE:bacterial_c_di_amp_signaling; downstream KhtU transport is outside that module boundary.

Required `just paint-losses BACSU khtT` was attempted; the PANTHER tree lookup did not return in the initial observation window. Current lineage-loss status remains UNKNOWN. This limitation does not negate the target-specific complex/localization evidence; no claim of verified absence of losses is made.

The same PAINT query subsequently completed successfully: no IRD or IKR loss was reported on the O07535 lineage. This supersedes the initial unavailable observation above.

## 2026-11-04 — PR #5997 review follow-up

Added a NEW cyclic-di-AMP binding recommendation supported by direct ITC and structural measurements, distinct from transporter regulation. [PMID:33790011 "We have confirmed c-di-AMP binding to KhtT and determined the crystal structure of this complex."] This preserves all five source annotation payloads and adds one experimentally demonstrated molecular activity.
