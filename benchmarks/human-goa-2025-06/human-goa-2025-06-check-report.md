# Check report: human-goa-2025-06

Generated 2026-11-26.

| check | pass | info | warn | fail |
|---|---|---|---|---|
| schema | 1 | 0 | 0 | 0 |
| novelty | 51 | 0 | 0 | 0 |
| present_in_current | 51 | 0 | 0 | 0 |
| date_window | 45 | 0 | 6 | 0 |
| review_agreement | 12 | 6 | 0 | 0 |
| prior_prediction | 43 | 0 | 7 | 0 |
| homolog_leakage | 3 | 47 | 0 | 0 |
| near_duplicate | 33 | 15 | 2 | 0 |
| uniprot_leakage | 49 | 48 | 5 | 0 |
| reference_recency | 0 | 51 | 102 | 0 |
| header_leakage | 45 | 0 | 6 | 0 |
| decoy | 72 | 0 | 0 | 0 |
| feature_label | 3 | 0 | 1 | 0 |
| balance | 0 | 0 | 1 | 0 |

## Stats

24 items, 51 targets; targets per item 1/1.0/7 (min/median/max); mean IC 9.494 bits; top reference share 0.196.

| dimension | value | count |
|---|---|---|
| aspect | C | 11 |
| aspect | F | 16 |
| aspect | P | 24 |
| assigned_by | ComplexPortal | 2 |
| assigned_by | IntAct | 1 |
| assigned_by | UOS_MCB | 1 |
| assigned_by | UniProt | 47 |
| difficulty | EASY | 7 |
| difficulty | HARD | 41 |
| difficulty | MEDIUM | 2 |
| difficulty | UNSET | 1 |
| evidence_code | EXP | 3 |
| evidence_code | IDA | 38 |
| evidence_code | IMP | 7 |
| evidence_code | IPI | 3 |
| feature | NONE | 20 |
| feature | PSEUDOENZYME | 4 |
| knowledge_category | LIMITED_KNOWLEDGE | 4 |
| knowledge_category | NO_KNOWLEDGE | 12 |
| knowledge_category | PARTIAL_KNOWLEDGE | 35 |
| negated | False | 50 |
| negated | True | 1 |
| source | GOA_RELEASE | 51 |
| split | TEST | 24 |
| top_reference | PMID:40446798 | 10 |
| top_reference | PMID:40108300 | 5 |
| top_reference | PMID:40836090 | 4 |
| top_reference | PMID:40963017 | 3 |
| top_reference | PMID:39353615 | 3 |

## Warnings and failures (130)

| check | status | item | term | message |
|---|---|---|---|---|
| reference_recency | WARN | human-goa-2025-06-O75096 | GO:0001618 | peptalk:claude-opus-5-5: PMID:41162706 published 2026-01-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-O75096 | GO:0001618 | ai-gene-review:claude-opus-5-5: PMID:41162706 published 2026-01-01, before model cutoff 2026-06-01 |
| uniprot_leakage | WARN | human-goa-2025-06-O95455 | GO:0005794 | label 'Golgi apparatus' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-O95455 | GO:0005794 | peptalk:claude-opus-5-5: PMID:40836090 published 2025-10-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-O95455 | GO:0005794 | ai-gene-review:claude-opus-5-5: PMID:40836090 published 2025-10-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-O95455 | GO:0006024 | peptalk:claude-opus-5-5: PMID:40836090 published 2025-10-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-O95455 | GO:0006024 | ai-gene-review:claude-opus-5-5: PMID:40836090 published 2025-10-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-O95455 | GO:0008460 | peptalk:claude-opus-5-5: PMID:40836090 published 2025-10-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-O95455 | GO:0008460 | ai-gene-review:claude-opus-5-5: PMID:40836090 published 2025-10-01, before model cutoff 2026-06-01 |
| header_leakage | WARN | human-goa-2025-06-O95455 | GO:0008460 | protein name 'UDP-D-glucose 4,6-dehydratase' shares ['4', '6', 'dehydratase', 'glucose'] with the target label (FULL-header conditions) |
| reference_recency | WARN | human-goa-2025-06-O95455 | GO:0050377 | peptalk:claude-opus-5-5: PMID:40836090 published 2025-10-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-O95455 | GO:0050377 | ai-gene-review:claude-opus-5-5: PMID:40836090 published 2025-10-01, before model cutoff 2026-06-01 |
| header_leakage | WARN | human-goa-2025-06-O95455 | GO:0050377 | protein name 'UDP-D-glucose 4,6-dehydratase' shares ['4', '6', 'dehydratase', 'glucose', 'udp'] with the target label (FULL-header conditions) |
| reference_recency | WARN | human-goa-2025-06-P04075 | GO:0035774 | peptalk:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P04075 | GO:0035774 | ai-gene-review:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P05164 | GO:0006337 | peptalk:claude-opus-5-5: PMID:40963017 published 2025-11-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P05164 | GO:0006337 | ai-gene-review:claude-opus-5-5: PMID:40963017 published 2025-11-01, before model cutoff 2026-06-01 |
| near_duplicate | WARN | human-goa-2025-06-P05164 | GO:0031491 | closest baseline term GO:0003682 chromatin binding (Lin 0.84) |
| reference_recency | WARN | human-goa-2025-06-P05164 | GO:0031491 | peptalk:claude-opus-5-5: PMID:40963017 published 2025-11-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P05164 | GO:0031491 | ai-gene-review:claude-opus-5-5: PMID:40963017 published 2025-11-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P05164 | GO:0140776 | peptalk:claude-opus-5-5: PMID:40963017 published 2025-11-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P05164 | GO:0140776 | ai-gene-review:claude-opus-5-5: PMID:40963017 published 2025-11-01, before model cutoff 2026-06-01 |
| date_window | WARN | human-goa-2025-06-P13473 | GO:0160020 | GAF date 20250520 before cutoff yet absent from baseline (late export or filtered from the baseline release) |
| reference_recency | WARN | human-goa-2025-06-P13473 | GO:0160020 | peptalk:claude-opus-5-5: PMID:40281343 published 2025-09-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P13473 | GO:0160020 | ai-gene-review:claude-opus-5-5: PMID:40281343 published 2025-09-01, before model cutoff 2026-06-01 |
| prior_prediction | WARN | human-goa-2025-06-P16260 | GO:1990559 | predicted before cutoff by IBA |
| reference_recency | WARN | human-goa-2025-06-P16260 | GO:1990559 | peptalk:claude-opus-5-5: PMID:40925986 published 2025-09-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P16260 | GO:1990559 | ai-gene-review:claude-opus-5-5: PMID:40925986 published 2025-09-01, before model cutoff 2026-06-01 |
| header_leakage | WARN | human-goa-2025-06-P16260 | GO:1990559 | protein name 'Mitochondrial coenzyme A transporter SLC25A16' shares ['a', 'coenzyme', 'mitochondrial'] with the target label (FULL-header conditions) |
| reference_recency | WARN | human-goa-2025-06-P43405 | GO:0034165 | peptalk:claude-opus-5-5: PMID:40980882 published 2025-11-12, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P43405 | GO:0034165 | ai-gene-review:claude-opus-5-5: PMID:40980882 published 2025-11-12, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49407 | GO:0001678 | peptalk:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49407 | GO:0001678 | ai-gene-review:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49407 | GO:0007166 | peptalk:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49407 | GO:0007166 | ai-gene-review:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49407 | GO:0035721 | peptalk:claude-opus-5-5: PMID:40384633 published 2025-10-15, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49407 | GO:0035721 | ai-gene-review:claude-opus-5-5: PMID:40384633 published 2025-10-15, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49407 | GO:1903568 | peptalk:claude-opus-5-5: PMID:40384633 published 2025-10-15, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49407 | GO:1903568 | ai-gene-review:claude-opus-5-5: PMID:40384633 published 2025-10-15, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49841 | GO:0032374 | peptalk:claude-opus-5-5: PMID:41741634 published 2026-04-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49841 | GO:0032374 | ai-gene-review:claude-opus-5-5: PMID:41741634 published 2026-04-01, before model cutoff 2026-06-01 |
| date_window | WARN | human-goa-2025-06-P49842 | GO:0000993 | GAF date 20250117 before cutoff yet absent from baseline (late export or filtered from the baseline release) |
| reference_recency | WARN | human-goa-2025-06-P49842 | GO:0000993 | peptalk:claude-opus-5-5: PMID:39353615 published 2024-11-27, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49842 | GO:0000993 | ai-gene-review:claude-opus-5-5: PMID:39353615 published 2024-11-27, before model cutoff 2026-06-01 |
| date_window | WARN | human-goa-2025-06-P49842 | GO:0006283 | GAF date 20250117 before cutoff yet absent from baseline (late export or filtered from the baseline release) |
| reference_recency | WARN | human-goa-2025-06-P49842 | GO:0006283 | peptalk:claude-opus-5-5: PMID:39353615 published 2024-11-27, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49842 | GO:0006283 | ai-gene-review:claude-opus-5-5: PMID:39353615 published 2024-11-27, before model cutoff 2026-06-01 |
| date_window | WARN | human-goa-2025-06-P49842 | GO:0008023 | GAF date 20250117 before cutoff yet absent from baseline (late export or filtered from the baseline release) |
| reference_recency | WARN | human-goa-2025-06-P49842 | GO:0008023 | peptalk:claude-opus-5-5: PMID:39547228 published 2024-12-12, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49842 | GO:0008023 | ai-gene-review:claude-opus-5-5: PMID:39547228 published 2024-12-12, before model cutoff 2026-06-01 |
| date_window | WARN | human-goa-2025-06-P49842 | GO:0062058 | GAF date 20250117 before cutoff yet absent from baseline (late export or filtered from the baseline release) |
| reference_recency | WARN | human-goa-2025-06-P49842 | GO:0062058 | peptalk:claude-opus-5-5: PMID:39353615 published 2024-11-27, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P49842 | GO:0062058 | ai-gene-review:claude-opus-5-5: PMID:39353615 published 2024-11-27, before model cutoff 2026-06-01 |
| uniprot_leakage | WARN | human-goa-2025-06-P51553 | GO:0001917 | label 'photoreceptor inner segment' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-P51553 | GO:0001917 | peptalk:claude-opus-5-5: PMID:40119724 published 2025-06-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P51553 | GO:0001917 | ai-gene-review:claude-opus-5-5: PMID:40119724 published 2025-06-01, before model cutoff 2026-06-01 |
| prior_prediction | WARN | human-goa-2025-06-P53597 | GO:0004776 | predicted before cutoff by IBA,IEA |
| reference_recency | WARN | human-goa-2025-06-P53597 | GO:0004776 | peptalk:claude-opus-5-5: PMID:40108300 published 2025-06-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P53597 | GO:0004776 | ai-gene-review:claude-opus-5-5: PMID:40108300 published 2025-06-01, before model cutoff 2026-06-01 |
| header_leakage | WARN | human-goa-2025-06-P53597 | GO:0004776 | protein name 'Succinate--CoA ligase [ADP/GDP-forming] subunit alpha, mitochondrial' shares ['coa', 'forming', 'gdp', 'ligase', 'succinate'] with the target label (FULL-header conditions) |
| reference_recency | WARN | human-goa-2025-06-P53597 | GO:0006108 | peptalk:claude-opus-5-5: PMID:40108300 published 2025-06-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P53597 | GO:0006108 | ai-gene-review:claude-opus-5-5: PMID:40108300 published 2025-06-01, before model cutoff 2026-06-01 |
| prior_prediction | WARN | human-goa-2025-06-P53597 | GO:0016878 | predicted before cutoff by IBA,IEA |
| reference_recency | WARN | human-goa-2025-06-P53597 | GO:0016878 | peptalk:claude-opus-5-5: PMID:40108300 published 2025-06-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P53597 | GO:0016878 | ai-gene-review:claude-opus-5-5: PMID:40108300 published 2025-06-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P53597 | GO:0050074 | peptalk:claude-opus-5-5: PMID:40108300 published 2025-06-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P53597 | GO:0050074 | ai-gene-review:claude-opus-5-5: PMID:40108300 published 2025-06-01, before model cutoff 2026-06-01 |
| header_leakage | WARN | human-goa-2025-06-P53597 | GO:0050074 | protein name 'Succinate--CoA ligase [ADP/GDP-forming] subunit alpha, mitochondrial' shares ['coa', 'ligase'] with the target label (FULL-header conditions) |
| reference_recency | WARN | human-goa-2025-06-P53597 | GO:0110052 | peptalk:claude-opus-5-5: PMID:40108300 published 2025-06-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P53597 | GO:0110052 | ai-gene-review:claude-opus-5-5: PMID:40108300 published 2025-06-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P98155 | GO:0001618 | peptalk:claude-opus-5-5: PMID:41162706 published 2026-01-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-P98155 | GO:0001618 | ai-gene-review:claude-opus-5-5: PMID:41162706 published 2026-01-01, before model cutoff 2026-06-01 |
| prior_prediction | WARN | human-goa-2025-06-Q13263 | GO:0000785 | predicted before cutoff by IEA |
| uniprot_leakage | WARN | human-goa-2025-06-Q13263 | GO:0000785 | label 'chromatin' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-Q13263 | GO:0000785 | peptalk:claude-opus-5-5: PMID:41109928 published 2025-12-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q13263 | GO:0000785 | ai-gene-review:claude-opus-5-5: PMID:41109928 published 2025-12-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q13263 | GO:0043124 | peptalk:claude-opus-5-5: PMID:39920527 published 2025-06-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q13263 | GO:0043124 | ai-gene-review:claude-opus-5-5: PMID:39920527 published 2025-06-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q15477 | GO:0070481 | peptalk:claude-opus-5-5: PMID:40441874 published 2025-07-16, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q15477 | GO:0070481 | ai-gene-review:claude-opus-5-5: PMID:40441874 published 2025-07-16, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q68DK2 | GO:0042802 | peptalk:claude-opus-5-5: PMID:40175557 published 2025-08-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q68DK2 | GO:0042802 | ai-gene-review:claude-opus-5-5: PMID:40175557 published 2025-08-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0001678 | peptalk:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0001678 | ai-gene-review:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| prior_prediction | WARN | human-goa-2025-06-Q86SM8 | GO:0005886 | predicted before cutoff by IBA,IEA |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0005886 | peptalk:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0005886 | ai-gene-review:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0007166 | peptalk:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0007166 | ai-gene-review:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0007189 | peptalk:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0007189 | ai-gene-review:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0035774 | peptalk:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0035774 | ai-gene-review:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0038182 | peptalk:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0038182 | ai-gene-review:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| header_leakage | WARN | human-goa-2025-06-Q86SM8 | GO:0038182 | protein name 'Mas-related G protein-coupled receptor member E' shares ['coupled', 'g', 'receptor'] with the target label (FULL-header conditions) |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0038184 | peptalk:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86SM8 | GO:0038184 | ai-gene-review:claude-opus-5-5: PMID:40446798 published 2025-08-21, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86WV6 | GO:0015485 | peptalk:claude-opus-5-5: PMID:41639452 published 2026-04-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86WV6 | GO:0015485 | ai-gene-review:claude-opus-5-5: PMID:41639452 published 2026-04-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86WV6 | GO:0036020 | peptalk:claude-opus-5-5: PMID:40973797 published 2025-11-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86WV6 | GO:0036020 | ai-gene-review:claude-opus-5-5: PMID:40973797 published 2025-11-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86WV6 | GO:0080025 | peptalk:claude-opus-5-5: PMID:41639452 published 2026-04-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q86WV6 | GO:0080025 | ai-gene-review:claude-opus-5-5: PMID:41639452 published 2026-04-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q8N7P1 | GO:0005739 | peptalk:claude-opus-5-5: PMID:39423811 published 2024-11-27, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q8N7P1 | GO:0005739 | ai-gene-review:claude-opus-5-5: PMID:39423811 published 2024-11-27, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q96C45 | GO:0030674 | peptalk:claude-opus-5-5: PMID:38096226 published 2023-12-14, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q96C45 | GO:0030674 | ai-gene-review:claude-opus-5-5: PMID:38096226 published 2023-12-14, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q96C45 | GO:0045880 | peptalk:claude-opus-5-5: PMID:38096226 published 2023-12-14, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q96C45 | GO:0045880 | ai-gene-review:claude-opus-5-5: PMID:38096226 published 2023-12-14, before model cutoff 2026-06-01 |
| uniprot_leakage | WARN | human-goa-2025-06-Q96C45 | GO:0097542 | label 'ciliary tip' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-Q96C45 | GO:0097542 | peptalk:claude-opus-5-5: PMID:38096226 published 2023-12-14, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q96C45 | GO:0097542 | ai-gene-review:claude-opus-5-5: PMID:38096226 published 2023-12-14, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q96DZ1 | GO:0000836 | peptalk:claude-opus-5-5: PMID:40593878 published 2025-07-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q96DZ1 | GO:0000836 | ai-gene-review:claude-opus-5-5: PMID:40593878 published 2025-07-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q96DZ1 | GO:0034099 | peptalk:claude-opus-5-5: PMID:40593878 published 2025-07-01, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q96DZ1 | GO:0034099 | ai-gene-review:claude-opus-5-5: PMID:40593878 published 2025-07-01, before model cutoff 2026-06-01 |
| near_duplicate | WARN | human-goa-2025-06-Q99836 | GO:0034162 | closest baseline term GO:0034158 toll-like receptor 8 signaling pathway (Lin 0.82) |
| reference_recency | WARN | human-goa-2025-06-Q99836 | GO:0034162 | peptalk:claude-opus-5-5: PMID:40980882 published 2025-11-12, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q99836 | GO:0034162 | ai-gene-review:claude-opus-5-5: PMID:40980882 published 2025-11-12, before model cutoff 2026-06-01 |
| prior_prediction | WARN | human-goa-2025-06-Q9HBU9 | GO:0002027 | predicted before cutoff by ISS |
| reference_recency | WARN | human-goa-2025-06-Q9HBU9 | GO:0002027 | peptalk:claude-opus-5-5: PMID:40409267 published 2025-07-03, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q9HBU9 | GO:0002027 | ai-gene-review:claude-opus-5-5: PMID:40409267 published 2025-07-03, before model cutoff 2026-06-01 |
| feature_label | WARN | human-goa-2025-06-Q9UBX7 |  | neither the protein's own names nor its comments support the PSEUDOENZYME label (the query may have matched a chain or domain name, or the entry was revised) |
| date_window | WARN | human-goa-2025-06-Q9UBX7 | GO:0005794 | GAF date 20240313 before cutoff yet absent from baseline (late export or filtered from the baseline release) |
| prior_prediction | WARN | human-goa-2025-06-Q9UBX7 | GO:0005794 | predicted before cutoff by IEA |
| uniprot_leakage | WARN | human-goa-2025-06-Q9UBX7 | GO:0005794 | label 'Golgi apparatus' appears in UniProt comment text |
| reference_recency | WARN | human-goa-2025-06-Q9UBX7 | GO:0005794 | peptalk:claude-opus-5-5: PMID:36689511 published 2023-01-23, before model cutoff 2026-06-01 |
| reference_recency | WARN | human-goa-2025-06-Q9UBX7 | GO:0005794 | ai-gene-review:claude-opus-5-5: PMID:36689511 published 2023-01-23, before model cutoff 2026-06-01 |
| balance | WARN |  |  | PMID:40446798 supplies targets to 3/24 items, so their scores are not independent |

## Sources

- baseline_gaf: https://release.geneontology.org/2025-06-01/annotations/goa_human.gaf.gz (release 2025-06-01, sha256 ca20b3c6d6c515dc8944496861314de3f94c83896f2ec49ff5e355f3446e539d)
- current_gaf: https://release.geneontology.org/2026-08-05/annotations/gaf/HUMAN-uniprot.gaf.gz (release 2026-08-05, sha256 a0afba19dfb1f8fa996bc1bdcd61fd0c9bd4cf0d2bf2509d09ac86993c0e70a2)
- current_ontology: https://release.geneontology.org/2026-08-05/ontology/go-basic.obo (release 2026-08-05, sha256 b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc)
- panther_subfamilies: https://rest.uniprot.org/uniprotkb/stream (release 2026_04, sha256 n/a)
- feature_pseudoenzyme: https://rest.uniprot.org/uniprotkb/stream (release 2026_04, sha256 n/a)
- uniprot_sequences: https://rest.uniprot.org/uniprotkb/stream (release , sha256 n/a)
- pubmed_dates: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi (release , sha256 n/a)
