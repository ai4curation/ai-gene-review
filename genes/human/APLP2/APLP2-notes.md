# APLP2 notes

## Biology
- APLP2 is an APP-family type I TM glycoprotein [PMID:8485127].
- APP/APLP homo- and heterodimers promote trans-cellular adhesion; endogenous APLP2 is needed for adhesion of mouse fibroblasts [PMID:16193067].
- The KPI domain inhibits trypsin-like proteases, including factor XIa and kallikreins [PMID:8307156].
  - It is a competitive mesotrypsin inhibitor that is also a slow mesotrypsin substrate [PMID:25301953].
- The NPXY tail binds the Fe65-family PTB domains [PMID:8855266; PMID:9461550].
- With Mint3 and Taz/Yap, it forms transcriptionally active complexes [PMID:21178287].
- Redundant with APP:
  - Double knockouts are mostly lethal postnatally; APLP2 single knockouts are normal, with no olfactory axon outgrowth defect [PMID:9461064].
  - NMJ transmission and LTP require both [PMID:21522131].

## GOA calls
- **Protein binding (24 rows):**
  - APP and APLP1 → MODIFY to protein dimerization activity (matching the APLP1 review) plus cell adhesion molecule binding.
  - Fe65-family → MODIFY to PTB domain binding. Mint3 → REMOVE (review round): the APLP2-Mint3 interface is not mapped.
  - MED12 (abstract-only AICD paper) → UNDECIDED.
  - ITM2B, a reproducible retina IP-MS hit → REMOVE, since there is no informative term (the validator rejects KEEP on bare protein binding).
  - Y2H/AP-MS screen hits → REMOVE.
- **DNA binding (NAS, homology to mouse CDEBP) and GPCR signaling (NAS, predicted G(o) motif) → MARK_AS_OVER_ANNOTATED.**
- **Non-core:** nucleus; secretory compartments (ER lumen, platelet alpha granule, exosome); heparin and metal binding IEA; axonogenesis IBA.
- Review round (PR #4158):
  - CNS development IBA → KEEP_AS_NON_CORE, consistent with axonogenesis: the phenotypes appear only in APP/APLP2 double knockouts and concern synaptic function.
  - Identical protein binding added as a core function.
  - Correctness left unset on PMID:16193067 because its erratum content is unknown.
