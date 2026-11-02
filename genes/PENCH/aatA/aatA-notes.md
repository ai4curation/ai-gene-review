# aatA (Penicillium chrysogenum) notes

## 2026-10-01 re-review (GOA refresh)

- Five IEA rows are no longer present in the current GOA snapshot and were marked
  `retired: true` (reviews retained): GO:0005777 peroxisome (GO_REF:0000043),
  GO:0005782 peroxisomal matrix (GO_REF:0000044), GO:0016740 transferase activity
  (GO_REF:0000043), GO:0016746 acyltransferase activity (GO_REF:0000043), GO:0017000
  antibiotic biosynthetic process (GO_REF:0000043). These keyword/SubCell-mapping rows
  were dropped upstream; peroxisomal matrix is now delivered via GO_REF:0000120
  (ARBA + SubCell), which was reviewed and ACCEPTed.
- New EXP rows for GO:0050640 isopenicillin-N N-acyltransferase activity (PMID:2110531,
  purified enzyme converts IPN to Pen G; PMID:1368505, ACT activity after heterologous
  cluster expression) were ACCEPTed.
- Replaced off-target suggested questions/experiments (amino acid / nitrogen metabolism,
  structure determination already done in PMID:20223213) with IAT-specific ones.
- Replaced several non-verbatim supporting_text snippets (core function and
  deep-research/bioinformatics placeholders) with verbatim quotes.
- Open question: the NEW proposal GO:0008234 cysteine-type peptidase activity models a
  single-turnover Ntn-hydrolase autoprocessing event; GO:0097264 self proteolysis alone may
  be sufficient. Left in place pending expert opinion.
