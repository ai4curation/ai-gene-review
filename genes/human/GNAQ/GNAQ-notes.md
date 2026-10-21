# GNAQ notes

## Deep research
- `just deep-research-falcon human GNAQ --fallback perplexity-lite` failed (providers unavailable,
  2026-10-21). Notes from cached publications and UniProt P50148.

## Function
- Gq-class heterotrimeric G protein alpha subunit. UniProt: "The alpha subunit has a low GTPase activity
  that converts bound GTP to GDP, thereby terminating the signal" and GNAQ activates PLC-beta "leading to
  production of diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP3)" (PMID:37991948).
- "Gαq increases the catalytic rate constant, kcat, of PLCβ3" [PMID:37991948]; PLC-β3 bound to activated
  Gα(q) structure; PLC-β3 is also a GAP for Gαq [PMID:20966218].
- Couples to many Gq-coupled receptors (CCKBR, NK3R, CaSR, MRGPRX2/X4, GPR142, proton-sensing GPCRs, KISS1R,
  NmU receptors) - all receptor-specific pathway annotations reflect the shared transducer role.
- Direct inhibition of TRPM8 by activated Gαq [PMID:22750945].
- Gq + beta-arrestin-1 required for AT1R-driven RhoA activation [PMID:15611106] (not GAP activity).
- Oncogenic Q209L/R183 mutants drive uveal melanoma via ARF6 [PMID:27265506].

## Localization
- "targeted to the cytoplasmic face of the plasma membrane through reversible lipid palmitoylation";
  DHHC3/7 palmitoylate; "Galpha(q) rapidly shuttles between the plasma membrane and the Golgi apparatus"
  [PMID:19001095]. Palmitoylation (Cys9/Cys10) needed for membrane association [PMID:9175863, G11 study].
- Conclusion: intracellular, peripheral on the cytoplasmic (inner) leaflet of the PM; Golgi shuttling pool.
  Not surface-exposed.

## Curation issues
- GTPase activator activity IDA (PMID:15611106): term means GAP; paper shows RhoA activation, so wrong sense.
- Glucose homeostasis ISS donor is mouse Gpr142 (MGI:2668437), a receptor, not a GNAQ homolog.
- AC-activating GPCR signaling IBA is inconsistent with Gq biology (Gq activates PLC-beta, not adenylyl cyclase).
