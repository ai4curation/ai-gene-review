# Mapk8 (rat, P49185) review notes

## Session 1 (initial review)

- `just fetch-gene rat Mapk8` resolved P49185 (MK08_RAT); 134 GOA rows seeded.
- No deep-research provider available; literature summary written by hand in
  `Mapk8-deep-research-manual.md` from cached publications and the UniProt record.
- Full text read: PMID:16618812, PMID:18188153, PMID:24475223, PMID:29166604, PMID:9487126,
  PMID:19332540. All others abstract-only.
- PMID:19332540 (palmitate, H4IIEC3 hepatocytes): shows JNK activation by mitochondrial ROS
  and rescue of insulin signalling by SP600125 [PMID:19332540 "These results suggest that JNK
  activation by palmitate contributed to palmitate-induced insulin resistance."]. Pan-JNK
  pharmacology only; does not establish that JNK1 (vs JNK2) is responsible, so no NEW
  annotation (e.g. negative regulation of insulin receptor signalling) was proposed from it.
- Mouse-sourced ISO rows were traced to their mouse (Q91Y86) source annotations in QuickGO
  to judge them (e.g. GO:0004712 came from a mouse IMP, PMID:29153991, which cannot show
  tyrosine kinase specificity -> MARK_AS_OVER_ANNOTATED).

### Key decisions
- General kinase MF rows (protein kinase, kinase, protein Ser/Thr kinase activity) -> MODIFY
  to GO:0004707 MAP kinase activity (already carried). MAPK cascade and stress-activated MAPK
  cascade -> MODIFY to GO:0007254 JNK cascade (already carried).
- GO:0097050 type B pancreatic cell apoptotic process (IMP, PMID:24475223) -> MODIFY to
  GO:2000675 negative regulation of type B pancreatic cell apoptotic process: JNK1 shRNA
  increased apoptosis [PMID:24475223 "These data suggest that JNK1 protects against palmitate
  and high glucose-induced β-cell apoptosis associated with reduced ER and mitochondrial
  stress."].
- Four bare protein binding rows (c-Jun, Syt4, GluR2L, GluR4 - all JNK1 substrates) -> REMOVE
  per protein-binding policy.
- Over-annotated: GO:0034349 glial cell apoptotic process (IEP), GO:0048666 neuron
  development (IEP), GO:0060395 SMAD protein signal transduction (IMP), GO:0035033 HDAC
  regulator activity, GO:0004712 Ser/Thr/Tyr kinase activity, broad gene-expression and
  protein-metabolism regulation terms.
- Kinesin binding (PMID:18932217) left UNDECIDED: abstract does not show direct binding.
- No NEW terms proposed. Candidate process terms from perturbation data (insulin signalling,
  autophagy) failed the strict NEW bar: pharmacology not isoform-specific, or JNK1 acts upstream
  via substrates already covered by kinase terms.
- Apoptosis-related regulation rows kept as non-core; sign is context dependent in rat cells
  (pro-apoptotic: PMID:11259632, PMID:12534344, PMID:14997384; protective: PMID:24475223,
  PMID:15309413).
