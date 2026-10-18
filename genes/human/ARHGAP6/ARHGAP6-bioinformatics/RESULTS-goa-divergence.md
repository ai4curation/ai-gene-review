# ARHGAP6 bioinformatics: UniProt vs GOA, and what depends on the gap

## Question

The UniProt flat file for ARHGAP6 lists three BHF-UCL phospholipase annotations
that do not appear in the QuickGO/GOA download this review is seeded from. Since
`just fetch-gene` builds `existing_annotations` from the GOA TSV, a row missing
there is never reviewed at all. **Is the divergence real, is it just term
obsolescence, and does anything downstream still depend on the missing rows?**

## Method

`check_goa_uniprot_divergence.py` diffs UniProt's GO cross-reference block
against the QuickGO annotation API for the same accession, then for each
divergent term asks two further questions from live data:

1. **Is the term obsolete?** Checked against **two independent services** --
   OLS4 and `api.geneontology.org`. These are known to disagree about
   obsolescence, so a verdict is only issued when they agree; a disagreement is
   printed as a disagreement rather than resolved to one service's answer.
2. **Does anything cite the missing annotation?** GOA records the source of an
   inferred annotation in WITH/FROM, so the script queries QuickGO for
   annotations *in any species* whose WITH/FROM names `O43182` for that term.
   A non-zero count means a projection is still being served whose stated human
   source no longer exists in the human record.

```
uv run check_goa_uniprot_divergence.py
uv run check_goa_uniprot_divergence.py --self-test
```

## Result (run 2026-09-18)

UniProt cross-references: **15** GO terms. QuickGO/GOA: **14** distinct GO terms. Shared: **12**.

### In UniProt, absent from GOA

| GO id | label [UniProt evidence] | obsolete? (OLS4 / GO API) | verdict | rows citing O43182 in WITH/FROM for this term |
|---|---|---|---|---|
| GO:0016004 | F:phospholipase activator activity [IDA:BHF-UCL] | active / active | active | **2** |
| GO:0043274 | F:phospholipase binding [IPI:BHF-UCL] | active / active | active | **2** |
| GO:0141214 | P:positive regulation of phospholipase C/protein kinase C signal transduction [IDA:BHF-UCL] | active / active | active | **2** |

Rows citing `O43182` for **GO:0016004**:

- `UniProtKB:A0A8I6AAE4 (Arhgap6, taxon 10116) ISO GO_REF:0000121`
- `UniProtKB:O54834 (Arhgap6, taxon 10090) ISO GO_REF:0000119`

Rows citing `O43182` for **GO:0043274**:

- `UniProtKB:A0A8I6AAE4 (Arhgap6, taxon 10116) ISO GO_REF:0000121`
- `UniProtKB:O54834 (Arhgap6, taxon 10090) ISO GO_REF:0000119`

Rows citing `O43182` for **GO:0141214**:

- `UniProtKB:A0A8I6AAE4 (Arhgap6, taxon 10116) ISO GO_REF:0000121`
- `UniProtKB:O54834 (Arhgap6, taxon 10090) ISO GO_REF:0000119`

### In GOA, absent from UniProt's cross-reference block

- GO:0005515 protein binding
- GO:0007165 signal transduction

## Interpretation

**The divergence is not term obsolescence.** 3 of the 3
terms present only in UniProt are live terms on both services checked, so GOA
dropping them is not the ontology retiring them.

**And the missing rows are still load-bearing.** For `GO:0016004`, `GO:0043274`, `GO:0141214`, GOA is currently serving
annotations in other species whose WITH/FROM column names `O43182` as the
source -- for a term `O43182` itself no longer carries in GOA. Those
projections are orphaned: the human annotation they were derived from is
not in the human record any more.

For the review this has a concrete consequence. Because the workflow seeds
`existing_annotations` from the GOA TSV, these annotations would silently
never be reviewed. They are therefore entered in the review as `NEW` rows --
not because they are new curation, but because they are pre-existing BHF-UCL
curation that has fallen out of the feed the review is built from.

## Caveats

- The comparison is term-level. Two sources can list the same GO id with
  different evidence codes or qualifiers and still appear to agree here.
- A WITH/FROM count is a count of *rows*, not of independent evidence; several
  rows may be the same projection replicated across species.
- This script establishes that annotations are missing from one feed and cited by
  another. It does not establish *why* they were removed, and does not assume the
  removal was an error.

