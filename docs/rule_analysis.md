# ARBA Rule Post-Enrichment Analysis

## Overview

The `rule_analysis` module provides deterministic analysis of UniProt ARBA rules after enrichment. It calculates InterPro domain overlap using Jaccard similarity and detects redundancy with existing InterPro2GO mappings.

## Key Features

- **InterPro Domain Overlap**: Calculate Jaccard similarity, set differences, and containment metrics between InterPro domains
- **Protein Count Queries**: Query UniProt API for SwissProt protein counts using boolean AND queries
- **InterPro2GO Mappings**: Download and cache official GO Consortium InterPro2GO mappings
- **Redundancy Detection**: Identify when rule annotations duplicate existing ipr2go mappings
- **Multiple Output Formats**: Export results as YAML, JSON, or human-readable text
- **Interpretation**: Automatic classification of overlap patterns (SUBSET, REDUNDANT, HIGH_OVERLAP, etc.)

## Quick Start

```python
from pathlib import Path
from ai_gene_review.etl.arba import ARBAClient
from ai_gene_review.etl.rule_analysis import analyze_rule_post_enrichment

# Load an ARBA rule
client = ARBAClient()
rule = client.fetch_rule("ARBA00026249")

# Run full analysis
analysis = analyze_rule_post_enrichment(rule, Path("rules/arba"))

# Check results
print(analysis["ipr2go_redundancy"]["summary"])
print(analysis["condition_sets_analysis"][0]["interpro_overlap"]["summary"])
```

## Command Line Tools

### Sync InterPro2GO Mappings

Download and cache the official InterPro2GO mapping file:

```bash
just sync-ipr2go
```

This downloads ~14,743 InterPro → GO mappings (2.9MB) from http://geneontology.org/external2go/interpro2go

### Demo Script

Run comprehensive analysis on any ARBA rule with flexible output formats:

```bash
# Display analysis report in console
uv run python examples/rule_analysis_demo.py ARBA00026249

# Save as YAML (default format, inferred from extension)
uv run python examples/rule_analysis_demo.py ARBA00026249 --output analysis.yaml

# Save as JSON
uv run python examples/rule_analysis_demo.py ARBA00026249 --output analysis.json

# Save as text report
uv run python examples/rule_analysis_demo.py ARBA00026249 --output report.txt --format text

# Explicitly specify format
uv run python examples/rule_analysis_demo.py ARBA00026249 --output analysis --format yaml
```

## Core Functions

### `fetch_interpro2go_mappings(cache_dir: Path) -> dict[str, list[str]]`

Download and parse InterPro2GO mappings from the GO Consortium.

**Returns:** Dict mapping InterPro IDs to lists of GO IDs

```python
from pathlib import Path
from ai_gene_review.etl.rule_analysis import fetch_interpro2go_mappings

mappings = fetch_interpro2go_mappings(Path("rules/arba"))
# {'IPR005982': ['GO:0004791'], 'IPR008255': ['GO:0016491'], ...}
```

### `get_swissprot_count_for_interpro(interpro_id: str) -> int`

Query UniProt API for count of SwissProt proteins with an InterPro domain.

**Query:** `(xref:interpro-{id}) AND (reviewed:true)`

```python
from ai_gene_review.etl.rule_analysis import get_swissprot_count_for_interpro

count = get_swissprot_count_for_interpro("IPR005982")
# 65
```

### `get_swissprot_count_for_interpro_intersection(interpro_ids: list[str]) -> int`

Query UniProt API for count of proteins matching ALL InterPro domains.

**Query:** `(xref:interpro-{id1}) AND (xref:interpro-{id2}) AND ... AND (reviewed:true)`

```python
from ai_gene_review.etl.rule_analysis import get_swissprot_count_for_interpro_intersection

count = get_swissprot_count_for_interpro_intersection(["IPR005982", "IPR008255"])
# 65
```

### `calculate_jaccard_similarity(interpro_a: str, interpro_b: str) -> float`

Calculate Jaccard similarity coefficient between two InterPro domains.

**Formula:** `Jaccard = |A ∩ B| / (|A| + |B| - |A ∩ B|)`

```python
from ai_gene_review.etl.rule_analysis import calculate_jaccard_similarity

similarity = calculate_jaccard_similarity("IPR005982", "IPR008255")
# 0.774
```

### `analyze_interpro_overlap_in_condition_set(condition_set: ConditionSet) -> dict`

Analyze all pairwise InterPro domain overlaps in a conjunctive condition set.

**Returns:** Dict with pairwise statistics (Jaccard, containment, counts) and summary

```python
from ai_gene_review.etl.arba import ARBAClient
from ai_gene_review.etl.rule_analysis import analyze_interpro_overlap_in_condition_set

client = ARBAClient()
rule = client.fetch_rule("ARBA00026249")
result = analyze_interpro_overlap_in_condition_set(rule.condition_sets[0])

print(result["summary"])
# "Analyzed 3 InterPro pairs. Average Jaccard similarity: 0.315. 1 pairs with >50% overlap."
```

### `analyze_ipr2go_redundancy(interpro_ids: list[str], rule_go_ids: list[str], ipr2go_mappings: dict) -> dict`

Check if rule GO annotations are redundant with existing InterPro2GO mappings.

**Returns:** Dict with redundant_annotations, novel_annotations, and summary

```python
from pathlib import Path
from ai_gene_review.etl.rule_analysis import fetch_interpro2go_mappings, analyze_ipr2go_redundancy

mappings = fetch_interpro2go_mappings(Path("rules/arba"))
result = analyze_ipr2go_redundancy(
    interpro_ids=["IPR005982", "IPR008255"],
    rule_go_ids=["GO:0004791"],
    ipr2go_mappings=mappings
)

print(result["summary"])
# "1 redundant annotation(s) (already in ipr2go). All annotations already in ipr2go."
```

### `analyze_rule_post_enrichment(rule: ARBARule, cache_dir: Path) -> dict`

Main analysis function - runs all 4 steps deterministically.

**Steps:**
1. Fetch SwissProt protein counts for InterPro IDs
2. Get InterPro2GO mappings from cached file
3. Calculate overlap (Jaccard similarity) for InterPro pairs
4. Analyze redundancy with ipr2go mappings

**Returns:** Complete analysis dict

```python
from pathlib import Path
from ai_gene_review.etl.arba import ARBAClient
from ai_gene_review.etl.rule_analysis import analyze_rule_post_enrichment

client = ARBAClient()
rule = client.fetch_rule("ARBA00026249")
analysis = analyze_rule_post_enrichment(rule, Path("rules/arba"))

# Structure:
# {
#   "rule_id": "ARBA00026249",
#   "condition_sets_analysis": [
#     {
#       "condition_set_index": 0,
#       "interpro_overlap": {
#         "pairs": [
#           {
#             "condition_a": "IPR005982",
#             "condition_b": "IPR008255",
#             "protein_database": "SWISSPROT",
#             "count_a": 65,
#             "count_b": 84,
#             "intersection_count": 65,
#             "a_minus_b_count": 0,
#             "b_minus_a_count": 19,
#             "jaccard_similarity": 0.774,
#             "containment_a_in_b": 1.0,
#             "containment_b_in_a": 0.774,
#             "interpretation": "SUBSET"
#           }
#         ],
#         "summary": "..."
#       }
#     }
#   ],
#   "ipr2go_redundancy": {
#     "redundant_annotations": [
#       {"go_id": "GO:0004791", "interpro_source": "IPR005982"}
#     ],
#     "novel_annotations": [],
#     "summary": "..."
#   }
# }
```

### `export_analysis_to_yaml(analysis: dict, output_path: Path) -> None`

Export analysis results to YAML file.

```python
from pathlib import Path
from ai_gene_review.etl.rule_analysis import export_analysis_to_yaml

export_analysis_to_yaml(analysis, Path("analysis.yaml"))
```

### `format_analysis_as_text(analysis: dict) -> str`

Format analysis results as human-readable text report.

```python
from ai_gene_review.etl.rule_analysis import format_analysis_as_text

text_report = format_analysis_as_text(analysis)
print(text_report)
```

## Example: ARBA00026249 Analysis

### Rule Structure

- **Condition Set 0:** IPR005982 AND IPR008255 AND IPR023753
- **Condition Set 1:** CATH.FunFam:3.50.50.60:FF:000064 AND Eukaryota
- **Condition Set 2:** Two FunFams AND Rattus
- **Annotation:** GO:0004791 (thioredoxin-disulfide reductase activity)

### InterPro Overlap Results

```
IPR005982 ↔ IPR008255:
  Jaccard similarity: 0.774 (high overlap)
  Intersection: 65 proteins
  Counts: 65 / 84
  Interpretation: IPR005982 is completely contained in IPR008255

IPR005982 ↔ IPR023753:
  Jaccard similarity: 0.075 (low overlap)
  Intersection: 65 proteins
  Counts: 65 / 869
  Interpretation: IPR023753 is much broader

IPR008255 ↔ IPR023753:
  Jaccard similarity: 0.097 (low overlap)
  Intersection: 84 proteins
  Counts: 84 / 869
  Interpretation: IPR023753 is much broader
```

### Redundancy Analysis

```
Redundant: GO:0004791 already mapped by IPR005982
```

The rule is **redundant** - the official InterPro2GO file already maps IPR005982 → GO:0004791, so this ARBA rule doesn't add novel information.

## Architecture

### API-Based Approach

Instead of downloading all proteins and computing intersections locally, we use the UniProt API's boolean query capability:

```python
# Query for intersection
query = "(xref:interpro-IPR005982) AND (xref:interpro-IPR008255) AND (reviewed:true)"
response = requests.get(UNIPROT_SEARCH_API, params={"query": query, "size": 1})
count = int(response.headers.get("X-Total-Results", 0))
```

**Benefits:**
- Fast: Only HTTP requests for counts
- Scalable: Works for any number of InterPro conditions
- Deterministic: Results are reproducible
- Simple: No local protein database needed

### Caching Strategy

- InterPro2GO file cached at `{cache_dir}/_interpro2go.txt`
- Downloaded once, reused on subsequent calls
- 14,743 InterPro → GO mappings (2.9MB file)
- No expiration - file is relatively stable

## Testing

Run all tests:

```bash
uv run pytest tests/test_rule_analysis.py -v
```

Run only integration tests (requires network):

```bash
uv run pytest tests/test_rule_analysis.py -v -m integration
```

All 13 tests should pass:
- ✓ InterPro2GO download and caching
- ✓ InterPro2GO parsing
- ✓ UniProt API queries (single and intersection)
- ✓ Jaccard similarity calculation
- ✓ InterPro overlap analysis
- ✓ Redundancy detection
- ✓ Edge cases (empty sets, no InterPro conditions)

## Performance

Typical analysis time for ARBA00026249:
- ~26 seconds for full test suite (13 tests)
- ~3 seconds for single rule analysis (3 API calls per pair)
- Dominated by API request delays (0.1s default between calls)

To speed up:
```python
# Reduce delay between API requests (use with caution - avoid rate limiting)
analysis = analyze_rule_post_enrichment(rule, cache_dir, request_delay=0.05)
```

## Future Enhancements

The current implementation provides the core analysis functionality. Potential future additions:

1. **Integration with enrichment workflow:** Add analysis results to `.enriched.json` files
2. **LinkML schema extension:** Add fields for storing analysis in structured format
3. **CLI commands:** Add `ai-gene-review analyze-rule` command
4. **Batch analysis:** Process multiple rules efficiently
5. **Visualization:** Generate plots of InterPro overlap networks
6. **Statistical tests:** Determine if overlap is significant vs random

## References

- [UniProt REST API Documentation](https://www.uniprot.org/help/api_queries)
- [InterPro2GO Mappings](http://geneontology.org/external2go/interpro2go)
- [ARBA Rules Documentation](https://www.uniprot.org/help/arba)
