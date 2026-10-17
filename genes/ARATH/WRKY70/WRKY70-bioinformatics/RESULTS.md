# WRKY70 DAP-seq promoter-target analysis: results

Analysis date: 2026-10-15. Methods, data URLs and versions: [README.md](README.md).
All numbers below are copied from the script outputs in `results/`,
`results_window_3kb_plus500/` and `results_test_wrky33/`; none are hardcoded in the code.

## Question

Is WRKY70 (AT3G56400) a direct regulator of SA biosynthesis genes (especially ICS1/SID2,
AT1G74710), SA-responsive genes (PR1, PR2, PR5), NPR1, and senescence markers? The literature
is split. Wang et al. 2006 (PMID:17096590) found ICS1 transcript and free SA elevated in
wrky54 wrky70 and proposed that "SA biosynthesis is actively repressed by low levels of
WRKY70 and WRKY54", but did not show WRKY70 binding at ICS1. Saleh et al. 2015
(PMID:26269953) proposed that at rest NPR1 interacts "with WRKY70 to repress PR1
transcription" at a PR1 W-box. Li et al. 2004 (PMID:14742872) framed WRKY70 as an activator
of SA-induced genes acting downstream of NPR1.

This analysis asks a narrower question that genome-wide binding data can answer: **does
WRKY70 protein bind these promoters in the one public genome-wide WRKY70 binding dataset
that could be obtained?**

## Data obtained and not obtained

- **Obtained:** O'Malley et al. 2016 (PMID:27203113) Plant Cistrome DAP-seq for WRKY70,
  dataset `WRKY_tnt/WRKY70_col`, downloaded from neomorph.salk.edu. It contains 8,244 GEM peak events
  on chr1 to chr5. The MEME motif from these peaks has E = 6.1e-1498 over 599 sites, and its
  core contains `GTTGAC`, a W-box (`data/WRKY70_col.meme_m1.txt`). The dataset is therefore
  a functional WRKY DAP-seq experiment. No ampDAP (methylation-free) library exists for
  WRKY70 on the server, only `col`.
- **Obtained for comparison:** 37 other WRKY DAP-seq peak sets from the same resource. Their
  peak counts run from 1,287 to 22,769 (`results/dataset_peak_counts.tsv`), and WRKY70 sits
  in the middle of that range.
- **Not obtained:** no in vivo WRKY70 ChIP-seq was located or downloaded. I did not search
  GEO, ChIP-Atlas or ReMap, because the first-choice DAP-seq source was available. That
  search is still open, and the absence of in vivo data is the main limitation below.
- **Not attempted:** a reproducible SA-treatment RNA-seq gene set. Curated GO BP gene sets
  from the TAIR GAF served as the "SA-responsive" set instead (see Enrichment).
- The authors' own gene-target list (`nS_targets`, 6,714 genes) is used only as a
  cross-check. Its assignment rule is not stated in the cached main text, and it overlaps
  only partly with my promoter definition: 2,607 of my 4,103 promoter-target genes.

## Per-gene result (main window: 2 kb upstream of TSS; `results/query_gene_promoters.tsv`)

WRKY70 peak rank is out of 8,244 peaks, ranked by signalValue (1 = strongest).
"Other WRKY datasets" is how many of the 37 other WRKY DAP-seq sets have a summit in the
same window.

| Gene | WRKY70 peaks in window | best peak (score / signal / rank) | summit offset(s) from TSS | nearest WRKY70 summit anywhere | in authors' nS_targets | other WRKY datasets with a peak (of 37) | TTGACY count (genome pct) | YGACTTTT count (genome pct) |
|---|---|---|---|---|---|---|---|---|
| ICS1/SID2 | **0** | - | - | -11,099 | False | 12 | 4 (89.9) | 1 (96.3) |
| ICS2 | 0 | - | - | +2,523 | False | 1 | 2 (60.3) | 1 (96.3) |
| EDS5 | **2** | 119 / 78.5 / 1981 | -502, -231 | -231 | True | 31 | 6 (98.1) | 1 (96.3) |
| PBS3 | 0 | - | - | +6,867 | False | 4 | 1 (35.1) | 1 (96.3) |
| SARD1 | 1 | 110 / 43.0 / 3691 | -200 | -200 | True | 3 | 2 (60.3) | 0 (76.2) |
| CBP60G | 1 | 123 / 96.0 / 1542 | -904 | -904 | True | 29 | 3 (79.0) | 1 (96.3) |
| EDS1 | 0 (summit at +75) | - | - | +75 | True | 3 | 3 (79.0) | 1 (96.3) |
| PAD4 | 0 | - | - | -4,412 | False | 10 | 4 (89.9) | 0 (76.2) |
| NPR1 | 0 (summit at +126) | - | - | +126 | True | 0 | 0 (11.6) | 1 (96.3) |
| PR1 | **0** | - | - | -12,626 | False | 11 | 4 (89.9) | 3 (99.9) |
| PR2/BGL2 | 0 | - | - | +6,840 | False | 5 | 1 (35.1) | 1 (96.3) |
| PR5 | 1 | 117 / 71.0 / 2226 | -993 | -993 | True | 11 | 3 (79.0) | 0 (76.2) |
| SAG12 | 0 | - | - | -14,920 | False | 0 | 3 (79.0) | 0 (76.2) |
| SAG13 | 0 | - | - | +13,755 | False | 16 | 3 (79.0) | 1 (96.3) |
| SEN1 | 0 | - | - | -10,596 | False | 1 | 3 (79.0) | 0 (76.2) |
| ORE1/NAC092 | 0 | - | - | +10,229 | False | 1 | 1 (35.1) | 2 (99.5) |
| WRKY70 (self) | 0 | - | - | -8,624 | False | 0 | 0 (11.6) | 1 (96.3) |
| ACT2 (control) | 1 | 110 / 41.9 / 3778 | -924 | -924 | False | 19 | 4 (89.9) | 2 (99.5) |

Notes on the table:

- **Genome pct** is the percentage of all 27,420 nuclear protein-coding promoter windows
  with a motif count less than or equal to this gene's. Counts are small integers with many
  ties, so these values are coarse.
- **Window sensitivity** (`results_window_3kb_plus500/`, -3 kb to +500 bp): the only changes
  are that NPR1 gains its +126 peak (score 128, signal 114.0, rank 1222) and EDS1 gains its
  +75 and +265 peaks. ICS1, ICS2, PBS3, PAD4, PR1, PR2, SAG12, SAG13, SEN1 and ORE1 still have
  no WRKY70 peak, and none of these has a WRKY70 summit within 2.5 kb of its TSS.
- **TAIR symbols** read back from the GAF match the intended loci. PR1 and PR5 appear as
  `At2g14610` and `At1g75040`; SEN1 appears as `STR15`; PR2 appears as `BG2`.

## Enrichment (`results/go_set_enrichment.tsv`)

- **Target definition:** at least one WRKY70 summit in the 2 kb upstream window. This gives
  4,103 of 27,420 nuclear protein-coding genes (15.0%).
- **Gene sets:** TAIR GAF annotations, excluding NOT, to the GO term plus its is_a and
  part_of descendants.
- **Test:** two-sided Fisher exact test, uncorrected, 6 tests.

| GO set | size | WRKY70 targets | OR | p |
|---|---|---|---|---|
| GO:0009751 response to salicylic acid | 173 | 39 (22.5%) | 1.66 | 7.3e-3 |
| GO:0009863 SA mediated signaling pathway | 45 | 9 | 1.42 | 0.40 |
| GO:0009697 SA biosynthetic process | 9 | 3 | 2.84 | 0.14 |
| GO:0010150 leaf senescence | 117 | 15 | 0.84 | 0.60 |
| GO:0006952 defense response | 964 | 220 (22.8%) | 1.72 | 5.1e-11 |
| GO:0015979 photosynthesis (control) | 170 | 22 | 0.84 | 0.52 |

**Specificity check: same test with WRKY33 as the focal TF.** This is the `test-other-tf`
run with a 1 kb window, so its window is narrower than the main WRKY70 run.
`results_test_wrky33/` gives:

| GO set | OR | p |
|---|---|---|
| GO:0009751 response to salicylic acid | 1.82 | 0.016 |
| GO:0006952 defense response | 1.96 | 3.9e-10 |

The modest enrichment of WRKY-bound promoters among SA-response and defense genes is
therefore **not WRKY70-specific**. It is consistent with a general property of W-box binding
WRKY proteins and of W-box-rich defense promoters. The GO:0009751 result for WRKY70
(p = 7.3e-3) would sit at the Bonferroni boundary for 6 tests (0.0083), so it should be read as weak.

## Interpretation

What the data show:

1. **No WRKY70 DAP-seq peak at ICS1/SID2.** No summit falls within -3 kb/+0.5 kb of the TSS,
   and the nearest is about 11 kb away. This is not because the ICS1 promoter is
   inaccessible to WRKY proteins in this assay: 12 of the 37 other WRKY DAP-seq datasets have
   a peak in the same 2 kb window. The promoter also carries 4 TTGACY W-boxes.
2. **No WRKY70 DAP-seq peak at PR1.** The same holds at PR1, even though the PR1 promoter has
   3 copies of the WRKY70-associated WT-box YGACTTTT (top 0.1% of promoters genome-wide) and is
   bound by 11 other WRKY datasets. There is also no WRKY70 peak at PR2, PBS3, ICS2 or PAD4.
3. **WRKY70 does have promoter-proximal peaks at other SA-pathway genes.** These are EDS5
   (2 peaks; best at rank 1981 of 8244), CBP60G (rank 1542), SARD1 (rank 3691) and PR5
   (rank 2226). There are also peaks just downstream of the TSS at NPR1 (+126; rank 1222)
   and EDS1 (+75, +265). EDS5 and CBP60G peaks are shared with 31 and 29 of 37 other WRKY
   datasets respectively, so they look like generic WRKY-bound sites, not WRKY70-selective
   ones. SARD1 (3 of 37 others) and NPR1 (0 of 37 others in the 2 kb window; 17 in the wider
   window) are less widely shared.
4. **No WRKY70 peak at the queried senescence genes.** This holds for SAG12, SAG13, SEN1 and
   ORE1. Leaf-senescence genes as a set are not enriched (OR 0.84). WRKY70 also shows no peak
   at its own promoter.
5. **A WRKY70 peak at a housekeeping control.** ACT2 has a WRKY70 peak (rank 3778), which is
   a reminder that a DAP-seq peak alone does not imply a regulatory relationship.

Bearing on the open question:

- **Does not support direct WRKY70 binding at ICS1.** The genome-wide in vitro binding data
  give no support to the hypothesis that WRKY70 represses ICS1 by binding its promoter
  directly (a "WRKY70 -| ICS1" direct edge). The repression of ICS1 and SA reported in
  wrky54 wrky70 (PMID:17096590) is equally compatible with indirect mechanisms, or with
  binding that needs partners, chromatin context or modifications absent from DAP-seq.
- **Neutral on WRKY70 at PR1.** The data do not contradict the WRKY70/NPR1-at-PR1-W-box model
  of PMID:26269953, which concerns a complex with NPR1 in vivo. They also give it no
  independent support.
- **No bearing on direction.** Nothing here addresses activator versus repressor: binding is
  not direction.

## Limitations (important)

- **DAP-seq is in vitro.** It uses in vitro translated WRKY70 (Halo-tagged) on naked,
  fragmented genomic DNA. In the paper's words, DAP-seq "uses in-vitro-expressed TF to
  interrogate naked gDNA fragments" (PMID:27203113). It ignores chromatin, partners (NPR1,
  WRKY54 and others), post-translational modifications (e.g. sumoylation), and induction
  conditions.
  - A **missing** peak means WRKY70 alone did not detectably enrich that fragment under
    these conditions. It does **not** rule out in vivo occupancy.
  - A **present** peak does not establish in vivo occupancy or regulation.
- **Single replicate, single library.** There is one WRKY70 dataset (Col-0 gDNA; no ampDAP),
  so sites occluded by DNA methylation could be missed. GEM peaks were used as distributed,
  and sub-threshold binding is invisible.
- **Promoter assignment is a convention.** TSS = Ensembl/Araport11 gene 5' end. Binding in
  introns, 3' regions or distal enhancers is not counted, although the nearest-summit
  column shows that none lie within about 10 kb of ICS1 or PR1.
- **Motif counts are sequence presence only.** W-boxes are very common: 88% of promoter
  windows have at least one TTGACY.
- **The GO "SA-responsive" sets are imperfect proxies.** They are curated, partly
  expression-based (IEP) annotations, not a defined SA-treatment transcriptome. No
  multiple-testing correction was applied.
- **No in vivo WRKY70 ChIP-seq was analysed.** Such data would be needed to test the
  feedback edge directly.

## Checklist

- [x] Scripts take all inputs and outputs as command-line arguments or config; no results
  are hardcoded (`scripts/promoter_targets.py`, `query_genes.yaml`, `justfile`).
- [x] Tested on another input: WRKY33_col_a as focal TF with a 1 kb window
  (`results_test_wrky33/`). It ran correctly and gave different, plausible output.
- [x] The analyses completed as expected (main run, window-sensitivity run, test run).
- [x] Direct script outputs are in the folder (`results*/`). Raw downloads are git-ignored
  and re-fetchable with `just download`; checksums are in `data/VERSIONS.txt`.
- [x] Provenance is documented (README data table, VERSIONS.txt).
- [?] Independent in vivo confirmation (ChIP-seq) is not available. Conclusions are limited
  to "in vitro DAP-seq binding is / is not detected".
