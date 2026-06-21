"""CLI interface for ai-gene-review."""

import re
import shlex
import shutil
import subprocess
import time
from pathlib import Path
from typing import List, Optional

import typer
from typing_extensions import Annotated

from linkml_data_qc.analyzer import ComplianceAnalyzer

from ai_gene_review.etl.gene import fetch_gene_data, fetch_gene_data_ncRNA, expand_organism_name
from ai_gene_review.etl.publication import (
    cache_publications,
    convert_doi_publication,
    doi_to_pmid,
    extract_pmids_from_yaml,
)
from ai_gene_review.etl.publication_refresh import (
    find_pmc_candidates,
    refetch_publications,
    get_refresh_summary,
    find_active_review_pmids,
)
from ai_gene_review.validation import (
    BatchValidationReport,
    ValidationReport,
    validate_gene_review,
    ValidationSeverity,
)
from ai_gene_review.validation.goa_validator import GOAValidator
from ai_gene_review.validation.validator import get_project_root, get_schema_path
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


def _tool_command(command_name: str) -> list[str]:
    """Return a command prefix for an installed validation CLI."""
    resolved = shutil.which(command_name)
    if resolved:
        return [resolved]

    uv = shutil.which("uv")
    if uv:
        return [uv, "run", command_name]

    return [command_name]


def _summarize_validator_output(output: str, max_chars: int = 1800) -> str:
    """Keep the actionable lines from external validator output."""
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    if not lines:
        return "no output"

    interesting = [
        line
        for line in lines
        if re.search(
            r"error|warn|mismatch|required|not of type|additional propert"
            r"|invalid|failed|not valid|not found",
            line,
            re.IGNORECASE,
        )
    ]
    selected = interesting or lines[-8:]
    summary = "; ".join(selected)
    if len(summary) > max_chars:
        return summary[: max_chars - 3] + "..."
    return summary


def _warning_lines(output: str) -> list[str]:
    # Matches both the linkml-reference-validator "[WARN]" / leading "WARN" style
    # and the linkml-term-validator "⚠️  WARN:" emoji style (ontology label drift).
    return [
        line.strip()
        for line in output.splitlines()
        if re.search(r"(^|\[)(WARN|WARNING)\b", line.strip(), re.IGNORECASE)
        or "⚠" in line
    ]


def _has_error_output(output: str) -> bool:
    # "❌ ERROR" is the linkml-term-validator error marker; the "❌ ... issue(s):"
    # header (also emitted for warning-only results) intentionally does not match.
    return bool(
        re.search(
            r"^\s*\[ERROR\]|❌\s*ERROR|Traceback|^Error:",
            output,
            re.IGNORECASE | re.MULTILINE,
        )
    )


def _run_validation_command(
    report: ValidationReport,
    phase: str,
    command: list[str],
    validation_category: str,
    check_type: str,
    cwd: Path,
    show_timing: bool = False,
) -> None:
    start = time.perf_counter()
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        report.add_issue(
            ValidationSeverity.ERROR,
            f"{phase} command not found: {command[0]}",
            path=str(report.file_path) if report.file_path else None,
            validation_category=validation_category,
            check_type=check_type,
        )
        return

    output = "\n".join(
        part for part in [completed.stdout, completed.stderr] if part
    ).strip()
    command_text = " ".join(shlex.quote(part) for part in command)
    details = {
        "command": command_text,
        "return_code": completed.returncode,
        "output": output,
    }

    warnings = _warning_lines(output)

    has_error_output = _has_error_output(output)

    if completed.returncode != 0 and (has_error_output or not warnings):
        report.add_issue(
            ValidationSeverity.ERROR,
            f"{phase} failed: {_summarize_validator_output(output)}",
            path=str(report.file_path) if report.file_path else None,
            details=details,
            validation_category=validation_category,
            check_type=check_type,
        )
    elif has_error_output:
        report.add_issue(
            ValidationSeverity.WARNING,
            f"{phase} reported error-like output despite exit code 0: {_summarize_validator_output(output)}",
            path=str(report.file_path) if report.file_path else None,
            details=details,
            validation_category=validation_category,
            check_type=check_type,
        )
    else:
        if warnings:
            report.add_issue(
                ValidationSeverity.WARNING,
                f"{phase} reported warnings: {_summarize_validator_output(chr(10).join(warnings))}",
                path=str(report.file_path) if report.file_path else None,
                details=details,
                validation_category=validation_category,
                check_type=check_type,
            )

    if show_timing:
        typer.echo(f"  {phase}: {time.perf_counter() - start:.2f}s")


def _merge_report(target: ValidationReport, source: ValidationReport) -> None:
    target.issues.extend(source.issues)
    if source.has_errors:
        target.is_valid = False


def _validate_gene_review_cli(
    yaml_file: Path,
    schema_path: Path,
    check_best_practices: bool,
    check_goa: bool,
    check_references: bool,
    check_schema: bool,
    check_terms: bool,
    show_timing: bool = False,
) -> ValidationReport:
    yaml_file = yaml_file.resolve()
    schema_path = schema_path.resolve()
    report = ValidationReport(file_path=yaml_file, is_valid=True)

    if not yaml_file.exists():
        report.add_issue(
            ValidationSeverity.ERROR,
            f"File not found: {yaml_file}",
            path=None,
            validation_category="FileValidator",
            check_type="file_exists",
        )
        return report

    project_root = get_project_root()

    if check_schema:
        _run_validation_command(
            report,
            "Schema validation",
            [
                *_tool_command("linkml-validate"),
                "--schema",
                str(schema_path),
                "--target-class",
                "GeneReview",
                str(yaml_file),
            ],
            "SchemaValidator",
            "linkml_validate",
            cwd=project_root,
            show_timing=show_timing,
        )

    if check_terms:
        term_wrapper = project_root / "scripts" / "run_term_validator.sh"
        oak_config = project_root / "conf" / "oak_config.yaml"
        term_command = (
            [str(term_wrapper)]
            if term_wrapper.exists()
            else _tool_command("linkml-term-validator")
        )
        command = [
            *term_command,
            "validate-data",
            str(yaml_file),
            "-s",
            str(schema_path),
            "-t",
            "GeneReview",
            "--labels",
        ]
        if oak_config.exists():
            command.extend(["-c", str(oak_config)])
        _run_validation_command(
            report,
            "Term validation",
            command,
            "TermValidator",
            "linkml_term_validator",
            cwd=project_root,
            show_timing=show_timing,
        )

    if check_references:
        reference_wrapper = project_root / "scripts" / "run_reference_validator.sh"
        reference_config = project_root / "conf" / "reference_validator_config.yaml"
        reference_command = (
            [str(reference_wrapper)]
            if reference_wrapper.exists()
            else _tool_command("linkml-reference-validator")
        )
        command = [
            *reference_command,
            "validate",
            "data",
            str(yaml_file),
            "--schema",
            str(schema_path),
            "--target-class",
            "GeneReview",
        ]
        if reference_config.exists():
            command.extend(["--config", str(reference_config)])
        _run_validation_command(
            report,
            "Reference validation",
            command,
            "ReferenceValidator",
            "linkml_reference_validator",
            cwd=project_root,
            show_timing=show_timing,
        )

    if check_best_practices:
        try:
            best_practices_report = validate_gene_review(
                yaml_file,
                schema_path,
                check_best_practices=True,
                check_goa=check_goa,
                check_supporting_text=check_references,
            )
            _merge_report(report, best_practices_report)
        except Exception as e:
            report.add_issue(
                ValidationSeverity.ERROR,
                f"Best practices validation failed: {e}",
                path=str(yaml_file),
                validation_category="BestPracticeValidator",
                check_type="custom_rules",
            )

    return report


def _validate_multiple_files_cli(
    yaml_files: list[Path],
    schema_path: Path,
    check_best_practices: bool,
    check_goa: bool,
    check_references: bool,
    check_schema: bool,
    check_terms: bool,
    show_progress: bool = False,
    show_timing: bool = False,
) -> BatchValidationReport:
    batch_report = BatchValidationReport()

    if show_progress and len(yaml_files) > 1:
        from rich.progress import (
            BarColumn,
            Progress,
            SpinnerColumn,
            TaskProgressColumn,
            TextColumn,
            TimeElapsedColumn,
        )

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            console=None,
        ) as progress:
            main_task = progress.add_task("Validating files...", total=len(yaml_files))

            for yaml_file in yaml_files:
                progress.update(main_task, description=f"Validating {yaml_file.name}")
                batch_report.reports.append(
                    _validate_gene_review_cli(
                        yaml_file,
                        schema_path,
                        check_best_practices,
                        check_goa,
                        check_references,
                        check_schema,
                        check_terms,
                        show_timing=show_timing,
                    )
                )
                progress.advance(main_task)
    else:
        for yaml_file in yaml_files:
            batch_report.reports.append(
                _validate_gene_review_cli(
                    yaml_file,
                    schema_path,
                    check_best_practices,
                    check_goa,
                    check_references,
                    check_schema,
                    check_terms,
                    show_timing=show_timing,
                )
            )

    return batch_report


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
    no_schema: Annotated[
        bool, typer.Option("--no-schema", help="Skip LinkML schema validation")
    ] = False,
    terms: Annotated[
        bool,
        typer.Option(
            "--terms",
            help="Run ontology term/label validation with linkml-term-validator",
        ),
    ] = False,
    no_goa: Annotated[
        bool, typer.Option("--no-goa", help="Skip GOA validation")
    ] = False,
    no_references: Annotated[
        bool,
        typer.Option(
            "--no-references",
            "--no-supporting-text",
            help="Skip reference title and supporting_text validation",
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
    """Validate gene review YAML files.

    By default this runs strict LinkML schema validation, reference validation
    for publication titles and supporting_text snippets, and custom
    best-practices checks. Use --terms to also run ontology term/label
    validation.

    Examples:
        ai-gene-review validate genes/human/CFAP300/CFAP300-ai-review.yaml
        ai-gene-review validate genes/human/*/*.yaml
        ai-gene-review validate test.yaml --schema custom_schema.yaml --verbose
        ai-gene-review validate test.yaml --terms
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
    check_references = not no_references
    check_schema = not no_schema
    schema_path = Path(schema).resolve() if schema else get_schema_path()

    # Validate single file or multiple files
    if len(all_files) == 1:
        yaml_file = all_files[0]
        typer.echo(f"Validating {yaml_file}...")

        report = _validate_gene_review_cli(
            yaml_file,
            schema_path,
            check_best_practices,
            check_goa,
            check_references,
            check_schema,
            terms,
            show_timing=show_timing,
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

        batch_report = _validate_multiple_files_cli(
            all_files,
            schema_path,
            check_best_practices,
            check_goa,
            check_references,
            check_schema,
            terms,
            show_progress=True,  # Enable progress bar for multiple files
            show_timing=show_timing,
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


@app.command()
def compliance(
    yaml_files: Annotated[list[Path], typer.Argument(help="YAML file(s) to analyze")],
    schema: Annotated[
        Optional[Path],
        typer.Option(
            "--schema",
            "-s",
            help="Path to LinkML schema (uses default if not provided)",
        ),
    ] = None,
    tsv_output: Annotated[
        Optional[Path],
        typer.Option(
            "--tsv-output",
            help="Output compliance results to TSV file (default: stdout)",
        ),
    ] = None,
):
    """Analyze recommended-field compliance using linkml-data-qc."""
    all_files: list[Path] = []
    for pattern in yaml_files:
        if "*" in str(pattern):
            from glob import glob

            matched = glob(str(pattern), recursive=True)
            all_files.extend(
                [Path(f) for f in matched if f.endswith(".yaml") or f.endswith(".yml")]
            )
        else:
            all_files.append(pattern)

    if not all_files:
        typer.echo("No files found to analyze", err=True)
        raise typer.Exit(code=1)

    schema_path = schema or get_schema_path()
    analyzer = ComplianceAnalyzer(str(schema_path))

    rows: list[tuple[str, str, str, str]] = []
    for yaml_file in all_files:
        report = analyzer.analyze_file(str(yaml_file), "GeneReview")
        for path_score in report.path_scores:
            for slot_score in path_score.slot_scores:
                if slot_score.populated == 0:
                    if path_score.path == "(root)":
                        slot_path = slot_score.slot_name
                    else:
                        slot_path = f"{path_score.path}.{slot_score.slot_name}"
                    rows.append(
                        (
                            str(yaml_file),
                            slot_path,
                            slot_score.slot_name,
                            path_score.parent_class,
                        )
                    )

    output_lines = ["file_path\tpath\tslot_name\tparent_class"]
    output_lines.extend("\t".join(row) for row in rows)

    if tsv_output:
        tsv_output.parent.mkdir(parents=True, exist_ok=True)
        tsv_output.write_text("\n".join(output_lines) + "\n")
    else:
        typer.echo("\n".join(output_lines))


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
def backfill_isoforms(
    yaml_file: Annotated[Path, typer.Argument(help="Gene review YAML file to update")],
    goa_file: Annotated[
        Optional[Path],
        typer.Option(
            "--goa", "-g", help="GOA TSV file (auto-detected if not provided)"
        ),
    ] = None,
    dry_run: Annotated[
        bool,
        typer.Option(
            "--dry-run", help="Show what would be updated without modifying files"
        ),
    ] = False,
):
    """Backfill isoform field on existing annotations from GOA data.

    This migration command adds the 'isoform' field to existing annotations
    that match isoform-specific annotations in the GOA file. It does NOT
    modify annotations that already have an isoform field.

    Use this to update existing gene reviews after the isoform tracking
    feature was added.

    Examples:
        ai-gene-review backfill-isoforms genes/human/WT1/WT1-ai-review.yaml
        ai-gene-review backfill-isoforms test.yaml --goa custom-goa.tsv
        ai-gene-review backfill-isoforms test.yaml --dry-run  # Preview changes
    """
    yaml_file = Path(yaml_file)

    if not yaml_file.exists():
        typer.echo(f"Error: YAML file not found: {yaml_file}", err=True)
        raise typer.Exit(code=1)

    # Initialize validator
    validator = GOAValidator()

    if dry_run:
        # Just show what would be updated
        try:
            goa_path = goa_file
            if goa_path is None:
                yaml_stem = yaml_file.stem
                if yaml_stem.endswith("-ai-review"):
                    gene_name = yaml_stem[:-10]
                    goa_path = yaml_file.parent / f"{gene_name}-goa.tsv"

            goa_annotations = validator.parse_goa_file(goa_path)
            isoform_anns = [a for a in goa_annotations if a.isoform]

            if not isoform_anns:
                typer.echo("No isoform-specific annotations found in GOA file")
                return

            typer.echo(f"Found {len(isoform_anns)} isoform-specific annotations in GOA:")
            for ann in isoform_anns:
                typer.echo(f"  {ann.go_id} ({ann.evidence_code}, {ann.reference}) -> {ann.isoform}")

            typer.echo("\nUse without --dry-run to apply these updates")
        except (ValueError, FileNotFoundError) as e:
            typer.echo(f"Error: {e}", err=True)
            raise typer.Exit(code=1)
        return

    try:
        updated_count, output_path = validator.backfill_isoforms(yaml_file, goa_file)

        if updated_count > 0:
            typer.echo(f"✓ Updated {updated_count} annotations with isoform info in {output_path}")
        else:
            typer.echo("✓ No annotations needed isoform updates")

    except (ValueError, FileNotFoundError) as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def backfill_qualifiers(
    yaml_file: Annotated[Path, typer.Argument(help="Gene review YAML file to update")],
    goa_file: Annotated[
        Optional[Path],
        typer.Option(
            "--goa", "-g", help="GOA TSV file (auto-detected if not provided)"
        ),
    ] = None,
    dry_run: Annotated[
        bool,
        typer.Option(
            "--dry-run", help="Show what would be updated without modifying files"
        ),
    ] = False,
):
    """Backfill GOA qualifier values on existing annotations from GOA data.

    Does NOT modify annotations that already have a qualifier field.

    Examples:
        ai-gene-review backfill-qualifiers genes/yeast/SET1/SET1-ai-review.yaml
        ai-gene-review backfill-qualifiers test.yaml --goa custom-goa.tsv
        ai-gene-review backfill-qualifiers test.yaml --dry-run
    """
    yaml_file = Path(yaml_file)

    if not yaml_file.exists():
        typer.echo(f"Error: YAML file not found: {yaml_file}", err=True)
        raise typer.Exit(code=1)

    validator = GOAValidator()

    if dry_run:
        try:
            goa_path = goa_file
            if goa_path is None:
                yaml_stem = yaml_file.stem
                if yaml_stem.endswith("-ai-review"):
                    gene_name = yaml_stem[:-10]
                    goa_path = yaml_file.parent / f"{gene_name}-goa.tsv"
                else:
                    typer.echo("Error: Could not derive GOA file path", err=True)
                    raise typer.Exit(code=1)

            goa_annotations = validator.parse_goa_file(goa_path)
            qualified = [
                (a, qualifier)
                for a in goa_annotations
                if (qualifier := validator._parse_qualifier(a.qualifier))
            ]
            if not qualified:
                typer.echo("No recognized qualifiers found in GOA file")
                return

            typer.echo(f"Found {len(qualified)} GOA annotations with recognized qualifiers:")
            for ann, qualifier in qualified:
                typer.echo(
                    f"  {qualifier} {ann.go_id} {ann.go_term} "
                    f"({ann.evidence_code}, {ann.reference})"
                )

            typer.echo("\nUse without --dry-run to apply these updates")
        except (ValueError, FileNotFoundError) as e:
            typer.echo(f"Error: {e}", err=True)
            raise typer.Exit(code=1)
        return

    try:
        updated_count, output_path = validator.backfill_qualifiers(yaml_file, goa_file)

        if updated_count > 0:
            typer.echo(f"Updated {updated_count} annotations with qualifier info in {output_path}")
        else:
            typer.echo("No annotations needed qualifier updates")

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
    from ai_gene_review.utils.pmid_utils import mark_invalid_pmids

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
def convert_doi_publications(
    publications_dir: Annotated[
        Path, typer.Option("--dir", help="Publications directory")
    ] = Path("publications"),
    dry_run: Annotated[
        bool, typer.Option("--dry-run", help="Show what would be converted without making changes")
    ] = False,
    delay: Annotated[
        float, typer.Option("--delay", "-d", help="Delay between DOI lookups in seconds")
    ] = 0.5,
):
    """Convert DOI-keyed publication files to PMID-keyed format.

    Finds all DOI_*.md files in the publications directory, resolves each DOI
    to a PMID via NCBI Entrez, and creates standard PMID-keyed files. The
    original DOI files are removed after successful conversion.

    Examples:
        ai-gene-review convert-doi-publications
        ai-gene-review convert-doi-publications --dry-run
        ai-gene-review convert-doi-publications --dir ./publications --delay 1.0
    """
    import time
    import yaml

    doi_files = sorted(publications_dir.glob("DOI_*.md"))

    if not doi_files:
        typer.echo("No DOI-keyed publication files found.")
        return

    typer.echo(f"Found {len(doi_files)} DOI-keyed publication files.")

    if dry_run:
        for f in doi_files:
            typer.echo(f"  Would convert: {f.name}")
        return

    converted = 0
    failed = 0
    skipped = 0

    for i, doi_file in enumerate(doi_files):
        if i > 0:
            time.sleep(delay)

        typer.echo(f"[{i + 1}/{len(doi_files)}] {doi_file.name}...")
        result = convert_doi_publication(doi_file, publications_dir)

        if result:
            converted += 1
        elif not doi_file.exists():
            # File was removed by conversion
            converted += 1
        else:
            # Check if it was skipped (PMID file exists) vs failed (no PMID found)
            content = doi_file.read_text()
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm = yaml.safe_load(parts[1])
                doi = fm.get("doi", "")
                resolved = doi_to_pmid(doi)
                if resolved and (publications_dir / f"PMID_{resolved}.md").exists():
                    skipped += 1
                else:
                    failed += 1
            else:
                failed += 1

    typer.echo(f"\nConversion complete: {converted} converted, {skipped} skipped (PMID exists), {failed} failed")


@app.command()
def refresh_publications_active(
    genes_dir: Annotated[
        Path, typer.Option("--genes-dir", help="Genes directory")
    ] = Path("genes"),
    publications_dir: Annotated[
        Path, typer.Option("--dir", help="Publications directory")
    ] = Path("publications"),
    force: Annotated[
        bool, typer.Option("--force", "-f", help="Force re-download even if cached")
    ] = False,
    delay: Annotated[
        float, typer.Option("--delay", "-d", help="Delay between requests")
    ] = 0.5,
    dry_run: Annotated[
        bool, typer.Option("--dry-run", help="Show what would be refreshed without fetching")
    ] = False,
):
    """Refresh publication stubs for genes under active review.

    Finds gene reviews with status IN_PROGRESS or DRAFT, collects all
    referenced PMIDs, and refreshes any that are missing or lack full text.

    Examples:
        ai-gene-review refresh-publications-active
        ai-gene-review refresh-publications-active --dry-run
        ai-gene-review refresh-publications-active --force --delay 1.0
    """
    typer.echo("Scanning for active gene reviews (IN_PROGRESS, DRAFT)...")

    result = find_active_review_pmids(genes_dir)

    if not result["reviews"]:
        typer.echo("No active reviews found.")
        return

    typer.echo(f"Found {len(result['reviews'])} active reviews with {len(result['pmids'])} unique PMIDs")

    for r in result["reviews"]:
        typer.echo(f"  {r['organism']}/{r['gene']} ({r['status']}) - {r['pmid_count']} PMIDs")

    if dry_run:
        missing = []
        stubs = []
        cached = []
        for pmid in result["pmids"]:
            pub_file = publications_dir / f"PMID_{pmid}.md"
            if not pub_file.exists():
                missing.append(pmid)
            elif force:
                stubs.append(pmid)
            else:
                content = pub_file.read_text()
                if "full_text_available: false" in content or "full_text_available: true" not in content:
                    stubs.append(pmid)
                else:
                    cached.append(pmid)

        typer.echo(f"\n  Missing (need fetch): {len(missing)}")
        typer.echo(f"  Stubs (need refresh): {len(stubs)}")
        typer.echo(f"  Cached (have full text): {len(cached)}")
        return

    success_count = cache_publications(result["pmids"], publications_dir, force, delay)
    typer.echo(f"\nRefreshed {success_count}/{len(result['pmids'])} publications for active reviews")


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
        visualizer.visualize_file(yaml_file)
        
        # Show statistics if requested
        if show_stats:
            import yaml as pyyaml
            from ai_gene_review.export.annotation_export import _dict_to_obj
            with open(yaml_file) as f:
                data = pyyaml.safe_load(f)
            gene_review = _dict_to_obj(data)
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
            typer.echo("\nRun without --dry-run to apply updates")

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
        typer.echo("Statistics:")
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
        typer.echo("\n(More results available, increase --limit to see more)")


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
        typer.echo("Statistics:")
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
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", help="Show what would be updated without writing files"),
    ] = False,
):
    """Sync rule review YAML files with analysis data.

    Updates review YAML files with:
    - pairwise_overlap sections for each condition set
    - entries section with entry-centric view of entities and relationships

    Also removes deprecated global_pairwise_overlap fields if present.

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
            dry_run=dry_run
        )

        typer.echo()
        typer.echo(f"Reviews processed: {stats['reviews_processed']}")
        typer.echo(f"Reviews updated: {stats['reviews_updated']}")
        typer.echo(f"Reviews skipped: {stats['reviews_skipped']}")
        typer.echo(f"Condition sets updated: {stats['total_condition_sets_updated']}")
        typer.echo(f"Entries generated: {stats['total_entries_generated']}")

        if dry_run:
            typer.echo("\n(dry run - no files written)")
    elif files:
        # Sync specific files
        for yaml_file in files:
            typer.echo(f"Syncing {yaml_file}...")
            stats = sync_review_with_analysis(
                yaml_file,
                dry_run=dry_run
            )

            if stats['status'] == 'updated':
                if stats.get('condition_sets_populated', 0) > 0:
                    typer.echo(f"  ✓ Populated {stats['condition_sets_populated']} condition set(s) from enriched.json")
                typer.echo(f"  ✓ Updated {stats['condition_sets_updated']} condition set(s)")
                typer.echo(f"  ✓ Generated {stats.get('entries_generated', 0)} entries")
            elif stats['status'] == 'skipped':
                typer.echo(f"  ⊘ Skipped: {stats['reason']}")

            if dry_run:
                typer.echo("  (dry run - no files written)")
    else:
        typer.echo("Please specify file(s) or use --all to sync all reviews", err=True)
        raise typer.Exit(code=1)


@app.command()
def render_projects(
    files: Annotated[
        Optional[List[Path]],
        typer.Argument(help="Project markdown file(s) to render"),
    ] = None,
    output_dir: Annotated[
        Path,
        typer.Option("--output-dir", "-o", help="Output directory for HTML files"),
    ] = Path("pages/projects"),
    genes_dir: Annotated[
        Path,
        typer.Option("--genes-dir", "-g", help="Genes directory for symbol index"),
    ] = Path("genes"),
    all_projects: Annotated[
        bool,
        typer.Option("--all", "-a", help="Render all project files in projects/"),
    ] = False,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Show detailed output including all warnings"),
    ] = False,
):
    """Render project markdown files to HTML with auto-linked gene symbols.

    Converts project markdown files (from projects/) to HTML, automatically
    linking gene symbols to their corresponding gene review pages.

    Gene symbols are detected using word boundaries and linked to:
    genes/{species}/{gene}/{gene}-ai-review.html

    For ambiguous symbols (same gene in multiple species), add a 'species'
    field to the markdown frontmatter to resolve:

        ---
        species: [human, mouse]
        ---

    Examples:
        # Render all projects
        ai-gene-review render-projects --all

        # Render a specific project
        ai-gene-review render-projects projects/FERROPTOSIS.md

        # Rendering projects/FOO.md also renders markdown under projects/FOO/
        # converts linked notebooks, and copies referenced local assets into
        # the mirrored output tree.

        # Render to custom output directory
        ai-gene-review render-projects --all -o docs/projects
    """
    from ai_gene_review.render_projects import (
        render_all_projects,
        render_project_bundle,
    )

    if all_projects:
        typer.echo("Rendering all project markdown files...")
        output_paths, warnings = render_all_projects(
            projects_dir=Path("projects"),
            output_dir=output_dir,
            genes_dir=genes_dir,
        )

        if verbose and warnings:
            typer.echo("\nAll warnings:")
            for warning in warnings:
                typer.echo(f"  - {warning}")

        typer.echo(f"\n✓ Rendered {len(output_paths)} projects to {output_dir}")

    elif files:
        total_warnings = []
        for md_file in files:
            if not md_file.exists():
                typer.echo(f"Error: File not found: {md_file}", err=True)
                continue

            try:
                output_paths, warnings = render_project_bundle(
                    md_file,
                    output_dir=output_dir,
                    genes_dir=genes_dir,
                    projects_dir=Path("projects"),
                )
                total_warnings.extend(warnings)
                rendered_pages = [
                    path for path in output_paths if path.suffix.lower() == ".html"
                ]
                copied_assets = [
                    path for path in output_paths if path.suffix.lower() != ".html"
                ]

                if warnings:
                    typer.echo(
                        f"✓ {md_file.name} -> {len(rendered_pages)} page(s), "
                        f"{len(copied_assets)} asset(s) ({len(warnings)} warnings)"
                    )
                    if verbose:
                        for w in warnings:
                            typer.echo(f"    - {w}")
                else:
                    typer.echo(
                        f"✓ {md_file.name} -> {len(rendered_pages)} page(s), "
                        f"{len(copied_assets)} asset(s)"
                    )

            except Exception as e:
                typer.echo(f"✗ {md_file.name}: {e}", err=True)

        if total_warnings and not verbose:
            typer.echo(f"\n{len(total_warnings)} warnings total (use --verbose to see all)")

    else:
        typer.echo("Please specify file(s) or use --all to render all projects", err=True)
        raise typer.Exit(code=1)


@app.command()
def render_modules(
    files: Annotated[
        Optional[List[Path]],
        typer.Argument(help="Module YAML file(s) to render"),
    ] = None,
    output_dir: Annotated[
        Path,
        typer.Option("--output-dir", "-o", help="Output directory for module HTML files"),
    ] = Path("pages/modules"),
    modules_dir: Annotated[
        Path,
        typer.Option("--modules-dir", "-m", help="Directory containing module YAML files"),
    ] = Path("modules"),
    all_modules: Annotated[
        bool,
        typer.Option("--all", "-a", help="Render all module YAML files in modules/"),
    ] = False,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Show detailed output including warnings"),
    ] = False,
):
    """Render module YAML files to HTML pages with an inline tree browser.

    Examples:
        # Render all modules and an index page
        ai-gene-review render-modules --all

        # Render a specific module
        ai-gene-review render-modules modules/gluconeogenesis.yaml
    """
    from ai_gene_review.render_modules import render_all_modules, render_module

    if all_modules:
        typer.echo("Rendering all module YAML files...")
        output_paths, warnings = render_all_modules(
            modules_dir=modules_dir,
            output_dir=output_dir,
        )

        if verbose and warnings:
            typer.echo("\nAll warnings:")
            for warning in warnings:
                typer.echo(f"  - {warning}")

        typer.echo(f"\nRendered {len(output_paths)} module page(s) to {output_dir}")
    elif files:
        total_warnings = []
        for module_file in files:
            if not module_file.exists():
                typer.echo(f"Error: File not found: {module_file}", err=True)
                continue

            try:
                output_path, warnings = render_module(
                    module_file,
                    output_dir=output_dir,
                    modules_dir=modules_dir,
                )
                total_warnings.extend(warnings)
                if warnings:
                    typer.echo(f"Rendered {module_file} -> {output_path} ({len(warnings)} warnings)")
                    if verbose:
                        for warning in warnings:
                            typer.echo(f"    - {warning}")
                else:
                    typer.echo(f"Rendered {module_file} -> {output_path}")
            except Exception as error:
                typer.echo(f"Error rendering {module_file}: {error}", err=True)

        if total_warnings and not verbose:
            typer.echo(f"\n{len(total_warnings)} warnings total (use --verbose to see all)")
    else:
        typer.echo("Please specify file(s) or use --all to render all modules", err=True)
        raise typer.Exit(code=1)


@app.command()
def render_module_notation(
    files: Annotated[
        Optional[List[Path]],
        typer.Argument(help="Module YAML file(s) to project into compact notation"),
    ] = None,
    output_dir: Annotated[
        Optional[Path],
        typer.Option(
            "--output-dir",
            "-o",
            help="Write <stem>-notation.txt per module here; if omitted, print to stdout",
        ),
    ] = None,
    modules_dir: Annotated[
        Path,
        typer.Option("--modules-dir", "-m", help="Directory containing module YAML files"),
    ] = Path("modules"),
    all_modules: Annotated[
        bool,
        typer.Option("--all", "-a", help="Project all module YAML files in modules/"),
    ] = False,
):
    """Project module YAML into a compact, human-readable symbol notation.

    This is a read-only view of the canonical YAML: a legend mapping short symbols
    to grounded entities (GO/ChEBI), a reactions block, and a regulation block in
    which the arrow encodes sign (-o activation, -| inhibition) and the bracketed
    tag encodes the SBO-grounded mechanism (competitive vs allosteric).

    Examples:
        # Print one module's notation to stdout
        ai-gene-review render-module-notation modules/methionine_cycle.yaml

        # Write notation files for every module
        ai-gene-review render-module-notation --all -o pages/modules
    """
    from ai_gene_review.module_notation import render_module_notation_file
    from ai_gene_review.render_modules import iter_module_files

    if all_modules:
        targets = iter_module_files(modules_dir)
    elif files:
        targets = list(files)
    else:
        typer.echo("Please specify file(s) or use --all", err=True)
        raise typer.Exit(code=1)

    for module_file in targets:
        if not module_file.exists():
            typer.echo(f"Error: File not found: {module_file}", err=True)
            continue
        notation = render_module_notation_file(module_file)
        if output_dir is None:
            typer.echo(notation)
        else:
            output_dir.mkdir(parents=True, exist_ok=True)
            out_path = output_dir / f"{module_file.stem}-notation.txt"
            out_path.write_text(notation)
            typer.echo(f"Wrote {module_file} -> {out_path}")


@app.command()
def compare_module_regulation(
    module_file: Annotated[
        Path, typer.Argument(help="Curated module YAML (e.g. modules/methionine_cycle.yaml)")
    ],
    maud_toml: Annotated[
        Path, typer.Argument(help="Maud model TOML to ingest as a regulatory source")
    ],
    mapping: Annotated[
        Optional[Path],
        typer.Option("--mapping", "-m", help="Reviewed id-mapping (source ids -> module symbols)"),
    ] = None,
    emit_candidates: Annotated[
        bool,
        typer.Option(
            "--emit-candidates",
            help="Also print source edges as candidate module connections (YAML)",
        ),
    ] = False,
):
    """Diff a curated module's regulation against a Maud model's regulatory tables.

    Reduces both sides to canonical (effector, enzyme, sign, mechanism) edges and
    reports agreements, missing/extra edges, and sign/mechanism conflicts. The Maud
    source is treated as evidence (mediated by the reviewed --mapping), not merged.

    Example:
        ai-gene-review compare-module-regulation \\
            modules/methionine_cycle.yaml \\
            models/methionine/methionine_cycle.regulation.toml \\
            -m models/methionine/maud_methionine_mapping.yaml
    """
    import yaml as _yaml

    from ai_gene_review.maud_ingest import candidate_connections, maud_edges_from_files
    from ai_gene_review.regulation_compare import (
        diff_edges,
        format_edge_diff,
        module_regulatory_edges,
    )

    if not module_file.exists():
        typer.echo(f"Error: module file not found: {module_file}", err=True)
        raise typer.Exit(code=1)
    if not maud_toml.exists():
        typer.echo(f"Error: TOML file not found: {maud_toml}", err=True)
        raise typer.Exit(code=1)

    curated = module_regulatory_edges(_yaml.safe_load(module_file.read_text()))
    source = maud_edges_from_files(maud_toml, mapping)
    diff = diff_edges(curated, source)
    typer.echo(format_edge_diff(diff, module_file.name, maud_toml.name))

    if emit_candidates:
        candidates = candidate_connections(source, source_id=f"file:{maud_toml}")
        typer.echo("# candidate connections (review before adding to a module):")
        typer.echo(_yaml.safe_dump(candidates, sort_keys=False))


@app.command()
def fetch_descriptions(
    organism: Annotated[
        str, typer.Argument(help="Organism name (e.g., human, yeast)")
    ],
    gene: Annotated[
        str, typer.Argument(help="Gene symbol (e.g., CAT2, TP53)")
    ],
    output_dir: Annotated[
        Optional[Path],
        typer.Option("--output-dir", "-o", help="Output directory (default: current directory)"),
    ] = None,
):
    """Fetch gene descriptions from external sources (Alliance_Imported, Alliance_Automated, UniProt, RefSeq).

    Creates a sidecar file: genes/<organism>/<gene>/<gene>-descriptions.yaml

    Examples:
        ai-gene-review fetch-descriptions yeast CAT2
        ai-gene-review fetch-descriptions human TP53
    """
    from ai_gene_review.etl.descriptions import fetch_and_save_gene_descriptions

    typer.echo(f"Fetching descriptions for {gene} ({organism})...")
    try:
        path = fetch_and_save_gene_descriptions(organism, gene, base_path=output_dir)
        typer.echo(f"Saved to {path}")
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def fetch_descriptions_bulk(
    organism: Annotated[
        str, typer.Argument(help="Organism name (e.g., yeast, human)")
    ],
    output_dir: Annotated[
        Optional[Path],
        typer.Option("--output-dir", "-o", help="Output directory (default: current directory)"),
    ] = None,
    delay: Annotated[
        float,
        typer.Option("--delay", "-d", help="Delay between API calls in seconds"),
    ] = 0.5,
    genes: Annotated[
        Optional[List[str]],
        typer.Option("--gene", "-g", help="Specific gene(s) to fetch (default: all)"),
    ] = None,
):
    """Fetch gene descriptions for all genes in an organism directory.

    Creates per-gene sidecar files at genes/<organism>/<gene>/<gene>-descriptions.yaml

    Examples:
        ai-gene-review fetch-descriptions-bulk yeast
        ai-gene-review fetch-descriptions-bulk yeast -g CAT2 -g SSA1
    """
    from ai_gene_review.etl.descriptions import fetch_organism_descriptions

    typer.echo(f"Fetching descriptions for all {organism} genes...")
    try:
        count = fetch_organism_descriptions(
            organism, base_path=output_dir, delay=delay, gene_symbols=genes,
        )
        typer.echo(f"Fetched descriptions for {count} genes")
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def descriptions_status(
    organism: Annotated[
        str, typer.Argument(help="Organism name (e.g., yeast, human)")
    ],
    output_dir: Annotated[
        Optional[Path],
        typer.Option("--output-dir", "-o", help="Output directory (default: current directory)"),
    ] = None,
    update: Annotated[
        bool,
        typer.Option("--update", help="Write computed status back into each YAML file"),
    ] = False,
    show_all: Annotated[
        bool,
        typer.Option("--all", help="Show all genes, not just summary"),
    ] = False,
):
    """Report review status of gene description files.

    Shows how many description files are STUB, IN_PROGRESS, REVIEWED, or COMPLETE.

    Examples:
        ai-gene-review descriptions-status yeast
        ai-gene-review descriptions-status yeast --update
        ai-gene-review descriptions-status yeast --all
    """
    from ai_gene_review.etl.descriptions import compute_organism_description_status

    report = compute_organism_description_status(organism, base_path=output_dir, update=update)

    typer.echo(f"\nDescription review status for {organism} ({report.total} genes):")
    for status in ["STUB", "IN_PROGRESS", "REVIEWED", "COMPLETE"]:
        count = report.by_status.get(status, 0)
        if count > 0:
            typer.echo(f"  {status}: {count}")

    if show_all:
        typer.echo("")
        for gene in report.genes:
            typer.echo(f"  {gene['gene_symbol']}: {gene['status']}")

    if update:
        typer.echo("\nStatus fields updated in YAML files.")


@app.command()
def analyze_evidence_sources(
    organism: Annotated[
        str, typer.Option("--organism", "-o", help="Organism subdirectory under genes/")
    ] = "human",
    genes_dir: Annotated[
        Path, typer.Option("--genes-dir", help="Root genes directory")
    ] = Path("genes"),
    cache_path: Annotated[
        Path,
        typer.Option(
            "--type-cache", help="TSV cache of PMID -> PubMed publication types"
        ),
    ] = Path("publications/publication_types.tsv"),
    output_dir: Annotated[
        Path, typer.Option("--output-dir", help="Directory for the report and TSVs")
    ] = Path("reports/evidence_sources"),
    refresh: Annotated[
        bool, typer.Option("--refresh", help="Re-fetch all publication types from PubMed")
    ] = False,
    no_network: Annotated[
        bool,
        typer.Option(
            "--no-network", help="Do not query PubMed; classify only from the cache"
        ),
    ] = False,
):
    """Analyze which evidence sources support GO annotation review decisions.

    Cross-tabulates reference publication_type (review vs primary vs deep
    research, inferred from PubMed PT metadata) against the manuscript section
    of each supporting-text snippet and the curator's review action, to test
    hypotheses about whether reviews / abstracts / deep research suffice.

    Examples:
        ai-gene-review analyze-evidence-sources --organism human
        ai-gene-review analyze-evidence-sources -o human --no-network
    """
    from ai_gene_review.tools.analyze_evidence_sources import (
        analyze_evidence_sources as _run,
    )

    report_path = _run(
        organism=organism,
        genes_dir=genes_dir,
        cache_path=cache_path,
        output_dir=output_dir,
        refresh=refresh,
        network=not no_network,
    )
    typer.echo(f"Report written to {report_path}")


@app.command()
def fetch_panther_paint(
    family: Annotated[
        Optional[str],
        typer.Argument(help="PANTHER family id (e.g., PTHR10177). Omit with --all."),
    ] = None,
    all_families: Annotated[
        bool,
        typer.Option(
            "--all",
            help="Process every cached family under interpro/panther/ in a single "
            "leaf-GAF pass (skips families with no node annotations).",
        ),
    ] = False,
    output_dir: Annotated[
        Optional[Path],
        typer.Option(
            "--output-dir",
            "-o",
            help="Repo root (default: current directory). Slice is written to "
            "interpro/panther/<FAMILY>/.",
        ),
    ] = None,
    cache_dir: Annotated[
        Optional[Path],
        typer.Option(
            "--cache-dir",
            help="Where to cache the downloaded PAINT GAFs (default: <repo>/.cache/panther).",
        ),
    ] = None,
    extra_uniprot: Annotated[
        Optional[List[str]],
        typer.Option(
            "--extra-uniprot",
            help="Extra member UniProt id(s) to include when resolving nodes "
            "(repeatable). Single-family mode only.",
        ),
    ] = None,
    force_download: Annotated[
        bool,
        typer.Option("--force-download", help="Re-download source GAFs even if cached."),
    ] = False,
):
    """Fetch PANTHER PAINT (PTN node-level) annotations for a family (or --all).

    Resolves the family's PTN tree nodes (from its cached ``<FAM>-entries.csv``
    member list joined against the leaf IBA GAF), then slices the node-level
    ``IBD.gaf`` (IBD/IRD/IKR annotations) for those nodes. Writes:

        interpro/panther/<FAMILY>/<FAMILY>-paint.tsv   (one row per node annotation)

    Run ``fetch-gene`` for a member first (or otherwise populate the family's
    ``<FAMILY>-entries.csv``) so the member list is available.

    Examples:
        ai-gene-review fetch-panther-paint PTHR10177
        ai-gene-review fetch-panther-paint PTHR35730 --extra-uniprot Q67XT3
        ai-gene-review fetch-panther-paint --all
    """
    from ai_gene_review.etl.panther_paint import (
        fetch_family_paint,
        fetch_all_family_paint,
    )

    repo_root = output_dir or Path.cwd()
    cache = cache_dir or (repo_root / ".cache" / "panther")
    panther_root = repo_root / "interpro" / "panther"

    if all_families:
        if family:
            typer.echo("❌ Pass either a FAMILY or --all, not both.")
            raise typer.Exit(code=1)
        typer.echo(
            "Resolving PTN nodes for ALL cached families (single leaf-GAF pass; "
            "this downloads/caches PAINT GAFs)..."
        )
        counts = fetch_all_family_paint(
            panther_root, cache_dir=cache, force_download=force_download
        )
        total = sum(counts.values())
        typer.echo(
            f"✓ Wrote PAINT slices for {len(counts)} family/families "
            f"({total} node-level annotations total)."
        )
        return

    if not family:
        typer.echo("❌ Provide a FAMILY id or use --all.")
        raise typer.Exit(code=1)

    family_dir = panther_root / family
    entries_csv = family_dir / f"{family}-entries.csv"
    if not entries_csv.exists():
        typer.echo(
            f"❌ {entries_csv} not found. Fetch the family first "
            f"(e.g. via fetch-gene for a member of {family})."
        )
        raise typer.Exit(code=1)

    typer.echo(f"Resolving PTN nodes for {family} (this downloads/caches PAINT GAFs)...")
    tsv_path, nodes = fetch_family_paint(
        family,
        entries_csv=entries_csv,
        out_dir=family_dir,
        cache_dir=cache,
        extra_uniprot=extra_uniprot,
        force_download=force_download,
    )
    n_annotations = sum(1 for _ in tsv_path.read_text().splitlines()) - 1
    typer.echo(
        f"✓ {family}: {len(nodes)} node(s), {n_annotations} node-level annotation(s)"
    )
    typer.echo(f"  {tsv_path}")


@app.command()
def fetch_gocam(
    model_id: Annotated[
        str,
        typer.Argument(
            help="GO-CAM model id (bare, gomodel: CURIE, or model URL)"
        ),
    ],
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", help="Top-level GO-CAM cache directory"),
    ] = Path("gocams"),
    force: Annotated[
        bool,
        typer.Option("--force", "-f", help="Re-fetch even if already cached"),
    ] = False,
):
    """Fetch and cache a single GO-CAM model as gocams/<id>/<id>-src.yaml.

    The model is downloaded as low-level Minerva JSON and translated into the
    activity-centric gocam-py YAML representation.

    Examples:
        ai-gene-review fetch-gocam gomodel:568b0f9600000284
        ai-gene-review fetch-gocam 568b0f9600000284 --force
    """
    from ai_gene_review.etl.gocam import cache_gocam_model, normalize_gocam_id

    mid = normalize_gocam_id(model_id)
    out = cache_gocam_model(mid, cache_dir=cache_dir, force=force)
    typer.echo(f"✓ Cached GO-CAM {mid}: {out}")


@app.command()
def cache_gocams(
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", help="Top-level GO-CAM cache directory"),
    ] = Path("gocams"),
    force: Annotated[
        bool,
        typer.Option("--force", "-f", help="Re-fetch models already cached"),
    ] = False,
    limit: Annotated[
        Optional[int],
        typer.Option("--limit", help="Only fetch the first N models (for testing)"),
    ] = None,
    no_index: Annotated[
        bool,
        typer.Option("--no-index", help="Skip rebuilding gocams/index.tsv afterwards"),
    ] = False,
):
    """Cache all ~2k production GO-CAM models, then rebuild the gene index.

    Each model is written to gocams/<id>/<id>-src.yaml. After caching, a
    gocams/index.tsv mapping gene products to GO-CAM activities is rebuilt
    (unless --no-index is given).

    Examples:
        ai-gene-review cache-gocams
        ai-gene-review cache-gocams --limit 50
    """
    from ai_gene_review.etl.gocam import (
        build_gene_index,
        cache_all_production_models,
    )

    def progress(done: int, total: int, ok: int, failed: int) -> None:
        if done % 50 == 0 or done == total:
            typer.echo(f"  {done}/{total} (ok={ok}, failed={failed})")

    summary = cache_all_production_models(
        cache_dir=cache_dir, force=force, limit=limit, progress=progress
    )
    typer.echo(
        f"✓ Cached {summary['ok']}/{summary['total']} GO-CAM models"
        f" ({summary['failed']} failed)"
    )
    for mid, err in summary["failures"][:20]:
        typer.echo(f"  ✗ {mid}: {err}")

    if not no_index:
        index = build_gene_index(cache_dir=cache_dir)
        n_rows = len(index.read_text().strip().splitlines()) - 1
        typer.echo(f"✓ Wrote {index} ({n_rows} activity rows)")


@app.command()
def seed_gocam_review(
    model_id: Annotated[
        str,
        typer.Argument(help="GO-CAM model id (must already be cached)"),
    ],
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", help="Top-level GO-CAM cache directory"),
    ] = Path("gocams"),
    force: Annotated[
        bool,
        typer.Option("--force", "-f", help="Overwrite an existing review stub"),
    ] = False,
):
    """Seed a GoCamReview stub at gocams/<id>/<id>-review.yaml.

    One activity_reviews entry is created per cached annoton, pre-filled with the
    gene product / MF / BP / CC and PENDING assessments to be completed by a
    reviewer. Validate with:
    `uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C GoCamReview <file>`
    """
    from ai_gene_review.etl.gocam import seed_gocam_review as _seed

    out = _seed(model_id, cache_dir=cache_dir, force=force)
    typer.echo(f"✓ Seeded GO-CAM review stub: {out}")


@app.command()
def gocam_index(
    cache_dir: Annotated[
        Path,
        typer.Option("--cache-dir", help="Top-level GO-CAM cache directory"),
    ] = Path("gocams"),
):
    """Rebuild gocams/index.tsv from the cached GO-CAM models.

    Produces one row per activity (annoton): gene product, model, taxon,
    molecular function, biological process, and cellular component.
    """
    from ai_gene_review.etl.gocam import build_gene_index

    index = build_gene_index(cache_dir=cache_dir)
    n_rows = len(index.read_text().strip().splitlines()) - 1
    typer.echo(f"✓ Wrote {index} ({n_rows} activity rows)")


@app.command()
def subtraction_report(
    paths: Annotated[
        Optional[List[Path]],
        typer.Argument(
            help="Gene review YAML files or directories (default: genes/)"
        ),
    ] = None,
    reference: Annotated[
        Optional[List[str]],
        typer.Option(
            "--ref",
            "-r",
            help="Reference id(s) to subtract, e.g. GO_REF:0000033 (repeatable)",
        ),
    ] = None,
    evidence: Annotated[
        Optional[List[str]],
        typer.Option(
            "--evidence",
            "-e",
            help="Evidence code(s) to subtract, e.g. IBA (repeatable)",
        ),
    ] = None,
    mode: Annotated[
        str,
        typer.Option(
            help="When both --ref and --evidence are given: 'any' (match either) or 'all' (match both)"
        ),
    ] = "any",
    keep_only: Annotated[
        bool,
        typer.Option(
            "--keep-only",
            help="Invert: subtract everything EXCEPT the filter (e.g. --keep-only -e IBA "
            "removes all non-IBA annotations, showing what is lost if IBA were the only "
            "evidence -- i.e. where IBA is too conservative)",
        ),
    ] = False,
    output: Annotated[
        Optional[Path],
        typer.Option(
            "--output",
            "-o",
            help="Output path. For markdown a file; for tsv a prefix "
            "(writes <prefix>-lost-annotations.tsv and <prefix>-core-functions.tsv)",
        ),
    ] = None,
    output_format: Annotated[
        str,
        typer.Option("--format", "-f", help="Output format: markdown or tsv"),
    ] = "markdown",
    adapter: Annotated[
        str,
        typer.Option(help="OAK adapter for GO closure"),
    ] = "sqlite:obo:go",
    no_closure: Annotated[
        bool,
        typer.Option(
            "--no-closure",
            help="Disable ontology closure (exact-term matching only)",
        ),
    ] = False,
    max_detail_genes: Annotated[
        Optional[int],
        typer.Option(help="Limit per-gene detail in the markdown report"),
    ] = None,
):
    """Report what is lost if a REF/evidence-code is removed from reviews.

    For the chosen reference id(s) and/or evidence code(s) (e.g. IBA /
    GO_REF:0000033), simulates removing the matching annotations and reports:

    \b
    1. Endorsed (ACCEPT/KEEP_AS_NON_CORE) annotations that disappear, flagged
       UNIQUE (no survivor covers the term) or REDUNDANT (a surviving annotation
       still asserts the term or a more specific descendant).
    2. Each core_functions GO term as RETAINED (still grounded by a survivor),
       LOST (only the subtracted evidence grounded it), or UNSUPPORTED.

    Closure (is_a + part_of) is applied so a specific surviving annotation can
    ground a more general core-function term.

    Use --keep-only to invert the scenario: subtract everything EXCEPT the
    filter. ``--keep-only -e IBA`` removes all non-IBA annotations, so LOST
    core_functions are the biology that IBA alone would miss (IBA too
    conservative).

    Examples:

    \b
        ai-gene-review subtraction-report -e IBA
        ai-gene-review subtraction-report -r GO_REF:0000033 -o reports/iba --format tsv
        ai-gene-review subtraction-report genes/human -e IBA -e ISS
        ai-gene-review subtraction-report genes/human --keep-only -e IBA
    """
    from ai_gene_review.analysis.subtraction_report import (
        SubtractionFilter,
        SubtractionReporter,
        iter_review_files,
        make_go_ancestor_fn,
        render_markdown,
        summarize,
        write_tsv_reports,
    )

    if not reference and not evidence:
        typer.echo(
            "Error: provide at least one --ref or --evidence to subtract.", err=True
        )
        raise typer.Exit(code=1)

    filt = SubtractionFilter.create(
        reference_ids=reference or [],
        evidence_codes=evidence or [],
        mode=mode,
        complement=keep_only,
    )

    search_paths = paths if paths else [Path("genes")]
    files = iter_review_files(search_paths)
    if not files:
        typer.echo("Error: no *-ai-review.yaml files found.", err=True)
        raise typer.Exit(code=1)
    typer.echo(f"Analyzing {len(files)} review files (filter: {filt.describe()})...", err=True)

    if no_closure:
        reporter = SubtractionReporter()
    else:
        reporter = SubtractionReporter(ancestors=make_go_ancestor_fn(adapter))

    results = reporter.analyze_files(files, filt)

    if output_format == "tsv":
        prefix = output if output else Path("reports/subtraction")
        lost_path, cf_path = write_tsv_reports(results, prefix)
        typer.echo(f"✓ Wrote {lost_path}")
        typer.echo(f"✓ Wrote {cf_path}")
    elif output_format == "markdown":
        md = render_markdown(results, filt, max_detail_genes=max_detail_genes)
        if output:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(md)
            typer.echo(f"✓ Wrote {output}")
        else:
            typer.echo(md)
    else:
        typer.echo(f"Error: unknown format {output_format!r}", err=True)
        raise typer.Exit(code=1)

    summary = summarize(results, filt)
    sc = summary["core_function_status_counts"]
    typer.echo(
        f"Summary: {summary['n_subtracted_annotations']} annotations subtracted; "
        f"{summary['n_lost_endorsed']} endorsed lost "
        f"({summary['n_lost_endorsed_unique']} unique); "
        f"core_functions terms RETAINED {sc['RETAINED']} / LOST {sc['LOST']} / "
        f"UNSUPPORTED {sc['UNSUPPORTED']}",
        err=True,
    )


def main():
    """Main entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
