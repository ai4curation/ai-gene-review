# Rule Review HTML Rendering

## Overview

This feature provides HTML rendering for ARBA/UniRule reviews, similar to the existing gene review HTML rendering. The HTML output combines:

- The rule review YAML (source of truth)
- Quantitative analysis statistics
- Domain overlap heatmap visualization
- Interactive tabbed sections for assessments

## Key Features

### 1. Comprehensive Rule Information

The HTML view displays:
- Rule ID, type, status, and action
- Detailed description and review summary
- Condition sets with domain conditions
- GO annotations
- Pairwise overlap analysis tables

### 2. Visual Statistics Dashboard

Four key metrics displayed in gradient cards:
- **Domain Pairs Analyzed**: Total pairwise comparisons performed
- **Condition Sets**: Number of alternative rule condition sets
- **Subset Relationships**: Count of domain subset relationships found
- **Redundant Annotations**: Number of annotations already in InterPro2GO

### 3. Dual Heatmap Visualization

Domain overlap analysis presented in two complementary formats:

**PNG Heatmap** (embedded as base64):
- Self-contained HTML files (no external PNG dependencies)
- Asymmetric containment matrix
- Domain IDs, labels, and protein counts on axes
- Color-coded overlap intensity
- Condition set grouping with separators
- Portable and shareable as a single file

**Interactive HTML Table Heatmap**:
- Simple, accessible table format
- Clickable cells linking to UniProt intersection queries
- Multiple metrics per cell: containment %, Jaccard similarity %, and intersection count
- Row and column headers hyperlinked to UniProt domain queries
- Condition set annotations on row headers (e.g., "CS: 0, 1")
- Protein counts for each domain
- Color-coded cells based on containment strength:
  - Red (≥90%): High containment
  - Orange (70-89%): Medium-high
  - Yellow (50-69%): Medium
  - Light green (30-49%): Medium-low
  - Green (1-29%): Low containment
  - Gray (0%): No overlap

### 4. Tabbed Assessment Sections

Six assessment categories with color-coded badges:
- **Parsimony**: Evaluation of rule complexity vs value
- **Literature Support**: Strength of scientific evidence
- **Condition Overlap**: Analysis of domain relationships
- **InterPro2GO**: Redundancy with existing manual curation
- **GO Specificity**: Appropriateness of term granularity
- **Taxonomic Scope**: Coverage across species

### 5. Comprehensive Hyperlinking

All identifiers and counts are clickable, linking to external resources:
- **CURIE links**: GO IDs, InterPro domains, CATH FunFam, NCBITaxon, PMIDs link to their respective databases
- **GO annotations**: Link to QuickGO for detailed term information
- **Condition domains**: Link to UniProt queries showing proteins with that domain
- **Count links**: In pairwise overlap tables, counts link to UniProt queries:
  - Condition A/B: Links to proteins with that domain
  - Count A/B: Links to proteins with respective domain
  - Intersection: Links to proteins with BOTH domains (AND query)
- **Heatmap table cells**:
  - Row/column headers: Link to UniProt queries for proteins with that domain
  - Cell contents: Link to UniProt intersection queries (proteins with BOTH domains)
  - All links open in new tabs for easy exploration

### 6. Complete Reference List

All supporting references with:
- Publication IDs (PMIDs, file references)
- Titles and key findings
- Direct supporting text excerpts

## Usage

### Using Just Commands (Recommended)

The easiest way to render rule reviews is using the justfile targets:

```bash
# Render a single rule review
just render-rule ARBA00026249

# Render all rules that have review YAML files
just render-all-rules

# Use a custom cache directory
just render-rule ARBA00026249 rules/unirule
just render-all-rules rules/unirule
```

### Basic Python API

```python
from ai_gene_review.etl.rule_analysis import render_rule_review_html
from pathlib import Path

rule_id = "ARBA00026249"
cache_dir = Path("rules/arba")

html_path = render_rule_review_html(rule_id, cache_dir)
# Generates: rules/arba/ARBA00026249/ARBA00026249-review.html
```

### Complete Workflow

The demo script shows the full analysis-to-HTML pipeline:

```bash
# Analyze rule and render HTML
uv run python examples/render_rule_review_demo.py ARBA00026249

# Just render existing YAML to HTML (skip analysis)
uv run python examples/render_rule_review_demo.py ARBA00026249 --skip-analysis

# Use custom output directory
uv run python examples/render_rule_review_demo.py ARBA00026249 --output-dir /tmp/demo
```

## File Structure

For rule `ARBA00026249`, the following files work together:

```
rules/arba/ARBA00026249/
├── ARBA00026249.json              # Raw rule from UniProt API
├── ARBA00026249.enriched.json     # Rule with added labels
├── ARBA00026249-review.yaml       # Manual review (source of truth)
├── ARBA00026249-analysis.txt      # Quantitative analysis text
├── ARBA00026249-heatmap.png       # Domain overlap visualization
└── ARBA00026249-review.html       # Generated HTML view
```

## Template Design

The Jinja2 template (`rule_review.html.j2`) follows the same design principles as gene reviews:

- Clean, modern CSS with CSS variables for theming
- Responsive layout with flexbox/grid
- Color-coded badges for quick visual scanning
- Embedded JavaScript for tab switching
- Mobile-friendly with proper viewport settings

### Color Scheme

Status badges:
- COMPLETE: Green (#d1fae5)
- IN_PROGRESS: Blue (#dbeafe)
- INITIALIZED: Yellow (#fef3c7)

Action badges:
- ACCEPT: Green (#22c55e)
- REMOVE: Red (#ef4444)
- MODIFY: Orange (#f97316)

Assessment badges:
- APPROPRIATE/STRONG: Green
- MINOR: Blue
- POOR/COMPLETE: Yellow-Red gradient

## Implementation Details

### Function: `render_rule_review_html()`

Located in `src/ai_gene_review/etl/rule_analysis.py`

**Parameters:**
- `rule_id`: ARBA/UniRule identifier
- `cache_dir`: Directory containing rule files
- `output_path`: Optional custom output path
- `template_path`: Optional custom template

**Process:**
1. Loads rule review YAML
2. Calculates statistics from YAML data
3. Checks for heatmap image
4. Renders Jinja2 template
5. Writes HTML to file

**Returns:** Path to generated HTML file

### Statistics Calculation

Stats are derived from the YAML review data:

```python
stats = {
    'condition_sets': len(condition_sets),
    'total_pairs': sum(len(cs.pairwise_overlap) for cs in condition_sets),
    'subset_relationships': count of 'SUBSET' interpretations,
    'redundant_annotations': len(ipr2go_redundancy.redundant_annotations)
}
```

### Heatmap Integration

If `{rule_id}-heatmap.png` exists, it's read and embedded inline as base64:

```python
import base64
with open(heatmap_path, 'rb') as f:
    heatmap_data = base64.b64encode(f.read()).decode('utf-8')
rule_data['heatmap_data'] = f"data:image/png;base64,{heatmap_data}"
```

```html
<img src="data:image/png;base64,iVBORw0KG..." alt="Domain Overlap Heatmap" />
```

This makes the HTML file self-contained with no external dependencies.

## Design Rationale

### Why HTML?

1. **Human-friendly**: Easier to read than YAML for reviewers
2. **Visual**: Heatmap and stats provide quick insights
3. **Shareable**: Can be opened in any browser, no special tools needed
4. **Archival**: Self-contained documentation of the review
5. **Navigable**: Tabs and sections organize complex information

### YAML as Source of Truth

The review YAML remains the canonical source:
- Version controlled
- Machine readable
- Programmatically processable
- Schema validated

The HTML is a **rendered view**, regenerated as needed from the YAML.

### Separation of Concerns

- **Analysis** (`analyze_rule_post_enrichment`): Quantitative data
- **Review** (`{rule_id}-review.yaml`): Qualitative assessment
- **Rendering** (`render_rule_review_html`): Presentation layer

## Comparison to Gene Reviews

### Similarities

- Jinja2 templating
- CSS design patterns
- YAML source of truth
- Embedded visualizations
- Statistics cards
- Reference sections

### Differences

- **Tabbed assessments**: Rules have 6 assessment categories vs genes' annotation tables
- **Condition sets**: Rules show alternative rule definitions
- **Domain overlap**: Pairwise tables instead of annotation history
- **No core functions**: Rules annotate, not synthesize function
- **Heatmap**: Domain overlap matrix vs gene pathway diagrams

## Future Enhancements

Potential improvements:

1. **Interactive heatmap**: Use Plotly for hover details
2. **Comparison view**: Show before/after for rule modifications
3. **Batch rendering**: Generate HTML for all rules at once
4. **Export options**: PDF generation via Playwright
5. **Validation panel**: Show schema validation results
6. **Change log**: Track review evolution over time

## Examples

See the generated HTML for ARBA00026249:
- `rules/arba/ARBA00026249/ARBA00026249-review.html`

This rule demonstrates:
- Complete redundancy with InterPro2GO
- Three condition sets with different approaches
- Subset relationships in domain overlap
- Strong literature support but poor parsimony
- Comprehensive assessment across all categories
