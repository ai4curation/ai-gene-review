# iModulonDB Integration

## Overview

The iModulonDB integration allows you to compare gene reviews with machine learning-derived transcriptional modules (iModulons) for bacterial genes. This provides independent validation of gene regulatory annotations using data-driven approaches.

## What is iModulonDB?

[iModulonDB](https://imodulondb.org/) is a database of independently modulated gene sets (iModulons) derived from applying Independent Component Analysis (ICA) to bacterial transcriptomes. iModulons represent co-regulated gene groups that explain variance across diverse growth conditions.

**Key Features:**
- Data-driven approach using hundreds of transcriptomes
- Identifies co-regulated gene modules
- Provides precision/recall metrics vs. known regulons
- Available for multiple bacterial species

**Reference:** Sastry et al. 2021, *Nucleic Acids Research* 49:D112-D120

## Supported Organisms

Currently supported organisms with iModulonDB datasets:

| Organism | Code | Dataset | Reference |
|----------|------|---------|-----------|
| *Pseudomonas putida* KT2440 | PSEPK / p_putida | precise321 | Lim et al. 2022 |
| *Escherichia coli* K-12 MG1655 | ecoli / e_coli | precise456 | Sastry et al. 2019 |
| *Bacillus subtilis* 168 | b_subtilis | precise91 | Rychel et al. 2020 |

To see the current list:
```bash
just list-imodulondb-organisms
```

## Quick Start

### Compare a Single Gene

```bash
just compare-imodulondb PSEPK BenR
```

This will:
1. Download iModulonDB data for *P. putida* (cached locally)
2. Find the BenR iModulon
3. Extract gene weights and statistics
4. Generate comparison report

Output: `genes/p_putida/BenR/BenR-imodulondb-comparison.md`

### Example Output

```markdown
# BenR iModulonDB Comparison

## BenR iModulon Statistics

| Metric | Value |
|--------|-------|
| **iModulon Size** | 10 genes |
| **Known Regulon Size** | 4 genes |
| **Precision** | 0.40 (40%) |
| **Recall** | 1.00 (100%) |
| **F1 Score** | 0.57 |

## Interpretation

**Consistency Level**: HIGH

✅ **Perfect Recall**: All known regulon members captured in iModulon.
⚠️ **Moderate Precision**: iModulon contains additional genes suggesting functional coupling.
```

## Use Cases

### 1. Validate Gene Review

After completing a gene review, compare with iModulonDB to:
- Confirm direct regulatory targets
- Identify potential novel targets
- Assess consistency with transcriptomic data

```bash
just compare-imodulondb PSEPK BenR
```

### 2. Identify Novel Regulatory Targets

iModulons may include genes not in literature-based regulons:
- Genes with high weights but not in review → novel predictions
- Functionally coupled genes (indirect regulation)
- Cross-pathway regulatory connections

### 3. Distinguish Direct vs. Functional Coupling

**Direct regulation**: High weight + known target (e.g., benABCD for BenR)
**Functional coupling**: High weight + downstream pathway (e.g., cat genes with ben genes)

### 4. Cross-Organism Comparison

Compare regulatory patterns across species:
```bash
just compare-imodulondb ecoli FliA
just compare-imodulondb bsubtilis SigD
# Compare flagellar regulation across organisms
```

## Understanding the Metrics

### iModulon Statistics

- **iModulon Size**: Number of genes in data-driven module
- **Known Regulon Size**: Number of validated targets from literature
- **True Positives (TP)**: Genes in both iModulon and known regulon
- **Precision**: TP / iModulon Size (fraction of iModulon that's validated)
- **Recall**: TP / Regulon Size (fraction of known targets captured)
- **F1 Score**: Harmonic mean of precision and recall

### Consistency Levels

- **HIGH** (F1 ≥ 0.5, Recall ≥ 0.8): Strong validation
- **MEDIUM** (F1 ≥ 0.4, Recall ≥ 0.6): Partial validation
- **LOW** (F1 < 0.4 or Recall < 0.6): Discrepancies warrant investigation

### Gene Weights

Gene weights from ICA indicate strength of co-regulation:
- **|weight| > 0.2**: Strong association (likely direct targets)
- **|weight| 0.1-0.2**: Moderate association (direct or coupled)
- **|weight| 0.05-0.1**: Weak association (may be indirect)
- **|weight| < 0.05**: Not significantly associated

## Interpreting Results

### Perfect Recall, Moderate Precision

**Example**: BenR has recall=1.0, precision=0.4

**Interpretation**:
- ✅ All known targets captured (good!)
- ⚠️ iModulon includes 6 additional genes
- These may be: (a) novel predictions, (b) functionally coupled, or (c) false positives

**Action**: Investigate high-weight genes not in review

### Imperfect Recall

**Example**: Recall = 0.7 (missing 30% of known targets)

**Possible reasons**:
- Known targets not co-expressed across conditions
- Context-specific regulation
- Data quality issues
- Literature over-annotation

**Action**: Check which genes are missing and why

### Low Precision

**Example**: Precision = 0.2 (80% of iModulon not validated)

**Possible reasons**:
- Captures functional pathway, not just direct regulation
- Novel targets awaiting experimental validation
- Promiscuous regulator with many targets
- iModulon captures complex regulatory logic

**Action**: Distinguish functional coupling from direct regulation

## Advanced Usage

### Custom Cache Directory

```bash
just compare-imodulondb PSEPK BenR --cache-dir /path/to/cache
```

### Batch Analysis

For multiple genes:
```bash
for gene in BenR CatR PcaR; do
  just compare-imodulondb PSEPK $gene
done
```

### Clean Cache

To re-download data:
```bash
just clean-imodulondb-cache
just compare-imodulondb PSEPK BenR
```

## File Structure

```
.cache/imodulondb/
  p_putida/
    supplementary_data.xlsx     # Downloaded from GitHub
  e_coli/
    supplementary_data.xlsx

genes/
  p_putida/
    BenR/
      BenR-imodulondb-comparison.md   # Generated comparison
```

## Implementation Details

### Data Source

iModulonDB data is downloaded from organism-specific GitHub repositories:
- **P. putida**: [SBRG/modulome_ppu](https://github.com/SBRG/modulome_ppu)
- **E. coli**: [SBRG/modulome_eco](https://github.com/SBRG/modulome_eco)
- **B. subtilis**: [SBRG/modulome_bsu](https://github.com/SBRG/modulome_bsu)

### Caching

- Downloaded files are cached in `.cache/imodulondb/`
- Subsequent runs use cached data (faster)
- Cache persists across sessions
- Use `just clean-imodulondb-cache` to force re-download

### Organism Mapping

Organism codes are mapped in: `src/ai_gene_review/data/imodulondb_organisms.yaml`

To add new organisms, edit this file with:
- Taxon ID
- iModulonDB code
- GitHub repository
- Dataset name
- Reference citation

## Troubleshooting

### "Organism not found in iModulonDB mapping"

**Solution**: Check organism code with `just list-imodulondb-organisms`

### "No iModulon found for regulator"

**Possible reasons**:
1. Gene is not a transcription factor
2. Gene name mismatch (try alternative names)
3. No iModulon identified for this regulator

**Solution**: Check available regulators in dataset

### "Download failed"

**Possible reasons**:
1. Network connectivity issues
2. GitHub repository moved
3. File path changed

**Solution**: Check GitHub repo exists, update organism mapping if needed

## Limitations

1. **Bacterial organisms only** - iModulonDB currently focuses on bacteria
2. **Dataset availability** - Only ~20 organisms have published datasets
3. **Gene name matching** - Requires exact match with regulator name
4. **Context-specific regulation** - iModulons average across conditions
5. **Indirect effects** - ICA captures co-expression, not just direct regulation

## Future Enhancements

Planned features (see `IMODULONDB_INTEGRATION_PLAN.md`):

- [ ] Automatic integration with `just fetch-gene`
- [ ] Validation checks during `just validate`
- [ ] Cross-organism comparison tools
- [ ] Interactive visualizations
- [ ] API-based access (when available)
- [ ] Support for condition-specific iModulons
- [ ] Integration with other regulatory databases

## Related Documentation

- [iModulonDB website](https://imodulondb.org/)
- [iModulonDB paper](https://doi.org/10.1093/nar/gkaa810)
- [Integration plan](../IMODULONDB_INTEGRATION_PLAN.md)
- [Example: BenR analysis](../genes/PSEPK/BenR/BenR-imodulondb-comparison.md)

## Citation

If you use iModulonDB data in your work, please cite:

- **iModulonDB**: Sastry AV et al. (2021) iModulonDB: a knowledgebase of microbial transcriptional regulation derived from machine learning. *Nucleic Acids Res* 49:D112-D120.
- **Organism-specific datasets**: See references in organism mapping file

## Questions?

For questions about:
- **This integration**: File an issue on GitHub
- **iModulonDB data**: Contact [iModulonDB team](https://imodulondb.org/)
- **Specific datasets**: See references in organism-specific papers
