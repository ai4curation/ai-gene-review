"""CLI interface for ai-gene-review."""

from pathlib import Path
from typing import List, Optional

import typer
from typing_extensions import Annotated

from ai_gene_review.etl.gene import fetch_gene_data, expand_organism_name
from ai_gene_review.etl.publication import (
    cache_publications,
    extract_pmids_from_yaml,
)
from ai_gene_review.validation import validate_gene_review, validate_multiple_files, ValidationSeverity
from ai_gene_review.validation.goa_validator import GOAValidator

app = typer.Typer(help="ai-gene-review: Gene data ETL and review tool.")


@app.command()
def fetch_gene(
    organism: Annotated[str, typer.Argument(help="Organism name (e.g., human, mouse, yeast)")],
    gene: Annotated[str, typer.Argument(help="Gene symbol (e.g., CFAP300, TP53, BRCA1)")],
    uniprot_id: Annotated[Optional[str], typer.Option("--uniprot-id", "-u", help="UniProt accession ID (optional, will be resolved if not provided)")] = None,
    output_dir: Annotated[Optional[Path], typer.Option("--output-dir", "-o", help="Output directory (default: current directory)")] = None,
    no_seed: Annotated[bool, typer.Option("--no-seed", help="Skip seeding ai-review.yaml with GOA annotations")] = False,
    fetch_titles: Annotated[bool, typer.Option("--fetch-titles/--no-fetch-titles", help="Fetch actual titles from PubMed when seeding (default: True)")] = True,
):
    """Fetch gene data from UniProt and GOA databases.
    
    Creates a directory structure:
    genes/<organism>/<gene>/
        <gene>-uniprot.txt
        <gene>-goa.tsv
        <gene>-ai-review.yaml (seeded with GOA annotations and reference titles)
    
    By default, fetches titles from PubMed and GO_REF sources to avoid validation errors.
    Use --no-fetch-titles to skip title fetching for faster execution.
    """
    try:
        typer.echo(f"Fetching data for {gene} ({organism})...")
        
        result = fetch_gene_data(
            gene_info=(organism, gene),
            uniprot_id=uniprot_id,
            base_path=output_dir,
            seed_annotations=not no_seed,
            fetch_titles=fetch_titles
        )
        
        # Show where files were created
        base_path = output_dir or Path.cwd()
        gene_dir = base_path / "genes" / organism / gene
        
        typer.echo("✓ Successfully fetched gene data!")
        typer.echo(f"Files created in: {gene_dir}")
        typer.echo(f"  - {gene}-uniprot.txt")
        typer.echo(f"  - {gene}-goa.tsv")
        
        # Display appropriate message for ai-review.yaml
        if not no_seed:
            if result['yaml_created']:
                typer.echo(f"  - {gene}-ai-review.yaml (created with {result['annotations_added']} GOA annotations)")
            elif result['yaml_existed']:
                if result['annotations_added'] > 0 or result.get('references_added', 0) > 0:
                    parts = []
                    if result['annotations_added'] > 0:
                        parts.append(f"{result['annotations_added']} annotations")
                    if result.get('references_added', 0) > 0:
                        parts.append(f"{result.get('references_added', 0)} references")
                    typer.echo(f"  - {gene}-ai-review.yaml (added {' and '.join(parts)})")
                else:
                    typer.echo(f"  - {gene}-ai-review.yaml (unmodified)")
        
    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def batch_fetch(
    input_file: Annotated[Path, typer.Argument(help="File containing organism,gene pairs (one per line)")],
    output_dir: Annotated[Optional[Path], typer.Option("--output-dir", "-o", help="Output directory (default: current directory)")] = None,
):
    """Fetch gene data for multiple genes from a file.
    
    Input file format (CSV or TSV):
    human,CFAP300
    human,TP53
    mouse,Trp53
    
    Or with UniProt IDs:
    human,CFAP300,Q9BRQ4
    human,TP53,P04637
    """
    if not input_file.exists():
        typer.echo(f"Error: Input file {input_file} not found", err=True)
        raise typer.Exit(code=1)
    
    lines = input_file.read_text().strip().split('\n')
    
    success_count = 0
    error_count = 0
    
    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        parts = [p.strip() for p in line.replace('\t', ',').split(',')]
        
        if len(parts) < 2:
            typer.echo(f"Line {line_num}: Invalid format, skipping: {line}", err=True)
            error_count += 1
            continue
        
        organism = parts[0]
        gene = parts[1]
        uniprot_id = parts[2] if len(parts) > 2 else None
        
        try:
            typer.echo(f"[{line_num}] Fetching {gene} ({organism})...")
            fetch_gene_data(
                gene_info=(organism, gene),
                uniprot_id=uniprot_id,
                base_path=output_dir
            )
            success_count += 1
            typer.echo("  ✓ Success")
        except Exception as e:
            typer.echo(f"  ✗ Failed: {e}", err=True)
            error_count += 1
    
    typer.echo(f"\nCompleted: {success_count} successful, {error_count} failed")
    
    if error_count > 0:
        raise typer.Exit(code=1)


@app.command()
def validate(
    yaml_files: Annotated[list[Path], typer.Argument(help="YAML file(s) to validate")],
    schema: Annotated[Optional[Path], typer.Option("--schema", "-s", help="Path to LinkML schema (uses default if not provided)")] = None,
    verbose: Annotated[bool, typer.Option("--verbose", "-v", help="Show detailed messages including warnings")] = False,
    strict: Annotated[bool, typer.Option("--strict", help="Treat warnings as errors")] = False,
    no_best_practices: Annotated[bool, typer.Option("--no-best-practices", help="Skip best practices checks")] = False,
    no_goa: Annotated[bool, typer.Option("--no-goa", help="Skip GOA validation")] = False,
):
    """Validate gene review YAML files against the LinkML schema.
    
    Examples:
        ai-gene-review validate genes/human/CFAP300/CFAP300-ai-review.yaml
        ai-gene-review validate genes/human/*/*.yaml
        ai-gene-review validate test.yaml --schema custom_schema.yaml --verbose
        ai-gene-review validate test.yaml --strict  # Fail on warnings too
    """
    # Handle glob patterns
    all_files = []
    for pattern in yaml_files:
        if "*" in str(pattern):
            # It's a glob pattern
            from glob import glob
            matched = glob(str(pattern), recursive=True)
            all_files.extend([Path(f) for f in matched if f.endswith('.yaml') or f.endswith('.yml')])
        else:
            all_files.append(pattern)
    
    if not all_files:
        typer.echo("No files found to validate", err=True)
        raise typer.Exit(code=1)
    
    check_best_practices = not no_best_practices
    check_goa = not no_goa
    
    # Validate single file or multiple files
    if len(all_files) == 1:
        yaml_file = all_files[0]
        typer.echo(f"Validating {yaml_file}...")
        
        report = validate_gene_review(yaml_file, schema, check_best_practices, check_goa)
        
        # Determine status symbol and color
        if report.is_valid and not (strict and report.has_warnings):
            status = "✓ Valid"
            if report.has_warnings:
                status += f" (with {report.warning_count} warnings)"
            typer.echo(status)
        else:
            typer.echo("✗ Invalid" if report.has_errors else "⚠ Warnings found", err=True)
        
        # Show issues based on verbosity
        if report.issues:
            if verbose:
                # Show all issues
                for issue in report.issues:
                    _print_issue(issue)
            else:
                # Show only errors and first few warnings
                errors_shown = 0
                warnings_shown = 0
                
                for issue in report.issues:
                    if issue.severity == ValidationSeverity.ERROR:
                        _print_issue(issue)
                        errors_shown += 1
                    elif issue.severity == ValidationSeverity.WARNING and warnings_shown < 3:
                        _print_issue(issue)
                        warnings_shown += 1
                
                remaining_warnings = report.warning_count - warnings_shown
                if remaining_warnings > 0:
                    typer.echo(f"  ... and {remaining_warnings} more warnings (use --verbose to see all)", err=True)
        
        # Exit code based on validation result and strict mode
        if not report.is_valid or (strict and report.has_warnings):
            raise typer.Exit(code=1)
            
    else:
        # Multiple files
        typer.echo(f"Validating {len(all_files)} files...")
        
        # Cast to List[Path | str] for type compatibility
        files_to_validate: list[Path | str] = [f for f in all_files]
        batch_report = validate_multiple_files(files_to_validate, schema, check_best_practices, check_goa)
        
        # Show summary
        typer.echo(batch_report.summary())
        
        # Show details for invalid files if verbose
        if verbose and batch_report.invalid_files > 0:
            typer.echo("\nDetailed issues:")
            for report in batch_report.get_invalid_reports():
                if report.file_path:
                    typer.echo(f"\n{report.file_path}:")
                    for issue in report.issues:
                        _print_issue(issue, indent="  ")
        
        # Exit with error if any files are invalid (or have warnings in strict mode)
        if batch_report.invalid_files > 0:
            raise typer.Exit(code=1)
        elif strict and batch_report.files_with_warnings > 0:
            typer.echo("Failing due to warnings (--strict mode)", err=True)
            raise typer.Exit(code=1)


def _print_issue(issue, indent="  "):
    """Helper to print a validation issue with appropriate formatting."""
    symbol = {
        ValidationSeverity.ERROR: "✗",
        ValidationSeverity.WARNING: "⚠",
        ValidationSeverity.INFO: "ℹ"
    }.get(issue.severity, "•")
    
    err = issue.severity in [ValidationSeverity.ERROR, ValidationSeverity.WARNING]
    typer.echo(f"{indent}{symbol} {issue}", err=err)


@app.command()
def fetch_pmid(
    pmids: Annotated[list[str], typer.Argument(help="PMID(s) to fetch (e.g., PMID:12345 or 12345)")],
    output_dir: Annotated[Optional[Path], typer.Option("--output-dir", "-o", help="Output directory for cached publications")] = None,
    force: Annotated[bool, typer.Option("--force", "-f", help="Force re-download even if cached")] = False,
    delay: Annotated[float, typer.Option("--delay", "-d", help="Delay between requests in seconds")] = 0.5,
):
    """Fetch and cache PubMed/PMC publications.
    
    Examples:
        ai-gene-review fetch-pmid PMID:29727692
        ai-gene-review fetch-pmid 29727692 29727693
        ai-gene-review fetch-pmid PMID:12345 --output-dir ./publications
    """
    output_dir = output_dir or Path("publications")
    
    typer.echo(f"Fetching {len(pmids)} publication(s)...")
    success_count = cache_publications(pmids, output_dir, force, delay)
    
    if success_count == len(pmids):
        typer.echo(f"✓ Successfully cached all {success_count} publications")
    else:
        typer.echo(f"⚠ Cached {success_count}/{len(pmids)} publications", err=True)
        if success_count < len(pmids):
            raise typer.Exit(code=1)


@app.command()
def fetch_pmids_from_file(
    input_file: Annotated[Path, typer.Argument(help="File containing PMIDs (one per line)")],
    output_dir: Annotated[Optional[Path], typer.Option("--output-dir", "-o", help="Output directory")] = None,
    force: Annotated[bool, typer.Option("--force", "-f", help="Force re-download even if cached")] = False,
    delay: Annotated[float, typer.Option("--delay", "-d", help="Delay between requests")] = 0.5,
):
    """Fetch publications from a file of PMIDs.
    
    File format:
    PMID:12345
    29727692
    # Comments are ignored
    """
    if not input_file.exists():
        typer.echo(f"Error: Input file {input_file} not found", err=True)
        raise typer.Exit(code=1)
    
    output_dir = output_dir or Path("publications")
    
    # Read PMIDs from file
    pmids = []
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                pmids.append(line)
    
    if not pmids:
        typer.echo("No PMIDs found in file", err=True)
        raise typer.Exit(code=1)
    
    typer.echo(f"Found {len(pmids)} PMIDs to fetch")
    
    success_count = cache_publications(pmids, output_dir, force, delay)
    
    if success_count == len(pmids):
        typer.echo(f"✓ Successfully cached all {success_count} publications")
    else:
        typer.echo(f"⚠ Cached {success_count}/{len(pmids)} publications", err=True)
        raise typer.Exit(code=1)


@app.command()
def validate_goa(
    yaml_file: Annotated[Path, typer.Argument(help="Gene review YAML file to validate")],
    goa_file: Annotated[Optional[Path], typer.Option("--goa", "-g", help="GOA TSV file (auto-detected if not provided)")] = None,
    strict: Annotated[bool, typer.Option("--strict", help="Fail on evidence type mismatches")] = False,
    verbose: Annotated[bool, typer.Option("--verbose", "-v", help="Show detailed validation results")] = False,
    show_all: Annotated[bool, typer.Option("--show-all", help="Show all mismatches, not just first few")] = False,
):
    """Validate that existing_annotations match the GOA source file.
    
    This command checks that the annotations in the YAML file match what's
    in the GOA (Gene Ontology Annotation) source file.
    
    Examples:
        ai-gene-review validate-goa genes/human/CFAP300/CFAP300-ai-review.yaml
        ai-gene-review validate-goa genes/human/RBFOX3/RBFOX3-ai-review.yaml --verbose
        ai-gene-review validate-goa test.yaml --goa custom-goa.tsv --strict
    """
    yaml_file = Path(yaml_file)
    
    if not yaml_file.exists():
        typer.echo(f"Error: YAML file not found: {yaml_file}", err=True)
        raise typer.Exit(code=1)
    
    # Initialize validator
    validator = GOAValidator()
    validator.strict_mode = strict
    
    # Validate against GOA
    typer.echo(f"Validating {yaml_file.name} against GOA file...")
    result = validator.validate_against_goa(yaml_file, goa_file)
    
    # Show summary
    summary = validator.get_summary(result)
    
    if result.is_valid:
        typer.echo(summary)
    else:
        typer.echo(summary, err=True)
    
    # Show detailed results if verbose or show_all
    if (verbose or show_all) and not result.is_valid:
        typer.echo("\nDetailed validation results:")
        
        if result.missing_in_yaml:
            typer.echo(f"\n{len(result.missing_in_yaml)} annotations in GOA but not in YAML:")
            limit = None if show_all else 10  # Show all or just first 10
            for i, ann in enumerate(result.missing_in_yaml[:limit] if limit else result.missing_in_yaml):
                typer.echo(f"  {i+1}. {ann.go_id} ({ann.go_term}) - {ann.evidence_code} - {ann.reference}")
            if limit and len(result.missing_in_yaml) > limit:
                typer.echo(f"  ... and {len(result.missing_in_yaml) - limit} more (use --show-all to see all)")
        
        if result.missing_in_goa:
            typer.echo(f"\n{len(result.missing_in_goa)} annotations in YAML but not in GOA:")
            limit = None if show_all else 10  # Show all or just first 10
            for i, yaml_ann in enumerate(result.missing_in_goa[:limit] if limit else result.missing_in_goa):
                go_id = yaml_ann.get('term', {}).get('id', 'unknown')
                label = yaml_ann.get('term', {}).get('label', 'unknown')
                evidence = yaml_ann.get('evidence_type', 'unknown')
                ref = yaml_ann.get('original_reference_id', 'unknown')
                typer.echo(f"  {i+1}. {go_id} ({label}) - {evidence} - {ref}")
            if limit and len(result.missing_in_goa) > limit:
                typer.echo(f"  ... and {len(result.missing_in_goa) - limit} more (use --show-all to see all)")
        
        if result.mismatched_labels:
            typer.echo(f"\n{len(result.mismatched_labels)} label mismatches:")
            for go_id, yaml_label, goa_label in result.mismatched_labels:
                typer.echo(f"  - {go_id}:")
                typer.echo(f"    YAML: '{yaml_label}'")
                typer.echo(f"    GOA:  '{goa_label}'")
        
        if result.mismatched_evidence:
            typer.echo(f"\n{len(result.mismatched_evidence)} evidence type mismatches:")
            for go_id, yaml_ev, goa_ev in result.mismatched_evidence:
                typer.echo(f"  - {go_id}:")
                typer.echo(f"    YAML: '{yaml_ev}'")
                typer.echo(f"    GOA:  '{goa_ev}'")
    
    # Exit with error if validation failed
    if not result.is_valid:
        raise typer.Exit(code=1)


@app.command()
def seed_goa(
    yaml_file: Annotated[Path, typer.Argument(help="Gene review YAML file to update")],
    goa_file: Annotated[Optional[Path], typer.Option("--goa", "-g", help="GOA TSV file (auto-detected if not provided)")] = None,
    output: Annotated[Optional[Path], typer.Option("--output", "-o", help="Output file (overwrites input if not specified)")] = None,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show what would be added without modifying files")] = False,
    fetch_titles: Annotated[bool, typer.Option("--fetch-titles/--no-fetch-titles", help="Fetch actual titles from PubMed (default: True)")] = True,
):
    """Seed missing GOA annotations into a gene review YAML file.
    
    This command adds any annotations from the GOA file that are missing
    from the YAML file. It does NOT overwrite existing annotations.
    The review sections are left empty for AI to fill in later.
    
    Examples:
        ai-gene-review seed-goa genes/human/JAK1/JAK1-ai-review.yaml
        ai-gene-review seed-goa test.yaml --goa custom-goa.tsv --output updated.yaml
        ai-gene-review seed-goa test.yaml --dry-run  # Preview changes
    """
    yaml_file = Path(yaml_file)
    
    if not yaml_file.exists() and not dry_run:
        typer.echo(f"Warning: YAML file not found: {yaml_file}", err=True)
        typer.echo("A new file will be created with seeded annotations.")
    
    # Initialize validator
    validator = GOAValidator()
    
    # First check what's missing
    if yaml_file.exists():
        typer.echo(f"Checking {yaml_file.name} for missing annotations...")
        result = validator.validate_against_goa(yaml_file, goa_file)
        
        if not result.missing_in_yaml:
            typer.echo("✓ No missing annotations to seed - YAML already contains all GOA annotations")
            return
        
        typer.echo(f"Found {len(result.missing_in_yaml)} missing annotations to seed:")
        for ann in result.missing_in_yaml[:5]:  # Show first 5
            typer.echo(f"  - {ann.go_id} ({ann.go_term})")
        if len(result.missing_in_yaml) > 5:
            typer.echo(f"  ... and {len(result.missing_in_yaml) - 5} more")
    else:
        typer.echo("Creating new YAML file with all GOA annotations...")
    
    if dry_run:
        typer.echo("\n--dry-run specified, no changes will be made")
        return
    
    # Perform the seeding
    try:
        added_count, output_path, refs_added = validator.seed_missing_annotations(
            yaml_file, 
            goa_file,
            output,
            fetch_titles=fetch_titles
        )
        
        if added_count > 0 or refs_added > 0:
            parts = []
            if added_count > 0:
                parts.append(f"{added_count} annotations")
            if refs_added > 0:
                parts.append(f"{refs_added} references")
            typer.echo(f"\n✓ Successfully added {' and '.join(parts)} to {output_path}")
            typer.echo("\nNote: Review sections left empty for AI to complete")
        else:
            typer.echo("\n✓ No annotations added (all GOA annotations already present)")
            
    except (ValueError, FileNotFoundError) as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def fetch_gene_pmids(
    organism: Annotated[str, typer.Argument(help="Organism name")],
    gene: Annotated[str, typer.Argument(help="Gene symbol")],
    output_dir: Annotated[Optional[Path], typer.Option("--output-dir", "-o", help="Output directory")] = None,
    force: Annotated[bool, typer.Option("--force", "-f", help="Force re-download even if cached")] = False,
    delay: Annotated[float, typer.Option("--delay", "-d", help="Delay between requests")] = 0.5,
):
    """Fetch all PMIDs referenced in a gene's review file.
    
    Example:
        ai-gene-review fetch-gene-pmids human CFAP300
    """
    output_dir = output_dir or Path("publications")
    
    # Construct path to gene review file
    review_file = Path("genes") / organism / gene / f"{gene}-ai-review.yaml"
    
    if not review_file.exists():
        typer.echo(f"Error: Review file not found: {review_file}", err=True)
        typer.echo(f"Hint: Run 'ai-gene-review fetch-gene {organism} {gene}' first", err=True)
        raise typer.Exit(code=1)
    
    # Extract PMIDs from the review file
    pmids = extract_pmids_from_yaml(review_file)
    
    if not pmids:
        typer.echo(f"No PMIDs found in {review_file}")
        return
    
    typer.echo(f"Found {len(pmids)} PMIDs in {gene} review file")
    for pmid in pmids:
        typer.echo(f"  - PMID:{pmid}")
    
    success_count = cache_publications(pmids, output_dir, force, delay)
    
    if success_count == len(pmids):
        typer.echo(f"✓ Successfully cached all {success_count} publications for {gene}")
    else:
        typer.echo(f"⚠ Cached {success_count}/{len(pmids)} publications", err=True)


@app.command()
def mark_invalid_pmids(
    yaml_file: Annotated[Path, typer.Argument(help="Gene review YAML file to update")],
    pmids: Annotated[List[str], typer.Argument(help="PMIDs to mark as invalid (e.g., PMID:12345 or 12345)")],
    output: Annotated[Optional[Path], typer.Option("--output", "-o", help="Output file (overwrites input if not specified)")] = None,
):
    """Mark PMIDs as invalid when they can't be retrieved from PubMed.
    
    This command adds is_invalid: true to references that can't be retrieved,
    preventing future validation warnings.
    
    Examples:
        ai-gene-review mark-invalid-pmids genes/human/JAK1/JAK1-ai-review.yaml PMID:34521819
        ai-gene-review mark-invalid-pmids test.yaml 34521819 12345 --output updated.yaml
    """
    from ai_gene_review.validation.publication_validator import mark_invalid_pmids
    
    yaml_file = Path(yaml_file)
    
    if not yaml_file.exists():
        typer.echo(f"Error: File not found: {yaml_file}", err=True)
        raise typer.Exit(code=1)
    
    typer.echo(f"Marking {len(pmids)} PMID(s) as invalid in {yaml_file.name}...")
    
    try:
        count = mark_invalid_pmids(yaml_file, pmids, output)
        
        if count > 0:
            output_path = output or yaml_file
            typer.echo(f"✓ Marked {count} reference(s) as invalid in {output_path}")
            typer.echo("\nThese PMIDs will be skipped during future validations.")
        else:
            typer.echo("No references were updated (PMIDs not found or already marked invalid)")
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def expand_organism(
    organisms: Annotated[List[str], typer.Argument(help="Organism codes, names, or taxon IDs to expand")],
):
    """Expand organism codes or names to full scientific names.
    
    Supports:
    - UniProt organism codes (e.g., PSEPK, ECOLI)
    - Common names (e.g., human, mouse, yeast)
    - NCBI taxon IDs (e.g., 9606, 10090)
    - Scientific names (preserved as-is)
    
    Examples:
        ai-gene-review expand-organism PSEPK
        ai-gene-review expand-organism human mouse ECOLI
        ai-gene-review expand-organism 9606 160488
    """
    for organism in organisms:
        expanded = expand_organism_name(organism)
        if expanded == organism:
            typer.echo(f"{organism} → {expanded} (unchanged)")
        else:
            typer.echo(f"{organism} → {expanded}")


def main():
    """Main entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
