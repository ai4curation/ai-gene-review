# Single-Organism IBA Phylogenetic Distance Analysis

## Overview

A recurrent question in IBA review is how to evaluate `IBA` annotations whose `WITH/FROM` column cites experimental descendants from **only a single organism** (excluding self-citations where the target gene's species is also a donor).

As established in [`IBA_REVIEW.md`](../IBA_REVIEW.md), a single-organism donor list is **not** intrinsically weak when the donor and target are close orthologs and the PAINT curator placed the ancestral `IBD` node at an appropriate clade (for example, mouse $\to$ human within `Euarchontoglires` or `Euteleostomi`). However, when a single organism's experimental annotation is used to seed an ancestral `IBD` deep in the tree—such as at `Opisthokonta`, `Eukaryota`, or `LUCA`—and then propagated down across kingdoms, domains, or multiple gene-duplication boundaries, the risk of over-propagation rises substantially.

This sub-project defines four quantitative distance metrics to measure "how far down (and up) the tree" a single-organism IBA travels, benchmarks them against existing review actions across all 25,298 positive GOA `IBA` annotations in the repository, and uses the resulting high-distance filter to identify candidate genes for targeted re-review.

---

## Corpus-Wide Prevalence

Across `genes/*/*/*-goa.tsv` and `interpro/panther/*/*-paint.tsv` (reproducible via `uv run python projects/IBA_REVIEW/single_organism_distance.py --summary`):

- **Total positive GOA `IBA` rows scanned**: **25,298** (across **6,382** GOA genes; **6,379** reviewed genes)
- **Single-organism GOA `IBA` rows (including self-species)**: **6,159** (**24.3%** of all positive IBAs)
- **Single-organism non-self `IBA` rows**: **3,517** (**13.9%** of all positive IBAs) across **2,165 genes** (**3,433** rated with a completed review action; **3,426** with a resolved donor UniProt `OC` lineage and **7** excluded in `Tier 0` due to unresolved donor lineage)
  - Strictly **1 single experimental seed token** (`n_seed_tokens == 1`): **2,867 rows** (**11.3%** of all IBAs)
  - Multiple paralog seed tokens (`n_seed_tokens >= 2`) from **1 single donor organism**: **650 rows** (**2.6%** of all IBAs)
- **Cached PAINT `IBD` assertions (`interpro/panther/*/*-paint.tsv`)**: **8,161 / 20,108** (**40.6%**) of all cached PAINT `IBD` ancestral rows rest on experimental evidence from a single resolved taxon.

---

## Action Classification: Propagation Failure vs Term Granularity Refinement

To avoid conflating true homology over-propagation with routine ontology-granularity adjustments, all tables below separate non-retained review actions into two distinct categories:

- **Propagation Failure (`Fail` = `REMOVE` + `MARK_AS_OVER_ANNOTATED`)**: The reviewer judged that the annotated function or process does not hold as a core or valid biological attribute of the target gene (with **`% REMOVE`** reported separately for outright false claims).
- **Term Granularity Refinement (`Refn` = `MODIFY` + `TOO_GENERAL`)**: The essence of the annotation is true of the target gene, but a more specific or better-scoped GO term is preferred.
- **Total Downgraded (`% Down` = `Fail` + `Refn`)**: The combined non-retained rate (`REMOVE` + `MARK_AS_OVER_ANNOTATED` + `MODIFY` + `TOO_GENERAL`), vs **Retained (`Keep` = `ACCEPT` + `KEEP_AS_NON_CORE`)**.

---

## Four Quantitative Distance Metrics

Implemented in [`single_organism_distance.py`](single_organism_distance.py):

### 1. Taxonomic LCA Clade Depth ($d_{\text{LCA}}$) & Branch Steps ($s_{\text{up}} + s_{\text{down}}$)

For each donor–target pair $(O_{\text{donor}}, O_{\text{target}})$, we find their Lowest Common Ancestor (LCA) along the UniProt/NCBI species `OC` phylogeny:
- **$d_{\text{LCA}}$**: Clade depth of $\text{LCA}(O_{\text{donor}}, O_{\text{target}})$ from `cellular_organisms` ($d_{\text{LCA}} = 0$ at `cellular_organisms`/`LUCA`, $1$ at `Eukaryota`/`Bacteria`, $2$ at `Metazoa`/`Fungi`/`Viridiplantae`, $3\text{–}4$ at `Bilateria`/`Protostomia`/`Deuterostomia`/`Ascomycota`, $6+$ at `Euteleostomi`/`Tetrapoda`/`Euarchontoglires`).
- **$s_{\text{up}} + s_{\text{down}}$**: Total taxonomic branch steps up from $O_{\text{donor}}$ to $\text{LCA}$ plus down from $\text{LCA}$ to $O_{\text{target}}$.

Across the 3,426 rated non-self single-organism IBA rows with resolved donor lineages (plus 7 rows in `Tier 0` with unresolved donor lineage), **Propagation Failure (`% Fail`)** and **`% REMOVE`** climb substantially as the donor–target LCA moves from close clades to cross-kingdom and cross-domain (`LUCA`) splits:

| Phylogenetic Tier | Representative LCA Clades | Rated | Keep | Fail | **% Fail** | Refn | **% Refn** | **% Down** | **% `REMOVE`** |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Tier 1: Close Clade** | `Euarchontoglires`, `Eutheria`, `Murinae`, `Caenorhabditis` | 1,346 | 1,158 | 108 | **8.0%** | 80 | **5.9%** | **14.0%** | **2.6%** |
| **Tier 2: Order / Subphylum Split** | `Saccharomycotina`, `Pezizomycotina`, `Magnoliopsida` | 73 | 60 | 1 | **1.4%** | 12 | **16.4%** | **17.8%** | **0.0%** |
| **Tier 3: Phylum / Subphylum Split** | `Euteleostomi` (Teleost $\leftrightarrow$ Mammal), `Ascomycota`, `Ecdysozoa` | 556 | 448 | 68 | **12.2%** | 40 | **7.2%** | **19.4%** | **5.9%** |
| **Tier 4: Deep Metazoa / Bilateria Split** | `Metazoa` / `Bilateria` (Protostomia [Worm/Fly] $\leftrightarrow$ Deuterostomia [Vertebrate]) | 500 | 403 | 68 | **13.6%** | 29 | **5.8%** | **19.4%** | **4.6%** |
| **Tier 5: Cross-Kingdom Opisthokonta / Amorphea / Bacteria** | `Opisthokonta` (Fungi $\leftrightarrow$ Metazoa), `Amorphea`, cross-phylum `Bacteria` | 735 | 577 | 101 | **13.7%** | 57 | **7.8%** | **21.5%** | **5.4%** |
| **Tier 6: Cross-Supergroup (Eukaryota root)** | `Eukaryota` (`Viridiplantae`/Algae $\leftrightarrow$ `Opisthokonta`/Protist) | 83 | 66 | 16 | **19.3%** | 1 | **1.2%** | **20.5%** | **10.8%** |
| **Tier 7: Cross-Domain (LUCA)** | `cellular_organisms` (`Bacteria`/`Archaea` $\leftrightarrow$ `Eukaryota`) | 133 | 91 | 30 | **22.6%** | 12 | **9.0%** | **31.6%** | **15.0%** |
| *Excluded: Tier 0 (Unknown donor lineage)* | *Unresolved external donor taxon* | *7* | *6* | *1* | *14.3%* | *0* | *0.0%* | *14.3%* | *14.3%* |

Key observations from Table 1:
- **Clade-to-Tier mapping (`classify_evolutionary_span`)**: `single_organism_distance.py` maps each donor–target LCA clade to Tiers 0–7: `Unknown` $\to$ Tier 0; `Cellular organisms (LUCA)` $\to$ Tier 7; `Eukaryota` $\to$ Tier 6 when either species is in `Viridiplantae`/Algae (`Arabidopsis`, `Oryza`, `Triticum`, `Chlamydomonas`), else Tier 5 (`Amorphea` or `Opisthokonta`); `Bacteria`/`Archaea` $\to$ Tier 5 vs intra-phylum bacterial clades (`Bacillati`, `Gammaproteobacteria`, `Enterobacteriaceae`, `Actinomycetes`) $\to$ Tier 3; `Metazoa` $\to$ Tier 4; phylum/subphylum clades (`Euteleostomi`, `Dikarya`, `Ascomycota`, `Viridiplantae`, `Embryophyta`, `Ecdysozoa`, `Arthropoda`) $\to$ Tier 3; order/subphylum fungal and plant clades (`Saccharomycotina`, `Pezizomycotina`, `Magnoliopsida`, `Pentapetalae`, `rosids`) $\to$ Tier 2; and close mammalian/model genera and superorders (`Eutheria`, `Boreoeutheria`, `Euarchontoglires`, `Primates`, `Hominidae`, `Glires`, `Rodentia`, `Murinae`, `Caenorhabditis`, `Aspergillus`, etc.) $\to$ Tier 1, with an explicit fallback to Tier 2 for any unenumerated intermediate clade.
- Separating **Propagation Failure (`% Fail`)** from **Term Refinement (`% Refn`)** confirms that the distance effect is driven by genuine over-propagation (`REMOVE` + `MARK_AS_OVER_ANNOTATED`), which nearly triples from **8.0%** in Tier 1 to **19.3%** in Tier 6 and **22.6%** in Tier 7, while outright **`% REMOVE`** increases nearly 6-fold (**2.6%** $\to$ **10.8%** $\to$ **15.0%**).
- By contrast, **Term Refinement (`% Refn`)** shows no systematic trend with distance (5.9%–9.0% across most tiers), and separating it explains the apparent anomaly in **Tier 2** ($n = 73$): 12 of the 13 downgraded rows (**16.4%**) are `MODIFY`/`TOO_GENERAL` granularity refinements, whereas only 1 row (**1.4%**, **0.0%** `REMOVE`) is a propagation failure.
- Note that sample sizes in **Tier 2** ($n = 73$), **Tier 6** ($n = 83$), and **Tier 7** ($n = 133$) are much smaller than in Tiers 1, 3, 4, and 5 ($n = 500\text{–}1{,}346$), so point estimates in those smaller tiers carry wider sampling uncertainty.

#### 1B. Total Taxonomic Branch Steps ($s_{\text{up}} + s_{\text{down}}$)

| Total Taxonomic Branch Steps ($s_{\text{up}} + s_{\text{down}}$) | Rated ($n$) | Fail | **% Fail** | Refn | **% Refn** | **% Down** | `REMOVE` | **% `REMOVE`** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **02–06 steps (Close: Genus/Family)** | 59 | 7 | **11.9%** | 2 | **3.4%** | **15.3%** | 5 | **8.5%** |
| **07–12 steps (Order/Superorder, e.g. Rodent–Primate)** | 690 | 55 | **8.0%** | 46 | **6.7%** | **14.6%** | 30 | **4.3%** |
| **13–18 steps (Phylum/Subphylum, e.g. Fish–Mammal)** | 1,214 | 100 | **8.2%** | 82 | **6.8%** | **15.0%** | 34 | **2.8%** |
| **19–24 steps (Kingdom/Supergroup, e.g. Yeast–Human)** | 913 | 147 | **16.1%** | 63 | **6.9%** | **23.0%** | 65 | **7.1%** |
| **25+ steps (Deep Bilateria / Cross-Kingdom / Cross-Domain)** | 550 | 83 | **15.1%** | 38 | **6.9%** | **22.0%** | 26 | **4.7%** |
| *Excluded (unknown donor lineage, `total_tax_steps < 0`)* | *7* | *1* | *14.3%* | *0* | *0.0%* | *14.3%* | *1* | *14.3%* |

*Note on non-monotonicity and UniProt `OC` lineage density*: Raw taxonomic step counts are non-monotonic at the extremes. The `02–06 steps` bin has a small sample size ($n = 59$, where 5 `REMOVE` rows produce an 8.5% `REMOVE` rate, largely on bacterial/yeast intragenus paralogs), and the `25+ steps` bin (4.7% `REMOVE`, 15.1% Fail) is lower than `19–24 steps` (7.1% `REMOVE`, 16.1% Fail) because metazoan UniProt `OC` lineages contain many more intermediate taxonomic ranks (~14–16 ranks in vertebrates/insects) than bacterial or fungal lineages (~6–9 ranks). Consequently, a cross-domain Bacteria $\to$ Bacteria or Yeast $\to$ Human pair often falls into `19–24 steps`, whereas a Worm $\to$ Human (`Bilateria`) pair falls into `25+ steps`. Named phylogenetic tiers (Table 1) are therefore a better-calibrated metric than raw `OC` rank counts.

---

### 2. Excess PAINT Node Depth ($\Delta_{\text{depth}} = d_{\text{LCA}} - d_{\text{PTN}}$)

Even when the single experimental donor and target are close relatives (e.g., `mouse` $\to$ `human`), a PAINT curator may have placed the ancestral `IBD` assertion at `LUCA` or `Eukaryota` rather than at `Mammalia` or `Vertebrata`.

Because UniProt `OC` rank depth varies across kingdoms, the lookup table `PAINT_TAXON_DEPTH` in [`single_organism_distance.py`](single_organism_distance.py) maps all 64 positive-IBD `taxon:*` identifiers across `interpro/panther/*/*-paint.tsv` to an approximate `OC` clade depth ($d_{\text{PTN}} = 0$ for `taxon:131567` `cellular_organisms` and bare `taxon:` root/composite nodes; $1$ for `Eukaryota`/`Opisthokonta`/`Bacteria`/`Archaea`; $2\text{–}5$ for intermediate `Metazoa`/`Bilateria`/`Chordata`/kingdom nodes; $6+$ for `Euteleostomi`/`Tetrapoda`/`Amniota`/`Mammalia`/`Euarchontoglires` and close genus/species nodes such as `Caenorhabditis` `taxon:6237`). Restricting to all **1,538 rated rows on close donor–target pairs ($d_{\text{LCA}} \ge 6$: 1,011 in locally cached PAINT families and 527 in uncached families)** holds donor–target evolutionary distance constant while isolating the effect of **PAINT ancestral node placement ($d_{\text{PTN}}$)**:

| PAINT Ancestral Node Placement ($d_{\text{PTN}}$) on Close Taxonomic Pairs ($d_{\text{LCA}} \ge 6$, total $n = 1{,}538$) | Rated ($n$) | Fail | **% Fail** | Refn | **% Refn** | **% Down** | `REMOVE` | **% `REMOVE`** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Scoped within clade / Vertebrata** ($d_{\text{PTN}} \ge 6$, e.g. `Euteleostomi`, `Tetrapoda`, `Mammalia`, `Caenorhabditis`) | 412 | 27 | **6.6%** | 29 | **7.0%** | **13.6%** | 2 | **0.5%** |
| **Intermediate Metazoa / Bilateria / Chordata** ($2 \le d_{\text{PTN}} \le 5$) | 252 | 18 | **7.1%** | 17 | **6.7%** | **13.9%** | 9 | **3.6%** |
| **Over-deeply placed at `LUCA` / `Eukaryota` / `Opisthokonta` or bare `taxon:`** ($d_{\text{PTN}} \le 1$, $\Delta_{\text{depth}} \ge 5$) | 347 | 29 | **8.4%** | 17 | **4.9%** | **13.3%** | 16 | **4.6%** |
| *Uncached PAINT family (no local `interpro/panther/*/*-paint.tsv` record)* | *527* | *50* | *9.5%* | *34* | *6.5%* | *15.9%* | *15* | *2.8%* |

*(The 347 rows at $d_{\text{PTN}} \le 1$ comprise 121 rows with explicit `taxon:131567` `LUCA` / `taxon:2759` `Eukaryota` / `taxon:33154` `Opisthokonta` labels [10 Fail = 8.3%, 5 `REMOVE` = 4.1%] and 226 rows whose `*-paint.tsv` record has a bare `taxon:` string indicating a family-root or composite-clade `IBD` placement [19 Fail = 8.4%, 11 `REMOVE` = 4.9%].)*

Within cached PAINT families on close donor–target pairs ($n = 1{,}011$), placing a single-organism `IBD` at `LUCA`/`Eukaryota`/`Opisthokonta`/root ($d_{\text{PTN}} \le 1$) or at intermediate pre-vertebrate nodes ($2 \le d_{\text{PTN}} \le 5$) raises the outright `REMOVE` rate **7- to 9-fold** (**3.6%–4.6%** vs **0.5%** when scoped within the clade, $d_{\text{PTN}} \ge 6$), and increases propagation failure from **6.6%** to **8.4%**.

---

### 3. PANTHER Subfamily Dilution (`SAME_SF` vs `CROSS_SF`)

Joining the target protein and single-organism donor protein against cached `interpro/panther/*/*-entries.csv` tests whether they reside in the **same PANTHER subfamily** (`SAME_SF`, typically direct 1:1 orthologs) or **different subfamilies** (`CROSS_SF`, separated by at least one gene-duplication/subfamily-divergence event). Across the 3,426 rated rows with known donor lineage (1,156 with resolved subfamily for both donor and target; 2,270 in `UNKNOWN_SF` where the PANTHER family or external donor seed is not in the local `*-entries.csv` cache):

| Taxonomic Regime | Subfamily Relationship | Rated ($n$) | Fail | **% Fail** | Refn | **% Refn** | **% Down** | `REMOVE` | **% `REMOVE`** |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Close / moderate taxa** ($d_{\text{LCA}} \ge 4$) | `SAME_SF` (same PANTHER subfamily) | 430 | 32 | **7.4%** | 27 | **6.3%** | **13.7%** | 10 | **2.3%** |
| **Close / moderate taxa** ($d_{\text{LCA}} \ge 4$) | `CROSS_SF` (cross-subfamily paralog) | 189 | 20 | **10.6%** | 21 | **11.1%** | **21.7%** | 8 | **4.2%** |
| **Distant taxa** ($0 \le d_{\text{LCA}} \le 3$) | `SAME_SF` (same PANTHER subfamily) | 260 | 32 | **12.3%** | 20 | **7.7%** | **20.0%** | 15 | **5.8%** |
| **Distant taxa** ($0 \le d_{\text{LCA}} \le 3$) | `CROSS_SF` (cross-subfamily paralog) | 277 | 53 | **19.1%** | 16 | **5.8%** | **24.9%** | 24 | **8.7%** |

Crossing a PANTHER subfamily boundary (`CROSS_SF`) increases the **Propagation Failure (`% Fail`)** rate from **7.4% $\to$ 10.6%** in close/moderate taxa and from **12.3% $\to$ 19.1%** in distant taxa, while nearly doubling the **`% REMOVE`** rate (**2.3% $\to$ 4.2%** and **5.8% $\to$ 8.7%**).

---

### 4. Exact PANTHER Tree Edge Steps (`steps_from_ibd`) & Duplications (`duplication_on_path`)

The TreeGrafter path audit (`projects/TREEGRAFTER/graft_paths_all.tsv`) records exact PANTHER tree edge steps (`steps_from_ibd`) and whether a gene-duplication node lies between the `IBD` assertion node and the target (`duplication_on_path`). Because `graft_paths_all.tsv` audits **TreeGrafter (`IEA`)** graft paths on non-PANTHER reference-proteome species (such as `9AVES`, `9POAL`, `AEDAE`) rather than the 3,433 GOA `IBA` population on PANTHER reference species, its direct row-level overlap with GOA `IBA` annotations is only $n = 2$ rows (Table 4B). Evaluating all **383 rated single-taxon `IBD` paths** in the TreeGrafter (`IEA`) audit (Table 4A) provides a complementary measurement of how tree-step length and intervening duplications affect single-donor `IBD` propagation failure:

#### Table 4A: All Single-Taxon `IBD` Paths in `projects/TREEGRAFTER/graft_paths_all.tsv` ($n = 383$ TreeGrafter `IEA` paths)

| Tree Path Regime (`steps_from_ibd`, `duplication_on_path`) | Rated ($n$) | Fail | **% Fail** | Refn | **% Refn** | **% Down** | `REMOVE` | **% `REMOVE`** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **`< 10` tree steps, `duplication_on_path = False`** | 209 | 27 | **12.9%** | 11 | **5.3%** | **18.2%** | 10 | **4.8%** |
| **`< 10` tree steps, `duplication_on_path = True`** | 162 | 28 | **17.3%** | 12 | **7.4%** | **24.7%** | 13 | **8.0%** |
| **`>= 10` tree steps, `duplication_on_path = False`** | 2 | 0 | **0.0%** | 0 | **0.0%** | **0.0%** | 0 | **0.0%** |
| **`>= 10` tree steps, `duplication_on_path = True`** | 10 | 2 | **20.0%** | 1 | **10.0%** | **30.0%** | 1 | **10.0%** |

#### Table 4B: Matched Non-Self GOA `IBA` Subset Overlapping `graft_paths_all.tsv` ($n = 2$)

| Tree Path Regime (`steps_from_ibd`, `duplication_on_path`) | Rated ($n$) | Fail | **% Fail** | Refn | **% Refn** | **% Down** | `REMOVE` | **% `REMOVE`** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **`< 10` tree steps, `duplication_on_path = False`** | 2 | 0 | **0.0%** | 0 | **0.0%** | **0.0%** | 0 | **0.0%** |
| **`< 10` tree steps, `duplication_on_path = True`** | 0 | 0 | **0.0%** | 0 | **0.0%** | **0.0%** | 0 | **0.0%** |
| **`>= 10` tree steps, `duplication_on_path = False`** | 0 | 0 | **0.0%** | 0 | **0.0%** | **0.0%** | 0 | **0.0%** |
| **`>= 10` tree steps, `duplication_on_path = True`** | 0 | 0 | **0.0%** | 0 | **0.0%** | **0.0%** | 0 | **0.0%** |

In Table 4A ($n = 383$ TreeGrafter `IEA` paths), crossing at least one duplication node (`duplication_on_path = True`) on paths of `< 10` steps increases the **Propagation Failure (`% Fail`)** rate from **12.9% $\to$ 17.3%** and the **`% REMOVE`** rate from **4.8% $\to$ 8.0%** ($n = 209$ vs $n = 162$), while paths of $\ge 10$ tree steps are rare in `graft_paths_all.tsv` ($n = 12$ total).

---

## Limitations and Methodological Confounds

1. **Circularity between phylogenetic distance and reviewer policy (and how `--candidates` works)**: The review actions (`REMOVE`, `MARK_AS_OVER_ANNOTATED`, `MODIFY`, `ACCEPT`, `KEEP_AS_NON_CORE`) in `genes/*/*/*-ai-review.yaml` are **not** an independent experimental ground truth. They were produced by AI and human reviewers following [`IBA_REVIEW.md`](../IBA_REVIEW.md) guidelines that explicitly instruct reviewers to check phylogenetic node placement, subfamily divergence, and cross-kingdom pathway differences. Consequently, higher failure rates in Tiers 5–7 and `CROSS_SF` reflect both genuine biological divergence and heightened reviewer scrutiny of deep-node propagations. Conversely, some high-distance single-organism IBAs in the baseline corpus remained at `ACCEPT` or `KEEP_AS_NON_CORE` even when the reviewer's own `reason` text noted a biological caveat. Specifically, `--candidates` in [`single_organism_distance.py`](single_organism_distance.py) filters on `tier >= 4`, `action in {"ACCEPT", "KEEP_AS_NON_CORE"}`, and `reason` matching 13 skeptical keywords (`"do not"`, `"does not"`, `"lacks"`, `"absent"`, `"plant"`, `"yeast-specific"`, `"only in"`, `"artifact"`, `"over-annotat"`, `"mislead"`, `"cytosolic"`, `"not directly"`, `"unlike"`); it does **not** filter on `CROSS_SF`. Thus, `--candidates` serves as an internal **reason-vs-action inconsistency detector**, which we supplemented with PANTHER family/ortholog consistency sweeps to assemble the 15 re-review candidates below.
2. **Sample size variation across strata**: While Tiers 1, 3, 4, and 5 have large denominators ($n = 500\text{–}1{,}346$), Tier 2 ($n = 73$), Tier 6 ($n = 83$), Tier 7 ($n = 133$), the `02–06 steps` bin ($n = 59$), and the `>= 10` TreeGrafter steps bins ($n = 2$ and $n = 10$) have small sample sizes where a handful of rows shift percentages by several points.
3. **Partial local cache coverage of PANTHER families**: Roughly 34% of close-pair single-organism IBAs (`527 / 1,538` in Metric 2) and 66% of all rated rows (`2,270 / 3,426` in Metric 3) belong to PANTHER families or external seed accessions not yet cached under `interpro/panther/`. Metrics 1 and 1B cover 99.8% (`3,426 / 3,433`) of rated rows because they use UniProt `OC` lineages directly.

---

## Candidate Failure Patterns Identified for Re-Review (and Valid Deep Conservation)

Combining `uv run python projects/IBA_REVIEW/single_organism_distance.py --candidates` (which flags Tier 4–7 `ACCEPT`/`KEEP_AS_NON_CORE` rows whose existing `reason` text contains skeptical keywords) with PANTHER family/ortholog consistency sweeps across sibling reviews surfaces five recurring biological failure mechanisms—comprising **15 candidate genes** partitioned into follow-up re-review PRs ([#5703](https://github.com/ai4curation/ai-gene-review/pull/5703) for Tiers 6–7 and [#5704](https://github.com/ai4curation/ai-gene-review/pull/5704) for Tiers 4–5)—alongside a sixth category of valid deep conservation:

1. **Cross-Domain Organelle / Pathway Projection (Bacteria $\leftrightarrow$ Eukaryota, Tier 7)**
   - *Mechanism*: A bacterial enzyme or plastid-targeted nuclear factor is used to seed a `LUCA` or bacterial node for a compartment-specific or pathway-specific claim that differs between bacteria, plastids, and eukaryotic cytosol/mitochondria, or aMOD over-annotation on a plastid subunit is propagated to bacteria.
   - *Candidates identified for re-review ([PR #5703](https://github.com/ai4curation/ai-gene-review/pull/5703))*:
     - `human/MDH1` (`GO:0006099 tricarboxylic acid cycle` from *M. tuberculosis* `mdh` `UniProtKB:P9WK13` via `PTN000600336` at `LUCA`; baseline action `KEEP_AS_NON_CORE` $\to$ proposed `REMOVE`): *M. tuberculosis* has a single TCA-cycle MDH, whereas eukaryotic `MDH1` is the cytosolic malate–aspartate shuttle isoform (mitochondrial `MDH2` runs the TCA cycle).
     - `BACSU/sigF` (`GO:0000976 transcription cis-regulatory region binding` from an *Arabidopsis thaliana* plastid sigma factor `TAIR:locus:2084420` [specific `SIG` paralog not identified in cached records] via `PTN000779307`; baseline action `ACCEPT` $\to$ proposed `REMOVE`): Bacterial sigma factors such as *B. subtilis* SigF recognize promoter DNA only as part of the RNA polymerase holoenzyme (`GO:0000990` / `GO:0016987`) and are non-core transcription factors under GO curation guidelines, matching `GO:0003899 DNA-directed 5'-3' RNA polymerase activity` from the same `PTN000779307|TAIR:locus:2084420` seed (which was already `REMOVE` in the baseline review).

2. **Plant Secondary Metabolism / Subfamily Expansion Projected to Fungi & Animals (Viridiplantae $\leftrightarrow$ Opisthokonta, Tier 6)**
   - *Mechanism*: Land plants expanded enzyme families for specialized pathways (agmatine-route putrescine synthesis, purine/cytokinin nucleoside hydrolysis, plastidial MEP-pathway isoprenoid synthesis) that are absent, non-physiological, or reversed in fungi and metazoans.
   - *Candidates identified for re-review ([PR #5703](https://github.com/ai4curation/ai-gene-review/pull/5703))*:
     - `SCHPO/SPAC11D3.09` & `SCHPO/SPAPB24D3.03` (`GO:0009446 putrescine biosynthetic process` from *Arabidopsis* agmatinases `AT4G08870`/`AT4G08900` via `PTN000144486` at `Eukaryota`; baseline action `KEEP_AS_NON_CORE` $\to$ proposed `MARK_AS_OVER_ANNOTATED`): Fungi synthesize putrescine from ornithine via ornithine decarboxylase and lack an endogenous arginine decarboxylase pathway to generate agmatine.
     - `SCHPO/SPAC17G8.02` & `SCHPO/SPBC1683.06c` (`GO:0006152 purine nucleoside catabolic process`, a single-organism Tier 6 IBA from *Arabidopsis* `NRH1`/`NRH2` `AGI_LocusCode:AT1G05620|AGI_LocusCode:AT2G36310` via `PTN000266727` at `Eukaryota`, baseline action `KEEP_AS_NON_CORE` $\to$ proposed `MARK_AS_OVER_ANNOTATED`; re-reviewed alongside the multi-organism IBA `GO:0008477 purine nucleosidase activity` on the same node `PTN000266727` [`AT1G05620|AT2G36310|UniProtKB:P22564|UniProtKB:Q4QDN1|UniProtKB:Q9I6Y9`], baseline action `KEEP_AS_NON_CORE` $\to$ proposed `MARK_AS_OVER_ANNOTATED` for F/P aspect consistency): Fungal Urh1-family enzymes (`SPAC17G8.02` and paralog `SPBC1683.06c`) are pyrimidine-preferring uridine hydrolases (`GO:0006218` / `GO:0047769`) with negligible purine nucleosidase activity.
     - `human/IDI1` & `human/IDI2` (`GO:0009240 isopentenyl diphosphate biosynthetic process` from *Arabidopsis* `IPP1` `AGI_LocusCode:AT5G16440` via `PTN000853999` at `Eukaryota`; baseline action `KEEP_AS_NON_CORE` $\to$ proposed `MARK_AS_OVER_ANNOTATED`): In the eukaryotic mevalonate pathway, mevalonate diphosphate decarboxylase (`MVD`) synthesizes IPP first and `IDI1`/`IDI2` catalyze its isomerization to DMAPP (`GO:0019682`), whereas the parent class `GO:0009240` treats IPP as the biosynthetic end-product (true in the plastidial/bacterial MEP pathway).

3. **Yeast-Specific Organelle Topologies Projected to Metazoa & Amoebozoa (Fungi $\leftrightarrow$ Metazoa/Amoebozoa, Tier 5–6)**
   - *Mechanism*: *S. cerevisiae* closed-mitosis / nucleus–vacuole junction (NVJ) processes are seeded at `Eukaryota` or `Opisthokonta` from a single SGD annotation and propagated to organisms that lack a yeast-type vacuole or NVJ.
   - *Candidates identified for re-review ([PR #5704](https://github.com/ai4curation/ai-gene-review/pull/5704))*:
     - `human/ATG4D` (`GO:0034727 piecemeal microautophagy of the nucleus` from *S. cerevisiae* `ATG4` `SGD:S000005167` via `PTN002503342` at `Eukaryota`; baseline action `KEEP_AS_NON_CORE` $\to$ proposed `MARK_AS_OVER_ANNOTATED`, matching sibling reviews `human/ATG4C` and `worm/atg-4.1`), plus `human/ATG2B` (`SGD:S000005186` via `PTN000324023`) and `DICDI/atg1` (`SGD:S000003148` via `PTN000681273` at `Eukaryota`; baseline actions `KEEP_AS_NON_CORE` $\to$ proposed `UNDECIDED`, matching sibling reviews `human/ATG2A` and `human/ULK1` where yeast-specific NVJ PMN vs broader nuclear-envelope autophagy remains an open ontology-scoping question).

4. **Metazoan Endomembrane / Tissue Specialization Projected to Fission Yeast (Metazoa $\to$ Fungi, Tier 5)**
   - *Mechanism*: Metazoan-specific organelle organization or cofactor-binding traits from a single human or *Drosophila* protein are placed at `Opisthokonta` or `LUCA` and inherited by fission yeast.
   - *Candidates identified for re-review ([PR #5704](https://github.com/ai4curation/ai-gene-review/pull/5704))*:
     - `SCHPO/lsb6` (`GO:0005802 trans-Golgi network`, `GO:0007030 Golgi organization`, `GO:0007032 endosome organization` from *Drosophila* `Pi4KIIalpha` `FB:FBgn0037339` via `PTN000305230`; baseline action `KEEP_AS_NON_CORE` $\to$ proposed `MARK_AS_OVER_ANNOTATED`).
     - `SCHPO/oar2` (`GO:0048038 quinone binding` from human mitochondrial `CBR4` `UniProtKB:Q8N4T8` via `PTN002449501` at `LUCA`; baseline action `KEEP_AS_NON_CORE` $\to$ proposed `MARK_AS_OVER_ANNOTATED`): Mammalian `CBR4` acquired secondary quinone reductase activity within the heterotetrameric HsHTD2–HsCBR4 mitochondrial FASII complex, whereas fungal 3-oxoacyl-ACP reductases (`OAR1`/`oar2`) are homotetrameric FASII reductases without demonstrated quinone-binding activity.
     - `SCHPO/cit1` (`GO:0005975 carbohydrate metabolic process` from human `CS` `UniProtKB:O75390` via `PTN000201223` at `LUCA`; baseline action `KEEP_AS_NON_CORE` $\to$ proposed `MARK_AS_OVER_ANNOTATED`): Over-broad parent term above TCA cycle (`GO:0006099`).

5. **Holdase vs ATP-Dependent Foldase Conflation in sHSPs (Protostomia $\to$ Deuterostomia, Tier 4)**
   - *Mechanism*: Six *Drosophila* small heat shock proteins in `D. melanogaster` (`Hsp23`, `Hsp26`, `Hsp27`, `l(2)efl`, `CG14207`, `CG7409`) seed `GO:0042026 protein refolding` at `Metazoa` (`PTN000897708`), propagating to vertebrate sHSPs (`DANRE/cryaa` and `DANRE/cryabb`, already `MARK_AS_OVER_ANNOTATED` in baseline; and `human/HSPB2`, baseline `KEEP_AS_NON_CORE` $\to$ proposed `MARK_AS_OVER_ANNOTATED` in [PR #5704](https://github.com/ai4curation/ai-gene-review/pull/5704)) that act as ATP-independent holdases (`GO:0050821 protein stabilization`) without documented Hsp70-refolding handoff.

6. **Valid Deep Conservation (When Single-Organism High-Distance IBAs Succeed)**
   - Importantly, **68.4% of Tier 7 (LUCA)** and **78.5% of Tier 5 (Opisthokonta)** single-organism IBAs are **retained (`ACCEPT` / `KEEP_AS_NON_CORE`)** in the baseline corpus. These succeed when:
     1. The term describes a **core catalytic molecular function** (`F` aspect, e.g., `malate dehydrogenase activity`, `isopentenyl-diphosphate delta-isomerase activity`, `uridine nucleosidase activity`, `3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity`).
     2. Active-site residues and domain architecture are conserved across the `SAME_SF` orthogroup without neofunctionalizing duplications.
     3. The term does not bake in lineage-specific anatomical, organelle-contact, or pathway-direction assumptions.
