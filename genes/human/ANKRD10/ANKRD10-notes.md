# ANKRD10 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANKRD10 (Q9NXR5) is Tdark. The only functional paper (PMID:40044952, full text) finds that in bladder cancer RBPMS loss shifts ANKRD10 splicing toward ANKRD10-2, which co-activates MYC. It is single-study and isoform-specific, so no NEW term.
- **GOA rows:** HPA nucleoplasm IDA accepted (the only location data). APPBP2 (HI-II-14) and DPP9 (BioPlex) protein-binding IPIs removed.
- **PAINT:** `just fetch-panther-paint PTHR24201` reports 6 annotated nodes and 9 node-level annotations, seeded by other clades (e.g. CDKN2 family, a zebrafish-supported node). ANKRD10 receives no IBA from any of them. Family files committed.
- **Knowledge gap:** MF_DARK, because a location survives review. The process is also unknown.

## 2026-10-04 round 2 (reviewer comments on #4082)

- **Isoform-2 interactome.** UniProt's INTERACTION block (from the cached record) lists 17 binary partners for isoform 2 (Q9NXR5-2), nine of them sequence-specific DNA-binding TFs: FOXI1, OTX1, PATZ1, PITX1, PITX2, POGZ, POU6F2, TLX3 and ZIC1. Only APPBP2 and DPP9 are listed for the canonical isoform.
  - The knowledge-gap boundary and the nucleoplasm reason now use this. It corroborates the nuclear, isoform-2-specific co-regulator picture.
  - The suggested experiment is re-aimed at validating these interactions. Y2H data alone justify no GO term.
- The removed IPI reasons now give the UniProt experiment counts (APPBP2 3, DPP9 2), and the MYC quote is detached from the nucleoplasm ACCEPT.
- **dark_aspect** kept as MF_DARK: a location survives review, so WHOLLY_DARK's "only root/IEA/protein binding survive" does not strictly apply, even though process is also unknown.
