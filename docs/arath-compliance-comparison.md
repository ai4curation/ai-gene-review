# ARATH compliance comparison

Baseline YAML revision: `429666d2e90edbbab38886f6a53d279b9a8280ab`. Current input: working tree (individual SHA-256 fingerprints in the companion JSON).

Both revisions are recomputed with the same current analyzer, schema, weights and evidence-code rules. The inclusive policy uses ACCEPT, MODIFY, REMOVE, KEEP_AS_NON_CORE, MARK_AS_OVER_ANNOTATED, NEW and UNDECIDED for every evidence rule. Thus changing a decision among these actions cannot remove that annotation from a rule denominator. PENDING or missing reviews remain outside action-conditioned rules. IEA does not require quotations; its inclusive check is sourced rationale.

These are completeness scores, not evidence-quality scores. Inclusive gains can reflect changed reference findings, core functions, other recommended fields, added/deleted rows and evidence presence. They do not isolate added evidence. New objects can still change total denominators; exact weighted numerators/denominators and rule counts are included below and in JSON.

| Gene | Contextual before → after | Inclusive before → after | Inclusive weighted numerator/denominator before → after | Literature support before → after | Inference support before → after |
| --- | --- | --- | --- | --- | --- |
| ABI1 | 54.85% → 94.54% | 56.36% → 91.05% | 195/346 → 407/447 | 0/46 → 37/46 | 8/10 → 10/10 |
| FLS2 | 58.20% → 96.62% | 56.39% → 95.72% | 181/321 → 380/397 | 2/38 → 38/38 | 0/13 → 11/13 |
| MYC2 | 57.68% → 93.51% | 59.22% → 91.28% | 183/309 → 335/367 | 0/42 → 37/42 | 8/9 → 9/9 |
| GL1 | 58.42% → 95.65% | 57.14% → 95.88% | 120/210 → 186/194 | 0/18 → 18/18 | 1/8 → 8/8 |
| FBL22 | 57.35% → 90.20% | 59.72% → 88.14% | 43/72 → 52/59 | 2/2 → 1/2 | 2/2 → 2/2 |
| EIN2 | 65.96% → 97.42% | 64.43% → 93.99% | 250/388 → 422/449 | 9/54 → 48/54 | 4/9 → 7/9 |
| AGO1 | 58.63% → 93.31% | 58.41% → 93.42% | 184/315 → 341/365 | 5/39 → 40/40 | 2/6 → 6/6 |
| CASPL1D1 | 59.09% → 77.88% | 60.00% → 71.55% | 54/90 → 83/116 | 0/6 → 2/7 | 1/1 → 1/1 |
| DRB1 | 58.87% → 92.20% | 60.47% → 90.60% | 156/258 → 270/298 | 2/31 → 27/32 | 6/6 → 6/6 |
| EIN3 | 58.59% → 93.89% | 57.69% → 92.93% | 75/130 → 171/184 | 3/17 → 16/17 | 0/0 → 0/0 |
| COI1 | 58.86% → 96.12% | 58.86% → 92.52% | 93/158 → 198/214 | 4/23 → 20/24 | 0/0 → 0/0 |

Historical contextual snapshot cross-check: 11 genes matched by path; maximum absolute difference from recomputed baseline: 0.000000 percentage points. Historical scores are not used in either comparison denominator.
