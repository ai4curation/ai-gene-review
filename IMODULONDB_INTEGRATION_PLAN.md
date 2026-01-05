# iModulonDB Integration Plan

## Goal
Make iModulonDB consistency analysis reproducible for any bacterial gene across multiple organisms.

## Current State

### What We Did Manually for BenR
1. ✅ Identified organism dataset (P. putida → putidaPRECISE321)
2. ✅ Downloaded supplementary data from GitHub (SBRG/modulome_ppu)
3. ✅ Extracted iModulon metadata from Excel file
4. ✅ Retrieved gene weights from M matrix
5. ✅ Compared with gene review annotations
6. ✅ Generated comparison report

### Challenges
- **Manual download** of 37.7 MB Excel file
- **Organism-specific** GitHub repositories
- **Hard-coded** column indices and sheet names
- **No caching** - re-downloads each time
- **Excel dependency** - requires openpyxl

## Architecture

### Option 1: Lightweight API Wrapper (Recommended)
**Pros**: Fast, minimal dependencies, leverages existing iModulonDB infrastructure
**Cons**: Requires iModulonDB API to be stable

```python
# src/ai_gene_review/external/imodulondb.py

class IModulonDBClient:
    """Client for accessing iModulonDB data via API and cached downloads."""

    def get_available_organisms(self) -> List[OrganismInfo]:
        """List all organisms with iModulon datasets."""

    def get_dataset_info(self, organism: str) -> DatasetInfo:
        """Get metadata for organism's dataset."""

    def get_imodulon(self, organism: str, regulator: str) -> IModulonData:
        """Get specific iModulon by regulator name."""

    def get_gene_imodulons(self, organism: str, gene_id: str) -> List[IModulonData]:
        """Get all iModulons containing a specific gene."""

    def compare_with_review(self, organism: str, gene_id: str,
                           review_file: Path) -> ComparisonReport:
        """Compare iModulon data with gene review."""
```

### Option 2: Local Database Cache
**Pros**: Fast lookups, no API dependency, works offline
**Cons**: Large storage, requires sync mechanism

```python
# Cache structure:
# .cache/imodulondb/
#   organisms.json          # List of available organisms
#   p_putida/
#     dataset_info.json     # Metadata
#     imodulons.parquet     # All iModulons
#     genes.parquet         # Gene-iModulon associations
#     M_matrix.parquet      # Gene weights
```

### Option 3: Hybrid Approach (Best of Both)
**Pros**: Fast + reliable + minimal storage
**Cons**: More complex implementation

- Use API for discovery and metadata
- Cache downloaded data locally
- Fall back to direct GitHub download if API fails

## Implementation Plan

### Phase 1: Core Data Access (Week 1)

#### 1.1 Create iModulonDB Client Module
```bash
touch src/ai_gene_review/external/__init__.py
touch src/ai_gene_review/external/imodulondb.py
touch src/ai_gene_review/external/models.py
```

**Files to create:**
- `models.py`: Pydantic models for iModulonDB data structures
- `imodulondb.py`: Client implementation
- `cache.py`: Local caching layer

#### 1.2 Implement Organism Mapping
Create a mapping file: `src/ai_gene_review/data/imodulondb_organisms.yaml`

```yaml
# Maps taxon IDs to iModulonDB organism codes and datasets
mappings:
  - taxon_id: "NCBITaxon:160488"
    taxon_label: "Pseudomonas putida KT2440"
    imodulondb_code: "p_putida"
    dataset: "precise321"
    github_repo: "SBRG/modulome_ppu"
    reference: "Lim et al. 2022, Metabolic Engineering 72:297-310"

  - taxon_id: "NCBITaxon:511145"
    taxon_label: "Escherichia coli str. K-12 substr. MG1655"
    imodulondb_code: "e_coli"
    dataset: "precise456"
    github_repo: "SBRG/modulome_eco"
    reference: "Sastry et al. 2019, Nature Biotechnology"

  # Add more organisms as datasets become available
```

#### 1.3 Implement Data Fetchers

**Priority 1**: Excel file parser
```python
# src/ai_gene_review/external/imodulondb_parser.py

def parse_supplementary_excel(excel_path: Path) -> IModulonDataset:
    """Parse Excel supplementary data into structured format."""

def extract_imodulon_table(wb: Workbook) -> pd.DataFrame:
    """Extract iModulon metadata table."""

def extract_gene_weights(wb: Workbook, imodulon_name: str) -> pd.DataFrame:
    """Extract gene weights for specific iModulon."""
```

**Priority 2**: GitHub downloader
```python
# src/ai_gene_review/external/github_client.py

def download_supplementary_data(organism: str, cache_dir: Path) -> Path:
    """Download from GitHub, return cached path."""

def get_latest_release_url(repo: str) -> str:
    """Get URL for latest release data."""
```

### Phase 2: Comparison Engine (Week 2)

#### 2.1 Create Comparison Module
```python
# src/ai_gene_review/analysis/imodulon_comparison.py

class IModulonComparator:
    """Compare gene reviews with iModulonDB data."""

    def compare_gene(self, organism: str, gene_id: str,
                    review_file: Path) -> ComparisonResult:
        """Full comparison for single gene."""

    def compare_regulon_overlap(self, review_genes: List[str],
                               imodulon_genes: List[str]) -> OverlapMetrics:
        """Calculate precision/recall/F1."""

    def identify_novel_targets(self, review_genes: List[str],
                              imodulon_genes: List[str]) -> List[str]:
        """Find genes in iModulon but not in review."""

    def generate_report(self, comparison: ComparisonResult) -> str:
        """Generate markdown comparison report."""
```

#### 2.2 Create Report Templates
```python
# src/ai_gene_review/templates/imodulon_report.md.jinja2

# {{ gene_symbol }} iModulonDB Comparison

## Dataset
- **Organism**: {{ organism_name }}
- **Dataset**: {{ dataset_name }}
- **Reference**: {{ reference }}

## {{ regulator }} iModulon Statistics
{{ imodulon_stats_table }}

## Gene Comparison
{{ gene_comparison_table }}

## Consistency Assessment
{{ consistency_summary }}

## Novel Predictions
{{ novel_genes_table }}
```

### Phase 3: CLI Integration (Week 3)

#### 3.1 Add CLI Commands

Update `project.justfile`:
```makefile
# Compare gene review with iModulonDB data
compare-imodulondb organism gene:
    uv run ai-gene-review compare-imodulondb {{organism}} {{gene}}

# Batch comparison for all genes in organism
compare-imodulondb-organism organism:
    uv run ai-gene-review compare-imodulondb-batch {{organism}}

# Update iModulonDB cache
update-imodulondb-cache organism="":
    uv run ai-gene-review update-imodulondb-cache {{organism}}

# List available iModulonDB organisms
list-imodulondb-organisms:
    uv run ai-gene-review list-imodulondb-organisms
```

#### 3.2 Add Python CLI Entry Points
```python
# src/ai_gene_review/cli/imodulondb.py

@app.command()
def compare_imodulondb(
    organism: str,
    gene: str,
    output_dir: Path = Path("."),
    force: bool = False
):
    """Compare gene review with iModulonDB data."""

@app.command()
def list_imodulondb_organisms():
    """List all organisms with iModulonDB datasets."""
```

### Phase 4: Automated Reports (Week 4)

#### 4.1 Add to Gene Review Workflow

Modify `fetch-gene` to optionally fetch iModulonDB data:
```bash
just fetch-gene PSEPK BenR --with-imodulondb
```

This would:
1. Create standard files (uniprot, goa, etc.)
2. Check if organism has iModulonDB dataset
3. Download and cache iModulon data
4. Generate preliminary comparison stub

#### 4.2 Add Validation Check

Update `validate` command to include iModulon consistency:
```bash
just validate PSEPK BenR --check-imodulondb
```

Output:
```
✅ Schema validation passed
✅ PMID references valid
⚠️  iModulonDB: 5/5 review genes found in iModulon
ℹ️  iModulonDB: 8 additional genes in iModulon (novel predictions)
📊 iModulonDB consistency: 95% (HIGH)
```

#### 4.3 Auto-generate Comparison Files

After completing a review, automatically generate:
- `GENE-imodulondb-comparison.md` - Detailed comparison
- `GENE-imodulondb-summary.yaml` - Machine-readable metrics

```yaml
# BenR-imodulondb-summary.yaml
organism: PSEPK
gene_symbol: BenR
dataset: putidaPRECISE321
imodulon_name: BenR
statistics:
  recall: 1.0
  precision: 0.4
  f1_score: 0.57
  review_genes: 5
  imodulon_genes: 13
  overlap: 5
consistency: HIGH
novel_genes:
  - locus_tag: PP_3765
    gene_name: mvaT
    weight: 0.1175
    product: H-NS family protein
```

## File Structure

```
src/ai_gene_review/
  external/
    __init__.py
    imodulondb.py          # Main client
    imodulondb_parser.py   # Excel/data parsing
    github_client.py       # GitHub downloads
    models.py              # Pydantic models
    cache.py               # Caching layer

  analysis/
    __init__.py
    imodulon_comparison.py # Comparison engine

  cli/
    imodulondb.py          # CLI commands

  data/
    imodulondb_organisms.yaml  # Organism mappings

  templates/
    imodulon_report.md.jinja2  # Report template

.cache/
  imodulondb/
    organisms.json
    p_putida/
      supplementary_data.xlsx
      imodulons_parsed.parquet
      genes_parsed.parquet
```

## Data Models

```python
# src/ai_gene_review/external/models.py

from pydantic import BaseModel
from typing import List, Optional

class OrganismInfo(BaseModel):
    """iModulonDB organism information."""
    taxon_id: str
    taxon_label: str
    imodulondb_code: str
    dataset: str
    github_repo: str
    reference: str
    available: bool = True

class IModulonMetadata(BaseModel):
    """Metadata for single iModulon."""
    name: str
    regulator: Optional[str]
    imodulon_size: int
    regulon_size: int
    precision: float
    recall: float
    f1_score: float
    true_positives: int
    pvalue: float
    category: str
    subcategory: str
    function: str

class GeneWeight(BaseModel):
    """Gene weight in iModulon."""
    locus_tag: str
    gene_name: Optional[str]
    weight: float
    product: Optional[str]

class IModulonData(BaseModel):
    """Complete iModulon data."""
    metadata: IModulonMetadata
    genes: List[GeneWeight]
    organism: str
    dataset: str

class ComparisonResult(BaseModel):
    """Result of comparison between review and iModulon."""
    organism: str
    gene_symbol: str
    imodulon_name: str
    review_genes: List[str]
    imodulon_genes: List[str]
    overlap_genes: List[str]
    novel_genes: List[GeneWeight]
    missing_genes: List[str]
    consistency_score: float
    consistency_level: str  # HIGH, MEDIUM, LOW
    metrics: Dict[str, float]
```

## Testing Strategy

### Unit Tests
```python
# tests/test_imodulondb_client.py
def test_organism_mapping_valid()
def test_parse_excel_file()
def test_extract_gene_weights()

# tests/test_imodulon_comparison.py
def test_calculate_overlap_metrics()
def test_identify_novel_genes()
def test_generate_comparison_report()
```

### Integration Tests
```python
# tests/integration/test_benr_comparison.py
def test_benr_comparison_full_pipeline():
    """Test complete BenR comparison matches manual analysis."""
    result = compare_gene("PSEPK", "BenR", review_file)
    assert result.consistency_level == "HIGH"
    assert result.metrics["recall"] == 1.0
    assert result.metrics["precision"] == 0.4
```

### Test Data
```
tests/fixtures/
  imodulondb/
    p_putida_sample.xlsx     # Minimal test Excel file
    expected_benr_comparison.yaml
```

## Dependency Management

Add to `pyproject.toml`:
```toml
dependencies = [
  # ... existing ...
  "openpyxl>=3.1.2",       # Excel parsing
  "pyarrow>=14.0.0",       # Parquet caching
  "jinja2>=3.1.6",         # Report templates (already there)
]
```

## Documentation

### User Guide
```markdown
# docs/imodulondb_integration.md

## Using iModulonDB Integration

### Check Available Organisms
```bash
just list-imodulondb-organisms
```

### Compare Single Gene
```bash
just compare-imodulondb PSEPK BenR
```

### Compare All Genes in Organism
```bash
just compare-imodulondb-organism PSEPK
```

### Interpreting Results
- **Consistency: HIGH** - Review strongly validated (>80% agreement)
- **Consistency: MEDIUM** - Partial validation (50-80% agreement)
- **Consistency: LOW** - Significant discrepancies (<50% agreement)
```

### Developer Guide
```markdown
# docs/dev/adding_imodulondb_organisms.md

## Adding New iModulonDB Organisms

1. Update `src/ai_gene_review/data/imodulondb_organisms.yaml`
2. Add GitHub repo info
3. Test with sample gene
4. Document in changelog
```

## Migration Path

### Step 1: MVP (Minimal Viable Product)
- [ ] Create organism mapping file
- [ ] Implement Excel parser
- [ ] Create comparison function
- [ ] Add CLI command for BenR specifically
- [ ] Verify matches manual analysis

### Step 2: Generalization
- [ ] Support multiple organisms (E. coli, B. subtilis, etc.)
- [ ] Add caching layer
- [ ] Implement GitHub downloader
- [ ] Create comparison reports

### Step 3: Integration
- [ ] Add to fetch-gene workflow
- [ ] Add to validation pipeline
- [ ] Auto-generate comparison files
- [ ] Add to documentation

### Step 4: Scale
- [ ] Batch processing
- [ ] Cross-organism comparisons
- [ ] API fallback mechanisms
- [ ] Performance optimization

## Success Criteria

✅ **Phase 1 Complete When**:
- Can run: `just compare-imodulondb PSEPK BenR`
- Output matches manual analysis (this document)
- Works for at least 3 organisms

✅ **Phase 2 Complete When**:
- Integrated into main workflow
- Cached for performance
- Documented with examples

✅ **Phase 3 Complete When**:
- Used by other researchers
- Validated on 50+ genes
- Published in methods paper

## Timeline

- **Week 1**: Core implementation (MVP)
- **Week 2**: Testing and validation
- **Week 3**: Integration and documentation
- **Week 4**: Polish and examples

**Total**: 4 weeks for production-ready system

## Future Enhancements

### Advanced Features
1. **Cross-organism comparison**: Compare regulatory patterns across species
2. **Time-series analysis**: Track iModulon activity across conditions
3. **Network visualization**: Interactive iModulon networks
4. **Machine learning**: Predict novel regulon members
5. **Integration with other databases**: RegulonDB, KEGG, etc.

### API Extensions
```python
def predict_imodulon_membership(gene_id: str, organism: str) -> float:
    """Predict likelihood of gene being in iModulon."""

def compare_across_organisms(gene_symbol: str, organisms: List[str]) -> CrossOrgComparison:
    """Compare iModulon patterns across organisms."""
```

## Questions to Resolve

1. **Data freshness**: How often to update cached data?
   - Suggestion: Monthly automatic checks for new releases

2. **Missing organisms**: What to do when organism not in iModulonDB?
   - Suggestion: Gracefully skip with informative message

3. **Multiple iModulons**: What if gene appears in multiple iModulons?
   - Suggestion: Report all, highlight strongest association

4. **Versioning**: How to track iModulonDB dataset versions?
   - Suggestion: Store dataset version in cache metadata

5. **Large files**: How to handle 37MB Excel files efficiently?
   - Suggestion: Convert to Parquet on first download, cache compressed

## Related Work

- **iModulonDB**: https://imodulondb.org/
- **ICA in transcriptomics**: Sastry et al. 2019, Nature Biotechnology
- **P. putida dataset**: Lim et al. 2022, Metabolic Engineering

## Contact

For questions about implementation:
- File issue: https://github.com/ai4curation/ai-gene-review/issues
- Discussion: Link to discussions forum
