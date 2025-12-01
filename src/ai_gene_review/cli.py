"""CLI interface for ai-gene-review."""

from pathlib import Path
from typing import List, Optional

import typer
from typing_extensions import Annotated

from ai_gene_review.etl.gene import fetch_gene_data, fetch_gene_data_ncRNA, expand_organism_name
from ai_gene_review.etl.publication import (
    cache_publications,
    extract_pmids_from_yaml,
)
from ai_gene_review.etl.publication_refresh import (
    find_pmc_candidates,
    refetch_publications,
    get_refresh_summary,
)
from ai_gene_review.validation import (
    validate_gene_review,
    validate_multiple_files,
    ValidationSeverity,
)
from ai_gene_review.validation.goa_validator import GOAValidator
from ai_gene_review.draw import ReviewVisualizer

app = typer.Typer(help="ai-gene-review: Gene data ETL and review tool.")


@app.command()
def fetch_gene(
    organism: Annotated[
        str, typer.Argument(help="Organism name (e.g., human, mouse, yeast)")
    ],
    gene: Annotated[
        str, typer.Argument(help="Gene symbol (e.g., CFAP300, TP53, BRCA1)")
    ],
    uniprot_id: Annotated[
        Optional[str],
        typer.Option(
            "--uniprot-id",
            "-u",
            help="UniProt accession ID (optional, will be resolved if not provided)",
        ),
    ] = None,
    output_dir: Annotated[
        Optional[Path],
        typer.Option(
            "--output-dir", "-o", help="Output directory (default: current directory)"
        ),
    ] = None,
    no_seed: Annotated[
        bool,
        typer.Option(
            "--no-seed", help="Skip seeding ai-review.yaml with GOA annotations"
        ),
    ] = False,
    fetch_titles: Annotated[
        bool,
        typer.Option(
            "--fetch-titles/--no-fetch-titles",
            help="Fetch actual titles from PubMed when seeding (default: True)",
        ),
    ] = True,
    alias: Annotated[
        Optional[str],
        typer.Option(
            "--alias",
            "-a",
            help="Alias to use for directory name and file prefixes instead of gene symbol",
        ),
    ] = None,
    force: Annotated[
        bool,
        typer.Option(
            "--force",
            "-f",
            help="Force overwrite existing UniProt and GOA files even if they differ from remote sources",
        ),
    ] = False,
):
    """Fetch gene data from UniProt and GOA databases.

    Creates a directory structure:
    genes/<organism>/<gene>/
        <gene>-uniprot.txt
        <gene>-goa.tsv
        <gene>-ai-review.yaml (seeded with GOA annotations and reference titles)

    By default, compares remote data with existing files and only overwrites if content differs.
    Existing files are preserved unless --force is used to override this protection.

    Use --no-fetch-titles to skip title fetching for faster execution.
    Use --alias to specify a custom name for the directory and file prefixes.

    Examples:
        ai-gene-review fetch-gene human TP53
        ai-gene-review fetch-gene human TP53 --force  # Force overwrite existing files
        ai-gene-review fetch-gene 9BACT F0JBF1 --alias HgcB
    """
    try:
        typer.echo(f"Fetching data for {gene} ({organism})...")

        result = fetch_gene_data(
            gene_info=(organism, gene),
            uniprot_id=uniprot_id,
            base_path=output_dir,
            seed_annotations=not no_seed,
            fetch_titles=fetch_titles,
            alias=alias,
            force=force,
        )

        # Show where files were created
        base_path = output_dir or Path.cwd()
        dir_name = alias if alias else gene
        file_prefix = alias if alias else gene
        gene_dir = base_path / "genes" / organism / dir_name

        typer.echo("✓ Gene data fetch completed!")
        typer.echo(f"Location: {gene_dir}")

        # Report any differences found that weren't updated
        differences_not_updated = []
        if not force:
            if result.get("uniprot_differences") and not result.get("uniprot_updated"):
                differences_not_updated.append(f"{file_prefix}-uniprot.txt differs from remote")
            if result.get("goa_differences") and not result.get("goa_updated"):
                differences_not_updated.append(f"{file_prefix}-goa.tsv differs from remote")

        if differences_not_updated:
            typer.echo("")
            typer.echo("⚠ Some files have differences but were not updated:")
            for diff in differences_not_updated:
                typer.echo(f"  - {diff}")
            typer.echo("Use --force to overwrite existing files")

        # Display appropriate message for ai-review.yaml
        if not no_seed:
            if result["yaml_created"]:
                typer.echo(
                    f"  - {file_prefix}-ai-review.yaml (created with {result['annotations_added']} GOA annotations)"
                )
            elif result["yaml_existed"]:
                if (
                    result["annotations_added"] > 0
                    or result.get("references_added", 0) > 0
                ):
                    parts = []
                    if result["annotations_added"] > 0:
                        parts.append(f"{result['annotations_added']} annotations")
                    if result.get("references_added", 0) > 0:
                        parts.append(f"{result.get('references_added', 0)} references")
                    typer.echo(
                        f"  - {file_prefix}-ai-review.yaml (added {' and '.join(parts)})"
                    )
                else:
                    typer.echo(f"  - {file_prefix}-ai-review.yaml (unmodified)")

    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def fetch_ncrna(
    organism: Annotated[
        str, typer.Argument(help="Organism name (e.g., human, mouse, yeast)")
    ],
    gene: Annotated[
        str, typer.Argument(help="Gene symbol (e.g., SNORD3A, XIST, H19)")
    ],
    rnacentral_id: Annotated[
        Optional[str],
        typer.Option(
            "--rnacentral-id",
            "-r",
            help="RNAcentral ID (optional, will be resolved if not provided)",
        ),
    ] = None,
    output_dir: Annotated[
        Optional[Path],
        typer.Option(
            "--output-dir", "-o", help="Output directory (default: current directory)"
        ),
    ] = None,
    no_seed: Annotated[
        bool,
        typer.Option(
            "--no-seed", help="Skip creating ai-review.yaml structure"
        ),
    ] = False,
    alias: Annotated[
        Optional[str],
        typer.Option(
            "--alias",
            "-a",
            help="Alias to use for directory name and file prefixes instead of gene symbol",
        ),
    ] = None,
    force: Annotated[
        bool,
        typer.Option(
            "--force",
            "-f",
            help="Force overwrite existing RNAcentral files even if they exist",
        ),
    ] = False,
):
    """Fetch ncRNA gene data from RNAcentral database.

    Creates a directory structure:
    genes/<organism>/<gene>/
        <gene>-rnacentral.json
        <gene>-ai-review.yaml (with ncRNA-specific structure)

    This command is designed for non-coding RNA genes and uses RNAcentral
    as the primary data source instead of UniProt.

    Use --alias to specify a custom name for the directory and file prefixes.
    """
    try:
        typer.echo(f"Fetching ncRNA data for {gene} ({organism})...")

        result = fetch_gene_data_ncRNA(
            gene_info=(organism, gene),
            rnacentral_id=rnacentral_id,
            base_path=output_dir,
            seed_annotations=not no_seed,
            alias=alias,
            force=force,
        )

        # Show where files were created
        base_path = output_dir or Path.cwd()
        dir_name = alias if alias else gene
        file_prefix = alias if alias else gene
        gene_dir = base_path / "genes" / organism / dir_name

        typer.echo("✓ ncRNA data fetch completed!")
        typer.echo(f"Location: {gene_dir}")

        # Report any differences found that weren't updated
        differences_not_updated = []
        if not force:
            if result.get("rnacentral_differences") and not result.get("rnacentral_updated"):
                differences_not_updated.append(f"{file_prefix}-rnacentral.json differs from remote")
            if result.get("goa_differences") and not result.get("goa_updated"):
                differences_not_updated.append(f"{file_prefix}-goa.tsv differs from remote")

        if differences_not_updated:
            typer.echo("")
            typer.echo("⚠ Some files have differences but were not updated:")
            for diff in differences_not_updated:
                typer.echo(f"  - {diff}")
            typer.echo("Use --force to overwrite existing files")

        # Display appropriate message for ai-review.yaml
        if not no_seed:
            if result["yaml_created"]:
                typer.echo(
                    f"  - {file_prefix}-ai-review.yaml (created with ncRNA structure)"
                )
            elif result["yaml_existed"]:
                typer.echo(f"  - {file_prefix}-ai-review.yaml (already exists)")

    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def batch_fetch(
    input_file: Annotated[
        Path, typer.Argument(help="File containing organism,gene pairs (one per line)")
    ],
    output_dir: Annotated[
        Optional[Path],
        typer.Option(
            "--output-dir", "-o", help="Output directory (default: current directory)"
        ),
    ] = None,
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

    lines = input_file.read_text().strip().split("\n")

    success_count = 0
    error_count = 0

    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        parts = [p.strip() for p in line.replace("\t", ",").split(",")]

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
                gene_info=(organism, gene), uniprot_id=uniprot_id, base_path=output_dir
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
    schema: Annotated[
        Optional[Path],
        typer.Option(
            "--schema",
            "-s",
            help="Path to LinkML schema (uses default if not provided)",
        ),
    ] = None,
    verbose: Annotated[
        bool,
        typer.Option(
            "--verbose", "-v", help="Show detailed messages including warnings"
        ),
    ] = False,
    strict: Annotated[
        bool, typer.Option("--strict", help="Treat warnings as errors")
    ] = False,
    no_best_practices: Annotated[
        bool, typer.Option("--no-best-practices", help="Skip best practices checks")
    ] = False,
    no_goa: Annotated[
        bool, typer.Option("--no-goa", help="Skip GOA validation")
    ] = False,
    no_supporting_text: Annotated[
        bool,
        typer.Option(
            "--no-supporting-text",
            help="Skip supporting_text validation against cached publications",
        ),
    ] = False,
    tsv_output: Annotated[
        Optional[Path],
        typer.Option(
            "--tsv-output",
            help="Output validation results to TSV file with categorized issues",
        ),
    ] = None,
    show_timing: Annotated[
        bool, typer.Option("--show-timing", help="Show timing information for validation steps")
    ] = False,
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
            all_files.extend(
                [Path(f) for f in matched if f.endswith(".yaml") or f.endswith(".yml")]
            )
        else:
            all_files.append(pattern)

    if not all_files:
        typer.echo("No files found to validate", err=True)
        raise typer.Exit(code=1)

    check_best_practices = not no_best_practices
    check_goa = not no_goa
    check_supporting_text = not no_supporting_text

    # Validate single file or multiple files
    if len(all_files) == 1:
        yaml_file = all_files[0]
        typer.echo(f"Validating {yaml_file}...")

        report = validate_gene_review(
            yaml_file, schema, check_best_practices, check_goa, check_supporting_text
        )

        # Determine status symbol and color
        if report.is_valid and not (strict and report.has_warnings):
            status = "✓ Valid"
            if report.has_warnings:
                status += f" (with {report.warning_count} warnings)"
            typer.echo(status)
        else:
            typer.echo(
                "✗ Invalid" if report.has_errors else "⚠ Warnings found", err=True
            )

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
                    elif (
                        issue.severity == ValidationSeverity.WARNING
                        and warnings_shown < 3
                    ):
                        _print_issue(issue)
                        warnings_shown += 1

                remaining_warnings = report.warning_count - warnings_shown
                if remaining_warnings > 0:
                    typer.echo(
                        f"  ... and {remaining_warnings} more warnings (use --verbose to see all)",
                        err=True,
                    )

        # Write TSV output if requested
        if tsv_output:
            try:
                from ai_gene_review.validation.validation_report import BatchValidationReport
                # Create a batch report with single file for TSV output
                batch_report = BatchValidationReport(reports=[report])
                batch_report.write_tsv(str(tsv_output))
                typer.echo(f"TSV output written to: {tsv_output}")
            except Exception as e:
                typer.echo(f"Error writing TSV output: {e}", err=True)

        # Exit code based on validation result and strict mode
        if not report.is_valid or (strict and report.has_warnings):
            raise typer.Exit(code=1)

    else:
        # Multiple files
        typer.echo(f"Validating {len(all_files)} files...")

        # Cast to List[Path | str] for type compatibility
        files_to_validate: list[Path | str] = [f for f in all_files]
        batch_report = validate_multiple_files(
            files_to_validate,
            schema,
            check_best_practices,
            check_goa,
            check_supporting_text,
            show_progress=True,  # Enable progress bar for multiple files
        )

        # Show summary
        typer.echo(batch_report.summary())

        # Write TSV output if requested
        if tsv_output:
            try:
                batch_report.write_tsv(str(tsv_output))
                typer.echo(f"TSV output written to: {tsv_output}")
            except Exception as e:
                typer.echo(f"Error writing TSV output: {e}", err=True)

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
        ValidationSeverity.INFO: "ℹ",
    }.get(issue.severity, "•")

    err = issue.severity in [ValidationSeverity.ERROR, ValidationSeverity.WARNING]
    typer.echo(f"{indent}{symbol} {issue}", err=err)


@app.command()
def fetch_pmid(
    pmids: Annotated[
        list[str], typer.Argument(help="PMID(s) to fetch (e.g., PMID:12345 or 12345)")
    ],
    output_dir: Annotated[
        Optional[Path],
        typer.Option(
            "--output-dir", "-o", help="Output directory for cached publications"
        ),
    ] = None,
    force: Annotated[
        bool, typer.Option("--force", "-f", help="Force re-download even if cached")
    ] = False,
    delay: Annotated[
        float, typer.Option("--delay", "-d", help="Delay between requests in seconds")
    ] = 0.5,
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
    input_file: Annotated[
        Path, typer.Argument(help="File containing PMIDs (one per line)")
    ],
    output_dir: Annotated[
        Optional[Path], typer.Option("--output-dir", "-o", help="Output directory")
    ] = None,
    force: Annotated[
        bool, typer.Option("--force", "-f", help="Force re-download even if cached")
    ] = False,
    delay: Annotated[
        float, typer.Option("--delay", "-d", help="Delay between requests")
    ] = 0.5,
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
            if line and not line.startswith("#"):
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
    yaml_file: Annotated[
        Path, typer.Argument(help="Gene review YAML file to validate")
    ],
    goa_file: Annotated[
        Optional[Path],
        typer.Option(
            "--goa", "-g", help="GOA TSV file (auto-detected if not provided)"
        ),
    ] = None,
    strict: Annotated[
        bool, typer.Option("--strict", help="Fail on evidence type mismatches")
    ] = False,
    verbose: Annotated[
        bool, typer.Option("--verbose", "-v", help="Show detailed validation results")
    ] = False,
    show_all: Annotated[
        bool, typer.Option("--show-all", help="Show all mismatches, not just first few")
    ] = False,
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
            typer.echo(
                f"\n{len(result.missing_in_yaml)} annotations in GOA but not in YAML:"
            )
            limit = None if show_all else 10  # Show all or just first 10
            for i, ann in enumerate(
                result.missing_in_yaml[:limit] if limit else result.missing_in_yaml
            ):
                typer.echo(
                    f"  {i + 1}. {ann.go_id} ({ann.go_term}) - {ann.evidence_code} - {ann.reference}"
                )
            if limit and len(result.missing_in_yaml) > limit:
                typer.echo(
                    f"  ... and {len(result.missing_in_yaml) - limit} more (use --show-all to see all)"
                )

        if result.missing_in_goa:
            typer.echo(
                f"\n{len(result.missing_in_goa)} annotations in YAML but not in GOA:"
            )
            limit = None if show_all else 10  # Show all or just first 10
            for i, yaml_ann in enumerate(
                result.missing_in_goa[:limit] if limit else result.missing_in_goa
            ):
                go_id = yaml_ann.get("term", {}).get("id", "unknown")
                label = yaml_ann.get("term", {}).get("label", "unknown")
                evidence = yaml_ann.get("evidence_type", "unknown")
                ref = yaml_ann.get("original_reference_id", "unknown")
                typer.echo(f"  {i + 1}. {go_id} ({label}) - {evidence} - {ref}")
            if limit and len(result.missing_in_goa) > limit:
                typer.echo(
                    f"  ... and {len(result.missing_in_goa) - limit} more (use --show-all to see all)"
                )

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
    goa_file: Annotated[
        Optional[Path],
        typer.Option(
            "--goa", "-g", help="GOA TSV file (auto-detected if not provided)"
        ),
    ] = None,
    output: Annotated[
        Optional[Path],
        typer.Option(
            "--output", "-o", help="Output file (overwrites input if not specified)"
        ),
    ] = None,
    dry_run: Annotated[
        bool,
        typer.Option(
            "--dry-run", help="Show what would be added without modifying files"
        ),
    ] = False,
    fetch_titles: Annotated[
        bool,
        typer.Option(
            "--fetch-titles/--no-fetch-titles",
            help="Fetch actual titles from PubMed (default: True)",
        ),
    ] = True,
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
            typer.echo(
                "✓ No missing annotations to seed - YAML already contains all GOA annotations"
            )
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
            yaml_file, goa_file, output, fetch_titles=fetch_titles
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
    output_dir: Annotated[
        Optional[Path], typer.Option("--output-dir", "-o", help="Output directory")
    ] = None,
    force: Annotated[
        bool, typer.Option("--force", "-f", help="Force re-download even if cached")
    ] = False,
    delay: Annotated[
        float, typer.Option("--delay", "-d", help="Delay between requests")
    ] = 0.5,
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
        typer.echo(
            f"Hint: Run 'ai-gene-review fetch-gene {organism} {gene}' first", err=True
        )
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
    pmids: Annotated[
        List[str],
        typer.Argument(help="PMIDs to mark as invalid (e.g., PMID:12345 or 12345)"),
    ],
    output: Annotated[
        Optional[Path],
        typer.Option(
            "--output", "-o", help="Output file (overwrites input if not specified)"
        ),
    ] = None,
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
            typer.echo(
                "No references were updated (PMIDs not found or already marked invalid)"
            )
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def refresh_publications(
    count: Annotated[
        Optional[int],
        typer.Option(
            "--count", "-c", help="Number of publications to process (default: all)"
        ),
    ] = None,
    delay: Annotated[
        float, typer.Option("--delay", "-d", help="Delay between requests in seconds")
    ] = 1.0,
    publications_dir: Annotated[
        Path, typer.Option("--dir", help="Publications directory")
    ] = Path("publications"),
    show_summary: Annotated[
        bool,
        typer.Option("--summary", help="Show summary of publications cache status"),
    ] = False,
    show_candidates: Annotated[
        int,
        typer.Option(
            "--show-candidates",
            help="Show sample of publications needing refresh (specify number)",
        ),
    ] = 0,
    force_all: Annotated[
        bool,
        typer.Option("--force-all", help="Force refresh ALL publications, not just those missing full text"),
    ] = False,
):
    """Refresh publications cache for PMC articles with missing full text.

    Identifies PMC articles that lack full text content and attempts to re-fetch
    them using enhanced retrieval methods (HTML and PDF fallbacks). This addresses
    cases where:

    - Articles became available since initial fetch
    - Enhanced system can retrieve content that XML-only approach missed
    - PMC access policies have relaxed over time
    - Better parsing of existing content formats is available

    Expected success rates:
    - Overall: ~90% for articles with PMC IDs
    - Recent articles (2010+): ~95% success
    - Older articles (pre-2010): ~80% success

    Examples:
        ai-gene-review refresh-publications --count 50 --delay 1.0
        ai-gene-review refresh-publications --summary
        ai-gene-review refresh-publications --show-candidates 10
    """
    # Show summary if requested
    if show_summary:
        summary = get_refresh_summary(publications_dir)
        typer.echo("Publications Cache Refresh Status:")
        typer.echo(f"  Total PMC articles: {summary['total_pmc_articles']}")
        typer.echo(f"  Need refresh: {summary['need_refresh']}")
        typer.echo(f"  Estimated success: ~{summary['estimated_success']} articles")
        typer.echo(f"  Expected success rate: {summary['success_rate_estimate']:.0%}")
        return

    # Show candidates if requested
    if show_candidates > 0:
        candidates = find_pmc_candidates(publications_dir)
        typer.echo("Sample of publications needing full text refresh:")
        for i, candidate in enumerate(candidates[:show_candidates]):
            typer.echo(f"  {candidate['file']} ({candidate['pmcid']})")
        if len(candidates) > show_candidates:
            typer.echo(f"  ... and {len(candidates) - show_candidates} more")
        return

    # Find candidates for refresh
    typer.echo("Scanning publications folder...")
    
    if force_all:
        # Get ALL publications for forced refresh
        import re
        from pathlib import Path
        
        candidates = []
        for file_path in sorted(publications_dir.glob("PMID_*.md")):
            match = re.match(r"PMID_(\d+)\.md", file_path.name)
            if match:
                pmid = match.group(1)
                candidates.append({
                    'pmid': pmid,
                    'file': file_path.name,
                    'pmcid': None,  # Will be determined during refresh
                    'full_text_available': False,  # Force refresh regardless
                    'has_full_text_section': False
                })
        
        if not candidates:
            typer.echo("No publication files found.")
            return
            
        typer.echo(f"Found {len(candidates)} publications to force refresh.")
    else:
        # Normal mode: only get candidates missing full text
        candidates = find_pmc_candidates(publications_dir)
        
        if not candidates:
            typer.echo("No candidates found for refresh.")
            return
        
        typer.echo(
            f"Found {len(candidates)} publications with PMC IDs but missing full text."
        )

    # Determine how many to process
    if count is None:
        total_to_process = len(candidates)
        typer.echo("Processing ALL publications...")
    else:
        total_to_process = min(count, len(candidates))
        typer.echo(f"Processing batch of {total_to_process} publications...")

    # Perform refresh
    stats = refetch_publications(
        candidates, max_requests=count, delay=delay, publications_dir=publications_dir
    )

    # Print summary
    typer.echo("=" * 60)
    typer.echo("REFRESH SUMMARY")
    typer.echo("=" * 60)
    typer.echo(f"Processed: {stats['processed']}")
    typer.echo(f"Success (full text retrieved): {stats['success']}")
    typer.echo(f"Failed (still no full text): {stats['failed']}")

    if stats["processed"] > 0:
        success_rate = stats["success"] / stats["processed"] * 100
        typer.echo(f"Success rate: {success_rate:.1f}%")

    typer.echo("\nRefresh complete!")


@app.command()
def expand_organism(
    organisms: Annotated[
        List[str], typer.Argument(help="Organism codes, names, or taxon IDs to expand")
    ],
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


@app.command()
def visualize(
    yaml_file: Annotated[
        Path, typer.Argument(help="Gene review YAML file to visualize")
    ],
    output: Annotated[
        Optional[Path],
        typer.Option(
            "--output", "-o", help="Output file (default: <gene>-review-visual.svg)"
        ),
    ] = None,
    format: Annotated[
        str,
        typer.Option(
            "--format", "-f", help="Output format (svg or png, requires Cairo for png)"
        ),
    ] = "svg",
    slim: Annotated[
        str,
        typer.Option(
            "--slim", "-s", help="GO slim subset to use (default: goslim_generic)"
        ),
    ] = "goslim_generic",
    show_stats: Annotated[
        bool,
        typer.Option("--stats", help="Show summary statistics"),
    ] = False,
):
    """Visualize gene review annotations and their actions.
    
    Creates a clean SVG visualization showing:
    - GO terms organized hierarchically by GO slim categories
    - Review actions (Accept, Modify, Remove, etc.) with visual indicators
    - Proposed replacement terms for modifications
    
    Examples:
        ai-gene-review visualize genes/human/CFAP300/CFAP300-ai-review.yaml
        ai-gene-review visualize genes/yeast/LPL1/LPL1-ai-review.yaml -o lpl1-visual.svg
        ai-gene-review visualize test.yaml --format png --stats
    """
    yaml_file = Path(yaml_file)
    
    if not yaml_file.exists():
        typer.echo(f"Error: File not found: {yaml_file}", err=True)
        raise typer.Exit(code=1)
    
    # Determine output path
    if output is None:
        # Default: same directory as input, with -review-visual suffix
        stem = yaml_file.stem.replace("-ai-review", "")
        output = yaml_file.parent / f"{stem}-review-visual.{format}"
    else:
        output = Path(output)
        # Add extension if not present
        if not output.suffix:
            output = output.with_suffix(f".{format}")
    
    typer.echo(f"Visualizing {yaml_file.name}...")
    
    try:
        # Create visualizer
        from ai_gene_review.draw.layout_engine import LayoutConfig
        config = LayoutConfig()
        visualizer = ReviewVisualizer(layout_config=config, slim_subset=slim)
        
        # Load and visualize the file
        drawing = visualizer.visualize_file(yaml_file)
        
        # Show statistics if requested
        if show_stats:
            import yaml
            with open(yaml_file) as f:
                data = yaml.safe_load(f)
            from ai_gene_review.datamodel.gene_review_model import GeneReview
            gene_review = GeneReview.model_validate(data)
            stats = visualizer.get_summary_stats(gene_review)
            
            typer.echo("\nSummary Statistics:")
            typer.echo(f"  Total annotations: {stats['total_annotations']}")
            typer.echo("  Actions:")
            for action, count in stats['actions'].items():
                if count > 0:
                    pct = stats['action_percentages'][action]
                    typer.echo(f"    {action}: {count} ({pct:.1f}%)")
        
        # Save the visualization
        visualizer.save(output, format)
        typer.echo(f"✓ Visualization saved to: {output}")
        
    except ImportError as e:
        if "Cairo" in str(e):
            typer.echo(
                "Error: Cairo is required for PNG export. Install with:", err=True
            )
            typer.echo("  pip install pycairo", err=True)
            typer.echo("Or use --format svg instead", err=True)
        else:
            typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"Error creating visualization: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def update_status(
    files: Annotated[
        Optional[List[Path]],
        typer.Argument(help="Gene review YAML file(s) to check/update (if omitted, scans all genes)"),
    ] = None,
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", "-n", help="Don't actually update files, just report what would be done"),
    ] = False,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Show detailed information for each file"),
    ] = False,
    report_only: Annotated[
        bool,
        typer.Option("--report-only", "-r", help="Only show files with status issues (mismatch or missing)"),
    ] = False,
):
    """Check and update the status field in gene review files.

    This command computes the expected status based on annotation states and validation warnings:
    - INITIALIZED: All annotations have action PENDING
    - IN_PROGRESS: At least one annotation is PENDING and at least one is not PENDING
    - DRAFT: No PENDING annotations, but may have validation warnings
    - COMPLETE: No PENDING annotations and no validation warnings

    Examples:
        # Update status for a specific file
        ai-gene-review update-status genes/human/CFAP300/CFAP300-ai-review.yaml

        # Check all gene review files (dry run)
        ai-gene-review update-status --dry-run

        # Update all files with verbose output
        ai-gene-review update-status --verbose

        # Only show files with issues
        ai-gene-review update-status --report-only
    """
    from ai_gene_review.status_manager import check_and_update_status

    # Determine which files to process
    if files:
        yaml_files = [Path(f) for f in files]
    else:
        # Scan all gene review files
        genes_dir = Path("genes")
        if not genes_dir.exists():
            typer.echo("Error: 'genes' directory not found", err=True)
            raise typer.Exit(code=1)

        yaml_files = list(genes_dir.glob("*/*/*.yaml"))
        # Filter to ai-review files only
        yaml_files = [f for f in yaml_files if f.stem.endswith("-ai-review")]

        if not yaml_files:
            typer.echo("No gene review files found in genes directory", err=True)
            raise typer.Exit(code=1)

    # Process files
    results = []
    for yaml_file in yaml_files:
        if not yaml_file.exists():
            typer.echo(f"Warning: File not found: {yaml_file}", err=True)
            continue

        result = check_and_update_status(yaml_file, dry_run=dry_run, verbose=verbose)
        results.append(result)

    # Summary reporting
    total = len(results)
    missing = sum(1 for r in results if r["needs_update"])
    mismatched = sum(1 for r in results if r["status_mismatch"])
    updated = sum(1 for r in results if r["updated"])
    has_warnings = sum(1 for r in results if r["has_warnings"])

    if report_only:
        # Only show files with issues
        issues = [r for r in results if r["needs_update"] or r["status_mismatch"]]

        if not issues:
            typer.echo("✓ All files have correct status")
        else:
            typer.echo(f"\nFiles with status issues: {len(issues)}/{total}")
            for result in issues:
                file_path = Path(result["file"])
                if result["needs_update"]:
                    typer.echo(f"  ⚠ {file_path}: status not set (should be {result['expected_status']})")
                elif result["status_mismatch"]:
                    typer.echo(
                        f"  ⚠ {file_path}: status mismatch "
                        f"(current={result['current_status']}, expected={result['expected_status']})"
                    )
    else:
        # Full summary
        typer.echo(f"\nProcessed {total} file(s)")
        typer.echo(f"  Status missing: {missing}")
        typer.echo(f"  Status mismatch: {mismatched}")
        if not dry_run:
            typer.echo(f"  Updated: {updated}")
        typer.echo(f"  Files with validation warnings: {has_warnings}")

        if dry_run and (missing > 0 or mismatched > 0):
            typer.echo(f"\nRun without --dry-run to apply updates")

    # Exit with error if there are mismatches
    if mismatched > 0:
        raise typer.Exit(code=1)


@app.command()
def arba_sync(
    query: Annotated[
        str,
        typer.Option("--query", "-q", help="Search query (default: all rules)"),
    ] = "*",
    batch_size: Annotated[
        int,
        typer.Option("--batch-size", "-b", help="Number of rules per API request"),
    ] = 500,
    force: Annotated[
        bool,
        typer.Option("--force", "-f", help="Force re-download even if cached"),
    ] = False,
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", "-d", help="Cache directory for ARBA rules"),
    ] = Path("rules/arba"),
    limit: Annotated[
        Optional[int],
        typer.Option("--limit", "-l", help="Maximum number of rules to fetch (for testing)"),
    ] = None,
    go_only: Annotated[
        bool,
        typer.Option("--go-only/--all", help="Only sync rules with GO annotations (default: GO only)"),
    ] = True,
):
    """Sync ARBA (Association-Rule-Based Annotator) rules from UniProt.

    Downloads and caches ARBA rules locally for offline access and analysis.
    By default, only syncs rules that have GO term annotations.

    Examples:
        # Sync ARBA rules with GO annotations (default)
        ai-gene-review arba-sync

        # Sync ALL ARBA rules (about 80,000 rules)
        ai-gene-review arba-sync --all

        # Sync rules for a specific EC number
        ai-gene-review arba-sync --query "ec:2.3.2.5"

        # Force re-download all rules
        ai-gene-review arba-sync --force

        # Test with a small batch
        ai-gene-review arba-sync --limit 100
    """
    from ai_gene_review.etl.arba import ARBAClient

    client = ARBAClient(cache_dir=cache_dir)

    # Get total count
    total = client.get_total_count()
    typer.echo(f"Total ARBA rules available: {total}")

    if go_only:
        typer.echo("Filtering for rules with GO annotations only")

    if limit:
        typer.echo(f"Limiting to {limit} matched rules (for testing)")

    # Progress callback
    def progress(fetched: int, total_available: int, matched: int) -> None:
        pct = (fetched / total_available) * 100 if total_available > 0 else 0
        typer.echo(f"  Scanned: {fetched}/{total_available} ({pct:.1f}%) | Matched: {matched}", nl=False)
        typer.echo("\r", nl=False)

    typer.echo(f"Syncing ARBA rules to {cache_dir}...")

    # Iterate and sync
    count = 0
    for rule in client.iter_all_rules(
        query=query,
        batch_size=batch_size,
        cache=True,
        go_only=go_only,
        progress_callback=progress
    ):
        count += 1
        if limit and count >= limit:
            break

    typer.echo(f"\n✓ Synced {count} ARBA rules to {cache_dir}")


@app.command()
def arba_stats(
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", "-d", help="Cache directory for ARBA rules"),
    ] = Path("rules/arba"),
):
    """Show statistics about the local ARBA cache.

    Examples:
        ai-gene-review arba-stats
        ai-gene-review arba-stats --cache-dir ./my-arba-cache
    """
    from ai_gene_review.etl.arba import ARBAClient

    client = ARBAClient(cache_dir=cache_dir)

    # Check if cache exists
    if not cache_dir.exists():
        typer.echo(f"No ARBA cache found at {cache_dir}")
        typer.echo("Run 'ai-gene-review arba-sync' to download rules")
        return

    stats = client.get_cache_stats()

    typer.echo(f"ARBA Cache Statistics ({cache_dir}):")
    typer.echo(f"  Cached rules: {stats['cached_rules']}")
    typer.echo(f"  Cache size: {stats['cache_size_mb']} MB")

    # Show metadata if available
    meta_file = cache_dir / "_metadata.json"
    if meta_file.exists():
        import json
        metadata = json.loads(meta_file.read_text())
        typer.echo(f"  Last sync: {metadata.get('last_sync', 'unknown')}")


@app.command()
def arba_lookup(
    rule_id: Annotated[
        str,
        typer.Argument(help="ARBA rule ID (e.g., ARBA00000001)"),
    ],
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", "-d", help="Cache directory for ARBA rules"),
    ] = Path("rules/arba"),
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
):
    """Look up a specific ARBA rule by ID.

    Examples:
        ai-gene-review arba-lookup ARBA00000001
        ai-gene-review arba-lookup ARBA00000001 --json
    """
    from ai_gene_review.etl.arba import ARBAClient
    import json

    client = ARBAClient(cache_dir=cache_dir)

    # Fetch the rule
    rule = client.fetch_rule(rule_id)

    if not rule:
        typer.echo(f"Rule {rule_id} not found", err=True)
        raise typer.Exit(code=1)

    if json_output:
        typer.echo(json.dumps(rule.to_json(), indent=2))
    else:
        typer.echo(f"Rule: {rule.uni_rule_id}")
        typer.echo(f"Version: {rule.version}")
        typer.echo(f"Created: {rule.created_date}")
        typer.echo(f"Modified: {rule.modified_date}")
        typer.echo(f"Statistics:")
        typer.echo(f"  Reviewed proteins: {rule.statistics.reviewed_count}")
        typer.echo(f"  Unreviewed proteins: {rule.statistics.unreviewed_count}")

        # Show conditions
        typer.echo(f"\nConditions ({len(rule.condition_sets)} sets):")
        for i, cs in enumerate(rule.condition_sets, 1):
            typer.echo(f"  Set {i}:")
            for cond in cs.conditions:
                neg = "NOT " if cond.is_negative else ""
                values = ", ".join(cv.value for cv in cond.values)
                typer.echo(f"    {neg}{cond.condition_type}: {values}")

        # Show annotations
        typer.echo(f"\nAnnotations ({len(rule.annotations)}):")
        for ann in rule.annotations:
            if ann.keyword:
                typer.echo(f"  Keyword: {ann.keyword.name} ({ann.keyword.kw_id})")
            elif ann.db_reference:
                typer.echo(f"  {ann.db_reference.database}: {ann.db_reference.ref_id}")
            elif ann.reaction:
                typer.echo(f"  Catalytic activity: {ann.reaction.name}")
                if ann.reaction.ec_number:
                    typer.echo(f"    EC: {ann.reaction.ec_number}")
            elif ann.subcellular_location:
                typer.echo(f"  Subcellular location: {ann.subcellular_location.location}")
            elif ann.pathway:
                typer.echo(f"  Pathway: {ann.pathway}")
            elif ann.text:
                typer.echo(f"  {ann.comment_type}: {ann.text}")


@app.command()
def arba_search(
    query: Annotated[
        str,
        typer.Argument(help="Search query (e.g., 'ec:2.3.2.5', 'keyword:transport')"),
    ],
    limit: Annotated[
        int,
        typer.Option("--limit", "-l", help="Maximum number of results"),
    ] = 25,
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", "-d", help="Cache directory for ARBA rules"),
    ] = Path("rules/arba"),
):
    """Search ARBA rules using the UniProt API.

    Examples:
        ai-gene-review arba-search "ec:2.3.2.5"
        ai-gene-review arba-search "keyword:transport" --limit 50
        ai-gene-review arba-search "cc_subcellular_location:membrane"
    """
    from ai_gene_review.etl.arba import ARBAClient

    client = ARBAClient(cache_dir=cache_dir)

    typer.echo(f"Searching ARBA rules for: {query}")

    rules, next_cursor = client.search(query=query, size=limit)

    if not rules:
        typer.echo("No rules found matching query")
        return

    typer.echo(f"\nFound {len(rules)} rules:")
    for rule in rules:
        # Get first annotation summary
        ann_summary = ""
        if rule.annotations:
            ann = rule.annotations[0]
            if ann.keyword:
                ann_summary = f"Keyword: {ann.keyword.name}"
            elif ann.reaction:
                ec = f" (EC {ann.reaction.ec_number})" if ann.reaction.ec_number else ""
                ann_summary = f"Catalytic activity{ec}"
            elif ann.subcellular_location:
                ann_summary = f"Location: {ann.subcellular_location.location}"

        typer.echo(f"  {rule.uni_rule_id}: {ann_summary} [{rule.statistics.total_count} proteins]")

    if next_cursor:
        typer.echo(f"\n(More results available, increase --limit to see more)")


# ============== UniRule Commands ==============


@app.command()
def unirule_sync(
    query: Annotated[
        str,
        typer.Option("--query", "-q", help="Search query (default: all rules)"),
    ] = "*",
    batch_size: Annotated[
        int,
        typer.Option("--batch-size", "-b", help="Number of rules per API request"),
    ] = 500,
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", "-d", help="Cache directory for UniRule rules"),
    ] = Path("rules/unirule"),
    limit: Annotated[
        Optional[int],
        typer.Option("--limit", "-l", help="Maximum number of rules to fetch (for testing)"),
    ] = None,
    go_only: Annotated[
        bool,
        typer.Option("--go-only/--all", help="Only sync rules with GO annotations (default: GO only)"),
    ] = True,
):
    """Sync UniRule (expert-curated annotation rules) from UniProt.

    Downloads and caches UniRules locally for offline access and analysis.
    By default, only syncs rules that have GO term annotations.

    Examples:
        # Sync UniRules with GO annotations (default)
        ai-gene-review unirule-sync

        # Sync ALL UniRules (about 9,500 rules)
        ai-gene-review unirule-sync --all

        # Test with a small batch
        ai-gene-review unirule-sync --limit 10
    """
    from ai_gene_review.etl.unirule import UniRuleClient

    client = UniRuleClient(cache_dir=cache_dir)

    total = client.get_total_count()
    typer.echo(f"Total UniRules available: {total}")

    if go_only:
        typer.echo("Filtering for rules with GO annotations only")

    if limit:
        typer.echo(f"Limiting to {limit} matched rules (for testing)")

    def progress(fetched: int, total_available: int, matched: int) -> None:
        pct = (fetched / total_available) * 100 if total_available > 0 else 0
        typer.echo(f"  Scanned: {fetched}/{total_available} ({pct:.1f}%) | Matched: {matched}", nl=False)
        typer.echo("\r", nl=False)

    typer.echo(f"Syncing UniRules to {cache_dir}...")

    count = 0
    for rule in client.iter_all_rules(
        query=query,
        batch_size=batch_size,
        cache=True,
        go_only=go_only,
        progress_callback=progress
    ):
        count += 1
        if limit and count >= limit:
            break

    typer.echo(f"\n✓ Synced {count} UniRules to {cache_dir}")


@app.command()
def unirule_stats(
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", "-d", help="Cache directory for UniRule rules"),
    ] = Path("rules/unirule"),
):
    """Show statistics about the local UniRule cache."""
    from ai_gene_review.etl.unirule import UniRuleClient

    client = UniRuleClient(cache_dir=cache_dir)

    if not cache_dir.exists():
        typer.echo(f"No UniRule cache found at {cache_dir}")
        typer.echo("Run 'ai-gene-review unirule-sync' to download rules")
        return

    stats = client.get_cache_stats()

    typer.echo(f"UniRule Cache Statistics ({cache_dir}):")
    typer.echo(f"  Cached rules: {stats['cached_rules']}")
    typer.echo(f"  Cache size: {stats['cache_size_mb']} MB")

    meta_file = cache_dir / "_metadata.json"
    if meta_file.exists():
        import json
        metadata = json.loads(meta_file.read_text())
        typer.echo(f"  Last sync: {metadata.get('last_sync', 'unknown')}")


@app.command()
def unirule_lookup(
    rule_id: Annotated[
        str,
        typer.Argument(help="UniRule ID (e.g., UR000000070)"),
    ],
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", "-d", help="Cache directory for UniRule rules"),
    ] = Path("rules/unirule"),
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
):
    """Look up a specific UniRule by ID."""
    from ai_gene_review.etl.unirule import UniRuleClient
    import json

    client = UniRuleClient(cache_dir=cache_dir)
    rule = client.fetch_rule(rule_id)

    if not rule:
        typer.echo(f"Rule {rule_id} not found", err=True)
        raise typer.Exit(code=1)

    if json_output:
        typer.echo(json.dumps(rule.to_json(), indent=2))
    else:
        typer.echo(f"Rule: {rule.uni_rule_id}")
        typer.echo(f"Version: {rule.info.version}")
        if rule.info.old_rule_num:
            typer.echo(f"Old Rule: {rule.info.old_rule_num}")
        if rule.info.data_class:
            typer.echo(f"Data Class: {rule.info.data_class}")
        typer.echo(f"Created: {rule.created_date}")
        typer.echo(f"Modified: {rule.modified_date}")
        typer.echo(f"Statistics:")
        typer.echo(f"  Reviewed proteins: {rule.statistics.reviewed_count}")
        typer.echo(f"  Unreviewed proteins: {rule.statistics.unreviewed_count}")

        typer.echo(f"\nConditions ({len(rule.condition_sets)} sets):")
        for i, cs in enumerate(rule.condition_sets, 1):
            typer.echo(f"  Set {i}:")
            for cond in cs.conditions:
                neg = "NOT " if cond.is_negative else ""
                values = ", ".join(cv.value for cv in cond.values)
                typer.echo(f"    {neg}{cond.condition_type}: {values}")

        typer.echo(f"\nAnnotations ({len(rule.annotations)}):")
        for ann in rule.annotations:
            if ann.keyword:
                typer.echo(f"  Keyword: {ann.keyword.name} ({ann.keyword.kw_id})")
            elif ann.db_reference:
                typer.echo(f"  {ann.db_reference.database}: {ann.db_reference.ref_id}")
            elif ann.reaction:
                typer.echo(f"  Catalytic activity: {ann.reaction.name}")
                if ann.reaction.ec_number:
                    typer.echo(f"    EC: {ann.reaction.ec_number}")
            elif ann.subcellular_location:
                typer.echo(f"  Subcellular location: {ann.subcellular_location.location}")
            elif ann.pathway:
                typer.echo(f"  Pathway: {ann.pathway}")
            elif ann.text:
                typer.echo(f"  {ann.comment_type}: {ann.text}")


@app.command()
def rules_enrich(
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", "-d", help="Cache directory for rules"),
    ] = Path("rules"),
    rule_type: Annotated[
        str,
        typer.Option("--type", "-t", help="Rule type to enrich: arba, unirule, or all"),
    ] = "all",
    limit: Annotated[
        Optional[int],
        typer.Option("--limit", "-l", help="Maximum number of rules to enrich (for testing)"),
    ] = None,
    force: Annotated[
        bool,
        typer.Option("--force", "-f", help="Force re-enrich even if .enriched.json exists"),
    ] = False,
):
    """Enrich cached rules with labels for GO terms, InterPro, FunFam, and taxa.

    This command processes cached rules and adds human-readable labels for:
    - GO terms (from QuickGO API)
    - InterPro entries (from InterPro API)
    - CATH FunFam families (from CATH API)
    - Taxa (normalized to NCBITaxon CURIEs)

    Enriched rules are saved to separate .enriched.json files, preserving originals:
    - ARBA00001.json          (original from API)
    - ARBA00001.enriched.json (with labels added)

    Examples:
        # Enrich all cached rules
        ai-gene-review rules-enrich

        # Enrich only ARBA rules
        ai-gene-review rules-enrich --type arba

        # Enrich only UniRules
        ai-gene-review rules-enrich --type unirule

        # Test with a few rules
        ai-gene-review rules-enrich --limit 10

        # Force re-enrich existing
        ai-gene-review rules-enrich --force
    """
    import json
    from ai_gene_review.etl.rule_enrichment import LabelEnricher, enrich_rule_json

    enricher = LabelEnricher(cache_dir=cache_dir)

    # Determine which directories to process
    dirs_to_process = []
    if rule_type in ("arba", "all"):
        arba_dir = cache_dir / "arba"
        if arba_dir.exists():
            # Match original files, exclude .enriched.json
            dirs_to_process.append(("ARBA", arba_dir, "ARBA*/ARBA*.json", ".enriched.json"))
    if rule_type in ("unirule", "all"):
        unirule_dir = cache_dir / "unirule"
        if unirule_dir.exists():
            dirs_to_process.append(("UniRule", unirule_dir, "UR*/UR*.json", ".enriched.json"))

    if not dirs_to_process:
        typer.echo(f"No rules found in {cache_dir}")
        raise typer.Exit(1)

    total_enriched = 0
    total_skipped = 0

    for name, rule_dir, pattern, enriched_suffix in dirs_to_process:
        typer.echo(f"\nProcessing {name} rules in {rule_dir}...")
        # Get original files (exclude .enriched.json)
        rule_files = sorted(
            f for f in rule_dir.glob(pattern)
            if not f.name.endswith(enriched_suffix)
        )
        count = len(rule_files)

        if limit:
            rule_files = rule_files[:limit]
            typer.echo(f"  Limiting to {limit} rules (of {count} total)")

        for i, rule_file in enumerate(rule_files, 1):
            # Determine output file path
            enriched_file = rule_file.with_suffix(".enriched.json")

            # Skip if already enriched (unless --force)
            if enriched_file.exists() and not force:
                total_skipped += 1
                continue

            # Load rule JSON
            rule_json = json.loads(rule_file.read_text())

            # Enrich
            enriched = enrich_rule_json(rule_json, enricher)

            # Save to separate file
            enriched_file.write_text(json.dumps(enriched, indent=2))

            if i % 100 == 0 or i == len(rule_files):
                typer.echo(f"  Enriched {i}/{len(rule_files)} rules", nl=False)
                typer.echo("\r", nl=False)

            total_enriched += 1

        typer.echo(f"\n  Completed {name}: {total_enriched} enriched, {total_skipped} skipped")

    typer.echo(f"\nTotal: {total_enriched} rules enriched, {total_skipped} skipped (already exist)")

    # Show cache stats
    typer.echo(f"\nLabel cache saved to {cache_dir / '_labels.json'}")


@app.command()
def rules_export(
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", "-d", help="Cache directory for rules"),
    ] = Path("rules"),
    output: Annotated[
        Path,
        typer.Option("--output", "-o", help="Output CSV file path"),
    ] = Path("rules/rules-export.csv"),
    rule_type: Annotated[
        str,
        typer.Option("--type", "-t", help="Rule type to export: arba, unirule, or all"),
    ] = "all",
    enriched: Annotated[
        bool,
        typer.Option("--enriched/--raw", help="Use enriched files with labels (default: enriched)"),
    ] = True,
):
    """Export rules to CSV with one row per condition set.

    Creates a flat CSV with pivoted condition columns (term1_*, term2_*, term3_*)
    and denormalized GO annotations. Each row represents a single conjunctive
    clause (AND of conditions) from the DNF rule structure.

    Requires running `rules-enrich` first if using --enriched (default).

    Examples:
        # Export all rules to default location
        ai-gene-review rules-export

        # Export only ARBA rules
        ai-gene-review rules-export --type arba

        # Export to custom path
        ai-gene-review rules-export -o my-export.csv

        # Export raw (un-enriched) files
        ai-gene-review rules-export --raw
    """
    from ai_gene_review.etl.rule_export import export_rules_to_csv, create_go_summary

    if enriched:
        typer.echo("Using enriched files (run `just rules-enrich` first if labels are missing)")
    else:
        typer.echo("Using raw files (labels will be empty)")

    def progress(rules: int, rows: int) -> None:
        typer.echo(f"  Processed {rules} rules, {rows} rows written", nl=False)
        typer.echo("\r", nl=False)

    typer.echo(f"Exporting {rule_type} rules from {cache_dir} to {output}...")

    rows = export_rules_to_csv(
        cache_dir=cache_dir,
        output_path=output,
        rule_type=rule_type,
        use_enriched=enriched,
        progress_callback=progress
    )

    typer.echo(f"\n✓ Exported {rows} rows to {output}")

    # Create GO summary
    typer.echo("Creating GO summary...")
    summary_path = create_go_summary(output)
    typer.echo(f"✓ GO summary written to {summary_path}")


@app.command()
def rules_validate(
    files: Annotated[
        Optional[list[Path]],
        typer.Argument(help="Rule review YAML file(s) to validate (or use --all)"),
    ] = None,
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", "-d", help="Cache directory for rules"),
    ] = Path("rules"),
    all_reviews: Annotated[
        bool,
        typer.Option("--all", "-a", help="Validate all *-review.yaml files in cache directory"),
    ] = False,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Show detailed messages including warnings"),
    ] = False,
):
    """Validate rule review YAML files against the LinkML schema.

    Validates RuleReview files including:
    - Schema compliance (RuleReview class)
    - PMID title verification (catches hallucinated references)

    Examples:
        # Validate a specific review
        ai-gene-review rules-validate rules/arba/ARBA00026249/ARBA00026249-review.yaml

        # Validate all reviews in the rules directory
        ai-gene-review rules-validate --all

        # Validate with verbose output
        ai-gene-review rules-validate --all -v
    """
    from ai_gene_review.validation.validator import validate_rule_review

    # Collect files to validate
    all_files: list[Path] = []

    if all_reviews:
        # Find all *-review.yaml files in cache_dir
        for review_file in cache_dir.rglob("*-review.yaml"):
            all_files.append(review_file)
        if not all_files:
            typer.echo(f"No review files found in {cache_dir}", err=True)
            raise typer.Exit(code=1)
        typer.echo(f"Found {len(all_files)} review file(s) to validate")
    elif files:
        all_files = list(files)
    else:
        typer.echo("Please specify file(s) or use --all to validate all reviews", err=True)
        raise typer.Exit(code=1)

    # Track results
    valid_count = 0
    invalid_count = 0

    for yaml_file in all_files:
        report = validate_rule_review(yaml_file)

        if report.is_valid:
            valid_count += 1
            if verbose:
                typer.echo(f"✓ {yaml_file}")
        else:
            invalid_count += 1
            typer.echo(f"✗ {yaml_file}", err=True)
            for issue in report.issues:
                typer.echo(f"  {issue}", err=True)

    # Summary
    typer.echo()
    if invalid_count == 0:
        typer.echo(f"✓ All {valid_count} review(s) valid")
    else:
        typer.echo(f"✗ {invalid_count} invalid, {valid_count} valid", err=True)
        raise typer.Exit(code=1)


@app.command()
def rules_sync(
    files: Annotated[
        Optional[list[Path]],
        typer.Argument(help="Rule review YAML file(s) to sync (or use --all)"),
    ] = None,
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", "-d", help="Cache directory for rules"),
    ] = Path("rules"),
    all_reviews: Annotated[
        bool,
        typer.Option("--all", "-a", help="Sync all *-review.yaml files in cache directory"),
    ] = False,
    rule_type: Annotated[
        str,
        typer.Option("--rule-type", "-t", help="Rule type to sync (arba, unirule, or all)"),
    ] = "all",
    containment_threshold: Annotated[
        float,
        typer.Option("--threshold", help="Minimum containment_a_in_b for global_pairwise_overlap"),
    ] = 0.8,
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", help="Show what would be updated without writing files"),
    ] = False,
):
    """Sync rule review YAML files with analysis data.

    Updates review YAML files with:
    - pairwise_overlap sections for each condition set
    - global_pairwise_overlap at rule level (filtered by containment threshold)

    Examples:
        # Sync a specific review
        ai-gene-review rules-sync rules/arba/ARBA00026249/ARBA00026249-review.yaml

        # Sync all ARBA reviews
        ai-gene-review rules-sync --all --rule-type arba

        # Dry run to preview changes
        ai-gene-review rules-sync --all --dry-run
    """
    from ai_gene_review.etl.rule_review_sync import sync_review_with_analysis, sync_all_reviews

    if all_reviews:
        # Sync all reviews
        typer.echo(f"Syncing all {rule_type} reviews in {cache_dir}...")
        stats = sync_all_reviews(
            cache_dir,
            rule_type=rule_type,
            containment_threshold=containment_threshold,
            dry_run=dry_run
        )

        typer.echo()
        typer.echo(f"Reviews processed: {stats['reviews_processed']}")
        typer.echo(f"Reviews updated: {stats['reviews_updated']}")
        typer.echo(f"Reviews skipped: {stats['reviews_skipped']}")
        typer.echo(f"Condition sets updated: {stats['total_condition_sets_updated']}")
        typer.echo(f"Global pairs added: {stats['total_global_pairs_added']}")

        if dry_run:
            typer.echo("\n(dry run - no files written)")
    elif files:
        # Sync specific files
        for yaml_file in files:
            typer.echo(f"Syncing {yaml_file}...")
            stats = sync_review_with_analysis(
                yaml_file,
                containment_threshold=containment_threshold,
                dry_run=dry_run
            )

            if stats['status'] == 'updated':
                typer.echo(f"  ✓ Updated {stats['condition_sets_updated']} condition set(s)")
                typer.echo(f"  ✓ Added {stats['global_pairs_added']} global pair(s)")
            elif stats['status'] == 'skipped':
                typer.echo(f"  ⊘ Skipped: {stats['reason']}")

            if dry_run:
                typer.echo("  (dry run - no files written)")
    else:
        typer.echo("Please specify file(s) or use --all to sync all reviews", err=True)
        raise typer.Exit(code=1)


def main():
    """Main entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
