# Curated entries outside their reference proteomes

Generated: 2026-10-18T22:54:14.286362+00:00. Scope: genes/POPTR.

Select **live Swiss-Prot accessions** in our local gene-review set whose **exact NCBI taxon** has a UniProt reference proteome, but whose accession belongs to none of those reference proteomes. All local review statuses, including drafts, are included; duplicate accessions are counted once.

## Summary

- Local review files: **141**; unique identifiers: **141**.
- Live Swiss-Prot: **141**; unreviewed: **0**; unresolved accessions: **0**.
- RNAcentral/non-protein identifiers: **0** (excluded from Swiss-Prot audit).
- Swiss-Prot already in an exact-taxon reference proteome: **135**.
- Swiss-Prot with no exact-taxon reference proteome: **0** (excluded; this can be expected for non-reference species/strains).
- **Candidates: 6 accessions across 1 taxa.**
- Local GOA available for **6/6** candidates; **0** have partial cache coverage.
- Cached GOA rows: **34**, including **1 non-IEA**, **0 experimental**, and **0 NOT** rows.

## GO evidence on candidate accessions

These are original cached GOA annotation rows, regardless of our review decisions. Reviewer-proposed NEW annotations are excluded. Exact duplicate rows across caches are counted once per accession. Non-IEA is not synonymous with experimental; IBA remains separately visible as phylogenetic curation. Missing caches are unknown, not zero.

| Evidence code | Annotation rows |
| --- | ---: |
| IEA | 33 |
| ISS | 1 |

## Candidate entries

| Accession | Local gene | Organism | Protein | Reference proteome(s) | Other proteome membership | GOA rows | Non-IEA | Experimental | Evidence counts | Links |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| [A9PCL4](https://www.uniprot.org/uniprotkb/A9PCL4/entry) | [POPTR/PRX2](https://github.com/ai4curation/ai-gene-review/blob/main/genes/POPTR/PRX2/PRX2-ai-review.yaml) | [Populus trichocarpa](https://www.uniprot.org/taxonomy/3694) | Peroxiredoxin-2 | [UP000006729](https://www.uniprot.org/proteomes/UP000006729) | None | 5 | 0 | 0 | IEA: 5 | [GOA](https://www.ebi.ac.uk/QuickGO/annotations?geneProductId=UniProtKB%3AA9PCL4) |
| [O65862](https://www.uniprot.org/uniprotkb/O65862/entry) | [POPTR/CCOAOMT1](https://github.com/ai4curation/ai-gene-review/blob/main/genes/POPTR/CCOAOMT1/CCOAOMT1-ai-review.yaml) | [Populus trichocarpa](https://www.uniprot.org/taxonomy/3694) | Caffeoyl-CoA O-methyltransferase 1 | [UP000006729](https://www.uniprot.org/proteomes/UP000006729) | None | 3 | 0 | 0 | IEA: 3 | [GOA](https://www.ebi.ac.uk/QuickGO/annotations?geneProductId=UniProtKB%3AO65862) |
| [O65922](https://www.uniprot.org/uniprotkb/O65922/entry) | [POPTR/CCOAOMT2](https://github.com/ai4curation/ai-gene-review/blob/main/genes/POPTR/CCOAOMT2/CCOAOMT2-ai-review.yaml) | [Populus trichocarpa](https://www.uniprot.org/taxonomy/3694) | Caffeoyl-CoA O-methyltransferase 2 | [UP000006729](https://www.uniprot.org/proteomes/UP000006729) | None | 3 | 0 | 0 | IEA: 3 | [GOA](https://www.ebi.ac.uk/QuickGO/annotations?geneProductId=UniProtKB%3AO65922) |
| [P16579](https://www.uniprot.org/uniprotkb/P16579/entry) | [POPTR/WIN6](https://github.com/ai4curation/ai-gene-review/blob/main/genes/POPTR/WIN6/WIN6-ai-review.yaml) | [Populus trichocarpa](https://www.uniprot.org/taxonomy/3694) | Acidic endochitinase WIN6 | [UP000006729](https://www.uniprot.org/proteomes/UP000006729) | None | 7 | 0 | 0 | IEA: 7 | [GOA](https://www.ebi.ac.uk/QuickGO/annotations?geneProductId=UniProtKB%3AP16579) |
| [P34105](https://www.uniprot.org/uniprotkb/P34105/entry) | [POPTR/MAOX](https://github.com/ai4curation/ai-gene-review/blob/main/genes/POPTR/MAOX/MAOX-ai-review.yaml) | [Populus trichocarpa](https://www.uniprot.org/taxonomy/3694) | NADP-dependent malic enzyme | [UP000006729](https://www.uniprot.org/proteomes/UP000006729) | None | 7 | 0 | 0 | IEA: 7 | [GOA](https://www.ebi.ac.uk/QuickGO/annotations?geneProductId=UniProtKB%3AP34105) |
| [P45730](https://www.uniprot.org/uniprotkb/P45730/entry) | [POPTR/PAL](https://github.com/ai4curation/ai-gene-review/blob/main/genes/POPTR/PAL/PAL-ai-review.yaml) | [Populus trichocarpa](https://www.uniprot.org/taxonomy/3694) | Phenylalanine ammonia-lyase | [UP000006729](https://www.uniprot.org/proteomes/UP000006729) | None | 9 | 1 | 0 | IEA: 8; ISS: 1 | [GOA](https://www.ebi.ac.uk/QuickGO/annotations?geneProductId=UniProtKB%3AP45730) |

## Interpretation and requested follow-up

Please check whether these curated accessions should be linked to the reference proteome, or whether another accession represents the same locus/sequence. If a TrEMBL counterpart exists, assess sequence equivalence and preservation of experimentally supported and other non-IEA GO annotations before changing the accession used in our reviews.

Absence of an accession does **not** establish absence of its gene, sequence, or GO annotations from the reference proteome, and does not imply planned deletion from Swiss-Prot. This report has not mapped alternative accessions or measured unique annotation loss. Different strains and descendant taxa are not treated as the same taxon.

## Provenance

UniProt release(s): 2026_03. API retrieval range: 2026-10-18T21:56:15.004855+00:00 to 2026-10-18T21:56:16.074111+00:00.

Membership uses the UniProtKB Proteomes cross-references and the Proteomes API's reference classification. API query caches expire after seven days; `--refresh` fetches anew and `--offline` reuses dated caches. Network/pagination failures abort instead of inferring absence. The CSV records GOA source paths and SHA-256 hashes; annotation dates below are GOA DATE values, not download timestamps.

| Accession | Local GOA source | GOA annotation date range | Cache status |
| --- | --- | --- | --- |
| A9PCL4 | [genes/POPTR/PRX2/PRX2-goa.tsv](https://github.com/ai4curation/ai-gene-review/blob/main/genes/POPTR/PRX2/PRX2-goa.tsv) | 20260601–20260601 | available |
| O65862 | [genes/POPTR/CCOAOMT1/CCOAOMT1-goa.tsv](https://github.com/ai4curation/ai-gene-review/blob/main/genes/POPTR/CCOAOMT1/CCOAOMT1-goa.tsv) | 20260227–20260428 | available |
| O65922 | [genes/POPTR/CCOAOMT2/CCOAOMT2-goa.tsv](https://github.com/ai4curation/ai-gene-review/blob/main/genes/POPTR/CCOAOMT2/CCOAOMT2-goa.tsv) | 20260227–20260428 | available |
| P16579 | [genes/POPTR/WIN6/WIN6-goa.tsv](https://github.com/ai4curation/ai-gene-review/blob/main/genes/POPTR/WIN6/WIN6-goa.tsv) | 20260601–20260601 | available |
| P34105 | [genes/POPTR/MAOX/MAOX-goa.tsv](https://github.com/ai4curation/ai-gene-review/blob/main/genes/POPTR/MAOX/MAOX-goa.tsv) | 20260428–20260428 | available |
| P45730 | [genes/POPTR/PAL/PAL-goa.tsv](https://github.com/ai4curation/ai-gene-review/blob/main/genes/POPTR/PAL/PAL-goa.tsv) | 20211209–20260428 | available |
