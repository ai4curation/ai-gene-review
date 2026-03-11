# SNIPE Architecture-Aware Feature Analysis (InterPro)

## Question

Suggest data-driven feature combinations for:

`IPR025280 + GIY-YIG nuclease + membrane targeting features`

to support an architecture-aware annotation strategy.

## Runs

- Primary run: `IPR025280` (SNIPE associated domain)
- Secondary validation run: `IPR029330` (small control run to test script on a different input)

Output folders:

- `results/IPR025280/`
- `results/IPR029330/`

## Key Results for IPR025280

### Architecture prevalence

Top architectures from `results/IPR025280/architecture_table.tsv`:

1. `PF13250:IPR025280-PF13455` -> 1109 proteins (68.80%)
2. `PF13250:IPR025280-PF10544:IPR018306` -> 270 proteins (16.75%)
3. `PF13250:IPR025280` -> 139 proteins (8.62%)

Top 3 cover 1518/1612 proteins (94.17%).

### Catalytic partner (GIY-YIG-like proxy) co-features

From `results/IPR025280/cooccurring_domain_weighted.tsv`:

- `PF13455` -> 1189 proteins (73.76%)
- `PF10544` + `IPR018306` -> 277 proteins (17.18%)

Combined, these catalytic co-features cover 1466/1612 proteins (90.94%).

### Membrane-targeting signals

From `results/IPR025280/nterm_tm_heuristic_overall.tsv`:

- N-terminal TM-like heuristic (first 70 aa): 990/1612 proteins (61.41%)

From `results/IPR025280/representative_extra_features.tsv`:

- Dominant representative `Q7MG17`: TMhelix `5-22`, signal peptide `1-23`
- Second representative `Q6AMX9`: TMhelix `7-24`

Rare but explicit membrane-associated accessory domains (from `cooccurring_domain_weighted.tsv`):

- `PF14470` / `IPR039519` (bacterial PH domain): 3 proteins (0.19%)
- `PF05154` / `IPR007829` (TM2 domain): 1 protein (0.06%)

Potentially membrane-linked but weaker evidence:

- `PF10708` / `IPR018929` (DUF2510): 76 proteins (4.71%); Pfam description notes many members are putative membrane proteins.

## Suggested Feature Sets for Rule Design

### Tier 1 (high-confidence)

Use all of:

1. `IPR025280` (SNIPE associated domain)
2. Catalytic partner: `PF13455` OR `IPR018306`/`PF10544`
3. At least one membrane-targeting signal:
   - N-terminal TMhelix/signal peptide (or equivalent N-term TM-like predictor), OR
   - membrane-associated domain such as `IPR007829` or `IPR039519` when present

### Tier 2 (exploratory / broader)

Use:

1. `IPR025280`
2. Catalytic partner: `PF13455` OR `IPR018306`/`PF10544`
3. Optional membrane-linked accessory: `IPR018929` (DUF2510)

with lower confidence due weaker direct membrane evidence.

## Recommended wording for the GO issue

Suggested architecture-aware implementation note:

`IPR025280 + (PF13455 OR IPR018306/PF10544) + (N-term TM/signal peptide OR membrane-associated accessory domain such as IPR007829/IPR039519; optional lower-confidence IPR018929).`

## Checklist

- [x] None of the scripts use hardcoded inputs or outputs
- [x] Scripts tested on at least one other input (`IPR029330`)
- [x] Analyses completed as expected for the primary target (`IPR025280`)
- [x] Direct script outputs are present in the analysis folder
- [x] Summary includes provenance and quantitative justification
