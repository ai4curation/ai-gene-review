# actI-ORF2 / KSβ / CLF (Q02062, SCO5088) — review notes

Part of the **BGC exemplar curation project** (`projects/BGC.md`). MIBiG BGC0000194
(*Streptomyces coelicolor* A3(2), actinorhodin type II PKS). GenBank CAC44201.1 →
UniProt **Q02062** (ACTI2_STRCO), gene *actI-ORF2* / SCO5088.

## Function

ActI-ORF2 is the **chain-length factor (CLF, KSβ)** of the actinorhodin minimal
type II PKS. It is the **non-catalytic** partner of the ketosynthase (ActI-ORF1,
KSα): together they form the heterodimeric KS-CLF that polymerizes the actinorhodin
polyketide chain, with CLF determining the chain length.

- "Although CLF regulates chain length, it does not have an active site; KS must
  catalyze both chain initiation and elongation." [PMID:15286722]
- The polyketide is elongated "inside an amphipathic tunnel approximately 17 Å in
  length at the heterodimer interface"; the first cyclization occurs within the
  KS-CLF tunnel. [PMID:15286722]
- KSβ/CLF descends from a ketosynthase but lacks the active-site cysteine, so it is
  catalytically dead — directly analogous to PqsB in PqsBC (see `genes/PSEAE/pqsB`).

## Annotation issues

- GO:0016746 acyltransferase activity (IEA) and GO:0016747 acyltransferase activity,
  transferring groups other than amino-acyl groups (IEA) → both
  **MARK_AS_OVER_ANNOTATED**: these attribute catalytic MF to a subunit with no
  active site. CLF `contributes_to` the KS-CLF activity / should be annotated to the
  complex, not as `enables`.

Add (NEW, via core_functions): **GO:0034082 type II polyketide synthase complex**
(CC) and **GO:1901112 actinorhodin biosynthetic process** (BP) — currently missing
from the GOA despite being well established.

## Predicted-complex evidence (BGC project)

Moriwaki et al. (bioRxiv 2025.10.26.684697) predict the KSα–KSβ/CLF heterodimer
(BGC0000194; CAC44200.1/CAC44201.1) at **ipTM 0.96**, matching PDB 1TQY.

## References
- PMID:15286722 — Keatinge-Clay et al. 2004, Nat Struct Mol Biol (act KS-CLF
  structure, PDB 1TQY). VERIFIED.
