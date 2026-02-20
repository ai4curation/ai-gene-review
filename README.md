
# AI Gene Review

AI-assisted tool for reviewing and curating gene annotations with **community feedback integration**. This project provides a structured workflow for validating existing Gene Ontology (GO) annotations using AI-driven analysis combined with literature research, bioinformatics evidence, and crowdsourced expert feedback.

## Overview

The AI Gene Review tool helps researchers and curators:
- **Review existing GO annotations** using strict, defined criteria
- **Synthesize high-quality annotations** from multiple evidence sources
- **Fetch and organize** gene data from UniProt and GOA databases
- **Validate annotation files** against LinkML schemas
- **Manage references** and supporting literature
- **Collect community feedback** through integrated voting and evaluation systems

## Quick Start

### Installation

1. Install [uv](https://docs.astral.sh/uv/) for dependency management
2. Install [just](https://github.com/casey/just) command runner (version 1.23.0 or later required):
   - See installation instructions at https://github.com/casey/just#installation
   - Verify version: `just --version`
3. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/cmungall/ai-gene-review.git
   cd ai-gene-review
   uv sync --group dev
   ```

### Basic Usage

**Fetch gene data:**
```bash
uv run ai-gene-review fetch-gene human TP53
```

**Validate a gene review file:**
```bash
uv run ai-gene-review validate genes/human/TP53/TP53-ai-review.yaml
```

**Fetch publications for a gene:**
```bash
uv run ai-gene-review fetch-gene-pmids genes/human/TP53/TP53-ai-review.yaml
```

**Generate statistics report:**

The stats command analyzes all gene review files in the `genes/` directory and generates an interactive HTML report with visualizations and metrics.

```bash
just stats                # Generate HTML report at docs/stats_report.html
just stats-open           # Generate and open in browser
```

*Prerequisites:* You need at least one completed gene review file (`*-ai-review.yaml`) in the `genes/` directory. The command will:
1. Export annotations from all review files to `exports/exported_annotations.tsv`
2. Execute the `docs/stats.ipynb` Jupyter notebook to generate visualizations
3. Create `docs/stats_report.html` with the statistics dashboard

## Workflow Overview

1. **Fetch Gene Data**: Download UniProt records and GO annotations
2. **Literature Research**: Gather supporting publications and evidence
3. **Create Review**: Structure annotations using the YAML schema
4. **Validate**: Check against LinkML schema and best practices
5. **Generate HTML**: Render interactive web pages with voting capabilities
6. **Collect Feedback**: Community voting and expert evaluation forms
7. **Iterate**: Refine annotations based on validation results and community input

## Key Features

- 🧬 **Multi-organism support**: Human, mouse, worm, and other model organisms
- 📚 **Literature integration**: Automatic PubMed citation fetching and caching
- ✅ **Schema validation**: LinkML-based validation for consistency
- 🛡️ **Anti-hallucination validation**: ID/label tuple checksums prevent AI fabrication of terms
- 🔄 **Batch processing**: Handle multiple genes efficiently
- 📊 **Structured reviews**: YAML-based gene annotation reviews
- 🔍 **Evidence tracking**: Detailed provenance and supporting text
- 🗳️ **Community voting**: Thumbs up/down feedback on AI decisions
- 📝 **Expert evaluation**: Detailed feedback forms for comprehensive gene review assessment
- 🎨 **Interactive web interface**: Rich HTML rendering with modern UI


## Resources

### Web Applications & Documentation

- **Main Project Site**: [https://ai4curation.io/ai-gene-review](https://ai4curation.io/ai-gene-review) *(coming soon)*
- **Interactive Web App**: [Browse Gene Reviews](https://ai4curation.io/ai-gene-review/app/index.html) - Search and explore gene annotation reviews
- **Statistics Dashboard**: [Summary Statistics](https://ai4curation.io/ai-gene-review/docs/stats_report.html) - Analytics and review metrics
- **Evaluation Form**: [https://go.lbl.gov/gene-eval](https://go.lbl.gov/gene-eval) - Detailed expert feedback form
- **Project Slides**: [Overview Presentation](https://docs.google.com/presentation/d/1xBFIQE0jt7K6kFg4zFzUwLDHtnDWat2ZVDarhcpA3_4/edit?slide=id.p#slide=id.p)

### Documentation Pages

- **Voting System Guide**: Learn how to provide feedback on AI curation decisions
- **Evaluation Form Guide**: Comprehensive guide for detailed gene review evaluation
- **GitHub Issues**: [Report bugs and feature requests](https://github.com/monarch-initiative/ai-gene-review/issues)

## Gene Review Structure

Each gene review follows a structured YAML format containing:

- **Gene metadata**: UniProt ID, gene symbol, taxon information
- **Description**: Comprehensive summary of gene function
- **References**: Literature and bioinformatics sources
- **Existing annotations**: Review of current GO annotations with actions (ACCEPT, MODIFY, REMOVE, etc.)
- **Core functions**: Curated essential gene functions

Example structure:
```yaml
id: Q9BRQ4
gene_symbol: CFAP300
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
description: >-
  CFAP300 is a cilium- and flagellum-specific protein...
existing_annotations:
  - term:
      id: GO:0005515
      label: protein binding
    action: MODIFY
    reason: "While evidence is strong, 'protein binding' is uninformative..."
```

## Example Data

The repository includes example gene reviews for:
- **Human**: BRCA1, CFAP300, RBFOX3, TP53
- **Mouse**: Various examples
- **Worm**: lrx-1

Browse the `genes/` directory to see complete examples.

## Community Feedback System

The AI Gene Review project includes a comprehensive feedback system to improve AI curation through community input:

### 🗳️ Quick Voting System

Every gene review page includes thumbs up/down voting on:
- **Individual annotation decisions** (ACCEPT, REMOVE, MODIFY actions)
- **Gene descriptions** and summaries
- **Core function definitions**
- **Suggested questions** for experts
- **Suggested experiments**
- **Documentation sections** (Deep Research, Notes, Bioinformatics Results)
- **Proposed new GO terms**
- **Pathway visualizations**

**Features:**
- Anonymous voting with session-based tracking
- Instant visual feedback with vote persistence
- Rate limiting to prevent abuse
- Vote data collection via Google Apps Script

### 📝 Detailed Evaluation Form

For comprehensive feedback, use the evaluation form at [https://go.lbl.gov/gene-eval](https://go.lbl.gov/gene-eval):

- **Structured assessment** of annotation quality
- **Pre-filled gene information** when accessed from gene pages
- **Multiple choice and free-text** questions
- **Expert-level feedback** for improving AI curation

**📹 Video Tutorial**: Watch a [step-by-step guide on performing evaluations](https://youtu.be/mr8CJBRV4eE) (YouTube)

### 🎯 Feedback Integration

The feedback system enables:
- **Data-driven improvements** to AI curation algorithms
- **Identification of problematic patterns** in automated annotations
- **Community validation** of AI decisions
- **Prioritization of genes** needing expert attention

### How to Provide Feedback

1. **Quick feedback**: Use 👍/👎 buttons on any gene review page
2. **Detailed feedback**: Click "📝 Provide Detailed Feedback" button or visit the evaluation form directly
3. **Technical feedback**: Submit issues and suggestions via [GitHub Issues](https://github.com/monarch-initiative/ai-gene-review/issues)

## Case Studies

### PedH (Pseudomonas putida KT2440) - Lanthanide-Dependent Alcohol Dehydrogenase

The review of **pedH** revealed several important curation insights:

#### Key Discoveries

1. **Lanthanide vs Calcium Dependency**: PedH was incorrectly annotated with "calcium ion binding" (GO:0005509) when it actually requires lanthanide ions (La³⁺, Ce³⁺, Pr³⁺, Nd³⁺, Sm³⁺) for activity. This highlights the importance of reviewing automated annotations based on sequence similarity.

2. **Cellular Localization Precision**: Bioinformatics analysis confirmed PedH is a **soluble periplasmic enzyme**, not membrane-associated:
   - Signal peptide (aa 1-25) directs export, then is cleaved
   - No transmembrane regions in mature protein
   - Functions throughout periplasmic space, not just at membrane boundaries
   - Led to choosing GO:0042597 (periplasmic space) over GO:0030288 (outer membrane-bounded periplasmic space)

3. **Dual Functional Roles**: PedH serves both as:
   - **Metabolic enzyme**: Oxidizes alcohols in 2-phenylethanol degradation pathway
   - **Regulatory sensor**: Part of lanthanide-sensing system controlling gene expression via PedS2/PedR2 two-component system

4. **Missing GO Terms Identified**: The review revealed gaps in GO:
   - No term for "lanthanide ion binding" (distinct from transition metal binding)
   - No term for "lanthanide-dependent alcohol dehydrogenase activity"

#### Lessons for Curation

- **Verify metal cofactors carefully** - Don't assume calcium when other metals are possible
- **Consider protein mobility** - Soluble vs membrane-associated matters for localization terms
- **Look for regulatory functions** - Enzymes may have sensory/regulatory roles beyond catalysis
- **Use bioinformatics to validate** - Signal peptide and TM predictions can clarify localization

## Anti-Hallucination Validation

The AI Gene Review system implements a robust **anti-hallucination validation mechanism** using **ID/label tuple checksums** to prevent AI systems from fabricating or misusing ontological terms.

### How It Works

Every ontology term in the system requires both an `id` (semantic identifier) and `label` (human-readable name):

```yaml
term:
  id: GO:0005515      # Ontology identifier
  label: protein binding  # Canonical label
```

### Validation Process

The `TermValidator` performs multi-layer validation:

1. **Format Validation**: Ensures IDs follow proper CURIE patterns (`PREFIX:NUMBER`)
2. **Existence Validation**: Verifies terms exist in authoritative ontologies via OAK/OLS APIs
3. **Label Matching**: Cross-references provided labels against canonical ontology labels
4. **Branch Validation**: Ensures GO terms are in correct ontological branches (MF/BP/CC)
5. **Obsolescence Checking**: Flags outdated terms

### Why This Prevents Hallucination

✅ **Dual Verification**: Both ID and label must be correct and consistent
✅ **External Truth Source**: Validates against authoritative ontologies (GO, HP, MONDO, etc.)
✅ **Real-time Checking**: Uses live API calls to catch fabricated terms
✅ **Semantic Consistency**: Ensures terms make sense in their context

### Examples

```yaml
# ❌ This would be caught as invalid
term:
  id: GO:0005515
  label: "DNA binding"  # Wrong label for GO:0005515

# ✅ This passes validation
term:
  id: GO:0005515  
  label: "protein binding"  # Correct canonical label

# ❌ This would be flagged as fabricated
term:
  id: GO:9999999
  label: "made up function"  # Non-existent term
```

### Supported Ontologies

The validator supports 10+ major ontologies:
- **GO**: Gene Ontology (molecular functions, biological processes, cellular components)
- **HP**: Human Phenotype Ontology
- **MONDO**: Mondo Disease Ontology  
- **CL**: Cell Ontology
- **UBERON**: Uberon Anatomy Ontology
- **CHEBI**: Chemical Entities of Biological Interest
- **PR**: Protein Ontology
- **SO**: Sequence Ontology
- **PATO**: Phenotype And Trait Ontology
- **NCBITaxon**: NCBI Taxonomy

This validation system represents a **novel approach to preventing ontological hallucination** in AI curation workflows and could serve as a model for other AI applications working with structured biological knowledge.

## Annotation Rule Review

In addition to reviewing individual gene annotations, the AI Gene Review system supports **systematic review of automated annotation rules** used by UniProt (ARBA and UniRule systems). These rules generate millions of GO annotations across protein databases, making their quality critical for downstream research.

### What are ARBA Rules?

ARBA (Association-Rule-Based Annotator) rules use combinations of:
- **InterPro domains**: Protein family signatures
- **PANTHER families**: Evolutionary classifications
- **CATH FunFams**: Functional families based on structure
- **Taxonomic restrictions**: Organism-specific constraints

When a protein matches all conditions in a rule, it receives the predicted GO annotation.

### Why Review Rules?

Automated rules can produce systematic errors affecting thousands of proteins:
- **Taxonomic over-annotation**: Mammalian functions applied to fungi/plants
- **GO term breadth**: Using vague parent terms instead of specific functions
- **Domain promiscuity**: Structural domains with multiple functional contexts
- **Catabolic/biosynthetic confusion**: Grouping enzymes with opposite activities

### Rule Review Workflow

```bash
# 1. Fetch rule data
just rules-fetch ARBA00089174

# 2. Run deep research (multiple providers)
just rules-deep-research-perplexity ARBA00089174
just rules-deep-research-falcon ARBA00089174

# 3. Create/update review YAML
# Reviews are stored in rules/arba/RULE_ID/RULE_ID-review.yaml

# 4. Validate the review
just rules-validate ARBA00089174

# 5. Validate all reviews
just rules-validate --all
```

### Rule Review Structure

Each rule review evaluates:

| Assessment | Valid Values | Description |
|------------|--------------|-------------|
| **parsimony** | PARSIMONIOUS, ACCEPTABLE, REDUNDANT, OVERLY_COMPLEX | Rule complexity vs necessity |
| **literature_support** | STRONG, MODERATE, WEAK, NONE, CONTRADICTED | Experimental evidence quality |
| **condition_overlap** | NONE, MINOR, SIGNIFICANT, COMPLETE | Redundancy between condition sets |
| **go_specificity** | TOO_BROAD, APPROPRIATE, TOO_NARROW, MISMATCHED | GO term choice appropriateness |
| **taxonomic_scope** | TOO_BROAD, APPROPRIATE, TOO_NARROW, MISSING, UNNECESSARY | Taxonomic restriction accuracy |

### Example Finding: False Positive Detection

When reviewing ARBA00089174 (adaptive thermogenesis), the system identified that S. pombe gene cps1 (a fungal carboxypeptidase) received this annotation despite adaptive thermogenesis being a mammalian-specific physiological process. This revealed the rule's Eukaryota scope was too broad and should be restricted to Mammalia.

### Rule Review Files

```
rules/
  arba/
    ARBA00089174/
      ARBA00089174.enriched.json     # Raw rule data from UniProt
      ARBA00089174-review.yaml        # Comprehensive review
      ARBA00089174-deep-research-perplexity.md   # Literature research
      ARBA00089174-deep-research-falcon.md       # Additional research
```

### Actions for Rules

- **ACCEPT**: Rule produces accurate annotations, no changes needed
- **MODIFY**: Rule has correct biological basis but needs refinement (taxonomic scope, GO term specificity, condition consolidation)
- **REMOVE**: Rule produces more false positives than valid annotations

## Repository Structure

* **[genes/](genes/)** - Gene review data organized by organism
  * `human/`, `mouse/`, `worm/` - Species-specific gene directories
  * Each gene folder contains: YAML review, UniProt data, GO annotations, notes
* **[rules/](rules/)** - Annotation rule reviews
  * `arba/` - ARBA rule reviews organized by rule ID
  * Each rule folder contains: enriched JSON, review YAML, deep research files
* **[docs/](docs/)** - MkDocs-managed documentation
* **[src/ai_gene_review/](src/ai_gene_review/)** - Core Python package
  * `cli.py` - Command-line interface
  * `schema/` - LinkML schema definitions
  * `etl/` - Data extraction and loading modules
* **[tests/](tests/)** - Python tests and example data
* **[publications/](publications/)** - Cached PubMed articles

## Developer Tools

This project uses [just](https://github.com/casey/just/) - a command runner similar to `make` but simpler and more user-friendly. Version 1.23.0 or later is required.

**Available commands:**
```bash
just --list           # Show all available commands
just test             # Run tests, type checking, and linting
just format           # Run code formatting checks
just install          # Install project dependencies
```

**CLI Commands:**
```bash
uv run ai-gene-review --help                    # Show CLI help
uv run ai-gene-review fetch-gene human BRCA1    # Fetch gene data
uv run ai-gene-review validate <yaml-file>      # Validate review file
uv run ai-gene-review batch-fetch <input-file>  # Process multiple genes
```

**HTML Rendering:**
```bash
just render human BRCA1        # Render single gene to HTML
just render-all                # Render all gene reviews to HTML
python -m ai_gene_review.render --all genes/    # Alternative rendering command
```

**Export Commands:**
```bash
just export-annotations-tsv    # Export to TSV format (used by stats)
just export-annotations-json   # Export to JSON format
just export-annotations-jsonl  # Export to JSONL format (one object per line)
just export-annotations-duckdb # Export to DuckDB database with redundancy analysis
```

*Note:* Export commands process all `*-ai-review.yaml` files in the `genes/` directory and create outputs in the `exports/` folder.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines including:
- Code of conduct and best practices
- Understanding LinkML schemas
- Pull request workflow
- Development setup

## Credits

This project uses the template [monarch-project-copier](https://github.com/monarch-initiative/monarch-project-copier)
