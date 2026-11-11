# Eef1a1 (rat) review notes

## Session 1 (CREATE)
- Fetched P62630; 66 GOA rows. No deep research API available; manual summary in
  Eef1a1-deep-research-manual.md.
- Read full text: PMID:19501573, PMID:31468715, PMID:21390260, PMID:20797626. Others abstract-only.
- Core: translation elongation factor activity, GTPase activity, translational elongation,
  cytosol / cytosolic ribosome. ACCEPTed across IBA/IEA/ISO/ISS.
- MODIFY: tRNA binding -> alpha-aminoacyl-tRNA binding (GO:1904678); mRNA binding -> mRNA 3'-UTR
  binding (GO:0003730) [PMID:19501573 "We conclude that a 5-bp internal stem in the MT-1 3'UTR is critical for binding of eEF1alpha and histidine-tRNA ligase, and that binding of eEF1alpha is facilitated through domains I and III."];
  cytoplasm -> cytosol; ribosome -> cytosolic ribosome; translation (IBA) -> translational elongation.
- Identical protein binding (IPI, PMID:19501573): over-annotated; the paper only speculates about
  multimeric RNA binding by domain I [PMID:19501573 "Domain I generated a second complex of slower migration, suggesting that it may bind as a multimer."]
- Positive regulation of neuron projection development (IMP, PMID:21390260): over-annotated;
  [PMID:21390260 "In contrast, treatment with eEF1A1 RNAi or the negative control of eEF1A1 RNAi alone did not alter the NGF-induced neurite outgrowth in PC12 cells"]
- IEP response terms (xenobiotic, NGF): expression readouts only -> over-annotated.
- GO:1903427 (IMP, PMID:23041468): paper is about EF-Tumt (Tufm, RGD:1305501); QuickGO shows the PMID
  annotated only to Eef1a1. UNDECIDED + source_defect WRONG_GENE_PRODUCT (PROBABLE) to RGD.
- Calmodulin binding ISO: donor mouse IDA cites PMID:12384497 (Leishmania EF-1alpha/SHP-1); cannot
  verify -> UNDECIDED.
- NOT nucleus ISO vs positive nucleus ISO/ISS: conflict; positive kept as non-core (EGF/ZPR1),
  NOT left UNDECIDED. The resulting consistency warning is deliberate.
- No NEW terms proposed (necessity/expression evidence only for extra processes).

## 2026-10-28: nucleus action consistency

- Re-examined the GO:0005634 rows. The two positive rows (ISO, ISS) and the NOT row (ISO,
  negated) are opposite claims, not one claim. Kept the positive rows KEEP_AS_NON_CORE
  (conditional EGF/ZPR1-driven nuclear entry) and the NOT row UNDECIDED, which is the
  resolution docs/action_consistency.md prescribes for a positive/NOT conflict; expanded the
  NOT row's reason to say so.
- A consistency_exception does not help: the action_consistency check reports no conflict for
  this pair (it flagged the exception as stale), and the older `inconsistent_review_actions`
  check ignores both `negated` and `consistency_exception`. The remaining warning is therefore a
  validator limitation, not a curation inconsistency. Status stays DRAFT per update-status.
