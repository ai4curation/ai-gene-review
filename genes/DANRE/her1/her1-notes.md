# her1 (Danio rerio, Q90463) — curation notes

- UniProt Q90463 (TrEMBL, "HER-1 protein", 328 aa); bHLH + Orange domain; PANTHER PTHR10985
  (BASIC HELIX-LOOP-HELIX TRANSCRIPTION FACTOR, HES-RELATED), no subfamily assigned.
- Paralog of her7; together the zebrafish counterparts of amniote Hes7 (segmentation clock).
- Notch target and clock component: [PMID:17535112 "Using transgenic lines of zebrafish expressing
  her1 or her7 under heat-shock control, we confirm the regulatory relationships postulated by the
  model."]
- DNA binding / repression: [PMID:22911291 "Importantly, we found that several H-box sites from the
  dlc, her1, and her7 promoters were bound by Her1 homodimers with comparably high affinity"];
  [PMID:22911291 "Combined, these results indicate that the strongest DNA binding is from Her1
  homodimers and Her7:Hes6 heterodimers; these have similar DNA binding specificity, and each dimer
  has the potential to directly repress dlc, her1, and her7."]
- FGF link via Her13.2 (hes6-related): [PMID:15905406 "augments autorepression of her1 in
  association with Her1 protein"]
- Phenotypes: [PMID:12117818 "indicating that her1 and her7 are necessary for normal somite
  formation"]; [PMID:22723933 "This indicates that the maintenance of r/c polarity in the
  anterior-most somites is regulated through Her1 activity."]; [PMID:16545363 "joint inactivation of
  her1 and her13.2 leads to a complete loss of all somitic borders"].
- IBA nodes: PTN004213585 (nucleus, DNA-binding TF activity, cis-reg DNA binding, neg. reg. of
  transcription by Pol II); PTN000105428 (A/P pattern specification, regulation of neurogenesis).
- Decisions: protein binding (IPI) removed (dimerization captured by heterodimerization term);
  identical protein binding -> protein homodimerization activity; DNA-templated transcription
  marked over-annotated; NEW GO:0001227 (IDA, PMID:22911291).
- Deep research: falcon runs timed out at 600 s (twice), relaunched with --timeout 2400; review
  written from cached full-text publications.
