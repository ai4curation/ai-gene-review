---
title: ProtNLM cross-cohort results
---
# Cross-cohort results

[Project overview](../PROTNLM_EVALUATION.md) · [Source counts](benchmark-summary.json) · [Summary generator](build_benchmark_summary.py) · [Narrative category index](narrative-review-index.yaml)

The scope contains **282 distinct protein records**, including **242 prediction targets** and 40 paired human reference records. Overlapping selections are counted once in the combined totals. These purposive, retrospective cohorts test informative biological distinctions; their proportions do not estimate proteome-wide accuracy.

## GO-term assessments

Each row counted here is one emitted GO term. Narrative functions, protein names and SL localization outputs are excluded. Zero GO PLI or REP judgments does not imply the absence of narrative errors.

| Category | GO claims |
|---|---:|
| COR | 53 |
| CNN | 32 |
| LSP | 83 |
| UNC | 103 |
| NPI | 17 |
| PLI | 0 |
| REP | 0 |
| **Total** | **288** |

## Narrative function reviews

**57 gene/accession review records** assess emitted FUNCTION text. A record may contain multiple paragraphs and multiple claim categories. Each category below counts records with at least one such judgment, once per record; categories overlap and must not be summed or pooled with GO counts. These are neither atomic-claim counts nor one verdict per whole paragraph. Name and localization assessments remain in the gene notes and are outside both denominators.

| Category present in function review | Review records |
|---|---:|
| COR | 1 |
| CNN | 19 |
| LSP | 1 |
| UNC | 25 |
| NPI | 14 |
| PLI | 13 |
| REP | 0 |
| SUPPORTED | 8 |

SUPPORTED records contain an explicitly supported claim whose review does not assign a novelty-specific COR/CNN/LSP category. They are preserved as such. References to separate GO judgments, hypothetical corrections, and claims explicitly not emitted are excluded.

### Individual narrative records

| Gene | Accession | Categories present | Evidence and claim distinctions |
|---|---|---|---|
| ARATH/DRS1 | Q9SAI7 | UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/ARATH/DRS1/DRS1-protnlm-function-review.md) |
| ARATH/FTSH12 | A0A1P8ARD2 | UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/ARATH/FTSH12/FTSH12-protnlm-function-review.md) |
| DANRE/dcxr | Q567K5 | PLI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DANRE/dcxr/dcxr-protnlm-function-review.md) |
| DROME/CG32706 | Q8IRM9 | CNN, UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DROME/CG32706/CG32706-protnlm-function-review.md) |
| DROME/CG5565 | Q9VQ04 | UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DROME/CG5565/CG5565-protnlm-function-review.md) |
| DROME/CG5611 | Q9VB17 | UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DROME/CG5611/CG5611-protnlm-function-review.md) |
| DROME/CycA | M9NFR3 | CNN | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DROME/CycA/CycA-protnlm-function-review.md) |
| DROME/Dic4 | Q9VVS1 | UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DROME/Dic4/Dic4-protnlm-function-review.md) |
| DROME/Gfat1 | A8Y5A1 | NPI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DROME/Gfat1/Gfat1-protnlm-function-review.md) |
| DROME/Lcp3 | A0A0B4KEF3 | LSP, UNC, NPI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DROME/Lcp3/Lcp3-protnlm-function-review.md) |
| DROME/TyrRS | Q9VV60 | CNN | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DROME/TyrRS/TyrRS-protnlm-function-review.md) |
| DROME/awd | A0A0B4LHX6 | CNN | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DROME/awd/awd-protnlm-function-review.md) |
| DROME/dati | Q9V4C9 | CNN | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DROME/dati/dati-protnlm-function-review.md) |
| DROME/ftz-f1 | M9NFK2 | PLI, SUPPORTED | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DROME/ftz-f1/ftz-f1-protnlm-function-review.md) |
| DROME/loqs | X2J5X6 | CNN, NPI, UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DROME/loqs/loqs-protnlm-function-review.md) |
| DROME/qkr58E-1 | Q9W255 | CNN, UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DROME/qkr58E-1/qkr58E-1-protnlm-function-review.md) |
| HORSE/ALG5 | A0A5F5PM72 | PLI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/ALG5/ALG5-protnlm-function-review.md) |
| HORSE/BCAT2 | A0A9L0TSN4 | SUPPORTED | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/BCAT2/BCAT2-protnlm-function-review.md) |
| HORSE/CAPSL | A0A3Q2I3U9 | NPI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/CAPSL/CAPSL-protnlm-function-review.md) |
| HORSE/CXCR3 | A0A9L0T1D1 | PLI, UNC, SUPPORTED | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/CXCR3/CXCR3-protnlm-function-review.md) |
| HORSE/DARS2 | A0A9L0SB67 | UNC, SUPPORTED | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/DARS2/DARS2-protnlm-function-review.md) |
| HORSE/DUOX1 | A0A9L0SQG9 | NPI, UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/DUOX1/DUOX1-protnlm-function-review.md) |
| HORSE/GHSR | F6QF00 | PLI, SUPPORTED | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/GHSR/GHSR-protnlm-function-review.md) |
| HORSE/GPAM | A0A9L0TTC1 | PLI, SUPPORTED | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/GPAM/GPAM-protnlm-function-review.md) |
| HORSE/HSPA4 | A0A9L0S5Z5 | PLI, SUPPORTED | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/HSPA4/HSPA4-protnlm-function-review.md) |
| HORSE/HSPD1 | F6Z587 | PLI, UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/HSPD1/HSPD1-protnlm-function-review.md) |
| HORSE/IRAK3 | A0A3Q2HDT6 | UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/IRAK3/IRAK3-protnlm-function-review.md) |
| HORSE/KRIT1 | A0A9L0SR44 | NPI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/KRIT1/KRIT1-protnlm-function-review.md) |
| HORSE/MYL10 | A0A9L0TJE1 | NPI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/MYL10/MYL10-protnlm-function-review.md) |
| HORSE/SHLD2 | A0A9L0RGD6 | COR, UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/SHLD2/SHLD2-protnlm-function-review.md) |
| HORSE/SIRT5 | F6S899 | UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/SIRT5/SIRT5-protnlm-function-review.md) |
| HORSE/USP8 | A0A9L0T7K6 | SUPPORTED | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/USP8/USP8-protnlm-function-review.md) |
| HORSE/VAPA | A0A3Q2H1L9 | PLI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/VAPA/VAPA-protnlm-function-review.md) |
| NEUCR/NCU04302 | Q1K772 | PLI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/NEUCR/NCU04302/NCU04302-protnlm-function-review.md) |
| NEUCR/NCU04637 | Q7S3B9 | NPI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/NEUCR/NCU04637/NCU04637-protnlm-function-review.md) |
| NEUCR/NCU06005 | Q7S2F2 | CNN, UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/NEUCR/NCU06005/NCU06005-protnlm-function-review.md) |
| SCHPO/cem1 | O94297 | CNN, UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/SCHPO/cem1/cem1-protnlm-function-review.md) |
| SCHPO/mre11 | Q09683 | CNN | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/SCHPO/mre11/mre11-protnlm-function-review.md) |
| SCHPO/rfc3 | O14003 | CNN | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/SCHPO/rfc3/rfc3-protnlm-function-review.md) |
| SCHPO/rpa49 | O14086 | CNN | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/SCHPO/rpa49/rpa49-protnlm-function-review.md) |
| SCHPO/rpo41 | O13993 | CNN | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/SCHPO/rpo41/rpo41-protnlm-function-review.md) |
| SCHPO/rrp36 | Q9P6P2 | CNN | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/SCHPO/rrp36/rrp36-protnlm-function-review.md) |
| SCHPO/spt16 | O94267 | CNN, UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/SCHPO/spt16/spt16-protnlm-function-review.md) |
| SCHPO/sws2 | O59772 | CNN, UNC, NPI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/SCHPO/sws2/sws2-protnlm-function-review.md) |
| SCHPO/vas2 | Q9P7N2 | CNN | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/SCHPO/vas2/vas2-protnlm-function-review.md) |
| SCHPO/yml6 | O74801 | CNN, UNC, NPI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/SCHPO/yml6/yml6-protnlm-function-review.md) |
| XENLA/uap1.S | Q6DCZ6 | PLI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/XENLA/uap1.S/uap1.S-protnlm-function-review.md) |
| human/DTD1 | A0A2R8YCT7 | NPI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/human/DTD1/DTD1-protnlm-function-review.md) |
| human/NARF | J3KS48 | PLI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/human/NARF/NARF-protnlm-function-review.md) |
| human/RHOJ | G3V4H1 | UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/human/RHOJ/RHOJ-protnlm-function-review.md) |
| mouse/Sdhaf2 | A0A494B8X4 | UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/mouse/Sdhaf2/Sdhaf2-protnlm-function-review.md) |
| mouse/Vmn2r73 | A0A3B2WCZ5 | NPI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/mouse/Vmn2r73/Vmn2r73-protnlm-function-review.md) |
| rat/Pnkd | B4F7D2 | PLI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/rat/Pnkd/Pnkd-protnlm-function-review.md) |
| rat/Ptk7 | A0A8I6ALM9 | NPI, UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/rat/Ptk7/Ptk7-protnlm-function-review.md) |
| worm/C28G1.2 | Q18287 | UNC | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/worm/C28G1.2/C28G1.2-protnlm-function-review.md) |
| worm/dpm-1 | U4PF58 | NPI | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/worm/dpm-1/dpm-1-protnlm-function-review.md) |
| worm/wdr-23 | S6FN32 | CNN | [Function review](https://github.com/ai4curation/ai-gene-review/blob/main/genes/worm/wdr-23/wdr-23-protnlm-function-review.md) |

## Cohort scope

The cohort rows retain overlapping selections, including six fly targets selected twice. Paired reference records provide evidence and contribute no extra prediction assessments. Use the deduplicated totals above for the combined corpus.

| Cohort | Records | GO claims | Narrative review records |
|---|---:|---:|---:|
| ARGO50 | 50 | 77 | 0 |
| HORSE40 | 40 | 89 | 17 |
| HORSE40_HUMAN_PAIR | 40 | 0 | 0 |
| FLY41 | 41 | 50 | 13 |
| FLY_LOCATION_KEYWORD | 29 | 0 | 0 |
| FLY_NEXT20 | 20 | 0 | 0 |
| POMBE20 | 20 | 32 | 10 |
| POMBE_REMAINING8 | 8 | 0 | 0 |
| NEUROSPORA20 | 20 | 21 | 3 |
| MOD_EVOLUTION20 | 20 | 19 | 14 |

## Source metadata

`source_method: ProtNLM2` names the model. `source_version` identifies the release, XML artifact or dated API snapshot. API retrieval timestamps are observation times, not model training dates. The pilot, exploratory XML and later API snapshots remain distinct; frozen responses and source references retain their original provenance.
