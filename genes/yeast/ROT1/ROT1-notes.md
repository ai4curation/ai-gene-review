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

The unfolded-protein binding IBA needed a different PAINT review. GOA used to
report the row with `PANTHER:PTN001999053`, but the 2026-10-01 live GOA no
longer contains any `GO:0051082` row and the current `PTHR28090` PAINT cache no
longer contains `GO:0051082` at that node; it retains ER membrane and de novo
protein folding instead. The underlying biology remains Rot1's antiaggregation
and ER folding-support activity [PMID:18508919], so the action stays `MODIFY`
to `GO:0044183 protein folding chaperone` on a retired historical row, while
the structured IBA root cause is `SOURCE_STALE_OR_MISSING`.

The newer-paper search found a 2025 peer-reviewed version of the 2024 UPR
preprint discussed in the Falcon report. Bartolutti et al. used inducible Rot1
as a UPR-independent ER chaperone to maintain euploid UPR-deficient populations
[PMID:40846641], which is consistent with the chaperone model but does not
change any of the four IBA decisions.

## 2026-10-01 current GOA refresh

`just fetch-gene yeast ROT1 --force` refreshed the live source to 22 GOA rows.
It backfilled qualifiers and current `WITH/FROM` entities on the 20 matching
historical rows, seeded two SGD rows from PMID:18508919, and left three
historical `GO:0051082 unfolded protein binding` rows unmatched by live GOA.

- Accepted the newly seeded `GO:0006458 'de novo' protein folding` IPI row for
  the KRE6 client (`SGD:S000006363`).
- Accepted the newly seeded `GO:0044183 protein folding chaperone` IPI row.
  This is the live SGD replacement for the older, generic `GO:0051082` molecular
  function rows.
- Marked the old `GO:0051082` IBA, IDA, and IMP rows `retired: true` rather
  than silently dropping their historical source assertions.

The newer-paper search through 2026-10-01 also found Janik et al. 2026
[PMID:42042339], which studies Candida albicans Rot1 and can complement an
S. cerevisiae rot1 deletion when its CUG codon is repaired for the S. cerevisiae
code. I cached and recorded it as cross-fungal context; it does not add a new
direct S. cerevisiae GO annotation.
