# PA3170 (MTA deaminase, Q9HZ64) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HZ64 --alias PA3170`; accession matches the worklist. No
deep-research provider used. Both papers cached with full text.

### Literature

- [PMID:23050701 "The substrate specificity reveals PA3170 protein to be a specific MTA deaminase."]
  MTA kcat 24.6 per s, Km 1.5 uM; adenosine kcat/Km 3.7 x 10^5 per M per s (40-fold lower); inactive
  on adenine, SAH, guanosine. Only MTA-acting activity in extracts; crystal structure with MTCF.
- [PMID:23968233 "The four enzymes from sg-2 can deaminate MTA but not SAH."] (Pa3170 is in sg-2.)
- PAO1 has a separate adenosine deaminase, PA0148 (listed among the candidate deaminases in
  PMID:23050701).

### Annotation decisions

- GO:0090614 (IDA): ACCEPT, core.
- GO:0004000 (IDA, PseudoCAP seed): KEEP_AS_NON_CORE; genuine secondary activity.
- GO:0019239 (IBA, IEA), GO:0016787, GO:0016810, GO:0016814 (IEA): TOO_GENERAL (GO:0090614 is_a all of them).
- Action counts: ACCEPT 1, KEEP_AS_NON_CORE 1, TOO_GENERAL 5. No source defects.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN005182504 | GO:0019239 deaminase activity | 5 | 82 (64 taxa) | GO:0004000 adenosine deaminase activity, IDA, PMID:23050701 (PseudoCAP); also GO:0090614 IDA PMID:23968233 (CACAO) | SOUND | Full text read; purified-enzyme kinetics on adenosine. The adenosine activity is secondary, but it does support the generic node term, which suits an amidohydrolase clade deaminating different adenine compounds. | Xcc2270 Q8P8H1, MJ1541 Q58936, Tm0936 Q9X034, Bc1793 Q81F14 | Yes |
