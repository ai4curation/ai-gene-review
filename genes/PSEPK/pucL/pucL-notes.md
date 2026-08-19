# pucL curation notes

## 2026-08-19

- Q88F12 has exact OHCU-decarboxylase support from RHEA:26301, EC 4.1.1.97,
  IPR017580, PTHR43466:SF1, and the PAINT IBD node PTN000044713
  [file:PSEPK/pucL/pucL-uniprot.txt "Xref=Rhea:RHEA:26301";
  file:interpro/panther/PTHR43466/PTHR43466-paint.tsv
  "PTN000044713\tGO:0051997\tF\tIBD"].
- GO:0019628 and GO:0051997 are core. GO:0000255 is retained as non-core
  product-level context because PucL forms allantoin but is specifically the
  terminal OHCU-decarboxylation step of urate catabolism
  [file:PSEPK/pucL/pucL-uniprot.txt "Purine metabolism; urate degradation;
  (S)-allantoin from urate: step 3/3"].
- The OpenScientist report independently recovers the exact OHCU-decarboxylase
  role and explicitly says the target lacks a direct experimental study. Its
  homolog-derived cytoplasmic, homodimeric, and His73 claims remain hypotheses.
  More importantly, its pathway-completeness section overlooks the
  COG3748/IPR010389 Q88F11/PP_4289 candidate and incorrectly declares the urate
  entry step a divergent, unannotated hole. That conclusion was rejected rather
  than propagated into this review or module.
