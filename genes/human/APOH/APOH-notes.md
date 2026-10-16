# APOH (beta2-glycoprotein I) notes

## Biology
- beta2GPI is an abundant plasma glycoprotein of unknown physiological function [PMID:16480936; PMID:32759297]. It is the main antigen in the antiphospholipid syndrome (APS).
- Core: binds anionic phospholipids (major PL-binding site in domain V) [PMID:15486070]; inhibits contact activation of the intrinsic pathway [PMID:4052628].
- Partners:
  - LDLR-family LA modules bind domain V [PMID:20223219].
  - PF4 [PMID:19805618]; apo(a) kringle IV [PMID:9269765]; MBL at domains II and IV [PMID:32759297].
  - Plasminogen: beta2GPI is a cofactor for tPA activation [PMID:16480936]; plasmin-nicked beta2GPI binds plasminogen kringle 5 and inhibits plasmin generation [PMID:14726399].
- Nicked beta2GPI is anti-angiogenic [PMID:17872974].
- PMID:222615 and PMID:7417307 have no abstract in the cache, only titles. Rows from them are kept as non-core with title quotes.

## GOA calls
- **Protein binding:**
  - Plasminogen and apo(a) → MODIFY to kringle domain binding.
  - PF4 → chemokine binding.
  - LDLR and mouse Lrp8 → LDL particle receptor binding.
  - MBL → REMOVE: no term fits binding a lectin at a non-carbohydrate site.
  - Y2H screen hits (LAMP2, SH3GLB1) → REMOVE.
- **Intrinsic coagulation (IDA) → MODIFY** to negative regulation of the intrinsic pathway.
- **Positive regulation of coagulation (TAS) → over-annotated:** the pro-thrombotic effect is the antibodies'.
- **Triglyceride transport (IDA/ISS) → over-annotated:** the evidence is clearance and LPL activation.
- **Lipid binding → MODIFY** to lipoprotein particle binding.
- **Non-core:** LPL rows, lipoprotein particle CC rows, fibrinolysis, plasminogen activation, anti-angiogenic, anti-apoptotic.
- Review round (PR #4160):
  - GO:0030195 → MODIFY to GO:2000267 (its is_a descendant, same finding).
  - Platelet dense granule → UNDECIDED.
  - Lrp8 → GO:0070325.
  - PMID:25081279 (thrombosis variant with less anticoagulant capacity) added as support.
