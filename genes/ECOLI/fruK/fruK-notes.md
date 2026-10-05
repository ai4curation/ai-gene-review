# fruK notes

## 2026-10-02

Seeded `fruK` with `just fetch-gene ECOLI fruK`, yielding 9 GOA annotations. The review follows the existing PSEPK `fruK` action pattern but anchors the exact activity in the E. coli record.

### Main function

FruK/P0AEW9 is the cytosolic 1-phosphofructokinase that follows the FruA/FruB fructose PTS. UniProt records the exact ATP-dependent beta-D-fructose 1-phosphate to beta-D-fructose 1,6-bisphosphate reaction as `RHEA:14213` and EC 2.7.1.56, with experimental support from the E. coli Fru1PK purification paper. The cached PMID:10833389 entry is abstract-only, so the review accepts EcoCyc's full-text IDA judgment while using UniProt's curated reaction as the exact reaction anchor.

### Process annotation

`PMID:4579702` directly supports the `GO:0006001 fructose catabolic process` row: the fructose 1-phosphate kinase mutant could not grow on fructose or fructose 1-phosphate, while the parent strain could. The broader `GO:0005975 carbohydrate metabolic process` InterPro row was therefore modified to `GO:0006001`.

### Broad molecular-function rows

The PAINT `GO:0008443 phosphofructokinase activity` row was kept as non-core because PTN001317471 is correctly substrate-generic across PfkB-family 1- and 6-phosphofructokinases. The ARBA `GO:0008443` row, `GO:0016301 kinase activity`, and `GO:0016773 phosphotransferase activity, alcohol group as acceptor` are lower-specificity electronic calls for the FruK reaction and were modified to `GO:0008662 1-phosphofructokinase activity`, which GOA already carries from both EcoCyc IDA evidence and RHEA/EC-based IEA evidence.
