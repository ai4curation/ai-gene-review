# E1BL04 (bovine XIRP2) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 prediction files were not opened or used.

### Sources
- The deep-research file `E1BL04-deep-research-falcon.md` failed. It contains "no contexts were retrieved" / "System error" and has no usable content, so it was not used.
- Cached via `just fetch-pmid`: PMID:17046827, 25772365, 37294664, 20360251, 17766470. PMID:15454575 was already cached.
- QuickGO (2026-10-20) was used to identify the experimental donors behind the IEA/IBA rows: human XIRP2 A4UGR9 and mouse Xirp2 Q4U4S6.

### Identity
- E1BL04 is an unreviewed 3561-aa product, PANTHER PTHR22591:SF1 (XIRP2). It aligns over 99% of human XIRP2 A4UGR9 (3374 aa) at 80.5% identity, against 36-38% for XIRP1 (`E1BL04-bioinformatics/RESULTS.md`).
- It is not a fragment. It lacks the C-terminal LIM domain/CTD present in mouse Xirp2 isoform 1 (Q4U4S6-1, LIM 3255-3315) and in the short stereocilia isoform (XEPLIN, isoform 3), so it is the LIM-less long isoform class (like human canonical A4UGR9).
- There are two other unreviewed bovine XIRP2 entries, A0AAA9SWG7 (936 aa) and A0AAA9SUE1 (957 aa), which may be short-isoform models.

### Evolutionary grounding
- PAINT node PTN000502290 is family-level, spanning SF1 and SF2. Its seeds are A4UGR9 (human XIRP2) and Q702N8 (human XIRP1). The earlier review wrongly called Q702N8 "mouse Xirp2". The IBD for actin filament organization (GO:0007015) is seeded by XIRP1 only. It is accepted because XIRP2-specific evidence agrees: the Xin-repeat properties are identical [PMID:15454575 "Human XIRP2 contains 28 Xin repeats with properties identical to those of Xin"], and the knockout disorganizes stereocilia actin [PMID:25772365 "At an ultrastructural level, the paracrystalline actin filaments became disorganized."].
- Ensembl Compara donors are mouse Xirp2 (Z disc and alpha-actinin binding, IDA, PMID:17046827; cell-cell junction, IDA, PMID:37294664; regulation of actin filament organization, IMP, PMID:25772365; positive regulation of protein localization, IMP, PMID:37294664) and human XIRP2 (stress fiber, focal adhesion and actin filament binding, IMP, PMID:15454575).
- PMID:37294664 assigns gamma-actin recruitment to stereocilia gaps to the short-isoform LIM/CTD [PMID:37294664 "The C-terminal domain (CTD) of XIRP2 is sufficient to pull down monomeric γ-actin."]. That region is absent from E1BL04, so GO:1903829 is marked as over-annotated (domain-architecture mismatch).
- Mouse knockout phenotypes (cardiac development, ventricular septum, conduction) were not proposed as process annotations, because they are necessity evidence.

### Changes vs previous review
- actin binding, actin cytoskeleton organization, cell junction and anchoring junction: changed from MARK_AS_OVER_ANNOTATED/KEEP_AS_NON_CORE to MODIFY, refined to actin filament binding, actin filament organization and cell-cell junction.
- positive regulation of protein localization: kept as MARK_AS_OVER_ANNOTATED, with a domain-architecture reason added.
- NEW: intercalated disc (GO:0014704), a location supported by the mouse ortholog [PMID:20360251 "The Xin repeat-containing proteins mXinalpha and mXinbeta localize to the intercalated disc of mouse heart"].
- Added PMID references and the bioinformatics comparison. The description was rewritten without claims of bovine-specific experiments.

### PANTHER family review
- `interpro/panther/PTHR22591/PTHR22591-review.yaml` places E1BL04 in SF1, which agrees. There is no subfamily disagreement.

### Modules
- No module in `modules/` covers Xin proteins, sarcomere/Z disc, intercalated disc or stereocilia.
