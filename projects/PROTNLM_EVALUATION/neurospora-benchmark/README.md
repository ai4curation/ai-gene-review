---
title: Neurospora benchmark data and reproduction
autolink_gene_symbols: false
---
# Neurospora benchmark data and reproduction

The [20-gene review cohort](../neurospora.md) contains every GO/function-bearing record in the published Neurospora crassa strain 74-OR23-1A subset, plus four explicitly selected localization cases. Selection was retrospective, after inspecting the available predictions. This is a focused biological evaluation, not a random sample or a prospective accuracy benchmark.

## Frozen inputs

- [Manifest](manifest.json): retrieval timestamp, source URLs and SHA-256 checksums of the three snapshot files.
- [Published species subset](snapshot/accessions.tsv): 51 accessions, taxon 367110. The full accession list was reused from the [pombe source snapshot](../pombe-benchmark/snapshot/published-accessions.tsv); the manifest records that provenance and the full-list checksum. Its date is separate from this cohort's live API retrieval.
- [Original API predictions](snapshot/predictions.jsonl.gz): complete JSON responses for all 51 exact accessions, including evidence metadata.
- [Current UniProt records](snapshot/uniprot.jsonl.gz): complete ordinary UniProt responses retrieved alongside the predictions. All 51 were TrEMBL records at retrieval.
- [Current sequences](sequences.fasta): derived from those ordinary records. These are not established as the exact prediction-time inputs.

The original outputs contain 21 GO claims, three function paragraphs and 24 localization claims. Sixteen genes have GO/function output; 18 have only localization output; 17 have names only. The selected 20 genes cover all 21 GO claims, all three paragraphs and ten localization claims. The remaining 31 records stay in the inventory without a claim of completed review.

## Explicit selection and gene identity

[selection.csv](selection.csv) records the 20 accession choices and reasons. The four localization additions are a characterized MAP kinase kinase (mek-1), an AP adaptor beta subunit (NCU09721), an FMO-family protein (NCU06296), and a GNAT-family protein (NCU12035). They sample distinct questions about conserved compartmental roles and the limits of family transfer.

[gene-map.csv](gene-map.csv) preserves accession, NCU locus and review-directory symbol. Most entries use the frozen UniProt primary gene name or NCU identifier. The glt-1 and vtc-4 names are grounded in primary literature: [PMID:24581151](https://pubmed.ncbi.nlm.nih.gov/24581151/) and [the Neurospora VTC study, Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC4664880/). NCU01633 and NCU08110 remain recorded as their locus identifiers.

## Derived tables

- [inventory.csv](inventory.csv): all 51 records and output counts.
- [review-cohort.csv](review-cohort.csv): the selected 20 genes.
- [prediction-statements.csv](prediction-statements.csv): every GO, paragraph and localization claim in the source census.
- [review-predictions.csv](review-predictions.csv): the 34 original statements in the selected cohort.
- [claim-provenance.csv](claim-provenance.csv): the original evidence objects, associated with each emitted claim.
- [summary.json](summary.json): deterministic source and cohort counts.
- [review-inventory.json](review-inventory.json): review coverage, exact IDs/labels, original paragraph retention, localization SL identifiers, source paths, sequence agreement, research reports and histories.

GO claims use PredictionReview YAML sidecars. Function paragraphs and localization claims use separate Markdown reports beside each main review. Localization identifiers are retained as emitted UniProt SL identifiers; a GO identifier attached to an evidence object does not replace the original localization claim. The three output types are not pooled into one accuracy denominator.

## Reproduction

Scripts: [source fetcher](fetch.py), [census derivation](summarize.py), and [review coverage audit](review_inventory.py).

Run from the repository root:

```bash
UV_NO_SYNC=1 uv run python projects/PROTNLM_EVALUATION/neurospora-benchmark/summarize.py
UV_NO_SYNC=1 uv run python projects/PROTNLM_EVALUATION/neurospora-benchmark/review_inventory.py
```

The first command verifies the snapshot checksums and exact accession/taxon joins, then derives the tables using the explicit selection and gene-name maps. The second checks coverage and file consistency; it does not assign biological assessments or certify the evidence.

To retrieve updated sources without replacing this benchmark:

```bash
UV_NO_SYNC=1 uv run python projects/PROTNLM_EVALUATION/neurospora-benchmark/fetch.py --out-dir /tmp/neurospora-new-snapshot
```

The output directory must be new or empty. This fetches source records only; it does not choose a new cohort. Reconcile accession/name changes and the manual selection explicitly before creating derived tables for a new snapshot.

For each gene, use `just validate NEUCR GENE`, and use `just validate-predictions PATH` for its GO sidecar where present. Research includes generated reports where available and explicitly labeled manual research reports where provider calls failed. Consequential findings are assessed against the underlying papers, sequence features and comparative evidence; a report's verdict alone does not establish a prediction.
