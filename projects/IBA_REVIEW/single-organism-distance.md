# Single-Organism IBA Phylogenetic Distance Analysis

## Overview

A recurrent question in IBA review is how to evaluate `IBA` annotations whose `WITH/FROM` column cites experimental descendants from **only a single organism** (excluding self-citations where the target gene's species is also a donor).

As established in [`IBA_REVIEW.md`](../IBA_REVIEW.md), a single-organism donor list is **not** intrinsically weak when the donor and target are close orthologs and the PAINT curator placed the ancestral `IBD` node at an appropriate clade (for example, mouse $\to$ human within `Euarchontoglires` or `Euteleostomi`). However, when a single organism's experimental annotation is used to seed an ancestral `IBD` deep in the tree—such as at `Opisthokonta`, `Eukaryota`, or `LUCA`—and then propagated down across kingdoms, domains, or multiple gene-duplication boundaries, the risk of over-propagation rises substantially.

This sub-project defines five quantitative distance and donor-topology metrics to measure "how far down (and up) the tree" a single-organism or single-clade IBA travels, benchmarks them against existing review actions across all 28,945 positive GOA `IBA` annotations in the repository, and uses the resulting high-distance filter to identify candidate genes for targeted re-review.

---

## Corpus-Wide Prevalence

Across `genes/*/*/*-goa.tsv` and `interpro/panther/*/*-paint.tsv` (reproducible via `uv run python projects/IBA_REVIEW/single_organism_distance.py --summary`):

- **Total positive GOA `IBA` rows scanned**: **28,945** (across **7,337** GOA genes; **7,330** reviewed genes)
- **Single-organism GOA `IBA` rows (including self-species)**: **7,173** (**24.8%** of all positive IBAs)
- **Single-organism non-self `IBA` rows**: **3,988** (**13.8%** of all positive IBAs) across **2,471 genes** (**3,890** rated with a completed review action; **3,883** with a resolved donor UniProt `OC` lineage and **7** excluded in `Tier 0` due to unresolved donor lineage)
  - Strictly **1 single experimental seed token** (`n_seed_tokens == 1`, Regime 1): **3,223 rows** (**11.1%** of all IBAs; **3,139** rated with resolved donor lineage)
  - Multiple paralog seed tokens (`n_seed_tokens >= 2`, Regime 2) from **1 single donor organism**: **765 rows** (**2.6%** of all IBAs; **744** rated with resolved donor lineage)
- **Multi-organism non-self resolved `IBA` rows** (`n_donor_taxa >= 2`, excluding self-species and unresolved external accessions): **5,422 rows** (**5,207** rated with resolved donor lineages: **1,262** unbracketed single-clade jumps in Regime 3 where $d_{\text{MRCA}} > d_{\text{LCA}}$, and **3,945** phylogenetically bracketed transfers in Regime 4 where $d_{\text{MRCA}} \le d_{\text{LCA}}$, plus **149** excluded in `Tier 0` due to an uncached donor species lineage)
- **Cached PAINT `IBD` assertions (`interpro/panther/*/*-paint.tsv`)**: **8,545 / 20,997** (**40.7%**) of all cached PAINT `IBD` ancestral rows rest on experimental evidence from a single resolved taxon.

---

## Action Classification: Propagation Failure vs Term Granularity Refinement

To avoid conflating true homology over-propagation with routine ontology-granularity adjustments, all tables below separate non-retained review actions into two distinct categories:

- **Propagation Failure (`Fail` = `REMOVE` + `MARK_AS_OVER_ANNOTATED`)**: The reviewer judged that the annotated function or process does not hold as a core or valid biological attribute of the target gene (with **`% REMOVE`** reported separately for outright false claims).
- **Term Granularity Refinement (`Refn` = `MODIFY` + `TOO_GENERAL`)**: The essence of the annotation is true of the target gene, but a more specific or better-scoped GO term is preferred.
- **Total Downgraded (`% Down` = `Fail` + `Refn`)**: The combined non-retained rate (`REMOVE` + `MARK_AS_OVER_ANNOTATED` + `MODIFY` + `TOO_GENERAL`), vs **Retained (`Keep` = `ACCEPT` + `KEEP_AS_NON_CORE`)**.

---

## Five Quantitative Distance & Donor-Topology Metrics

Implemented in [`single_organism_distance.py`](single_organism_distance.py):

### 1. Taxonomic LCA Clade Depth ($d_{\text{LCA}}$) & Branch Steps ($s_{\text{up}} + s_{\text{down}}$)

For each donor–target pair $(O_{\text{donor}}, O_{\text{target}})$, we find their Lowest Common Ancestor (LCA) along the UniProt/NCBI species `OC` phylogeny:
- **$d_{\text{LCA}}$**: Clade depth of $\text{LCA}(O_{\text{donor}}, O_{\text{target}})$ from `cellular_organisms` ($d_{\text{LCA}} = 0$ at `cellular_organisms`/`LUCA`, $1$ at `Eukaryota`/`Bacteria`, $2$ at `Metazoa`/`Fungi`/`Viridiplantae`, $3\text{–}4$ at `Bilateria`/`Protostomia`/`Deuterostomia`/`Ascomycota`, $6+$ at `Euteleostomi`/`Tetrapoda`/`Euarchontoglires`).
- **$s_{\text{up}} + s_{\text{down}}$**: Total taxonomic branch steps up from $O_{\text{donor}}$ to $\text{LCA}$ plus down from $\text{LCA}$ to $O_{\text{target}}$.

Across the 3,883 rated non-self single-organism IBA rows with resolved donor lineages (plus 7 rows in `Tier 0` with unresolved donor lineage), **Propagation Failure (`% Fail`)** and **`% REMOVE`** climb substantially as the donor–target LCA moves from close clades to cross-kingdom and cross-domain (`LUCA`) splits:

| Phylogenetic Tier | Representative LCA Clades | Rated | Keep | Fail | **% Fail** | Refn | **% Refn** | **% Down** | **% `REMOVE`** |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Tier 1: Close Clade** | `Euarchontoglires`, `Eutheria`, `Murinae`, `Caenorhabditis` | 1,519 | 1,302 | 121 | **8.0%** | 96 | **6.3%** | **14.3%** | **2.5%** |
| **Tier 2: Intermediate / Unenumerated Clade** | `Saccharomycotina`, `Pezizomycotina`, `Magnoliopsida`, plus unenumerated residual clades (`Mammalia`, `Fungi`, `Bilateria`, `Xenopus`, etc.) | 101 | 76 | 7 | **6.9%** | 18 | **17.8%** | **24.8%** | **2.0%** |
| **Tier 3: Phylum / Subphylum Split** | `Euteleostomi` (Teleost $\leftrightarrow$ Mammal), `Ascomycota`, `Ecdysozoa` | 657 | 512 | 90 | **13.7%** | 55 | **8.4%** | **22.1%** | **5.6%** |
| **Tier 4: Deep Metazoa / Bilateria Split** | `Metazoa` / `Bilateria` (Protostomia [Worm/Fly] $\leftrightarrow$ Deuterostomia [Vertebrate]) | 542 | 426 | 84 | **15.5%** | 32 | **5.9%** | **21.4%** | **4.4%** |
| **Tier 5: Cross-Kingdom Opisthokonta / Amorphea / Bacteria** | `Opisthokonta` (Fungi $\leftrightarrow$ Metazoa), `Amorphea`, cross-phylum `Bacteria` | 808 | 617 | 122 | **15.1%** | 69 | **8.5%** | **23.6%** | **5.6%** |
| **Tier 6: Cross-Supergroup (Eukaryota root)** | `Eukaryota` (`Viridiplantae`/Algae $\leftrightarrow$ `Opisthokonta`/Protist) | 95 | 64 | 27 | **28.4%** | 4 | **4.2%** | **32.6%** | **12.6%** |
| **Tier 7: Cross-Domain (LUCA)** | `cellular_organisms` (`Bacteria`/`Archaea` $\leftrightarrow$ `Eukaryota`) | 161 | 105 | 40 | **24.8%** | 16 | **9.9%** | **34.8%** | **16.1%** |
| *Excluded: Tier 0 (Unknown donor lineage)* | *Unresolved external donor taxon* | *7* | *6* | *1* | *14.3%* | *0* | *0.0%* | *14.3%* | *14.3%* |

Key observations from Table 1:
- **Clade-to-Tier mapping (`classify_evolutionary_span`)**: `single_organism_distance.py` maps each donor–target LCA clade to Tiers 0–7: `Unknown` $\to$ Tier 0; `Cellular organisms (LUCA)` $\to$ Tier 7; `Eukaryota` $\to$ Tier 6 when either species is in `Viridiplantae`/Algae (`Arabidopsis`, `Oryza`, `Triticum`, `Chlamydomonas`), else Tier 5 (`Amorphea` or `Opisthokonta`); `Bacteria`/`Archaea` $\to$ Tier 5 vs intra-phylum bacterial clades (`Bacillati`, `Gammaproteobacteria`, `Enterobacteriaceae`, `Actinomycetes`) $\to$ Tier 3; `Metazoa` $\to$ Tier 4; phylum/subphylum clades (`Euteleostomi`, `Dikarya`, `Ascomycota`, `Viridiplantae`, `Embryophyta`, `Ecdysozoa`, `Arthropoda`) $\to$ Tier 3; order/subphylum fungal and plant clades (`Saccharomycotina`, `Pezizomycotina`, `Magnoliopsida`, `Pentapetalae`, `rosids`) $\to$ Tier 2; and close mammalian/model genera and superorders (`Eutheria`, `Boreoeutheria`, `Euarchontoglires`, `Primates`, `Hominidae`, `Glires`, `Rodentia`, `Murinae`, `Caenorhabditis`, `Aspergillus`, etc.) $\to$ Tier 1, with an explicit fallback (`Tier 2: Other ({lca})`) routing any unenumerated LCA clade to Tier 2 (see §Limitations item 4).
- Separating **Propagation Failure (`% Fail`)** from **Term Refinement (`% Refn`)** confirms that the distance effect is driven by genuine over-propagation (`REMOVE` + `MARK_AS_OVER_ANNOTATED`), which more than triples from **8.0%** in Tier 1 to **28.4%** in Tier 6 and **24.8%** in Tier 7, while outright **`% REMOVE`** increases more than 6-fold (**2.5%** $\to$ **12.6%** $\to$ **16.1%**).
- By contrast, **Term Refinement (`% Refn`)** shows no systematic trend with distance (4.2%–9.9% across Tiers 1 and 3–7), and separating it explains the high total downgrade rate in **Tier 2** ($n = 101$): 18 of the 25 downgraded rows (**17.8%**) are `MODIFY`/`TOO_GENERAL` granularity refinements, whereas only 7 rows (**6.9%**, **2.0%** `REMOVE`) are propagation failures.
- Note that sample sizes in **Tier 2** ($n = 101$), **Tier 6** ($n = 95$), and **Tier 7** ($n = 161$) are much smaller than in Tiers 1, 3, 4, and 5 ($n = 542\text{–}1{,}519$), so point estimates in those smaller tiers carry wider sampling uncertainty.

#### 1B. Total Taxonomic Branch Steps ($s_{\text{up}} + s_{\text{down}}$)

| Total Taxonomic Branch Steps ($s_{\text{up}} + s_{\text{down}}$) | Rated ($n$) | Fail | **% Fail** | Refn | **% Refn** | **% Down** | `REMOVE` | **% `REMOVE`** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **02–06 steps (Close: Genus/Family)** | 160 | 22 | **13.8%** | 13 | **8.1%** | **21.9%** | 11 | **6.9%** |
| **07–12 steps (Order/Superorder, e.g. Rodent–Primate)** | 796 | 66 | **8.3%** | 59 | **7.4%** | **15.7%** | 33 | **4.1%** |
| **13–18 steps (Phylum/Subphylum, e.g. Fish–Mammal)** | 1,340 | 114 | **8.5%** | 97 | **7.2%** | **15.7%** | 38 | **2.8%** |
| **19–24 steps (Kingdom/Supergroup, e.g. Yeast–Human)** | 991 | 180 | **18.2%** | 79 | **8.0%** | **26.1%** | 76 | **7.7%** |
| **25+ steps (Deep Bilateria / Cross-Kingdom / Cross-Domain)** | 596 | 109 | **18.3%** | 42 | **7.0%** | **25.3%** | 26 | **4.4%** |
| *Excluded (unknown donor lineage, `total_tax_steps < 0`)* | *7* | *1* | *14.3%* | *0* | *0.0%* | *14.3%* | *1* | *14.3%* |

*Note on non-monotonicity and UniProt `OC` lineage density*: Raw taxonomic step counts are non-monotonic at the extremes. The `02–06 steps` bin ($n = 160$, 13.8% Fail, 6.9% `REMOVE`) is enriched for intragenus/intraphylum bacterial and fungal paralog transfers, and the `25+ steps` bin (4.4% `REMOVE`, 18.3% Fail) has a lower `REMOVE` rate than `19–24 steps` (7.7% `REMOVE`, 18.2% Fail) because metazoan UniProt `OC` lineages contain many more intermediate taxonomic ranks (~14–16 ranks in vertebrates/insects) than bacterial or fungal lineages (~6–9 ranks). Consequently, a cross-domain Bacteria $\to$ Bacteria or Yeast $\to$ Human pair often falls into `19–24 steps`, whereas a Worm $\to$ Human (`Bilateria`) pair falls into `25+ steps`. Named phylogenetic tiers (Table 1) are therefore a better-calibrated metric than raw `OC` rank counts.

---

### 2. Excess PAINT Node Depth ($\Delta_{\text{depth}} = d_{\text{LCA}} - d_{\text{PTN}}$)

Even when the single experimental donor and target are close relatives (e.g., `mouse` $\to$ `human`), a PAINT curator may have placed the ancestral `IBD` assertion at `LUCA` or `Eukaryota` rather than at `Mammalia` or `Vertebrata`.

Because UniProt `OC` rank depth varies across kingdoms, the lookup table `PAINT_TAXON_DEPTH` in [`single_organism_distance.py`](single_organism_distance.py) maps all 63 explicit positive-IBD `taxon:<id>` identifiers across `interpro/panther/*/*-paint.tsv` to an approximate `OC` clade depth ($d_{\text{PTN}} = 0$ for `taxon:131567` `cellular_organisms`; $1$ for `Eukaryota`/`Opisthokonta`/`Bacteria`/`Archaea`; $2\text{–}5$ for intermediate `Metazoa`/`Bilateria`/`Chordata`/kingdom nodes; $6+$ for `Euteleostomi`/`Tetrapoda`/`Amniota`/`Mammalia`/`Euarchontoglires` and close genus/species nodes such as `Caenorhabditis` `taxon:6237`). Rows in `*-paint.tsv` whose `taxon` column is a bare `taxon:` string (meaning no taxon constraint was recorded in the PAINT GAF; see `src/ai_gene_review/etl/panther_paint.py`) are reported separately rather than assigned a clade depth. Restricting to all **1,751 rated rows on close donor–target pairs ($d_{\text{LCA}} \ge 6$: 917 in locally cached PAINT families with an explicit node taxid, 246 in cached families with an unrecorded blank `taxon:`, and 588 in uncached families)** holds donor–target evolutionary distance constant while isolating the effect of **PAINT ancestral node placement ($d_{\text{PTN}}$)**:

| PAINT Ancestral Node Placement ($d_{\text{PTN}}$) on Close Taxonomic Pairs ($d_{\text{LCA}} \ge 6$, total $n = 1{,}751$) | Rated ($n$) | Fail | **% Fail** | Refn | **% Refn** | **% Down** | `REMOVE` | **% `REMOVE`** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Scoped within clade / Vertebrata** ($d_{\text{PTN}} \ge 6$, e.g. `Euteleostomi`, `Tetrapoda`, `Mammalia`, `Caenorhabditis`) | 486 | 31 | **6.4%** | 36 | **7.4%** | **13.8%** | 2 | **0.4%** |
| **Intermediate Metazoa / Bilateria / Chordata** ($2 \le d_{\text{PTN}} \le 5$) | 298 | 23 | **7.7%** | 24 | **8.1%** | **15.8%** | 10 | **3.4%** |
| **Over-deeply placed at `LUCA` / `Eukaryota` / `Opisthokonta`** ($d_{\text{PTN}} \le 1$, $\Delta_{\text{depth}} \ge 5$) | 133 | 10 | **7.5%** | 8 | **6.0%** | **13.5%** | 5 | **3.8%** |
| *Unrecorded / unmapped PAINT taxon (blank `taxon:` in `*-paint.tsv`)* | *246* | *20* | *8.1%* | *11* | *4.5%* | *12.6%* | *12* | *4.9%* |
| *Uncached PAINT family (no local `interpro/panther/*/*-paint.tsv` record)* | *588* | *60* | *10.2%* | *42* | *7.1%* | *17.3%* | *18* | *3.1%* |

Within cached PAINT families with an explicit node taxon on close donor–target pairs ($n = 917$), placing a single-organism `IBD` at `LUCA`/`Eukaryota`/`Opisthokonta` ($d_{\text{PTN}} \le 1$, $n = 133$) or at intermediate pre-vertebrate nodes ($2 \le d_{\text{PTN}} \le 5$, $n = 298$) raises the outright `REMOVE` rate **8- to 9-fold** (**3.4%–3.8%** vs **0.4%** when scoped within the clade, $d_{\text{PTN}} \ge 6$), and increases propagation failure from **6.4%** to **7.5%–7.7%**. (An additional 246 rows in cached families have a blank `taxon:` column in `*-paint.tsv`—where the PAINT GAF did not record a node taxon constraint, spanning both shallow mouse-only nodes and deeper nodes—and show an 8.1% Fail / 4.9% `REMOVE` rate.)

---

### 3. PANTHER Subfamily Dilution (`SAME_SF` vs `CROSS_SF`)

Joining the target protein and single-organism donor protein against cached `interpro/panther/*/*-entries.csv` tests whether they reside in the **same PANTHER subfamily** (`SAME_SF`, typically direct 1:1 orthologs) or **different subfamilies** (`CROSS_SF`, separated by at least one gene-duplication/subfamily-divergence event). Across the 3,883 rated rows with known donor lineage (1,379 with resolved subfamily for both donor and target; 2,504 in `UNKNOWN_SF` where the PANTHER family or external donor seed is not in the local `*-entries.csv` cache):

| Taxonomic Regime | Subfamily Relationship | Rated ($n$) | Fail | **% Fail** | Refn | **% Refn** | **% Down** | `REMOVE` | **% `REMOVE`** |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Close / moderate taxa** ($d_{\text{LCA}} \ge 4$) | `SAME_SF` (same PANTHER subfamily) | 509 | 43 | **8.4%** | 37 | **7.3%** | **15.7%** | 12 | **2.4%** |
| **Close / moderate taxa** ($d_{\text{LCA}} \ge 4$) | `CROSS_SF` (cross-subfamily paralog) | 242 | 26 | **10.7%** | 31 | **12.8%** | **23.6%** | 11 | **4.5%** |
| **Distant taxa** ($0 \le d_{\text{LCA}} \le 3$) | `SAME_SF` (same PANTHER subfamily) | 313 | 40 | **12.8%** | 31 | **9.9%** | **22.7%** | 17 | **5.4%** |
| **Distant taxa** ($0 \le d_{\text{LCA}} \le 3$) | `CROSS_SF` (cross-subfamily paralog) | 315 | 77 | **24.4%** | 18 | **5.7%** | **30.2%** | 29 | **9.2%** |

Crossing a PANTHER subfamily boundary (`CROSS_SF`) increases the **Propagation Failure (`% Fail`)** rate from **8.4% $\to$ 10.7%** in close/moderate taxa and nearly doubles it from **12.8% $\to$ 24.4%** in distant taxa, while nearly doubling the **`% REMOVE`** rate (**2.4% $\to$ 4.5%** and **5.4% $\to$ 9.2%**).

---

### 4. Exact PANTHER Tree Edge Steps (`steps_from_ibd`) & Duplications (`duplication_on_path`)

The TreeGrafter path audit (`projects/TREEGRAFTER/graft_paths_all.tsv`) records exact PANTHER tree edge steps (`steps_from_ibd`) and whether a gene-duplication node lies between the `IBD` assertion node and the target (`duplication_on_path`). Because `graft_paths_all.tsv` audits **TreeGrafter (`IEA`)** graft paths on non-PANTHER reference-proteome species (such as `9AVES`, `9POAL`, `AEDAE`) rather than the 3,890 GOA `IBA` population on PANTHER reference species, its direct row-level overlap with GOA `IBA` annotations is only $n = 2$ rows (Table 4B). Evaluating all **386 rated single-taxon `IBD` paths** in the TreeGrafter (`IEA`) audit (Table 4A) provides a complementary measurement of how tree-step length and intervening duplications affect single-donor `IBD` propagation failure:

#### Table 4A: All Single-Taxon `IBD` Paths in `projects/TREEGRAFTER/graft_paths_all.tsv` ($n = 386$ TreeGrafter `IEA` paths)

| Tree Path Regime (`steps_from_ibd`, `duplication_on_path`) | Rated ($n$) | Fail | **% Fail** | Refn | **% Refn** | **% Down** | `REMOVE` | **% `REMOVE`** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **`< 10` tree steps, `duplication_on_path = False`** | 210 | 28 | **13.3%** | 11 | **5.2%** | **18.6%** | 11 | **5.2%** |
| **`< 10` tree steps, `duplication_on_path = True`** | 164 | 28 | **17.1%** | 12 | **7.3%** | **24.4%** | 13 | **7.9%** |
| **`>= 10` tree steps, `duplication_on_path = False`** | 2 | 0 | **0.0%** | 0 | **0.0%** | **0.0%** | 0 | **0.0%** |
| **`>= 10` tree steps, `duplication_on_path = True`** | 10 | 2 | **20.0%** | 1 | **10.0%** | **30.0%** | 1 | **10.0%** |

#### Table 4B: Matched Non-Self GOA `IBA` Subset Overlapping `graft_paths_all.tsv` ($n = 2$)

| Tree Path Regime (`steps_from_ibd`, `duplication_on_path`) | Rated ($n$) | Fail | **% Fail** | Refn | **% Refn** | **% Down** | `REMOVE` | **% `REMOVE`** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **`< 10` tree steps, `duplication_on_path = False`** | 2 | 0 | **0.0%** | 0 | **0.0%** | **0.0%** | 0 | **0.0%** |
| **`< 10` tree steps, `duplication_on_path = True`** | 0 | 0 | **0.0%** | 0 | **0.0%** | **0.0%** | 0 | **0.0%** |
| **`>= 10` tree steps, `duplication_on_path = False`** | 0 | 0 | **0.0%** | 0 | **0.0%** | **0.0%** | 0 | **0.0%** |
| **`>= 10` tree steps, `duplication_on_path = True`** | 0 | 0 | **0.0%** | 0 | **0.0%** | **0.0%** | 0 | **0.0%** |

In Table 4A ($n = 386$ TreeGrafter `IEA` paths), crossing at least one duplication node (`duplication_on_path = True`) on paths of `< 10` steps increases the **Propagation Failure (`% Fail`)** rate from **13.3% $\to$ 17.1%** and the **`% REMOVE`** rate from **5.2% $\to$ 7.9%** ($n = 210$ vs $n = 164$), while paths of $\ge 10$ tree steps are rare in `graft_paths_all.tsv` ($n = 12$ total).

---

### 5. Donor-Support Topology Regimes: Single-Gene vs Multi-Paralog vs Single-Clade Jump vs Bracketed Multi-Species ($d_{\text{MRCA}}$ vs $d_{\text{LCA}}$)

A natural follow-up question is whether the elevated propagation failure rate of single-organism IBAs is caused by having only **one experimental seed gene**, or by **lack of phylogenetic bracketing** around the target organism. To test this across all **9,410 resolved non-self GOA `IBA` rows** (**9,246** rated with a completed review action: **9,090** with resolved donor lineages and **156** in `Tier 0`), [`single_organism_distance.py --regimes`](single_organism_distance.py) computes both the **donor-set MRCA clade depth ($d_{\text{MRCA}}$)** across all donor taxa in `WITH/FROM` and the **closest donor–target LCA depth ($d_{\text{LCA}}$)**, partitioning every non-self IBA into four topological regimes:

1. **Regime 1 (`R1_SINGLE_GENE`: 1 taxon, 1 seed token)**: Strictly one experimental donor gene in a single non-self species ($n = 3{,}139$ rated with resolved donor lineage).
2. **Regime 2 (`R2_MULTI_PARALOG_SINGLE_TAXON`: 1 taxon, $\ge 2$ seed tokens)**: Multiple experimental paralog/co-annotated seed genes, all from the same single non-self species ($n = 744$ rated; note that $3{,}139 + 744 = 3{,}883$, matching the Table 1 resolved-lineage single-organism total).
3. **Regime 3 (`R3_SINGLE_CLADE_JUMP`: $\ge 2$ donor taxa, $d_{\text{MRCA}} > d_{\text{LCA}}$)**: Multiple donor species are cited in `WITH/FROM`, but all donor species coalesce within a single restricted clade ($d_{\text{MRCA}} > d_{\text{LCA}}$) before jumping out to the target organism—for example, `mouse` + `rat` (`Rodentia` / `Glires`) jumping to `worm` or `yeast`, `worm` + `fly` (`Ecdysozoa`) jumping to `human`, or `E. coli` + `M. tuberculosis` (`Bacteria`) jumping to `human` ($n = 1{,}262$ rated).
4. **Regime 4 (`R4_BRACKETED_MULTI_SPECIES`: $\ge 2$ donor taxa, $d_{\text{MRCA}} \le d_{\text{LCA}}$)**: Multiple donor species span across or phylogenetically bracket the target organism's LCA—for example, `yeast` + `mouse` bracketing `human`, or `fly` + `zebrafish` bracketing `human` ($n = 3{,}945$ rated).

#### Table 5A: Propagation Failure & Refinement by Donor-Support Topology Regime ($n = 9{,}090$ resolved-lineage rated rows; $n = 9{,}246$ incl. Tier 0)

| Donor-Support Topology Regime | Rated | Keep | Fail | **% Fail** | Refn | **% Refn** | **% Down** | **% `REMOVE`** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **R1: Single donor gene** (`1 taxon, 1 seed`) | 3,139 | 2,503 | 398 | **12.7%** | 238 | **7.6%** | **20.3%** | **4.7%** |
| **R2: Multi-paralog single taxon** (`1 taxon, >= 2 seeds`) | 744 | 599 | 93 | **12.5%** | 52 | **7.0%** | **19.5%** | **4.7%** |
| **R3: Multi-species single-clade jump** (`>= 2 taxa`, $d_{\text{MRCA}} > d_{\text{LCA}}$) | 1,262 | 1,033 | 141 | **11.2%** | 88 | **7.0%** | **18.1%** | **4.0%** |
| **R4: Bracketed multi-species** (`>= 2 taxa`, $d_{\text{MRCA}} \le d_{\text{LCA}}$) | 3,945 | 3,420 | 227 | **5.8%** | 298 | **7.6%** | **13.3%** | **2.1%** |
| *Excluded: Tier 0 / Unknown donor lineage* (`7` single-taxon + `149` multi-taxon) | *156* | *131* | *10* | *6.4%* | *15* | *9.6%* | *16.0%* | *3.2%* |

#### Table 5B: Donor-Support Regimes Stratified by Phylogenetic Distance Band ($d_{\text{LCA}}$ Tiers)

| Distance Band ($d_{\text{LCA}}$ Tier of Closest Donor) | Donor-Support Regime | Rated ($n$) | Fail | **% Fail** | Refn | **% Refn** | **% Down** | `REMOVE` | **% `REMOVE`** |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Close / Intermediate Clade (Tiers 1–2)** | **R1: Single donor gene** | 1,266 | 106 | **8.4%** | 89 | **7.0%** | **15.4%** | 35 | **2.8%** |
| **Close / Intermediate Clade (Tiers 1–2)** | **R2: Multi-paralog single taxon** | 354 | 22 | **6.2%** | 25 | **7.1%** | **13.3%** | 5 | **1.4%** |
| **Close / Intermediate Clade (Tiers 1–2)** | **R3: Multi-species single-clade jump** | 323 | 13 | **4.0%** | 24 | **7.4%** | **11.5%** | 7 | **2.2%** |
| **Close / Intermediate Clade (Tiers 1–2)** | **R4: Bracketed multi-species** | 1,338 | 71 | **5.3%** | 92 | **6.9%** | **12.2%** | 22 | **1.6%** |
| **Phylum / Bilateria Split (Tiers 3–4)** | **R1: Single donor gene** | 938 | 124 | **13.2%** | 68 | **7.2%** | **20.5%** | 43 | **4.6%** |
| **Phylum / Bilateria Split (Tiers 3–4)** | **R2: Multi-paralog single taxon** | 261 | 50 | **19.2%** | 19 | **7.3%** | **26.4%** | 18 | **6.9%** |
| **Phylum / Bilateria Split (Tiers 3–4)** | **R3: Multi-species single-clade jump** | 458 | 55 | **12.0%** | 28 | **6.1%** | **18.1%** | 19 | **4.1%** |
| **Phylum / Bilateria Split (Tiers 3–4)** | **R4: Bracketed multi-species** | 1,978 | 106 | **5.4%** | 169 | **8.5%** | **13.9%** | 41 | **2.1%** |
| **Cross-Kingdom / Supergroup / LUCA (Tiers 5–7)** | **R1: Single donor gene** | 935 | 168 | **18.0%** | 81 | **8.7%** | **26.6%** | 71 | **7.6%** |
| **Cross-Kingdom / Supergroup / LUCA (Tiers 5–7)** | **R2: Multi-paralog single taxon** | 129 | 21 | **16.3%** | 8 | **6.2%** | **22.5%** | 12 | **9.3%** |
| **Cross-Kingdom / Supergroup / LUCA (Tiers 5–7)** | **R3: Multi-species single-clade jump** | 481 | 73 | **15.2%** | 36 | **7.5%** | **22.7%** | 25 | **5.2%** |
| **Cross-Kingdom / Supergroup / LUCA (Tiers 5–7)** | **R4: Bracketed multi-species** | 629 | 50 | **7.9%** | 37 | **5.9%** | **13.8%** | 21 | **3.3%** |

Key takeaways from Tables 5A and 5B:
- **Multiple paralogs in a single species (`R2`) do not reduce propagation failure relative to a single donor gene (`R1`)**: Overall failure (`12.5%` vs `12.7%`) and outright `REMOVE` (`4.7%` vs `4.7%`) are virtually identical between `R2` and `R1`. In **Tiers 3–4 (Phylum/Bilateria Split)**, `R2` has an even higher failure rate than `R1` (**19.2% Fail, 6.9% `REMOVE`** on $n = 261$ vs **13.2% Fail, 4.6% `REMOVE`** on $n = 938$), and in **Tier 6 (`Viridiplantae` $\leftrightarrow$ `Opisthokonta`)** `R2` reaches **48.0% Fail (24.0% `REMOVE`, $n = 25$)** because multiple co-annotated paralogs in one donor organism typically reflect a lineage-specific gene-family expansion or a deep PAINT node spanning a duplication boundary.
- **Multi-species single-clade jumps (`R3`: $d_{\text{MRCA}} > d_{\text{LCA}}$) behave like single-organism jumps (`R1`/`R2`), not like bracketed multi-species IBAs (`R4`)**: Citing two or more donor species from the *same* donor clade (e.g. `mouse` + `rat`, `worm` + `fly`, or two bacteria) yields an overall failure rate of **11.2% (`4.0% REMOVE`, $n = 1{,}262$)**—nearly double that of phylogenetically bracketed multi-species IBAs (**5.8% Fail, `2.1% REMOVE`, $n = 3{,}945$**). In **Tiers 3–4** (**12.0% Fail** in `R3` vs **5.4% Fail** in `R4`; **15.4% Fail, 5.7% `REMOVE`** in Tier 4 Bilateria jumps, $n = 318$) and **Tiers 5–7** (**15.2% Fail** in `R3` vs **7.9% Fail** in `R4`), unbracketed single-clade jumps fail at **2.0- to 2.2-fold higher rates** than bracketed transfers at the same closest-donor distance.
- **Term refinement (`% Refn`) is invariant across all four regimes (`7.0%–7.6%`)**, confirming that the separation between unbracketed (`R1`, `R2`, `R3`: **11.2%–12.7% Fail**) and bracketed (`R4`: **5.8% Fail**) transfers is driven specifically by homology over-propagation rather than ontology granularity preferences.

---

## Limitations and Methodological Confounds

1. **Circularity between phylogenetic distance and reviewer policy (and how `--candidates` works)**: The review actions (`REMOVE`, `MARK_AS_OVER_ANNOTATED`, `MODIFY`, `ACCEPT`, `KEEP_AS_NON_CORE`) in `genes/*/*/*-ai-review.yaml` are **not** an independent experimental ground truth. They were produced by AI and human reviewers following [`IBA_REVIEW.md`](../IBA_REVIEW.md) guidelines that explicitly instruct reviewers to check phylogenetic node placement, subfamily divergence, and cross-kingdom pathway differences. Consequently, higher failure rates in Tiers 5–7, `CROSS_SF`, and unbracketed regimes (`R1`–`R3`) reflect both genuine biological divergence and heightened reviewer scrutiny of deep-node propagations. Conversely, some high-distance single-organism and single-clade IBAs in the baseline corpus remained at `ACCEPT` or `KEEP_AS_NON_CORE` even when the reviewer's own `reason` text noted a biological caveat. Specifically, `--candidates` in [`single_organism_distance.py`](single_organism_distance.py) filters on `tier >= 4`, `action in {"ACCEPT", "KEEP_AS_NON_CORE"}`, and `reason` matching 13 skeptical keywords (`"do not"`, `"does not"`, `"lacks"`, `"absent"`, `"plant"`, `"yeast-specific"`, `"only in"`, `"artifact"`, `"over-annotat"`, `"mislead"`, `"cytosolic"`, `"not directly"`, `"unlike"`); it does **not** filter on `CROSS_SF`. Thus, `--candidates` serves as an internal **reason-vs-action inconsistency detector**, which we supplemented with PANTHER family/ortholog consistency sweeps across Regimes 1–3 to assemble the re-review candidates below. Note that harmonizing candidate proposals with sibling reviews on the same PAINT node is itself subject to the same-pipeline circularity caveat, since those sibling reviews were generated under the same curation guidelines.
2. **Sample size variation across strata**: While Tiers 1, 3, 4, and 5 have large denominators ($n = 542\text{–}1{,}519$), Tier 2 ($n = 101$), Tier 6 ($n = 95$), Tier 7 ($n = 161$), the `02–06 steps` bin ($n = 160$), and the `>= 10` TreeGrafter steps bins ($n = 2$ and $n = 10$) have smaller sample sizes where a handful of rows shift percentages by several points.
3. **Partial local cache coverage of PANTHER families and external donor species**: Roughly 34% of close-pair single-organism IBAs (`588 / 1,751` in Metric 2, plus `246 / 1,751` with an unrecorded blank `taxon:` in `*-paint.tsv`) and 64% of all rated single-organism rows (`2,504 / 3,883` in Metric 3) belong to PANTHER families or external seed accessions not yet cached or lacking taxon metadata under `interpro/panther/`. Metrics 1 and 1B cover 99.8% (`3,883 / 3,890`) of rated single-organism rows (`7` excluded in `Tier 0` from *Sus scrofa* `9823` lacking a local `*-uniprot.txt` file), and Metric 5 covers 98.3% (`9,090 / 9,246`) of rated non-self resolved IBA rows across Regimes 1–4 (`156` excluded in `Tier 0`: `7` single-taxon and `149` multi-taxon rows citing at least one donor species without a local `*-uniprot.txt` lineage).
4. **Residual clade fallback in Tier 2 (`classify_evolutionary_span`)**: Because `classify_evolutionary_span` routes any unenumerated LCA clade string to `Tier 2: Other ({lca})`, Tier 2 ($n = 101$ rated single-organism rows) combines 99 explicitly mapped fungal/plant order/subphylum rows (`Magnoliopsida`: 51, `Saccharomycotina`: 39, `rosids`: 6, `Pentapetalae`: 2, `Pezizomycotina`: 1) with 2 fallback rows (`Poaceae`: 1, `Pseudomonadati`: 1).

---

## Candidate Failure Patterns Identified for Re-Review (and Valid Deep Conservation)

Combining `uv run python projects/IBA_REVIEW/single_organism_distance.py --candidates` (which flags Tier 4–7 `ACCEPT`/`KEEP_AS_NON_CORE` rows whose existing `reason` text contains skeptical keywords) with PANTHER family/ortholog consistency sweeps across single-organism (`R1`/`R2`) and single-clade jump (`R3`) reviews surfaces six recurring biological failure mechanisms—comprising **15 initial single-organism candidate genes** ([PR #5703](https://github.com/ai4curation/ai-gene-review/pull/5703) for Tiers 6–7 and [PR #5704](https://github.com/ai4curation/ai-gene-review/pull/5704) for Tiers 4–5), **13 follow-up single-organism sibling/skeptical audit genes** ([PR #5857](https://github.com/ai4curation/ai-gene-review/pull/5857) and [PR #5861](https://github.com/ai4curation/ai-gene-review/pull/5861)), and **5 multi-paralog (`R2`) and single-clade jump (`R3`) candidate genes**—alongside valid deep conservation:

1. **Cross-Domain Organelle / Pathway Projection (Bacteria $\leftrightarrow$ Eukaryota, Tier 7)**
   - *Mechanism*: A bacterial enzyme or plastid-targeted nuclear factor is used to seed a `LUCA` or bacterial node for a compartment-specific or pathway-specific claim that differs between bacteria, plastids, and eukaryotic cytosol/mitochondria, or a MOD over-annotation on a plastid subunit is propagated to bacteria.
   - *Single-organism (`R1`) candidates ([PR #5703](https://github.com/ai4curation/ai-gene-review/pull/5703) & [PR #5861](https://github.com/ai4curation/ai-gene-review/pull/5861))*:
     - `human/MDH1` (`GO:0006099 tricarboxylic acid cycle` from *M. tuberculosis* `mdh` `UniProtKB:P9WK13` via `PTN000600336` at `LUCA`; `KEEP_AS_NON_CORE` $\to$ `REMOVE` in [PR #5703](https://github.com/ai4curation/ai-gene-review/pull/5703)): *M. tuberculosis* has a single TCA-cycle MDH, whereas eukaryotic `MDH1` is the cytosolic malate–aspartate shuttle isoform (mitochondrial `MDH2` runs the TCA cycle).
     - `BACSU/sigF` (`GO:0000976 transcription cis-regulatory region binding` from an *Arabidopsis thaliana* plastid sigma factor `TAIR:locus:2084420` via `PTN000779307`; `ACCEPT` $\to$ `REMOVE` in [PR #5703](https://github.com/ai4curation/ai-gene-review/pull/5703)): Bacterial sigma factors recognize promoter DNA only as part of the RNA polymerase holoenzyme (`GO:0016987` sigma factor activity; `GO:0003677` DNA binding), aligning `sigF` with paralog `BACSU/sigG`.
     - `SALTY/glxR` (`GO:0006281 DNA repair` from *E. coli* `rutR` `UniProtKB:P0ACU2` via `PTN000612735`; `KEEP_AS_NON_CORE` $\to$ `REMOVE` in [PR #5861](https://github.com/ai4curation/ai-gene-review/pull/5861)): Cross-subfamily propagation from pyrimidine-catabolic regulator RutR (`PTHR13977:SF172`) to distinct allantoin/glyoxylate regulator GlxR (`PTHR13977:SF64`).
   - *Single-clade jump (`R3`) candidate*:
     - `human/ASAH2` (`GO:0042759 long-chain fatty acid biosynthetic process` from two bacterial neutral ceramidases in *M. tuberculosis* and *P. aeruginosa* `UniProtKB:O06769|UniProtKB:Q9I596` via `PTN004377481` at `LUCA`; baseline action `ACCEPT` $\to$ proposed `MARK_AS_OVER_ANNOTATED`): `ASAH2` is a catabolic plasma-membrane neutral ceramidase (`GO:0006672` ceramide metabolic process) that releases free fatty acids by hydrolyzing sphingolipids (`PMID:10781606`, `PMID:16009708`) rather than catalyzing *de novo* long-chain fatty acid biosynthesis; re-reviewing to `MARK_AS_OVER_ANNOTATED` harmonizes `human/ASAH2` with 1:1 vertebrate ortholog `DANRE/asah2` on the same `PTN004377481` node.

2. **Plant Secondary Metabolism / Subfamily Expansion Projected to Fungi & Animals (Viridiplantae $\leftrightarrow$ Opisthokonta, Tier 6)**
   - *Mechanism*: Land plants expanded enzyme families for specialized pathways (agmatine-route putrescine synthesis, purine/cytokinin nucleoside hydrolysis, plastidial MEP-pathway isoprenoid synthesis, secondary-metabolite glycosyltransferases) that are absent, non-physiological, or reversed in fungi and metazoans.
   - *Single-organism (`R1`/`R2`) candidates ([PR #5703](https://github.com/ai4curation/ai-gene-review/pull/5703) & [PR #5861](https://github.com/ai4curation/ai-gene-review/pull/5861))*:
     - `SCHPO/SPAC11D3.09` & `SCHPO/SPAPB24D3.03` (`GO:0009446 putrescine biosynthetic process` from *Arabidopsis* agmatinases `AT4G08870`/`AT4G08900` via `PTN000144486` at `Eukaryota`; `KEEP_AS_NON_CORE` $\to$ `MARK_AS_OVER_ANNOTATED` in [PR #5703](https://github.com/ai4curation/ai-gene-review/pull/5703)): Fungi synthesize putrescine from ornithine via ornithine decarboxylase and lack an endogenous arginine decarboxylase pathway to generate agmatine.
     - `SCHPO/SPAC17G8.02` & `SCHPO/SPBC1683.06c` (`GO:0006152 purine nucleoside catabolic process`, a Regime 2 Tier 6 IBA from *Arabidopsis* `NRH1`/`NRH2` `AGI_LocusCode:AT1G05620|AGI_LocusCode:AT2G36310` via `PTN000266727` at `Eukaryota`, `KEEP_AS_NON_CORE` $\to$ `MARK_AS_OVER_ANNOTATED` alongside `GO:0008477 purine nucleosidase activity` in [PR #5703](https://github.com/ai4curation/ai-gene-review/pull/5703)): Fungal Urh1-family enzymes are pyrimidine-preferring uridine hydrolases (`GO:0006218` / `GO:0045437`) with negligible purine nucleosidase activity.
     - `human/IDI1` & `human/IDI2` (`GO:0009240 isopentenyl diphosphate biosynthetic process` from *Arabidopsis* `IPP1` `AGI_LocusCode:AT5G16440` via `PTN000853999` at `Eukaryota`; `KEEP_AS_NON_CORE` $\to$ `MARK_AS_OVER_ANNOTATED` in [PR #5703](https://github.com/ai4curation/ai-gene-review/pull/5703)): In the eukaryotic mevalonate pathway, `MVD` synthesizes IPP first and `IDI1`/`IDI2` catalyze its isomerization to DMAPP (`GO:0004452` / `GO:0050992`).
     - `human/UGT3A2` (`GO:0008194 UDP-glycosyltransferase activity` from *Arabidopsis* `UGT80A2` `AGI_LocusCode:AT3G07020` via `PTN000370674`; `ACCEPT` $\to$ `MARK_AS_OVER_ANNOTATED` in [PR #5861](https://github.com/ai4curation/ai-gene-review/pull/5861)): `GO:0008194` is a general parent already entailed by the enzyme's experimental sugar-specific activities (`GO:0008375` / `GO:0035250`, `PMID:18728071`).

3. **Yeast-Specific Organelle Topologies & Fermentation Pathways Projected to Metazoa & Amoebozoa (Fungi $\leftrightarrow$ Metazoa/Amoebozoa, Tier 5–6)**
   - *Mechanism*: *S. cerevisiae* closed-mitosis / nucleus–vacuole junction (NVJ) processes or yeast fermentation pathways are seeded at `Eukaryota` or `Opisthokonta` from SGD annotations and propagated to organisms that lack a yeast-type vacuole, NVJ, or fermentation ester synthesis.
   - *Single-organism (`R1`) candidates ([PR #5704](https://github.com/ai4curation/ai-gene-review/pull/5704))*:
     - `human/ATG4D` (`GO:0034727 piecemeal microautophagy of the nucleus` from *S. cerevisiae* `ATG4` `SGD:S000005167` via `PTN002503342` at `Eukaryota`; `KEEP_AS_NON_CORE` $\to$ `MARK_AS_OVER_ANNOTATED` in [PR #5704](https://github.com/ai4curation/ai-gene-review/pull/5704), matching `human/ATG4C` and `worm/atg-4.1`), plus `human/ATG2B` (`SGD:S000005186` via `PTN000324023`) and `DICDI/atg1` (`SGD:S000003148` via `PTN000681273`; `KEEP_AS_NON_CORE` $\to$ `UNDECIDED` in [PR #5704](https://github.com/ai4curation/ai-gene-review/pull/5704), matching `human/ATG2A` and `human/ULK1`).
   - *Multi-paralog single-taxon (`R2`) candidate*:
     - `human/ABHD2` (`GO:0051792 medium-chain fatty acid biosynthetic process` and `GO:0051793 medium-chain fatty acid catabolic process` from three *S. cerevisiae* fermentation medium-chain fatty acid ethyl ester synthases/esterases `EHT1|EEB1|YMR210W` `SGD:S000000381|SGD:S000004823|SGD:S000006016` via `PTN000082647` at `Opisthokonta`; baseline action `KEEP_AS_NON_CORE` $\to$ proposed `MARK_AS_OVER_ANNOTATED`): Human `ABHD2` (`PTHR10896:SF54`) is a progesterone-activated plasma-membrane 2-arachidonoylglycerol (long-chain monoacylglycerol) lipase (`GO:0047372` acylglycerol lipase activity, `PMID:26989199`) and has no demonstrated physiological role in yeast-type medium-chain fatty acid synthesis or catabolism.

4. **Metazoan Endomembrane / Tissue / Developmental Specialization Projected to Fungi or Invertebrates (Metazoa $\to$ Fungi / Protostomia, Tier 4–5)**
   - *Mechanism*: Metazoan- or vertebrate-specific organelle localization, cofactor-binding, or developmental symmetry traits from one or two animal donors are placed at `Bilateria`, `Opisthokonta`, or `LUCA` and inherited by fungi or invertebrates lacking the donor pathway or organelle specialization.
   - *Single-organism (`R1`) candidates ([PR #5704](https://github.com/ai4curation/ai-gene-review/pull/5704), [PR #5857](https://github.com/ai4curation/ai-gene-review/pull/5857), & [PR #5861](https://github.com/ai4curation/ai-gene-review/pull/5861))*:
     - `SCHPO/lsb6` (`GO:0005802 trans-Golgi network`, `GO:0007030 Golgi organization`, `GO:0007032 endosome organization` from *Drosophila* `Pi4KIIalpha` `FB:FBgn0037339` via `PTN000305230`; `KEEP_AS_NON_CORE` $\to$ `MARK_AS_OVER_ANNOTATED` in [PR #5704](https://github.com/ai4curation/ai-gene-review/pull/5704), plus `yeast/LSB6` `GO:0007030` harmonized to `MARK_AS_OVER_ANNOTATED` in [PR #5857](https://github.com/ai4curation/ai-gene-review/pull/5857)).
     - `SCHPO/oar2` (`GO:0048038 quinone binding` from human mitochondrial `CBR4` `UniProtKB:Q8N4T8` via `PTN002449501` at `LUCA`; `KEEP_AS_NON_CORE` $\to$ `MARK_AS_OVER_ANNOTATED` in [PR #5704](https://github.com/ai4curation/ai-gene-review/pull/5704), plus `yeast/OAR1` harmonized to `MARK_AS_OVER_ANNOTATED` in [PR #5857](https://github.com/ai4curation/ai-gene-review/pull/5857)).
     - `SCHPO/cit1` (`GO:0005975 carbohydrate metabolic process` from human `CS` `UniProtKB:O75390` via `PTN000201223` at `LUCA`; `KEEP_AS_NON_CORE` $\to$ `MARK_AS_OVER_ANNOTATED` in [PR #5704](https://github.com/ai4curation/ai-gene-review/pull/5704), plus `yeast/CIT1`, `yeast/CIT2`, `yeast/CIT3`, `human/CS`, and `mouse/Cs` harmonized in [PR #5857](https://github.com/ai4curation/ai-gene-review/pull/5857)).
     - `SCHPO/hsp3101` (`GO:0000723 telomere maintenance` from *S. cerevisiae* `HSP31` via `PTN001631196`; `KEEP_AS_NON_CORE` $\to$ `MARK_AS_OVER_ANNOTATED` in [PR #5861](https://github.com/ai4curation/ai-gene-review/pull/5861)), `yeast/SDS22` (`GO:0007059 chromosome segregation` from *S. pombe* `sds22` via `PTN000018096`; `ACCEPT` $\to$ `KEEP_AS_NON_CORE` in [PR #5861](https://github.com/ai4curation/ai-gene-review/pull/5861)), and `human/DNAJA3` (`GO:0030835 negative regulation of actin filament depolymerization` from *Drosophila* `l(2)tid` via `PTN000017508`; `KEEP_AS_NON_CORE` $\to$ `MARK_AS_OVER_ANNOTATED` in [PR #5861](https://github.com/ai4curation/ai-gene-review/pull/5861)).
   - *Single-clade jump (`R3`) candidates*:
     - `ANOGA/DNAAF1` (`GO:0007368 determination of left/right symmetry` from two vertebrate `Euteleostomi` donors `Danio rerio|Homo sapiens` `UniProtKB:Q8NEP3|ZFIN:ZDB-GENE-031114-4` via `PTN002915666` at `Bilateria`; baseline action `KEEP_AS_NON_CORE` $\to$ proposed `REMOVE`): Left–right body-axis determination via motile nodal cilia is a deuterostome/vertebrate developmental mechanism absent in dipteran insects such as *Anopheles gambiae*, which establish body axes via non-ciliary maternal and planar-polarity cues (`PMID:19804775`).
     - `worm/pdr-1` (`GO:0005783 endoplasmic reticulum` and `GO:0005794 Golgi apparatus` from two mammalian `Euarchontoglires` donors `Homo sapiens|Rattus norvegicus` `RGD:61797|UniProtKB:O60260` via `PTN000188399` at `Bilateria`; baseline action `UNDECIDED` $\to$ proposed `MARK_AS_OVER_ANNOTATED`): *C. elegans* PDR-1 functions in the cytosol and at depolarized mitochondria for ubiquitylation and mitophagy (`PMID:15961382`, `PMID:25896323`), with no evidence of ER or Golgi localization in worms; re-reviewing to `MARK_AS_OVER_ANNOTATED` harmonizes `worm/pdr-1` with invertebrate ortholog `DROME/park` on the same `PTN000188399` node.

5. **Invertebrate Single-Ortholog vs Vertebrate Paralog Subfunctionalization (Protostomia $\to$ Deuterostomia, Tier 4)**
   - *Mechanism*: Invertebrate `Ecdysozoa` donors (*C. elegans*, *D. melanogaster*) have a single ancestral gene before vertebrate whole-genome duplication, and their full ancestral function set is placed at `Bilateria`/`Eumetazoa` and propagated into a vertebrate paralog that lost part of the ancestral toolkit (`PSEUDO_OR_SUBACTIVITY_LOSS` / `FUNCTIONAL_DIVERGENCE`).
   - *Single-organism (`R2`) sHSP candidates ([PR #5704](https://github.com/ai4curation/ai-gene-review/pull/5704) & [PR #5857](https://github.com/ai4curation/ai-gene-review/pull/5857))*: Six *Drosophila* small heat shock proteins (`Hsp23`, `Hsp26`, `Hsp27`, `l(2)efl`, `CG14207`, `CG7409`) seed `GO:0042026 protein refolding` on `PTN000897708`, propagating to vertebrate sHSPs (`human/HSPB2` in [PR #5704](https://github.com/ai4curation/ai-gene-review/pull/5704), and `human/HSPB3`, `human/HSPB7`, `human/HSPB9`, `DANRE/hspb11` in [PR #5857](https://github.com/ai4curation/ai-gene-review/pull/5857)) that act as ATP-independent holdases rather than active refoldases.
   - *Single-clade jump (`R3`) candidate*:
     - `human/PARD3B` (`GO:0007155 cell adhesion` from `Ecdysozoa` donors `C. elegans par-3|D. melanogaster baz` `FB:FBgn0000163|WB:WBGene00003918` via `PTN001046835`, and `GO:0000226 microtubule cytoskeleton organization` from `FB:FBgn0000163|MGI:MGI:2135608|WB:WBGene00003918` on the same node, where `MGI:2135608` is canonical `Pard3` in `PTHR16484:SF7` rather than `PARD3B` in `PTHR16484:SF4`; baseline actions `KEEP_AS_NON_CORE` $\to$ proposed `MARK_AS_OVER_ANNOTATED`): Unlike canonical `PARD3`, vertebrate `PARD3B` (Par3L) does not bind aPKC (`PRKCI`/`PRKCZ`, `PMID:12234934`, `PMID:34815476`) and underwent subfunctionalization, so propagating canonical `par-3`/`baz`/`Pard3` cell-adhesion and microtubule-organization annotations across the vertebrate duplication boundary over-annotates `PARD3B` (harmonizing `human/PARD3B` with 1:1 mammalian ortholog `HORSE/PARD3B` on `PTN001046835`).

6. **Valid Deep Conservation (When Single-Organism and Single-Clade High-Distance IBAs Succeed)**
   - Importantly, **65.2% of Tier 7 (LUCA)** and **76.4% of Tier 5 (Opisthokonta)** single-organism IBAs—and **81.9% of Regime 3 single-clade jumps overall**—are **retained (`ACCEPT` / `KEEP_AS_NON_CORE`)** in the corpus. These succeed when:
     1. The term describes a **core catalytic molecular function** (`F` aspect, e.g., `malate dehydrogenase activity`, `isopentenyl-diphosphate delta-isomerase activity`, `uridine nucleosidase activity`, `3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity`).
     2. Active-site residues and domain architecture are conserved across the `SAME_SF` orthogroup without neofunctionalizing duplications.
     3. The term does not bake in lineage-specific anatomical, organelle-contact, or pathway-direction assumptions.
