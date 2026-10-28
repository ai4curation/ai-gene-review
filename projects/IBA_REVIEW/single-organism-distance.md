# Single-Organism IBA Phylogenetic Distance Analysis

## Overview

A recurrent question in IBA review is how to evaluate `IBA` annotations whose `WITH/FROM` column cites experimental descendants from **only a single organism** (excluding self-citations where the target gene is also a donor).

As established in [`IBA_REVIEW.md`](../IBA_REVIEW.md), a single-organism donor list is **not** intrinsically weak when the donor and target are close orthologs and the PAINT curator placed the ancestral `IBD` node at an appropriate clade (for example, mouse $\to$ human within `Euarchontoglires` or `Euteleostomi`). However, when a single organism's experimental annotation is used to seed an ancestral `IBD` deep in the tree—such as at `Opisthokonta`, `Eukaryota`, or `LUCA`—and then propagated down across kingdoms, domains, or multiple gene-duplication boundaries, the risk of over-propagation rises sharply.

This sub-project defines four quantitative distance metrics to measure "how far down (and up) the tree" a single-organism IBA travels, benchmarks them across all 25,298 positive GOA `IBA` annotations in the repository, and uses the resulting high-distance filter to drive targeted re-reviews.

---

## Corpus-Wide Prevalence

Across `genes/*/*/*-goa.tsv` and `interpro/panther/*/*-paint.tsv`:

- **Total positive GOA `IBA` rows**: **25,298** (across 2,711 reviewed genes)
- **Single-organism GOA `IBA` rows (including self-species)**: **6,159** (**24.3%** of all positive IBAs)
- **Single-organism non-self `IBA` rows**: **3,517** (**13.9%** of all positive IBAs) across **2,165 genes** (**3,433** rated with a completed review action)
  - Strictly **1 single donor gene** (`donor_count == 1`): **2,756 rows** (10.9% of all IBAs)
  - Multiple paralogs (`donor_count >= 2`) from **1 single donor organism**: **761 rows** (3.0% of all IBAs)
- **Cached PAINT `IBD` assertions (`interpro/panther/*/*-paint.tsv`)**: **8,161 / 20,108** (**40.6%**) of all cached PAINT `IBD` ancestral rows rest on experimental evidence from a single resolved taxon.

---

## Four Quantitative Distance Metrics

Implemented in [`single_organism_distance.py`](single_organism_distance.py):

### 1. Taxonomic LCA Clade Depth ($d_{\text{LCA}}$) & Branch Steps ($s_{\text{up}} + s_{\text{down}}$)

For each donor–target pair $(O_{\text{donor}}, O_{\text{target}})$, we find their Lowest Common Ancestor (LCA) along the UniProt/NCBI species phylogeny:
- **$d_{\text{LCA}}$**: Clade depth of $\text{LCA}(O_{\text{donor}}, O_{\text{target}})$ from `cellular_organisms` ($d_{\text{LCA}} = 0$ at `cellular_organisms`/`LUCA`, $1$ at `Eukaryota`/`Bacteria`, $2$ at `Metazoa`/`Fungi`/`Viridiplantae`, $3\text{–}4$ at `Bilateria`/`Protostomia`/`Deuterostomia`/`Ascomycota`, $6+$ at `Euteleostomi`/`Tetrapoda`/`Euarchontoglires`).
- **$s_{\text{up}} + s_{\text{down}}$**: Total taxonomic branch steps up from $O_{\text{donor}}$ to $\text{LCA}$ plus down from $\text{LCA}$ to $O_{\text{target}}$.

Across the 3,433 rated non-self single-organism IBA rows, curator downgrade rates (`REMOVE` + `MARK_AS_OVER_ANNOTATED` + `MODIFY` + `TOO_GENERAL`) and `REMOVE` rates increase substantially as the donor–target LCA moves from close clades to cross-kingdom and cross-domain (`LUCA`) splits:

| Phylogenetic Tier | Representative LCA Clades | Rated IBAs | Retained (`ACCEPT` / `KEEP`) | Downgraded | **% Downgraded** | **% `REMOVE`** |
|---|---|---:|---:|---:|---:|---:|
| **Tier 1: Close Clade** | `Euarchontoglires`, `Eutheria`, `Murinae`, `Caenorhabditis` | 1,346 | 1,158 | 188 | **14.0%** | **2.6%** |
| **Tier 2: Order / Subphylum Split** | `Saccharomycotina`, `Pezizomycotina`, `Magnoliopsida` | 80 | 66 | 14 | **17.5%** | **1.2%** |
| **Tier 3: Phylum / Subphylum Split** | `Euteleostomi` (Teleost $\leftrightarrow$ Mammal), `Ascomycota`, `Ecdysozoa` | 556 | 448 | 108 | **19.4%** | **5.9%** |
| **Tier 4: Deep Metazoa / Bilateria Split** | `Metazoa` / `Bilateria` (Protostomia [Worm/Fly] $\leftrightarrow$ Deuterostomia [Vertebrate]) | 500 | 403 | 97 | **19.4%** | **4.6%** |
| **Tier 5: Cross-Kingdom Opisthokonta / Amorphea / Bacteria** | `Opisthokonta` (Fungi $\leftrightarrow$ Metazoa), `Amorphea`, cross-phylum `Bacteria` | 735 | 577 | 158 | **21.5%** | **5.4%** |
| **Tier 6: Cross-Supergroup (Eukaryota root)** | `Eukaryota` (`Viridiplantae`/Algae $\leftrightarrow$ `Opisthokonta`/Protist) | 83 | 66 | 17 | **20.5%** | **10.8%** |
| **Tier 7: Cross-Domain (LUCA)** | `cellular_organisms` (`Bacteria`/`Archaea` $\leftrightarrow$ `Eukaryota`) | 133 | 91 | 42 | **31.6%** | **15.0%** |

Notice that outright **`REMOVE` rates increase nearly 6-fold** from Tier 1 (**2.6%**) to Tier 6 (**10.8%**) and Tier 7 (**15.0%**), while overall downgrade rates more than double (**14.0%** $\to$ **31.6%**).

Grouped by total taxonomic branch steps ($s_{\text{up}} + s_{\text{down}}$):
- **2–6 steps (Close: Genus/Family)**: **15.3%** downgraded (9 / 59; `REMOVE` 8.5%)
- **7–12 steps (Order/Superorder, e.g. Rodent–Primate)**: **14.6%** downgraded (101 / 690; `REMOVE` 4.3%)
- **13–18 steps (Phylum/Subphylum, e.g. Fish–Mammal)**: **15.0%** downgraded (182 / 1,214; `REMOVE` 2.8%)
- **19–24 steps (Kingdom/Supergroup, e.g. Yeast–Human)**: **23.0%** downgraded (210 / 913; `REMOVE` 7.1%)
- **25+ steps (Deep Bilateria / Cross-Kingdom / Cross-Domain)**: **22.0%** downgraded (121 / 550; `REMOVE` 4.7%)

---

### 2. Excess PAINT Node Depth ($\Delta_{\text{depth}} = d_{\text{LCA}} - d_{\text{PTN}}$)

Even when the single experimental donor and target are close relatives (e.g., `mouse` $\to$ `human`), a PAINT curator may have placed the ancestral `IBD` assertion at `LUCA` or `Eukaryota` rather than at `Mammalia` or `Vertebrata`. Defining $\Delta_{\text{depth}} = d_{\text{LCA}} - d_{\text{PTN}}$ isolates this **over-deep node placement** effect while holding donor–target distance constant within close vertebrate pairs ($d_{\text{LCA}} \ge 6$):

| PAINT Ancestral Node Placement ($d_{\text{PTN}}$) on Close Vertebrate Pairs ($d_{\text{LCA}} \ge 6$) | Rated IBAs | Downgraded | **% Downgraded** | **% `REMOVE`** |
|---|---:|---:|---:|---:|
| **Scoped within Vertebrata** ($d_{\text{PTN}} \ge 6$, e.g. `Euteleostomi`, `Tetrapoda`, `Mammalia`) | 404 | 54 | **13.4%** | **0.5%** |
| **Over-deeply placed at `LUCA` or `Eukaryota`** ($d_{\text{PTN}} \le 1$, $\Delta_{\text{depth}} \ge 5$) | 121 | 18 | **14.9%** | **4.1%** |

Even on close vertebrate pairs, placing a single-organism `IBD` at `LUCA` or `Eukaryota` raises the outright `REMOVE` rate **8-fold** (**0.5%** $\to$ **4.1%**).

---

### 3. PANTHER Subfamily Dilution (`SAME_SF` vs `CROSS_SF`)

Joining the target protein and single-organism donor protein against `interpro/panther/*/*-entries.csv` tests whether they reside in the **same PANTHER subfamily** (`SAME_SF`, typically direct 1:1 orthologs) or **different subfamilies** (`CROSS_SF`, separated by at least one gene-duplication/subfamily-divergence event):

| Taxonomic Regime | Subfamily Relationship | Rated IBAs | Downgraded | **% Downgraded** | **% `REMOVE`** |
|---|---|---:|---:|---:|---:|
| **Close / moderate taxa** ($d_{\text{LCA}} \ge 4$) | `SAME_SF` (same PANTHER subfamily) | 430 | 59 | **13.7%** | **2.3%** |
| **Close / moderate taxa** ($d_{\text{LCA}} \ge 4$) | `CROSS_SF` (cross-subfamily paralog) | 189 | 41 | **21.7%** | **4.2%** |
| **Distant taxa** ($d_{\text{LCA}} \le 3$) | `SAME_SF` (same PANTHER subfamily) | 262 | 52 | **19.8%** | **5.7%** |
| **Distant taxa** ($d_{\text{LCA}} \le 3$) | `CROSS_SF` (cross-subfamily paralog) | 282 | 70 | **24.8%** | **8.9%** |

Crossing a PANTHER subfamily boundary adds a **+5 to +8 percentage-point** downgrade penalty and nearly **doubles the `REMOVE` rate** within both close and distant taxonomic regimes.

---

### 4. Exact PANTHER Tree Edge Steps (`steps_from_ibd`) & Duplications (`duplication_on_path`)

Evaluating single-organism `IBD` paths in the TreeGrafter path audit (`projects/TREEGRAFTER/graft_paths_all.tsv`) separates short orthologous paths from deep paths that cross gene-duplication nodes (`duplication_on_path = True`):
- Short paths (`< 10` tree steps from the `IBD` node with `duplication_on_path = False`) show **0.0%** `REMOVE` rate in the matched GOA IBA subset, whereas long paths ($\ge 10$ tree steps from `IBD` with `duplication_on_path = True`) concentrate the cross-paralog over-propagations.

---

## Six Recurring Biological Failure Patterns in High-Distance Single-Organism IBAs

Auditing Tier 4–7 single-organism IBAs reveals six systematic mechanisms by which single-organism deep-node IBAs fail:

1. **Cross-Domain Organelle / Pathway Projection (Bacteria $\leftrightarrow$ Eukaryota, Tier 7)**
   - *Mechanism*: A bacterial metabolic enzyme or plastid-derived factor is used to seed a `LUCA` node (`d_PTN = 0`) for a compartment-specific or pathway-specific process that differs in eukaryotic cytosolic/mitochondrial isoforms.
   - *Examples*:
     - `human/MDH1` (`GO:0006099 tricarboxylic acid cycle` from *M. tuberculosis* `mdh` `UniProtKB:P9WK13` via `PTN000600336` at `LUCA`): *M. tuberculosis* has a single TCA-cycle MDH, whereas eukaryotic `MDH1` is the cytosolic malate–aspartate shuttle isoform (mitochondrial `MDH2` runs the TCA cycle).
     - `BACSU/sigF` (`GO:0000976 transcription cis-regulatory region binding` from *Arabidopsis* plastid `SIG2` via `PTN000779307` at `LUCA`): Sigma factors bind promoter DNA only within the RNA polymerase holoenzyme (`GO:0000987`), not autonomously as `GO:0000976` requires.

2. **Plant Secondary Metabolism / Subfamily Expansion Projected to Fungi & Animals (Viridiplantae $\leftrightarrow$ Opisthokonta, Tier 6)**
   - *Mechanism*: Land plants expanded enzyme families for specialized pathways (agmatine-route putrescine synthesis, purine/cytokinin nucleoside hydrolysis, plastidial MEP-pathway isoprenoid synthesis) that are absent or reversed in fungi and metazoans.
   - *Examples*:
     - `SCHPO/SPAC11D3.09` & `SCHPO/SPAPB24D3.03` (`GO:0009446 putrescine biosynthetic process` from *Arabidopsis* agmatinases `AT4G08870`/`AT4G08900` via `PTN000144486` at `Eukaryota`): Fungi synthesize putrescine from ornithine via ornithine decarboxylase and lack arginine decarboxylase.
     - `SCHPO/SPAC17G8.02` & `SCHPO/SPBC1683.06c` (`GO:0006152 purine nucleoside catabolic process` & `GO:0008477 purine nucleosidase activity` from *Arabidopsis* `NRH1`/`NRH2` via `PTN000266727` at `Eukaryota`): Fungal Urh1-family enzymes are pyrimidine-specific uridine hydrolases with negligible purine activity.
     - `human/IDI1` & `human/IDI2` (`GO:0009240 isopentenyl diphosphate biosynthetic process` from *Arabidopsis* `IPP1` `AT5G16440` via `PTN000853999` at `LUCA`): In the eukaryotic mevalonate pathway, decarboxylation produces IPP first and IDI1/IDI2 *consume* IPP to form DMAPP.

3. **Yeast-Specific Organelle Topologies Projected to Metazoa & Amoebozoa (Fungi $\leftrightarrow$ Metazoa/Amoebozoa, Tier 5–6)**
   - *Mechanism*: *S. cerevisiae* Closed-mitosis / nucleus–vacuole junction (NVJ) processes are seeded at `Eukaryota` or `Opisthokonta` from a single SGD annotation and propagated to organisms that lack a yeast-type vacuole or NVJ.
   - *Examples*:
     - `human/ATG4D`, `human/ATG2B`, & `DICDI/atg1` (`GO:0034727 piecemeal microautophagy of the nucleus` from *S. cerevisiae* `ATG4`/`ATG2`/`ATG1` via `PTN000086985`/`PTN000018094`/`PTN000419822` at `Eukaryota`): PMN is a budding-yeast NVJ process (Nvj1p–Vac8p) absent in mammalian cells and *Dictyostelium*.

4. **Metazoan Endomembrane / Tissue Specialization Projected to Fission Yeast (Metazoa $\to$ Fungi, Tier 5)**
   - *Mechanism*: Metazoan-specific organelle organization or cofactor-binding traits from a single human or *Drosophila* protein are placed at `Opisthokonta` or `LUCA` and inherited by fission yeast.
   - *Examples*:
     - `SCHPO/lsb6` (`GO:0005802 trans-Golgi network`, `GO:0007030 Golgi organization`, `GO:0007032 endosome organization` from *Drosophila* `Pi4KIIalpha` `FB:FBgn0037339` via `PTN000305230`).
     - `SCHPO/oar2` (`GO:0048038 quinone binding` from human mitochondrial `CBR4` `UniProtKB:Q8N4T8` via `PTN002449501` at `LUCA`): Mammalian `CBR4` acquired secondary quinone reductase activity within the mitochondrial FASII complex, whereas fungal 3-oxoacyl-ACP reductases (`OAR1`/`oar2`) lack quinone-binding activity.
     - `SCHPO/cit1` (`GO:0005975 carbohydrate metabolic process` from human `CS` `UniProtKB:O75390` via `PTN000201223` at `LUCA`): Over-broad parent term above TCA cycle.

5. **Holdase vs ATP-Dependent Foldase Conflation in sHSPs (Protostomia $\to$ Deuterostomia, Tier 4)**
   - *Mechanism*: Six *Drosophila* small heat shock proteins in `S. melanogaster` seed `GO:0042026 protein refolding` at `Bilateria` (`PTN000897708`), propagating to vertebrate sHSPs (`human/HSPB2`, `DANRE/cryaa`) that act strictly as ATP-independent holdases (`GO:0050821 protein stabilization`) without documented Hsp70-refolding handoff.

6. **Valid Deep Conservation (When Single-Organism High-Distance IBAs Succeed)**
   - Importantly, **68.4% of Tier 7 (LUCA)** and **78.5% of Tier 5 (Opisthokonta)** single-organism IBAs are **retained (`ACCEPT` / `KEEP_AS_NON_CORE`)**. These succeed when:
     1. The term describes a **core catalytic molecular function** (`F` aspect, e.g., `malate dehydrogenase activity`, `isopentenyl-diphosphate delta-isomerase activity`, `uridine nucleosidase activity`, `3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity`).
     2. Active-site residues and domain architecture are conserved across the `SAME_SF` orthogroup without neofunctionalizing duplications.
     3. The term does not bake in lineage-specific anatomical, organelle-contact, or pathway-direction assumptions.
