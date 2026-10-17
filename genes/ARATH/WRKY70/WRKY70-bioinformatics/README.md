# WRKY70 DAP-seq promoter-target analysis

Question: does Arabidopsis WRKY70 (AT3G56400, UniProt Q9LY00) bind the promoters of
SA-biosynthesis genes (especially ICS1/SID2, AT1G74710), SA-responsive marker genes
(PR1, PR2, PR5), NPR1, and senescence marker genes in genome-wide binding data? Are
WRKY70-bound promoters enriched among curated SA-response genes?

Summary of findings: see [RESULTS.md](RESULTS.md).

## Data sources (all public; raw files are downloaded into `data/`, which is git-ignored)

| Input | URL | Version / notes |
|---|---|---|
| WRKY70 DAP-seq peaks (O'Malley et al. 2016, Cell, PMID:27203113; dataset `WRKY_tnt/WRKY70_col`, Col-0 gDNA library, no ampDAP library exists for WRKY70) | http://neomorph.salk.edu/dap_web/pages/dap_data_v4/peaks/WRKY_tnt/WRKY70_col/chr1-5/chr1-5_GEM_events.narrowPeak | files dated 2018-10-02 on the server; GEM events, 201 bp, summit = col2 + col10 |
| WRKY70 DAP-seq gene-target list as distributed by the authors | .../dap_data_v4/genes/WRKY_tnt/WRKY70_col/chr1-5/chr1-5_GEM_events.nS_targets.txt | assignment rule is not stated in the cached main text of the paper; used only as a cross-check |
| WRKY70 DAP-seq MEME motif | .../dap_data_v4/motifs/WRKY_tnt/WRKY70_col/meme_out/meme_m1.txt | |
| All other WRKY DAP-seq peak sets (37 datasets, col and colamp) | .../dap_data_v4/peaks/WRKY_tnt/<dataset>/chr1-5/chr1-5_GEM_events.narrowPeak | used to ask whether a promoter peak is WRKY70-specific or shared by the WRKY family |
| WRKY33 DAP-seq gene-target list (only for the test run) | .../dap_data_v4/genes/WRKY_tnt/WRKY33_col_a/chr1-5/chr1-5_GEM_events.nS_targets.txt | |
| TAIR10 gene models | https://ftp.ensemblgenomes.ebi.ac.uk/pub/plants/release-63/gtf/arabidopsis_thaliana/Arabidopsis_thaliana.TAIR10.63.gtf.gz | Ensembl Plants release 63; gene features are `araport11`-sourced |
| TAIR10 genome | https://ftp.ensemblgenomes.ebi.ac.uk/pub/plants/release-63/fasta/arabidopsis_thaliana/dna/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz | |
| GO ontology | https://current.geneontology.org/ontology/go-basic.obo | `data-version` recorded in `data/VERSIONS.txt` |
| TAIR GO annotations | https://current.geneontology.org/annotations/tair.gaf.gz | `date-generated` recorded in `data/VERSIONS.txt` |

`data/VERSIONS.txt` (committed) records download time, GO/GAF versions and sha256 checksums.

## Method

`scripts/promoter_targets.py` (all parameters on the command line; query loci and GO sets in
`query_genes.yaml`):

1. TSS = 5' end of the Ensembl `gene` feature (strand aware). Promoter window = `-upstream`
   to `+downstream` bp relative to the TSS (main run: -2000 to 0, i.e. the 2 kb upstream of
   the TSS; sensitivity run: -3000 to +500). A peak is assigned to a promoter if its
   summit lies in the window.
2. For each query gene: number of WRKY70 peaks, max narrowPeak score (col 5), max
   signalValue (col 7), rank of the best peak among all WRKY70 peaks (ranked by
   signalValue), summit offsets, the offset of the nearest WRKY70 summit anywhere on the
   chromosome, membership in the authors' `nS_targets` list, and which of the other 37 WRKY
   DAP-seq datasets have a summit in the same window.
3. Motif presence (not binding): both-strand counts of the W-box `TTGACY` and the WT-box
   `YGACTTTT` (the WRKY70-preferred element reported by Machens et al. 2014, PMID:24104863) in the window,
   with the genome-wide percentile (fraction of all nuclear protein-coding promoter windows
   with a count less than or equal to this one).
4. Enrichment: universe = nuclear protein-coding genes; "target" = >=1 WRKY70 summit in the
   promoter window. GO sets = genes directly annotated (non-NOT, any evidence code) in the
   TAIR GAF to the term or any is_a/part_of descendant. Two-sided Fisher exact test, no
   multiple-testing correction (6 sets; report p-values as is).

## Rerun

```bash
cd genes/ARATH/WRKY70/WRKY70-bioinformatics
just all            # download + analyze + analyze-wide + test-other-tf
# or individually:
just download       # ~105 MB into data/
just analyze        # -> results/
just analyze-wide   # -> results_window_3kb_plus500/
just test-other-tf  # WRKY33_col_a as focal TF, 1 kb window -> results_test_wrky33/
```

The default interpreter is `uv run --project . python`, which installs the pinned
dependencies from `pyproject.toml` (pyyaml 6.0.2, scipy 1.16.1) on first use. Override with
`PYTHON=python3 just analyze` if those packages are already installed.

## Outputs

- `results/query_gene_promoters.tsv` - per query gene table
- `results/go_set_enrichment.tsv` - Fisher tests
- `results/wbox_background.tsv` - genome-wide motif-count distribution per promoter window
- `results/dataset_peak_counts.tsv` - peaks per comparison WRKY dataset
- `results/run_summary.txt` - parameters and global counts
- same files in `results_window_3kb_plus500/` and `results_test_wrky33/`
