# cryabb (alpha-crystallin B chain b) — curation notes

Zebrafish cryabb (cryab2, hspb5b, alphaB2-crystallin; UniProt A0A8M9Q8E3) is the broadly
expressed alphaB-crystallin paralog. Primary source: Smith et al. 2006 [PMID:16420472
"RT-PCR showed that alphaB2-crystallin is expressed predominantly in lens but, reminiscent of
mammalian alphaB-crystallin, also has lower constitutive expression in heart, brain, skeletal
muscle and liver."]. The 2026-09-27 session migrated the review off obsolete GO:0051082
(issue #2222) and proposed a holdase chaperone activity NTR.

## Re-review 2026-09-29

Validation before edits: 1 error (5 yaml rows no longer in GOA) and 3 PENDING rows.

What changed and why:

- Removed the five rows absent from the refreshed GOA: GO:0051082 IBA and IDA (obsolete;
  the IDA was migrated by ZFIN to GO:0140309), GO:0005212 IEA via GO_REF:0000120,
  GO:0009892 IEA, GO:0046872 IEA.
- GO:0140309 unfolded protein holdase activity (IDA, new row): MODIFY -> holdase chaperone
  activity NTR. The assay is the classic holdase readout [PMID:16420472 "The chaperone-like
  activity of purified recombinant alphaB2 protein was assayed by measuring its ability to
  prevent the chemically induced aggregation of alpha-lactalbumin and lysozyme."], but the
  term definition (checked via QuickGO) is still a carrier activity that "escorts it to an
  acceptor molecule or to a specific location", which was not tested (go-ontology#30552).
  Same replacement as the GO:0042026 protein refolding IBA row, so actions are consistent.
- GO:0005886 plasma membrane (IEA, ARBA, new row): REMOVE. No signal/TM features, no UniProt
  SUBCELLULAR LOCATION line, ZFIN ND for CC; cryabb is a soluble lens protein [PMID:16420472
  "2D gel electrophoresis indicated that alphaB2-crystallin makes up approximately 0.16% of
  total zebrafish lens protein."].
- GO:0005212 structural constituent of eye lens (IEA, InterPro, new row): KEEP_AS_NON_CORE;
  GO:0005198 structural molecule activity (IEA, ARBA): ACCEPT -> MARK_AS_OVER_ANNOTATED
  (generic parent, minor lens component, activity is chaperoning).
- ZFIN morphant IMP rows (PMID:25866181, abstract-only, cryabb not named in the abstract;
  curator deferred to): GO:0007519 skeletal muscle tissue development ACCEPT ->
  KEEP_AS_NON_CORE and GO:0060047 heart contraction ACCEPT -> KEEP_AS_NON_CORE (downstream
  tissue/organ phenotypes); GO:0030239 myofibril assembly kept ACCEPT as the process where
  the holdase does the work [PMID:25866181 "targeted ablation of MFM genes in zebrafish led
  to compromised skeletal muscle function mostly due to myofibrillar degeneration as well as
  severe heart failure."]. core_functions.directly_involved_in trimmed accordingly.
- Added two cached papers: Elicker & Hutson 2007 [PMID:17888590 "In response to a one-hour
  heat shock at 37°C, we found the expression of several sHSPs, hspb1, hspb4, hspb8, hspb9 ,
  and hspb11 , to be upregulated more than five-fold"] (cryabb = hspb5b is not in that list,
  so zebrafish heat induction is modest) and Park et al. 2023 [PMID:37577747 "Our data
  suggest that cryabb functions as a stress–response gene regulated by both glucocorticoid
  stress and oxidative stress."; "the loss of αB-crystallin function is associated with a
  cardiac phenotype that presents as embryonic cardiac edema"]. Used for GO:0009408 (ACCEPT,
  argued from the sHSP node placement), GO:0060047 and GO:0036438.
- Rewrote all templated summaries/reasons, replaced deep-research-only support with primary
  quotes where available, added reference_review to every PMID, rewrote description
  (removed UniProt keyword commentary), added suggested_questions/experiments.

Validation after edits: zero errors, zero warnings. Open point: no zebrafish localization
experiment exists (ZFIN ND), and the muscle evidence is morpholino-only.
