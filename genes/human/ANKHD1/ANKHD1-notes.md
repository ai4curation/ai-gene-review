# ANKHD1 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANKHD1 is MASK1, one of two human homologs of fly Mask; ANKRD17 is MASK2 (PMID:23333314).
  - In human cells it complexes with YAP and co-purifies TEAD3.
  - Its knockdown lowers TEAD reporter activity and YAP targets (CTGF, ANKRD1, FN1, CYR61) without changing non-targets.
  - Fly Mask is on target promoters with Yorkie and Scalloped (PMID:23333315).
- **IBA GO:0090575 (Pol II transcription regulator complex, fly Mask donor):** ACCEPT. It is supported for the human protein too.
- **IBA GO:0045087 innate immune response (donor: the paralog ANKRD17):** MARK_AS_OVER_ANNOTATED. The propagation was PROPAGATION_BAD / WRONG_ORTHOLOG_OR_PARALOG in round 1 and is UNRESOLVED from round 2; see below.
  - ANKHD1 binds NOD2, but its knockdown does not change NOD2-NF-kB signaling (PMID:27812135, full text).
  - This is a single readout, so not REMOVE.
- **NEW GO:0045944** positive regulation of transcription by RNA polymerase II (IMP, PMID:23333314). Comparator: fly Mask carries GO:0045944 (IGI).
- **Protein-binding IPIs removed:** NOD2 (real but with no measured function) and NFKBIE ×2 (proteome-scale screens).
- **RNA binding:** KH domain plus mRNA-capture HDAs, accepted. One renal-cancer study reports miRNA binding (PMID:29695508).
- **Errata:**
  - PMID:21988832's erratum is an author-name fix.
  - PMID:14743216's 2004 erratum has no PubMed record and could not be read, so its correctness is unset.
- **Not used from affinage:** the single-group cancer claims (SMYD3, CDK4, RBM39), and, corrected in round 2, a structural membrane-deformation study (PMID:31255983) that is not a cancer claim.

## 2026-10-04 round 2 (reviewer comments on #4073)

- **Propagation reviews now carry source_entities.**
  - GO:0090575 (accepted): PTN001506277 and fly Mask both SUPPORTS_TRANSFER.
  - GO:0045087: the same node is UNRESOLVED, and the paralog ANKRD17 is SUPPORTS_SOURCE_BUT_NOT_TARGET.
- **Innate immunity: PROPAGATION_BAD changed to UNRESOLVED.** ANKRD17's donor IDA (PMID:23711367) is in myeloid and epithelial cells. The only ANKHD1 negative is a HEK293T reporter with co-transfected NOD2, so the settings don't match. MARK_AS_OVER_ANNOTATED stays.
- **RNA binding:** added as a second core function (GO:0003723), supported by the KH-domain RIP result (PMID:29695508, now quoted from the abstract rather than the title) and mRNA capture. RNA binding is isoform-restricted: VSP_028456 removes residues 628-2542, so isoforms 2 and 3 lack the KH domain.
- **Other fixes:**
  - The NFKBIE REMOVE reasons now name each source's method.
  - The p21 repression (PMID:25483783) and membrane-deformation (PMID:31255983) papers are accounted for in the affinage reference_review.
