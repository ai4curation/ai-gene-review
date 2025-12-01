## Add your own just recipes here. This is imported by the main justfile.

all: validate-all test

# Fetch gene data from UniProt and GOA
# Use --alias to specify a custom directory name and file prefix
# Use --force to overwrite existing UniProt and GOA files
# Example: just fetch-gene 9BACT F0JBF1 --alias HgcB
# Example: just fetch-gene human TP53 --force
fetch-gene organism gene *args="":
    #!/usr/bin/env bash
    # Check if gene directory already exists and warn if --force not used
    gene_dir="genes/{{organism}}/{{gene}}"
    if [[ "{{args}}" != *"--force"* ]] && [ -d "$gene_dir" ]; then
        uniprot_file="$gene_dir/{{gene}}-uniprot.txt"
        goa_file="$gene_dir/{{gene}}-goa.tsv"
        if [ -f "$uniprot_file" ] || [ -f "$goa_file" ]; then
            echo "⚠️  Gene data for {{organism}}/{{gene}} already exists."
            echo "   To prevent churn, existing files will not be overwritten unless they differ from remote."
            echo "   Use 'just fetch-gene {{organism}} {{gene}} --force' to force overwrite."
            echo ""
        fi
    fi
    uv run ai-gene-review fetch-gene {{organism}} {{gene}} --output-dir . {{args}}

# Fetch ncRNA gene data from RNAcentral
# Use --alias to specify a custom directory name and file prefix
# Use --force to overwrite existing RNAcentral files
# Example: just fetch-ncrna human SNORD3A
# Example: just fetch-ncrna human XIST --alias lncRNA-XIST
# Example: just fetch-ncrna human U1 --rnacentral-id URS000012345_9606
fetch-ncrna organism gene *args="":
    uv run ai-gene-review fetch-ncrna {{organism}} {{gene}} --output-dir . {{args}}

# Fetch ncRNA gene data from RNAcentral (alias for consistency)
fetch-rna-gene organism gene *args="":
    uv run ai-gene-review fetch-ncrna {{organism}} {{gene}} --output-dir . {{args}}


# Deep research using OpenAI (GPT models)
# Gene symbol automatically looked up from UniProt file if --alias not provided
# Examples:
#   just deep-research-openai human TP53              # gene_symbol=TP53, gene_id=TP53
#   just deep-research-openai ARATH BRI1              # Looks up gene symbol from UniProt
#   just deep-research-openai METEA C5B1I4 --alias mllA  # gene_symbol=mllA, gene_id=C5B1I4
#   just deep-research-openai human CFAP300 --extra-args --param "model=gpt-4o"
deep-research-openai organism gene_id *args="":
    uv run python scripts/deep_research_wrapper.py {{organism}} {{gene_id}} openai {{args}}

# Deep research using Perplexity (sonar models)
# Gene symbol automatically looked up from UniProt file if --alias not provided
# Examples:
#   just deep-research-perplexity human TP53          # gene_symbol=TP53, gene_id=TP53
#   just deep-research-perplexity METEA mxcE          # Looks up gene symbol from UniProt
#   just deep-research-perplexity METEA C5B1I4 --alias mllA  # gene_symbol=mllA, gene_id=C5B1I4
deep-research-perplexity organism gene_id *args="":
    uv run python scripts/deep_research_wrapper.py {{organism}} {{gene_id}} perplexity {{args}}

# Quick Perplexity research with low reasoning effort
# Gene symbol automatically looked up from UniProt file if --alias not provided
# Examples:
#   just deep-research-perplexity-lite human TP53     # Fast research
#   just deep-research-perplexity-lite ARATH BRI1 --alias brassinosteroid-receptor
deep-research-perplexity-lite organism gene_id *args="":
    uv run python scripts/deep_research_wrapper.py {{organism}} {{gene_id}} perplexity-lite {{args}}

# Deep research using Falcon (local models)
# Gene symbol automatically looked up from UniProt file if --alias not provided
# Examples:
#   just deep-research-falcon human TP53
#   just deep-research-falcon METEA C5B1I4 --alias mllA
deep-research-falcon organism gene_id *args="":
    uv run python scripts/deep_research_wrapper.py {{organism}} {{gene_id}} falcon {{args}}

# Deep research using Cyberian
# Gene symbol automatically looked up from UniProt file if --alias not provided
# Examples:
#   just deep-research-cyberian human TP53
#   just deep-research-cyberian METEA C5B1I4 --alias mllA
deep-research-cyberian organism gene_id *args="":
    uv run python scripts/deep_research_wrapper.py {{organism}} {{gene_id}} cyberian {{args}}

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
# Update ontology term cache from current annotations
# Examples:
#   just update-cache            # Update GO cache only (default)
#   just update-cache go         # Update GO cache
#   just update-cache all        # Update all ontology caches
update-cache ontology="go":
    @echo "Updating ontology cache for {{ontology}}..."
    uv run python src/ai_gene_review/tools/build_ontology_cache.py --ontology {{ontology}}

# Fix incorrect ontology term labels in YAML files using cache
# Examples:
#   just fix-labels                          # Fix all files (dry run)
#   just fix-labels --write                  # Fix all files (write changes)
#   just fix-labels genes/human/TP53/TP53-ai-review.yaml --write   # Fix specific file
fix-labels *args="":
    #!/usr/bin/env bash
    if [[ "{{args}}" == *"--write"* ]]; then
        # Remove --write flag and pass to script without --dry-run
        other_args=$(echo "{{args}}" | sed 's/--write//')
        uv run python src/ai_gene_review/tools/fix_labels.py $other_args
    else
        # Default to dry run
        uv run python src/ai_gene_review/tools/fix_labels.py --dry-run {{args}}
    fi

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

# Update status field for a single gene review file
update-status organism gene:
    uv run ai-gene-review update-status genes/{{organism}}/{{gene}}/{{gene}}-ai-review.yaml

# Update status field for all gene reviews (dry run - shows what would be updated)
update-status-all-dry-run:
    uv run ai-gene-review update-status --dry-run

# Update status field for all gene reviews
update-status-all:
    uv run ai-gene-review update-status

# Check status field for all gene reviews and report issues only
check-status:
    uv run ai-gene-review update-status --report-only

# Update status field for a specific organism
update-status-organism organism:
    #!/usr/bin/env bash
    echo "Updating status for all {{organism}} genes..."
    for yaml in genes/{{organism}}/*/*-ai-review.yaml; do
        if [ -f "$yaml" ]; then
            uv run ai-gene-review update-status "$yaml"
        fi
    done

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

# Render a single gene review YAML as HTML (custom renderer)
render organism gene:
    uv run python -m ai_gene_review.render genes/{{organism}}/{{gene}}/{{gene}}-ai-review.yaml

# Render all gene reviews for an organism as HTML
render-organism organism:
    uv run python -m ai_gene_review.render --all genes/{{organism}}

# Render all gene reviews as HTML
render-all:
    uv run python -m ai_gene_review.render --all genes/

# Render a single rule review YAML as HTML
render-rule rule_id cache_dir="rules/arba":
    uv run python -c "from ai_gene_review.etl.rule_analysis import render_rule_review_html; from pathlib import Path; render_rule_review_html('{{rule_id}}', Path('{{cache_dir}}'))"

# Render all rule reviews as HTML (for rules with review YAML files)
render-all-rules cache_dir="rules/arba":
    #!/usr/bin/env bash
    echo "Rendering all rule reviews in {{cache_dir}}..."
    count=0
    for review_yaml in {{cache_dir}}/*/*-review.yaml; do
        if [ -f "$review_yaml" ]; then
            rule_id=$(basename "$review_yaml" | sed 's/-review.yaml$//')
            echo "  Rendering $rule_id..."
            uv run python -c "from ai_gene_review.etl.rule_analysis import render_rule_review_html; from pathlib import Path; render_rule_review_html('$rule_id', Path('{{cache_dir}}'))"
            count=$((count + 1))
        fi
    done
    echo "✓ Rendered $count rule reviews"

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


# Batch fetch genes from a file (basic fetch only)
batch-fetch input_file output_dir=".":
    uv run ai-gene-review batch-fetch {{input_file}} --output-dir {{output_dir}}

# Batch gene pipeline: fetch genes and run deep research
# Providers: openai, perplexity, perplexity-lite, falcon
# Examples:
#   just batch-pipeline genes.txt --providers perplexity
#   just batch-pipeline genes.txt --providers openai perplexity --force
#   just batch-pipeline genes.txt --skip-fetch --providers perplexity
batch-pipeline input_file *args="":
    uv run python scripts/batch_gene_pipeline.py {{input_file}} {{args}}

# Example: Fetch common human genes
fetch-examples:
    uv run ai-gene-review fetch-gene human TP53
    uv run ai-gene-review fetch-gene human BRCA1
    uv run ai-gene-review fetch-gene human EGFR
    uv run ai-gene-review fetch-gene human CFAP300

# Example: Fetch common human ncRNA genes
fetch-ncrna-examples:
    uv run ai-gene-review fetch-ncrna human SNORD3A    # snoRNA
    uv run ai-gene-review fetch-ncrna human XIST       # lncRNA
    uv run ai-gene-review fetch-ncrna human H19        # lncRNA
    uv run ai-gene-review fetch-ncrna human MIR21      # miRNA

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

# Find genes that lack deep research files (GENE-deep-research-PROVIDER.md pattern)
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

            # Check for pattern: GENE-deep-research-PROVIDER.md (includes legacy patterns)
            if ! ls "$gene_dir"*-*research*.md >/dev/null 2>&1; then
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

# ============== InterPro Family Data Management ==============

# Fetch PANTHER family metadata via InterPro API and store in interpro/panther/PTHRnnnn/ directory
# By default includes reviewed protein entries as CSV file
fetch-panther-family family_id *args="":
    @echo "Fetching PANTHER family metadata for {{family_id}} via InterPro API..."
    uv run python src/ai_gene_review/tools/fetch_interpro_family_simple.py panther {{family_id}} --include-proteins {{args}}

# Fetch PANTHER family metadata only (no protein entries CSV)
fetch-panther-family-metadata-only family_id *args="":
    @echo "Fetching PANTHER family metadata only for {{family_id}} via InterPro API..."
    uv run python src/ai_gene_review/tools/fetch_interpro_family_simple.py panther {{family_id}} {{args}}

# Fetch any InterPro family metadata (panther, pfam, etc.) and store in interpro/database/family_id/ directory
# By default only includes metadata (no protein entries) - use --include-proteins to add entries CSV
fetch-interpro-family database family_id *args="":
    @echo "Fetching {{database}} family metadata for {{family_id}} via InterPro API..."
    uv run python src/ai_gene_review/tools/fetch_interpro_family_simple.py {{database}} {{family_id}} {{args}}

# Fetch InterPro family with protein entries CSV
fetch-interpro-family-with-proteins database family_id *args="":
    @echo "Fetching {{database}} family metadata and proteins for {{family_id}} via InterPro API..."
    uv run python src/ai_gene_review/tools/fetch_interpro_family_simple.py {{database}} {{family_id}} --include-proteins {{args}}

# Fetch PANTHER family data for a specific gene (looks up family from gene)
fetch-gene-panther-family organism gene:
    @echo "Fetching PANTHER family data for {{organism}}/{{gene}}..."
    uv run python src/ai_gene_review/tools/fetch_gene_panther_family.py {{organism}} {{gene}}

# ============== iModulonDB Integration ==============

# Compare gene review with iModulonDB data (for bacterial transcription factors)
# Examples:
#   just compare-imodulondb PSEPK BenR
#   just compare-imodulondb ecoli FliA
compare-imodulondb organism gene *args="":
    @echo "Comparing {{organism}}/{{gene}} with iModulonDB..."
    uv run python scripts/compare_with_imodulondb_v2.py {{organism}} {{gene}} {{args}}

# List available organisms in iModulonDB
list-imodulondb-organisms:
    @echo "Available iModulonDB organisms:"
    @uv run python -c "import yaml; data = yaml.safe_load(open('src/ai_gene_review/data/imodulondb_organisms.yaml')); print('\n'.join(f'  - {m[\"taxon_label\"]} ({m[\"imodulondb_code\"]})' for m in data['mappings'] if m['available']))"

# Clean iModulonDB cache
clean-imodulondb-cache:
    @echo "Cleaning iModulonDB cache..."
    rm -rf .cache/imodulondb
    @echo "✓ Cache cleaned"

# ============== UniProt Rules (ARBA, UniRule) ==============

# Sync ARBA rules with GO annotations from UniProt (stores in rules/arba/)
# By default only syncs rules that have GO term annotations
# Examples:
#   just arba-sync                     # Sync GO-annotated rules only (default)
#   just arba-sync --all               # Sync ALL rules (~80k)
#   just arba-sync --limit 10          # Test with small batch
arba-sync *args="":
    uv run ai-gene-review arba-sync {{args}}

# Sync UniRules with GO annotations from UniProt (stores in rules/unirule/)
# By default only syncs rules that have GO term annotations
# Examples:
#   just unirule-sync                  # Sync GO-annotated rules only (default)
#   just unirule-sync --all            # Sync ALL rules (~9.5k)
#   just unirule-sync --limit 10       # Test with small batch
unirule-sync *args="":
    uv run ai-gene-review unirule-sync {{args}}

# Sync all UniProt rules (ARBA + UniRule) with GO annotations
rules-sync:
    @echo "Syncing ARBA rules..."
    uv run ai-gene-review arba-sync
    @echo ""
    @echo "Syncing UniRules..."
    uv run ai-gene-review unirule-sync
    @echo ""
    @echo "✓ All rules synced"

# Enrich cached rules with labels (GO, InterPro, FunFam, taxa)
rules-enrich *args="":
    uv run ai-gene-review rules-enrich {{args}}

# Export rules to CSV (one row per condition set)
rules-export *args="":
    uv run ai-gene-review rules-export {{args}}

# Validate rule review YAML files
# Examples:
#   just rules-validate rules/arba/ARBA00026249/ARBA00026249-review.yaml
#   just rules-validate --all
#   just rules-validate --all -v
rules-validate *args="":
    uv run ai-gene-review rules-validate {{args}}

# Sync rule review YAML files with analysis data (pairwise_overlap sections)
# Examples:
#   just sync-rule-review rules/arba/ARBA00026249/ARBA00026249-review.yaml
#   just sync-rule-review --all --rule-type arba
#   just sync-rule-review --all --dry-run
sync-rule-review *args="":
    uv run ai-gene-review rules-sync {{args}}

# Deep research for rules using Perplexity
# Example: just rules-deep-research-perplexity ARBA00026249
rules-deep-research-perplexity rule_id *args="":
    uv run python scripts/rules_deep_research_wrapper.py {{rule_id}} perplexity {{args}}

# Deep research for rules using Perplexity-lite (faster, cheaper)
# Example: just rules-deep-research-perplexity-lite UR000000070
rules-deep-research-perplexity-lite rule_id *args="":
    uv run python scripts/rules_deep_research_wrapper.py {{rule_id}} perplexity-lite {{args}}

# Deep research for rules using OpenAI
# Example: just rules-deep-research-openai ARBA00026249
rules-deep-research-openai rule_id *args="":
    uv run python scripts/rules_deep_research_wrapper.py {{rule_id}} openai {{args}}

# Deep research for rules using Falcon
# Example: just rules-deep-research-falcon ARBA00026249
rules-deep-research-falcon rule_id *args="":
    uv run python scripts/rules_deep_research_wrapper.py {{rule_id}} falcon {{args}}

# Deep research for rules using Cyberian
# Example: just rules-deep-research-cyberian ARBA00026249
rules-deep-research-cyberian rule_id *args="":
    uv run python scripts/rules_deep_research_wrapper.py {{rule_id}} cyberian {{args}}

# Sync InterPro2GO mappings from GO Consortium
# Downloads official InterPro2GO mapping file and caches it
sync-ipr2go cache_dir="rules/arba":
    @echo "Syncing InterPro2GO mappings to {{cache_dir}}..."
    uv run python -c "from ai_gene_review.etl.rule_analysis import fetch_interpro2go_mappings; from pathlib import Path; mappings = fetch_interpro2go_mappings(Path('{{cache_dir}}')); print(f'✓ Cached {len(mappings)} InterPro → GO mappings')"

# Analyze an ARBA rule for InterPro overlap and ipr2go redundancy
# Outputs YAML, JSON, and text formats
# Example: just analyze-rule ARBA00026249
# Example: just analyze-rule ARBA00026249 --cache-dir rules/arba
analyze-rule rule_id *args="":
    #!/usr/bin/env bash
    set -euo pipefail  # Fail fast on errors, undefined variables, and pipe failures

    cache_dir="rules/arba"
    if [[ "{{args}}" == *"--cache-dir"* ]]; then
        cache_dir=$(echo "{{args}}" | sed -n 's/.*--cache-dir \([^ ]*\).*/\1/p')
    fi

    # Extract rule type from ID
    if [[ "{{rule_id}}" == ARBA* ]]; then
        rule_dir="$cache_dir/{{rule_id}}"
    else
        rule_dir="$cache_dir/{{rule_id}}"
    fi

    mkdir -p "$rule_dir"

    echo "Analyzing {{rule_id}}..."

    # Run analysis once and save all formats (efficient)
    uv run python examples/rule_analysis_demo.py {{rule_id}} \
        --cache-dir "$cache_dir" \
        --output-dir "$rule_dir" \
        --no-report

    echo ""
    echo "✓ Analysis complete. Files created:"
    echo "  - $rule_dir/{{rule_id}}-analysis.yaml"
    echo "  - $rule_dir/{{rule_id}}-analysis.json"
    echo "  - $rule_dir/{{rule_id}}-analysis.txt"
    echo "  - $rule_dir/{{rule_id}}-heatmap.png"
    echo ""
    echo "Text report:"
    echo "----------------------------------------"
    cat "$rule_dir/{{rule_id}}-analysis.txt"

# ============== AI4CUI Dashboard ==============

# Launch the AI4CUI API server (required for V2 dashboard)
ui-api port="5124":
    @echo "Launching AI4CUI API server on port {{port}}..."
    @echo "This provides fast HTTP endpoints for job status queries"
    @echo "Dashboard can connect to http://localhost:{{port}}"
    uv run python -m ai4cui --api-only --api-port {{port}}

# Launch the V2 AI4CUI dashboard (requires API server running)
ui port="5123" api_port="5124":
    @echo "Launching AI4CUI V2 Dashboard on port {{port}}..."
    @echo "Connecting to API server at http://localhost:{{api_port}}"
    @echo "NOTE: Make sure API server is running: just ui-api"
    uv run python -m ai4cui --use-api --port {{port}} --api-port {{api_port}}

# Launch the legacy AI4CUI dashboard (direct file I/O, slower)
ui-legacy port="5123":
    @echo "Launching AI4CUI Legacy Dashboard on port {{port}}..."
    @echo "Using direct file I/O (may be slow for 343+ genes)"
    @echo "For better performance, use 'just ui' with API server"
    uv run python -m ai4cui --legacy --port {{port}}
