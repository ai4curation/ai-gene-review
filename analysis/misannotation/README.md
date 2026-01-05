# Misannotation Analysis

This analysis framework identifies potentially misannotated genes based on computational approaches inspired by [PMC8491902](https://pmc.ncbi.nlm.nih.gov/articles/PMC8491902/), which found that 78% of enzyme annotations may be incorrect.

## Approach

We implement two key computational checks:

### 1. Sequence Similarity Analysis (`sequence_similarity_analyzer.py`)
- **Risk Threshold**: <25% sequence identity with characterized proteins = HIGH risk
- **Method**: BLAST against SwissProt (reviewed proteins only)
- **Output**: Risk assessment for each gene based on similarity to known proteins

### 2. Domain Architecture Analysis (`domain_analyzer.py`)
- **Consistency Check**: Protein domains should match functional GO annotations
- **Method**: Compare InterPro domains with expected domains for GO terms
- **Output**: Identifies genes with domain-function mismatches

## Usage

### Quick Analysis (Human genes only)
```bash
just analyze-misannotation-quick human
```

### Full Analysis (All organisms)
```bash
just analyze-misannotation-full
```

### Organism-specific Analysis
```bash
just analyze-misannotation human
just analyze-domains human
```

### Generate Summary Report
```bash
just summarize-misannotation-risk
```

## Output Files

- `analysis/misannotation/sequence_risk.json` - Sequence similarity risk assessment
- `analysis/misannotation/domain_risk.json` - Domain architecture analysis
- `analysis/misannotation/*.tsv` - Tab-separated summary files for easy analysis

## Risk Categories

### HIGH Risk
- <25% sequence identity with characterized proteins
- Missing expected protein domains
- No functional annotations

### MEDIUM Risk
- 25-50% sequence identity with characterized proteins
- Some domain inconsistencies

### LOW Risk
- >50% sequence identity with characterized proteins
- Consistent domain architecture

## Expected Results

Based on PMC8491902, we expect to find:
- ~17-78% of genes with potential annotation issues
- Higher risk rates in less-studied organisms
- Enrichment of misannotations in computationally predicted genes

## Integration with Validation System

High-risk genes identified by this analysis should be:
1. Flagged in validation reports
2. Prioritized for experimental validation
3. Reviewed by domain experts
4. Potentially marked for reannotation

## Dependencies

- `biopython` - For BLAST analysis and sequence handling
- `requests` - For UniProt/InterPro API calls
- Standard Python libraries (json, yaml, etc.)

## Caching

Both analyzers cache results to avoid repeated API calls:
- Protein sequences cached as FASTA files
- BLAST results cached as JSON
- InterPro domain data cached as JSON

Cache location: `analysis/misannotation/cache/`