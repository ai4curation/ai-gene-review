# ROT1 curation notes

## 2026 IBA re-review

Re-checked the four current ROT1 IBA annotations against GOA, the cached
`PTHR28090` PAINT table, and the cached Rot1 literature:

- `GO:0005789 endoplasmic reticulum membrane`, tracing to `PANTHER:PTN001999053`
- `GO:0006458 'de novo' protein folding`, tracing to `PANTHER:PTN001999053`
- `GO:0007118 budding cell apical bud growth`, tracing to `PANTHER:PTN001999057`
- `GO:0051082 unfolded protein binding`, tracing in GOA to `PANTHER:PTN001999053`

All four rows list the S. cerevisiae target `SGD:S000004813` as a descendant
evidence, which is expected for a target-supported PAINT node. The ER membrane
and de novo folding rows are core Rot1 annotations and now carry
`NO_FAILURE_CORE`. The apical bud-growth row is experimentally observed in
S. cerevisiae but downstream of ER proteostasis and cell-wall defects, so it now
carries `NO_FAILURE_NON_CORE`.

The unfolded-protein binding IBA needed a different PAINT review. GOA still
reports the row with `PANTHER:PTN001999053`, but the current `PTHR28090` PAINT
cache no longer contains `GO:0051082` at that node; it retains ER membrane and
de novo protein folding instead. The underlying biology remains Rot1's
antiaggregation and ER folding-support activity [PMID:18508919], so the action
stays `MODIFY` to `GO:0044183 protein folding chaperone`, while the structured
IBA root cause is `SOURCE_STALE_OR_MISSING`.

The newer-paper search found a 2025 peer-reviewed version of the 2024 UPR
preprint discussed in the Falcon report. Bartolutti et al. used inducible Rot1
as a UPR-independent ER chaperone to maintain euploid UPR-deficient populations
[PMID:40846641], which is consistent with the chaperone model but does not
change any of the four IBA decisions.
