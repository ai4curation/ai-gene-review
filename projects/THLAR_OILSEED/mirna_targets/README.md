# Plant & Pennycress (*Thlaspi arvense*) `miRNA -> Target` Datasets

This directory contains parsed, cross-mapped public plant `miRNA -> target` datasets and pennycress (*Thlaspi arvense*, taxon `13288`, assembly `T_arvense_v2` / `GCA_911865555.2`, UniProt proteome `UP000836841`) miRNA locus and target tables supporting the `THLAR_OILSEED` project and plant small RNA gene reviews.

---

## 1. Files in `projects/THLAR_OILSEED/mirna_targets/`

| File | Rows | Description |
| :--- | ---: | :--- |
| [`thlar_mirna_loci_72.tsv`](thlar_mirna_loci_72.tsv) | 72 | All **72 ShortStack-curated pennycress miRNA loci** from Nunn et al. (2022) (*Plant Biotechnol. J.* 20:944–963, PMID:34990041 / PMC9055812, Supplementary Figure 9 & Supplementary Info 1): **53 conserved loci across 25 families** + **19 novel species-specific `Cluster_...` loci**, with heatmap rank, conservation scope, mature 5'->3' sequence, tissue expression profile (Pollen / Inflorescence / Root / Leaf), and pennycress CDS target counts. |
| [`thlar_mirna_targets.tsv`](thlar_mirna_targets.tsv) | 88 | **88 high-confidence conserved miRNA target sites across 73 unique `TAV2_LOCUS` pennycress genes** (`T_arvense_v2` CDSs), cross-mapped to `Tarvense_...` gene IDs, NCBI `CAH...` protein IDs, **73/73 UniProtKB `A0AAU9...` accessions**, 9-tissue mRNA-seq TPM (`pbi13775-sup-0002-DataS1.tsv`), Allen target scores, cleavage site predictions, and *Arabidopsis thaliana* ortholog modules. |
| [`tardb_ath_degradome.tsv`](tardb_ath_degradome.tsv) | 168 | Gene-level deduplicated degradome/PARE-validated *Arabidopsis thaliana* `miRNA -> target` cleavage interactions (151 unique AGI target genes across 168 `(miRNA_family, Target_Gene_AGI)` pairs; Allen score $\le 2.0$, best CleaveLand $p$-value, base-pairing alignment; full 413-row transcript-level table in scratch) parsed from TarDB (`http://www.biosequencing.cn/TarDB/`, Liu et al. 2021, PMID:33980168). |
| [`goa_tair_mirna_annotations.tsv`](goa_tair_mirna_annotations.tsv) | 54 | Non-IEA GO annotations for *A. thaliana* miRNA genes (`goa_arabidopsis_rna.gaf.gz`) and protein-coding miRNA pathway / target genes (`tair.gaf.gz`), documenting both experimental RNAcentral `has_input` annotations and substrate-vs-actor mis-annotations (`CSD1`, `CSD2`, `PXMT1`). |

### Additional Large Brassicaceae & Literature Datasets
Additional multi-species and literature corpora surveyed for this dataset include:
- `tardb_brassicaceae_conserved.tsv` (**11,749 rows** across 6 Brassicaceae species: *A. thaliana* `ath` 3,510; *A. lyrata* `aly` 2,364; *Capsella rubella* `cru` 790; *Eutrema salsugineum* `esa` 1,133 [Lineage II]; *Brassica rapa* `bra` 3,520 [Lineage II]; *B. oleracea* `bol` 432 [Lineage II]).
- `pmiren_ath_targets.tsv` (**5,876 rows** across 455 *A. thaliana* miRNAs from PmiREN 3.0/3.1, including 219 degradome-validated rows with T-plot PDF URLs).
- `pmiren_esa_targets.tsv` (**774 rows** in *Eutrema salsugineum*, the closest Lineage II relative of *Thlaspi arvense* in PmiREN).
- `pmiren_literature_plant_relations.tsv` (**1,309 rows** of literature-curated plant `miRNA -> target` relations with PMIDs, DOIs, and verbatim supporting sentences from PmiREN 3.1 `miRNA_QA_dataset_v1.zip`, Figshare DOI `10.6084/m9.figshare.34024083`).

---

## 2. Summary of the 72 Pennycress miRNA Loci (Nunn et al. 2022)

Nunn et al. (2022) (*Plant Biotechnol. J.* 20:944–963, PMID:34990041 / PMC9055812) sequenced sRNAs across 4 pennycress tissues (Pollen, Inflorescence, Root, and Rosette Leaf) and annotated 74 candidate miRNA loci with ShortStack v3.8.5 against the `T_arvense_v2` reference genome, confirming **72 bona fide miRNA loci** (after rejecting `Cluster_11184` and `Cluster_1133`):

- **53 Conserved Loci across 25 miRNA Families:**
  - **20 broadly conserved Rosid families:** `miR156` (8 loci), `miR166` (5), `miR160` (3), `miR164` (3), `miR171` (3), `miR172` (3), `miR159` (2), `miR162` (2), `miR167` (2), `miR169` (2), `miR319` (2), `miR390` (2), `miR396` (2, including `Cluster_18198`), `miR168` (1), `miR393` (1), `miR395` (1), `miR397` (1), `miR398` (1), `miR399` (1), `miR403` (1), `miR408` (1, `Cluster_8158`).
  - **4 Brassicaceae-specific families:** `miR157` (2 loci), `miR165` (2 loci), `miR161` (1 locus).
  - **1 family shared only with rice:** `miR817` (1 locus).
- **19 Novel Species-Specific Loci (`Thlaspi arvense`):**
  - `Cluster_229`, `Cluster_1094`, `Cluster_1095`, `Cluster_2822`, `Cluster_3759`, `Cluster_5256`, `Cluster_7729`, `Cluster_10185`, `Cluster_10472`, `Cluster_10717`, `Cluster_10911`, `Cluster_11286`, `Cluster_13389`, `Cluster_14209`, `Cluster_15766`, `Cluster_16169`, `Cluster_16503`, `Cluster_16818`, `Cluster_18440`.

---

## 3. Conserved `miRNA -> Target` Regulatory Modules in Pennycress & Relevance to `THLAR_OILSEED`

| miRNA Family | Pennycress Loci | Pennycress Target Genes (`TAV2_LOCUS` / UniProtKB) | *Arabidopsis* Orthologs | Biological & Oilseed Domestication Role |
| :--- | :--- | :--- | :--- | :--- |
| **`miR156` / `miR157`** | 10 loci (`miR156` x8, `miR157` x2) | 7 SBP-box TFs: `TAV2_LOCUS686` (`A0AAU9R598`), `TAV2_LOCUS8053` (`A0AAU9RQH6`), `TAV2_LOCUS13245` (`A0AAU9S4J6`), `TAV2_LOCUS687` (`A0AAU9R5F0`), `TAV2_LOCUS16487` (`A0AAU9SHU7`), `TAV2_LOCUS22078` (`A0AAU9SUB7`), `TAV2_LOCUS17655` (`A0AAU9SHM7`) | `SPL2/3/4/5/6/9/10/11/13/15` | Controls vegetative-to-reproductive phase transition, flowering time, silique maturation, and seed oil/mucilage partitioning (`miR156-SPL-miR172-AP2/WRI1` cascade). |
| **`miR172`** | 3 loci (`miR172`, `.1`, `.2`) | 6 AP2/ERF TFs: `TAV2_LOCUS18783` (`A0AAU9SIR0`), `TAV2_LOCUS23360` (`A0AAU9T1Q2`), `TAV2_LOCUS13511` (`A0AAU9S9H0`), `TAV2_LOCUS15398` (`A0AAU9SFF7`), `TAV2_LOCUS5241` (`A0AAU9RHM9`), `TAV2_LOCUS12280` (`A0AAU9S8K1`) | `AP2`, `TOE1`, `TOE2`, `TOE3`, `SMZ`, `SNZ` | Represses `AP2`-clade floral repressors; `AP2` negatively regulates seed size, seed coat mucilage, and embryo oil accumulation (`WRI1`-linked lipid synthesis; see `projects/THLAR_OILSEED.md`). |
| **`miR395`** | 1 locus (`miR395`) | ATP sulfurylase `TAV2_LOCUS7508` (`A0AAU9RRK7`, **peak TPM 1655.64 in `seed_pod`**) & sulfate transporters `TAV2_LOCUS14532` (`A0AAU9S8I4`), `TAV2_LOCUS21835` (`A0AAU9SVI0`) | `APS1/3/4` (`AT3G22890`, `AT5G43780`), `SULTR2;1` (`AT5G10180`) | Directs sulfate assimilation (PAPS synthesis) and root-to-pod sulfate translocation required for **glucosinolate (sinigrin) biosynthesis** in pennycress seeds (`AOP2`/`GTR1`/`GTR2` module). |
| **`miR396`** | 2 loci (`miR396`, `miR396.1` / `Cluster_18198`) | 7 Growth-Regulating Factors (`GRF`): `TAV2_LOCUS16031` (`A0AAU9SIN8`, peak TPM 93.5 in `green_seed`), `TAV2_LOCUS24911` (`A0AAU9T2T6`, 42.2 in `green_seed`), `TAV2_LOCUS13594` (`A0AAU9S7K7`, 27.4 in `green_seed`), `TAV2_LOCUS13892` (`A0AAU9S9E5`), `TAV2_LOCUS23382` (`A0AAU9T6Q2`), `TAV2_LOCUS19183` (`A0AAU9SNP5`), `TAV2_LOCUS11916` (`A0AAU9S2D3`) | `GRF1/2/3/4/7/8/9` | Canonical 1-nt bulge cleavage site (`CCGTTCAAGAAAGCCTGTGGAA`); major regulator of embryo cell proliferation, seed size, and seed oil content in Brassicaceae oilseeds. |
| **`miR397`** | 1 locus (`miR397`) | 2 Laccases: `TAV2_LOCUS14099` (`A0AAU9S9S2`, **peak TPM 202.75 in `seed_pod`**) & `TAV2_LOCUS22308` (`A0AAU9SLN0`) | `LAC2`, `LAC4`/`IRX12`, `LAC17` | Regulates seed pod and seed coat lignin polymerization, pod shatter resistance (`IND` pathway), and seed coat permeability/dormancy (`TT` module). |
| **`miR160` / `miR167` / `miR393`** | 6 loci (`miR160` x3, `miR167` x2, `miR393` x1) | `ARF10/16/17`: `TAV2_LOCUS15436` (`A0AAU9SP38`), `TAV2_LOCUS19535` (`A0AAU9T051`), `TAV2_LOCUS13658` (`A0AAU9S5Q0`), `TAV2_LOCUS23883` (`A0AAU9T4H6`), `TAV2_LOCUS4572` (`A0AAU9RG42`); `ARF6/8`: `TAV2_LOCUS16836` (`A0AAU9SGH2`), `TAV2_LOCUS23322` (`A0AAU9T5K7`); `TIR1/AFB`: `TAV2_LOCUS4099` (`A0AAU9RGU5`), `TAV2_LOCUS16707` (`A0AAU9SBX4`), `TAV2_LOCUS7969` (`A0AAU9RKX6`), `TAV2_LOCUS18979` (`A0AAU9SS77`) | `ARF10/16/17`, `ARF6/8`, `TIR1/AFB1-3`, `bHLH77` | Coordinates auxin perception and signaling across root architecture, flower/anther maturation, silique elongation, and seed dormancy. |
| **`miR164` / `miR165` / `miR166`** | 10 loci (`miR164` x3, `miR165` x2, `miR166` x5) | 6 NAC TFs (`TAV2_LOCUS5185` / `A0AAU9RIK5`, `TAV2_LOCUS20428` / `A0AAU9SW16`, etc.) & 6 HD-ZIP III TFs (`TAV2_LOCUS3035` / `A0AAU9RAT6`, `TAV2_LOCUS21990` / `A0AAU9SL93`, etc.) | `CUC1/2`, `NAC1`, `ORE1`; `PHB`, `PHV`, `REV`, `ATHB-8/15` | Controls carpel margin/septum fusion, ovule integument polarity, vascular patterning, and pod senescence. |
| **`miR162`** | 2 loci (`miR162`, `miR162.1`) | `DCL1`: `TAV2_LOCUS3068` (`A0AAU9RFA2`, peak TPM 91.37 in `inflorescence`) | `DCL1` (`AT1G01040`) | Negative feedback cleavage of `DCL1` mRNA to maintain miRNA biogenesis homeostasis (`modules/plant_mirna_biogenesis.yaml`). |
| **`miR161` / `miR390`** | 3 loci (`miR161` x1, `miR390` x2) | 6 `PPR` genes (`TAV2_LOCUS6988` / `A0AAU9RU77`, `TAV2_LOCUS5004` / `A0AAU9RSC9`, etc.) & 2 `LRR` genes (`TAV2_LOCUS8390`, `TAV2_LOCUS8392`) | `PPR-P` clade, `TAS3` | Triggers secondary phasiRNA and `TAS3` tasiRNA biogenesis (`GO:0035278`). |

---

## 4. GOA / TAIR Curation Audit (`goa_tair_mirna_annotations.tsv`)

Inspection of `goa_arabidopsis_rna.gaf.gz` and `tair.gaf.gz` revealed two critical curation findings for plant miRNAs and their targets:

1. **Severe under-curation of experimentally validated plant miRNA targets in RNAcentral/GOA:**
   - Out of **892 miRNA annotations** in `goa_arabidopsis_rna.gaf.gz`, **888 (99.5%)** are uncurated `IEA` annotations to generic `GO:0035195` (*miRNA-mediated post-transcriptional gene silencing*) and `GO:0016442` (*RISC complex*) without target extensions.
   - Only **2 *Arabidopsis* miRNAs** have experimental (`IDA`) annotations in `goa_arabidopsis_rna.gaf.gz`: `URS00005C2DB4_3702` (`ath-miR390a/b-5p`, with `has_input(UniProtKB:Q1EBS9)`) and `URS00005F3E4D_3702` (`ath-miR173-5p`), both from `PMID:34192539` for secondary siRNA (`tasiRNA`) biogenesis (`GO:0035278`).
2. **Substrate-vs-actor mis-annotation on protein-coding target genes in `tair.gaf.gz`:**
   - Three *Arabidopsis* protein-coding genes — **`CSD1` (`AT1G08830`)**, **`CSD2` (`AT2G28190`)** (Cu/Zn superoxide dismutases cleaved by `miR398`, `PMID:16861386`), and **`PXMT1` (`AT1G66700`)** (paraxanthine methyltransferase cleaved by `miR163`, `PMID:21602291`, `PMID:26768601`, `PMID:28401908`) — are annotated in `tair.gaf.gz` as `involved_in GO:0035195` (*miRNA-mediated post-transcriptional gene silencing*, `IEP`).
   - Per our GO curation guidelines (`AGENTS.md`, *"Do not add what curators deliberately declined to add"*), being the mRNA substrate cleaved by a miRNA-loaded RISC is **not** participation in the silencing machinery (`GO:0035195`). Those `GO:0035195` rows on `CSD1`, `CSD2`, and `PXMT1` should be marked `REMOVE` when reviewing those genes.
