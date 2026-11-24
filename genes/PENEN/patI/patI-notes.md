# patI (Penicillium expansum) notes

## 2026-10-01 re-review (GOA refresh)

- Four IEA rows are no longer present in the current GOA snapshot and were marked
  `retired: true` (reviews retained): GO:0004497 monooxygenase activity (GO_REF:0000120),
  GO:0016491 oxidoreductase activity (GO_REF:0000043), GO:0043386 mycotoxin biosynthetic
  process (GO_REF:0000117), GO:0046872 metal ion binding (GO_REF:0000043).
- Current replacements reviewed: GO:0004497 via GO_REF:0000002 (InterPro2GO) ACCEPT;
  GO:0044550 secondary metabolite biosynthetic process (ARBA, GO_REF:0000117)
  KEEP_AS_NON_CORE (general parent of patulin biosynthesis).
- New EXP row GO:0005789 ER membrane (PMID:30680886) ACCEPTed (abstract-only cache; defer
  to curator).
- Replaced placeholder supporting_text quotes (citation header "Epub 2019 Mar 6...",
  "See deep research file...") with verbatim abstract/UniProt text; the proposed new term's
  support was re-pointed to the UniProt FUNCTION text (not present in the abstract-only cache).
- Still no GO term for 3-hydroxybenzyl alcohol hydroxylase activity (RHEA:62212); proposal kept.
