# iModulonDB Integration - Current Status

## Issue: E. coli Dataset Format Mismatch

### Problem

When running:
```bash
just compare-imodulondb ecoli FliA
```

**Error**: `❌ iModulonDB data not available for Escherichia coli str. K-12 substr. MG1655`

### Root Cause

Different iModulonDB datasets use different data formats:

| Organism | Format | Repository | Status |
|----------|--------|------------|--------|
| P. putida KT2440 | Excel (`.xlsx`) | [SBRG/modulome_ppu](https://github.com/SBRG/modulome_ppu) | ✅ Working |
| E. coli K-12 | CSV files | [SBRG/precise-db](https://github.com/SBRG/precise-db) | ❌ Not implemented |
| B. subtilis 168 | Unknown | [SBRG/modulome_bsu](https://github.com/SBRG/modulome_bsu) | ❌ Not verified |

### E. coli Data Structure

The E. coli dataset (Sastry et al. 2019) uses separate CSV files instead of a single Excel file:

```
SBRG/precise-db/data/
  imodulon_gene_names.txt      # Gene names per iModulon
  imodulon_gene_bnumbers.txt   # B-numbers per iModulon
  gene_info.csv                # Gene metadata
  TRN.csv                      # Transcriptional regulatory network
  A.csv                        # Activity matrix
  S.csv                        # Source matrix (gene weights)
  metadata.csv                 # Sample metadata
  log_tpm.csv                  # Expression data
```

### Solution Options

#### Option 1: Implement CSV Parser (Recommended)

Add CSV parsing support to handle E. coli format:

```python
# In scripts/compare_with_imodulondb.py

def parse_csv_dataset(data_dir: Path) -> IModulonDataset:
    """Parse E. coli style CSV dataset."""

    # Read iModulon gene lists
    imodulons = parse_imodulon_gene_file(data_dir / "imodulon_gene_names.txt")

    # Read gene weights from S.csv (source matrix)
    gene_weights = pd.read_csv(data_dir / "S.csv", index_col=0)

    # Read TRN to get regulators
    trn = pd.read_csv(data_dir / "TRN.csv")

    return combine_into_imodulon_dataset(imodulons, gene_weights, trn)
```

**Effort**: ~4 hours
**Benefit**: Enables E. coli analysis (largest bacterial dataset)

#### Option 2: Convert CSV to Excel Format

Pre-process E. coli data into the same format as P. putida:

```bash
# One-time conversion
python scripts/convert_csv_to_excel.py \
  --input SBRG/precise-db/data/ \
  --output .cache/imodulondb/e_coli/supplementary_data.xlsx
```

**Effort**: ~2 hours
**Benefit**: Reuses existing Excel parser
**Drawback**: Extra conversion step, less maintainable

#### Option 3: Use iModulonDB API (Future)

Wait for iModulonDB to provide a unified API:

**Effort**: 0 (waiting)
**Benefit**: Unified interface for all organisms
**Drawback**: Timeline unknown

### Recommended Next Steps

1. **Short-term** (this week):
   - Document E. coli limitation
   - Mark as `available: false` in organism mapping ✅ Done
   - Show clear error message ✅ Done

2. **Medium-term** (next 2 weeks):
   - Implement CSV parser (Option 1)
   - Test with E. coli FliA
   - Add 2-3 E. coli examples to documentation

3. **Long-term** (1 month):
   - Standardize format detection
   - Support both Excel and CSV automatically
   - Add pymodulon package integration

### Workaround for Now

For E. coli genes, you can:

1. **Use iModulonDB website directly**: https://imodulondb.org/
   - Search for gene (e.g., FliA)
   - View iModulon membership
   - Download data manually

2. **Use pymodulon Python package**:
```python
import pymodulon as pm

# Load E. coli dataset
ica_data = pm.io.load_json_model("e_coli_precise")

# Get FliA iModulon
flia_im = ica_data.imodulon_table.loc['FliA']
flia_genes = ica_data.M['FliA'].sort_values(ascending=False)

print(flia_genes.head(10))
```

3. **Wait for CSV parser implementation** (coming soon!)

### Implementation Checklist for CSV Support

- [ ] Create `parse_csv_dataset()` function
- [ ] Download E. coli CSV files to cache
- [ ] Parse imodulon_gene_names.txt
- [ ] Parse S.csv for gene weights
- [ ] Parse TRN.csv for regulator mapping
- [ ] Map gene names to b-numbers
- [ ] Test with FliA iModulon
- [ ] Update documentation
- [ ] Add to CI/CD tests

### E. coli iModulon Example (Manual Check)

To verify what we'd get with CSV support, here's what FliA iModulon contains (from iModulonDB website):

**FliA iModulon**:
- **Size**: 39 genes
- **Regulator**: FliA (σ28)
- **Function**: Flagellar biosynthesis
- **Top genes**: flgK, flgL, fliC, fliD, fliS, flgM, fliT

This would be very useful for validating flagellar gene reviews!

## Current Working Organisms

### ✅ Pseudomonas putida KT2440

```bash
just compare-imodulondb PSEPK BenR     # ✅ Works!
just compare-imodulondb PSEPK CatR     # ✅ Should work
just compare-imodulondb PSEPK PcaR     # ✅ Should work
```

**Example regulators in P. putida dataset**:
- BenR (aromatic catabolism)
- CatR (catechol degradation)
- PcaR (protocatechuate degradation)
- TtgR (toluene tolerance)
- DmpR (phenol degradation)
- Many more...

## Summary

**Current status**: ✅ Working for P. putida with Excel format
**E. coli status**: ❌ Blocked by CSV format difference
**Fix timeline**: 1-2 weeks to implement CSV parser
**Workaround**: Use iModulonDB website or pymodulon package

The core infrastructure is solid - we just need to add CSV parsing support to unlock E. coli and potentially other organisms!

## Testing Instructions

### What Works Now

```bash
# This works:
just compare-imodulondb PSEPK BenR

# This fails gracefully with clear message:
just compare-imodulondb ecoli FliA
# Output: ❌ iModulonDB data not available for Escherichia coli str. K-12 substr. MG1655
```

### After CSV Parser Implementation

```bash
# This will work:
just compare-imodulondb ecoli FliA
just compare-imodulondb ecoli FliZ
just compare-imodulondb ecoli CRP
```

## References

- **P. putida dataset**: Lim et al. 2022, *Metabolic Engineering* 72:297-310
- **E. coli dataset**: Sastry et al. 2019, *Nature Communications* 10:5536
- **iModulonDB**: https://imodulondb.org/
- **pymodulon**: https://github.com/SBRG/pymodulon
- **precise-db repo**: https://github.com/SBRG/precise-db
