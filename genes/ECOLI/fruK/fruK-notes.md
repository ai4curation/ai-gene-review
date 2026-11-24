# fruK notes

## 2026-10-02

Seeded `fruK` with `just fetch-gene ECOLI fruK`, yielding 9 GOA annotations. The review follows the existing PSEPK `fruK` action pattern but anchors the exact activity in the E. coli record.

### Main function

FruK/P0AEW9 is the cytosolic 1-phosphofructokinase that follows the FruA/FruB fructose PTS. UniProt records the exact ATP-dependent beta-D-fructose 1-phosphate to beta-D-fructose 1,6-bisphosphate reaction as `RHEA:14213` and EC 2.7.1.56, with experimental support from the E. coli Fru1PK purification paper. The cached PMID:10833389 entry is abstract-only, so the review accepts EcoCyc's full-text IDA judgment while using UniProt's curated reaction as the exact reaction anchor.

### Process annotation

`PMID:4579702` directly supports the `GO:0006001 fructose catabolic process` row: the fructose 1-phosphate kinase mutant could not grow on fructose or fructose 1-phosphate, while the parent strain could. The broader `GO:0005975 carbohydrate metabolic process` InterPro row was therefore modified to `GO:0006001`.

### Broad molecular-function rows

The PAINT `GO:0008443 phosphofructokinase activity` row was kept as non-core because PTN001317471 is correctly substrate-generic across PfkB-family 1- and 6-phosphofructokinases. The ARBA `GO:0008443` row, `GO:0016301 kinase activity`, and `GO:0016773 phosphotransferase activity, alcohol group as acceptor` are lower-specificity electronic calls for the FruK reaction and were modified to `GO:0008662 1-phosphofructokinase activity`, which GOA already carries from both EcoCyc IDA evidence and RHEA/EC-based IEA evidence.


## 2026-11-06 comparative fructose-PTS review

Reviewed all original annotation rows and complete biological scope. Payloads, row order and source bytes are preserved. Broad true terms were refined rather than called over-annotated. No new GO annotation is proposed solely to fill a pathway diagram. Current GO definitions were checked against QuickGO; net phosphohistidine-donor transport and the immediate phosphocysteine step are compatible descriptions of one group-translocation mechanism.

A genuine default Falcon attempt failed with HTTP403; no provider report was fabricated. The review is based on cached primary literature, curated source statements and sequence/domain evidence.

Full PMID38723750 reveals a critical construct boundary: the purified pET3a FruK gifted from the PMID10833389 study differs from P0AEW9 and matches reported Salmonella FruK sequences. Separate constructs are EHEC; native growth used BW25113/Keio and endogenous pull-down used strain3.300. Reverse activity was inferred from ATP production with an ADP/F1,6BP-dependent luciferase assay; it is not a direct canonical-K12 in-vivo flux measurement. Cra binding is real, but the paper treats altered operator binding, looping and transcriptional outcomes as hypotheses. No bare protein-binding or unproven co-regulator GO assertion is added. A 2025 structure search hit (PMC12585703) is a conference abstract, not a full structural primary report, and is not used as decisive evidence.
