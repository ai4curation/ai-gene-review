# Pgam2 review notes

## Evidence summary
- [UniProtKB:P16290] UniProt describes Pgam2 as catalyzing interconversion of 3- and 2-phosphoglycerate with 2,3-bisphosphoglycerate as primer.
- [PMID:15720133] The fetched GOA file uses this publication for phosphoglycerate mutase activity and gluconeogenesis.

## Curation decisions
- Core function: phosphoglycerate mutase 2 (phosphoglycerate mutase activity, GO:0004619).
- Specific catalytic activities and direct metabolic processes were accepted.
- Broad parent, localization, binding, and stimulus-response annotations were modified, kept non-core, or marked over-annotated according to support.

## Re-review 2026-10-10

- GOA refresh added three rows; none retired. Two ISO rows (GO_REF:0000121) are donor-splits from human PGAM2 (UniProtKB:P15259): GO:0004619 phosphoglycerate mutase activity and GO:0006096 (now labelled "glycolysis" in GO). Both ACCEPT, matching the mouse-donor (MGI:1933118) siblings [UniProtKB:P16290 "Catalyzes the interconversion of 3- and 2-phosphoglycerate with 2,3-bisphosphoglycerate as the primer of the reaction."].
- New GO:1990917 ooplasm IEA (ARBA:ARBA00093730): MARK_AS_OVER_ANNOTATED, consistent with the IDA ooplasm row. The cited localization study is on skeletal muscle [PMID:2158448 "the enzyme was found in both cytosol and nucleus of rat skeletal muscle"]; GO defines ooplasm as "The cytoplasm of an ovum" (QuickGO). The ARBA rule most likely propagates the RGD IDA row.
- Replaced two stale UniProt quotes (DR GO line for GO:0004082 IEA:UniProtKB-EC no longer present) with the FUNCTION CC text.
- Description stripped of review/curation commentary.
- Open question: was the RGD ooplasm IDA (PMID:2158448) intended as sarcoplasm (GO:0016528)? If so, the IDA row and the ARBA rule derived from it should be corrected at source.
