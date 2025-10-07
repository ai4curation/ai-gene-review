## Add your own just recipes here. This is imported by the main justfile.

all: validate-all test

# Fetch gene data from UniProt and GOA
# Use --alias to specify a custom directory name and file prefix
# Use --force to overwrite existing UniProt and GOA files
# Example: just fetch-gene 9BACT F0JBF1 --alias HgcB
# Example: just fetch-gene human TP53 --force
fetch-gene organism gene *args="":
    uv run ai-gene-review fetch-gene {{organism}} {{gene}} --output-dir . {{args}}

# Conduct deep research on a gene using OpenAI Deep Research API
# Use --alias to specify a custom directory name and file prefix
# Example: just deep-research human CFAP300
# Example: just deep-research ACEPA A0A1Y0Y121 --alias xdhB
deep-research organism gene_or_uniprot *args="":
    uv run python src/ai_gene_review/tools/deep_research.py {{organism}} {{gene_or_uniprot}} {{args}}

# Conduct deep research on a gene using FutureHouse Falcon API
# Use --alias to specify a custom directory name and file prefix
# Example: just deep-research-falcon human CFAP300
# Example: just deep-research-falcon ACEPA A0A1Y0Y121 --alias xdhB
deep-research-falcon organism gene_or_uniprot *args="":
    uv run python src/ai_gene_review/tools/deep_research_falcon.py {{organism}} {{gene_or_uniprot}} {{args}}

# Fetch a specific PMID
fetch-pmid pmid output_dir="publications":
    uv run ai-gene-review fetch-pmid {{pmid}} --output-dir {{output_dir}}

# Fetch all PMIDs referenced in a gene's review file
fetch-gene-pmids organism gene output_dir="publications":
    uv run ai-gene-review fetch-gene-pmids {{organism}} {{gene}} --output-dir {{output_dir}}

# Fetch PMIDs from a file
fetch-pmids-from-file file output_dir="publications":
    uv run ai-gene-review fetch-pmids-from-file {{file}} --output-dir {{output_dir}}

# Refresh PMID titles in gene review YAML files (replaces TODO placeholders with actual titles)
refresh-pmid-titles organism="" gene="":
    #!/usr/bin/env bash
    if [ -n "{{organism}}" ] && [ -n "{{gene}}" ]; then
        echo "Refreshing PMID titles for {{organism}}/{{gene}}..."
        uv run python src/ai_gene_review/cli/refresh_pmid_titles.py genes/{{organism}}/{{gene}}/{{gene}}-ai-review.yaml
    elif [ -n "{{organism}}" ]; then
        echo "Refreshing PMID titles for all {{organism}} genes..."
        for yaml in genes/{{organism}}/*/*-ai-review.yaml; do
            if [ -f "$yaml" ]; then
                uv run python src/ai_gene_review/cli/refresh_pmid_titles.py "$yaml"
            fi
        done
    else
        echo "Refreshing PMID titles for all genes..."
        uv run python src/ai_gene_review/cli/refresh_pmid_titles.py --all-genes
    fi

# Refresh PMID titles for all genes (alias)
refresh-all-pmid-titles:
    uv run python src/ai_gene_review/cli/refresh_pmid_titles.py --all-genes

# Validate gene review YAML files against LinkML schema (for multiple files or patterns)
validate-files files:
    uv run ai-gene-review validate {{files}}

# Validate a specific gene's review file AND check PMID references (short alias)
validate organism gene:
    @echo "Validating {{organism}}/{{gene}} review file..."
    uv run ai-gene-review validate --verbose genes/{{organism}}/{{gene}}/{{gene}}-ai-review.yaml
    @echo ""
    @echo "Checking PMID references in markdown files..."
    uv run python src/ai_gene_review/tools/validate_pmid_references.py genes/{{organism}}/{{gene}}/

# Validate a specific gene's review file AND check PMID references (long name for clarity)
validate-gene organism gene:
    @echo "Validating {{organism}}/{{gene}} review file..."
    uv run ai-gene-review validate genes/{{organism}}/{{gene}}/{{gene}}-ai-review.yaml
    @echo ""
    @echo "Checking PMID references in markdown files..."
    @uv run python src/ai_gene_review/tools/validate_pmid_references.py genes/{{organism}}/{{gene}}/ || (echo "❌ PMID validation failed" && exit 1)

# Validate with verbose output
validate-gene-verbose organism gene:
    uv run ai-gene-review validate genes/{{organism}}/{{gene}}/{{gene}}-ai-review.yaml --verbose

# Validate all genes for an organism (shows detailed errors by default)
validate-organism organism:
    @mkdir -p reports
    uv run ai-gene-review validate --verbose --tsv-output reports/validation-{{organism}}.tsv "genes/{{organism}}/*/*-ai-review.yaml"

# Validate all gene review files (shows detailed errors by default)
validate-all:
    @echo "Validating all gene review YAML files..."
    @mkdir -p reports
    uv run ai-gene-review validate --verbose --tsv-output reports/validation-all.tsv "genes/*/*/*-ai-review.yaml"
    @echo ""
    @echo "Checking PMID references in all pathway markdown files..."
    @uv run python src/ai_gene_review/tools/validate_pmid_references.py genes/ || (echo "❌ PMID validation failed" && exit 1)

# Validate all gene review files (summary only, no details)
validate-all-summary:
    @mkdir -p reports
    uv run ai-gene-review validate --tsv-output reports/validation-summary.tsv "genes/*/*/*-ai-review.yaml"

# Validate all gene review files (strict mode - warnings become errors)
validate-all-strict:
    @mkdir -p reports
    uv run ai-gene-review validate --verbose --strict --tsv-output reports/validation-strict.tsv "genes/*/*/*-ai-review.yaml"

# Comprehensive validation: YAML schema + PMID references + mermaid syntax
validate-comprehensive:
    @echo "==================== COMPREHENSIVE VALIDATION ===================="
    @echo ""
    @echo "Step 1/3: Validating YAML files against schema..."
    @echo "=================================================================="
    uv run ai-gene-review validate --verbose "genes/*/*/*-ai-review.yaml"
    @echo ""
    @echo "Step 2/3: Checking PMID references in markdown files..."
    @echo "=================================================================="
    uv run python src/ai_gene_review/tools/validate_pmid_references.py genes/
    @echo ""
    @echo "Step 3/3: Validating mermaid diagrams..."
    @echo "=================================================================="
    uv run python src/ai_gene_review/tools/validate_mermaid.py genes/
    @echo ""
    @echo "==================== VALIDATION COMPLETE ===================="

# Seed missing GOA annotations in a gene's review file
seed-goa organism gene:
    uv run ai-gene-review seed-goa genes/{{organism}}/{{gene}}/{{gene}}-ai-review.yaml

# Seed missing GOA annotations for all genes in an organism
seed-goa-organism organism:
    #!/usr/bin/env bash
    echo "Seeding missing GOA annotations for all {{organism}} genes..."
    count=0
    for yaml in genes/{{organism}}/*/*-ai-review.yaml; do
        if [ -f "$yaml" ]; then
            gene=$(basename $(dirname "$yaml"))
            echo "Processing $gene..."
            uv run ai-gene-review seed-goa "$yaml" || echo "  Warning: Failed to seed $gene"
            count=$((count + 1))
        fi
    done
    echo "Processed $count genes in {{organism}}"

# Seed missing GOA annotations for ALL genes (use with caution)
seed-goa-all:
    #!/usr/bin/env bash
    echo "Seeding missing GOA annotations for ALL genes..."
    total=0
    for organism_dir in genes/*/; do
        if [ -d "$organism_dir" ]; then
            organism=$(basename "$organism_dir")
            echo "Processing organism: $organism"
            count=0
            for yaml in "$organism_dir"/*/*-ai-review.yaml; do
                if [ -f "$yaml" ]; then
                    gene=$(basename $(dirname "$yaml"))
                    echo "  Processing $gene..."
                    uv run ai-gene-review seed-goa "$yaml" || echo "    Warning: Failed to seed $gene"
                    count=$((count + 1))
                fi
            done
            echo "  Processed $count genes in $organism"
            total=$((total + count))
        fi
    done
    echo "Total: Processed $total genes across all organisms"

# Validate GOA annotations for a specific gene
validate-goa organism gene:
    uv run ai-gene-review validate-goa genes/{{organism}}/{{gene}}/{{gene}}-ai-review.yaml

# Validate GOA annotations for all genes in an organism
validate-goa-organism organism:
    #!/usr/bin/env bash
    echo "Validating GOA annotations for all {{organism}} genes..."
    failed=0
    passed=0
    for yaml in genes/{{organism}}/*/*-ai-review.yaml; do
        if [ -f "$yaml" ]; then
            gene=$(basename $(dirname "$yaml"))
            if uv run ai-gene-review validate-goa "$yaml" > /dev/null 2>&1; then
                echo "✓ $gene"
                passed=$((passed + 1))
            else
                echo "✗ $gene - missing GOA annotations"
                failed=$((failed + 1))
            fi
        fi
    done
    echo "Summary: $passed passed, $failed failed"
    if [ $failed -gt 0 ]; then
        echo "Run 'just seed-goa-organism {{organism}}' to add missing annotations"
    fi

# Check which genes are missing GOA annotations (dry run)
check-missing-goa organism:
    #!/usr/bin/env bash
    echo "Checking for missing GOA annotations in {{organism}} genes..."
    missing=0
    for yaml in genes/{{organism}}/*/*-ai-review.yaml; do
        if [ -f "$yaml" ]; then
            gene=$(basename $(dirname "$yaml"))
            # Use dry-run to check without modifying
            output=$(uv run ai-gene-review seed-goa "$yaml" --dry-run 2>&1)
            if echo "$output" | grep -q "Would add [1-9]"; then
                count=$(echo "$output" | grep -o "Would add [0-9]*" | grep -o "[0-9]*")
                echo "  $gene: missing $count annotations"
                missing=$((missing + 1))
            fi
        fi
    done
    if [ $missing -eq 0 ]; then
        echo "All genes have complete GOA annotations!"
    else
        echo "Total: $missing genes with missing annotations"
        echo "Run 'just seed-goa-organism {{organism}}' to fix"
    fi

# ============== Rendering ==============

# Render a single gene review YAML as markdown
render organism gene:
    uv run python scripts/render_review.py genes/{{organism}}/{{gene}}/{{gene}}-ai-review.yaml

# Render all gene reviews for an organism as markdown
render-organism organism:
    uv run python scripts/render_review.py --all genes/{{organism}}

# Render all gene reviews as markdown
render-all:
    uv run python scripts/render_review.py --all genes/

# ============== Visualization ==============

# Visualize gene review annotations and actions as SVG
visualize organism gene *args="":
    uv run ai-gene-review visualize genes/{{organism}}/{{gene}}/{{gene}}-ai-review.yaml {{args}}

# Visualize with statistics
visualize-stats organism gene:
    uv run ai-gene-review visualize genes/{{organism}}/{{gene}}/{{gene}}-ai-review.yaml --stats

# Visualize all genes in an organism (creates SVGs for each)
visualize-organism organism:
    #!/usr/bin/env bash
    for yaml in genes/{{organism}}/*/*-ai-review.yaml; do
        if [ -f "$yaml" ]; then
            echo "Visualizing $(basename $yaml)..."
            uv run ai-gene-review visualize "$yaml"
        fi
    done

# Visualize all gene reviews (creates SVGs for each)
visualize-all:
    #!/usr/bin/env bash
    for yaml in genes/*/*/*-ai-review.yaml; do
        if [ -f "$yaml" ]; then
            echo "Visualizing $(basename $yaml)..."
            uv run ai-gene-review visualize "$yaml"
        fi
    done

# Export existing_annotations to CSV format
export-annotations output_file="exports/exported_annotations.csv":
    @mkdir -p exports
    uv run python -c "from ai_gene_review.export import TabularExporter; from pathlib import Path; exporter = TabularExporter(); files = list(Path('genes').glob('**/*-ai-review.yaml')); print(f'Found {len(files)} files'); exporter.export_to_csv(files, '{{output_file}}'); print(f'Exported to {{output_file}}')"

# Export existing_annotations to TSV format  
export-annotations-tsv output_file="exports/exported_annotations.tsv":
    @mkdir -p exports
    uv run python -c "from ai_gene_review.export import TabularExporter; from pathlib import Path; exporter = TabularExporter(); files = list(Path('genes').glob('**/*-ai-review.yaml')); print(f'Found {len(files)} files'); exporter.export_to_tsv(files, '{{output_file}}'); print(f'Exported to {{output_file}}')"

# Export existing_annotations to JSON format (for linkml-browser)
export-annotations-json output_file="exports/exported_annotations.json":
    @mkdir -p exports
    uv run python -c "from ai_gene_review.export import JSONExporter; from pathlib import Path; exporter = JSONExporter(); files = list(Path('genes').glob('**/*-ai-review.yaml')); print(f'Found {len(files)} files'); exporter.export_to_json(files, '{{output_file}}'); print(f'Exported to {{output_file}}')"

# Generate statistics HTML report from annotation data
stats output_file="docs/stats_report.html":
    @echo "📊 Generating statistics report..."
    @just export-annotations-tsv
    @echo "📈 Running statistical analysis notebook..."
    uv run jupyter nbconvert --to html --execute --ExecutePreprocessor.timeout=600 \
        docs/stats.ipynb --output $(basename {{output_file}}) \
        --output-dir $(dirname {{output_file}})
    @echo "✅ Statistics report generated: {{output_file}}"
    @echo "📂 Open with: open {{output_file}}"

# Generate and open statistics report
stats-open: stats
    @open docs/stats_report.html

# Export annotations for a specific organism
export-organism-annotations organism output_file="exports/exported_annotations.csv":
    @mkdir -p exports
    uv run python -c "from ai_gene_review.export import TabularExporter; from pathlib import Path; exporter = TabularExporter(); files = list(Path('genes/{{organism}}').glob('**/*-ai-review.yaml')); print(f'Found {len(files)} files for {{organism}}'); exporter.export_to_csv(files, '{{output_file}}'); print(f'Exported to {{output_file}}')"


# Batch fetch genes from a file
batch-fetch input_file output_dir=".":
    uv run ai-gene-review batch-fetch {{input_file}} --output-dir {{output_dir}}

# Example: Fetch common human genes
fetch-examples:
    uv run ai-gene-review fetch-gene human TP53
    uv run ai-gene-review fetch-gene human BRCA1
    uv run ai-gene-review fetch-gene human EGFR
    uv run ai-gene-review fetch-gene human CFAP300

# Build static site from gene markdown files
build-site:
    uv run build-site

# Build and serve the site
build-and-serve: build-site
    uv run mkdocs serve

# Generate project artifacts from LinkML schema
gen-project:
    uv run gen-project src/ai_gene_review/schema/gene_review.yaml -d assets

pydantic:
    uv run gen-pydantic src/ai_gene_review/schema/gene_review.yaml > src/ai_gene_review/datamodel/gene_review_model.py.tmp && mv src/ai_gene_review/datamodel/gene_review_model.py.tmp src/ai_gene_review/datamodel/gene_review_model.py

gen-all: gen-project pydantic

# Deploy linkml-browser app for viewing exported annotations
deploy-browser: export-annotations-json
    @echo "Deploying linkml-browser to app/ directory..."
    @rm -rf app
    uv run linkml-browser deploy \
        exports/exported_annotations.json \
        app \
        --schema src/ai_gene_review/schema/display_schema.json \
        --title "Gene Annotation Review Browser" \
        --description "Browse and filter gene annotation reviews" \
        --force
    @cp src/ai_gene_review/browser/index.html app/
    @echo "Browser deployed to app/ directory"
    @echo "To view: open app/index.html or run 'just serve-browser'"

# Serve the linkml-browser app locally  
serve-browser:
    @echo "Starting local server for linkml-browser..."
    @cd app && python3 -m http.server 8080

# Update browser data without regenerating HTML
update-browser-data: export-annotations-json
    @echo "Updating browser data..."
    uv run linkml-browser deploy \
        exports/exported_annotations.json \
        app \
        --schema src/ai_gene_review/schema/display_schema.json \
        --title "Gene Annotation Review Browser" \
        --description "Browse and filter gene annotation reviews" \
        --force
    @cp src/ai_gene_review/browser/index.html app/
    @echo "Data updated in app/"

# ============== Markdown and Documentation Tools ==============

# Validate mermaid diagrams in a markdown file or directory
validate-mermaid path="genes/":
    @echo "Validating mermaid diagrams in {{path}}..."
    uv run python src/ai_gene_review/tools/validate_mermaid_mmdc.py {{path}}

# Convert markdown file with mermaid to HTML
convert-to-html md_file:
    @echo "Converting {{md_file}} to HTML..."
    uv run python src/ai_gene_review/tools/markdown_to_html.py {{md_file}}

# Convert gene pathway markdown to HTML
gene-pathway-html organism gene:
    @echo "Converting {{organism}}/{{gene}} pathway to HTML..."
    uv run python src/ai_gene_review/tools/markdown_to_html.py \
        genes/{{organism}}/{{gene}}/{{gene}}-pathway.md \
        genes/{{organism}}/{{gene}}/{{gene}}-pathway.html

# Validate all mermaid diagrams in gene files
validate-all-mermaid:
    @echo "Validating all mermaid diagrams in gene files..."
    uv run python src/ai_gene_review/tools/validate_mermaid.py genes/

# Validate PMID references in markdown against review YAML
validate-pmids path:
    @echo "Validating PMID references in {{path}}..."
    uv run python src/ai_gene_review/tools/validate_pmid_references.py {{path}}

# Validate all PMID references in gene markdown files
validate-all-pmids:
    @echo "Validating all PMID references in gene files..."
    uv run python src/ai_gene_review/tools/validate_pmid_references.py genes/

# Validate PMIDs for a specific gene
validate-gene-pmids organism gene:
    @echo "Validating PMID references for {{organism}}/{{gene}}..."
    uv run python src/ai_gene_review/tools/validate_pmid_references.py genes/{{organism}}/{{gene}}/

# ============== Misannotation Analysis ==============
# For misannotation analysis, use: cd analysis/misannotation && just help

# Convert all pathway markdown files to HTML
convert-all-pathways:
    #!/usr/bin/env bash
    count=0
    for pathway in $(find genes -name "*-pathway.md" -type f); do
        echo "Converting $pathway..."
        uv run python src/ai_gene_review/tools/markdown_to_html.py "$pathway"
        count=$((count + 1))
    done
    echo "All $count pathway files converted!"

# Find genes that lack deep research files (GENE-deep-research.md or GENE-falcon-research.md)
find-genes-missing-research:
    #!/usr/bin/env bash
    echo "Finding gene directories missing deep research files..."
    missing_count=0
    total_count=0
    for gene_dir in genes/*/*/; do
        if [ -d "$gene_dir" ]; then
            gene=$(basename "$gene_dir")
            org=$(basename $(dirname "$gene_dir"))
            total_count=$((total_count + 1))

            # Check for either pattern: GENE-deep-research.md or GENE-falcon-research.md
            if ! ls "$gene_dir"*-*research.md >/dev/null 2>&1; then
                echo "$org/$gene"
                missing_count=$((missing_count + 1))
            fi
        fi
    done
    echo ""
    echo "Summary: $missing_count of $total_count genes lack deep research files"

# ============== Publications Cache Management ==============

# Refresh publications cache for PMC articles with missing full text (small batch)
refresh-publications count="50":
    @echo "Refreshing publications cache ({{count}} articles)..."
    uv run ai-gene-review refresh-publications --count {{count}} --delay 1.0

# Refresh all publications cache for PMC articles with missing full text
refresh-publications-all:
    @echo "Refreshing ALL publications with missing full text..."
    @echo "This may take several hours. Use Ctrl+C to cancel."
    @sleep 3
    uv run ai-gene-review refresh-publications --delay 0.8

# Check status of publications cache (how many need refresh)
check-publications-cache:
    @echo "Checking publications cache status..."
    uv run ai-gene-review refresh-publications --summary

# Show sample of publications that need refresh
show-refresh-candidates count="10":
    @echo "Sample of publications needing full text refresh:"
    uv run ai-gene-review refresh-publications --show-candidates {{count}}

# Force refresh ALL publications with updated metadata (use with caution)
refresh-publications-force-all count="20000":
    @echo "Force refreshing ALL publications with updated metadata..."
    @echo "This will refresh {{count}} publications (or all if less exist)"
    @echo "Estimated time: ~12 minutes per 700 publications"
    @echo "Press Ctrl+C to cancel, starting in 3 seconds..."
    @sleep 3
    uv run ai-gene-review refresh-publications --force-all --count {{count}} --delay 1.0

# Force refresh a smaller batch of ALL publications for testing
refresh-publications-force-test count="10":
    @echo "Force refreshing {{count}} publications for testing..."
    uv run ai-gene-review refresh-publications --force-all --count {{count}} --delay 1.0