# fruK notes

## 2026-10-02

Seeded `fruK` with `just fetch-gene ECOLI fruK`, yielding 9 GOA annotations. The review follows the existing PSEPK `fruK` action pattern but anchors the exact activity in the E. coli record.

### Main function

FruK/P0AEW9 is the cytosolic 1-phosphofructokinase that follows the FruA/FruB fructose PTS. UniProt records the exact ATP-dependent beta-D-fructose 1-phosphate to beta-D-fructose 1,6-bisphosphate reaction as `RHEA:14213` and EC 2.7.1.56, with experimental support from the E. coli Fru1PK purification paper. The cached PMID:10833389 entry is abstract-only, so the review accepts EcoCyc's full-text IDA judgment while using UniProt's curated reaction as the exact reaction anchor.

### Process annotation

`PMID:4579702` directly supports the `GO:0006001 fructose catabolic process` row: the fructose 1-phosphate kinase mutant could not grow on fructose or fructose 1-phosphate, while the parent strain could. The broader `GO:0005975 carbohydrate metabolic process` InterPro row was therefore modified to `GO:0006001`.

### Broad molecular-function rows

The PAINT `GO:0008443 phosphofructokinase activity` row was kept as non-core because PTN001317471 is correctly substrate-generic across PfkB-family 1- and 6-phosphofructokinases. The ARBA `GO:0008443` row, `GO:0016301 kinase activity`, and `GO:0016773 phosphotransferase activity, alcohol group as acceptor` are lower-specificity electronic calls for the FruK reaction and were modified to `GO:0008662 1-phosphofructokinase activity`, which GOA already carries from both EcoCyc IDA evidence and RHEA/EC-based IEA evidence.

## 2026-11-05 completion pass (Claude, AI-assisted)

- Deep research: `just deep-research ECOLI fruK --provider perplexity` was tried once and failed
  ("Provider 'perplexity' not available. Available: falcon, openscientist, claude_code"). No
  provider deep-research file exists for this gene; the review rests on the cached publications
  and the curated UniProt record.
- `GO:0008443 phosphofructokinase activity` rows (IBA and ARBA IEA) made consistent as
  `TOO_GENERAL`. The PAINT node PTN001317471 is soundly placed: its IBD seeds are FruK
  (P0AEW9, this gene, expected because of its own experimental activity) and the PfkB-type
  6-phosphofructokinases P06999 and P9WID3, so the substrate-generic term is the right
  common denominator at that node. For FruK itself the accepted child `GO:0008662` entails
  it, and UniProt records the enzyme as "specific for fructose-l-phosphate" (Ref.6).
  The previous split (IBA KEEP_AS_NON_CORE, IEA MODIFY) violated same-term consistency.
- `GO:0016301 kinase activity` and `GO:0016773 phosphotransferase activity, alcohol group
  as acceptor` changed from MODIFY to `TOO_GENERAL`: both are is_a ancestors of the accepted
  `GO:0008662`, so the specific term already exists rather than needing to be proposed.
- Replaced a UniProt `DE` EC-number quote (a label, not evidence) with the experimentally
  attributed CC FUNCTION statement. All rows now carry vetted supporting text; status COMPLETE.
