# Check report: human-goa-2025-06

Generated 2026-11-25.

| check | pass/info | warn | fail |
|---|---|---|---|
| schema | 1 | 0 | 0 |
| novelty | 68 | 0 | 0 |
| present_in_current | 68 | 0 | 0 |
| date_window | 62 | 6 | 0 |
| prior_prediction | 59 | 8 | 0 |
| homolog_leakage | 66 | 1 | 0 |
| near_duplicate | 63 | 4 | 0 |
| uniprot_leakage | 125 | 11 | 0 |
| reference_recency | 204 | 68 | 0 |
| header_leakage | 63 | 5 | 0 |
| decoy | 72 | 0 | 0 |
| review_agreement | 12 | 0 | 0 |
| feature_label | 3 | 1 | 0 |
| balance | 1 | 0 | 0 |

## Stats

24 items, 68 targets; targets per item 1/2.0/7 (min/median/max); mean IC 8.728 bits; top reference share 0.176.

| dimension | value | count |
|---|---|---|
| aspect | C | 14 |
| aspect | F | 22 |
| aspect | P | 32 |
| assigned_by | UOS_MCB | 4 |
| assigned_by | UniProt | 64 |
| difficulty | EASY | 8 |
| difficulty | HARD | 56 |
| difficulty | MEDIUM | 3 |
| difficulty | UNSET | 1 |
| evidence_code | EXP | 5 |
| evidence_code | IDA | 57 |
| evidence_code | IMP | 6 |
| feature | NONE | 20 |
| feature | PSEUDOENZYME | 4 |
| knowledge_category | LIMITED_KNOWLEDGE | 9 |
| knowledge_category | NO_KNOWLEDGE | 14 |
| knowledge_category | PARTIAL_KNOWLEDGE | 45 |
| negated | False | 67 |
| negated | True | 1 |
| source | GOA_RELEASE | 68 |
| split | TEST | 24 |
| top_reference | PMID:40446798 | 12 |
| top_reference | PMID:41167449 | 7 |
| top_reference | PMID:40963017 | 6 |
| top_reference | PMID:40836090 | 5 |
| top_reference | PMID:40593606 | 5 |

## Warnings and failures (104)

| check | status | item | term | message |
|---|---|---|---|---|
| uniprot_leakage | WARN | human-goa-2025-06-O95455 | GO:0005783 | label 'endoplasmic reticulum' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-O95455 | GO:0005783 | agent-review: PMID:40836090 published 2025-10-01, before model cutoff 2026-06-01 |
| uniprot_leakage | WARN | human-goa-2025-06-O95455 | GO:0005794 | label 'Golgi apparatus' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-O95455 | GO:0005794 | agent-review: PMID:40836090 published 2025-10-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-O95455 | GO:0006024 | agent-review: PMID:40836090 published 2025-10-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-O95455 | GO:0008460 | agent-review: PMID:40836090 published 2025-10-01, before model cutoff 2026-06-01 |
| header_leakage | WARN | human-goa-2025-06-O95455 | GO:0008460 | protein name 'UDP-D-glucose 4,6-dehydratase' shares ['4', '6', 'dehydratase', 'glucose'] with the target label (FULL-header conditions) |
| reference_recency | WARN | human-goa-2025-06-O95455 | GO:0050377 | agent-review: PMID:40836090 published 2025-10-01, before model cutoff 2026-06-01 |
| header_leakage | WARN | human-goa-2025-06-O95455 | GO:0050377 | protein name 'UDP-D-glucose 4,6-dehydratase' shares ['4', '6', 'dehydratase', 'glucose', 'udp'] with the target label (FULL-header conditions) |
| reference_recency | WARN | human-goa-2025-06-P04075 | GO:0035774 | agent-review: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P05164 | GO:0006337 | agent-review: PMID:40963017 published 2025-11-01, before model cutoff 2026-06-01 |
| near_duplicate | WARN | human-goa-2025-06-P05164 | GO:0031491 | closest baseline term GO:0003682 chromatin binding (Lin 0.84) |
| reference_recency | WARN | human-goa-2025-06-P05164 | GO:0031491 | agent-review: PMID:40963017 published 2025-11-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P05164 | GO:0070944 | agent-review: PMID:40963017 published 2025-11-01, before model cutoff 2026-06-01 |
| uniprot_leakage | WARN | human-goa-2025-06-P05164 | GO:0140644 | label 'neutrophil extracellular trap' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-P05164 | GO:0140644 | agent-review: PMID:40963017 published 2025-11-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P05164 | GO:0140645 | agent-review: PMID:40963017 published 2025-11-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P05164 | GO:0140776 | agent-review: PMID:40963017 published 2025-11-01, before model cutoff 2026-06-01 |
| prior_prediction | WARN | human-goa-2025-06-P0C7U0 | GO:0016020 | predicted before cutoff by IBA,IEA |
| uniprot_leakage | WARN | human-goa-2025-06-P0C7U0 | GO:0016020 | label 'membrane' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-P0C7U0 | GO:0016020 | agent-review: PMID:40576023 published 2025-09-01, before model cutoff 2026-06-01 |
| prior_prediction | WARN | human-goa-2025-06-P0DMS8 | GO:0001609 | predicted before cutoff by IBA,IEA |
| reference_recency | WARN | human-goa-2025-06-P0DMS8 | GO:0001609 | agent-review: PMID:40825947 published 2025-08-18, before model cutoff 2026-06-01 |
| feature_label | WARN | human-goa-2025-06-P28370 |  | PSEUDOENZYME label rests on comment text only (check it is about this protein's canonical form) |
| prior_prediction | WARN | human-goa-2025-06-P28370 | GO:0016887 | predicted before cutoff by IEA |
| reference_recency | WARN | human-goa-2025-06-P28370 | GO:0016887 | agent-review: PMID:39413208 published 2024-11-27, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P31749 | GO:0051897 | agent-review: PMID:40285646 published 2025-07-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P32754 | GO:0001734 | agent-review: PMID:41317403 published 2026-02-01, before model cutoff 2026-06-01 |
| uniprot_leakage | WARN | human-goa-2025-06-P32754 | GO:0005634 | label 'nucleus' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-P32754 | GO:0005634 | agent-review: PMID:41317403 published 2026-02-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P43405 | GO:0034165 | agent-review: PMID:40980882 published 2025-11-12, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49407 | GO:0001678 | agent-review: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49407 | GO:0007166 | agent-review: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| near_duplicate | WARN | human-goa-2025-06-P49407 | GO:0030674 | closest baseline term GO:0060090 molecular adaptor activity (Lin 0.97) |
| reference_recency | WARN | human-goa-2025-06-P49407 | GO:0030674 | agent-review: PMID:40384633 published 2025-10-15, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49407 | GO:0035721 | agent-review: PMID:40384633 published 2025-10-15, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49407 | GO:1903568 | agent-review: PMID:40384633 published 2025-10-15, before model cutoff 2026-06-01 |
| date_window | WARN | human-goa-2025-06-P49842 | GO:0000993 | GAF date 20250117 before cutoff yet absent from baseline (late export or filtered from the baseline release) |
| reference_recency | WARN | human-goa-2025-06-P49842 | GO:0000993 | agent-review: PMID:39353615 published 2024-11-27, before model cutoff 2026-06-01 |
| date_window | WARN | human-goa-2025-06-P49842 | GO:0006283 | GAF date 20250117 before cutoff yet absent from baseline (late export or filtered from the baseline release) |
| reference_recency | WARN | human-goa-2025-06-P49842 | GO:0006283 | agent-review: PMID:39353615 published 2024-11-27, before model cutoff 2026-06-01 |
| date_window | WARN | human-goa-2025-06-P49842 | GO:0008023 | GAF date 20250117 before cutoff yet absent from baseline (late export or filtered from the baseline release) |
| reference_recency | WARN | human-goa-2025-06-P49842 | GO:0008023 | agent-review: PMID:39547223 published 2024-12-19, before model cutoff 2026-06-01 |
| date_window | WARN | human-goa-2025-06-P49842 | GO:0062058 | GAF date 20250117 before cutoff yet absent from baseline (late export or filtered from the baseline release) |
| reference_recency | WARN | human-goa-2025-06-P49842 | GO:0062058 | agent-review: PMID:39353615 published 2024-11-27, before model cutoff 2026-06-01 |
| uniprot_leakage | WARN | human-goa-2025-06-P49903 | GO:0005694 | label 'chromosome' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-P49903 | GO:0005694 | agent-review: PMID:40608935 published 2025-07-03, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P63092 | GO:0001678 | agent-review: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| near_duplicate | WARN | human-goa-2025-06-P63092 | GO:0035774 | closest baseline term GO:0050796 regulation of insulin secretion (Lin 0.84) |
| reference_recency | WARN | human-goa-2025-06-P63092 | GO:0035774 | agent-review: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P98161 | GO:0007005 | agent-review: PMID:41166294 published 2025-10-30, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P98161 | GO:0044233 | agent-review: PMID:41166294 published 2025-10-30, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q14258 | GO:0010507 | agent-review: PMID:40542578 published 2025-06-20, before model cutoff 2026-06-01 |
| uniprot_leakage | WARN | human-goa-2025-06-Q494V2 | GO:0000922 | label 'spindle pole' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-Q494V2 | GO:0000922 | agent-review: PMID:40593606 published 2025-07-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q494V2 | GO:0007052 | agent-review: PMID:40593606 published 2025-07-01, before model cutoff 2026-06-01 |
| uniprot_leakage | WARN | human-goa-2025-06-Q494V2 | GO:0007059 | label 'chromosome segregation' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-Q494V2 | GO:0007059 | agent-review: PMID:40593606 published 2025-07-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q494V2 | GO:0008017 | agent-review: PMID:40593606 published 2025-07-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q494V2 | GO:0043616 | agent-review: PMID:40593606 published 2025-07-01, before model cutoff 2026-06-01 |
| date_window | WARN | human-goa-2025-06-Q6UXB2 | GO:0008009 | GAF date 20250505 before cutoff yet absent from baseline (late export or filtered from the baseline release) |
| reference_recency | WARN | human-goa-2025-06-Q6UXB2 | GO:0008009 | agent-review: PMID:40279398 published 2025-11-01, before model cutoff 2026-06-01 |
| header_leakage | WARN | human-goa-2025-06-Q6UXB2 | GO:0008009 | protein name 'C-X-C motif chemokine 17' shares ['chemokine'] with the target label (FULL-header conditions) |
| prior_prediction | WARN | human-goa-2025-06-Q6UXB2 | GO:0016477 | predicted before cutoff by IBA,IEA |
| reference_recency | WARN | human-goa-2025-06-Q6UXB2 | GO:0016477 | agent-review: PMID:41167449 published 2026-01-01, before model cutoff 2026-06-01 |
| date_window | WARN | human-goa-2025-06-Q6UXB2 | GO:0030595 | GAF date 20250505 before cutoff yet absent from baseline (late export or filtered from the baseline release) |
| prior_prediction | WARN | human-goa-2025-06-Q6UXB2 | GO:0030595 | predicted before cutoff by IBA,IEA |
| reference_recency | WARN | human-goa-2025-06-Q6UXB2 | GO:0030595 | agent-review: PMID:40279398 published 2025-11-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q6UXB2 | GO:0042056 | agent-review: PMID:41167449 published 2026-01-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q6UXB2 | GO:0070098 | agent-review: PMID:41167449 published 2026-01-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0001678 | agent-review: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| prior_prediction | WARN | human-goa-2025-06-Q86SM8 | GO:0005886 | predicted before cutoff by IBA,IEA |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0005886 | agent-review: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0007166 | agent-review: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0007189 | agent-review: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0035774 | agent-review: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0038182 | agent-review: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| header_leakage | WARN | human-goa-2025-06-Q86SM8 | GO:0038182 | protein name 'Mas-related G protein-coupled receptor member E' shares ['coupled', 'g', 'receptor'] with the target label (FULL-header conditions) |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0038184 | agent-review: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q8N7P1 | GO:0005739 | agent-review: PMID:39423811 published 2024-11-27, before model cutoff 2026-06-01 |
| uniprot_leakage | WARN | human-goa-2025-06-Q8NAG6 | GO:0030496 | label 'midbody' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-Q8NAG6 | GO:0030496 | agent-review: PMID:41361016 published 2025-12-08, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q8WU10 | GO:0000968 | agent-review: PMID:40069351 published 2025-07-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q8WU10 | GO:0003954 | agent-review: PMID:40069351 published 2025-07-01, before model cutoff 2026-06-01 |
| uniprot_leakage | WARN | human-goa-2025-06-Q8WU10 | GO:0003959 | label 'NADPH dehydrogenase activity' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-Q8WU10 | GO:0003959 | agent-review: PMID:40069351 published 2025-07-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q8WU10 | GO:0140299 | agent-review: PMID:40069351 published 2025-07-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q96C45 | GO:0030674 | agent-review: PMID:38096226 published 2023-12-14, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q96C45 | GO:0045880 | agent-review: PMID:38096226 published 2023-12-14, before model cutoff 2026-06-01 |
| uniprot_leakage | WARN | human-goa-2025-06-Q96C45 | GO:0097542 | label 'ciliary tip' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-Q96C45 | GO:0097542 | agent-review: PMID:38096226 published 2023-12-14, before model cutoff 2026-06-01 |
| prior_prediction | WARN | human-goa-2025-06-Q96LB2 | GO:0004930 | predicted before cutoff by IBA,IEA |
| homolog_leakage | WARN | human-goa-2025-06-Q96LB2 | GO:0004930 | known on 1 PTHR11334:SF22 homolog(s) at baseline |
| near_duplicate | WARN | human-goa-2025-06-Q96LB2 | GO:0004930 | closest baseline term GO:0004888 transmembrane signaling receptor activity (Lin 0.86) |
| reference_recency | WARN | human-goa-2025-06-Q96LB2 | GO:0004930 | agent-review: PMID:41167449 published 2026-01-01, before model cutoff 2026-06-01 |
| header_leakage | WARN | human-goa-2025-06-Q96LB2 | GO:0004930 | protein name 'Mas-related G protein-coupled receptor member X1' shares ['coupled', 'g', 'receptor'] with the target label (FULL-header conditions) |
| reference_recency | WARN | human-goa-2025-06-Q96LB2 | GO:0016477 | agent-review: PMID:41167449 published 2026-01-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q96LB2 | GO:0016493 | agent-review: PMID:41167449 published 2026-01-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q96LB2 | GO:0070098 | agent-review: PMID:41167449 published 2026-01-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q9P0L0 | GO:0032374 | agent-review: PMID:41741634 published 2026-04-01, before model cutoff 2026-06-01 |
| prior_prediction | WARN | human-goa-2025-06-Q9P0L0 | GO:0043495 | predicted before cutoff by IBA |
| reference_recency | WARN | human-goa-2025-06-Q9P0L0 | GO:0043495 | agent-review: PMID:41856286 published 2026-05-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q9P0L0 | GO:0140284 | agent-review: PMID:41741634 published 2026-04-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q9P0L0 | GO:0170016 | agent-review: PMID:41741634 published 2026-04-01, before model cutoff 2026-06-01 |

## Sources

- baseline_gaf: https://release.geneontology.org/2025-06-01/annotations/goa_human.gaf.gz (release 2025-06-01, sha256 ca20b3c6d6c515dc8944496861314de3f94c83896f2ec49ff5e355f3446e539d)
- current_gaf: https://release.geneontology.org/2026-08-05/annotations/gaf/HUMAN-uniprot.gaf.gz (release 2026-08-05, sha256 a0afba19dfb1f8fa996bc1bdcd61fd0c9bd4cf0d2bf2509d09ac86993c0e70a2)
- current_ontology: https://release.geneontology.org/2026-08-05/ontology/go-basic.obo (release 2026-08-05, sha256 b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc)
- panther_subfamilies: https://rest.uniprot.org/uniprotkb/stream (release 2026_04, sha256 n/a)
- feature_pseudoenzyme: https://rest.uniprot.org/uniprotkb/stream (release 2026_04, sha256 n/a)
- uniprot_sequences: https://rest.uniprot.org/uniprotkb/stream (release , sha256 n/a)
- pubmed_dates: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi (release , sha256 n/a)
