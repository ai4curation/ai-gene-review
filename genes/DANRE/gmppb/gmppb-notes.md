# Notes for DANRE gmppb

## 2026-05-09 review notes

- Core function is mannose-1-phosphate guanylyltransferase activity producing GDP-mannose [PMID:23768512 "GMPPB catalyzes the formation of GDP-mannose from GTP and mannose-1-phosphate"].
- Glycoprotein biosynthesis is retained because GDP-mannose is required for protein glycosylation and zebrafish knockdown reduces DAG1/alpha-dystroglycan glycosylation [PMID:23768512 "reduced glycosylation of α-DG"].
- Muscle and neuron development terms are kept non-core as downstream phenotypes of impaired glycosylation [PMID:35006422 "enzymatic activity of GMPPB mutants correlates with muscular and neuronal phenotypes in zebrafish"].

## Re-review 2026-09-29

Starting state: valid with 1 warning (3 PENDING rows); reasons were one-liners repeated across
rows and the same five quotes (including deep-research paraphrases) were attached to unrelated
terms.

Resolved the 3 PENDING rows:

- GO:0004475 (IBA, PTN000500861): ACCEPT. Single-activity family with yeast, Candida,
  Arabidopsis, human and zebrafish donors; the target's presence in its own WITH/FROM marks
  the EXP grounding rather than circularity.
- GO:0005737 cytoplasm (IBA, PTN000500804): ACCEPT. GDP-mannose synthesis is cytosolic; no
  signal peptide or anchor in UniProt. Added as the `locations` entry of the core function,
  which previously had none.
- GO:0005575 cellular_component (ND): ACCEPT. Accurate statement that no experimental
  localization exists for zebrafish gmppb; not in conflict with the cytoplasm IBA inference.

Action changes and arguments:

- GO:0009101 glycoprotein biosynthetic process (IMP, PMID:23768512): ACCEPT ->
  KEEP_AS_NON_CORE, matching the IBA row for the same term, which had been non-core. The
  participation test decides it: gmppb makes the donor sugar, the mannosyltransferases do the
  glycosylation. Hypoglycosylation on knockdown [PMID:23768512 "reduced glycosylation of α-DG"]
  demonstrates necessity, which is what supplying a substrate means.
- GO:0016740 transferase activity kept MODIFY to GO:0004475; GO:0005525 GTP binding kept
  non-core, now argued as substrate binding within the annotated catalytic activity rather than
  a switch function.
- The four developmental IMP rows (skeletal muscle, muscle cell, neuron development) stay
  KEEP_AS_NON_CORE, now with the rescue evidence quoted [PMID:35006422 "GMPPB V111G mutant with
  decreased activity fails to rescue axonal phenotype in gmppb MO-injected zebrafish."; "Thus,
  enzymatic activity of GMPPB might be a critical determinant for phenotypes of zebrafish."],
  which shows the phenotypes track catalytic competence and so are downstream of the metabolic
  step.
- GO:0004475 EXP (PMID:33986552): kept ACCEPT, with a note that the enzymology is on the human
  GMPPA-GMPPB complex while the same paper's in vivo test is in zebrafish [PMID:33986552
  "disruption of the interactions between GMPPA and GMPPB or the binding of GDP-Man to GMPPA in
  \nzebrafish leads to abnormal brain development and muscle abnormality"]. This is the
  ECO:0000269 source behind the UniProt catalytic activity.
- Replaced the repeated boilerplate supporting_text with term-specific quotes throughout; kept
  one deep-research quote (Mg2+/mannose-1-P dependence of the assay) because it adds assay
  detail absent from UniProt.
- Added reference_review to all 3 PMIDs (PMID:23768512 and PMID:33986552 are abstract-only
  caches, noted), rewrote the description (mechanism, GMPPA feedback, zebrafish expression
  profile, phenotypes) and the core function, and filled the empty questions and experiments.

Validation after edits: zero errors, zero warnings.
